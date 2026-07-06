---
type: index
status: active
created: 2026-07-05
tags: [facilities, directory]
---

# Facilities Directory

All known client sites, whether or not they have vault data yet.

**Create-on-first-fact rule.** A facility gets files only when there is real content — rates, contacts, heater cards, or job actuals. The empty pre-scaffolded overviews (blank rate/contact/heater tables, no data) were archived 2026-07-05 to `archive/02-facilities-scaffolds/` with their paths preserved. Recover any one with `git mv` back into place when its first real fact arrives, or create fresh from `templates/_facility-template.md`. See [[vault-source-of-truth]] for the edit guardrail.

## Live — facilities with data

| Client | Site | What's there |
|---|---|---|
| ExxonMobil | Baytown, TX | Facility overview `_facility.md` + heater cards [[F-301]], [[F-371A]], [[F-802]] (Task Duration actuals); proposals [[DSP25084]], [[DSP26039]] |
| Marathon | Garyville, LA | Facility overview `_facility.md` + heater cards [[210-1401A]], [[210-1402B]], [[210-1403A]], [[210-1404B]]; proposal [[DSP26058]] (1Q2027 TA, two Double Pumpers) |
| Syncrude | Mildred Lake (Fort McMurray), AB | Facility overview `_facility.md` + draft card [[7-1-F-1]] (renamed 2026-07-06 from "7-2 F-1" — Jesse confirmed 7-1 F-1 is correct). Job History: CND24002 (2024, not yet ingested) and CND25004 (2025, full field data) — two separate real jobs on this heater |
| HF Sinclair | Artesia, NM (Navajo Refinery) | Facility overview `_facility.md` (contracted rates, DSP26080) + draft cards [[H-2421]], [[H-2501]] (verify on use; H-2501 source note truncated) |
| P66 | Ponca City, OK | Facility overview `_facility.md` (contracted rates, DSP25061) + heater cards [[H-28]], [[H-29]] (Task Duration actuals, USA25041 — combined job, not split per heater); proposal doc [[DSP26030-H28-H29-Decoke-Proposal-May2026|DSP26030]] |
| Valero | Port Arthur, TX | **New 2026-07-06.** Facility overview `_facility.md` (contracted + actual-billed rates, DSP26035/USA26025) + heater cards [[H-102A]], [[H-102B]] (real tube geometry, connection info, and per-heater Task Duration actuals from the USA26025 job report; emergency mobilization, 59% cost overrun) |

## Known sites — no vault data yet

Scaffolds archived 2026-07-05; recreate on first fact. **FHR and Flint-Hills Corpus Christi were duplicate scaffolds for the same facility** (Flint Hills Resources) — use **Flint-Hills** as the client name when data arrives.

| Client | Sites |
|---|---|
| BASF | Beaumont TX, Bishop TX |
| BP | Cherry Point WA, Whiting IN |
| Big West Oil | Salt Lake City UT |
| Buckeye | Corpus Christi TX |
| CHS | McPherson KS |
| CITGO | Corpus Christi TX |
| Cenovus | Toledo OH |
| Chevron | Geismar LA, Pasadena TX |
| Delek | Big Spring TX, El Dorado AR |
| Denka | La Place LA |
| Energy Transfer | Mont Belvieu TX |
| ExxonMobil | Baton Rouge LA |
| Flint-Hills (FHR) | Corpus Christi TX, Pine Bend MN |
| HCC | Indianapolis IN |
| HF Sinclair | Rawlins WY, Tulsa OK |
| Hunt | Tuscaloosa AL |
| Invista | Victoria TX |
| Magellan-ONEOK | Corpus Christi TX |
| Marathon | Catlettsburg KY, Dickinson ND, Mandan ND, St Paul Park MN, West Union WV |
| ONEOK | Mont Belvieu TX |
| P66 | Hallettsville TX, Linden NJ, Sweeny TX, Westlake LA, Wood River IL |
| PEMEX | Deer Park TX |
| Par Pacific | Tacoma WA |
| Targa | Mont Belvieu TX |
| Valero | Benicia CA, Houston TX, Meraux LA, Sunray TX, Texas City TX, Three Rivers TX, Wilmington CA |
