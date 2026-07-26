---
type: facility
facility-id: ExxonMobil-Baytown-TX
client: ExxonMobil
city: Baytown
state: TX
last-updated: 2026-07-26
tags: [facility, ExxonMobil]
---

# ExxonMobil — Baytown, TX

---

## Site Access

| Field | Value |
|---|---|
| Address | (not recorded) |
| Gate / check-in | (not recorded) |
| Badge / access requirements | (not recorded) |
| Site contact | (not recorded) |
| Site contact phone | (not recorded) |
| Escort requirements | (not recorded) |

---

## Site Equipment and Constraints

| Resource | Detail |
|---|---|
| Crane | ExxonMobil-controlled overhead crane — coordinate mobilization timing with ExxonMobil |
| Filter press | Known capacity constraint on multi-TriMax jobs; consider larger or dual press on future bids |
| Water supply | (not recorded) |

---

## Site Safety and Procedures

---

## Rate History — Baytown

<!-- Replaced the single "Contracted Rates — PS8 F-802" block on 2026-07-26. That block was
correctly labeled with its source quote per the rfq-intake-protocol rule, and carried the
same DSP25084 rates reproduced below — it was not wrong, just one column wide. Widening it
to all three Baytown quotes is what exposed DSP25123's bad filtration standby row. The old
"no rate schedule found for DSP26039" line is retired: DSP26039 does carry a full schedule. -->


**Rates at this site are per-bid, not per-facility.** Baytown bids go through different
groups and divisions, and competitive pressure varies by bid, so no single row here is
"the Baytown rate." Each quote note is authoritative for the bid it records; this table
exists to show the spread and flag outliers, not to be quoted from.

| Line Item | DSP25084 (F-802, 2025-07-15, awarded) | DSP25123 (F-901, 2026-04-06, awarded) | DSP26039 (F-301/F-371A, 2026-04-07, pending) | House standard |
|---|---|---|---|---|
| TriMax Triple — Pigging | $800/hr | $800/hr | $800/hr | $800/hr |
| TriMax Double — Pigging | $650/hr | $650/hr | — | $650/hr |
| TriMax Smart Pigging | $600/hr | $600/hr | $600/hr | $600/hr |
| TriMax Rig-In / Out / Over | $500/hr | $500/hr | $500/hr | $500/hr |
| TriMax Standby | $500/hr | $500/hr | $500/hr | $500/hr |
| Filtration | $200/hr | $200/hr | $200/hr | $200/hr |
| Filtration Standby | $150/hr | ~~$35/hr~~ → $150/hr | $150/hr | $150/hr |
| Support Unit | $35/hr | (row absent) | $30/hr | $30/hr |
| Crew Truck | $25/hr | $25/hr | $25/hr | $25/hr |
| 4×3 Pump | $1,016/shift | $1,016/shift | $85/hr | — (basis varies) |
| Project Manager | $94.75/hr | (row absent) | $94.75/hr | $94.75/hr |
| Per Diem | $150/day | $150/day | $150/day | $150/day |
| DEF | $180/shift | $180/shift | $180/shift | $180/shift |

Notes on the three cells that are not clean:

**Filtration Standby $35 on DSP25123 is an error, not a price** — resolved by Jesse
2026-07-26. The F-901 sheet was built from the F-802 template and a deleted Support Unit
row pulled its $35 up into the filtration standby cell, taking the PM row with it.
$150/hr governs. Filtration was declined before execution, so it never reached an
invoice. Detail on [[DSP25123]].

**Support Unit $35 on DSP25084 stands as what that awarded contract carried.** $30/hr is
the house standard (`04-knowledge/pricing/_cost-model.md`, `usadebusk-estimating`) and is
what the newer DSP26039 carries. Per Jesse 2026-07-26, $30 will be right for the majority
of bids, but Baytown is not one buyer — different groups and divisions, different
competitive positions. Confirm against the governing contract per bid; do not treat any
row above as a default.

**4×3 pump basis changed** between DSP25084/25123 ($1,016/shift) and DSP26039 ($85/hr).
Not reconciled — check which basis the governing contract uses before pricing it.

## Labor Rates — PS8 F-802 (USA26022, quoted vs. actual billed)

| Role               | Quoted ($/hr) | Actual Billed ($/hr) | Notes                                                                                                     |
| ------------------ | ------------- | -------------------- | --------------------------------------------------------------------------------------------------------- |
| Project Manager    | 94.75         | 64.92                | Actual QB billed PM at the Day Supervisor rate — flag before assuming $94.75 is what actually gets billed |
| Supervisor (Day)   | 64.92         | 64.92                | Matches                                                                                                   |
| Supervisor (Night) | 67.79         | 67.79                | Matches                                                                                                   |
| Operator           | 55.39         | 55.39                | Matches                                                                                                   |

Source: DSP# 25084 Rev 2 PS8 F-802 Furnace Decoke 2 TriMax.pdf (quoted);
USA26022 EXXONMOBIL F-802 TriMax Ticket Breakdown.xlsx (actual QB Sheet).

**Quote vs. Actual Overage:** Quoted $211,730.36 vs. actual billed $274,508.25
(change-order Rev 1 revised price) — $62,777.88 over. Actual combined TriMax
pigging hours (110 = TriMax4 55 + TriMax6 55) exceeded quoted 60 project hours;
standby (98 hrs combined) was not planned in the quote at all.

---

## Heaters at This Facility

- [[F-802]]
- [[F-901]]
- [[F-301]]
- [[F-371A]]

---

## Notes
