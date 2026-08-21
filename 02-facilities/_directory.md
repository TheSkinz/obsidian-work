---
type: index
status: active
created: 2026-07-05
tags: [facilities, directory]
---

# Facilities Directory

**Create-on-first-fact rule.** A facility gets files only when there is real content — rates, contacts, heater cards, or job actuals. Create fresh from `04-knowledge/_facility-template.md` when the first fact arrives; there's no scaffold-recovery step to think about anymore. (An older, incompatible duplicate at `templates/_facility-template.md` was removed 2026-07-06 — this is now the only facility template.) **2026-07-06:** dropped the pre-scaffolded "known sites, no data yet" list below (and the empty directories it produced) — that was a leftover from an earlier vault concept and served no purpose once the facility-data lane moved to low-ceremony, capture-what-you-have (see `04-knowledge/knowledge-system-governance.md`).

## Facilities

| Client | Site | What's there |
|---|---|---|
| ExxonMobil | Baytown, TX | Facility overview `_facility.md` + heater cards [[F-301]], [[F-371A]], [[F-802]] (Task Duration actuals); proposals [[DSP25084]], [[DSP26039]] |
| Marathon | Garyville, LA | Facility overview `_facility.md` + heater cards [[210-1401A]], [[210-1402B]], [[210-1403A]], [[210-1404B]]; [[DSP26058]] — lost to competitor (1Q2027 TA, two Double Pumpers) |
| Syncrude | Mildred Lake (Fort McMurray), AB | Facility overview `_facility.md` + draft card [[7-1-F-1]] (renamed 2026-07-06 from "7-2 F-1" — Jesse confirmed 7-1 F-1 is correct). Job History: CND24002 (2024, not yet ingested) and CND25004 (2025, full field data) — two separate real jobs on this heater |
| HF Sinclair | Artesia, NM (Navajo Refinery) | Facility overview `_facility.md` + pending quote [[DSP26080]] (quote-specific rates, Feb. 2027) + draft cards [[H-2421]], [[H-30]], [[H-2501]] (verify on use; H-2501 source note truncated) |
| P66 | Ponca City, OK | Facility overview `_facility.md` (contracted rates, DSP25061) + heater cards [[H-28]], [[H-29]] (Task Duration actuals, USA25041 — combined job, not split per heater); proposal doc [[DSP26030_H28_H29|DSP26030]] |
| Westlake South | Westlake, LA | **New 2026-07-27.** Filed under the **Westlake Chemical** company tier (`02-facilities/Westlake-Chemical/Westlake-LA/`) alongside Geismar and Plaquemine, but `client:` stays **Westlake South** — the name the customer rep signs with. Facility overview `_facility.md` + heater card [[H-101]] — H-101 TE II EDC Furnace, also called TE-II / 71-1686 (EDC pyrolysis, Tri-Ethane unit; geometry from the governing 1976 Selas as-builts, coil confirmed as-built by Jesse; 1989 data sheet superseded and conflicts on the radiant only). New to the vault, **not** new to USADebusk — bid and lost here in 2024, and the governing contract/rates live outside the vault. Site formerly PPG Industries; do not create a second record under PPG, Lake Charles, or TE-II. Quote # pending. |
| Formosa | Point Comfort, TX | **New 2026-07-27.** Facility overview `_facility.md` + heater card [[VR-401C]] (MM2 unit, TP-347H stainless, 3,213 ft single circuit). From `DSP#26075` (ITB V84SU, July 2026 decoke — bid only, no vault note) — **submitted and lost**, no job executed, no contracted rates. Card carries an unresolved 5.0" OD convection tube flagged in the source data; verify against the as-built before any future pigging. |
| PBF | Toledo, OH | **New 2026-07-27.** Facility overview `_facility.md` + heater card [[H-311]]. From `DSP#25141` (bid 2025-11-11, $108,204.70 T&M, Spring 2026 outage — bid only, no vault note) — **award outcome unknown, confirm**. Bid as a third party under **Steady-Flux**, not directly to PBF, so the DSP#25141 rates are not a PBF contract precedent. Street address is in Oregon, OH; the bid names the site Toledo — do not create a second record under Oregon-OH. |
| Flint Hills | Corpus Christi, TX | **New 2026-07-27.** Facility overview `_facility.md` + heater cards [[01-BA-105]] (Raw Oil Charge Preheater / "Cat Feed") and [[02-BA-201]] (Debutanizer Reboiler, FCCU) + quote note [[DSP26006]] (quote-specific emergency rates, Jan 2026 — **not** a facility contract schedule). Both cards carry USA26005 Task Duration actuals from the eleven service receipts; job quoted, executed, and invoiced ($106,420.31 vs $102,634.00 quoted, overrun entirely customer-caused stand-by). **Coil footage is unrecovered on both heaters** — no ft/hr for the rollup until Jesse supplies it. Client is also called FHR; do not create a second record under that name. |
| Valero | Port Arthur, TX | **New 2026-07-06.** Facility overview `_facility.md` (contracted + actual-billed rates, DSP26035/USA26025) + heater cards [[H-102A]], [[H-102B]] (real tube geometry, connection info, and per-heater Task Duration actuals from the USA26025 job report; emergency mobilization, 59% cost overrun) |
