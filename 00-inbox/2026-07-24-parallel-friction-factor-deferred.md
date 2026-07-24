---
type: note
status: inbox
created: 2026-07-24
revisit-trigger: "Actuals rollup carries 3-4 routine multi-pass rows with a recorded Mode -> decide whether the Duration Model gets a mode-friction term — event: check when a multi-pass TA lands actuals"
tags: [inbox, estimating, actuals, duration-model, deferred]
---

# Parallel-friction factor — deliberately left unpriced, revisit when the sample grows

The 2026-07-24 duration-basis ruling settled that 100 ft/hr is a per-pig rate and that a
simultaneous pass set takes one coil's elapsed time. What it did **not** settle is how much
slower a pig runs when several circuits are pigged at once.

The evidence that there is a penalty is real but thin. Two routine multi-pass rows in
[[estimating-actuals-rollup]] normalize to 47 (HF-0012, mode 3) and 52 (F-802, mode 5) ft/hr
per pig, against a routine mode-1 mean near 132. Two clients, same direction, roughly a 60%
degradation. That is a signal, not a model — and both rows carry service and geometry
confounds (12k-ft coker, 14k-ft crude) that the benchmark already derates for separately, so
some of that gap is double-counted fouling rather than parallelism.

**What was decided instead of a number:** the skill now requires any multi-pass estimate to
read those rows and state in the duration math what allowance was applied and why, including
"none". Discipline without false precision.

**Why this is worth returning to.** Claude reached for exactly +25% twice, unprompted, in two
unrelated fixtures (F1 at mode 3, F6 at mode 6). That convergence is a model artifact, not
evidence — but it means estimates will drift toward a factor nobody chose unless a real one
gets set. And the direction of the error is the dangerous one: F6 priced a first-time hard-coke
coker job at an effective 60 ft/hr per pig when F-802, a *milder* routine crude job on the same
client's 2-rig configuration, actually ran 52. Quoting a dirtier job faster than a cleaner one
ran is the wrong way round.

**The trigger:** a third and fourth routine multi-pass row with a recorded `Mode`. Note the
rollup already flags that 3 rows carry an elapsed rate but no Mode — backfilling `Mode` on
those Task Durations rows might reach the threshold without waiting for a new job. Cheapest
first step when this fires.

Related: [[2026-07-22-routine-ftphr-baseline-established]], [[2026-07-22-spec-mode-normalized-rollup]].
