---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-28
review_after: 2026-08-28
revisit-trigger: "Next time `_canonical-heater-card.md` is opened for a change carrying its own weight -> decide the structured per-coilset actuals sub-table, bundled with the parked Pig Specifications Condition column (parked 2026-07-29) — event: check at heater-card schema change"
related:
  - "[[idea-rollup-per-rig-coilset-grain]]"
  - "[[idea-pig-actuals-maturation]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, estimating, schema, actuals]
---

# Idea Research — Re-grain the Actuals Rollup to One Row per Rig-Coilset

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Two `unexplored` idea-seeds existed:
`idea-rollup-per-rig-coilset-grain` (created 2026-07-25) and `idea-vault-stats-layer` (created
2026-07-26). The former is older and was processed. The seed's own **Gate:** line reads "None
— researchable now," so this is case (b): proceed to research directly, no gate check needed.

## Evidence

**1. The seed's own open question 3 — does the per-coilset split live in structured data or only
in prose? — is answered directly, and the answer is prose, by deliberate schema design, not
oversight.** `04-knowledge/_canonical-heater-card.md` (lines 209–221) states the Task Durations
table is "one row per job... per-rig split stays in Field Notes, never averaged into this table,"
and the template's Field Notes subsection (line 272) carries a freeform
`**Per-rig split (multi-Trimax only):**` field with no fixed structure. This is a conscious
information-architecture decision already baked into the schema, not a gap that happened by
accident.

**2. The two cards the seed cites as having clean splits do not even agree with each other on
what "the split" contains, confirming a parser would be brittle.** `02-facilities/Syncrude/
Fort-McMurray-AB/7-1-F-1.md` (lines 138–147) gives a full per-coilset, per-task-column
breakdown for CND25004: "Trimax 5 (coils 2/3/4, triple mode) = 6 rig-in / 48 pig / 6 smart /
3 rig-out = 63; Trimax 6 (coils 5/6/7, triple mode) = 6 / 35 / 4 / 3 = 48; Trimax 6 (coils 1 & 8)
= 2 / 36 / 8 / 7 = 53." `02-facilities/CHS/McPherson-KS/HF-0011.md` (lines 117–121), by contrast,
gives only an hours-by-mode split with no coilset or footage mapping at all: "the 96 pig hours
mix modes (62 triple + 34 double)" — no per-pass or per-coilset figures exist anywhere in that
card. Even the ingest skill's own template example (`~/.claude/skills/usadebusk-vault-ingest/
SKILL.md` line 343) is coarser still: `Trimax 4 = 136 hrs, Trimax 6 = 132 hrs` — a per-rig total,
not a per-coilset, per-task breakdown. Three different levels of detail across three sources
that are all supposedly the same field.

**3. Item 1 of the seed ("does the 62/34 split map to specific passes and footage?") is not
settleable from files — it is missing data, not an unmade decision.** HF-0011's Task Durations
row note and Field Notes contain the mode-hours split and nothing else; no per-coilset footage
or pass mapping exists anywhere in that card to check against. The seed frames this as "needs
Jesse first," which is correct, but the file evidence goes one step further: Jesse would be
supplying new data (from the underlying ticket breakdown/receipts, if a pass-level footage
breakdown exists there) rather than confirming an existing one.

**4. External research confirms both halves of this independently.** Re-graining a job-costing
rollup from job-level to equipment/work-unit level is standard, well-established practice —
activity-based costing assigns "every cost directly to the task or sub-task that incurred it,"
which is exactly what the seed proposes. Separately, extracting structured fields from short,
abbreviation-heavy maintenance narrative text is a recognized hard NLP subproblem: dedicated
research systems built for this exact text type (maintenance work-order narratives) report low
recall even with purpose-built named-entity extraction, per current literature (MaintIE,
OMIn/"Trusted Knowledge Extraction for O&M Intelligence"). Point 2's evidence — three sources
disagreeing on format — is the same failure mode that literature describes, seen firsthand in
this vault's own two cards.

**5. Vault-internal precedent already states the fix.** This is the same pattern the vault's
own working history has already hit and resolved elsewhere: capture the structured field at the
point of ingest (when parsing the source job report's own tables, which are themselves
structured in the PDF, per 7-1-F-1's Field Notes) rather than retrofitting a parser onto
already-committed, inconsistently-phrased prose. `idea-pig-actuals-maturation` (closed
2026-07-26) hit the identical fork one field over — a Condition column deferred as "ride along
the next time the card schema is opened for a reason carrying its own weight" — and this seed's
schema question is the same kind of change to the same table family.

## Interpretation

**Sound idea, premature to build.** The concept — re-grain the rollup to expose the clean
per-rig-coilset measurements that already exist inside two job reports — is directionally
correct and matches standard job-costing practice (point 4). But it is blocked on a Lane 4
schema decision that has not been made: today's canonical schema deliberately keeps per-rig
splits as unstructured prose, and the two example cards prove that prose is inconsistent
card-to-card (points 1–2), so a script cannot safely re-grain what does not yet exist as
structured data. This is not "premature — wait for more data" the way the pig-actuals seed's
ft-per-pig rollup was; it is "premature — the schema change and the ingest-time capture point
haven't been decided," and building a prose parser to bridge that gap would recreate a known
NLP failure mode rather than solve it (point 4). Items 1 and 2 in the seed are correctly flagged
as needing Jesse, and file evidence shows item 1 specifically may need new data, not just a
decision.

## Recommended Action

**Park as a bundled Lane 4 schema proposal, not a script task.** Concretely, if Jesse wants to
proceed: (a) decide whether to add a structured per-coilset actuals sub-table to
`_canonical-heater-card.md` (e.g. Job #, Rig, Coils, Mode, Rig-In, Pig, Smart Pig, Rig-Out,
Footage) rather than asking a script to parse Field Notes prose; (b) if approved, capture new
splits as structured data going forward at `usadebusk-vault-ingest` time, when the source job
report's own duration tables are still structured — not as a later re-parse; (c) hand-migrate
only the small number of cards that already carry a usable prose split (7-1-F-1's two rows;
HF-0011 stays blended per point 3 until Jesse supplies or rules out a footage mapping) rather
than writing a parser for two data points; (d) bundle this decision with the still-parked Pig
Specifications `Condition` column from `idea-pig-actuals-maturation`, since both are riding the
same "next time the schema is opened for a reason carrying its own weight" trigger. Separately
and not gating the schema decision: Jesse's read on whether the Syncrude ~6 ft/hr figure (item 2)
includes fill/flush time before it enters any service-class benchmark.

## Decision

- [ ] Approved — add structured per-coilset actuals table to canonical schema (Lane 4), bundle with Condition-column change
- [ ] Approved with edits
- [x] **Park — revisit next time the card schema is opened for another reason** — Jesse, 2026-07-29
- [ ] Drop

**Why parked rather than built.** The blocker is an undecided Lane 4 schema change, not thin data.
The canonical card deliberately holds per-rig splits as freeform Field Notes prose, and the three
sources that carry that field disagree on what it contains — 7-1-F-1 has a full per-coilset
per-task breakdown, HF-0011 has hours-by-mode with no coilset or footage mapping, the ingest
skill's example has only a per-rig total. Writing a parser across that recreates a documented
maintenance-narrative extraction failure mode for two usable data points. When the schema is next
opened for a reason that earns it, decide the structured sub-table and capture at ingest time
going forward; hand-migrate 7-1-F-1 only. Bundled with the Pig Specifications `Condition` column
from `idea-pig-actuals-maturation`, which rides the same trigger.

**Separately, and not gating any of the above:** Jesse's read on whether the Syncrude ~6 ft/hr
figure includes fill/flush time is still needed before that figure enters any service-class
benchmark. Filed to `00-inbox/`.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-29 | Parked to the heater-card schema trigger; bundled with the Condition-column change | Jesse (ruling) / Claude (Opus 5) | Walked through in session. No schema or script change made. Syncrude fill/flush question split out to `00-inbox/`. |
