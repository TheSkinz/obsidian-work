---
type: review
status: resolved
review_type: canonical-update
source_authority: secondary
confidence: medium
created: 2026-06-26
review_after: 2026-07-03
related:
  - CND25004
  - [[7-2-F-1]]
  - [[_facility]]
tags: [review, knowledge-system, Syncrude, heater-card, CND25004]
---

# Candidate Canonical Updates From CND25004

## Trigger

Post-routing extraction pass for CND25004. The report is now routed under `03-jobs/Syncrude/` and can feed candidate facility/heater knowledge through the approval workflow.

## Proposed Changes Made As Draft

Created draft source-derived heater scaffold:

- `02-facilities/Syncrude/Fort-McMurray-AB/7-2-F-1.md`

This is not fully canonical yet. It is marked `status: draft`, `source_authority: secondary`, and `confidence: medium` because the source is a job report with an already documented body-field defect.

## Candidate Facility Facts

| Fact | Source | Proposed Destination | Approval Need |
|---|---|---|---|
| Facility is Syncrude Refinery - Mildred Lake / Wood Buffalo, AB. | CND25004 customer details. | [[_facility]] identity/notes. | Review naming preference: Fort McMurray vs Wood Buffalo vs Mildred Lake. |
| Site training listed as CSO / Syncrude Site Specific. | CND25004 project details. | [[_facility]] site access/safety. | Low; still source-derived. |
| Hydrant / soda ash solution / chemical mixed in tank used on job. | CND25004 project details. | Facility constraints and heater card water source. | Medium; distinguish site standard from job-specific condition. |

## Candidate Heater Facts

| Fact | Source | Proposed Destination | Approval Need |
|---|---|---|---|
| Heater tag/name is 7-2 F-1 Bitumen Column Feed Heater. | CND25004 pigging details and coil data. | `7-2-F-1.md` identity. | Low. |
| 8 coils reported. | CND25004 configuration and coil data. | `7-2-F-1.md` identity/config rollup. | Medium; verify physical arrangement. |
| Convection: OD 6.625, schedule 40, wall 0.280, ID 6.065, 16 tubes, length 1040, U-bends. | CND25004 coil data. | `7-2-F-1.md` tube geometry. | Medium; verify length semantics before estimating. |
| Radiant: OD 6.625, schedule 40, wall 0.280, ID 6.065, 31 tubes, length 1271, U-bends. | CND25004 coil data. | `7-2-F-1.md` tube geometry. | Medium; verify length semantics before estimating. |
| Launcher location: 16 launchers, inlet control valve station / outlet radiant outlet flanges. | CND25004 pigging details. | `7-2-F-1.md` connection info / field notes. | Medium; flange sizes not recorded. |

## Candidate Job Facts To Keep In CND25004

| Fact | Why It Stays Job-Specific |
|---|---|
| Quest Smart Pig all 8 coils. | Customer/job election, not a permanent heater fact. |
| TriMax 5 and TriMax 6 deployment. | Dispatch/resource decision, not a heater-card field. |
| Kicksolve added during pigging. | Job condition/response; may inform lessons learned but not fixed heater geometry. |
| Standby and duration tables. | Job execution history; useful for estimating precedent, not core heater identity. |
| Crew names and receipt numbers. | Field/job report evidence, not canonical facility/heater knowledge. |

## Issues Found

| Issue | Impact | Proposed Handling |
|---|---|---|
| Report body contains `JOB #: CND25002`. | Source-body defect can poison routing/search if copied blindly. | Already preserved warning in CND25004; CND25004 confirmed by Jesse. |
| Dewater detail says 10 in swab; pig table says 10.5 in swab. | Possible equipment-size mismatch. | Leave both in notes; create contradiction only if sizing is used operationally. |
| Length fields may be total or per-circuit. | Estimating error risk. | Mark ambiguous until drawing/heater card source confirms. |

## Decision

- [x] Approve draft heater scaffold as source-derived record
- [x] Promote selected facts to reviewed heater-card status (identity facts only; geometry stays medium confidence)
- [x] Revise facility naming/key — resolved as Mildred Lake
- [x] Create contradiction for 10 in vs 10.5 in swab detail — resolved as 10 in
- [ ] Need more source material — deferred

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-06-26 | Created draft heater scaffold and candidate canonical update review. | Codex |
| 2026-06-29 | Approved scaffold to source-derived; promoted identity facts; facility named Mildred Lake; swab resolved to 10 in; more source deferred. Applied to 7-2-F-1.md, _facility.md, and equipment-library.md. | Jesse |
