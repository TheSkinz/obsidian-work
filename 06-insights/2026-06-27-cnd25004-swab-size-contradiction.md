---
type: contradiction
status: resolved
source_authority: secondary
confidence: high
created: 2026-06-27
review_after: 2026-07-04
related:
  - CND25004
  - [[7-2-F-1]]
  - [[2026-06-26-cnd25004-candidate-canonical-updates]]
tags: [contradiction, knowledge-system, Syncrude, CND25004, pigging]
---

# Contradiction - CND25004 Swab Size

## Trigger

The open review [[2026-06-26-cnd25004-candidate-canonical-updates]] flagged a possible swab-size mismatch in CND25004. This is a small, evidence-backed contradiction that affects whether swab size should be copied into heater-card or estimating references.

## Evidence

| Claim | Source | Authority | Notes |
|---|---|---|---|
| Dewater setup used `1600 cfm compressor / 10" Swab`. | `03-jobs/Syncrude/CND25004.md`, project details / pigging details. | Secondary source job report. | This appears in the high-level dewater field. |
| Trimax 5 receipt detail says the job was dewatered with `10.5” swabs`. | `03-jobs/Syncrude/CND25004.md`, receipt 10153, dated 2025-09-13. | Secondary source job report. | This is a field execution detail. |
| Pig utilization table lists `10.5”` with total `3`, foam `0`, TC `0`, swab `3`. | `03-jobs/Syncrude/CND25004.md`, PIGS UTILIZED table. | Secondary source job report. | This is the structured consumption summary. |
| Draft heater scaffold preserves both values and asks whether the wording should be normalized. | `02-facilities/Syncrude/Fort-McMurray-AB/7-2-F-1.md`, Field Notes / Open Questions. | Draft source-derived scaffold. | Not reviewed canonical heater-card evidence. |

## Proposed Action

Do not normalize this to either `10 in` or `10.5 in` yet. Treat the correct swab size as unresolved until a stronger source is available, such as original service receipts, tool inventory/loadout records, the source DOCX table before conversion, or Jesse confirmation.

## Approval Boundary

No source note, draft heater card, canonical heater-card fact, estimating reference, SOP, or customer-facing material should be edited from this contradiction without Jesse approving the exact change. Both source claims should remain preserved as raw evidence.

## Risks / Open Questions

- The difference may be a shorthand/rounding issue, but it may also indicate a tool-size mismatch.
- If copied into an estimating or equipment reference, the wrong value could affect future pig/swab planning.
- The report is already known to contain a separate body-field defect (`JOB #: CND25002`), so source-table details should be verified before promotion.

## Decision

- [x] Confirm `10.5 in` swabs as correct

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-06-27 | Created contradiction note; no source or canonical notes modified. | Codex | Daily Vault Review Loop. |
| 2026-07-05 | Jesse confirmed 10.5 in swabs (receipt 10153 + pig-utilization table outweigh the summary field). Corrected `02-facilities/Syncrude/Fort-McMurray-AB/7-2-F-1.md`, which had self-asserted the opposite (10 in) resolution without going through this review. | Claude |
