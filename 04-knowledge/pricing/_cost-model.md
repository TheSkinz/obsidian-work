---
type: reference
tags: [pricing, internal]
source: Six most recent DSP# Excel workups, analyzed 2026-07-19
verified: 2026-07-19
last-updated: 2026-07-19
related:
  - rfq-intake-protocol
---

# Internal Cost Model

**Internal cost only — never appears in a client-facing document.** Bill rates are contract-specific and live on the quote note or its governing contract, not here; see [[rfq-intake-protocol]] and the rate-grain review note.

**What "cost" means here:** these are the hardcoded **standard / divisional transfer cost** rates carried in the estimating workbooks. They are *not* a finance-certified burdened schedule — there is no separate burden %, G&A, fuel, or ownership amortization layer in any workup. Treat these as the estimating floor, not automatically as the company stop price. Settle the difference with finance before using this to justify a below-standard bid.

**Units match the bill unit** so line margin computes directly: hourly for equipment and labor, per person-day for per diem, per each for pigs, per mile for equipment travel.

**Cost is company-wide and stable.** Across all six workups spanning Jan–Jul 2026, two facilities, and three contract regimes, every internal cost rate was identical. Only bill rates and quantities moved. This is why cost belongs in one vault note while rates do not.

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

## Margin structure — where the flex actually is

Observed across all six workups, and the most decision-relevant thing in this file:

| Category | Typical margin | Flexibility when bidding competitively |
|---|---|---|
| Equipment | 50–70% | **This is the lever.** Nearly all competitive room lives here |
| Labor | 17–28% | Limited |
| Per Diem | 13.3%, locked | None — $130 cost against a $150 contract line |
| Materials (pigs, DEF) | ≈ markup only, 7–14% | None — it *is* the markup |

Cutting price to win means cutting the equipment rate. Per diem and materials are effectively pass-through and cannot absorb a reduction; labor absorbs very little. A bid that discounts across the board is really discounting equipment while pretending otherwise.

Blended job margin has landed between **42% and 54.5%** across every workup analyzed, plus 44.3% on DSP26058 (Marathon Garyville) from a separate source. Below roughly 42% blended is outside recent precedent and worth a deliberate decision rather than a slide.

---

## Known anomalies — verify before relying on these lines

**Rig-out cost chains from stand-by, not ops.** In the workbook the rig-out cost rate links to the stand-by rate ($100/hr) rather than the ops rate ($184/hr): `AD26=184 → … → AD30=100 → AD31=AD30`. If rig-out genuinely consumes the same resources as rig-in, this understates rig-out cost by $84/hr and overstates that line's margin on every job. Unresolved — either intentional or a link error. Rig-out is a fixed ~6 hr event on essentially every job, so the error is small per job but systematic across all of them.

**Filter stand-by bill rate is inconsistent within one facility.** DSP26071.2 bills filter stand-by at $35/hr; other Exxon Baytown workups bill it at $150/hr against the same $20/hr cost. That is a 4× spread on the same line at the same site. Either a negotiated difference or an error worth catching.

**Cost rates have not moved since at least January 2026.** Nothing in the workups updated across seven months. Plausible for standard rates, but worth confirming they are still current rather than stale defaults.

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
