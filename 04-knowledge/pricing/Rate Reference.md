---
type: reference
tags: [pricing, rates]
last-updated: 
source: USADeBusk internal rate schedule
verified: never
---

# Standard Rate Reference

_Base bill rates before facility-specific contract negotiation. See each facility
file for contracted rates that override these. Fill every cell below — a blank
means "use baseline," which is the current state and why every proposal
currently guesses._

## Crew Day Rates (Bill)
_12-hr shift, per skill's Labor pricing structure._

| Configuration | Day Rate ($) | Notes |
|---------------|----------|-------|
| 2-man crew | | |
| 3-man crew | | |
| 4-man crew | | |

## TriMax Pumper — Hourly Task Rates (Bill)
_Billed by task, not a flat day rate — matches Section 9 Hourly Charge Out Rates._

| Task | Rate ($/hr) | Notes |
|---|---|---|
| Rig-In | | |
| Pig | | |
| Smart Pig | | |
| Stand-By | | |

## Filter Press — Hourly Task Rates (Bill)
_Two rates only: pumping vs. non-pumping/stand-by (rig-in, rig-out, waiting)._

| Task | Rate ($/hr) | Notes |
|---|---|---|
| Pumping (TriMax actively pigging) | | |
| Non-Pumping / Stand-By | | |

## Standby / Downtime — Applicability by Cause
_Standby applies only to TriMax Pumper and Filter Press rate lines above (see
usadebusk-estimating). This table is NOT a third rate schedule — it records
whether each cause is billable at the standby rates above, per contract._

| Scenario | Billable? (Y/N) | Notes |
|----------|------|-------|
| Weather hold | | |
| Client delay | | |
| Equipment downtime | | |

## Notes

**2026-07-06 SharePoint pull:** searched for a standalone base/standard rate
schedule — none exists. Only facility-specific contracted rates were found
(now recorded on each facility's `_facility.md`: ExxonMobil Baytown, HF
Sinclair Navajo, P66 Ponca City). None of the source documents contained crew
day rates, a base TriMax/Filter Press day rate, or standby-cause rates
(weather/client/equipment) — those cells above are still genuinely blank and
only Jesse has the numbers.

**2026-07-06 QB Ticket Breakdown pull:** cross-checked quoted vs. actual
billed rates for three jobs (F-802, Valero PA H-102A/B, P66 H-28/H-29).
Confirms crew/equipment rates genuinely vary by facility and even drift
within the same job from what was quoted (e.g., Valero PA billed TriMax
pigging at $550/hr vs. $500/hr quoted; ExxonMobil billed the PM role at the
Day Supervisor rate rather than the quoted PM rate). This is why a single
company-wide "base" rate can't substitute for facility-specific figures —
see each facility's `_facility.md` for the actual numbers found.
