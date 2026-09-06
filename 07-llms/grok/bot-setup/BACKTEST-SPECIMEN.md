---
title: Grok Bot estimating skills — back-test specimen
created: 2026-09-06
tags: [grok, grok-bot, estimating, backtest, specimen]
---

# Back-test specimen — the four estimating skills against DSP26085

**Read this, not the four skill files.** The specimen is what shows whether the port is right.

**Fixture:** [[DSP26085]] — ExxonMobil Baytown, 27GF1A F-201 Treat Gas heater, submitted
2026-07-06, status pending. One Trimax, one support unit, filtration, 2 crew trucks. Four
convection coils looped to **2 circuits** via temporary 5" convection-inlet loops; all pigs launched
and received at the radiant outlets. Quoted **36 hrs total — 6 Rig-in | 18 Pig | 6 Smart Pig |
6 Rig-out**, total $46,657.08.

Every figure below was read from the quote note and the heater card, then predicted independently
from the ported skill text.

## Six rules reproduce the real quote exactly

| Rule as ported | Predicts | Quote carries | |
|---|---|---|---|
| Rig-in default 6 hrs, no departure triggered (connections not 40+ ft with double/triple) | 6 | **6** | pass |
| Rig-out mirrors rig-in at the whole figure | 6 | **6** | pass |
| Pigging = one circuit's path / 100 ft/hr, **not** heater-total footage / 100 | see below | **18** | pass |
| Crew trucks: all travel, **only one bills hourly at project hours** | 36 hrs, Qty 1 | **`Crew Truck \| 36 \| Hrs`**, one line, 2 trucks mobilized | pass |
| Filter press two rates — pumping is **pigging only**, non-pumping is rig-in + rig-out + smart pig + stand-by | 18 pumping / 18 non-pumping | **Filtration 18 @ $200 · Filter Stand-by 18 @ $150** | pass |
| No PM row in the allocation block means no PM is billed; the Travis Trenholm name in the duration block is a placeholder, not an assignment | no PM line | no PM line; note reads *"Project Manager (quoted): Travis Trenholm — not billed as a line item"* | pass |

**The pigging check is the one that matters most**, because it is the rule with the largest failure
mode. The card records convection at **540 ft/pass, 4 coils, 2,160 ft heater total**, looped to
2 circuits — so each circuit's pig path is 1,080 ft of convection plus its radiant run, which the
card records as **unrecorded footage**. Heater-total arithmetic would give 2,160+ / 100 = **21.6+ hrs
and rising** once radiant is counted. The quoted 18 hrs corresponds to a single circuit's full path
at ~1,800 ft, with the second circuit running in parallel for free. **The port predicts the shape of
the real answer; the arithmetic it forbids does not.**

Labor also reconciles: `Day Operator | Qty 2 | Hrs (combined) 48` is 2 x 24, which is the ported
"Labor Amt = combined man-hours = Qty x per-person shift hours" and not a per-person figure.

## One rule is falsified — Smart Pig is not a flat 4 hours

**The ported text says "Smart Pig: 4 hrs when elected. One event covering the pass set, not a
per-pass figure."** That is faithful to both sources — `usadebusk-estimating` and
`01-context/estimating-approach.md:38` each state it as a flat 4.

**It does not predict the real quotes.**

| Job | Shape | Smart Pig hrs |
|---|---|---|
| DSP26085 · F-201 | 1 heater, 4 passes, 2 circuits | **6** |
| F-301 / F-371A | paired 2-heater line item | **8** |
| CHS HP-0003 / HP-0006 | 2 heaters, billed together | 4 (2 + 2) |

F-201's own card states it outright at line 102: *"Smart pigging / inspection | Elected | **6 hrs
quoted on DSP26085 — all 4 passes.**"* So the card, the quote and the rule disagree, and the card
and quote agree with each other.

**Ruled the same day. Smart Pig is 2 hrs per pass** (Jesse, 2026-09-06), replacing the flat 4.

**The premise of the finding was wrong, and that is the more useful lesson.** There is no scaling
law to recover, because there was never a rule generating those numbers: *"There isn't a specific
logic I use to determine the smart pig hours, because I don't know how long it will actually take.
Several jobs are going to have conflicting information about that number."*

So the back-test found a real gap in the written rule and then over-read it — treating a line Jesse
estimates by feel as though a derivable rule sat behind three data points. **Under the new figure
DSP26085's 4 passes give 8 hrs against a quoted 6, and that disagreement is expected rather than a
defect to chase.** The ported skill now says so explicitly, so a Bot takes 2 hrs per pass and moves
on instead of opening an investigation.

Propagated to all four places that stated the old figure: `01-context/estimating-approach.md`,
`04-knowledge/concepts/estimating-pricing.md`, the `usadebusk-estimating` skill, and
[[duration-model]] — leaving any of them behind would have recreated the rig-in drift in reverse.

## What the composition pass found

Running intake → duration → work-up → proposal end to end on one bid surfaced nothing where two
rules collide. The specific collision the plan was watching for — rig-in and rig-over reading
"silence" in opposite directions — does not occur here, because both ported rules state the
affirmative trigger in the same words and cross-reference each other. DSP26085 is silent on
pipefitters, so both take the bare figure: rig-in 6, and rig-over 0 (a 2-circuit job in double mode
is `ceil(2/2) - 1 = 0`, and the quote carries no rig-over line). Consistent.

## Verdict

**Port is sound on everything checkable.** Six rules reproduce a real quote to the hour and to the
line, including the two that have each cost real money (crew truck, PM hours) and the one with the
largest blast radius (per-pig, not heater-total).

**One rule was already wrong before it was ported**, and the back-test is what surfaced it. That is
the back-test working, not the port failing.

**Not yet checked:** the pre-send gate, which needs a workup/quotation pair rather than a quote note;
and the mob/demob costing build-up, which needs the workup's internal cost columns. Both are worth a
second specimen if the trial goes past the first week.
