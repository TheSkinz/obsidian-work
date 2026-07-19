---
type: facility
facility-id: <Client>-<City>-<ST>
  # ↑ JOIN KEY — heater cards and job cards reference this value in their facility frontmatter.
client: <Client name>
city: <City>
state: <ST>
last-updated: <YYYY-MM-DD>
tags: [facility, <Client>]
---

<!--
FACILITY TEMPLATE — site-level facts only.
This file holds information that belongs to the SITE, not to any single heater or job:
access procedures, site contacts, shared equipment constraints, facility-specific safety
requirements, and lessons learned that apply across all heaters at this location.

If a fact applies to a specific heater (tube geometry, metallurgy, pig sizing) it belongs
on the heater card, not here. If it applies to a specific job (durations, standby causes,
overages) it belongs on the job card or in the heater card's Field Notes under that job.

The test: "would this still be true if we decoked a DIFFERENT heater at this site?" If yes,
it's a facility fact. If no, it belongs on the heater card or job card.
-->

# <Client> — <City>, <ST>

---

## Site Access

| Field | Value |
|---|---|
| Address | |
| Gate / check-in | |
| Badge / access requirements | |
| Site contact | |
| Site contact phone | |
| Escort requirements | |

---

## Site Equipment and Constraints

<!--
Shared resources at this facility that affect planning/execution across heaters.
Example: crane availability, filter press capacity, water supply source/limitations.
-->

| Resource | Detail |
|---|---|
| Crane | |
| Filter press | |
| Water supply | |

---

## Site Safety and Procedures

<!--
Facility-specific safety requirements beyond standard USADeBusk SOPs.
-->

---

## Rates — do not add

<!--
Deliberately absent. Rates are a property of a CONTRACT, not of a facility:
one site can carry several concurrent contracts from different departments
(turnaround, maintenance, procurement, capital projects) at different rates,
and rates are also adjusted per bid to stay competitive.

Rates live on the quote note that used them, identified by its `rate-basis`
field. Do not backfill a rates section here. Existing facility cards that
carry one (Baytown, Navajo, Ponca City, Port Arthur) label it with the
specific quote and heaters it came from — keep that labeling; those blocks
are historical record of one contract, not a facility rate schedule.

Decided 2026-07-19, proposal A of 06-insights/2026-07-19-rate-model-grain-review.
-->

---

## Heaters at This Facility

<!--
Auto-populated by Dataview query or maintained manually — list of heater cards at this site.
Wikilinks preferred so graph view works.
-->

- [[<HeaterTag>]]

---

## Notes
