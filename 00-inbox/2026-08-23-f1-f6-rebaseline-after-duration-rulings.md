---
type: note
status: inbox
created: 2026-08-23
revisit-trigger: "Before the next regression battery, or before trusting an f1/f6 diff — both fixtures encode rules struck 2026-08-23"
tags: [inbox, regression, estimating, duration-model]
---

# f1 and f6 baselines are invalidated by the 2026-08-23 duration rulings — re-cut required

**What happened.** Four Lane 4 rulings on 2026-08-23 (config commit `5d38984`, vault `6f10370`) struck the **25–40% parallel-friction allowance** and the **whole-shift landing**, gated the **rate derate**, and changed **coil rounding to nearest-even**. Two rules were added: the **pre-inspection task allowance** for already-decoked coils, and the **reduced rig-in on subsequent heaters** of one mobilization.

**Why the baselines are dead.** `~/.claude/regression/frozen/f1-proposal-output.md` and `f6-duration-mobdemob-output.md` both encode the struck rules in their duration math — f6 in particular exists to exercise the duration model, and its promoted run explicitly stated a parallel-friction allowance *because the rule then required it*. Every number downstream of pigging hours in both fixtures is now wrong against the amended skill.

**Do NOT hand-patch them.** The standing rule from the 2026-07-24 battery is that re-authoring a baseline's figures makes the arithmetic the reviewer's and destroys the record of raw model behaviour. Replay both fixtures against the amended skill, judge the runs, and re-promote from passing runs.

**Expect the diffs to be large.** On the live case that produced these rulings, the pre-correction skill gave **168 project hours against Jesse's 94**. A replay that comes back much shorter than the old baseline is the change landing, not a regression.

**Better fixture available.** [[DSP26100]] (Valero Three Rivers, three heaters, sent 2026-08-22) is a **real** estimate with Jesse's own hours and a finished workup behind it, where f1 and f6 are synthetic. It already verifies: the amended path reproduces **H-1102 exactly** (`1,775 ÷ 100 = 17.75 → 18`, total 30) and **100-H-2 within 2 hrs** (26 v Jesse's shaved 24). 100-H-1 is not a genuine test — its 8-hr allowance is now written into the skill and returns by construction. **Worth considering whether DSP#26100 should replace or supplement f6 as the duration fixture.**

**Also unresolved from that session:** SteadyFlux's *"Onsite support (24 hours) — Included"* against the 16 smart-pig support hours quoted across three heaters. If it means 24 hrs of USADebusk pumping per heater that is 60 hours and roughly $24,000 unpriced on a sent quote. Tracked on [[DSP26100]]'s open items; it is Jesse's call to raise with SteadyFlux, not a vault task.

Related: [[2026-07-24-parallel-friction-factor-deferred]] — the note that called the band's evidence confounded four days before the band was written, now marked resolved.
