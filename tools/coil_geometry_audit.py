#!/usr/bin/env python3
"""coil_geometry_audit.py — which heater cards carry coil geometry good enough
to work from, and exactly what blocks the rest.

Writes 04-knowledge/coil-geometry-audit.md. Pure standard library, matching the
vault_lint.py / vault_health.py / estimating_rollup.py convention.

WHY THIS EXISTS (2026-08-24 reshape of the 2026-08-01 approval). The approved
coil-visualization build was Tier 2+3: port buildGeometry() out of
apps/pig-tracker/pig-tracker.html and render an SVG coil elevation per card. Two
things reshaped it. First, that function is 136 lines of JavaScript and this
directory is stdlib Python, so "extract the layout engine" is a port, not a lift.
Second, the exploration's flagship argument -- that a renderer would force hidden
geometry into the open -- has weakened, because the cards now surface those
irregularities themselves (H-28 records "4 (+2 heater-wide)" right in Config
Rollup, and ROLLUP-SCALE already checks that arithmetic).

What survived is narrower and needs no renderer: FOURTEEN OF FORTY-FOUR CARDS
CANNOT BE DRAWN AT ALL, AND NOTHING PRODUCED THAT LIST. That list is the
cross-cutting artifact -- a backlog of where coil geometry is missing,
unclassifiable, or compound. The drawing is optional; knowing which cards you
can trust is not.

THE HAZARD THIS IS BUILT AGAINST. estimating_rollup.num() is deliberately
tolerant: num("4 (+2 heater-wide)") returns 4.0, silently dropping the "+2".
H-28's radiant row is a live instance -- two tubes that do not distribute evenly
across four passes. A validator that reaches for num() first reports that card
clean and hides the exact defect it was built to find. So every cell goes
through classify_cell() BEFORE any numeric parse, and a cell whose numeric prefix
does not account for its whole content is COMPOUND, never a number.

NOT A LINT RULE, SO NO FIXTURE IS OWED. vault_lint.py's contract is "no fixture,
no rule" (see tools/fixtures/README.md). This is a standalone generator like
estimating_rollup.py and pig_usage_rollup.py, so it carries no fixture. If any
check here is ever promoted INTO vault_lint.py, it owes a fixture at that point.

RUN ON DEMAND. Not wired to a loop -- the loops that would have scheduled it were
stopped 2026-08-21. Re-run before citing it, same standing caveat CLAUDE.md
records for pig_usage_rollup.py.

Usage:
    python tools/coil_geometry_audit.py           write the report
    python tools/coil_geometry_audit.py --print   also print to stdout

Windows: `py tools/coil_geometry_audit.py`.

Exit codes: 0 always. This reports a backlog; a backlog is not a failure.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estimating_rollup  # noqa: E402  (same-dir sibling module)

OUT_REL = "04-knowledge/coil-geometry-audit.md"

# Tube Geometry column order, locked by vault_lint.TUBE_GEOM_HEADER. Indices are
# taken from this list rather than hardcoded so a schema change surfaces here as
# a rename rather than as a silently-shifted column.
COLS = ["Section", "Arrangement", "Metallurgy", "OD (in)", "Sched", "Wall (in)",
        "ID (in)", "Tubes/Circuit", "Avg Length (ft)", "Length/Circuit (ft)",
        "Return Bend Type"]
C_SECTION = COLS.index("Section")
C_ID = COLS.index("ID (in)")
C_TUBES = COLS.index("Tubes/Circuit")
C_AVGLEN = COLS.index("Avg Length (ft)")
C_LENCIRC = COLS.index("Length/Circuit (ft)")

# Zone classification. Prefix match resolves 109 of 112 segment rows in the
# fleet as of 2026-08-24. The canonical card invites free text in this column
# ("Radiant -- segment 1 of N", "Convection -- Sch 120 portion"), so a prefix is
# the honest reading; an exact-match enum would reject most real cards.
ZONE_PATTERNS = [
    ("radiant", re.compile(r"^radiant\b", re.IGNORECASE)),
    ("convection", re.compile(r"^convection\b", re.IGNORECASE)),
    ("crossover", re.compile(r"^cross-?over\b", re.IGNORECASE)),
]

# "Not recorded" is an EXPECTED, VALID value per the canonical card -- the
# customer did not supply it. That is a different fact from an empty cell, which
# means nobody has filled the card in. Collapsing the two would misreport the
# fleet as lazier than it is, so they stay separate finding classes.
#
# The parenthesised form is what the cards actually use -- "(not recorded)", not
# "not recorded". The first cut of this rule matched only the bare form and
# reported 26 rows as COMPOUND that were nothing of the kind.
RECORDED_ABSENT_RE = re.compile(
    r"^(not\s+(recorded|stated|totaled|totalled)|unrecorded|unknown|n/?a|--?|tbd)$",
    re.IGNORECASE)
PAREN_WRAP_RE = re.compile(r"^[\(\[\{]\s*(.*?)\s*[\)\]\}]$")

# Numeric notation ACTUALLY used across the 44 cards, surveyed 2026-08-24 rather
# than assumed -- the first cut of these patterns allowed only a tilde and no
# thousands separator, which misread "≈1,067" and "≈33 (tube + bend)" as having
# no number in them at all and inflated the length gap by roughly a third.
#   approximation:  ~ and ≈ both appear
#   grouping:       1,067
#   trailing:       a unit or a footnote asterisk
# Ranges ("~35.2–41.8") are deliberately NOT accepted: two numbers is two
# numbers, and a serpentine cannot be drawn from a span.
APPROX = r"[~≈]?"
DIGITS = r"\d[\d,]*(?:\.\d+)?"
CLEAN_NUM_RE = re.compile(rf"^{APPROX}{DIGITS}\s*(in|ft|\")?\*?$", re.IGNORECASE)
LEAD_NUM_RE = re.compile(rf"^{APPROX}({DIGITS})\s*(.*)$", re.DOTALL)

# SCALE MISMATCH -- the defect this tool exists to catch. Tubes/Circuit and
# Length/Circuit are PER-CIRCUIT columns. A cell that answers at heater scale
# instead ("2 heater-wide") is not compound and not missing: it is the right
# number at the wrong scale, and num() reads it as a per-circuit figure,
# understating by the circuit count. H-28's radiant segment 2 of 2 is the live
# instance -- 2 tubes recorded heater-wide across 4 passes, the exact "2 tubes
# cannot split evenly across 4 coils" case the 2026-07-30 exploration named.
#
# JUDGE THE QUALIFIER THAT IMMEDIATELY FOLLOWS THE NUMBER, NOT THE WHOLE CELL.
# The first cut of this searched the entire remainder for a scale word and
# produced two false positives out of six findings -- enough to discredit the
# whole report:
#   B-1001  "18/circuit (36 heater-total ÷ 2 circuits)"  -- 18 IS per-circuit and
#           matches Config Rollup; the total is only cited in the derivation.
#   B-151   "~152 × ~22.4 avg ≈ 3,405 ft (approx, single pass total)" -- a
#           single-pass heater, where per-circuit and heater total are the same
#           number by definition.
# What the number is labelled AS decides its scale. What the parenthetical
# happens to mention does not.
SCALE_LEADING_RE = re.compile(
    r"^(total|heater[-\s]?wide|heater[-\s]?total|per[-\s]heater)\b", re.IGNORECASE)
PER_CIRCUIT_LEADING_RE = re.compile(
    r"^(/|per[-\s])\s*(circuit|pass|leg)\b", re.IGNORECASE)

OK, ABSENT, EMPTY, COMPOUND, QUALIFIED, HEATER, SCALE, IRREDUCIBLE = (
    "ok", "recorded-absent", "unfilled", "compound", "qualified",
    "heater-scale", "scale-mismatch", "heater-scale only (irreducible)")
USABLE = {OK, QUALIFIED}

# A heater-scale value splits two ways, and conflating them sends someone to
# "fix" a correct card (Jesse, 2026-08-24):
#   SCALE       -- a per-circuit column carrying a heater total WHEN A PER-CIRCUIT
#                  VALUE EXISTS. Our error. B-102's "16 total (8/pass × 2 passes)".
#   IRREDUCIBLE -- the card faithfully recording a heater-wide fact that CANNOT be
#                  per-circuit. H-28's "2 heater-wide": 2 tubes across 4 passes do
#                  not divide, and which pass carries them is unstated at source.
#                  A customer-data gap, not a card defect.
# Both still block a drawing. Only the first is ours to fix.
#
# The tell is NOT in the cell. The first attempt looked for a "N/pass" figure in
# the same cell, which mislabelled B-102's length cells as irreducible -- they
# offer no per-leg figure of their own, but Config Rollup carries ~1,847, so they
# are plainly reducible. What actually distinguishes the two is whether the CARD
# anywhere says the quantity does not distribute evenly. H-28's Config Rollup
# per-circuit cell reads "4 (+2 heater-wide)" and its note says the two 5.76"
# tubes "don't distribute evenly"; B-102's says nothing of the kind.
NON_DISTRIBUTING_RE = re.compile(
    r"(heater[-\s]?wide|do(es)?n'?t\s+distribute|not\s+distribute|"
    r"cannot\s+(be\s+)?(split|divided?)|uneven)", re.IGNORECASE)


def classify_cell(cell: str) -> tuple[str, float | None]:
    """Return (state, value). Value is set for OK and QUALIFIED only.

    Order matters: every structural test runs BEFORE any numeric parse, because
    estimating_rollup.num() is deliberately tolerant and would return 2.0 for
    "2 heater-wide" -- silently converting a heater-wide count into a per-circuit
    one. Reaching for num() first is the way to build this wrong.
    """
    s = (cell or "").strip()
    if not s:
        return EMPTY, None
    inner = PAREN_WRAP_RE.match(s)
    if RECORDED_ABSENT_RE.match(inner.group(1) if inner else s):
        return ABSENT, None
    if CLEAN_NUM_RE.match(s):
        return OK, estimating_rollup.num(s)

    m = LEAD_NUM_RE.match(s)
    if not m:
        # Content, but it does not even start with a number.
        return COMPOUND, None
    value, rest = float(m.group(1).replace(",", "")), m.group(2)
    if SCALE_LEADING_RE.match(rest):
        # Heater-scale, but WHICH KIND cannot be decided from this cell. Whether a
        # per-circuit value exists is a fact about the card, not about the string
        # -- B-102's length cells state no per-leg figure of their own, yet Config
        # Rollup carries ~1,847, so they are our error and not irreducible. The
        # caller resolves HEATER -> SCALE or IRREDUCIBLE against Config Rollup.
        return HEATER, None
    if PER_CIRCUIT_LEADING_RE.match(rest):
        # Explicitly labelled per-circuit. That label resolves the ambiguity the
        # digit rule below guards against, so a derivation in the parenthetical
        # is provenance, not a second value.
        return QUALIFIED, value
    if re.search(r"\d", rest):
        # A second number in the cell -- multi-valued (mixed bores per pass,
        # "46 (2 + 44)", "40/circuit (80 heater-total / 2)"). Not resolvable here.
        return COMPOUND, None
    # A single number carrying prose provenance -- "5.761 (design)", "2
    # pieces/pass". The value is unambiguous; the note is annotation.
    return QUALIFIED, value


def classify_zone(section: str) -> str | None:
    s = (section or "").strip()
    for zone, pat in ZONE_PATTERNS:
        if pat.match(s):
            return zone
    return None


def audit_row(row: list[str], resolve) -> dict:
    """Check one Tube Geometry segment row. Returns its zone and its blockers.

    `resolve(zone, state)` turns the cell-local HEATER verdict into SCALE or
    IRREDUCIBLE using the card's Config Rollup; see config_rollup_per_circuit().
    """
    r = (row + [""] * len(COLS))[:len(COLS)]
    section = r[C_SECTION].strip()
    zone = classify_zone(section)
    blockers = []

    def state_of(idx: int) -> str:
        return resolve(zone, classify_cell(r[idx])[0])

    if zone is None:
        # Service-named sections ("Treat Gas", "Superheat Steam") land here. They
        # are real coil sections but not one of the three zones a serpentine is
        # drawn from, so they fail loudly rather than defaulting into a bucket.
        blockers.append(("section does not classify to a zone", section))

    # Blockers are (cause, detail) pairs, never pre-joined strings. The cause is
    # what the gap tally groups on and the detail is the offending cell text.
    # Formatting them together up front and regex-stripping the detail back out
    # at tally time does not work: the cells themselves contain em dashes and
    # parentheses, so any stripper truncates mid-cell.
    for label, idx in (("tube count", C_TUBES), ("bore ID", C_ID)):
        state = state_of(idx)
        if state in USABLE:
            continue
        # Quote the cell only where the text IS the finding; for a plain absence
        # the cause already says everything.
        detail = r[idx].strip() if state in (COMPOUND, SCALE, IRREDUCIBLE) else ""
        blockers.append((f"{label} {state}", detail))

    # Length is satisfied by EITHER column, so it only blocks when both fail --
    # and the report names which way each failed. Lumping "the customer never
    # gave us a length" together with "the length is there but is not a plain
    # number" would hide the difference between a gap we cannot close and one we
    # can, which is the whole point of separating the states.
    avg_state, lc_state = state_of(C_AVGLEN), state_of(C_LENCIRC)
    if avg_state not in USABLE and lc_state not in USABLE:
        quoted = [r[i].strip() for i, st in
                  ((C_AVGLEN, avg_state), (C_LENCIRC, lc_state)) if st in (COMPOUND, SCALE, IRREDUCIBLE)]
        blockers.append((f"no usable length (avg {avg_state}, per-circuit {lc_state})",
                         " / ".join(quoted)))

    return {"section": section, "zone": zone, "blockers": blockers}


# Config Rollup columns: Scale | Section | Pipe ID(s) | Total Tubes | Total Length | Notes
CR_SCALE, CR_SECTION, CR_TUBES = 0, 1, 3


def zones_named(section: str) -> tuple[str, ...]:
    """Every zone a Config Rollup Section names, in canonical order.

    Config Rollup rows are NOT always one zone. Several cards carry a single
    combined row -- HP-0003's "Convection + Radiant" with "22 (12 conv + 10 rad)"
    -- because the source quote gave per-pass totals only. Prefix-matching such a
    row to "convection" alone charges the whole circuit's tube count to one zone
    and invents a contradiction on a card that reconciles perfectly.
    """
    s = (section or "").strip()
    return tuple(z for z, pat in ZONE_PATTERNS
                 if re.search(r"\b" + pat.pattern.lstrip("^"), s, re.IGNORECASE))


def config_rollup_per_circuit(text: str) -> list[dict]:
    """Per-circuit rows of Config Rollup.

    Returns one entry per row: {"zones", "raw", "value", "non_distributing"}.
    Config Rollup is the estimating reference and carries BOTH scales explicitly
    in its Scale column, which is why it can adjudicate what Tube Geometry's
    per-circuit columns should hold.
    """
    out: list[dict] = []
    for row in estimating_rollup.table_rows(
            estimating_rollup.section_lines(text, "Config Rollup")):
        r = (row + [""] * 6)[:6]
        if r[CR_SCALE].strip().lower() != "per circuit":
            continue
        zones = zones_named(r[CR_SECTION])
        if not zones:
            continue
        raw = r[CR_TUBES].strip()
        state, value = classify_cell(raw)
        if value is None and state not in (ABSENT, EMPTY):
            # Leading number with provenance that classify_cell would not take
            # (e.g. "22/leg (16 × 6\" + 6 × 8\")"). The Scale column already
            # asserts per-circuit, so the leading number is the per-circuit value.
            m = LEAD_NUM_RE.match(raw)
            if m:
                value = float(m.group(1).replace(",", ""))
        out.append({"zones": zones, "raw": raw, "value": value,
                    "non_distributing": bool(NON_DISTRIBUTING_RE.search(raw))})
    return out


def audit_card(text: str) -> dict:
    lines = estimating_rollup.section_lines(text, "Tube Geometry")
    rows = estimating_rollup.table_rows(lines)
    if not rows:
        return {"rows": [], "blockers": [("no Tube Geometry table", "", "")],
                "segments": 0, "contradictions": []}

    rollup = config_rollup_per_circuit(text)

    def rows_for(zone: str | None) -> list[dict]:
        return [cr for cr in rollup if zone in cr["zones"]]

    def resolve(zone: str | None, state: str) -> str:
        if state != HEATER:
            return state
        crs = rows_for(zone)
        # No per-circuit row to adjudicate against, or the card itself says the
        # quantity does not distribute -> the heater-scale figure is the only
        # honest one there is. Otherwise a per-circuit value exists and this
        # column should have carried it.
        if not crs or any(cr["non_distributing"] for cr in crs):
            return IRREDUCIBLE
        return SCALE

    results = [audit_row(r, resolve) for r in rows]
    # (section, cause, detail) -- kept as fields so the tally can group on cause
    # alone without parsing a rendered string back apart.
    blockers = [(res["section"] or "(unnamed section)", cause, detail)
                for res in results for cause, detail in res["blockers"]]

    # CROSS-CHECK: Tube Geometry's per-circuit tube counts, summed by zone,
    # against Config Rollup's Per circuit row for that zone. Nothing else does
    # this -- ROLLUP-SCALE checks Config Rollup's INTERNAL arithmetic only, which
    # is why B-102 carried heater totals in per-circuit columns from its
    # 2026-07-07 ingest until a tool built for something else tripped over it.
    #
    # Only compare when BOTH sides parse cleanly. A cross-check that manufactures
    # alarms on honestly-messy cards gets ignored, which is how the original
    # defect survived.
    contradictions = []
    for cr in rollup:
        if cr["value"] is None or cr["non_distributing"]:
            continue
        seg_values = []
        for res, raw in zip(results, rows):
            if res["zone"] not in cr["zones"]:
                continue
            cell = ((raw + [""] * len(COLS))[:len(COLS)])[C_TUBES]
            state, value = classify_cell(cell)
            if state == HEATER:
                # The defect case. A per-circuit column holding a heater total
                # still parses to a number, and comparing it IS the point -- an
                # earlier cut skipped every non-clean cell and so stepped over
                # B-102, the one card known to be broken.
                m = LEAD_NUM_RE.match(cell.strip())
                value = float(m.group(1).replace(",", "")) if m else None
            elif state not in USABLE:
                value = None
            if value is None:
                seg_values = None
                break
            seg_values.append(value)
        if not seg_values:
            continue
        total = sum(seg_values)
        if abs(total - cr["value"]) > 0.01:
            contradictions.append(
                (" + ".join(cr["zones"]), total, cr["value"], cr["raw"]))

    return {"rows": results, "blockers": blockers, "segments": len(results),
            "contradictions": contradictions}


def build(root: Path) -> str:
    renderable, blocked, contradictions = [], [], []
    total_segments = 0
    zone_counts: dict[str, int] = {}

    for path, fm, text in estimating_rollup.heater_cards(root):
        tag = fm.get("heater-tag") or path.stem
        client = fm.get("client", "?")
        res = audit_card(text)
        total_segments += res["segments"]
        for r in res["rows"]:
            z = r["zone"] or "UNCLASSIFIED"
            zone_counts[z] = zone_counts.get(z, 0) + 1
        entry = {"tag": tag, "client": client, "rel": path.relative_to(root).as_posix(),
                 "segments": res["segments"], "blockers": res["blockers"]}
        (blocked if res["blockers"] else renderable).append(entry)
        for zone, tg_total, cr_value, cr_raw in res.get("contradictions", []):
            contradictions.append((tag, client, path.relative_to(root).as_posix(),
                                   zone, tg_total, cr_value, cr_raw))

    total = len(renderable) + len(blocked)
    out = [
        "<!-- GENERATED by tools/coil_geometry_audit.py - do not edit; rerun to refresh. -->",
        "# Coil Geometry Audit",
        f"**Generated:** {date.today().isoformat()} — "
        f"**{len(renderable)} of {total}** heater cards carry coil geometry complete enough "
        "to work from; the rest are listed below with what blocks them.",
        "",
        "Run on demand — this is **not wired to a loop**, so re-run it before citing it. "
        "A blocked card is a backlog item, not an error: `not recorded` is a valid value on "
        "the canonical card, because customers do not always supply full tube specs. What "
        "this separates is *the customer never told us* from *nobody filled the card in* "
        "from *the value is there but is not a plain number*.",
        "",
        f"Segment rows examined: **{total_segments}**. Zones: "
        + ", ".join(f"{k} {v}" for k, v in sorted(zone_counts.items())) + ".",
        "",
    ]
    # Contradictions first: a card that disagrees with itself is a stronger
    # finding than a card that is merely incomplete, and it is the one class here
    # that can put a wrong number in front of a customer.
    out += ["## Tube Geometry contradicts Config Rollup", ""]
    if contradictions:
        out += ["A card's per-circuit tube counts must sum to its Config Rollup "
                "`Per circuit` row for the same zone. Where they do not, one of the two "
                "is wrong and the card cannot be trusted for estimating until it is settled. "
                "Rows are skipped, not guessed, wherever either side is compound, absent, "
                "or recorded as not distributing evenly.",
                "",
                "| Heater | Client | Zone | Tube Geometry sum | Config Rollup per circuit |",
                "|---|---|---|---|---|"]
        out += [f"| [[{t}]] | {c} | {z} | {tg:g} | {cr:g} (`{raw}`) |"
                for t, c, _rel, z, tg, cr, raw in
                sorted(contradictions, key=lambda x: (x[1], x[0]))]
    else:
        out.append("- none — every comparable card reconciles")

    out += ["", "## Cards you can work from", ""]
    if renderable:
        out += ["| Heater | Client | Segments |", "|---|---|---|"]
        out += [f"| [[{e['tag']}]] | {e['client']} | {e['segments']} |"
                for e in sorted(renderable, key=lambda e: (e["client"], e["tag"]))]
    else:
        out.append("- none")

    out += ["", "## Coverage gaps", ""]
    if blocked:
        for e in sorted(blocked, key=lambda e: (e["client"], e["tag"])):
            out.append(f"**{e['tag']}** ({e['client']}) — `{e['rel']}`")
            for section, cause, detail in e["blockers"]:
                shown = f" — `{detail}`" if detail else ""
                out.append(f"  - {section}: {cause}{shown}")
            out.append("")
    else:
        out.append("- none — every card carries complete coil geometry")

    # Grouped tally, so the backlog reads as causes rather than as a card list.
    causes: dict[str, int] = {}
    for e in blocked:
        for _section, cause, _detail in e["blockers"]:
            causes[cause] = causes.get(cause, 0) + 1
    if causes:
        out += ["## Gaps by cause", "", "| Cause | Segment rows |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in sorted(causes.items(), key=lambda kv: -kv[1])]
        out.append("")

    return "\n".join(out) + "\n"


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
