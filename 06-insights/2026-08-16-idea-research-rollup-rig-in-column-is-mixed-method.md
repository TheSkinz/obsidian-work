---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-16
review_after: 2026-09-16
related:
  - "[[2026-08-15-idea-rollup-rig-in-column-is-mixed-method]]"
  - "[[estimating-actuals-rollup]]"
  - "[[idea-rollup-per-rig-coilset-grain]]"
tags: [review, knowledge-system, idea-research, estimating, rollup, data-quality]
---

# Idea Research — The Actuals Rollup's Rig-In Column Is Mixed-Method

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-16. Four `unexplored` idea-seeds
existed, all created 2026-08-15 (tied on frontmatter date); ordered by file mtime/commit time
this seed (`idea-rollup-rig-in-column-is-mixed-method`, committed 2026-08-15 18:45:27) was
oldest. Its `**Gate:**` line reads "None — researchable now," so this is case (b): proceed to
research directly, no gate check needed.

## Evidence

**1. The skill-level rule the seed cites is confirmed current.** `usadebusk-estimating/SKILL.md`
(2026-08-15 entries): "Rig-in never exceeds 12 hours, and rarely exceeds 8" and "Do not spend
estimating effort on rig-in precision... It is a coarse six-value selector" (values 2/4/6/8/10/12).
The rollup's own 8-rows-above-12 anomaly the seed flags is real and matches the current table in
`04-knowledge/estimating-actuals-rollup.md` (16, 16, 22, 14, 14, 14, 27*, 34.5*).

**2. Spot-checking the two asterisked outliers shows the mixing is real but not the mechanism the
seed names.** `02-facilities/Valero/Port-Arthur-TX/H-102A.md` and `H-102B.md` carry footnotes on
their 27* and 34.5* rows: "Source job report gives a single combined 'Rigging' figure... that
bundles rig-in, rig-out, and rig-over rather than breaking them out... Matches the QB Ticket
Breakdown billed hours exactly." These are USADebusk's own billed actuals, not another salesman's
quoted figure — the contamination here is *task bundling* (three tasks' hours collapsed into the
Rig-In cell), not cross-source provenance. Both rows already carry visible `*` markers and an
inline explanation, so this specific failure mode is already surfaced, just not machine-readable
(the rollup script doesn't propagate the asterisk or footnote into its own table).

**3. Spot-checking a non-asterisked outlier undercuts the seed's headline mechanism further.**
`HF-009A.md` / `HF-009B.md` (rig-in = 16, no asterisk) carry a Notes-table entry: "**Quoted
basis:** 6 rig-in · 32 decoking · 4 smart pig · 6 rig-out = 48 hrs for both heaters together" —
i.e. the *quote* was 6, and the Task Durations table's 16 is the recorded actual that overran it.
This is not a case of another salesman's quoted number being passed off as an actual; it is a
real (if surprising) USADebusk actual that happens to exceed both the 12-hr ceiling and the
quoted basis. Two of the seed's implied "contaminated" rows, checked directly, turn out to be
genuine — if heterogeneous — actuals rather than quote-as-measurement substitutions.

**4. The seed's framing ("other salesmen's own method for determining rig-in") is Jesse's verbal
framing from the 2026-08-15 session, not yet verified against a specific row.** No file found in
`02-facilities/` or `06-insights/` names a specific row as sourced from another salesman's quote
rather than a USADebusk-executed job. The two anomaly types actually documented in the cards
(bundled-task figures per point 2, and quote-vs-actual overrun per point 3) are both legitimate
provenance problems worth flagging, but neither is the specific "other salesman's method" case
the seed's prose describes. Whether that third case exists in the table is unresolved — it would
need Jesse to identify which specific rows (if any) came from a quote rather than an executed
job's paperwork.

**5. Vault-internal precedent: the sibling seed processed 2026-07-28 hit the identical
information-architecture fork one field over.** `06-insights/2026-07-28-idea-research-
rollup-per-rig-coilset-grain.md` found that per-rig-coilset detail lives only in freeform Field
Notes prose by deliberate schema design, and recommended capturing structure at ingest time
rather than retrofitting a parser onto already-committed prose (citing the same "recreates a
documented maintenance-narrative extraction failure mode" reasoning applicable here). That
seed's Decision was "Park — revisit next time the card schema is opened for another reason,"
bundled with a `Condition`-column addition. This rig-in seed is schema-adjacent in the same way:
the fix requires either a new column/marker or richer per-row provenance capture, not a pure
script change to the existing table shape.

**6. External research confirms the standard fix pattern.** General data-quality practice is to
carry a *separate qualifier/flag column* for provenance or measurement-quality distinctions
rather than folding a caveat into a shared narrative paragraph — "a separate column should be
used for data qualifiers, descriptions, and flags, otherwise there is the potential for problems
to develop during analyses" (Dataversity, data quality metrics best practices), and quality-flag
conventions commonly use small coded values (e.g. 0/-1/1 for unexamined/problem/good) attached
per-row rather than table-wide. This matches what H-102A/B already do informally (inline `*` +
footnote) — the gap is that the convention exists in exactly two rows and isn't propagated by
`tools/estimating_rollup.py` into the generated table, so a reader of the rollup alone (rather
than the source card) doesn't see it.

Sources: [Data Quality Metrics Best Practices](https://www.dataversity.net/articles/data-quality-metrics-best-practices/), [How to Make a Data Quality Dashboard? Examples and Best Practices](https://dqops.com/how-to-make-a-data-quality-dashboard/)

## Interpretation

**Partially sound, partially premature — and the seed's own headline claim needs revision before
any fix is built.** The observable problem (Rig-In column rendered as if uniform measurement,
when it visibly is not) is real and confirmed by point 1. But the *cause* the seed names —
contamination by other salesmen's quoting method — is not what the two checked anomalies turn out
to be (points 2–3); both are genuine USADebusk actuals with their own, different provenance
wrinkles (task-bundling, quote-overrun). This matters because the fix a reader would reach for
under the seed's stated cause (mark rows as "quote" vs "actual") would not address what's
actually in the two rows checked (mark rows as "combined-task figure" vs "clean single-task
figure"). A machine-readable version of the fix should encode *what kind* of number each cell is
(clean measurement / bundled-task figure / actual-exceeds-quote / unknown), not a binary
quote-vs-actual flag, and that taxonomy isn't fully known without Jesse auditing the remaining
six unchecked outlier rows (16 HF-009A/B already checked; 22, 14, 14, 14 unchecked). Point 4's gap
is not settleable from files — whether any row is literally a different salesman's number is a
question only Jesse can answer.

## Recommended Action

**Bounded one-shot investigation, not a build.** Concretely: (a) Jesse reviews the remaining
unchecked rig-in outliers (H-20 = 22, H-28/H-29 = 14/14 both from 24012, 01-BA-105 = 10.5) and
classifies each as clean-actual / bundled-task-figure / quote-derived / unknown — this is a
15-minute pass against source job reports, not new research; (b) once the taxonomy is known,
extend the existing `*`-footnote convention (already used in H-102A/B) into a proper per-row
qualifier that `tools/estimating_rollup.py` can read and surface as its own column or inline tag,
rather than leaving it invisible outside the source card; (c) bundle this with the still-parked
per-rig-coilset schema decision from `idea-rollup-per-rig-coilset-grain` (point 5) since both are
"next time the Task Durations schema is opened" changes touching the same table family — a
second bundled schema opening is lower-risk than two separate ones. Do not build a script-only
fix (e.g. silently excluding rig-in from benchmark comparison) without step (a); that would treat
an unverified guess as fact, which is the same trap the seed itself is flagging one level up.

## Decision

- [ ] Approved — Jesse classifies remaining outlier rows, then extend the footnote convention into a rollup-visible qualifier (bundle with per-rig-coilset schema change)
- [ ] Approved with edits
- [x] Park — revisit next time the Task Durations schema is opened for another reason — **ruled 2026-08-21.** Not queued separately: this note's ask *is* part of the per-coilset schema bundle already open as **DQ-017**, and a second row for a subset of one decision is how the queue stopped being "the single place every open decision lives." Folded into DQ-017's ask instead.
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-21 | Folded into DQ-017 rather than queued separately. | Claude | The ask is a subset of the per-coilset schema bundle already open as DQ-017. A second row for part of one decision is the pattern that made the queue's charter false. |
|  |  |  |  |
