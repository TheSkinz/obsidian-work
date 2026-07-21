# Estimating Approach
**Layer:** 01-context — loads every session (thin orientation, not the full method)
**Authority:** The `usadebusk-estimating` skill owns estimating in full — commercial structure, third-party markup, equipment/crew profile, rate-application discipline, and the 14-section proposal composition (intake checklist, section templates, guardrails). Load it for any bid. This file keeps only the duration model — the one piece worth having cold before the skill loads — and does not restate the skill's pricing or section content.

---

## Duration model

Baseline pigging rate: **100 ft/hr per pass.** Adjust the rate downward (more hours required) for:
- Coker or crude service
- Pitch presence
- Hard fouling history
- Tight tube ID (under ~3")

Standard fixed durations: Rig-in 6 hrs, Rig-out 6 hrs, Smart Pig 4 hrs (when applicable). All tasks run a 12-hr shift cycle; pigging runs 24/7.

**Before finalizing any duration, check `04-knowledge/estimating-actuals-rollup.md`** — the generated cross-heater table of every recorded actual against these benchmarks. Reference, not authority (benchmark changes are Jesse's call), but an estimate that ignores a contradicting actual is a bug. An actual only governs when coil condition matches — a crash/emergency decoke runs dirtier than routine, so don't apply one mode's ft/hr to the other. Never assume tube footage or pass count; derive from provided data.
