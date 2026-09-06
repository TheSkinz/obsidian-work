# Skill — Work-Up Billing Math

**Owner Bot:** Estimator
**Source:** ported from `usadebusk-estimating` § Work-Up Billing Math and § Pricing Structure.
Canonical schema home: `/workspace/vault/04-knowledge/_canonical-job-sheet.md`; live instance:
`02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.md`.

**No rate numbers live in this skill.** Rates belong to a **contract**, not to a facility and not to
a table — one site can carry several concurrent contracts at different rates, and rates are adjusted
per bid to stay competitive. Read them from the governing contract or bid instructions for *this*
opportunity. The vault's `04-knowledge/rate-history-rollup.md` records what was quoted historically
and states outright that **nothing in it can be quoted from**; the Baseline Rate Table in the
estimating skill is captioned *generic rates for new facilities without contract rates* and diverges
from what is actually quoted on most lines. Use both as precedent, never as a source of truth.

Where a figure appears below it is there to make a rule legible — the size of an error, or a formula
anchor marked "confirm per contract". None of them is a rate to quote.

## Pricing structure

| Category | Type | Line items |
|---|---|---|
| Equipment | Hourly task-based | Trimax Pumper (Rig-In / Pig / Smart Pig / Stand-By rates) |
| Support equipment | Hourly fixed | 4x3 Pump, Filter Press (pumping / non-pumping), Support Units, Crew Trucks |
| Labor | Hourly (12-hr shifts) | PM, Supervisor (Day/Night), Operator (Day/Night) |
| Per Diem | Daily per person | 1 PD per 12-hr shift |
| Materials | Unit rate | Pigs (by size/type), DEF (per shift) |
| Third Party | Cost + markup | Vac truck, light plant, compressor, rental, flights |
| Mob/Demob | Lump sum (~95% of jobs) | Equipment miles + crew travel labor + driver per diem |

## Per-heater Qty / Item / Amt / Unit conventions

- **Shift basis:** day-shifts x 12h (last may be partial) + night-shifts x 12h = heater total pumper
  hours.
- **Labor Amt = combined man-hours** = Qty x per-person shift hours. Two Day Operators over
  44 h/person = 88.
- **Equipment lines** (pumper, support unit, filter unit, crew truck) bill at the heater's pumper
  total hours. **The filter unit line appears only when filtration was elected** — omit the row on a
  non-filtered job rather than carrying it at zero.
- **Per Diem bills per day; headcount excludes the billable Project Manager.**
- **DEF bills per shift at the quoted shift count as given** — not derived from total shift count.
- A billable Project Manager line appears per-heater **only when the quote carries one**.

The quote's resource plan can differ from the actual mobilized crew — the job sheet reflects the
quote; actuals reconcile on the job report.

## The two rules that have each cost real money

Both are counter-intuitive and both have been got wrong.

**Crew trucks: ALL mobilized trucks bill on mob/demob, but only ONE bills hourly — Qty 1 at project
hours, however many travelled.** (Jesse, 2026-08-15.) The trucks taxi each shift between the hotel
and the facility, and a truck bills only while it is *inside* the facility. Dayshift brings one in
and takes it out at shift change; nightshift brings the other in and does the same. Exactly one
truck is on site at any moment, so `2 shifts x 12 hrs = 24 truck-hours per day` — one truck billed
around the clock. No truck is dedicated to a shift; they are interchangeable. **The extra truck is a
traveling piece on mob/demob, never a second hourly line.**

Worked actuals: USA26038 H-19, 48 hrs total gives `Crew Truck | 48 | Hrs` at Qty 1; H-20, 80 hrs
total gives `Crew Truck | 80 | Hrs` at Qty 1. **Billing a second truck hourly over-quotes by the full
project hours x the truck rate — on a 48-hr job, $720.** This does **not** reduce the mob/demob piece
count: a job enumerating two crew trucks travels both, and both carry mileage and a driver.

**A Project Manager is always on dayshift and bills like any other dayshift employee** — day-side
per-person hours, the same figure as the Day Supervisor. **Never the full project duration.**
(Jesse, 2026-07-25.) Worked actual: USA26038 H-20, 80 hrs total, day side 44 and night side 36 gives
`Project Manager | 44 | Hrs`, matching `Day Supervisor | 44 | Hrs`, not the 80. **Billing a PM the
project total over-quotes by the night-side hours: on a 45-hr, 4-shift job that is $1,680, roughly
2.8% of a $60k quote.** This is a billing-hours rule only — the per-diem exclusion above is separate
and still applies.

## Stand-by applies to two rate lines only

**Trimax Pumper and Filter Press.** Triggered when the project is not actively moving forward
(rig-in, rig-out, waiting) and USADebusk cannot rig-in, pig, or smart-pig. **All other resources —
support equipment, labor, per diem, materials, mob/demob — bill unchanged regardless of stand-by
status.** There is no generic stand-by line; Plant Down Time bills through these two rates.

**Filter Press has two rates.** Pumping rate: **pigging only**. Non-pumping / stand-by rate: rig-in,
rig-out, smart pigging, stand-by.

**Filter press capacity is an equipment-profile decision, not an afterthought.** One press against
2x Trimax is a known failure point: USA26022 (F-802, ExxonMobil Baytown) hit capacity repeatedly
during pigging and generated **20 hrs of billable stand-by, $25,628.17**, on a routine crude heater.
Solids load scales with circuits running at once and with fouling severity, so a first-time or
hard-coke job at mode 4+ is worse than that case, not better. When the profile puts two or more
Trimax against a single press, **confirm with Jesse whether a second press is in scope** — it is
never a given, and there is no larger press, so more capacity means another press rather than a
bigger one. **Do not attempt to reason about which presses are free or where they are;** the vault
does not track fleet availability. Where a second press is not in scope, name press capacity as a
stated stand-by risk in the proposal — do not leave it unstated.

## Third-party markup

One of three tiers — **5%, 10%, or 15%** — set by the specific project/facility contract, **never a
default**. Always confirm before finalizing any proposal or invoice. Recent work has mostly landed
at 15%, but that is an observation, not a default: price the rate this contract carries.

## Mob/demob: the workup figure is not the quotable figure

Mob and demob bill as a **lump sum — a flat fee charged regardless of what actually happens during
the mobilization.** The workup still builds it up from equipment miles, crew travel labor and driver
per diem, but **that build-up exists for internal cost and profit visibility only.** What may be
*billed* is whatever the governing contract allows, and a contract frequently caps it below the
built-up cost. The workup is a template used across every facility; the contract is per-customer, so
the two legitimately disagree.

- **Never quote the workup's mob/demob number without checking it against this contract.** It is an
  input to the margin picture, not an output to the customer.
- **Do not reconcile mob/demob between workup and quotation.** A gap equal to a whole number of
  mob/demob units is the **expected signature of a capped lump sum, not an error.** Reconcile the
  execution lines — decoke, labor and per diem, materials — and treat mob/demob as contract-governed.
- **A multi-truck job may carry mob/demob per truck.** Whether it does is a contract and scope
  question, not arithmetic — ask rather than derive. Observed on DSP26058, where two truck pages each
  carried the same lump sum against a workup counting it once.

### The costing build-up

Basis: Deer Park, TX shop to facility, one-way miles per trip. Mob and demob are calculated
separately; demob mirrors mob as the return trip. Presented as **two lump-sum line items.**

1. **Equipment travel** — one-way miles x the contract mileage rate x number of equipment pieces
   traveling. That rate **includes driver labor**, so drivers carry no separate travel-labor line.
   Confirm the rate per job. **One driver per piece — drivers = pieces traveling.**
2. **Driver per diem** — drivers x drive-days x the contract per-diem rate. `Drive-days = total
   one-way drive time / ~10 hrs per day`, rounded up; **any drive over 1 hour accrues at least one
   per diem**, and per diem accrues per driver per drive-day (2 drivers x 2-day haul = 4 per diems).
3. **Non-driver crew travel** — `(total crew - drivers) x the Crew Travel (non-driver) rate x actual
   travel hours` (drive or air; typically 8, occasionally as low as 1). That is the only travel-labor
   rate on the table, since drivers are covered by the mileage line. **Precedence: a travel rate
   stated by the governing contract or the bid instructions governs, whatever figure it carries —
   including one that happens to equal a role rate.** Only where none is stated does the baseline
   apply, and there the point holds that **travel labor is not billed at the traveller's role rate by
   default.** Each non-driver also receives exactly one day of per diem. **Non-driver travel never
   exceeds one day.**
4. **Travel ancillaries** — rental cars, flights and other travel rentals at the quoted day/unit rate
   plus contract third-party markup.

Costing is distinct from scheduling. The Duration Model governs how mob/demob occupies the schedule;
it does not set price, and a schedule figure never becomes a quotation line.

## Safety boundaries

Never invent a rate. If the governing contract does not carry the rate you need, say so and stop.
Show every hour x rate calculation in a working note before producing a quotation table. Flag
discrepancies; never adjust a number to make a total reconcile. Propose-only — nothing you produce
leaves for a customer without Jesse reading it first.
