---
type: note
status: inbox
created: 2026-08-21
tags: [estimating, duration, syncrude, CND26001, 7-1-F-1]
---

# CND26001 duration build-up — looped 8→4, and the one number that moves it three shifts

Worked 2026-08-21 after Jesse confirmed the looping election. **Time-boxed: mob 2026-08-25.**
Reference working note, not a quote. Rates and elections are per-job inputs.

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

**Mode was confirmed on 2026-08-21 and no figure below moved** — the build-up had already assumed two circuits per Trimax in one set, which is what Jesse stated. The change is that the 70 / 37 hr pigging figures and the 104 / 71 raw totals now rest on a stated equipment plan rather than on my inference.

## Rate selection

Condition- and heater-matched actuals exist, so they govern over the 100 ft/hr benchmark. Per the outlier rule, the 48-hr set (Trimax 5, coils 2/3/4, 47 ft/hr) is **excluded** — it ran the same rig configuration and mode as the 35-hr set on the same heater and came out 13 hrs apart, which is a problem specific to that coil set, not how this heater cleans. Stated here because an unstated exclusion is indistinguishable from cherry-picking.

That leaves two clustering sets, and **they do not agree on the question that matters:**

- **Trimax 6, coils 5/6/7, triple mode, 35 hrs → 64 ft/hr per pig.** Unambiguous: three separate coils, elapsed against one coil's footage. Embeds triple-mode parallel friction.
- **Trimax 6, coils 1 & 8, double mode, 36 hrs → 62 ft/hr *or* 124 ft/hr.** Unresolved. If 1 & 8 ran **looped**, the 36 hrs covered 4,474 ft in series and the rate is 124.

## The two readings

**A — 1 & 8 ran UNLOOPED (fall back to the 64 ft/hr triple set).**

```
per circuit   4,474 ft ÷ 64 ft/hr = 69.9  →  70 hrs   (circuit round-up)
sets          4 circuits, 2 per Trimax (double)     →  1 set, 0 rig-overs
allowance     NONE ADDED — see below
elapsed pig                                   70 hrs
```

**B — 1 & 8 ran LOOPED (124 ft/hr is a direct precedent for this exact operation).**

```
per circuit   4,474 ft ÷ 124 ft/hr = 36.1  →  37 hrs
sets          4 circuits, 2 per Trimax (double)      →  1 set, 0 rig-overs
elapsed pig                                    37 hrs
```

**No parallel-friction allowance is stacked on either.** The 25–40% band applies to a rate that has not already been degraded; both of these are set-elapsed against one coil's footage on *this heater*, so they already embed their own job's friction. Adding the band on top double-counts — the skill's own caution. Directionally the CND26001 profile is no worse than the source: 2 circuits per Trimax across two rigs and two crews is milder than one Trimax running three.

## Build-up

| Line | A (unlooped basis) | B (looped basis) | Basis |
|---|---|---|---|
| Rig-in | 8 | 8 | Large tier. All at grade, but 8 circuit lines across 2 Trimax at double. **Vault rig-in actuals deliberately not used** — mixed-method column, per the skill. |
| Pig | 70 | 37 | Above |
| Smart pig | 18 | 18 | CND25004 actual. Quest smart-pigged all 8 coils on both prior jobs; **election for CND26001 is TBD**. |
| Rig-over | 0 | 0 | `ceil(4 ÷ 4) − 1 = 0` — all four circuits run at once |
| Rig-out | 8 | 8 | Mirrors rig-in |
| **Raw total** | **104** | **71** | |
| Shift landing | 8.7 shifts | 5.9 shifts | |

**Reading A trips the mid-band diagnostic.** 104 sits 8 above 96 and 4 below 108 — both landings are large, which per the rule means an input is unresolved rather than the job genuinely falling between shifts. **Do not book a pad.** The softest line is named below and it is worth 33 hours, far more than any landing adjustment.

**Reading B lands at 72 (6 shifts) on its own**, +1 from raw — the signature of a build-up whose inputs are settled.

## The one thing worth resolving before mob

**Did CND25004's coils 1 & 8 run looped?** It is worth **33 pigging hours — close to three shifts** — and it is the difference between a clean 6-shift job and a 9-shift one. Resolvable two ways: the CND25004 ticket breakdown, or Jesse's recollection.

Evidence currently splits. The drawing shows 1 & 8's outlet spools already paired at grade, and they were the one non-triple grouping on that job — both point looped. Against that, the set is recorded as **double mode**, and by the card's own convention Mode counts passes pigged *simultaneously*, so a looped 1 & 8 would have been mode 1. That is a ticket label, not proof.

Until it is settled, **carry A (104 raw) as the estimate** — it is the defensible reading, and the residual risk on this heater runs one-directional toward longer, not shorter.

## Stand-by history — recorded, not forecast

CND25004 ran ~192 hrs of stand-by against 119 pig hrs; CND24002 ran 36. Both were waiting on the plant to de-inventory, drain, blind, and install the temporary 90s that bring the connection points to grade.

**This is history and nothing more. Do not carry it into the estimate.** Stand-by on this heater is customer-caused, and USADebusk neither controls it nor can anticipate it (Jesse, 2026-08-21): *"We will have to clean the heater when they are ready whenever that may be."* It is not a risk line, not a pad, not an open item, and not a thing to confirm with Syncrude. The customer's own note that the plant is running ahead of schedule changes none of that and is not evidence about what will happen — a schedule note is not a commitment, and on-time, a shift early and a shift late are all the same job to us.

The general rule this instance sits under is in `usadebusk-estimating`: customer-caused stand-by is not an estimating input, while stand-by USADebusk's own equipment profile causes — the F-802 filter-press case — is foreseeable and stays statable. This job has no filtration at all, so that side does not arise here.
