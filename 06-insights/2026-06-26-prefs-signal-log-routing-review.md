---
type: review
status: resolved
review_type: inbox
source_authority: inferred
confidence: high
created: 2026-06-26
review_after: 2026-07-03
related:
  - [[prefs-signal-log]]
  - [[vault-agent-loop-spec]]
  - [[vault-source-of-truth]]
tags: [review, knowledge-system, inbox, routing, non-work]
---

# Prefs Signal Log Routing Review

## Trigger

Manual Vault Review Loop run selected `00-inbox/prefs-signal-log.md` as the safest useful item. The note appears to be personal/AI preference workflow material rather than USADeBusk operational knowledge.

## Evidence

| Evidence | Source | Authority | Notes |
|---|---|---|---|
| Session is titled `Prefs audit + redesign`. | `00-inbox/prefs-signal-log.md` | Source note body. | This is about AI/user preference design, not a customer, facility, job, proposal, SOP, or field execution item. |
| The note says the signal log target was `00-inbox`, then move to permanent vault after stabilization. | `00-inbox/prefs-signal-log.md` | Source note body. | The note itself says its current location is temporary. |
| Next actions reference user preferences, `/close`, weekly audit prompt, and a closeout skill. | `00-inbox/prefs-signal-log.md` | Source note body. | Better fit for a personal/AI tooling vault than the USADeBusk work vault. |
| Current vault source-of-truth guardrail defines this vault as USADeBusk operational knowledge. | [[vault-source-of-truth]] and [[knowledge-system-governance]] | Governance notes. | Moving across vaults requires approval; this loop should only create a review artifact. |

## Proposed Action

Do not process this as USADeBusk operational knowledge. Recommended disposition:

1. Confirm whether `prefs-signal-log.md` belongs in a personal/AI tooling vault, such as `claude-obsidian` or a future personal vault.
2. If approved, move it out of `obsidian-usadebusk` or archive it with a note explaining why it is non-work material.
3. If it stays temporarily, add frontmatter marking it as `type: personal-workflow` or `type: ai-workflow`, `status: pending-relocation`, and tags like `[non-work, ai-workflow]` so dashboard/retrieval filters can distinguish it from USADeBusk operations.

## Approval Boundary

This loop run did not move, edit, archive, or delete `00-inbox/prefs-signal-log.md`.

Specific approval is required before:

- moving the note to another vault,
- archiving it,
- editing its frontmatter,
- creating a new personal vault destination,
- or changing any cross-vault organization rule.

## Risks / Open Questions

- Mixing personal/AI preference material into the work vault can pollute retrieval for USADeBusk operational questions.
- Moving it to another vault may be the right answer, but cross-vault moves should be explicit because they affect source-of-truth and sync behavior.
- The note may still be useful as design evidence for a future personal agent loop or closeout skill.

## Decision

- [x] Move to AI/tooling vault

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-06-26 | Created routing review only; source inbox note was not modified. | Codex |
| 2026-07-05 | Jesse approved moving to AI/tooling content. Vault scope has since expanded to include an LLM-knowledge layer (`07-llms/`, per CLAUDE.md), so this stayed in-vault: moved to `07-llms/claude/prefs-signal-log.md` rather than a separate vault. | Claude |
