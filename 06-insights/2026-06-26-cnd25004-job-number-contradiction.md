---
type: contradiction
status: resolved
source_authority: mixed
confidence: high
created: 2026-06-26
review_after: 2026-07-03
related:
  - CND25004
  - [[2026-06-26-knowledge-system-pilot-review]]
tags: [contradiction, knowledge-system, job-number, Syncrude]
---

# Contradiction - Syncrude Job Number

## Conflicting Claims

| Claim | Source | Authority | Date |
|---|---|---|---|
| The note frontmatter identifies the job as `CND25004`. | `00-inbox/CND25004.md` frontmatter: `job_number: CND25004`; filename `CND25004.md`; source file name references `CND25004`. | Imported source metadata / file naming. | Source imported 2026-05-21. |
| The body table identifies the job as `CND25002`. | `00-inbox/CND25004.md`, Customer Details table, `JOB #: CND25002`. | Body content from imported job report. | Execution listed as September 2025. |

## Why This Matters

Job number is a routing key. It affects where the note belongs, whether a new job record should be created, how future search retrieves the report, and whether later job/facility/heater facts attach to the correct record.

## Source Hierarchy Check

The body content may reflect the original report, while the filename and frontmatter may reflect import/routing metadata. Neither should be silently treated as authoritative until the original DOCX, job folder, PO, or other job-control source confirms the correct CND number.

## Proposed Resolution

Do not rename, route, or canonicalize the Syncrude report yet. First confirm the governing job number from one of these sources:

1. Original source DOCX properties or filename lineage.
2. Customer/job control folder naming.
3. Service receipts or final job report package.
4. PO/job-control document.
5. Jesse confirmation.

After confirmation, update routing, tags, and any derived job/facility records through a review note.

## Decision

- [x] Resolved
- [ ] Resolved with exception
- [ ] Escalated to Jesse
- [ ] Needs more source material

## Resolution Log

| Date | Decision | By | Notes |
|---|---|---|---|
| 2026-06-26 | Created contradiction note; no source note modified. | Codex | Initial self-improving KB pilot loop. |
| 2026-06-26 | Resolved CND25004 as governing Syncrude job number after Jesse confirmation; routed note and preserved CND25002 body defect warning. | Codex | Source note moved to `03-jobs/Syncrude/CND25004.md`. |




