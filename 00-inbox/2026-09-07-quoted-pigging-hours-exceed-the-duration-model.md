---
title: Quoted pigging hours run above what the duration model produces — unreconciled
created: 2026-09-07
status: open
type: idea-seed
tags: [estimating, duration-model, grok-bot, parked]
---

# Real quotes carry more pigging hours than the documented model gives

**Found while building a blind test fixture, parked before it was resolved.** The Grok Bot Estimator
was to be graded against DSP26080 (HF Sinclair Navajo, three heaters, February 2027 outage). Working
the fixture required knowing the right answer, and the right answer did not come out of the model.

| Heater | Pig path per the card | Model gives | Quote carries |
|---|---|---|---|
| H-2421 | ~980–1,000 ft, two circuits looped by field jumper into one continuous path | ~10 hrs | **12** |
| H-30 | 4 passes × 443 ft, not looped | ~10 hrs incl. rig-over | **12** |
| H-2501 | 6 passes × ~1,028 ft, not looped, mixed 6″/4″ radiant bore | ~22 hrs incl. rig-over | **48** |

**H-2421's 12 hrs is corroborated, not a one-off.** [[DSP26092]] quoted the same heater at *"rig-in
6 / pig 12 / smart pig 4 / rig-out 6, double mode"* and was won; [[DSP26080]] quotes 12 again. Two
independent quotes, same figure.

**The derate gate is shut on all three.** Every one has an empty Task Durations table — no actuals,
no recorded fouling history — so `estimating-approach.md` says a first-time unknown heater takes the
round 100 ft/hr. The gap is therefore not a derate that the rule permits.

**H-2501 is the one that matters.** 48 against ~22 is more than double, which is too large to be
rounding, shift packaging, or a mode assumption. Jesse's read (2026-09-07) is that the numbers **are
derived** and something in the geometry accounts for it.

## Ruled out by arithmetic, so the answer is elsewhere

Shift packaging alone (12/12/48 are all multiples of 12, but it does not explain H-2501's size).
Equipment mode (no single mode reconciles the three against each other). A multi-pig progression
(that multiplies cleanly, and 12 ÷ 10 = 1.2 is not a pig count).

## Candidates, none confirmed

Whether the pigging line covers more than pig travel — setup, pig changes, dewatering, flow tests
between passes. Whether these coils carry a known slow service that opens the derate without an
actual on the card. Whether one Trimax is mode-limited on these heaters so passes do not parallelise
as assumed. Whether H-2501's **mixed 6″/4″ radiant bore** forces a longer progression than a
single-bore coil — the actuals rollup already notes the routine spread is service-shaped, with
multi-bore coils at the slow end.

## Why this outlives the Grok Bot test

**A session following the documented method lands roughly 30% low on H-2501.** That is a gap between
the written method and the practised one, and it sits in `01-context/estimating-approach.md`, in the
`usadebusk-estimating` skill, and now in the ported Grok Bot Duration Model skill — three places.

**Parked, not dropped** (Jesse, 2026-09-07): bids are rarely built in Claude Code and no finalized
bid has ever been produced there, so the estimating workflow is not mature enough to hand to a Bot
and the test was measuring something premature. The arithmetic question stands on its own and is
worth answering the next time a bid is actually worked.
