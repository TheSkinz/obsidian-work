# Insights & Refinements Log
**Layer:** 06-insights
**Source:** Master Reference Module 10 (migrated 2026-04-25)
**Format for new entries:** `[Date] | [Module/Topic Reference] | Insight or refinement`

---

**[2026-06-13] | System — Module 10 Integration Pass complete:** All pre-approved changes from the Fable planning session applied. Skills (A1–A7), Master Reference Doc (MRD-1..5), and B1 diagrams (D1) updated. Module 10 housekeeping done — Entries 1, 4, 5, 7, 8, 9, 10 retired; Entries 2, 3, 6 kept. GDoc portion (B1g–B5g + GDoc Module 10 retirements) remains Jesse's manual task. Two open flags: chloride ppm (DRAFTED-NOT-CANONICAL) and B2 control-action sequences (operator-unconfirmed). See [[B5-Module10_Integration_Complete]].

**[2026-06-06] | System — Desktop\Refineries folder migrated to USADeBusk vault tree:** 73 files cleared from Desktop\Refineries — 64 moved into structured `OneDrive\USADeBusk\Facilities\` and `Company\` tree, 9 deleted. 30 new facility folders created covering 24 client sites (CITGO, BP, Valero ×3, P66, Westlake ×2, PBF, Monroe, Ergon, Hunt, BASF, Dow, Sinclair WY, NWR, Syncrude, HF Sinclair ×2, Ecopetrol, Marathon, Flint Hills). Desktop folder is now empty. See [[2026-06-06-refineries-migration]].

**[2026-06-06] | System — USADeBusk OneDrive Company structure established (Part 1):** `USADeBusk\Company\` created with SOPs, Templates, Canada-Compliance, Equipment\H2-Convection-Box, Equipment\Spools. Historical archive staged at `_Pending-Archive\00_History\` (3,242 files, 2013–2022). jutsey\ user-profile folder (548 items) deleted permanently. Two scheduled-pricing spreadsheets routed to `Company\` root. Phase 2 (routing 00_History to Facilities by client) is a separate session. See [[onedrive-company-structure]].

**[2026-03] | Equipment — Second TriMax config:** When running 2x TriMax simultaneously, each unit has its own clean tank (3,000 gal) and dirty tank (2,000 gal). One shared 4×3 pump and one shared filter press. T-connections with valve manifolds on both sides link each dirty tank outlet to shared pump suction; clean filtrate returns to respective clean tanks. Both units pig the same direction — B→R means convection-inlet-to-radiant-outlet, the standard pig travel direction.

**[2026-03] | Process — Crossover reducer:** The reducer between convection outlet and radiant inlet sits on the cross-over piping (external). Significant obstruction point — has been encountered as a blockage location when transitioning from 5" convection pigs to 6" radiant pigs. Must be addressed explicitly in pig progression planning for mixed-ID heaters.

**[2026-03] | Process — Looped circuit transit times:** Looped passes (joined via jumper spool) have pig transit times of 15–20 minutes or more for long circuits. Extended blind period between pig launches — careful monitoring required. Final pig size may need to be larger (e.g., 6.5" vs. 6.25") to achieve full wall contact through the longer combined circuit.

**[2026-03] | System — Skills architecture deployed:** Five USADeBusk skills built and uploaded to Claude.ai: usadebusk-core, usadebusk-equipment, usadebusk-estimating, usadebusk-sop, usadebusk-ops. Core loads on all tasks; others load by task type. Skills available in all chats and projects.

**[2026-03] | System — Project instructions updated to v2:** All three Claude Projects updated — knowledge base sections removed, domain context now sourced from skills. Project instructions retain task-specific templates, section structures, and workflow rules not covered by skills.

**[2026-03] | Commercial — Third-party markup clarification:** 10% is the baseline (no contract). Some facilities have contract rates as low as 5%. Always confirm applicable rate before invoicing or finalizing a proposal.

**[2026-05-21] | System — vault-ingest skill v2 deployed:** Skill updated with collision suffix logic (DSP26058.md → DSP26058-r2.md), revised-proposal overwrite with `revision:` frontmatter field, field-report merge into existing job cards under `## Field Reports`, CND job number pattern, DSP# correction table (DSP#26012 → ExxonMobil; DSP#25012 → CITGO Corpus), and auto-creation of known-client subfolders. Client list expanded from 28 to 32 (Formosa, PBF, Suncor, Westlake). Skill committed and pushed to TheSkinz/claude-config.

**[2026-05-21] | System — sales-proposals routing pattern confirmed:** DSP# documents route to `05-projects/sales-proposals/[Client]/DSP#####.md` (no `#` in filename). Revision suffix from filename (e.g. DSP24021.2) maps to `revision:` frontmatter field — single file, no per-revision copies. Collision with existing vault file → append `-r2`, `-r3` suffix.

**[2026-03] | Equipment — Tube dimensions added:** 8" Sch 40 (ID 7.981") and 10" Sch 40 (ID 10.020") added to tube dimensions table.

**[2026-03] | SOPs — Pending master doc update:** Variant B stainless chloride limits from Technical Documentation project not yet fully integrated. Values: fresh solution ≤250 ppm chloride, spent solution ≤500 ppm, verify <0.5 ppm before fill. **Status: integrated into 04-knowledge/concepts/industry-foundation.md on 2026-04-25.**
