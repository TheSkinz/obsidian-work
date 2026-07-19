---
type: reference
tags: [pricing, internal]
source: Six most recent DSP# Excel workups, analyzed 2026-07-19
verified: never
confidence: low
last-updated: 2026-07-19
related:
  - rfq-intake-protocol
---

# Internal Cost Model

**Internal cost only — never appears in a client-facing document.** Bill rates are contract-specific and live on the quote note or its governing contract, not here; see [[rfq-intake-protocol]] and the rate-grain review note.

> [!warning] These figures are approximations, not measured cost.
> Per Jesse, 2026-07-19: the cost rates in the estimating workups exist to give a **general perception of cost and profit on a project**, and are known to be inaccurate. He intends to revise them. Nothing below is a validated cost.
>
> **Legitimate use:** comparing projects to each other on a consistent basis, sanity-checking that a bid is in the normal shape, seeing which categories carry margin *relative to one another*.
>
> **Illegitimate use:** treating any margin figure here as a floor, a stop price, or a justification for how far a rate can be cut. The model cannot answer "how low can we go" — it was never built to.

**What "cost" means here:** hardcoded standard rates carried in the estimating workbooks. Not finance-certified, not burdened — no burden %, G&A, fuel, or ownership amortization layer exists in any workup — and per the warning above, not verified against actual cost either.

**Units match the bill unit** so line margin computes directly: hourly for equipment and labor, per person-day for per diem, per each for pigs, per mile for equipment travel. The units are sound even where the values are not.

**The rates are identical across all six workups** spanning Jan–Jul 2026, two facilities, and three contract regimes; only bill rates and quantities moved. Read this as *the values are a shared unrevised assumption*, not as evidence that real cost is uniform across facilities and equipment. Whether cost genuinely is company-wide is an open question these workbooks cannot answer.

---

## Tier 1 — the four families that drive margin

| Line | Cost | Unit |
|---|---:|---|
| TriMax Pumper — ops (rig-in / pig / smart pig) | 184.00 | $/hr |
| TriMax Pumper — stand-by (and rig-out, see anomaly) | 100.00 | $/hr |
| Project Manager | 70.00 | $/hr |
| Day Supervisor | 50.36 | $/hr |
| Night Supervisor | 50.36 | $/hr |
| Operator | 47.63 | $/hr |
| Per Diem | 130.00 | $/person-day |
| DEF | 100.00 | $/shift |

### Pig cost catalog

Charge = cost × (1 + markup).

| Size | Cost ($/ea) |
|---|---:|
| 4" Pin | 59.00 |
| 4.125" Pin | 59.00 |
| 4.25" Pin | 64.90 |
| 5" Pin | 89.70 |
| 5.25" Pin | 94.40 |
| 6" Pin | 118.00 |
| 6.25" Pin | 129.80 |
| 6.5" Pin | 142.80 |
| 8" Pin | 230.10 |
| 8.25" Pin | 247.80 |
| 10" Pin | 483.80 |
| 10.25" Pin | 531.00 |

---

## Tier 2 — mob/demob and support equipment

| Line | Cost | Unit |
|---|---:|---|
| Equipment travel (pumper / support / filter) | 1.60 | $/mile |
| Crew truck travel | 1.60 | $/mile |
| Driver travel labor | 31.34 | $/hr |
| Non-driver travel labor | 31.34 | $/hr |
| Mob per diem (driver or operator) | 130.00 | $/day |
| Support Unit | 3.45 | $/hr |
| Filter — pumping | 130.00 | $/hr |
| Filter — stand-by (Exxon workups) | 20.00 | $/hr |
| Filter — stand-by (Formosa workups) | 50.00 | $/hr |
| Crew Truck | 3.37 | $/hr |
| 4×3 Trash Pump (Exxon, hourly) | 50.00 | $/hr |
| 4×3 Trash Pump / compressor (Formosa, shift-billed) | 50% of shift bill rate | — |

Local Baytown work often runs 0 mob miles, so mob cost is mostly travel labor plus per diem rather than equipment mileage. Mob/demob remains the lump-sum variance bucket regardless of its size.

---

## Tier 3 — burden and overhead

**Not present in any workup.** No burden %, G&A, fuel schedule, or equipment ownership amortization exists in the estimating template. Obtain from finance separately if a true burdened floor is ever required.

---

## Margin structure — read as shape, not as numbers

Every percentage below inherits the accuracy warning at the top. What survives the caveat is the *ordering* and the *structural* claims, not the values.

| Category | Apparent margin | How much to trust it |
|---|---|---|
| Equipment | 50–70% | Directional only — the cost input is the least validated figure in the model |
| Labor | 17–28% | Directional, though labor cost is likelier to be close since it derives from wages |
| Per Diem | 13.3% | Arithmetic from an assumed $130 against a $150 contract line — the *spread* is soft, but per diem is genuinely near pass-through |
| Materials (pigs, DEF) | ≈ markup only | **Structurally true regardless of cost accuracy** — charge is defined as cost × (1 + markup), so the margin *is* the markup by construction |

The one claim that holds independent of the numbers: materials margin is the markup, by definition, so materials cannot absorb a discount no matter what the underlying cost turns out to be. Per diem is close to the same, being a near pass-through against a fixed contract line.

Beyond that, the apparent picture is that equipment carries most of the margin and would be the natural place to concede in a competitive bid. **Do not act on that without better cost data.** If equipment cost is understated, the real room is smaller than it looks — and equipment cost is exactly the figure most likely to be a placeholder.

Blended workup margin ranged 42.0%–54.5% across the six files, with DSP26058 at 44.3% from a separate source. This is a useful consistency check that a new bid is in the normal *shape*. It is **not** a floor.

---

## Known anomalies — verify before relying on these lines

**Rig-out cost chains from stand-by, not ops.** In the workbook the rig-out cost rate links to the stand-by rate ($100/hr) rather than the ops rate ($184/hr): `AD26=184 → … → AD30=100 → AD31=AD30`. If rig-out genuinely consumes the same resources as rig-in, this understates rig-out cost by $84/hr and overstates that line's margin on every job. Unresolved — either intentional or a link error. Rig-out is a fixed ~6 hr event on essentially every job, so the error is small per job but systematic across all of them.

**Filter stand-by bill rate is inconsistent within one facility.** DSP26071.2 bills filter stand-by at $35/hr; other Exxon Baytown workups bill it at $150/hr against the same $20/hr cost. That is a 4× spread on the same line at the same site. Either a negotiated difference or an error worth catching.

**Cost rates have not moved since at least January 2026** and are known to be approximate. Jesse intends to revise them. Until that happens, treat the whole Tier 1/Tier 2 table as provisional.

## What would make this model trustworthy

In rough order of value, and none of it derivable from the workbooks:

1. **Real equipment cost per hour for the TriMax pumper.** It is the largest single cost line, carries the most apparent margin, and is the least validated number here. Fixing this one figure moves the model more than everything else combined.
2. **Actual burdened labor cost by role** — wages plus burden, rather than the assumed standard rate.
3. **Real per-unit pig cost** from purchasing, against the catalog above.
4. **Whether cost genuinely varies by facility or job type**, which the current uniform placeholders make impossible to see.
5. **A burden/overhead layer** (Tier 3), absent entirely, needed before any figure here can be called a floor.

---

## Source Basis

| Source | Authority | Date | Notes |
|---|---|---|---|
| `Desktop\Facilities\DSP-workup-rates-vs-cost.md` | Primary (Jesse's analysis) | 2026-07-19 | Extraction from six most recent DSP# workbooks: 26071.2, 26085, 26061, 26075, 26068.1, 25156 |
| Underlying workbooks | Primary | 2026-06 to 2026-07 | Exxon Baytown and Formosa Point Comfort; per-file totals cross-checked against Excel cached values |
| `DSP26058.md` Internal Financials | Corroborating | 2026-05-12 | Marathon Garyville, 44.3% blended — consistent with the observed band |

To refresh from a future workup: open the project-named cost tab (skip Insert Quote, Pricing Table, Heater Data), read the hardcoded Cost Rate column in the first heater block, the Mob Q-column costs, and the pig catalog with its markup, then diff against the tables above.

---

## Change Log

| Date | Change | Trigger |
|---|---|---|
| 2026-07-19 | Populated from workup analysis; restructured to hourly units, added margin-structure and anomalies sections | File had been an empty skeleton with day-rate units that could not compute line margin against hourly bill rates |
