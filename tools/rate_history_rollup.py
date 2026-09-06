#!/usr/bin/env python3
"""rate_history_rollup.py — aggregate the `## Hourly Charge-Out Rates` table from
every quote note into 04-knowledge/rate-history-rollup.md.

The cross-quote view that did not exist. Bill rates are scattered one-per-quote-note,
so "what did we charge at Baytown last time" meant opening files individually. The
concrete argument for building it: DSP25123 (F-901, ExxonMobil Baytown) carried
Filtration Standby at $35/hr against $150/hr on every other quote that has the row —
the sheet was built from the F-802 template and a deleted Support Unit row pulled the
$35 up one cell. It was caught only by cross-reading three Baytown quotes side by
side, which is precisely the manual work this report replaces.

REFERENCE ONLY — this report never changes a rate. Rates belong to a contract, not to
a facility or to this table, and nothing here can be quoted from. Any correction it
surfaces is Lane 4: Jesse decides.

DESIGN CONSTRAINTS, all ruled on before this was written (see
04-knowledge/concepts/rfq-intake-protocol.md § Open Questions):

  * SHOW THE SPREAD, DO NOT COLLAPSE IT. The unit of truth is the quote note. This
    report date-orders and compares; it does not resolve. That is why labels the
    source distinguishes stay distinguished — triple-mode pigging and mode-unstated
    pigging are separate rows even though a tidier table would merge them.
  * THE COMPARISON COLUMN IS `Most common (derived)`, NOT `House standard`
    (Jesse, 2026-09-06). There is no artifact that is the house standard. The
    estimating skill's Baseline Rate Table is the only named company-wide schedule
    and it is captioned "generic rates for new facilities without contract rates";
    it diverges from what is actually quoted on most lines (Pumper: Pig $500 vs the
    $650-800 quoted, PM $80 vs $94.75, Crew Truck $15 vs $25, DEF $125 vs $180).
    Anchoring there would flag nearly every cell and destroy the flag's meaning. So
    the column is computed, and it PRINTS ITS OWN SUPPORT COUNT — with nine quotes a
    5-4 split is a coin flip and an unqualified modal value would read as canon.
  * DEPARTMENT/DIVISION IS NOT THE DISCRIMINATOR. An earlier reading attributed the
    spread to different groups issuing bids at one site; Jesse walked that back on
    2026-07-26. Department correlates, it does not cause. Do not re-derive it.

Pure standard library. Writes a GENERATED file.

Usage:
    python tools/rate_history_rollup.py           write the rollup
    python tools/rate_history_rollup.py --print   also print to stdout

Windows: `py tools/rate_history_rollup.py`.

Exit codes: 0 always. Unmapped labels are a backlog, and a backlog is not a failure.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estimating_rollup  # noqa: E402  (same-dir sibling module)

OUT_REL = "04-knowledge/rate-history-rollup.md"
FACILITIES = "02-facilities"
RATE_HEADING = "Hourly Charge-Out Rates"

# A quote note whose rate section is a pointer rather than a table. The rates are
# real and belong in the comparison, but they are not this quote's own schedule, so
# the column is sourced and HELD OUT OF THE MODAL COUNT (see build()). The Valero
# card says outright that no contract rates are confirmed for the site and that the
# set is precedent carried from DSP26094 / DSP26035.
POINTERS = {
    "DSP26100": (
        "02-facilities/Valero/Three-Rivers-TX/_facility.md",
        "Contracted Rates",
        "facility card — Valero precedent set, unconfirmed for this site",
    ),
}


def norm_label(s: str) -> str:
    """Fold a source line-item label to a lookup key.

    The corpus uses `4x3` and `4×3` (U+00D7), `Stand-by` and `Standby`, `Rig-In/Out`
    and `Rig-in / Out`, and inconsistent capitalisation. None of that is meaningful.
    """
    s = s.replace("×", "x").replace("–", "-").replace("—", "-")
    s = re.sub(r"[*_`]", "", s)                 # markdown emphasis
    s = re.sub(r"\s+", " ", s).strip().lower()
    s = re.sub(r"\s*/\s*", "/", s)              # "Rig-In / Out" -> "rig-in/out"
    return s.rstrip(".:").strip()


# --- The alias map -------------------------------------------------------------
#
# HAND-MAINTAINED, AND IT HAS TO BE. Service labels are not normalised across quote
# notes and never will be: the same line is written `Trimax Pumper Triple Mode:
# Pigging`, `Triple: Pigging`, `Pumper: Pigging` and `Trimax Pigging` in four
# different notes. There is no rule that recovers the canonical form from the string.
#
# ADDING TO THIS MAP IS THE MAINTENANCE COST OF THE REPORT. An unrecognised label is
# NEVER dropped — it lands in the `Unmapped labels` section of the output, because a
# silently dropped row is exactly how a DSP25123 gets missed a second time.
#
# WHAT IS DELIBERATELY *NOT* MERGED, and why: where a source distinguishes pumping
# mode or shift, the distinction is preserved. Collapsing `Triple Mode: Pigging`
# ($800) with an unlabelled `Pumper: Pigging` ($500-800) would manufacture a spread
# that is really a difference in what the row means.
ALIASES: dict[str, str] = {}


def _alias(canon: str, *sources: str) -> None:
    for s in sources:
        ALIASES[norm_label(s)] = canon


_alias("Pumper — Rig-In / Rig-Out / Rig-Over",
       "Pumper: Rig-In/Out", "Pumper: Rig-in/Out", "Pumper: Rigging",
       "Trimax Pumper: Rig-In / Out / Rig Over", "Trimax Rig-In/Out",
       "Trimax: Rigging", "Trimax Rigging",
       "Decoking pumper — rig-in / rig-over / rig-out / stand-by")
_alias("Pumper — Pigging (triple mode)",
       "Trimax Pumper Triple Mode: Pigging", "Triple: Pigging")
_alias("Pumper — Pigging (double mode)",
       "Trimax Pumper Double Mode: Pigging", "Double: Pigging")
_alias("Pumper — Pigging (mode not stated)",
       "Pumper: Pigging", "Trimax Pigging", "Trimax: Pigging",
       "Decoking pumper — pigging (incl. hoses, launchers, receivers, whip checks)")
_alias("Pumper — Smart Pig",
       "Pumper: Smart Pig", "Trimax Pumper: Smart Pigging", "Trimax: Smart Pig",
       "Decoking pumper — smart pig support")
_alias("Pumper — Stand-by",
       "Pumper: Stand-by", "Trimax Pumper Standby", "Trimax Stand-by",
       "Trimax: Stand-by")
_alias("Support Unit", "Support Unit")
_alias("Support trailer", "Support trailer")
_alias("Support tractor", "Support tractor")
_alias("Filtration", "Filtration", "Filtration Unit", "Filtration — pumping")
_alias("Filtration Stand-by",
       "Filter Stand-by", "Filtration Standby", "Filtration — stand-by")
_alias("Crew Truck", "Crew Truck", "Crew truck")
_alias("4x3 Trash Pump",
       "4×3 Trash Pump", "4x3 Trash Pump", "4×3 High Head Diesel Pump",
       "4×3 pump", "4x3 pump")
_alias("Project Manager", "Project Manager", "Pigging Project Manager")
_alias("Supervisor (day)",
       "Day Supervisor", "Pigging Supervision (Days)", "Pigging Supervision (Day)")
_alias("Supervisor (night)",
       "Night Supervisor", "Pigging Supervision (Nights)",
       "Pigging Night Shift Supervision")
_alias("Supervisor (shift not stated)", "Supervisor")
_alias("Operator", "Operator", "Pigging Operator")
_alias("Per Diem", "Per Diem")
_alias("Per Diem — Supervision", "Per Diem — Supervision")
_alias("Per Diem — Operator", "Per Diem — Operator")
_alias("Consumables per man", "Consumables per man")
_alias("Drain hose", "Drain hose")
_alias("Pressure hose", "Pressure hose")
_alias("Equipment travel", "Equipment travel")
_alias("Crew travel (non-driver)", "Crew travel (non-driver)")
_alias("DEF", "DEF")
_alias("Third-party markup",
       "Third Party", "Third-party markup", "Mark-up", "Markup")
_alias("Decoking pigs", "Decoking Pigs", "Decoking pigs")

# Row order in the output. Anything mapped but missing from this list is appended
# alphabetically, so forgetting to order a new alias degrades placement, not content.
CANON_ORDER = [
    "Pumper — Rig-In / Rig-Out / Rig-Over",
    "Pumper — Pigging (triple mode)",
    "Pumper — Pigging (double mode)",
    "Pumper — Pigging (mode not stated)",
    "Pumper — Smart Pig",
    "Pumper — Stand-by",
    "Support Unit",
    "Support trailer",
    "Support tractor",
    "Filtration",
    "Filtration Stand-by",
    "4x3 Trash Pump",
    "Crew Truck",
    "Drain hose",
    "Pressure hose",
    "Project Manager",
    "Supervisor (day)",
    "Supervisor (night)",
    "Supervisor (shift not stated)",
    "Operator",
    "Per Diem",
    "Per Diem — Supervision",
    "Per Diem — Operator",
    "Consumables per man",
    "DEF",
    "Equipment travel",
    "Crew travel (non-driver)",
    "Third-party markup",
    "Decoking pigs",
]

# Rows that live inside a rate table but are not rates. Excluded BY NAME rather than
# by a numeric filter, so that a genuinely new rate line is never silently swallowed
# by a heuristic.
#   DSP26039 `Composite Rate $1,318.38/hr` — a derived project metric.
#   DSP25084 `Mobilization | Waived | per mile` — a commercial term for that job.
#   Valero   `Mob / Demob | Lump sum | Per project` — likewise.
NOT_A_RATE = {
    norm_label("Composite Rate"),
    norm_label("Mobilization"),
    norm_label("Mob / Demob"),
}

# Lines whose "unit" cell is not a unit. The corpus writes the markup line's unit as
# `mark-up`, `Third party`, `ea`, `—`, and — on the Valero card — the whole sentence
# `Stated against the Decoking Pigs line`. None of that is a billing basis, and
# keying rows on it splits one line item into four rows that are really one.
UNITLESS = {"Third-party markup", "Decoking pigs"}

UNIT_MAP = {
    "/hr": "hr", "hr": "hr", "hour": "hr", "/hour": "hr",
    "/day": "day", "day": "day", "per day": "day",
    "/shift": "shift", "shift": "shift", "per shift": "shift",
    "mile": "mile", "per mile": "mile", "/mile": "mile",
    "ea": "ea", "each": "ea", "/ea": "ea",
    "mark-up": "mark-up", "markup": "mark-up", "third party": "mark-up",
    "per hose / day": "hose/day", "per hose/day": "hose/day",
    "per project": "project",
}


def split_unit(cell: str) -> tuple[str, str]:
    """(normalised unit, trailing prose) for one Unit cell.

    Folds the four unit vocabularies in the corpus onto one — `/hr` · `Hour` · `hour`
    all mean the same thing; `—` or empty means not stated. Anything unrecognised is
    passed through verbatim rather than guessed at, because the unit is half of what
    makes two rates comparable.

    The second return value is the rest of the cell. DSP26071 writes its filter
    stand-by unit as `/hr — changed by approved CO, see note below`, and that clause
    is the only machine-readable trace of the change order anywhere in the table. It
    is carried through to the superseded-cells section rather than discarded.
    """
    s = re.sub(r"[*_`]", "", cell or "").strip()
    parts = re.split(r"\s+[-—–]\s+", s, maxsplit=1)
    s, rest = parts[0].strip(), (parts[1].strip() if len(parts) > 1 else "")
    if s in {"", "-", "–", "—"}:
        return "(not stated)", rest
    return UNIT_MAP.get(s.lower(), s), rest


MONEY = re.compile(r"\$\s*([\d,]+(?:\.\d+)?)")


def parse_rate(cell: str) -> tuple[str, float | None, str | None, bool]:
    """(display, numeric, text_key, superseded) for one Rate cell.

    THE HAZARD THIS EXISTS FOR. `estimating_rollup.num()` is deliberately tolerant and
    returns the FIRST number it finds — on `~~$35.00~~ → **$150.00**` that is 35.0,
    the struck figure, which is the wrong one and is exactly the defect this whole
    report was built to surface. So the superseded form is detected first and the
    POST-arrow figure is what counts.

    The display string is the source cell verbatim. Strikethrough and bold are
    preserved because they carry the supersession; normalising them away would erase
    the signal. `~~$35~~ → $150` renders in Obsidian as it reads here.
    """
    raw = (cell or "").strip()
    superseded = "~~" in raw and ("→" in raw or "->" in raw)
    if superseded:
        # Everything after the arrow is what governs.
        tail = re.split(r"→|->", raw, maxsplit=1)[1]
        m = MONEY.search(tail)
        val = float(m.group(1).replace(",", "")) if m else None
        return raw, val, None, True
    m = MONEY.search(raw)
    if m:
        return raw, float(m.group(1).replace(",", "")), None, False
    # Non-numeric but real: `15%`, `cost + 15%`, `Cost + 5%`, `Waived`, `Lump sum`.
    key = re.sub(r"[*_`]", "", raw).strip().lower()
    # A markup is the same commercial term however it is written. `15%`,
    # `cost + 15%` and `Cost + 15%` are one rate, and comparing them as strings
    # manufactures a divergence out of three spellings. The percentage is the term.
    pct = re.fullmatch(r"(?:cost\s*\+\s*)?(\d+(?:\.\d+)?)\s*%", key)
    if pct:
        key = f"{pct.group(1)}%"
    return raw, None, (key or None), False


def quote_notes(root: Path):
    """Every `type: quote` note under 02-facilities, in path order."""
    for p in sorted((root / FACILITIES).rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fm = estimating_rollup.parse_frontmatter(text)
        if fm.get("type") == "quote":
            yield p, fm, text


def frontmatter_list(text: str, key: str) -> list[str]:
    """The items of a YAML list-valued frontmatter key.

    `estimating_rollup.parse_frontmatter` keeps scalar `key: value` lines only, so
    `heaters:` comes back empty from it. That is correct for its own use and wrong
    here, where the heater tags are the column's identity. Parsed rather than left
    blank, because a blank provenance cell is worse than no column.
    """
    out: list[str] = []
    in_fm = False
    in_key = False
    for line in text.splitlines():
        s = line.strip()
        if s == "---":
            if in_fm:
                break
            in_fm = True
            continue
        if not in_fm:
            continue
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            in_key = True
            continue
        if in_key:
            m = re.match(r"^\s+-\s+(.*)$", line)
            if m:
                out.append(m.group(1).strip().strip("'\""))
                continue
            in_key = False
    return out


def quote_id(fm: dict[str, str], path: Path) -> str:
    """The quote's own number.

    NEVER derived from the filename. `DSP26071.md` carries `quote-number: DSP26071.2`,
    `DSP24005.md` carries `DSP24005.2`, and `DSP26006.md` carries `DSP#26006`. Three
    of thirteen disagree with their own filename.
    """
    return (fm.get("quote-number") or path.stem).strip()


def short_id(qid: str) -> str:
    """Column key: `DSP#26006` and `DSP26071.2` both shorten to a sortable token."""
    return re.sub(r"[^A-Za-z0-9]", "", qid)


def read_rate_rows(text: str, heading: str) -> list[tuple[str, str, str]]:
    """(label, rate cell, unit cell) for the first table under `## {heading}`.

    The blank line after the heading is not guaranteed — DSP26039 and DSP26058 start
    the table on the very next line, and DSP26095 has two paragraphs of prose in
    between. `table_rows` skips non-pipe lines, so both shapes fall out for free.
    Header naming is not stable either (`Service` / `Description` / `Line Item`), so
    columns are taken by POSITION, which is stable at three across the whole corpus.
    """
    out = []
    for r in estimating_rollup.table_rows(estimating_rollup.section_lines(text, heading)):
        if len(r) < 2:
            continue
        r = (r + ["", "", ""])[:3]
        if not r[0].strip():
            continue
        out.append((r[0].strip(), r[1].strip(), r[2].strip()))
    return out


def section_prose(text: str, heading: str) -> str:
    """Non-table, non-blank lines under a heading — how a pointer section reads."""
    lines = [l.strip() for l in estimating_rollup.section_lines(text, heading)]
    return " ".join(l for l in lines
                    if l and not l.startswith("|") and not re.fullmatch(r"-{3,}", l))


class Quote:
    def __init__(self, path: Path, fm: dict[str, str], qid: str):
        self.path = path
        self.fm = fm
        self.qid = qid
        self.key = short_id(qid)
        # (canon, unit) -> (display, numeric, text_key, superseded, unit_note)
        self.cells: dict[tuple[str, str], tuple] = {}
        self.unmapped: list[tuple[str, str, str]] = []
        self.source_note: str | None = None   # set for pointer-sourced columns
        self.no_rate_section = False
        self.prose_only = ""
        self.heaters: list[str] = []

    @property
    def submitted(self) -> str:
        return (self.fm.get("date-submitted") or "").strip() or "(not recorded)"

    @property
    def sort_key(self) -> tuple:
        # An undated quote sorts LAST, not first. DSP26080 records no
        # date-submitted, and an empty string ahead of every real date would put a
        # 2027 bid at the head of a table whose whole point is chronological order.
        d = (self.fm.get("date-submitted") or "").strip()
        return (1, "", self.key) if not d else (0, d, self.key)

    @property
    def counts_toward_modal(self) -> bool:
        # A pointer column carries someone else's schedule. Counting it as a vote
        # would let an unconfirmed precedent set the figure everything else is
        # measured against.
        return self.source_note is None and bool(self.cells)


def load_quotes(root: Path) -> tuple[list[Quote], list[Quote]]:
    """(quotes with rates, quotes with no rate section) — both are results."""
    with_rates: list[Quote] = []
    rateless: list[Quote] = []
    for path, fm, text in quote_notes(root):
        q = Quote(path, fm, quote_id(fm, path))
        rows = read_rate_rows(text, RATE_HEADING)
        if not rows:
            pointer = POINTERS.get(short_id(q.qid))
            if pointer and (root / pointer[0]).exists():
                ptext = (root / pointer[0]).read_text(encoding="utf-8", errors="replace")
                rows = read_rate_rows(ptext, pointer[1])
                q.source_note = pointer[2]
                q.prose_only = section_prose(text, RATE_HEADING)
            if not rows:
                q.no_rate_section = True
                q.heaters = frontmatter_list(text, "heaters")
                rateless.append(q)
                continue
        q.heaters = frontmatter_list(text, "heaters")
        for label, rate, unit in rows:
            nl = norm_label(label)
            if nl in NOT_A_RATE:
                continue
            canon = ALIASES.get(nl)
            if canon is None:
                q.unmapped.append((label, rate, unit))
                continue
            u, unit_note = split_unit(unit)
            if canon in UNITLESS:
                u = "markup"
            q.cells[(canon, u)] = parse_rate(rate) + (unit_note,)
        with_rates.append(q)
    with_rates.sort(key=lambda x: x.sort_key)
    rateless.sort(key=lambda x: x.key)
    return with_rates, rateless


def modal(values: list) -> tuple[object | None, int, int, bool]:
    """(value, support, population, tied). Tied modes are reported, never broken."""
    if not values:
        return None, 0, 0, False
    counts = Counter(values)
    top = max(counts.values())
    winners = [v for v, c in counts.items() if c == top]
    return winners[0], top, len(values), len(winners) > 1


def fmt_money(v: float) -> str:
    return f"${v:,.2f}"


def build(root: Path) -> str:
    quotes, rateless = load_quotes(root)
    voting = [q for q in quotes if q.counts_toward_modal]

    rows = sorted({k for q in quotes for k in q.cells},
                  key=lambda k: (CANON_ORDER.index(k[0]) if k[0] in CANON_ORDER
                                 else len(CANON_ORDER), k[0], k[1]))

    lines = [
        "<!-- GENERATED by tools/rate_history_rollup.py - do not edit; rerun to refresh. -->",
        "# Rate History Rollup",
        f"**Generated:** {date.today().isoformat()} — every `## {RATE_HEADING}` table in the "
        "vault, date-ordered, against the most common figure across quotes.",
        "",
        "> **These rates are expired or contract-bound, not available.** Rates belong to a "
        "**contract**, not to a facility and not to this table. A short-form scope contract "
        "freezes its rates for one identified scope and **ends when that scope completes**, so "
        "a figure here is a record of what was charged and when. **Nothing in this table can "
        "be quoted from.** The rates for the next bid come from that bid's own contract or bid "
        "instructions — see `04-knowledge/concepts/rfq-intake-protocol.md` § 3.",
        "",
        "> **Read a divergence as a flag, not as a regime.** USADebusk prefers to run the same "
        "rates at every facility, so most cells should agree. Where one does not, there are "
        "**two legitimate drivers** (Jesse, 2026-07-26): **contract term** — a short-form "
        "contract froze an older figure, so two quotes differing can be two moments in time "
        "rather than two policies; and **competitive pressure** — rates cut to win a contested "
        "RFQ, a deliberate commercial act rather than drift. "
        "**Department or division is NOT the discriminator** — that reading was walked back on "
        "2026-07-26. Department correlates; it does not cause.",
        "",
        "> **`Most common (derived)` is computed here — it is not a house standard.** No "
        "artifact in the vault or the skills is the house standard. The `usadebusk-estimating` "
        "Baseline Rate Table is the only named company-wide schedule and it is captioned "
        "*generic rates for new facilities without contract rates*; it diverges from what is "
        "actually quoted on most lines. So this column is the plurality of what was really "
        "charged, **and it prints its own support count**. Read `(5 of 9)` as a coin flip and "
        "`(9 of 9)` as a settled practice. A tie is reported as a tie and never broken.",
        "",
    ]

    # --- Column key ---------------------------------------------------------
    lines += [
        "## Column key",
        "",
        "Provenance for every column, read from each note's own frontmatter. "
        "**The quote number is never derived from the filename** — three notes disagree with "
        "their own (`DSP26071.md` → `DSP26071.2`, `DSP24005.md` → `DSP24005.2`, "
        "`DSP26006.md` → `DSP#26006`).",
        "",
        "| Col | Quote | Client / facility | Heaters | Submitted | Status | Rate basis | Billing basis | Source |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for q in quotes:
        fm = q.fm
        heaters = ", ".join(q.heaters) or fm.get("unit_id") or "(not recorded)"
        client = " / ".join(x for x in [fm.get("client", ""), fm.get("facility", "")] if x)
        src = q.source_note or "own quote note"
        lines.append(
            f"| `{q.key}` | [[{q.path.stem}\\|{q.qid}]] | {client or '?'} | "
            f"{heaters} | {q.submitted} | **{fm.get('status', '?')}** | "
            f"{fm.get('rate-basis') or '(not recorded)'} | "
            f"{fm.get('billing-basis') or '(not recorded)'} | {src} |")
    lines.append("")

    # --- The table ----------------------------------------------------------
    hdr = " | ".join(f"`{q.key}`" for q in quotes)
    lines += [
        "## Rates",
        "",
        f"| Line Item | Unit | {hdr} | Most common (derived) |",
        "|---" * (len(quotes) + 3) + "|",
    ]
    flagged: list[str] = []
    superseded_cells: list[str] = []
    for canon, unit in rows:
        cells = []
        nums = [q.cells[(canon, unit)][1] for q in voting if (canon, unit) in q.cells
                and q.cells[(canon, unit)][1] is not None]
        texts = [q.cells[(canon, unit)][2] for q in voting if (canon, unit) in q.cells
                 and q.cells[(canon, unit)][2] is not None]
        if nums:
            mval, sup, pop, tied = modal(nums)
        else:
            mval, sup, pop, tied = modal(texts)
        for q in quotes:
            got = q.cells.get((canon, unit))
            if got is None:
                cells.append("—")
                continue
            disp, val, txt, sup_flag, unit_note = got
            if sup_flag:
                superseded_cells.append(
                    f"`{canon}` ({unit}) — {q.qid}: {disp}"
                    + (f". Source note on the cell: *{unit_note}*" if unit_note else ""))
            eff = val if val is not None else txt
            mark = ""
            if mval is not None and eff is not None and eff != mval and not tied:
                mark = "**≠** "
                flagged.append(
                    f"`{canon}` ({unit}) — {q.qid} at {disp}, against "
                    f"{fmt_money(mval) if isinstance(mval, float) else mval} "
                    f"on {sup} of {pop}")
            cells.append(f"{mark}{disp}")
        if mval is None:
            mcol = "—"
        else:
            shown = fmt_money(mval) if isinstance(mval, float) else str(mval)
            mcol = f"{shown} ({sup} of {pop})" + (" — **tied**" if tied else "")
        lines.append(f"| {canon} | {unit} | " + " | ".join(cells) + f" | {mcol} |")

    lines += [
        "",
        "**Reading a cell.** `—` means that quote's schedule does not carry this line. It does "
        "**not** distinguish *not priced for this scope* from *the row is missing because of a "
        "sheet defect* — DSP25123 is missing its Support Unit and Project Manager rows for "
        "exactly the second reason, and nothing in the source table says so. Open the note. "
        "**≠** marks a cell whose effective figure differs from the plurality; it is a prompt to "
        "read the note, not a verdict. A struck cell (`~~$35~~ → $150`) records a rate that was "
        "superseded — the figure **after** the arrow is the one that governs and the one counted "
        "here.",
        "",
        "**Units are not collapsed across bases.** `4x3 Trash Pump` appears on separate rows for "
        "`hr` and `shift` because it is genuinely billed both ways ($85/hr on the later Baytown "
        "sheets, $1,016/shift on the earlier ones) and that basis change is unreconciled. Two "
        "rates on different bases are not a spread; they are different questions.",
        "",
        "> ⚠ **`Pumper — Pigging (mode not stated)` is the one row whose ≠ marks may not be "
        "divergences at all.** Pigging is priced by mode — triple runs above double — but only "
        "DSP25084 and DSP25123 label the mode, and DSP26039 labels it as `Triple: Pigging`. Every "
        "other note writes an unqualified `Pumper: Pigging` or `Trimax Pigging`, so that row mixes "
        "triple-mode, double-mode and unknown-mode figures on one line. DSP26071.2's $800 reads as "
        "a triple rate and DSP26085's $650 as a double, which would make both of them agree with "
        "the mode-specific rows above rather than diverge from this one. **The rollup cannot tell** "
        "— the source does not say. Read this row against the note, and if the mode label is worth "
        "having, it has to be written at bid time.",
        "",
    ]

    # --- Superseded ---------------------------------------------------------
    lines += ["## Superseded cells", ""]
    if superseded_cells:
        lines.append(
            "A rate struck and replaced in its own source table. **Both figures are real** — the "
            "struck one is what went to the customer, the replacement is what governs — so neither "
            "is edited away here. The figure after the arrow is the one counted in the plurality "
            "column.")
        lines.append("")
        lines += [f"- {s}" for s in superseded_cells]
        lines += [
            "",
            "> **$35/hr has appeared at ExxonMobil Baytown three different ways and the number "
            "alone diagnoses nothing.** On DSP25123 it was a template artifact — the F-901 sheet "
            "was built from the F-802 template and a deleted Support Unit row pulled the $35 up "
            "one cell. On DSP26071.2 it was a genuinely negotiated rate. On USA26041, the job that "
            "quote became, it was renegotiated to $150 by the account manager before mobilization. "
            "Read the surrounding note rather than pattern-matching the figure.",
        ]
    else:
        lines.append("- none — no cell in any rate table records a superseded figure")
    lines.append("")

    # --- Divergences --------------------------------------------------------
    lines += ["## Cells that differ from the plurality", ""]
    if flagged:
        lines += [f"- {f}" for f in flagged]
    else:
        lines.append("- none — every priced cell matches its row's plurality")
    lines += [
        "",
        "> Each of these is a question, not an error. Check the quote's `rate-basis` and "
        "`billing-basis` first, then the prose caveats in the note itself — most rate tables in "
        "the corpus carry a paragraph immediately after them qualifying the figures.",
        "",
    ]

    # --- Coverage -----------------------------------------------------------
    lines += ["## Coverage", ""]
    lines.append(
        f"- **{len(quotes)}** quote note(s) contribute a rate schedule; **{len(voting)}** of "
        "them vote in the plurality column.")
    for q in quotes:
        if q.source_note:
            lines.append(
                f"- `{q.key}` is **sourced, not self-carried** — its `## {RATE_HEADING}` "
                f"section is a pointer ({q.source_note}). Held out of the plurality count: an "
                "unconfirmed precedent must not set the figure everything else is measured "
                f"against. The note reads: *{q.prose_only[:280]}*")
    if rateless:
        lines += [
            "",
            "**Quote notes with no rate schedule — absent by design, not a gap.** A quote with "
            "no hourly rate table simply has no such section; do not add an empty one.",
            "",
        ]
        for q in rateless:
            lines.append(
                f"- [[{q.path.stem}\\|{q.qid}]] — {q.fm.get('client', '?')}, "
                f"status `{q.fm.get('status', '?')}`")
    lines += [
        "",
        "**Rates that exist only as prose are out of scope for this table** and are not parsed. "
        "Known instances, all real billable figures: DSP25123's trailing *\"Plus $50.00/hr per "
        "additional pump when smart pigging with multiple tools\"*; DSP26092's smart-pig support "
        "bullets; DSP26030's pipe-delimited commercial line; DSP24005's separately-quoted "
        "filtration option. Read those notes directly.",
        "",
    ]

    # --- Unmapped -----------------------------------------------------------
    unmapped = [(q, lab, rate, unit) for q in quotes for (lab, rate, unit) in q.unmapped]
    lines += ["## Unmapped labels", ""]
    if not unmapped:
        lines.append(
            "- none — every line item in every rate table resolved through the alias map")
    else:
        lines.append(
            "**These rows were read but not placed.** They are listed rather than dropped: a "
            "silently discarded row is how a bad rate survives a second review. Add each to "
            "`ALIASES` in `tools/rate_history_rollup.py`, or to `NOT_A_RATE` if it is not a "
            "rate, then re-run.")
        lines.append("")
        lines.append("| Quote | Label as written | Rate | Unit |")
        lines.append("|---|---|---|---|")
        for q, lab, rate, unit in unmapped:
            lines.append(f"| `{q.key}` | {lab} | {rate} | {unit} |")

    lines += [
        "",
        "## Reading this",
        "",
        "- **This report resolves nothing.** It date-orders and compares. Where two quotes "
        "disagree, the quote note is the unit of truth and both figures stand — each belonged "
        "to a contract that set its own rates and then ended.",
        "- **The plurality column is descriptive, not normative.** It says what was most often "
        "charged, not what should be. Take the governing figure for a new bid from that bid's "
        "contract or bid instructions.",
        "- **A rate correction is Lane 4.** If something here looks wrong, raise it with Jesse "
        "rather than editing a quote note from this table. What the table is for is making the "
        "cross-quote read cheap enough to actually do — the DSP25123 $35/hr filtration standby "
        "cell was found only by opening three Baytown quotes side by side.",
        "- **Regenerate before citing.** Nothing schedules this script; it is on-demand like "
        "`coil_geometry_audit.py`.",
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
