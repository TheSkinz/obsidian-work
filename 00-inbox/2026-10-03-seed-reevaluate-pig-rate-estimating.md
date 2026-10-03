---
type: idea-seed
status: unexplored
created: 2026-10-03
tags: [idea, estimating, future]
---

# Re-evaluate how the pig line is estimated

<!-- vault-loop: Lane 4 (estimating method). Needs Jesse's call; do not self-route. -->

Idea seed captured 2026-10-03 for a future discussion session. The read below is tentative, so confirm intent with Jesse before designing anything.

**Tentative read:** A prompt-audit on 2026-10-03 found that the worked example in `usadebusk-estimating` uses 80 ft/hr while stating "derate gate not met", which contradicts its own gate (gate not met means the 100 ft/hr benchmark applies). Jesse's response was broader than the example. He has historically used 100 ft/hr as a default, but several factors move the real rate, and he is not always privy to them. He uses the skill infrequently and is unsure whether the estimating method itself should be re-evaluated. He deferred the question to another session.

**To explore:** Which rate-moving factors he actually knows at bid time and which he does not. Whether the gated-derate structure still fits how he estimates. Whether the worked example should be fixed now or wait on the method decision. The rollup's routine mean (about 99 ft/hr, spread 47–259) is relevant evidence. A second prompt-audit pass on 2026-10-03 also found that the skill hard-codes that figure as a dated snapshot ("As of 2026-07-22… five routine mode-normalized rates… mean ≈99", `usadebusk-estimating` around line 133). Whatever the method becomes, the skill should point at `04-knowledge/estimating-actuals-rollup.md` rather than carry a number frozen in July.
