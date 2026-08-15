# Estimating Approach
**Layer:** 01-context — loads every session (thin orientation, not the full method)
**Authority:** The `usadebusk-estimating` skill owns estimating in full — commercial structure, third-party markup, equipment/crew profile, rate-application discipline, and the 14-section proposal composition (intake checklist, section templates, guardrails). Load it for any bid. This file keeps only the duration model — the one piece worth having cold before the skill loads — and does not restate the skill's pricing or section content.

---

## Duration model

Baseline pigging rate: **100 ft/hr per single unlooped coil.** Adjust the rate downward (more hours required) for:
- Coker, crude, or vacuum service — vacuum runs long as a rule (multiple tube sizes, hard coke, and pigging the larger tube sizes from the larger outlet launcher)
- Multiple tube sizes on one coil — each size is pigged to completion in sequence, adding hours
- Pitch presence
- Hard fouling history
- Tight tube ID (under ~3")

**100 ft/hr is a per-pig rate, not a heater-total rate** (ruled 2026-07-24). It describes one pig on one coil. Heater-total footage ÷ 100 is wrong — it double-counts circuits pigged simultaneously and over-quotes every multi-pass job. Elapsed pigging time for a pass set is **one coil's time**, however many circuits that set carries. Round the per-coil figure up to the next whole hour, once, at the coil level. Parallel is not free, but there is no fixed friction factor: check the rollup's multi-pass rows and state what allowance you applied, including "none".

Method: cost one *unlooped* coil (footage ÷ rate) → decide whether coils can/should be looped → lay out pass sets by equipment mode → add rig-overs → sum with rig-in/rig-out. Rig-in tiers (**rig-out matches rig-in**): Small **4** / Moderate **6** / Large **8** / Very large **12** hrs. **Tier from the launcher/receiver connection points, not from the heater** — coil footage and pass count have little to do with rig-in. The tier follows the total hose and hard pipe that physically has to be built, and three drivers set that: connection elevation, run distance from the pumper, and **mode** (pumps utilized, which sets circuit lines and therefore hose count). They **multiply — a low reading on one does not offset a high one**. Elevation and distance settle at the job walk; mode is known at bid time from the equipment plan, so price from mode where no walk has happened. **12 hrs is a ceiling, not a rung reached by accumulation**, and the ~2 hr pipefitter-wait adder stacks *inside* it (Very large + fitter wait = 12, not 14). The skill carries the hose-count figures behind the tiers. Rig-over between pass sets = `ceil(passes ÷ mode) − 1` (mode = passes cleaned per set: double 2, triple 3), ~1 hr when launchers/receivers are pre-installed on the added passes, ~2 hr when waiting on fitters to install them. Smart Pig 4 hrs when applicable. All tasks run a 12-hr shift cycle; pigging runs 24/7.

**Before finalizing any duration, check `04-knowledge/estimating-actuals-rollup.md`** — the generated cross-heater table of every recorded actual against these benchmarks. Reference, not authority (benchmark changes are Jesse's call), but an estimate that ignores a contradicting actual is a bug. An actual only governs when coil condition matches — a crash/emergency decoke runs dirtier than routine, so don't apply one mode's ft/hr to the other. Never assume tube footage or pass count; derive from provided data.
