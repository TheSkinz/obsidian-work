---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-06-26
review_after: 2026-09-26
tags: [knowledge-system, governance]
---

# Knowledge System Governance

This note governs the self-improving knowledge workflow for the USADeBusk vault. It extends the existing `CLAUDE.md` insight loop without replacing the current folder structure, heater-card schema, or job/proposal templates.

## Operating Principle

The vault improves through reviewable proposals, not silent rewrites. Agents may inspect, summarize, compare, and propose. Canonical notes change only after approval when the change affects customer-facing content, pricing, safety, field execution, SOPs, heater-card facts, or source hierarchy.

## Source Hierarchy

When sources disagree, use this default order unless Jesse explicitly overrides it.

| Rank | Source Type | Notes |
|---|---|---|
| 1 | Signed contract, customer PO, customer-issued spec, approved drawing | Highest authority for customer-specific requirements. |
| 2 | Approved SOP, final proposal, final job report, completed heater card | Operational authority after review. |
| 3 | Customer email, RFQ, meeting notes from named customer contact | Strong source, but may be superseded. |
| 4 | Service receipt, field log, PM note, job closeout observation | Strong for what happened in the field. |
| 5 | Internal template, estimating note, prior similar job | Useful precedent, not automatic authority. |
| 6 | AI summary, inferred relationship, unreviewed import | Never canonical without source review. |

If a lower-ranked source appears newer or more specific, create a contradiction note instead of blending the claims.

## Status Values

Use these values consistently where practical.

| Status | Meaning |
|---|---|
| inbox | Captured but not processed. |
| draft | Structured but not trusted as canonical. |
| active | Current working record. |
| reviewed | Checked against source material. |
| for-review | Needs Jesse or domain review. |
| stale | Likely outdated or due for review. |
| deprecated | Superseded. Keep for audit/history only. |
| unresolved | Contradiction or question still open. |
| complete | Closed job, finished item, or completed review. |

## Agent Permissions

| Action | Allowed? | Rule |
|---|---|---|
| Create review notes | Yes | Use templates and cite source notes. |
| Suggest tags, links, and properties | Yes | Put suggestions in a review note first when uncertain. |
| Update inbox/source notes | Yes, with care | Preserve raw evidence and original wording. |
| Update canonical knowledge | Approval required | Applies to SOPs, heater cards, pricing, proposals, safety, and field execution. |
| Delete notes | No | Archive or mark deprecated unless Jesse explicitly approves deletion. |
| Merge conflicting claims | No | Create a contradiction note instead. |

## Core Loops

### Inbox Processing

Process one item at a time. Identify note type, source authority, related facility/job/heater/proposal, candidate tags, and whether the item should become a source note, review note, or canonical update.

### Contradiction Handling

When two notes disagree, create a contradiction note with the exact claims and source links. Do not resolve by averaging, summarizing away the conflict, or picking the newer note unless the source hierarchy supports it.

### Retrieval Feedback

When a question is answered poorly, create a question note. Record the expected sources, what was retrieved, what was missed, and what metadata/link/template change would improve retrieval next time.

### Stale Review

Use `review_after`, `last_reviewed`, and `status: stale` to build review queues. A stale note is not wrong; it is due for verification.

## First Pilot Scope

For the first phase, apply this only to new review notes, new source notes, unresolved contradictions, and dashboard views. Do not mass-edit existing job, facility, heater, or proposal notes until the review loop is proven.
