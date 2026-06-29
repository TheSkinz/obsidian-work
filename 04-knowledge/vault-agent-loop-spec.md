---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-06-27
review_after: 2026-07-26
related:
  - [[knowledge-system-governance]]
  - [[vault-source-of-truth]]
  - [[knowledge-review-dashboard]]
tags: [knowledge-system, agent-loop, vault-review, governance]
---

# Vault Agent Loop Spec

This note defines the scheduled command loop for maintaining the USADeBusk Obsidian vault. It turns the proven CND25004 pilot workflow into a repeatable agent loop with strict approval boundaries.

## Loop Name

Vault Review Loop

## Trigger

Recurring schedule:

```text
Monday and Friday mornings at 8:00 AM America/Chicago.
```

Manual on-demand command:

```text
Run the Vault Review Loop on obsidian-work. Pick one safest item and create a review note only.
```

## Scope

Canonical vault only:

```text
C:\Users\Jwuts\obsidian-work
```

Before any write, verify the target path starts with the canonical vault path in [[vault-source-of-truth]].

## Goal

Improve vault trust, retrieval, and maintenance by finding one small reviewable item per run. The loop should create evidence-backed review artifacts, not silently reorganize the vault.

## Loop Steps

1. Observe current state.
2. Retrieve only the minimum relevant notes.
3. Identify candidate issues.
4. Pick one safest useful item.
5. Create a review, contradiction, or question note.
6. Stop before mutating source/canonical notes unless Jesse has explicitly approved the specific change.
7. Log approved changes after they are applied.

## Observation Targets

Check these areas in order:

| Order | Area | Purpose |
|---:|---|---|
| 1 | `00-inbox/` | Unprocessed source notes and routing candidates. |
| 2 | `06-insights/` | Open reviews, contradictions, and prior loop notes. |
| 3 | `04-knowledge/` | Governance, canonical rules, evaluation questions, stale/due notes. |
| 4 | `02-facilities/` | Only when a specific facility/heater is needed for the selected item. |
| 5 | `change-log.md` | Confirm history before writing or closing a loop. |

Never scan the whole vault deeply unless the selected item requires it.

## Candidate Issue Types

| Type | Create |
|---|---|
| Unprocessed source | Review note. |
| Conflicting claims | Contradiction note. |
| Poor retrieval or missing source | Question note. |
| Stale note or due review | Review note. |
| Candidate facility/heater/job update | Review note first; draft scaffold only after approval or when explicitly low-risk and marked draft/source-derived. |
| Duplicate vault/source-of-truth concern | Review note; no file moves or deletion. |

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read vault notes | Stay within canonical vault unless source evidence requires a referenced local source path. |
| Create review notes in `06-insights/` | Must include trigger, evidence, proposed change, risks, decision checklist, and apply log. |
| Create contradiction notes in `06-insights/` | Must quote or precisely paraphrase the conflicting claims and link sources. |
| Create question notes in `06-insights/` or `04-knowledge/` | Must include expected sources and retrieval failure type. |
| Create draft/source-derived scaffolds | Only when explicitly approved or clearly requested; must be marked `status: draft`, `source_authority: secondary`, and `confidence: medium` or lower. |
| Append to `change-log.md` | Only after a real approved change is applied. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Delete files or folders | Data loss risk. |
| Archive or move source notes | Routing/source-of-truth impact. |
| Mark draft heater cards as reviewed | Canonical fact promotion. |
| Edit pricing, SOP, safety, field execution, customer-facing, or heater-card facts | Operational risk. |
| Merge conflicting claims | Must preserve contradiction trail. |
| Bulk edit metadata across many notes | Sync and regression risk. |
| Change recurring schedule | Requires explicit approval. |

## Selection Rule

Pick one item per run. Prefer the smallest item that improves trust or retrieval. Do not batch unrelated cleanup.

Recommended priority:

1. High-risk contradiction with clear source trail.
2. Inbox item with obvious routing but no canonical edits needed.
3. Open review waiting for evidence gathering.
4. Stale/due governance or canonical note.
5. Retrieval evaluation failure.

## Output Artifact Requirements

Every loop-created review artifact must include:

| Section | Required Content |
|---|---|
| Trigger | Why the item was selected. |
| Evidence | Source notes, paths, dates, and authority. |
| Proposed Action | What should happen next. |
| Approval Boundary | What cannot happen without Jesse approval. |
| Risks / Open Questions | Uncertainty and operational impact. |
| Decision | Checkboxes for approve/reject/needs more source material. |
| Apply Log | Date/action/by after any approved change. |

## Stop Conditions

Stop and report instead of continuing when:

- The selected item touches safety, pricing, SOP execution, customer-facing content, or heater-card facts and approval has not been given.
- Source authority is unclear.
- The path is outside the canonical vault.
- The same class of failure happens twice.
- OneDrive sync or file existence state is ambiguous.

## Success Criteria

A successful loop run leaves the vault better by one small increment:

- one review note created,
- one contradiction documented,
- one question/evaluation item captured,
- one approved source routed,
- or one approved draft scaffold created.

The loop is successful even if it stops with a well-documented blocker. It is not successful if it makes broad silent changes.
