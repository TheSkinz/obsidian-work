---
type: idea-seed
status: researched
created: 2026-08-15
tags: [idea, estimating, actuals, rollup, data-quality]
related:
  - "[[estimating-actuals-rollup]]"
  - "[[2026-08-16-idea-research-rollup-rig-in-column-is-mixed-method]]"
---

# The actuals rollup presents a mixed-method column as if it were measurement

**Gate:** None — researchable now.

Jesse, 2026-08-15: *"The problem with some of the durations in the vault is that it includes other salesmen's quotes who have their own method for determining rig-in durations."*

The rule that came out of that is now in `usadebusk-estimating` — vault rig-in actuals are not a calibration basis, do not average or fit them. What is **not** solved is that `04-knowledge/estimating-actuals-rollup.md` still renders the Rig-In column identically to every other column, with no visible marker that it is a different kind of number.

The column spans **2 to 34.5 hours**, with eight rows above the 12-hr cap (16, 16, 22, 14, 14, 14, 27\*, 34.5\*) and many odd values that Jesse's own method could never produce, since his rig-in is always one of 2/4/6/8/10/12. Anyone reading the table cold — human or agent — sees a measurement series.

## To explore

- Should the generating script (`tools/estimating_rollup.py`) annotate the Rig-In column, or drop it from the benchmark comparison entirely while keeping it in the per-row detail?
- Is provenance recoverable per row at all? Some rows presumably came from USADebusk-executed job paperwork and some from other salesmen's quoted figures — if the source is knowable, a provenance marker is better than a blanket caveat. If it is not knowable, the blanket caveat is the honest ceiling.
- Does the same mixing affect any other column? The caution was scoped to rig-in deliberately, and the pigging columns are explicitly still a valid cross-check on condition- and mode-matched rows — but that scoping was Jesse's judgment in the moment, not an audit.
- Knock-on: F6's `rigout_risk_note` leans on F-802 running "rig-in 4 against rig-out 20," a 5x miss on the mirror rule. If that rig-in 4 is another salesman's quoted figure, the multiple compares a quote against an actual and is not a measurement. Already caveated in the frozen baseline, but the underlying row is unresolved.

Low urgency — no live bid depends on it. Genuinely cross-cutting though: it touches every duration estimate that consults the rollup.
