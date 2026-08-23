# Estimating & Pricing Logic
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Module 6
**See also:** 01-context/estimating-approach.md (condensed session reference)

---

## Primary estimating drivers

1. Pass / circuit count — equipment qty and job duration
2. Tube ID — pig sizing, launcher size, adapter requirements
3. Total footage per pass — primary pigging duration driver
4. Expected fouling type — standard coke vs. hard coke/pitch (coker/crude units)
5. Equipment profile — 1x, 2x, or 3x Trimax
6. Travel distance — mob/demob mileage
7. Crew size — headcount drives labor and per diem

Note: Metallurgy does not significantly change the estimate. Customer typically handles soda ash.

## Duration model

All projects built on 12-hour shift cycles. Operations run 24/7 with Day and Night shift handovers.

Mob/Demob: 12-hour simultaneous Day and Night events (fixed).

Total duration = Rig-In + Pigging Hours + Rig-Out ± Rig-Over + Stand-By

**Pigging duration benchmark:** ~100 ft/hour per single unlooped coil (nominal fouling baseline)
- 3,000 ft coil = ~30 pigging hours for that coil
- **The derate is GATED (Jesse, 2026-08-23): apply it only where there is reason to believe the coil is dirty** — prior actuals on that heater, known fouling history, or hard service seen on that unit. A **first-time unknown heater takes the round 100 ft/hr**. Where the gate is met, reduce the ft/hour rate for: harder fouling (coker / crude / vacuum), pitch presence, tube restrictions, multiple tube sizes on one coil (each size pigged to completion in sequence). ⚠ **`first-time cleans with no prior data` was removed from this list** — it is the condition under which the derate does *not* apply, and the inversion drove a live estimate 79% over.
- Vacuum heaters run long as a rule — multiple tube sizes + hard coke + pigging the larger tube sizes from the larger outlet launcher
- Adjust using: prior cleaning data for same heater when available, job walk observations, coil loop configuration
- Build-up method: cost one unlooped coil → decide looping → lay out pass sets by equipment mode → add rig-overs → sum with rig-in/rig-out
- **Per-pig, not heater-total** (ruled 2026-07-24): heater-total footage ÷ 100 is wrong — it double-counts circuits pigged simultaneously. Elapsed time for a pass set is one coil's time, however many circuits it carries. **Round the per-coil figure to the nearest EVEN hour — up or down — once, at the coil level** (Jesse, 2026-08-23; replaces the former always-round-up rule). ⚠ **Parallel is free — there is no friction allowance and no pass set is ever marked up for running multiple circuits** (Jesse, 2026-08-23): a designated pigging tech is assigned to each pass and runs their own pump, circuit and pig changes, so double mode takes no longer than single. The "25–40% parallel-friction allowance" carried in `usadebusk-estimating` 2026-07-28 to 2026-08-23 is a **dead rule**. ⚠ **Do not land the total on a multiple of 12** — that rule was removed 2026-08-23 ("for now"); shifts and days are a presentation rounding only

Rig-In / Rig-Out: Fixed events; **rig-out matches rig-in**. Tier by heater size/height and the hard-pipe run to reach the launchers: Small 4 / Moderate 6 (majority) / Large 8 / Very large 12 hrs. Rig-Over between pass sets = `ceil(passes ÷ mode) − 1` (mode = passes cleaned per set: double 2, triple 3), ~1 hr with launchers/receivers pre-installed on the added passes else ~2 hr. Smart Pig: 4 hrs when applicable. **On a multi-heater mobilization the FIRST heater takes the full tier and subsequent heaters in close proximity take a reduced figure** (Jesse, 2026-08-23 — 6 vs 4 on DSP#26100), because the pumper stays partially rigged; that is why `Rig-Over` reads 0 on a job where the equipment moves between heaters. **Pre-inspection pigging on an already-decoked coil is a task allowance, not footage ÷ rate** — see `usadebusk-estimating` and [[DSP26100]].

SIMOPS (multi-heater jobs): Overlapping heater timeline visibility required — resource stacking and scheduling commitments must be visible across all heater cards simultaneously.

## Pricing structure

| Category | Pricing type | Line items |
|---|---|---|
| Equipment | Hourly task-based | Trimax Pumper (rates vary: Rig-In / Pigging / Stand-By) |
| Support equipment | Hourly fixed | 4×3 Trash Pump, Filter Press (pumping / non-pumping), Support Units, Crew Trucks |
| Labor | Hourly (12-hr shifts) | Supervisor/Lead (Day/Night), Technician/Operator (Day/Night) |
| Per Diem | Fixed daily allowance | 1 PD per 12-hour shift per person |
| Materials | Unit rate | Pigs (Foam, HR, TC, Swab — per pig), DEF (per shift) |
| Third Party | Cost + markup | Vac truck, light plant, compressor, rental vehicles, flights |
| Mob/Demob | Lump sum (95%) | Equipment (per mile), crew trucks (per mile), labor travel hours, per diem |

**Filter Press billing — two rates:**
- Pumping rate: when Trimax is actively pigging
- Non-pumping / stand-by rate: during rig-in, rig-out, stand-by

## Baseline rate table

Generic rates for new facilities without established contract rates. Use as starting estimate only — replace with actual contract rates before finalizing any proposal.

Third-party markup: 5%, 10%, or 15% per the specific facility/project contract — no default. Always confirm.

| Category | Description | Rate | Unit |
|---|---|---|---|
| Third Party | Cost + markup | 5 / 10 / 15% | Per contract — no default; confirm the applicable rate |
| Mob/Equipment | Trimax Travel | $3.00 | Mile |
| Mob/Equipment | Support Travel | $3.00 | Mile |
| Mob/Equipment | Crew Truck Travel | $3.00 | Mile |
| Mob/Labor | Crew Travel (non-driver) | $58.00 | Hour |
| Per Diem | Per Diem | $150.00 | Day |
| Equipment | Pumper: Rigging | $500.00 | Hour |
| Equipment | Pumper: Pig | $500.00 | Hour |
| Equipment | Pumper: Smart Pig | $500.00 | Hour |
| Equipment | Pumper: Stand-by | $500.00 | Hour |
| Equipment | Support Unit | $30.00 | Hour |
| Equipment | Filtration | $200.00 | Hour |
| Equipment | Filter Stand-by | $150.00 | Hour |
| Equipment | Crew Truck | $15.00 | Hour |
| Equipment | 4×3 Trash Pump | $50.00 | Hour |
| Labor | Project Manager | $80.00 | Hour |
| Labor | Supervisor | $74.00 | Hour |
| Labor | Operator | $64.00 | Hour |
| Materials | DEF | $125.00 | Shift |
| Materials | 4" Pigs | $59.00 | Each |
| Materials | 4.25" Pigs | $64.90 | Each |
| Materials | 5" Pigs | $89.70 | Each |
| Materials | 5.25" Pigs | $94.40 | Each |
| Materials | 6" Pigs | $118.00 | Each |
| Materials | 6.25" Pigs | $129.80 | Each |
| Materials | 6.5" Pigs | $142.80 | Each |
| Materials | 8" Pigs | $230.10 | Each |
| Materials | 8.25" Pigs | $247.80 | Each |
| Materials | 10" Pigs | $483.80 | Each |
| Materials | 10.25" Pigs | $531.00 | Each |

## Proposal cost categories

All proposals broken into: Mobilization | Demobilization | Equipment | Labor | Materials | Per Diem

## Heater card format

Each heater gets a task sequence card:
Rig-In → Pig → [Rig-Over] → [additional Pig passes] → [Smart Pig] → [Stand-By] → Rig-Out

Rig-Over occurs between passes or heaters mid-job, not before pigging begins.
