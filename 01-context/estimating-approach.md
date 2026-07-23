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

Method: cost one *unlooped* coil (footage ÷ rate) → decide whether coils can/should be looped → lay out pass sets by equipment mode → add rig-overs → sum with rig-in/rig-out. Rig-in tiers (**rig-out matches rig-in**): Small **4** / Moderate **6** / Large **8** / Very large **12** hrs, set by heater size/height and the hard-pipe run to reach the launchers (read at the job walk). Rig-over between pass sets = `ceil(passes ÷ mode) − 1` (mode = passes cleaned per set: double 2, triple 3), ~1 hr when launchers/receivers are pre-installed on the added passes, ~2 hr when waiting on fitters to install them. Smart Pig 4 hrs when applicable. All tasks run a 12-hr shift cycle; pigging runs 24/7.

**Before finalizing any duration, check `04-knowledge/estimating-actuals-rollup.md`** — the generated cross-heater table of every recorded actual against these benchmarks. Reference, not authority (benchmark changes are Jesse's call), but an estimate that ignores a contradicting actual is a bug. An actual only governs when coil condition matches — a crash/emergency decoke runs dirtier than routine, so don't apply one mode's ft/hr to the other. Never assume tube footage or pass count; derive from provided data.
