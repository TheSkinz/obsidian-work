---
type: task
status: open
created: 2026-07-23
tags: [pointer-dead, source-files, estate-hygiene]
---

# Three dead source-file pointers to re-point

Surfaced 2026-07-23 by the new POINTER-DEAD lint rule (built this session — see [[2026-07-23-triage-vault-architecture-first-principles]]). The OneDrive estate reorg (`Desktop\` → `Desktop\Facilities\`) broke four recorded bid trails; DSP26080 was re-pointed in-session, these three could not be located in a bounded search. Each currently reads as a standing lint warning — filed here so it reaches you actively rather than sitting in the ~37-warning backlog.

You know where these archives went; a minute each. Open the quote note's `## Source Files` section, fix the path, and the warning clears on the next lint run.

| Quote note | Last-recorded path (dead) |
|---|---|
| [[DSP25084]] | `C:\Users\Jwuts\OneDrive\Desktop\Business Archive\2026\Exxon Baytown PS8\DSP# 25084 Rev 2 PS8 F-802 Furnace Decoke 2 TriMax.pdf` |
| [[DSP26039]] | `C:\Users\Jwuts\OneDrive\Desktop\Exxon Baytown_HU9-F301_371\ExxonMobil Baytown HU9 Unit\Quote & Workup\` |
| [[DSP26058]] | `C:\Users\Jwuts\OneDrive\Desktop\Marathon Garryville Bid\FW_ {External} RFQ – 1Q2027 TAR Pigging Services (Garyville Refinery)\1Q27 Pigging Docs\Submit\` |

Note there is now a `Desktop\Facilities\Business Archive\` and a `Desktop\Facilities\Exxon Baytown\` — the DSP25084 and DSP26039 targets likely moved under one of those. DSP26058's Marathon folder was not found under `Desktop\` at all; it may have gone to SharePoint (canonical for job docs per the 2026-07-22 audit) or been archived.

**Watch for the U+00A0 gotcha:** DSP26080's folder name ended in an invisible non-breaking space that broke every retyped path until the folder was renamed. If a path looks right but still won't resolve, check for a trailing invisible character on the folder name.
