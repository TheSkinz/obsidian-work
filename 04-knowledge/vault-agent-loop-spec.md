---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-07-29
review_after: 2026-10-29
related:
  - [[knowledge-system-governance]]
  - [[vault-source-of-truth]]
  - [[knowledge-review-dashboard]]
  - [[vault-idea-loop-spec]]
  - [[vault-capture-loop-spec]]
  - [[vault-prestaging-loop-spec]]
  - [[decision-queue]]
tags: [knowledge-system, agent-loop, vault-review, governance]
---

# Vault Agent Loop Spec

This note defines the scheduled command loop for maintaining the USADebusk Obsidian vault. It turns the proven CAD25004 pilot workflow into a repeatable agent loop with strict approval boundaries.

## Loop Name

Vault Review Loop

## Trigger

On-demand only. Run manually after a batch of operational work, or whenever you want the operational core reviewed:

```text
Run the Vault Review Loop on obsidian-work. Pick one safest item and create a review note only.
```

**Scheduled monthly as of 2026-08-21** — task `vault-review-loop`, 04:00 on the 8th — while remaining runnable on demand with the line above. This reverses the original "deliberately not scheduled" rule, and the reasoning for that rule is worth stating because only half of it survived. The half that holds: this loop governs high-stakes operational content that must not change without Jesse present, and it still does not — it is propose-only, so an unattended run writes a review note and a queue row and nothing else. The half that did not hold: leaving the *analysis* on-demand meant it happened rarely, while the loops that generated work for it ran nightly. The architecture audit measured this loop at 9 of 10 notes causing a real change, the highest rate in the system, and the two daily generators at ~53% — the system was running its best loop least often. Capture is stopped, so the sentence below about it handling the content layer on a schedule no longer describes anything live.

It is explicitly allowed to write nothing. A month with no item worth a decision should end in silence, not a manufactured note; this loop replaced three that spoke whether or not they had anything to say. It runs locally against the working tree — no cloud routine, no separate clone.

**What has changed underneath this loop since it was written (reconciled 2026-07-29).** Two things now do work this spec originally assigned to the loop itself. The Pre-Staging Loop ([[vault-prestaging-loop-spec]], added 2026-07-28) runs daily and *prepares* operational deferrals into evidence-backed proposals, so on most runs the analysis step is already done and waiting in [[decision-queue]] — this loop's job is increasingly to apply an approved proposal rather than to go hunting for an item. And `tools/vault_lint.py` now mechanically detects most of what the Staleness Check section below was written to catch by hand. Read both sections in that light.

## Scope

Canonical vault only:

```text
C:\Users\Jwuts\obsidian-work
```

Before any write, verify the target path starts with the canonical vault path in [[vault-source-of-truth]].

## Governance Scope

This loop governs the **operational core** of the vault:

- `04-knowledge/` (canonical rules, governance, equipment, SOPs)
- Pricing, SOP, safety, field-execution, and customer-facing content wherever it appears
- `change-log.md`

**`02-facilities/` is no longer governed here.** The 2026-07-06 facility-data ruling in [[knowledge-system-governance]] moved heater-card and facility content to **Lane 1 in full** — creating, correcting, and resolving discrepancies in that content needs no approval and no contradiction note. This loop does not gate it and should not manufacture review notes for it. The one carve-out the ruling kept: a card actively feeding a *pending bid or customer-facing document right now* is customer-facing content, and that is in scope here.

It does **not** govern `00-inbox/` content routing or the `07-llms/`, `08-systems/`, `09-interests/` content layers. Those are owned by the Vault Capture Loop ([[vault-capture-loop-spec]]). When a harvested item is operational, it routes here under this loop's approval boundaries regardless of which session produced it — in practice it now arrives pre-analyzed, via the Pre-Staging Loop, as a `review_type: pre-staged` note plus a [[decision-queue]] row. A pre-staged note is an unreviewed inference, not settled vault truth; verify its Source Material before applying anything from it.

`change-log.md` is a **shared append-only history**. Both loops append their own dated entries; neither edits or removes the other's. This loop logs approved operational changes; the capture loop logs its scheduled run summaries. Single-writer-per-entry, never a shared edit.

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
| 1 | `50-dashboards/decision-queue.md` | Open rows waiting on Jesse. Work already prepared beats work still to be found. |
| 2 | `50-dashboards/health.md` and the lint report | Mechanical signal — FAIL rows, overdue reviews, dead links. Read it instead of rescanning by hand. |
| 3 | `06-reviews/` | Open reviews (including `review_type: pre-staged`), contradictions, prior loop notes. |
| 4 | `00-inbox/` | Unprocessed source notes and routing candidates. |
| 5 | `04-knowledge/` | Governance, canonical rules, evaluation questions, stale/due notes. |
| 6 | `02-facilities/` | Read-only context when the selected item needs a specific facility or heater. Not a review target — Lane 1. |
| 7 | `change-log.md` | Confirm history before writing or closing a loop. |

Never scan the whole vault deeply unless the selected item requires it.

## Candidate Issue Types

| Type | Create |
|---|---|
| Unprocessed source | Review note. |
| Conflicting claims | Contradiction note. |
| Poor retrieval or missing source | Question note. |
| Stale note or due review | Review note. |
| Candidate facility/heater update | Not this loop's work — Lane 1, just make the change. The exception is a card feeding a pending bid or customer document right now. |
| Duplicate vault/source-of-truth concern | Review note; no file moves or deletion. |

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read vault notes | Stay within canonical vault unless source evidence requires a referenced local source path. |
| Create review notes in `06-reviews/` | Must include trigger, evidence, proposed change, risks, decision checklist, and apply log. |
| Create contradiction notes in `06-reviews/` | Must quote or precisely paraphrase the conflicting claims and link sources. |
| Create question notes in `06-reviews/` or `04-knowledge/` | Must include expected sources and retrieval failure type. |
| Create draft/source-derived scaffolds | Only when explicitly approved or clearly requested; must be marked `status: draft`, `source_authority: secondary`, and `confidence: medium` or lower. |
| Append to `change-log.md` | Only after a real approved change is applied. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Delete files or folders | Data loss risk. |
| Archive or move source notes | Routing/source-of-truth impact. |
| Edit pricing, SOP, safety, field-execution, or customer-facing content | Operational risk. Heater-card and facility facts are **excluded** — Lane 1 since 2026-07-06. |
| Close or check off a decision-queue row | Closing is human-gated by the queue's own rules; this loop applies what Jesse approved, it does not decide. |
| Merge conflicting claims | Must preserve contradiction trail. |
| Bulk edit metadata across many notes | Sync and regression risk. |
| Convert this loop to an automated/unattended schedule | Operational core must stay manually triggered and reviewed while present. |

## Selection Rule

Pick one item per run. Prefer the smallest item that improves trust or retrieval. Do not batch unrelated cleanup.

Recommended priority:

1. An open [[decision-queue]] row Jesse is ready to decide — the analysis already exists and his presence is the scarce input.
2. High-risk contradiction with clear source trail.
3. Inbox item with obvious routing but no canonical edits needed.
4. Open review waiting for evidence gathering.
5. Stale/due governance or canonical note.
6. Retrieval evaluation failure.

Applying an *approved* decision-queue row is not "one item" against this budget — it is the payoff of a prior run and can be done alongside the run's one new item. Adding to the queue is bounded; draining it is not.

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

## Staleness Check Categories

Originally mined from the claude-obsidian wiki-lint audit as a manual scan. **Four of the five categories are now mechanical** — `tools/vault_lint.py` implements them as rules, and their current state is already in `50-dashboards/lint-report.md`. Do not re-scan by hand for these; read the report.

| Category | Now covered by | Loop's remaining job |
|---|---|---|
| Dead links | `DEAD-LINK` | None — read the report. |
| Frontmatter gaps | `OP-FRONTMATTER` (operational `source`/`verified`) | None. This is the standing provenance-backfill warning list, not a per-run finding. |
| Stale reviews | `REVIEW-OVERDUE` (fires on `review_after`, skips terminal-status notes) | None for detection. **Doing** the overdue review is a legitimate item to select. |
| Orphan pages | `ORPHAN` | None. Informational; never propose deletion off an orphan warning. |
| **Stale claims** | *nothing — this is the loop's own work* | An operational claim contradicted by a newer source note. Judgment, not pattern-matching. Create a contradiction note; do not merge. |

That last row is the point of this section now. Lint finds broken *structure*; only a reading agent finds a claim that is well-formed and wrong. Spend the run there.

Dropped as non-transferable: semantic tiling (requires ollama + wiki structure), DragonScale address validity, Dataview/canvas dashboard generation.

The scan may surface several issues at once; the loop still creates one review note for the single highest-priority item per the Selection Rule. Un-actioned flags are simply re-detected on the next on-demand run — there is no backlog artifact, and that is acceptable because this loop is manual and infrequent.

## Stop Conditions

Stop and report instead of continuing when:

- The selected item touches safety, pricing, SOP execution, or customer-facing content and approval has not been given.
- Source authority is unclear.
- The path is outside the canonical vault.
- The same class of failure happens twice.
- Git working-tree or file-existence state is ambiguous (uncommitted conflicts, missing expected files).

## Success Criteria

A successful loop run leaves the vault better by one small increment:

- one review note created,
- one contradiction documented,
- one question/evaluation item captured,
- one approved source routed,
- or one approved draft scaffold created.

The loop is successful even if it stops with a well-documented blocker. It is not successful if it makes broad silent changes.
