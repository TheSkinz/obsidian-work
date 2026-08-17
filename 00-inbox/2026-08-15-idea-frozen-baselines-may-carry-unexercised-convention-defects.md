---
type: idea-seed
status: researched
created: 2026-08-15
tags: [idea, regression, knowledge-system, tooling]
related:
  - "[[2026-08-07-prestaged-f4-instruction-density-second-fixture]]"
  - "[[2026-08-17-idea-research-frozen-baselines-unexercised-defects]]"
---

# Frozen baselines can carry defects no replay will ever surface

**Gate:** None — researchable now.

On 2026-08-15 the F1 baseline was found to have been billing **two crew trucks hourly** since promotion — 2 × 48 = 96 truck-hours, a $720 over-quote on every replay. It survived four promotions because every replay reproduced it, and it only surfaced when two runs happened to read an ambiguous sentence differently and the diff forced the question to Jesse.

That is a structural blind spot, not bad luck. **A frozen baseline is only tested on the axes where runs disagree.** Where the skill is ambiguous but every run happens to resolve the ambiguity the same way, the baseline freezes one arbitrary reading as truth, and the regression suite actively defends it — a future correct run reads as drift.

## To explore

- How many other conventions in the frozen set are frozen *readings* rather than *rules*? The crew-truck case had a tell: the skill sentence named the item in the singular with no quantity statement. That pattern is greppable — rules that name a countable item without saying how quantity behaves.
- Is there a cheap audit? One pass over each frozen baseline's line-item math asking "which of these numbers is traceable to a stated rule, and which is a reading?" — closer to a checklist than a build.
- Related but distinct, from the same day: F6's diff key 5 was found to be **self-confirming**, because `usadebusk-estimating`'s shift-landing worked example names that fixture and its answer. Recorded in the baseline and deliberately not fixed (Jesse: precision engineering on a line that does not warrant it). But the general question stands — do other skill worked examples name their own fixtures? That is the inverse failure: a diff key that can no longer fail.
- Both failure modes share a root: **the suite cannot see what it was never asked.** Worth thinking about whether anything cheap detects that, or whether it is inherently a human-judgment gap that only surfaces on disagreement.

Cross-cutting — it affects the trustworthiness of every fixture, and the F1 case shows the cost is real money in a proposal rather than an abstract quality point.
