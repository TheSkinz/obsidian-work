---
type: finding
status: open
created: 2026-09-03
tags: [inbox, estimating, duration-model, regression, needs-ruling]
---

# The pipefitter adder has no home once rig-in is already at the 12-hr cap

Found by the 2026-09-03 F6 regression replay, unprompted. Not predicted by the session plan. **No rule has been changed — this is a proposal.**

## The mechanic

`usadebusk-estimating` sets rig-in as one of six values (2, 4, 6, 8, 10, 12) with 12 as a hard ceiling, and adds roughly 2 hrs where the customer's pipefitters hang the launchers and receivers and USADebusk will be waiting on them. The trigger is affirmative — it fires only on a positive statement, not on silence.

On F6's fixture both conditions hold at once: the tier reads Very large at **12** on its own (elevation × run distance × mode 6), and the job data states the fitters hang the launchers and USADebusk will wait. So the adder fires and is then **absorbed by the cap** — 12 + 2 is still 12. Rig-out mirrors, so the same absorption happens again.

## Why it matters

Roughly **4 hrs of stated, customer-caused exposure across both rig sides appears nowhere in the total.** The skill's instruction is to carry it as a stated risk, and the run did exactly that — correctly, which is why F6 passed. But the estimate itself holds no slack for a delay the job data explicitly told us about.

This is not the same thing as the customer-caused stand-by rule (`2593967`), which says plant readiness is not forecastable and must not be priced. This one is different in kind: the fitters hanging launchers is inside the rig-in scope we are quoting, not the plant's release of the heater, and the job data stated it rather than us guessing it.

## What is genuinely open

Three readings, and this is a Lane 4 duration-model question that only Jesse can settle:

1. **Correct as-is.** The cap is a cap; a stated risk in the duration math is the right and sufficient treatment, and adding hours would be padding of exactly the kind the T&M asymmetry argument rejects.
2. **The cap should lift for a stated adder.** Rig-in stays a six-value selector for the tier, but an affirmative fitter statement can carry it past 12 — which would break the "always one of six values" rule at `8d6a154` and needs that rule amended in the same breath.
3. **The exposure belongs somewhere other than rig-in.** A separate stated line, or a named open item with its swing costed, rather than hours buried inside a capped task line.

**Do not resolve this by picking a number.** The 25–40% parallel allowance was manufactured in a regression session exactly this way and priced real work for a month before being struck.

## Note on scope

`8d6a154` also rules that rig-in precision is explicitly **not** where estimating effort belongs, because pigging hours carry the money and the schedule risk. That argues for reading (1) — leave it alone — unless a real job has actually been hurt by the absorbed hours. Worth checking the F-802 and CAD26001 actuals for a rig-in overrun attributable to fitter wait before spending a cycle on this.

Related: [[2026-09-03-regression-battery-findings]]
