---
type: idea-seed
status: unexplored
created: 2026-07-25
tags: [idea, vault-system, future, estimating, schema]
---

# Maturing pig actuals — the Condition column and the ft-per-pig rollup

Idea seed captured 2026-07-25 for a future session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** As of 2026-07-25 the pig-actuals write-back exists (config `950f7a0`): `usadebusk-vault-ingest` fills a heater card's `## Pig Specifications` from the job report's PIGS USED table, and `usadebusk-estimating` step 1 reads a `USA#####`/`DSP#####` actuals wall off the `Source` column. Two follow-ons were deliberately deferred at the time, both waiting on data rather than on a decision being hard.

The first is a **`Condition` column on Pig Specifications**. A crashed furnace consumes more pigs than routine service for the same reason it pigs slower, so the condition-match rule that already governs Task Durations should extend to pigs. This was held because it is a Lane 4 schema change to `04-knowledge/_canonical-heater-card.md` (and therefore `templates/_heater-template.md`), and because with no counts yet in the table there was nothing for a condition tag to discriminate between. The recommendation recorded at the time was to let it ride along the next time the card schema is opened for a reason carrying its own weight, rather than as a standalone change.

The second is a **ft-per-pig rollup**, the pig equivalent of `tools/estimating_rollup.py` → `04-knowledge/estimating-actuals-rollup.md`. It would turn estimating's step 2 (scale off coil footage) from intuition into a rate segmented by bore size and condition. Not built because the vault holds exactly one usable data point — HF-0012 at ~180 pigs over 12,036 ft, roughly one pig per 67 ft — and a formula off one point is a formula pretending to be evidence.

**To explore:** the trigger is data volume, so the first question is when to look again — the rough figure discussed was three or four heaters carrying real counts, which will accumulate on their own now that ingest writes them. Then: does the ft-per-pig ratio actually hold across bore sizes, or does a 4" coil consume proportionally more or fewer pigs per foot than a 6"? Does condition move it as much as it moves duration? Is a rollup script warranted at all, or does a handful of rows read directly off the cards do the same job without another generated artifact to maintain? And the honest prior question: pig cost ran about 6% of the F1 quote on a line that trues up at invoice, so establish that tightening it clears the ROI bar before building anything.

Background on why the method is deliberately crude, and the two-consumer split between the estimate's 1/4" cost granularity and the field pig load list's 1/8" increments, is in `usadebusk-estimating` under Pig Quantity Estimating. Related: [[idea-orphaned-equipment-rules-proposal-path]].
