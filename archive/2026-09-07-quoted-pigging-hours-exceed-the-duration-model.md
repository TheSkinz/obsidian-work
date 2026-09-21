---
title: Quoted pigging hours run above what the duration model produces — unreconciled
created: 2026-09-07
status: resolved
type: idea-seed
tags: [estimating, duration-model, grok-bot, resolved]
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

---

## RULED 2026-09-17 (Jesse) — the Pig line is the pigging task, not pig travel

**The answer is the first candidate above: the pigging line covers more than pig travel.** 100 ft/hr
describes a pig moving through a coil; the quoted `Pig` line covers the whole task built around that
travel — fill, flush, flow tests between passes, pig changes, working the size progression,
dewatering. `footage / rate` is the **floor** of that line, not the answer. The other candidates were
offered and none was taken: the mixed 6"/4" radiant bore, a slow-service derate, and a mode-limited
Trimax are all unadopted.

**No multiplier was ruled and none may be derived from these three rows.** H-2501 sits at roughly 2x
the model and H-2421 at roughly 1.2x — that is not one factor, and fitting a coefficient across them
is precisely the parallel-friction failure: a number invented to suppress model variance, carried
four weeks, struck 2026-08-23. What an estimate must now do is price the travel component, size the
surrounding work to the job, and **state the two parts separately in the duration math**.

**Applied to all three homes this note named**, since a ruling that lands in one layer and not the
others is the documented failure mode: `01-context/estimating-approach.md`,
`~/.claude/skills/usadebusk-estimating/SKILL.md` — placed with a pointer to the localized-hard-spot
paragraph, which is a specific hypothesis sitting inside this general class and is still not a
derate — and `07-llms/grok/bot-setup/skills/duration-model.md`.

**Still open, and deliberately not answered here: how much the surrounding work is worth.** That
needs actuals with the pigging line broken out, which no card currently carries — all three DSP26080
heaters have empty Task Durations tables. Revisit when a job returns with the split recorded.
