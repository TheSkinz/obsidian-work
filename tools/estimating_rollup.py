#!/usr/bin/env python3
"""estimating_rollup.py — aggregate Task Durations actuals across all heater
cards into 04-knowledge/estimating-actuals-rollup.md.

This is the vault's return path for job data: every completed job's actuals,
side by side with the estimating benchmarks (100 ft/hr pigging, 6 hr rig-in,
6 hr rig-out), so estimates calibrate against reality as the dataset grows.

REFERENCE ONLY — this report never changes a rate or a skill value. Estimating
benchmark changes are Lane 4: Jesse decides, then usadebusk-estimating is
edited in the config repo.

Pure standard library. Writes a GENERATED file.

Usage:
    python tools/estimating_rollup.py           write the rollup
    python tools/estimating_rollup.py --print   also print to stdout

Windows: `py -3 tools/estimating_rollup.py`.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

OUT_REL = "04-knowledge/estimating-actuals-rollup.md"
FACILITIES = "02-facilities"

# Benchmarks as currently stated in usadebusk-estimating (Duration Model).
BENCH_FT_PER_HR = 100.0
BENCH_RIG_IN = 6.0
BENCH_RIG_OUT = 6.0

TD_COLS = ["Date", "Job #", "Rigs", "Rig-In", "Pig", "Smart Pig",
           "Rig-Over", "Rig-Out", "Stand-By", "Total", "Condition", "Mode"]


def parse_frontmatter(text: str) -> dict[str, str]:
    fm: dict[str, str] = {}
    lines = text.splitlines()
    # Leading blank lines and full-line HTML comments precede the fence on
    # loop-marked notes; see frontmatter_start() in vault_lint.py.
    start = None
    for i, line in enumerate(lines):
        s = line.strip()
        if not s or (s.startswith("<!--") and s.endswith("-->")):
            continue
        start = i if s == "---" else None
        break
    if start is None:
        return fm
    for line in lines[start + 1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip().strip("'\"")
    return fm


def section_lines(text: str, heading: str) -> list[str]:
    """Lines of the section starting at `## {heading}` up to the next ## heading."""
    out: list[str] = []
    in_section = False
    for line in text.splitlines():
        if re.match(rf"^##\s+.*{re.escape(heading)}", line):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            out.append(line)
    return out


def table_rows(lines: list[str]) -> list[list[str]]:
    """Data rows of the first markdown table in `lines` (header + separator skipped)."""
    rows: list[list[str]] = []
    seen_header = False
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not seen_header:
            seen_header = True  # header row
            continue
        if all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells):
            continue  # separator row
        if any(c for c in cells):
            rows.append(cells)
    return rows


def num(cell: str | None) -> float | None:
    """Tolerant numeric parse: '~385.8' -> 385.8; '?', '-', '(not verified)' -> None."""
    if cell is None:
        return None
    s = cell.strip().lstrip("~").replace(",", "")
    m = re.match(r"^-?\d+(\.\d+)?", s)
    return float(m.group(0)) if m else None


def rig_method(r: list[str]) -> str:
    """What KIND of number this row's rig columns hold (DQ-017 Q3).

    The Rig-In column is known mixed-method: a cell may be a clean single-rig
    elapsed measurement, a sum across rigs, a two-heater job total, several
    tasks collapsed into one figure, or a number from a job whose own sources
    disagree. Printed side by side they read as one series, and fitting a
    duration rule to that series is how a defect becomes a rule.

    DELIBERATELY CONSERVATIVE. The default is `unmarked`, NOT `clean` — it
    means no method problem is *recorded*, not that the figure was verified.
    HF-0011 is why: its Rig-Out of 3 is the BILLED figure, with a further 8 hrs
    customer-signed and never billed, and no token on that row says so. A
    positive `clean` claim would have swept that row into a rule.

    Only `combined-heaters`, multi-rig `hours-blended`, and `rig-quarantined`
    are mechanically decidable. The `*` glyph is NOT: it marks "the card
    footnotes this cell" and means different things on different rows —
    bundled rig-in+over+out at Valero, an absent-by-design side of a rig-over
    pair at Flint Hills. So it resolves to `see card` rather than a guess.
    """
    cond = r[10].lower()
    if "rig-quarantined" in cond:
        return "quarantined"
    # `*` on a rig cell: the card carries a footnote. Reasons differ per row and
    # are not machine-readable — do not collapse them into one label.
    if any("*" in r[i] for i in (3, 6, 7)):
        return "see card"
    if "combined-heaters" in cond:
        return "combined"
    if "hours-blended" in cond:
        rigs = num(r[2])
        # Multi-rig blended rows SUM across rigs rather than measuring elapsed
        # (7-1 F-1 CND25004: rig-in 14 = 6 + 6 + 2 over three coil sets).
        return "2-rig-sum" if rigs and rigs > 1 else "blended"
    return "unmarked"


def heater_cards(root: Path):
    for p in sorted((root / FACILITIES).rglob("*.md")):
        if p.name.startswith("_"):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fm = parse_frontmatter(text)
        if fm.get("type") == "heater":
            yield p, fm, text


def heater_total_footage(text: str) -> float | None:
    """Sum the numeric Total Length values of 'Heater total' rows in Config Rollup."""
    total = 0.0
    found = False
    for row in table_rows(section_lines(text, "Config Rollup")):
        if row and row[0].strip().lower() == "heater total" and len(row) >= 5:
            v = num(row[4])
            if v is not None:
                total += v
                found = True
    return total if found else None


def build(root: Path) -> str:
    actual_rows = []
    gaps = []
    for path, fm, text in heater_cards(root):
        tag = fm.get("heater-tag") or path.stem
        client = fm.get("client", "?")
        footage = heater_total_footage(text)
        rows = table_rows(section_lines(text, "Task Durations"))
        if not rows:
            gaps.append(f"{tag} ({client}) — no Task Durations actuals yet")
            continue
        for r in rows:
            r = (r + [""] * len(TD_COLS))[:len(TD_COLS)]
            pig = num(r[4])
            mode = num(r[11])
            fthr = None
            norm = None
            # A combined-heaters row carries the whole job's hours on every heater it
            # touched; dividing one heater's footage by them understates the rate.
            combined = "combined-heaters" in r[10].lower()
            if pig and footage and not combined:
                fthr = footage / pig
                # Mode = passes pigged simultaneously; dividing the elapsed rate by it
                # approximates the single-pig travel rate comparable to the benchmark.
                if mode and mode > 0:
                    norm = fthr / mode
            actual_rows.append((tag, client, r, footage, fthr, norm))

    lines = [
        "<!-- GENERATED by tools/estimating_rollup.py - do not edit; rerun to refresh. -->",
        "# Estimating Actuals Rollup",
        f"**Generated:** {date.today().isoformat()} — all Task Durations actuals across "
        "heater cards, against the estimating benchmarks. Reference only: benchmark or "
        "rate changes are Lane 4 (Jesse decides; `usadebusk-estimating` is then edited "
        "in the config repo).",
        "",
        f"Benchmarks as stated in `usadebusk-estimating`: **{BENCH_FT_PER_HR:.0f} ft/hr** "
        f"pigging (nominal fouling), **{BENCH_RIG_IN:.0f} hr** rig-in / "
        f"**{BENCH_RIG_OUT:.0f} hr** rig-out proposal defaults.",
        "",
        "> Interpretation caution: task hours are ELAPSED wall-clock (per the canonical "
        "card schema). `ft / elapsed pig-hr` divides heater-total footage by elapsed Pig "
        "hours and reads high on double/triple-mode jobs, where several passes are pigged "
        "at once. `ft/hr per pig (norm)` divides that by `Mode` (passes pigged "
        "simultaneously) to approximate a single-pig travel rate comparable to the "
        f"{BENCH_FT_PER_HR:.0f} ft/hr benchmark. A `-` means the figure is undefined (no "
        "footage, combined-heaters, or — normalized column — no Mode recorded); the "
        "approximation is exact when the pass count divides evenly into sets of Mode.",
        "",
        "## Actuals",
        "",
        "| Heater | Client | Date | Job # | Condition | Rigs | Mode | Rig-In | Pig | "
        "Smart Pig | Rig-Out | Rig method | Stand-By | Total | Heater footage (ft) | "
        "ft / elapsed pig-hr | ft/hr per pig (norm) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    if not actual_rows:
        lines.append("| _no actuals recorded yet_ | | | | | | | | | | | | | | | | |")
    for tag, client, r, footage, fthr, norm in actual_rows:
        foot_s = f"{footage:,.0f}" if footage else "(not recorded)"
        fthr_s = f"{fthr:.0f}" if fthr else "-"
        norm_s = f"{norm:.0f}" if norm else "-"
        mode_s = r[11].strip() or "?"
        cond = r[10].strip() or "unknown"
        lines.append(
            f"| {tag} | {client} | {r[0]} | {r[1]} | {cond} | {r[2]} | {mode_s} | {r[3]} | "
            f"{r[4]} | {r[5]} | {r[7]} | {rig_method(r)} | {r[8]} | {r[9]} | {foot_s} | "
            f"{fthr_s} | {norm_s} |")

    lines += [
        "",
        "> **`Rig method` — read this before comparing any two rig figures** (DQ-017 Q3). "
        "The Rig-In and Rig-Out columns are **mixed-method**: cells that print alike were "
        "produced five different ways, and a rule fitted across them inherits the defect. "
        "`unmarked` = no method problem is *recorded* — **not** a verified measurement; "
        "HF-0011's Rig-Out of 3 is the billed figure with a further 8 hrs customer-signed "
        "and never billed, and nothing on that row says so. `combined` = the hours are a "
        "multi-heater job total written on each card. `2-rig-sum` = summed across rigs, not "
        "elapsed (7-1 F-1 CND25004's rig-in 14 = 6 + 6 + 2 across three coil sets). "
        "`blended` = the source did not separate this row's tasks cleanly; the card says "
        "which. `see card` = the cell carries a `*` footnote, and the reasons genuinely "
        "differ — Valero bundles rig-in + rig-over + rig-out into one \"Rigging\" figure, "
        "while the Flint Hills pair is one continuous rig-over where each heater's missing "
        "side is absent by design. `quarantined` = the job's own sources do not reconcile "
        "(both HF Sinclair heaters, USA25051/USA26038 — see their card row notes). "
        "**Only `unmarked` rows are candidates for deriving anything, and they are "
        "candidates, not evidence.**",
    ]

    # `unmarked` alone is not the derivable set: a row can be unmarked and still be
    # missing one of the two figures (HP-0007 records no Rig-In). Count the pairs.
    unmarked = [x for x in actual_rows if rig_method(x[2]) == "unmarked"]
    pairs = [x for x in unmarked if num(x[2][3]) is not None and num(x[2][7]) is not None]
    lines += [
        "",
        f"> **{len(pairs)} of {len(actual_rows)} rows carry a rig-in/rig-out pair that is "
        f"both `unmarked` and complete** ({len(unmarked)} rows are `unmarked`, but not all "
        "record both figures). That is the whole population available for any question "
        "about how rig-out relates to rig-in — small enough that a difference between a "
        "handful of jobs will look like a difference between facilities. Count the "
        "distinct **jobs** behind these rows before reading a pattern into them.",
    ]

    # Job-class segmentation — crash and routine rows must never be averaged together.
    # Segment on the mode-normalized per-pig rate so different modes are comparable.
    # `crash` is a CALLOUT label (unscheduled mobilization), not a fouling grade
    # (Jesse, 2026-08-20 / DQ-026) — the segmentation is by job class, not coil state.
    by_cond: dict[str, list[float]] = {}
    unnormalized = 0
    for tag, client, r, footage, fthr, norm in actual_rows:
        if fthr is None:
            continue
        if norm is None:
            unnormalized += 1
            continue
        key = (r[10].strip() or "unknown").split(",")[0].strip().lower()
        by_cond.setdefault(key, []).append(norm)
    lines += ["", "## ft/hr per pig by job class", ""]
    lines += [
        "Mode-normalized per-pig rates (elapsed ÷ Mode), so jobs run in different modes "
        "compare on one basis. A decoke's hours are evidence only for the next decoke of the "
        "**same job class**, so crash rows must not be used to estimate a routine clean (or "
        "vice versa). Classification rule: job details saying \"emergency\" mean `crash` "
        "(Jesse, 2026-07-19).",
        "",
        "> **What `crash` means, and what this gap is not** (Jesse, 2026-08-20 / DQ-026). "
        "`crash` labels an **unscheduled mobilization** — the facility hit operational trouble "
        "and needed a crew on a moment's notice. It is a callout label, not a fouling grade: "
        "the coil is usually dirty, but not by definition, and nothing in this table measures "
        "how dirty. **Do not read the crash-vs-routine gap as a coke measurement.** It is also "
        "confounded — four of the six crash rows are multi-mode (2–3) large vacuum heaters, so "
        "the ÷Mode normalization is doing work that a fouling reading would wrongly credit to "
        "coke. The crash mean is still the right basis for pricing an **emergency quote**, "
        "because emergency jobs are what carry whatever the gap actually reflects — schedule "
        "pressure, unfamiliar heater, night work, fouling, or all of it. It is the wrong basis "
        "for a planned clean, and the wrong evidence for any claim about coil condition.",
        "",
        "| Job class | Rows w/ norm rate | Range (ft/hr per pig) | Mean |",
        "|---|---|---|---|",
    ]
    if not by_cond:
        lines.append("| _none_ | 0 | - | - |")
    for key in sorted(by_cond):
        vals = by_cond[key]
        rng = f"{min(vals):.0f}–{max(vals):.0f}" if len(vals) > 1 else f"{vals[0]:.0f}"
        lines.append(
            f"| {key} | {len(vals)} | {rng} | {sum(vals) / len(vals):.0f} |")
    if unnormalized:
        lines += [
            "",
            f"> {unnormalized} row(s) carry an elapsed rate but no `Mode`, so they are "
            "excluded from these per-pig means — add `Mode` to those Task Durations rows "
            "to include them.",
        ]
    if "routine" not in by_cond:
        lines += [
            "",
            "> ⚠ **No routine-condition actuals carry a ft/hr figure.** Every usable rate "
            f"above comes from a non-routine job, so the {BENCH_FT_PER_HR:.0f} ft/hr "
            "benchmark currently has zero routine actuals either supporting or "
            "contradicting it. Do not read a low crash rate as evidence the benchmark is "
            "too high.",
        ]
    lines += [
        "",
        "## Coverage gaps",
        "",
    ]
    lines += [f"- {g}" for g in gaps] or ["- none — every card carries actuals"]
    lines += [
        "",
        "## Reading this",
        "",
        f"- With **{len(actual_rows)}** actual job row(s), this is a growing dataset, not a "
        "calibrated model. Treat per-job ft/hr as anecdotes until several same-service "
        "jobs accumulate.",
        "- **Check the per-coilset spread before deriving a rate from any row** (Jesse, "
        "2026-08-20 / DQ-027). Coils on one heater clean within a few hours of each other; a "
        "coil set 12–24 hrs off its siblings means a problem specific to that coil that decoke, "
        "or corrupt data. Derive off the sets that cluster, never the outlier, and say in the "
        "duration math that you excluded it. Rows here are per-job heater totals, so the spread "
        "is not visible from this table — go to the card's Field Notes / job report.",
        "- **Rig-In/Rig-Out actuals well off the "
        f"{BENCH_RIG_IN:.0f}/{BENCH_RIG_OUT:.0f} hr defaults are a signal only on "
        "`unmarked` rows** — check the `Rig method` column first. A `combined`, "
        "`2-rig-sum`, `blended`, `see card` or `quarantined` row is far off the default "
        "because of how the number was produced, not because the job ran long, and "
        "reading it as a duration signal is the specific error this column exists to "
        "prevent. ft/hr consistently off "
        f"{BENCH_FT_PER_HR:.0f} is the other signal. Either way, raise it with Jesse "
        "rather than editing the skill from here.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("--print", action="store_true", dest="do_print")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()
    if not (root / "CLAUDE.md").exists():
        print(f"ERROR: {root} does not look like the vault root (no CLAUDE.md).")
        return 1

    content = build(root)
    out = root / OUT_REL
    out.write_text(content, encoding="utf-8")
    print(f"Wrote {out}")
    if args.do_print:
        print("\n" + content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
