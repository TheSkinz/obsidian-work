---
title: OneDrive — Company Folder Structure
type: decision
tags: [ops, file-management, onedrive, reference]
created: 2026-06-06
updated: 2026-06-06
related:
  - "[[onedrive-facilities-structure]]"
---

# OneDrive — Company Folder Structure

Canonical reference for `USADeBusk\Company\` and `USADeBusk\_Pending-Archive\`, established June 2026 as Part 1 of the migration from `Desktop\Refineries\`.

**Root path:** `C:\Users\Jwuts\OneDrive\USADeBusk\`

---

## Folder Structure

```
USADeBusk\
  Company\
    SOPs\
    Templates\
    Canada-Compliance\
    Equipment\
      H2-Convection-Box\
      Spools\
  _Pending-Archive\
    00_History\
```

---

## What Lives Where

**`Company\SOPs\`** — Internal USADeBusk SOPs. Migrated from `Refineries\USADeBusk\SOPs\`. Contains 6 files: DeBusk Elevated Rig-In Procedure (docx+pdf), Pigging Truck with Filter Press SOP, USADebusk Lodged Pig Removal SOP-001-REV0 (docx+pdf), USADebusk OPS RIGIN Checklist-001_REV0.

**`Company\Templates\`** — Empty at migration. Reserved for document templates.

**`Company\Canada-Compliance\`** — Canadian operational docs. Migrated from `Refineries\01_Debusk Canada\`. Contains: Debusk Services Canada Lodged Pig Removal SOP-001-REV0 (docx+pdf).

**`Company\Equipment\H2-Convection-Box\`** — H2 convection box reference files. Migrated from `Refineries\01_USADebusk H2 Convection Box\`. Contains coil profiles, heater drawings, and photos for H-2_233 and H-H2_373.

**`Company\Equipment\Spools\`** — Spool reference files. Migrated from `Refineries\01_USADebusk_Spools\`. Contains Spool Inventory.xlsx, 4 spool images, a PDF, and a text extraction file.

**`Company\` (root loose files)** — Two pricing spreadsheets routed here from `00_History` root:
- `Proposed Scheduled Pricing 1 year- 7 percent.xlsx`
- `Proposed Scheduled Pricing 2 year - 13 percent.xlsx`

**`_Pending-Archive\00_History\`** — Historical project files 2013–2022, staged for Phase 2 routing. 3,242 files across subfolders: 2013–2022 Projects, A-US Gulf, Debusk - Copy, Jason Software. Root holds: `Pig Timer2.xlsm` and `US Template - Jesse Utsey - Director US Pigging Decoking.pdf`.

---

## Migration Source Mapping

| Source (`Refineries\`) | Destination (`USADeBusk\`) |
|---|---|
| `USADeBusk\SOPs\` | `Company\SOPs\` |
| `01_Debusk Canada\` | `Company\Canada-Compliance\` |
| `01_USADebusk H2 Convection Box\` | `Company\Equipment\H2-Convection-Box\` |
| `01_USADebusk_Spools\` | `Company\Equipment\Spools\` |
| `00_History\` | `_Pending-Archive\00_History\` |

**Permanently deleted:**
- `00_History\jutsey\` — 548-item Windows user profile backup (Favorites, Links, Searches, .url/.lnk files). No business value.
- 4 empty source dirs post-move: `USADeBusk\`, `01_Debusk Canada\`, `01_USADebusk H2 Convection Box\`, `01_USADebusk_Spools\`.

---

## Migration Script

`C:\Users\Jwuts\OneDrive\Desktop\Refineries\migrate.ps1`

Supports dry-run (`.\migrate.ps1`) and execute (`.\migrate.ps1 -Execute`) modes. Uses `robocopy /E /MOVE` for all folder transfers.

**Known issue:** robocopy `/MOVE` on OneDrive-synced paths can drop root-level loose files to the parent Desktop directory rather than the destination. The 4 root files of `00_History` landed at `C:\Users\Jwuts\OneDrive\Desktop\` and were manually routed to their correct destinations after the script completed.

---

## Phase 2 — Pending

`_Pending-Archive\00_History\` contains 2013–2022 historical project files. Phase 2 routing (by year/client to `Facilities\`) is a separate session.
