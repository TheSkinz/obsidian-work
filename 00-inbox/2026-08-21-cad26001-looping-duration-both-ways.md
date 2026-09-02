---
type: note
status: inbox
created: 2026-08-21
tags: [estimating, duration, syncrude, CAD26001, 7-1-F-1]
---

# CAD26001 duration build-up — looped 8→4, settled at 84 hrs / 7 shifts

Worked 2026-08-21 after Jesse confirmed the looping election, and **closed the same day** when he
resolved the CAD25004 coils 1 & 8 question that had been the one open input. **Mob 2026-08-25.**
Reference working note, not a quote. Rates and elections are per-job inputs.

**Answer: 84 hrs, 7 shifts** — rig-in 8 · pig 47 · smart pig 18 · rig-out 8 = 81 raw, landed at 84.

> [!important] Scope — this is a reference expectation, not an estimate, and nothing here is an open item.
> **CAD26001 is already quoted, awarded, and about to execute for the third time** (Jesse, 2026-08-21).
> There is no bid to price and no number anyone is going to re-open before mob. **If the job goes over,
> it goes to a change order and other people negotiate it** — that is not Jesse's line and not this note's.
> So the shift-landing, band-position and boundary-slack machinery below is **bid-time apparatus applied
> after the fact.** It was worth computing for exactly two reasons and no others: (1) it says what to
> expect on site, and (2) it becomes the quote-vs-actual comparison once the Task Durations row is filled
> in after the job. **Do not read any line below as a thing to confirm, chase, tighten, or raise.**

## Inputs

| Input | Value | Source |
|---|---|---|
| Coils | 8, uniform — 2,237 ft each (1,040 conv + 1,197 rad), 47 tubes | [[7-1-F-1]] Config Rollup, drawing-verified 2026-08-20 |
| Bore | Single 6.065" ID throughout, no telescoping | Quest title block + coil revamp BOM |
| Looping | **8 → 4 circuits at the radiant outlet flanges** | Jesse, 2026-08-21 |
| Circuit length | **4,474 ft** (2 × 2,237) | Derived |
| Pairing | Undecided — **and duration-neutral**, coils are uniform | Jesse, 2026-08-21 |
| Equipment | 2× Trimax (5 + 6), Support 5 + 6. **No filtration — not used on this heater, settled** | [[active-jobs]]; Jesse, 2026-08-21 |
| **Mode** | **Both Trimax in double mode; all 4 looped circuits pigged simultaneously** — one pass set, 0 rig-overs | **Stated by Jesse, 2026-08-21** (not derived) |
| Job class | `routine` — planned TA | Card Job History |
| Connections | All launchers and receivers **at grade** | Card, Jesse 2026-08-20 |

**Pairing does not affect hours.** All 8 coils are identical, so every pairing gives the same 4,474 ft circuit. What pairing changes is loop-spool routing at the outlet end, not the duration. Do not hold the estimate for it.

**Mode was confirmed by Jesse on 2026-08-21**, matching what the build-up had assumed — two circuits per Trimax in one set. It matters more than it first appeared: because each Trimax runs *two* looped circuits rather than the one that earned the 124 ft/hr precedent, it is the reason a parallel allowance applies at all. See Rate basis.

## Rate selection

Condition- and heater-matched actuals exist, so they govern over the 100 ft/hr benchmark. Per the outlier rule, the 48-hr set (Trimax 5, coils 2/3/4, 47 ft/hr) is **excluded** — it ran the same rig configuration and mode as the 35-hr set on the same heater and came out 13 hrs apart, which is a problem specific to that coil set, not how this heater cleans. Stated here because an unstated exclusion is indistinguishable from cherry-picking.

That leaves two clustering sets, and **the governing one is now settled:**

- **Trimax 6, coils 1 & 8, LOOPED into one 4,474 ft circuit, 36 hrs → 124 ft/hr per pig.** **RESOLVED 2026-08-21** (Jesse): 1 & 8 were looped and were the only looped pair on CAD25004. It was a deliberate test of whether a looped pair is too much footage for one circuit and whether it could still be done in a similar time. It could — and that result is why CAD26001 loops all eight. **This is a direct precedent for exactly the operation CAD26001 runs**, on this heater, this service, this job class.
- **Trimax 6, coils 5/6/7, triple mode, 35 hrs → 64 ft/hr per pig.** Retained as the parallel-friction reference below, not as the rate.

**The test result, in the numbers:** 4,474 ft looped in 36 hrs against 2,237 ft per coil unlooped in 35 hrs. Double the footage per circuit for one hour more elapsed. The looped circuit is not close to a limit.

## Rate basis and the one allowance that applies

**124 ft/hr is the rate. But it was earned single-circuit, and CAD26001 is not.** On CAD25004 the sets ran **sequentially** — when Trimax 6 pigged the looped 1 & 8, that circuit had the rig's undivided attention. CAD26001 asks **each Trimax to run two looped circuits at once**. So unlike the 64 ft/hr triple figure, **124 does not already embed multi-circuit friction**, and the 25–40% band applies on top of it. This is the one place the precedent does not transfer clean.

**Where in the band, and why.** Sitting at the **low end, 25%**, on the grounds the skill names: single bore throughout with no telescoping and no size sequencing, all connections at grade, a known heater on its third campaign with the same rig pair, and only **two** circuits per rig — the mildest multi-circuit case there is. Against that, CAD25004's own data suggests going from one circuit to three roughly halved each pig's speed (0.00805 vs 0.01565 hr/ft), so one-to-two could plausibly sit at the top of the band instead.

**It does not matter — and that is the useful part.** Both ends of the band land on the same shift count:

```
25%   37 × 1.25 = 46.25  →  47 hrs   →  raw total 81  →  84 hrs = 7 shifts
40%   37 × 1.40 = 51.8   →  52 hrs   →  raw total 86  →  84 hrs = 7 shifts
```

The estimate is **insensitive to the allowance judgment**, so no effort is worth spending narrowing it. Carrying **25% / 47 pigging hrs** as the stated figure.

```
per circuit   4,474 ft ÷ 124 ft/hr = 36.1  →  37 hrs   (circuit round-up — step 1)
allowance     37 × 1.25 = 46.25            →  47 hrs   (allowance on the ROUNDED 37, then
                                                        round the set — step 2)
sets          4 circuits, 2 per Trimax (double) → 1 set, 0 rig-overs
elapsed pig                                       47 hrs
```

## Build-up

| Line | Hrs | Basis |
|---|---|---|
| Rig-in | 8 | Large tier. All at grade, but 8 circuit lines across 2 Trimax at double. **Vault rig-in actuals deliberately not used** — mixed-method column, per the skill. |
| Pig | 47 | Above: 124 ft/hr precedent + 25% parallel allowance |
| Smart pig | 18 | CAD25004 actual (CAD24002 ran 9). Quest smart-pigged all 8 coils on **both** prior campaigns, so it carries on the recurrence — not treated as an open election. |
| Rig-over | 0 | `ceil(4 ÷ 4) − 1 = 0` — all four circuits run at once |
| Rig-out | 8 | Mirrors rig-in |
| **Raw total** | **81** | |
| **Landed** | **84 — 7 shifts** | +3, small and one-directional |

**The landing is stable.** 81 sits 9 above 72 and 3 below 84, so it is not in the middle third and the mid-band diagnostic does not fire — the nearer boundary is also the one the residual risk points toward. And as shown above, a 40% allowance instead of 25% raises the raw to 86 and **still lands on 84**. The shift count does not move on any judgment left in this build-up.

**Smart pig is the widest line** — 18 hrs on CAD25004 against 9 on CAD24002. At the low end the total is 72 and the job runs 6 shifts rather than 7. Noted so the range is on the record, **not as something to pin down**: see the scope note below.

**For comparison, what looping buys.** CAD25004 pigged the same 8 coils in three sequential sets for **119 pig hours**. CAD26001 does all 8 in one set of 4 looped circuits for **47**. The test that produced the 124 ft/hr figure is the reason.

## Stand-by history — recorded, not forecast

CAD25004 ran ~192 hrs of stand-by against 119 pig hrs; CAD24002 ran 36. Both were waiting on the plant to de-inventory, drain, blind, and install the temporary 90s that bring the connection points to grade.

**This is history and nothing more. Do not carry it into the estimate.** Stand-by on this heater is customer-caused, and USADebusk neither controls it nor can anticipate it (Jesse, 2026-08-21): *"We will have to clean the heater when they are ready whenever that may be."* It is not a risk line, not a pad, not an open item, and not a thing to confirm with Syncrude. The customer's own note that the plant is running ahead of schedule changes none of that and is not evidence about what will happen — a schedule note is not a commitment, and on-time, a shift early and a shift late are all the same job to us.

The general rule this instance sits under is in `usadebusk-estimating`: customer-caused stand-by is not an estimating input, while stand-by USADebusk's own equipment profile causes — the F-802 filter-press case — is foreseeable and stays statable. This job has no filtration at all, so that side does not arise here.
