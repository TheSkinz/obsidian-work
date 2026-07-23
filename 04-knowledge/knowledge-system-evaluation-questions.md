---
type: evaluation-set
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-07-23
review_after: 2026-09-26
tags: [knowledge-system, evaluation, retrieval]
---

# Knowledge System Evaluation Questions

Use these questions to test whether the vault is becoming easier to retrieve from and trust. A good answer should cite the specific notes it used, identify uncertainty, and avoid blending unresolved conflicts.

## Core Retrieval Tests

| ID | Question | Expected Source Area | Pass Criteria |
|---|---|---|---|
| KS-001 | What is the current source hierarchy when two notes disagree? | `04-knowledge/knowledge-system-governance.md` | Names the hierarchy and says to create a contradiction note when authority is unclear. |
| KS-002 | What is the current heater-card schema authority? | `04-knowledge/_canonical-heater-card.md`, `CLAUDE.md` | Identifies the canonical heater card and does not infer heater facts from jobs alone. |
| KS-003 | What is the standard SOP formatting authority for USADeBusk documents? | `CLAUDE.md`, `04-knowledge/sops/sop-formatting-standard.md` | Names the governing note and preserves USADeBusk formatting constraints. |
| KS-004 | Which inbox items are unprocessed or need routing? | `00-inbox`, dashboard | Lists inbox notes by status/type and flags routing gaps. |
| KS-005 | Which active or stale items need review? | dashboard, frontmatter fields | Uses status/review fields instead of guessing from note age only. |

## Domain Retrieval Tests

| ID | Question | Expected Source Area | Pass Criteria |
|---|---|---|---|
| USA-001 | What is the preferred terminology for furnace decoking and TriMax equipment? | `CLAUDE.md`, USADeBusk core references | Uses Furnace Decoking/Pigging correctly and avoids banned dual-pumper wording. |
| USA-002 | For a heater with stainless metallurgy, what special passivation issue must be considered? | heater cards, `04-knowledge/_canonical-heater-card.md`, SOP guidance | Mentions soda ash/passivation only when metallurgy supports it. |
| USA-003 | What facts belong on a heater card versus job-specific options? | `04-knowledge/_canonical-heater-card.md` | Separates heater facts from customer/job decisions like filtration or smart pigging. |
| USA-004 | What information is needed before drafting an SOP? | SOP guidance, heater card schema | Does not assume metallurgy, water source, pass count, flange details, or customer standards. |
| USA-005 | How should a completed job report feed back into facility/heater knowledge? | job notes, heater cards, review workflow | Proposes reviewable updates instead of directly rewriting canonical notes. |

## Feedback Fields

When a question fails, create a `type: question` note and capture:

| Field | Meaning |
|---|---|
| expected_sources | Notes that should have been retrieved. |
| retrieved_sources | Notes actually retrieved. |
| failure_type | missing-link, missing-property, stale-source, contradiction, poor-query, missing-canonical-note. |
| proposed_fix | Metadata, link, template, or canonical-note improvement. |
| approval_needed | Whether the proposed fix touches customer-facing, safety, pricing, SOP, field, or heater-card facts. |
