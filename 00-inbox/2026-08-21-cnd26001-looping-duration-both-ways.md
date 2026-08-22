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
| Equipment | 2× Trimax (5 + 6), Support 5 + 6. No filter press assigned | [[active-jobs]] |
| Job class | `routine` — planned TA | Card Job History |
| Connections | All launchers and receivers **at grade** | Card, Jesse 2026-08-20 |

**Pairing does not affect hours.** All 8 coils are identical, so every pairing gives the same 4,474 ft circuit. What pairing changes is loop-spool routing at the outlet end, not the duration. Do not hold the estimate for it.

## Rate selection

Condition- and heater-matched actuals exist, so they govern over the 100 ft/hr benchmark. Per the outlier rule, the 48-hr set (Trimax 5, coils 2/3/4, 47 ft/hr) is **excluded** — it ran the same rig configuration and mode as the 35-hr set on the same heater and came out 13 hrs apart, which is a problem specific to that coil set, not how this heater cleans. Stated here because an unstated exclusion is indistinguishable from cherry-picking.

That leaves two clustering sets, and **they do not agree on the question that matters:**

- **Trimax 6, coils 5/6/7, triple mode, 35 hrs → 64 ft/hr per pig.** Unambiguous: three separate coils, elapsed against one coil's footage. Embeds triple-mode parallel friction.
- **Trimax 6, coils 1 & 8, double mode, 36 hrs → 62 ft/hr *or* 124 ft/hr.** Unresolved. If 1 & 8 ran **looped**, the 36 hrs covered 4,474 ft in series and the rate is 124.

## The two readings

**A — 1 & 8 ran UNLOOPED (fall back to the 64 ft/hr triple set).**

```
per circuit   4,474 ft ÷ 64 ft/hr = 69.9  →  70 hrs   (circuit round-up)
sets          4 circuits, 2 per Trimax     →  1 set, 0 rig-overs
allowance     NONE ADDED — see below
elapsed pig                                   70 hrs
```

**B — 1 & 8 ran LOOPED (124 ft/hr is a direct precedent for this exact operation).**

```
per circuit   4,474 ft ÷ 124 ft/hr = 36.1  →  37 hrs
sets          4 circuits, 2 per Trimax      →  1 set, 0 rig-overs
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

## The exposure that dwarfs both readings

**Stand-by, not pigging.** CND25004 ran ~192 hrs of stand-by against 119 pig hrs, and CND24002 ran 36 — both waiting on the plant to de-inventory, drain, blind, and install the temporary 90s that bring both connection points to grade. Those 90s are a plant-side prerequisite and are the standing stand-by source on this heater. Whatever the pigging line resolves to, **the schedule risk on CND26001 is the plant's readiness, and it has historically been larger than the entire pigging duration.** Active-jobs notes the plant is reportedly running ahead of schedule this time, which would reverse the pattern — worth confirming rather than assuming.

Also unpriced: no filter press is assigned, and nothing covers filtration if Syncrude elects it.
