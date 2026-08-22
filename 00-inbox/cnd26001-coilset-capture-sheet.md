---
type: note
status: active
created: 2026-08-21
tags: [CND26001, syncrude, 7-1-F-1, actuals, capture, DQ-017]
related:
  - "[[7-1-F-1]]"
  - "[[2026-08-21-cnd26001-looping-duration-both-ways]]"
---

# CND26001 — Coilset Capture Sheet

Carry this on shift. It feeds `## Coilset Durations` on [[7-1-F-1]] at ingest (DQ-017 Phase 1, ruled 2026-08-21).

**Record what you run on nights.** Day-shift circuits come from the ticket breakdown — don't reconstruct them from hearsay. A blank is better than a guess; `?` is a real value in this schema.

**Reference only.** CND26001 is quoted, awarded and executing. Nothing here changes the job; it is the actuals return path so the next Syncrude bid has a real number instead of a struck one.

## What the job is expected to be

Third campaign on 7-1 F-1. **8 coils looped into 4 circuits at the radiant outlet flanges.** Both Trimax in **double mode** — each rig runs 2 looped circuits simultaneously, all 4 circuits at once, so **0 rig-overs**. Every coil is uniform at 2,237 ft, so **every looped circuit is 4,474 ft whatever the pairing.**

Quoted duration 84 hrs / 7 shifts (rig-in 8 · pig 47 · smart pig 18 · rig-out 8 = 81 raw). Basis is CND25004's looped 1&8 at 124 ft/hr plus a 25% parallel allowance. **The allowance is the untested part** — 124 was earned with one Trimax on one circuit; this job asks each rig for two at once. What actually happens is the thing worth measuring.

---

## 1. Circuit pairing — fill in first

Pairing was undecided at mob and is duration-neutral. Record what was actually built.

| Circuit | Coils looped | Rig | Launcher location | Notes |
|---|---|---|---|---|
| A | ___ & ___ | TM__ | | |
| B | ___ & ___ | TM__ | | |
| C | ___ & ___ | TM__ | | |
| D | ___ & ___ | TM__ | | |

---

## 2. Per-circuit clock — the sheet's whole point

**Per circuit, not per rig.** The card row aggregates to one row per rig, but an outlier only shows at this resolution: if two circuits on the same rig, same mode, same footage come out 12+ hrs apart, that is the `outlier` flag, and it is invisible once the hours are summed. This is exactly what went unrecorded on CND25004 and produced the struck ~6 ft/hr figure.

| Circuit | Rig-In start | Rig-In stop | Pig start | Pig stop | Smart start | Smart stop | Rig-Out start | Rig-Out stop |
|---|---|---|---|---|---|---|---|---|
| A | | | | | | | | |
| B | | | | | | | | |
| C | | | | | | | | |
| D | | | | | | | | |

Clock times, not durations — the subtraction happens at ingest and stays auditable.

**Pig hours include flow-test time.** Before/after flow tests are not broken out; fold them into Pig, same as the parent schema.

---

## 3. Stand-by — separate, and per rig

Stand-by is **not** a coilset figure and does not go in the table above. It is per rig, and on this heater it is customer-caused and not forecastable — CND24002 ran 36 hrs, CND25004 ran ~192 waiting on de-inventory, draining and blinding.

| Rig | Hours | Cause |
|---|---|---|
| TM5 | | |
| TM6 | | |

Cause matters more than the number. "Waiting on plant to install blinds" is the record; "delay" is not.

---

## 4. Coil condition — per circuit

How dirty the coil actually **was**, first pig out. `light` · `moderate` · `heavy` · `unknown`.

This is the field the vault has never had. Job class (`routine`) is already known and is a different thing — it says the job was planned, not that the coil was clean.

| Circuit | Condition | What you saw |
|---|---|---|
| A | | |
| B | | |
| C | | |
| D | | |

---

## 5. Pigs run — per circuit if you can

Feeds `## Pig Specifications` and `pig_usage_rollup.py`. CND25004's progression was 5.5" → 6.0" → 6.25" → 6.5" TC, Kicksolve against pitch/resid, 10.5" swabs to dewater.

| Circuit | Sizes / sequence | Count | Anything stuck or abnormal |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |
| D | | | |

---

## 6. Anything that broke the plan

Free text. Obstacles, plant procedures worth carrying to the next bid, and specifically: **did running two looped circuits per rig cost more than the 25% allowance assumed?** That is the one question this job can answer and no prior job could.

---

## At ingest — what this becomes

Two rows on [[7-1-F-1]]'s `## Coilset Durations`, one per rig, `Mode` 2, `Circuit ft` 4,474:

| Job # | Coils | Rig | Mode | Circuit ft | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Total | Coil condition | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CND26001 | (A + B) | TM5 | 2 | 4,474 | | | | – | | | | |
| CND26001 | (C + D) | TM6 | 2 | 4,474 | | | | – | | | | |

Then `ft/hr per pig = 4,474 ÷ Pig` for each rig — directly comparable to CND25004's **124 ft/hr** single-circuit figure, which is the number the CND26001 estimate was built on. Flag a rig `outlier` if its two circuits came out far apart; the parent `## Task Durations` row takes the summed hours, Stand-By, and `routine`.
