#!/usr/bin/env python3
"""pig_usage_rollup.py — aggregate Pig Specifications actuals across all heater
cards into 04-knowledge/pig-usage-rollup.md.

Sibling to estimating_rollup.py, same pattern and same contract: read one named
section off every heater card, aggregate, emit a GENERATED reference page.
Where that script answers "how long did it take", this one answers "how many
pigs did it eat, at what bore, over how much footage".

REFERENCE ONLY — this report never changes a rate, a quantity method, or a
skill value. Pig-quantity method changes are Lane 4 (Jesse decides; then
usadebusk-estimating is edited in the config repo).

Deliberately NOT computed here (Jesse, 2026-07-26): any pooled or modelled
ft-per-pig rate by bore and condition. This build shows raw counts and the
per-job arithmetic only, so the shape of the data is visible before anyone
fits a number to it. Most bore x condition cells hold 1-3 points; a raw
per-cell mean would mislead and a shrinkage estimate is a separate decision.

Pure standard library. Writes a GENERATED file.

Usage:
    python tools/pig_usage_rollup.py           write the rollup
    python tools/pig_usage_rollup.py --print   also print to stdout

Windows: `py -3 tools/pig_usage_rollup.py`.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from estimating_rollup import (
    heater_cards,
    heater_total_footage,
    num,
    section_lines,
    table_rows,
)

OUT_REL = "04-knowledge/pig-usage-rollup.md"

PS_COLS = ["Size", "Type", "Qty", "Unit Cost", "Billed As", "Source"]

# Largest OD that can plausibly be a pig. Above this the Size cell is carrying
# some other measurement (tool length on Honeycomb rows, for example).
MAX_PLAUSIBLE_PIG_OD = 20.0

JOB_RE = re.compile(r"\b(USA\d{5}|CND\d{5})\b")
QUOTE_RE = re.compile(r"\bDSP\d{4,5}", re.IGNORECASE)


def job_number(source: str) -> str | None:
    """The USA#####/CND##### that sources an actual row. None if not an actual."""
    m = JOB_RE.search(source or "")
    return m.group(1) if m else None


def size_value(cell: str) -> float | None:
    """Single nominal pig size in inches, or None for ranges and 'Mixed' cells.

    Real cards carry `5.5 in`, `6.0 in`, `3.0"-4.1"` and
    `Mixed 2"-8" (see Field Notes ...)`. Only the single-size form can be
    totalled by size; the rest stay in the per-job totals but are excluded
    from any size breakdown rather than being silently collapsed to one end
    of their range.
    """
    s = (cell or "").strip()
    if not s:
        return None
    if re.search(r"mixed|various", s, re.IGNORECASE):
        return None
    # A range: two numbers joined by a dash/en-dash, optionally quoted.
    if re.search(r"\d\s*[-–—]\s*\d", s):
        return None
    v = num(s)
    # Sanity ceiling. Some rows carry a figure that is not a bore at all — the
    # Honeycomb rows on H-19/H-20 read 76", 84", 104", which are tool lengths,
    # not diameters. Nothing in the vault runs a pig above ~20" OD, so anything
    # larger is a different measurement wearing the Size column. Excluded from
    # size totals and reported under Data quality rather than silently listed
    # alongside real pig sizes.
    if v is not None and v > MAX_PLAUSIBLE_PIG_OD:
        return None
    return v


def governing_bore(text: str) -> float | None:
    """Smallest tube ID across all Tube Geometry rows — what pig sizing keys off."""
    ids: list[float] = []
    for row in table_rows(section_lines(text, "Tube Geometry")):
        if len(row) >= 7:
            v = num(row[6])
            if v:
                ids.append(v)
    return min(ids) if ids else None


def conditions_by_job(text: str) -> dict[str, str]:
    """Map Job # -> Condition from this card's Task Durations table.

    Pig Specifications has no Condition column of its own — adding one is a
    Lane 4 card-schema change parked in idea-pig-actuals-maturation. Joining
    on Job # gets the same segmentation for free and without touching the
    schema, for any job that also carries a durations row.
    """
    out: dict[str, str] = {}
    for row in table_rows(section_lines(text, "Task Durations")):
        if len(row) >= 11:
            job = (row[1] or "").strip()
            cond = (row[10] or "").strip()
            if job and cond:
                out[job] = cond
    return out


def build(root: Path) -> str:
    actuals: list[dict] = []          # one entry per actual pig row
    quoted = 0
    unsourced = 0
    gaps: list[str] = []
    unparsed_size: list[str] = []
    implausible_size: list[str] = []

    for path, fm, text in heater_cards(root):
        tag = fm.get("heater-tag") or path.stem
        client = fm.get("client", "?")
        rows = table_rows(section_lines(text, "Pig Specifications"))
        if not rows:
            gaps.append(f"{tag} ({client}) — no Pig Specifications rows yet")
            continue
        footage = heater_total_footage(text)
        bore = governing_bore(text)
        conds = conditions_by_job(text)
        saw_actual = False
        for r in rows:
            r = (r + [""] * len(PS_COLS))[:len(PS_COLS)]
            size_s, type_s, qty_s, _cost, _billed, source = r
            job = job_number(source)
            if job is None:
                if QUOTE_RE.search(source):
                    quoted += 1
                else:
                    unsourced += 1
                continue
            saw_actual = True
            qty = num(qty_s)
            sv = size_value(size_s)
            if sv is None and size_s.strip():
                raw = num(size_s)
                if raw is not None and raw > MAX_PLAUSIBLE_PIG_OD:
                    implausible_size.append(f"{tag} ({type_s.strip() or '?'}): `{size_s.strip()}`")
                else:
                    unparsed_size.append(f"{tag}: `{size_s.strip()}`")
            # A combined-heaters total is the whole job's count repeated on every
            # card it touched. Summing those across cards multiplies the job's real
            # pig consumption by its heater count, so they are flagged and excluded
            # from every total rather than double-counted.
            combined = bool(re.search(r"combined", f"{source} {qty_s}", re.IGNORECASE))
            actuals.append({
                "tag": tag, "client": client, "job": job,
                "size_s": size_s.strip() or "(not recorded)", "size": sv,
                "type": type_s.strip() or "?",
                "qty_s": qty_s.strip() or "?", "qty": qty,
                "approx": "~" in qty_s,
                "combined": combined,
                "bore": bore, "footage": footage,
                "cond": conds.get(job, "unknown"),
            })
        if not saw_actual:
            gaps.append(f"{tag} ({client}) — Pig Specifications rows present but none "
                        "sourced to a USA#####/CND##### job (quoted or unsourced)")

    cards_with = len({a["tag"] for a in actuals})
    jobs = sorted({a["job"] for a in actuals})

    L = [
        "<!-- GENERATED by tools/pig_usage_rollup.py - do not edit; rerun to refresh. -->",
        "# Pig Usage Rollup",
        f"**Generated:** {date.today().isoformat()} — every `## Pig Specifications` row "
        "across all heater cards that is sourced to a real job, with the heater's "
        "governing bore and total footage alongside. Reference only: pig-quantity method "
        "changes are Lane 4 (Jesse decides; `usadebusk-estimating` is then edited in the "
        "config repo).",
        "",
        "> **The actuals wall is the `Source` column.** A row sourced to a `USA#####` or "
        "`CND#####` is what a job really consumed and is counted here. A row sourced to a "
        "`DSP#####` is a quoted figure and is excluded — quoted and actual pig counts must "
        "never be summed together. Rows with neither are excluded and reported as a gap.",
        "",
        "> **No ft-per-pig rate is computed.** Per-job `ft / pig` below is plain division "
        "shown per row so you can see it, not a model. A pooled rate by bore and condition "
        "was deliberately not built (Jesse, 2026-07-26): most bore×condition cells hold "
        "one to three points, where a raw per-cell mean misleads. Deciding whether a "
        "shrinkage estimate is worth it is a separate call — see "
        "[[idea-pig-actuals-maturation]].",
        "",
        f"**Coverage:** {len(actuals)} actual pig row(s) across {cards_with} heater card(s) "
        f"and {len(jobs)} job(s) — {', '.join(jobs) if jobs else 'none'}. "
        f"Excluded: {quoted} quoted (DSP-sourced) row(s), {unsourced} unsourced row(s).",
        "",
        "## Actual pig rows",
        "",
        "| Heater | Client | Job # | Condition | Pig size | Type | Qty | Governing bore (in) "
        "| Heater footage (ft) | ft / pig |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    if not actuals:
        L.append("| _no job-sourced pig rows yet_ | | | | | | | | | |")
    for a in sorted(actuals, key=lambda x: (x["client"], x["tag"], x["size"] or 0)):
        bore_s = f"{a['bore']:.3f}" if a["bore"] else "(not recorded)"
        foot_s = f"{a['footage']:,.0f}" if a["footage"] else "(not recorded)"
        if a["combined"]:
            ftpig = "– (combined)"
        elif a["qty"] and a["footage"]:
            ftpig = f"{a['footage'] / a['qty']:,.0f}"
        else:
            ftpig = "-"
        qty_s = a["qty_s"] + (" ⚠" if a["combined"] else "")
        L.append(f"| {a['tag']} | {a['client']} | {a['job']} | {a['cond']} | {a['size_s']} | "
                 f"{a['type']} | {qty_s} | {bore_s} | {foot_s} | {ftpig} |")

    # ---- totals by pig size (single-size rows only) -------------------------
    by_size: dict[float, list[dict]] = {}
    for a in actuals:
        if a["size"] is not None and a["qty"] and not a["combined"]:
            by_size.setdefault(a["size"], []).append(a)
    L += [
        "", "## Totals by pig size", "",
        "Single-size rows only. Rows carrying a size *range* (`3.0\"–4.1\"`) or `Mixed` "
        "cannot be attributed to one size and are excluded here — they still appear above "
        "and in the per-job totals. Combined-heaters rows are excluded everywhere.",
        "",
        "| Pig size (in) | Total qty | Rows | Jobs | Heaters |",
        "|---|---|---|---|---|",
    ]
    if not by_size:
        L.append("| _none parseable_ | | | | |")
    for size in sorted(by_size):
        g = by_size[size]
        tot = sum(a["qty"] for a in g if a["qty"])
        approx = any(a["approx"] for a in g)
        L.append(f"| {size:g} | {tot:,.0f}{' (approx)' if approx else ''} | {len(g)} | "
                 f"{len({a['job'] for a in g})} | {len({a['tag'] for a in g})} |")

    # ---- per job x heater -----------------------------------------------------
    by_jh: dict[tuple[str, str], list[dict]] = {}
    for a in actuals:
        by_jh.setdefault((a["job"], a["tag"]), []).append(a)
    L += [
        "", "## Per job and heater", "",
        "The line an estimate would actually scale off: total pigs consumed on one heater "
        "for one job, against that heater's footage and bore. A `combined` flag means the "
        "job report gave one pig total across several heaters and it is repeated on each "
        "card — that figure is not divisible by heater and its `ft / pig` is meaningless, "
        "so it is shown but never totalled.",
        "",
        "> **`combined-heaters` in the Condition column is a different flag** and does not "
        "invalidate the pig figures. It is inherited from the card's Task Durations row, "
        "where it means the *hours* were a multi-heater job total. Pig counts carry their "
        "own combined marker in the `Source` column, and only that one suppresses `ft / "
        "pig` here. A row can honestly show blended hours and per-heater pig counts.",
        "",
        "| Job # | Heater | Client | Condition | Governing bore (in) | Footage (ft) | "
        "Total pigs | ft / pig |",
        "|---|---|---|---|---|---|---|---|",
    ]
    if not by_jh:
        L.append("| _none_ | | | | | | | |")
    for (job, tag) in sorted(by_jh):
        g = by_jh[(job, tag)]
        a0 = g[0]
        combined = any(a["combined"] for a in g)
        qtys = [a["qty"] for a in g if a["qty"] and not a["combined"]]
        tot = sum(qtys) if qtys else None
        approx = any(a["approx"] for a in g)
        bore_s = f"{a0['bore']:.3f}" if a0["bore"] else "(not recorded)"
        foot_s = f"{a0['footage']:,.0f}" if a0["footage"] else "(not recorded)"
        if combined:
            tot_s = (g[0]["qty_s"] + " ⚠ combined") if len(g) == 1 else "⚠ combined"
            ftpig = "–"
        elif tot:
            tot_s = f"{tot:,.0f}{' (approx)' if approx else ''}"
            ftpig = f"{a0['footage'] / tot:,.0f}" if a0["footage"] else "-"
        else:
            tot_s, ftpig = "?", "-"
        L.append(f"| {job} | {tag} | {a0['client']} | {a0['cond']} | {bore_s} | {foot_s} | "
                 f"{tot_s} | {ftpig} |")

    # ---- spread by bore and by condition, counts only ---------------------------
    by_bore: dict[float, list[float]] = {}
    by_cond: dict[str, list[tuple[str, str, float]]] = {}
    for (job, tag), g in by_jh.items():
        a0 = g[0]
        if any(a["combined"] for a in g) or not a0["bore"] or not a0["footage"]:
            continue
        qtys = [a["qty"] for a in g if a["qty"]]
        if not qtys:
            continue
        rate = a0["footage"] / sum(qtys)
        by_bore.setdefault(round(a0["bore"], 3), []).append(rate)
        # Condition key: the leading token only. ", hours-blended" and
        # ", combined-heaters" are hours-side qualifiers and do not change the
        # coil state the pig count is evidence for.
        ckey = (a0["cond"] or "unknown").split(",")[0].strip().lower() or "unknown"
        by_cond.setdefault(ckey, []).append((job, tag, rate))
    L += [
        "", "## ft / pig spread by governing bore", "",
        "Counts and range only — **no mean, no fitted rate.** With this many points per "
        "cell the spread is the honest summary; a central figure would imply a precision "
        "the dataset does not carry. Read it to see whether a bore effect is even visible "
        "before anyone models one.",
        "",
        "| Governing bore (in) | Job×heater points | ft / pig range |",
        "|---|---|---|",
    ]
    if not by_bore:
        L.append("| _none_ | 0 | - |")
    for bore in sorted(by_bore):
        v = by_bore[bore]
        rng = f"{min(v):,.0f}–{max(v):,.0f}" if len(v) > 1 else f"{v[0]:,.0f}"
        L.append(f"| {bore:g} | {len(v)} | {rng} |")

    L += [
        "", "## ft / pig spread by coil condition", "",
        "Same treatment, segmented the other way. Condition qualifiers "
        "(`, hours-blended`, `, combined-heaters`) are stripped — they describe how the "
        "*hours* were recorded, not the coil state. A lower ft/pig means more pigs "
        "consumed per foot of coil.",
        "",
        "| Condition | Job×heater points | ft / pig range | Heaters |",
        "|---|---|---|---|",
    ]
    if not by_cond:
        L.append("| _none_ | 0 | - | - |")
    for ckey in sorted(by_cond):
        v = [r for _, _, r in by_cond[ckey]]
        rng = f"{min(v):,.0f}–{max(v):,.0f}" if len(v) > 1 else f"{v[0]:,.0f}"
        who = ", ".join(sorted(t for _, t, _ in by_cond[ckey]))
        L.append(f"| {ckey} | {len(v)} | {rng} | {who} |")

    # ---- data quality ----------------------------------------------------------
    L += ["", "## Data quality", ""]
    if unparsed_size:
        L += [
            f"**{len(unparsed_size)} row(s) carry a size that is a range or `Mixed`,** so "
            "they cannot join the size breakdown. Not an error — a job report that reports "
            "a size band is reporting what it has. Listed so the limit is visible:",
            "",
        ] + [f"- {u}" for u in sorted(set(unparsed_size))] + [""]
    if implausible_size:
        L += [
            f"**{len(set(implausible_size))} row(s) carry a Size above "
            f"{MAX_PLAUSIBLE_PIG_OD:.0f}\", which is not a pig OD.** All are Honeycomb "
            "tools, so the cell is almost certainly recording tool *length* rather than "
            "diameter. Excluded from the size breakdown — but the quantities are real and "
            "still count toward the per-job totals. Worth correcting on the cards, or "
            "giving Honeycomb its own unit, next time one is open:",
            "",
        ] + [f"- {u}" for u in sorted(set(implausible_size))] + [""]
    if quoted or unsourced:
        L += [
            f"**Excluded rows:** {quoted} sourced to a DSP# (quoted, not actual), "
            f"{unsourced} with no recoverable source. An unsourced quantity cannot be "
            "told apart from a quoted one, which is why the schema requires the number "
            "that sources it.",
            "",
        ]
    L += ["## Coverage gaps", ""]
    L += [f"- {g}" for g in gaps] or ["- none — every card carries job-sourced pig rows"]
    L += [
        "",
        "## Reading this",
        "",
        f"- **{len(actuals)} row(s) across {len(jobs)} job(s)** is enough to look at and not "
        "enough to fit. Treat any single heater's ft/pig as an anecdote.",
        "- Condition comes from each card's Task Durations row for the same Job #, not from "
        "the pig table — a job with pig rows but no durations row shows `unknown`. Same "
        "rule as durations: a crashed furnace eats more pigs than routine service, so "
        "crash and routine figures must not be pooled.",
        "- **Bore and condition are confounded in this dataset — do not read the bore table "
        "as a bore effect.** The only two crash points are H-19 and H-20, and both sit at "
        "the same 3.068\" bore. So the low ft/pig at small bore and the low ft/pig on crash "
        "jobs are the same two rows counted twice, and nothing here separates them. "
        "Untangling it needs either a crash job at a large bore or a routine job at a small "
        "one; until one lands, condition is the better-supported reading, because it splits "
        "cleanly (crash 15–43 against routine 41–212) while bore does not order at all — "
        "6.065\" spans 43–212 on its own.",
        "- If a real effect looks worth using, the next step is a decision about shrinkage "
        "estimation, not a formula written straight off these rows.",
    ]
    return "\n".join(L) + "\n"


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
