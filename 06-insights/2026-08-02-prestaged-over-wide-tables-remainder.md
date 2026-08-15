---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-02
related:
  - "[[02-facilities/_directory|_directory]]"
  - "[[_canonical-heater-card]]"
tags: [review, vault-hygiene, schema, heater-card, lint]
---

# Review — What to do about the two things `e4de4a5` deliberately left open

## Trigger

Pre-staging loop run 2026-08-02, processing the oldest genuine-open-question candidate
carrying a `vault-loop:` marker after five older items skipped as already-covered or
execution-corrections: `00-inbox/2026-07-27-over-wide-tables-remainder.md`. That note is a
follow-on to config commit `e4de4a5`, which dropped the Tube Geometry `Notes` column and
moved 75 notes across 39 cards into keyed blocks, cutting over-wide rows in `02-facilities`
from 82 to 48. It names three things left over: a directory-table width problem, a
key/value-table width question, and an open lint-coverage question. Only the first and
third carry a genuine open question — the second is explicitly "probably leave alone,"
recorded so a future session doesn't re-litigate it, and is excluded from this note on that
basis (matching the one-question-per-note scope this loop already used on
2026-07-31 for a similar multi-item source note).

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-27-over-wide-tables-remainder.md` (read this run) | Observed | States `_directory.md`'s Facilities table has cells running to 765 and 647 characters, asks whether the directory should become a scannable index with narrative pushed to each `_facility.md` or stay a "rich directory" and be tolerated; separately asks whether the new 11-column Tube Geometry header deserves a machine-checked lint lock like `DURATIONS-HEADER`, since the current protection (a dead-string rule in `usadebusk-core`) only catches an agent re-adding the dropped `Notes` column, not a hand edit or a card authored from a stale copy. |
| `02-facilities/_directory.md` (read this run) | Observed | Confirmed current: the Westlake South row's "What's there" cell alone runs well past 700 characters of prose (facility history, folder-tier rationale, do-not-duplicate warnings). The problem the inbox note describes is unchanged as of 2026-08-02 — nothing has restructured this table since. |
| `tools/vault_lint.py:466-503` (read this run) | Observed | `check_durations_header()` is the existing precedent: it anchors on the `## Task Durations` heading, reads only the first table row beneath it, and compares column tuples case-insensitively against a canonical schema constant (`DURATIONS_HEADER`), firing a warning-level `DURATIONS-HEADER` finding on any missing/extra/reordered/renamed column. A `TUBE-GEOM-HEADER` rule would be a near-identical anchor-and-compare pass against `## Tube Geometry`. |
| `04-knowledge/_canonical-heater-card.md:90-91` (read this run) | Observed | The current canonical Tube Geometry header is 11 columns: `Section \| Arrangement \| Metallurgy \| OD (in) \| Sched \| Wall (in) \| ID (in) \| Tubes/Circuit \| Avg Length (ft) \| Length/Circuit (ft) \| Return Bend Type` — no `Notes` column, consistent with what `e4de4a5` produced. |
| `~/.claude/skills/usadebusk-core/SKILL.md:9` (grepped this run) | Observed | Confirms the "dead string" pattern the inbox note refers to exists elsewhere in the same skill (the `USADeBusk` spelling reversal), so a bare dead-string reversion guard without a machine check is an established, if weaker, pattern in this vault — not unique to Tube Geometry. |
| `git log -- 02-facilities/_directory.md` since 2026-07-27 (checked this run) | Observed | Only a rename/repoint commit (`7c8df0b`) has touched the file since the inbox note was filed; no structural change was made. The width question is genuinely unaddressed, not partially covered. |

## The Question

Two independent open items ride on this one inbox note. (1) Should `02-facilities/_directory.md`'s Facilities table stay a one-line-per-facility index with the long narrative content pushed down into each `_facility.md`, or is the current rich-prose directory acceptable as-is because nobody reads it as a scannable table? (2) Should the new 11-column Tube Geometry header get a `vault_lint.py` rule mirroring `DURATIONS-HEADER` — catching a hand edit or a stale-copy-authored card, not just an agent reversion — or is the existing dead-string guard in `usadebusk-core` sufficient protection for a schema change this recent?

## Proposed Change

### For (1) — `_directory.md` narrative width

**A. Leave it as a rich directory, tolerated.** No restructuring. The table already serves as the de facto per-facility summary Jesse and any session land on first; splitting it would mean opening two files (directory + `_facility.md`) to get the same picture one file gives now.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Trim the Facilities table to one line per site, push narrative to `_facility.md`.** Keep only Client / Site / a short pointer list of card and quote links; move history, folder-tier rationale, and do-not-duplicate warnings into each facility's own `_facility.md` (which already exists for every row). Restores the table's scannability at the cost of one extra hop to read the "why."

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

### For (3) — Tube Geometry header lock

**C. Build `TUBE-GEOM-HEADER` in `vault_lint.py`, modeled directly on `check_durations_header()`.** Anchor on `## Tube Geometry`, canonicalize the 11-column header from `_canonical-heater-card.md`, warn (not error, matching `DURATIONS-HEADER`'s severity) on any deviation. Closes the hand-edit and stale-copy gaps the dead-string guard cannot see.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**D. Leave the dead-string guard as the only protection.** The schema changed 2026-07-27 and has not drifted since; a second lint rule is process for a problem that has not recurred. Revisit only if a hand-edited or stale-copy card actually surfaces a reverted header.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

For (1): Option A's risk is that the directory keeps growing — seven of nine rows already carry multi-sentence cells, and each new facility (three opened 2026-07-27 alone) adds another. Option B's risk is the one the inbox note itself names: this is schema/workflow judgment, not a data fact, and restructuring an index table that "nobody reads as a table" for the sake of a lint metric nobody has complained about may be solving a problem only the linter has. Neither option is reversible for free — B means touching nine `_facility.md` files and the index in one pass.

For (3): Option C's risk is scope-creep into "which canonical tables deserve a header lock," which the inbox note explicitly flags as the bigger unresolved question underneath — building one more one-off rule answers this instance without answering that question, and a third near-identical table showing up later would raise it again. Option D's risk is exactly the gap the inbox note describes: a hand edit or a card copied from a pre-`e4de4a5` template would silently reintroduce the `Notes` column with nothing to catch it until a human notices during review.

## Decision

**Resolved 2026-08-15 (Jesse, in session). (1) A approved, B rejected. (3) C approved, D rejected.**

**On (1) — leave `_directory.md` rich.** Only the linter is complaining. The table is what a session lands on first, and splitting it costs a second file open on every read to recover the "why" one file currently gives. Option B's own risk paragraph names the real objection to itself: restructuring an index nobody reads as a table, to satisfy a width metric nobody has complained about, is solving a problem only the linter has. The growth risk A carries is real but slow, and it is cheaper to revisit at the point the table actually becomes unreadable than to pay B's nine-file restructuring cost now against a hypothetical.

**On (3) — build the lock.** The survey that decided it: all 41 heater cards plus the exemplar and the template carried the identical 11-column header, with no variants and no optional columns. That makes the lock free — it fires on zero existing files, so it is pure drift protection with no backlog to burn down, which is a materially better position than `DURATIONS-HEADER` was in when it was written (that one was locking a drift that had already happened). D's argument that the schema "has not drifted since" is true and is exactly why now is the cheap moment: the lock costs nothing to adopt while everything conforms, and the gap it closes — a card authored from a pre-`e4de4a5` template — gets more likely, not less, as the template ages out of memory.

The scope-creep concern option C's risk paragraph raises ("which canonical tables deserve a header lock") is noted and deliberately not answered here. Two locks is not a pattern demanding a framework; if a third near-identical table appears, that is the moment to generalize, not before.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Both sub-questions ruled and (3) applied. Surveyed every `## Tube Geometry` header in the vault first — 41 cards + exemplar + template, all identical at 11 columns, no variants — which is what made C free to adopt. Added `TUBE_GEOM_HEADER` / `TUBE_GEOM_HEADING_RE` constants and `check_tube_geom_header()` to `tools/vault_lint.py`, modeled on `check_durations_header()` and registered alongside it; warning severity, no optional columns. Shipped with fixture `tools/fixtures/02-facilities/TestClient/Test-City-TX/T-300.md` (carries the pre-`e4de4a5` trailing `Notes` column) per the no-fixture-no-rule contract, and added `TUBE-GEOM-HEADER` to the self-test's expected set. Self-test passes at 15 rules; a real lint pass shows zero TUBE-GEOM-HEADER hits and warnings unchanged at 58. No change to `_directory.md` per (1). | Claude (review queue) |
| 2026-08-02 | Note filed by pre-staging loop from `00-inbox/2026-07-27-over-wide-tables-remainder.md`; confirmed via `_directory.md`, `vault_lint.py`, and `_canonical-heater-card.md` that both sub-questions remain genuinely open and unaddressed by any commit since 2026-07-27. No vault content modified beyond the source marker. | Claude (pre-staging loop) |
