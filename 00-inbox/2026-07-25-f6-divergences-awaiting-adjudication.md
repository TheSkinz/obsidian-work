---
type: note
status: open
created: 2026-07-25
tags: [inbox, regression, estimating, awaiting-decision]
---

# F6 replay — two divergences awaiting Jesse's call

F6 was replayed 2026-07-25 after the estimating change `bb78eb8`, because it is the other estimating fixture and its job data (2× TriMax against 1 filter press) is the exact configuration the rewritten `:111` paragraph governs. The change itself verified clean — nine of ten diff keys held and the corrected press paragraph was adopted near-verbatim. Frozen was **not** re-cut. Run at `~/.claude/regression/runs/claude-opus-5/f6-duration-mobdemob-2026-07-25.md`; record in config commit `2eebec6`.

Two divergences remain open. Neither was caused by the change, and both are numbers, which is what the suite says needs your eye rather than an agent's.

**1. Rig tier — 8 hrs against frozen's 6.** The run tiered the heater Large rather than Moderate, reasoning from heater design: a six-pass coker charge heater at 5,400 ft with a two-rig spread and a long hard-pipe run to reach six launcher positions. It named a job walk as governing and worth 4 hrs if it pulls the tier back. The skill genuinely leaves the tier to judgment, so this is not a rule violation — but rig-out matches rig-in, so the call moves 4 hours at each end. Question: is Large right for that heater shape, or is Moderate the correct default until a job walk says otherwise?

**2. Non-driver travel rate — $64.00 against frozen's $58.00.** This is a defect in the fixture, not in either run. The F6 replay prompt says "Use baseline rates" while the job data states non-driver travel bills at the operator rate of $64.00/hr, and the skill's precedence rule says a rate stated by the governing contract or bid instructions governs whatever figure it carries — including one that happens to equal a role rate. Frozen read the prompt as controlling; this run read the skill as controlling. Both defensible. Worth $72 across mob and demob, so the money is irrelevant; the problem is that the ambiguity will regenerate this diff on every future replay. Fix is to reword the fixture so it tests one reading or the other deliberately.

Item 2 is cheap and worth doing whatever you decide on item 1.
