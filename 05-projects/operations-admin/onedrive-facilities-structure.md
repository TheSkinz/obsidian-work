---
title: OneDrive — Facilities Folder Structure
tags: [ops, file-management, onedrive, reference]
created: 2026-06-06
updated: 2026-06-06
---

# OneDrive — Facilities Folder Structure

Canonical reference for the `USADeBusk\Facilities` file hierarchy, established June 2026. Migrated from legacy `Desktop\Refineries` structure.

**Root path:** `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\`

---

## Naming Convention

Folder names follow `[Company] [City] [State]` format. Use the operating company name, not the parent, where applicable (e.g., PEMEX not IMP; CITGO not Citgo Petroleum).

Each facility gets three standard subfolders:

```
[Facility]\
  Reference\
    Drawings\
  Bids\
  Jobs\
```

Exceptions: facilities with no active job history get `Bids\` only.

---

## Facilities — Full Structure

| Folder Name | Notes |
|---|---|
| BASF Bishop TX | |
| BP Cherry Point WA | |
| BP Whiting IN | |
| Cenovus Lima OH | |
| CHS Laurel MT | |
| CITGO Corpus Christi TX | |
| CITGO Lemont IL | |
| Delek Big Spring TX | |
| Ecopetrol Bogota Colombia | |
| Ergon Newell WV | |
| ExxonMobil Baton Rouge LA | |
| ExxonMobil Baytown TX | Active bids: Baytown 730 2027, HU9 F-301 2027, NRU F9A 2026 |
| Flint Hills Corpus Christi TX | |
| Formosa Point Comfort TX | |
| FPL Turkey Point Homestead FL | **Bids only** |
| Hunt Tuscaloosa AL | |
| Invista Victoria TX | |
| Kinder Morgan Galena Park TX | **Bids only** |
| Marathon Catlettsburg KY | |
| Marathon Detroit MI | |
| Marathon Garyville LA | |
| MPLX West Union WV | |
| NWR Redwater AB | |
| ONEOK Mont Belvieu TX | |
| P66 Bayway NJ | |
| P66 Ferndale WA | |
| P66 Ponca City OK | |
| P66 Westlake LA | formerly "P66 Lake Charles" in source |
| P66 Wood River IL | |
| Par Pacific Kapolei HI | |
| PBF Paulsboro NJ | |
| PBF Toledo OH | |
| PEMEX Deer Park TX | |
| Sinclair Artesia NM | |
| Sinclair Rawlins WY | |
| Suncor Commerce City CO | |
| Suncor Edmonton AB | |
| Targa Mont Belvieu TX | |
| Tesoro Mandan ND | |
| Valero McKee TX | |
| Valero Meraux LA | |
| Valero Port Arthur TX | |
| Westlake Westlake LA | |

---

## Active Job/Bid Subfolders (as of 2026-06-06)

```
ExxonMobil Baytown TX\Bids\Baytown 730 2027
ExxonMobil Baytown TX\Bids\HU9 F-301 2027
ExxonMobil Baytown TX\Bids\NRU F9A 2026
ExxonMobil Baytown TX\Jobs\USA26007 2026-02
ExxonMobil Baytown TX\Jobs\USA26022 2026-05
Invista Victoria TX\Jobs\USA26006 2026
MPLX West Union WV\Jobs\USA25055 2025-10
P66 Bayway NJ\Jobs\USA26021 2026-03
P66 Ponca City OK\Bids\H-28 H-29 Cokers 2026
P66 Ponca City OK\Jobs\USA25041 2025
P66 Westlake LA\Jobs\USA26018 2026-05
Westlake Westlake LA\Bids\Furnace Pigging 2024-10
Westlake Westlake LA\Bids\EDC Furnace 2025
```

---

## Migration Notes (Refineries → Facilities, 2026-06-06)

**Script:** `C:\Users\Jwuts\OneDrive\Desktop\Migrate-Facilities.ps1`

Corrections discovered during migration that were not obvious from the spec:

- **Westlake Chemical DSP items** were individual xlsx files, not subfolders. Moved as files; remaining folder content (Final, RE_ Bids) merged to Westlake Westlake LA root.
- **2026 Exxon Baytown folder names** had "Exxon Baytown" prefix not reflected in the audit: `Exxon Baytown HU9 F-301 2027`, `Exxon Baytown NRU Job walk`, `Exxon Baytown_F9A_ April 2026`, `Exxon Baytown PS8`.
- **Valero McKee .zip** was at the `2026\` root, not inside the `Valero McKee\` subfolder. Extracted 5 loose files and merged to Valero McKee TX.
- **Suncor Canada .zip** was in `Suncor\` root alongside the `Suncor Canada\` folder — deleted per spec after folder was moved.
- **USA25041 P66 PCR H28 H29.pdf** was found inside the Ponca City bid folder and routed to `P66 Ponca City OK\Jobs\USA25041 2025\` before the bid folder was moved.

**Remaining at Refineries root (not migrated):** loose files — DSP estimates, SOPs, photos, job reports, and reference ZIPs. Not scoped for this migration. One to note: `DSP# 26065 P-66 Lake Charles H-15001 & H-14 Fall 2026.xlsx` belongs in `P66 Westlake LA\Bids\` if you want to route it.

---

## Loose File Routing Rules

Files found at `2026\` root were matched by filename pattern and routed:

| Pattern | Destination |
|---|---|
| `DSP#26005` | ExxonMobil Baytown TX\Bids\NRU F9A 2026 |
| `DSP#26030` | P66 Ponca City OK\Bids\H-28 H-29 Cokers 2026 |
| `USA26006` | Invista Victoria TX\Jobs\USA26006 2026 |
| `Meraux` + `safety` | Valero Meraux LA |
| `V7J3U` | Formosa Point Comfort TX\Bids |
