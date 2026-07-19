# Workflow Map
**Layer:** 01-context — loads every session
**Purpose:** Mobilized USADeBusk jobs and their status — nothing else. Update when a job mobilizes, changes state, or closes. Personal-tooling and side-project status lives in agent auto-memory (`~/.claude/projects/.../memory/`), which tracks it better than a manually-updated table; this file stopped claiming that role 2026-07-19 after drifting stale against it.

---

## Mobilized Jobs

| Job | Status | Next Action |
|---|---|---|
| *None currently mobilized.* | — | Add at mobilization. |

Vault structure is stable post-cleanup: `03-jobs/` and `05-projects/` decommissioned, job actuals dissolved into heater cards. Facility population continues as routine work, not a tracked project.

---

## Paused / Deferred

| Project | Status | Resume Trigger |
|---|---|---|
| LLM Knowledge Base / Wiki | Paused — architecture designed | Explicit decision to resume |
| SOP → Diagram Visualization Pipeline | Parked — separate project | Separate session |

---

## Claude Projects (Retired 2026-07-07)

Jesse no longer uses claude.ai chat Projects — Claude Code is the primary interface for all of this work, with the skills at `~/.claude/skills/` carrying the knowledge the project system prompts used to. (Gemini also retired; Copilot M365 is the company-provided tool for Microsoft-ecosystem tasks.) Rows kept for history:

| Project | Status | Where the capability lives now |
|---|---|---|
| Sales & Proposals | Retired 2026-06-15 | `usadebusk-estimating` skill |
| Technical Docs | Retired 2026-07-07 | `usadebusk-sop` skill |
| Operations & Admin | Retired 2026-07-07 | `usadebusk-ops` skill |
| Field Execution | Retired 2026-07-07 | `usadebusk-fieldpm` skill (dormant between mobilizations) |

---

## Recently Completed

| Job / Project | Completed | Notes |
|---|---|---|
| Valero Port Arthur (USA26025) | Complete | Reference only. Dual-rig, dual-shift coker job. |
| Outlook Email Security Architecture | Deployed | 5-rule corrective architecture. 48-hr audit recommended post-deploy. smtp.com in Rule 02A flagged as known gap. |
| USADeBusk Claude Architecture | Deployed | 6 skills, 3 project system prompts + Field Execution. Master Reference Document (10 modules) in GDrive. |
| Google Drive Architecture | Finalized | Two-tree structure: DeBusk/ (facility-first) + AI Workflow/ (separate). |
