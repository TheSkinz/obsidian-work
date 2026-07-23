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
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
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
        "Smart Pig | Rig-Out | Stand-By | Total | Heater footage (ft) | "
        "ft / elapsed pig-hr | ft/hr per pig (norm) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    if not actual_rows:
        lines.append("| _no actuals recorded yet_ | | | | | | | | | | | | | | | |")
    for tag, client, r, footage, fthr, norm in actual_rows:
        foot_s = f"{footage:,.0f}" if footage else "(not recorded)"
        fthr_s = f"{fthr:.0f}" if fthr else "-"
        norm_s = f"{norm:.0f}" if norm else "-"
        mode_s = r[11].strip() or "?"
        cond = r[10].strip() or "unknown"
        lines.append(
            f"| {tag} | {client} | {r[0]} | {r[1]} | {cond} | {r[2]} | {mode_s} | {r[3]} | "
            f"{r[4]} | {r[5]} | {r[7]} | {r[8]} | {r[9]} | {foot_s} | {fthr_s} | {norm_s} |")

    # Condition segmentation — crash and routine rows must never be averaged together.
    # Segment on the mode-normalized per-pig rate so different modes are comparable.
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
    lines += ["", "## ft/hr per pig by coil condition", ""]
    lines += [
        "Mode-normalized per-pig rates (elapsed ÷ Mode), so jobs run in different modes "
        "compare on one basis. A decoke's hours are evidence only for the next decoke of the "
        "**same condition**. A crashed furnace runs significantly dirtier than routine "
        "service fouling, so crash rows must not be used to estimate a routine clean (or "
        "vice versa). Classification rule: job details saying \"emergency\" mean `crash` "
        "(Jesse, 2026-07-19).",
        "",
        "| Condition | Rows w/ norm rate | Range (ft/hr per pig) | Mean |",
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
        "- Rig-In/Rig-Out actuals well off the "
        f"{BENCH_RIG_IN:.0f}/{BENCH_RIG_OUT:.0f} hr defaults, or ft/hr consistently off "
        f"{BENCH_FT_PER_HR:.0f}, are the signal to revisit the Duration Model — raise it "
        "with Jesse rather than editing the skill from here.",
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
