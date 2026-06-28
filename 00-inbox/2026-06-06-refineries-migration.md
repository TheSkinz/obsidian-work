---
type: session-log
date: 2026-06-06
status: complete
tags: [system, onedrive, migration, file-management]
---

# Refineries Desktop Folder Migration — 2026-06-06

## What Happened

Migrated 73 files from `Desktop\Refineries` (an unsorted working folder) into the structured `OneDrive\USADeBusk\` tree. Ran a PowerShell dry-run first, reviewed the plan, confirmed it clean, then executed.

## Migration Stats

- **Folders created:** 30 new (6 already existed)
- **Files moved:** 64
- **Files deleted:** 9 (junk/personal: timesheets, non-bill time PDFs, resume, temp files)
- **NOT FOUND:** `DDT Heater Information.xlsx` — was already gone before execution, skipped cleanly

## Folder Structure Created

All paths relative to `OneDrive\USADeBusk\`:

**Company:**
- `Company\Vendors` — NDA with Steady Flux
- `Company\Assets` — logo/rig photos
- `Company\Templates` (existed) — blank timesheet, PTO form
- `Company\SOPs` (existed) — Closed Loop Decoking SOP, Pipeline Flow Diagram
- `Company\Equipment` (existed) — equipment spec zip, pump curve

**Facilities added this session:**
ExxonMobil Baton Rouge LA, CITGO Lemont IL, CITGO Lake Charles LA, BP Whiting IN, Valero Port Arthur TX, Valero McKee TX, Valero Meraux LA, P66 Lake Charles LA, Westlake Chemical Geismar LA, Westlake Chemical Plaquemine LA, PBF Energy Torrance CA, Monroe Energy Trainer PA, Ergon Newell WV, Hunt Refining Tuscaloosa AL, BASF Bishop TX, Dow Knoxville TN, Sinclair Wyoming WY, NWR Redwater AB, Syncrude Fort McMurray AB, HF Sinclair Navajo Artesia NM, HF Sinclair Tulsa OK, Ecopetrol Bogota Colombia, Marathon Robinson IL, Flint Hills Pine Bend MN

(ExxonMobil Baytown TX, Suncor Commerce City CO, Invista Victoria TX were already scaffolded.)

## Technical Notes

Three files had whitespace anomalies in their names (double spaces, trailing spaces, apostrophe in extension). Script used `Get-ChildItem -Filter` wildcard matching for those three only; all matched exactly one file each.

Script at `C:\Users\Jwuts\migrate-refineries.ps1` — kept for reference, can be deleted.

Source folder (`Desktop\Refineries`) is now empty.

## Deleted Files

migrate.ps1, Travis Trenholm_Resume.docx, download.png, New SOP.pdf, Water Flow Final.pdf, Nonbilltime 7-8.pdf, Nonbilltime 7-9.pdf, PREVIOUS-Shipping_7012408 - Copy.pdf, Turkey Florida.xlsx
