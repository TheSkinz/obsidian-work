---
type: review
status: complete
review_type: contradiction
source_authority: mixed
confidence: medium
created: 2026-06-26
review_after: 2026-07-03
related:
  - CAD25004
  - [[2026-06-26-cad25004-job-number-contradiction]]
  - [[knowledge-system-governance]]
tags: [review, knowledge-system, job-number, Syncrude, routing]
---

# CAD25004 Routing Review - Syncrude

## Trigger

Follow-up investigation for the Syncrude job-number contradiction. The inbox note is named `CAD25004.md` and frontmatter identifies `job_number: CAD25004`, but the imported report body contains `JOB #: CAD25002`.

## Evidence Found

| Evidence | Supports | Notes |
|---|---|---|
| `OneDrive/USADeBusk/Facilities/Syncrude\Syncrude Fort McMurray AB/Jobs/CAD25004 2025-09/` | CAD25004 | Dedicated Syncrude job folder uses `CAD25004 2025-09`. |
| `CAD25004 Syncrude Fort McMurray 7-2 F-1 Heater Job Report.docx` | CAD25004 | Source DOCX filename uses CAD25004. |
| DOCX internal text search | CAD25002 body defect | Bundled text extraction found `CAD25004` 0 times and `CAD25002` 1 time inside the document body. |
| `OneDrive/USADeBusk/Facilities/North West Redwater\NWR Redwater AB/CAD25002 NWR Final Tickets.pdf` and related history files | CAD25002 belongs to NWR | Separate NWR Redwater source trail uses CAD25002. |
| Vault `change-log.md` line for 2026-05-21 | CAD25004 routing | Existing ingest log says CAD25004 was held in inbox because Syncrude was not scaffolded. |

## Interpretation

The strongest current interpretation is that Syncrude should remain associated with `CAD25004`, and the `CAD25002` inside the report body is likely a copied/stale job-number field or report content defect. This is not certain enough for silent canonicalization because the body of the source report is still a primary artifact.

## Recommended Action

1. Keep `00-inbox/CAD25004.md` in place for now.
2. Do not rename it to `CAD25002`.
3. Confirm `CAD25004` against a job-control source, PO, service receipts, or Jesse confirmation.
4. If confirmed, update the inbox note routing and tag metadata through an approved edit, and preserve a note that the imported report body had an internal job-number defect.
5. If the body is confirmed correct instead, investigate why the Syncrude folder and DOCX filename use CAD25004 and why NWR Redwater also uses CAD25002.

## Proposed Approved Edit After Confirmation

If `CAD25004` is confirmed:

- Set `client: Syncrude` or approved client naming.
- Set `facility: Syncrude-Fort-McMurray-AB` or approved facility key.
- Keep `job_number: CAD25004`.
- Change `routing` from `unresolved` to the approved route.
- Add tags such as `[source, job-report, Syncrude, CAD25004]`.
- Add a warning note near the source summary that the report body contains `JOB #: CAD25002` and was treated as an unresolved content defect unless corrected by source authority.

## Decision

- [x] Confirm CAD25004 as governing job number
- [ ] Confirm CAD25002 as governing job number
- [ ] Need more source material
- [ ] Ask Jesse

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-06-26 | Located Syncrude source folder, source DOCX filename, DOCX internal job-number text, and separate NWR CAD25002 evidence. No source notes modified. | Codex |
| 2026-06-26 | Routed confirmed CAD25004 source note to `03-jobs/Syncrude/CAD25004.md` and created `02-facilities/Syncrude/Fort-McMurray-AB/_facility.md`. | Codex |



