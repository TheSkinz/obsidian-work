---
type: quote
quote-number: "pending — Jesse to assign"
client: Valero
facility: Valero-Wilmington-CA
heaters:
  - 20H200
  - 20H2000
  - 31H3000
value: (not priced)
status: pending
date-execution: 2026-11
source: "RFQ email Shad Mackner to Travis Trenholm 2026-10-08 09:20; drawing PDFs 20H200 All Drawings, 20H2000 All Drawings, 31H3000 DRWG, 31H3000-Heater Tubes"
verified: never
---

# Valero Wilmington — Nov 30 2026 heater pigging (DSP# pending)

Rename this note to its DSP# when Jesse assigns it.

## Links

- Facility: [[02-facilities/Valero/Wilmington-CA/_facility|Valero Wilmington, CA]]
- Heaters: [[20H200]] · [[20H2000]] · [[31H3000]]

---

## RFQ (Shad Mackner, Turnaround Supt, 2026-10-08, to Travis)

Pig **20H200 and 20H2000, possibly 31H3000**, week of **2026-11-30**. All heaters at the same time: "definitely 2 trucks, maybe 3" if 31H3000 is in. **No smart pig.** Valero Process Engineering wants the coke loaded into **55-gallon drums** instead of the truck's water tank, to see how much comes out. Valero asks how many trucks we can provide that week. Job walk on request through Lorenzo Salazar, 310-350-4454.

## Rulings (Jesse, 2026-10-08)

- **No filter press.** Valero supplies the drums. The intent is to capture the fines and shovel them into the barrels at the end of the decoke, so drums are a customer-provided Section 8 item and the clean-out sits inside rig-out.
- **Rates come from the Valero contract**, which Jesse will send. Nothing is priced until it arrives. Precedent only: DSP26094 (Texas City) and DSP26035 (Port Arthur) carry an identical Valero rate set, which reads as a Valero master schedule — see the Three Rivers facility note.
- **Pumper allocation is unknown.** One, two and three Trimax are all viable; Jesse confirms how Valero wants the pumpers scheduled on 2026-10-09.
- **DSP#** assigned by Jesse.

---

## Drawing extraction

All figures below are read from the scans unless marked *computed* or *inferred*. Heater cards carry only the stated values.

### 20H200 — Vacuum Tower Feed (Born 1969, stated tube schedule)

2 passes (A, B). Per pass:

| Segment | OD / sched | Tubes | Lengths (stated) | ft (computed) | ID (computed, nominal sched) | Default max pig (computed) |
|---|---|---|---|---|---|---|
| Convection | 4.5" Sch 120 | 10 | 2 × 39'-4", 8 × 35'-6" | 362.7 | 3.624 | 3.750 |
| Radiant 1 | 4.5" Sch 120 | 15 | 1 × 39'-4", 14 × 36'-3¾" | 547.7 | 3.624 | 3.750 |
| Radiant 2 | 6⅝" Sch 80 | 2 | 35'-7¼", 36'-0¾" | 71.7 | 5.761 | 6.000 |
| Radiant 3 (outlet) | 8⅝" Sch 80 | 1 | 38'-10" | 38.8 | 7.625 | 7.875 |
| **Pass** | | **28** | | **1,020.9** | | |

Heater total 2,041.8 ft straight tube (computed), bends excluded. Footage by bore per pass: 4.5" 910.4 / 6⅝" 71.7 / 8⅝" 38.8. Inlet 4" 300# RFWN at el. 15'-4⅝"; outlet 8" 300# RFWN at el. 2'-3 9/16". Return bends are a mix of cast U-bends and 850# mule ears. The schedule states "avg wall", so actual IDs may sit off the nominal-schedule figures above.

Recompute check: 2(39.333) + 8(35.5) = 362.67; 39.333 + 14(36.3125) = 547.71; 35.604 + 36.063 = 71.67; 38.83. Sum 1,020.88.

### 20H2000 — Vacuum (HRC 1979, GA callouts only, pressure-parts sheet missing)

- Convection: 14 tubes of 4.5" OD × 0.237" AW, two per row → **2 passes, 7 tubes/pass (inferred)**, 23'-3" effective → 162.8 ft/pass.
- Radiant: callout "(29) 4.500 × 0.237 AW, A335 P9" → **29 tubes/pass (inferred)**, 23'-0" effective → 667.0 ft/pass.
- Outlet: one 6.625" × 0.280" AW A312 TP316L, length not stated.
- **~830 ft/pass, ~1,660 ft heater (inferred, bends and outlet excluded).** ID 4.026" (computed from 0.237 wall) → default max pig 4.250"; outlet 6.065" → 6.250".
- Inlet terminal ~el. 22'-6", outlet near grade. Flanges not stated.

### 31H3000 — Coker Feed (HRC 1973 GA, 2017 crossover iso)

- **2 passes (inferred from the iso):** B → A → C and E → D → F.
- Counted on the iso (inferred): convection ~24 tubes/pass (8 rows × 3); radiant ~50/pass (B ~10, A ~24, C ~16).
- Radiant effective length 31'-2" (GA, stated) → ~1,558 ft/pass. Convection length not legible; at a similar ~31 ft it adds ~744 ft.
- **~2,300 ft/pass, ~4,600 ft heater (inferred).** Tube OD, schedule and flanges unknown.

---

## Pass picture

**6 passes total, 2 per heater.** 20H200's count is stated; the other two are inferred.

| Heater | Passes | ft/pass | Travel hrs (100 ft/hr) | Per-coil figure |
|---|---|---|---|---|
| 20H200 | 2 | 1,021 | 10.2 | 10 |
| 20H2000 | 2 (inferred) | ~830 | 8.3 | 8 |
| 31H3000 | 2 (inferred) | ~2,300 | 23.0 | 22–24 (footage uncertain; an exact 23.0 ties and rounds down to 22) |

**Derate gate: shut on all three.** There is no recorded history on any of these heaters, so the round 100 ft/hr applies. Vacuum service, three bores per pass and mule-ear bends on 20H200, and coker service on 31H3000, are the conditions that would derate if the gate were open. They are listed here as exposure, not applied.

**These are travel figures only.** The Pig line also covers fill, flush, flow tests, pig changes, working through the size progression (three sizes on 20H200), dewatering and shovelling the fines into Valero's drums. That surrounding work is Jesse's judgment and is stated separately once he sizes it.

**Rig-in:** 6 hrs default on each heater. 20H200's connections are at 15 ft and grade, and 20H2000's inlet is at ~22 ft, so neither reaches the >40 ft departure. 31H3000's elevations are unknown, so it takes the default. A Trimax moving on to a nearby heater takes a reduced 4/4; a distant one takes a full rig-out and rig-in. Whether units 20 and 31 are close is unknown. Rig-out mirrors rig-in.

---

## Allocation scenarios (alternatives; Valero's choice confirmed 2026-10-09)

Travel-component elapsed times, before Jesse's pigging allowance:

| Scenario | Trimax | Mode | Sequence | Critical path (travel basis) |
|---|---|---|---|---|
| A — one per heater | 3 | double each | all concurrent | 31H3000: 6 + 22–24 + 6 ≈ 34–36 hrs |
| B — two pumpers, heaters whole | 2 | double | T1: 20H200 then 20H2000 (6+10+6, then 4+8+4 if adjacent); T2: 31H3000 | T1 ≈ 38 hrs; T2 ≈ 34–36 hrs |
| C — two pumpers, all 6 passes at once | 2 | triple each | one pumper takes a heater plus one pass of the other 20-unit heater, or similar split | 31H3000 sets it; needs a heater split across pumpers |
| D — RFQ base (31H3000 out) | 2 | double | 20H200 and 20H2000 concurrent | 20H200: 6 + 10 + 6 = 22 hrs |
| E — one pumper | 1 | double | three heaters in sequence | ≈ 22 + 16 + 34–36 = 72–74 hrs (20H2000 at a reduced 4/4 if adjacent; 31H3000 at a full rig, assuming unit 31 is distant) |

Rig-over is 0 in every scenario: each heater is one pass set in double mode.

---

## Pig quantity inputs (hard pigs only)

There is no history on any of the three heaters, so quantity scales off footage by bore. Foam and swab pigs are outside the method and unpriced pending Jesse.

| Heater | Bore | ft (heater) | Default size (computed) |
|---|---|---|---|
| 20H200 | 4.5" Sch 120 | 1,821 | up to 3.750" |
| 20H200 | 6⅝" Sch 80 | 143 | up to 6.000" |
| 20H200 | 8⅝" Sch 80 | 78 | up to 7.875" |
| 20H2000 | 4.5" × 0.237 | ~1,660 (inferred) | up to 4.250" |
| 20H2000 | 6⅝" × 0.280 outlet | not stated | up to 6.250" |
| 31H3000 | unknown | ~4,600 (inferred) | unknown |

---

## Mob/demob cost build-up (internal; billable lump sum is contract-governed)

Deer Park, TX → Wilmington, CA is **~1,550 one-way road miles (estimate, not measured)**, roughly 23–25 hrs of driving, so **3 drive-days** per driver at ~10 hrs/day.

At the baseline rates, per piece per end: 1,550 × $3.00 = **$4,650** in mileage, plus 3 driver per diems × $150 = **$450**, so **~$5,100**. Non-drivers each get travel labor at the contract travel rate × actual travel hours, plus 1 per diem; flights and rental cars are a likely third-party line at this distance.

**Piece count per Trimax is a must-ask** (Trimax, support unit, crew trucks), so no total is carried. With no filter press, pieces run lower than on a filtration job.

---

## Open — RFI to Valero

1. 20H2000 pressure-parts drawing 79-614-5-T-11 and the crude-increase revision sheets WD-20-0240-H thru 0242-H.
2. 31H3000 coil sheets 1–6, 8 and 9 of the 31H3000 set (tube OD, schedule, lengths, return bends), plus WD-31-100-1 (convection bundle addition).
3. Inlet/outlet flange size and rating for 20H2000 and 31H3000, and whether 20H200's 1969 flanges (4" / 8" 300#) are still current.
4. Launcher/receiver elevations and access for all three, and whether spools or 180s are needed.
5. Water source and supply size.
6. Pumper allocation (Jesse's call with Valero, 2026-10-09).

## Open — Jesse

- DSP#, Valero contract rates and markup tier.
- Pigging task allowance over the travel floor, per heater.
- Pieces traveling per Trimax.
- Fleet availability for 3 Trimax the week of 11-30.
