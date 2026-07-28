<!-- vault-loop: operational — estimating regression fixture divergences awaiting Jesse's call, Lane 4 (04-knowledge, usadebusk-estimating scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: note
status: open
created: 2026-07-25
tags: [inbox, regression, estimating, awaiting-decision]
---

# F6 replay — two divergences awaiting Jesse's call

F6 was replayed 2026-07-25 after the estimating change `bb78eb8`, because it is the other estimating fixture and its job data (2× Trimax against 1 filter press) is the exact configuration the rewritten `:111` paragraph governs. The change itself verified clean — nine of ten diff keys held and the corrected press paragraph was adopted near-verbatim. Frozen was **not** re-cut. Run at `~/.claude/regression/runs/claude-opus-5/f6-duration-mobdemob-2026-07-25.md`; record in config commit `2eebec6`.

Two divergences remain open. Neither was caused by the change, and both are numbers, which is what the suite says needs your eye rather than an agent's.

**RESOLVED IN PART 2026-07-25 — the question was wrong, and the answer replaced the rule.** Jesse: rig tier has almost nothing to do with coil footage or pass count. It is set by **where the launcher/receiver connections are** — their elevation above grade, and the run distance from the Trimax pumper to them. Connections on the bottom deck of the radiant section at ~8 ft are a walk-up; connections 60 ft up mean a crane to hang hard pipe and hoses plus roughly that much added pipe and hose. Both are settled at the job walk. A **~2 hr adder** applies where USADebusk will be waiting on the customer's pipefitters to hang the launchers — known in advance on some heaters, a real recurring cost rather than a contingency. Written into `usadebusk-estimating` (config `98ac964`); the Small/Moderate/Large/Very-large hours survive only as an explicit no-job-walk fallback, not as a heater-size lookup. Item 2 below is also fixed — the fixture now says a job-stated rate governs, and the replay returned Mob and Demob at **$3,774.00** each, which frozen's own frontmatter already names as the correct figure.

**STILL OPEN — two sub-rules, worth 2 hrs.** Jesse's figure for that heater shape is **rig-in 12**; the replay derived 10 (Large 8 + 2 fitter wait). The gap localizes to two things the new wording does not say. First, **does the pipefitter adder stack on top of the tier, or is waiting on fitters one of the conditions that pushes the tier itself up a step?** The run stacked it. If it is the latter, the heater is Very large 12 and the adder is already inside — which lands exactly on Jesse's number. Second, **does rig-out mirror the tier, or the tier plus adders?** The run mirrored tier only, giving rig-in 10 against rig-out 8, which quietly breaks "rig-out matches rig-in" without saying so; its reasoning is defensible (USADebusk pulls its own pipe on the way out, the fitters remove their own launchers) but it is unwritten, so it will drift again. F6's frozen was **not** re-cut and still carries 6/6 and the known-wrong $3,738.

*(original)* **1. Rig tier — 8 hrs against frozen's 6.** The run tiered the heater Large rather than Moderate, reasoning from heater design: a six-pass coker charge heater at 5,400 ft with a two-rig spread and a long hard-pipe run to reach six launcher positions. It named a job walk as governing and worth 4 hrs if it pulls the tier back. The skill genuinely leaves the tier to judgment, so this is not a rule violation — but rig-out matches rig-in, so the call moves 4 hours at each end. Question: is Large right for that heater shape, or is Moderate the correct default until a job walk says otherwise?

**2. Non-driver travel rate — $64.00 against frozen's $58.00.** This is a defect in the fixture, not in either run. The F6 replay prompt says "Use baseline rates" while the job data states non-driver travel bills at the operator rate of $64.00/hr, and the skill's precedence rule says a rate stated by the governing contract or bid instructions governs whatever figure it carries — including one that happens to equal a role rate. Frozen read the prompt as controlling; this run read the skill as controlling. Both defensible. Worth $72 across mob and demob, so the money is irrelevant; the problem is that the ambiguity will regenerate this diff on every future replay. Fix is to reword the fixture so it tests one reading or the other deliberately.

Item 2 is cheap and worth doing whatever you decide on item 1.
