---
type: review
status: open
review_type: proposal
source_authority: inferred
confidence: medium
created: 2026-07-28
review_after: 2026-08-28
related:
  - vault-capture-loop-spec
  - vault-agent-loop-spec
  - knowledge-system-governance
tags: [review, knowledge-system, agent-loop, capture, governance]
---

# Review — The deferred-operational pile has no unattended path forward

## Trigger

Session 2026-07-28, from Jesse's question about safely speeding up the ingestion pipeline without requiring his immediate interaction. Recon on the live system showed the bottleneck is not loop cadence — it is that the dominant capture-loop outcome is *defer*, and the only consumer of deferred items fires manually.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/.capture-state.json` | Observed | Transcript dispositions run 41 `defer` to 9 `harvested` to 61 `skip`. Deferral is the dominant non-skip outcome by better than 4:1. |
| `00-inbox/` file scan | Observed | 16 notes carry the `<!-- vault-loop: -->` no-home/defer marker. Inbox stood at 43 items before this session's terminal-seed sweep took it to 36. |
| `50-dashboards/health.md` (2026-07-27) | Observed | Open decision rows: 0 of a cap of 10. Review notes awaiting decision: 1. All heartbeats ok. The analysis machinery is idle while the input pile grows. |
| `04-knowledge/vault-capture-loop-spec.md` | Primary | Scope section: an operational inbox item is left in place with a routing note, and the loop stops. By design it never writes the operational core. |
| `04-knowledge/vault-agent-loop-spec.md` | Primary | The only consumer of deferred operational items. Trigger is on-demand only — Jesse says "run the Vault Review Loop." |
| `04-knowledge/knowledge-system-governance.md`, Lane 4 | Primary | "In unattended runs, do not apply — instead **add a row to the decision queue** … or an **Open Flag** on the affected card." The unattended propose-only behavior is *already specified policy*; nothing currently exercises it on a schedule. |

## The Problem, Stated Plainly

Capture is fast and getting faster (now daily). It reliably identifies operational content and correctly refuses to touch it. But the handoff target is a manual trigger, so every operational finding waits on Jesse not just to *decide* — which is correct and non-delegable — but to *initiate the analysis*, which is not. He arrives to a pile of raw notes and must fund the reading himself, which is exactly the friction that makes the trigger get skipped, which grows the pile.

The distinction this proposal turns on: **deciding is Lane 4 and stays with Jesse; preparing the decision is not.**

## Proposed Change

### A. A scheduled, propose-only pre-staging pass over deferred inbox items

A new bounded loop (or an added phase on the capture loop) that reads inbox items carrying the defer marker and, for each, writes a review note in `06-insights/` with populated Source Material and a Decision checklist, plus a `50-dashboards/decision-queue.md` row. It writes **no** operational content — not `02-facilities/`, not `04-knowledge/`, not pricing, SOP, safety, or heater-card facts. Its entire output is proposals.

Jesse then arrives to approve or reject rather than to read and analyze.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### B. The existing decision-queue cap is the bound

Governance already pauses proposal-generating loops at 10 open decision rows. That cap becomes this loop's natural throttle: it pre-stages until the queue is full, then stops and waits for Jesse to drain it. No new bounding mechanism is needed, and the failure mode is self-limiting — a runaway pass fills 10 slots and halts.

This is the specific reason the proposal is bounded-propose-only rather than the unbounded policing pattern Jesse has previously rejected.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### C. One item per run, oldest first

Matching the Idea Research Loop's proven shape rather than batch-processing the backlog. Keeps each run cheap, keeps output reviewable, and means a bad pass damages one note instead of sixteen. At the current pile of 16 and a daily cadence, the backlog clears in about two weeks without Jesse touching it.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

The honest risk is proposal spam: sixteen mediocre review notes are worse than sixteen raw inbox notes, because they carry an implied claim of analysis. The one-item-per-run bound in (C) is the mitigation, and the first three runs should be read critically before the loop is trusted to keep going.

A pre-staged review note is an *unreviewed inference*. It must be visibly marked as such, or a future session may read a machine-drafted Source Material table as settled vault truth. Every note this loop produces should carry `source_authority: inferred` and `status: open`.

This adds a fifth-and-a-half scheduled loop to a system that already has five, against Jesse's standing preference for drop-and-forget over machinery. The counter is that it adds no new *trigger* for him to remember — it feeds the dashboard he already reads at session start.

Some deferred items are genuinely not worth a review note (the DSP26085 wrong-quote-number item is an execution correction, not a knowledge question). The loop needs a skip disposition, or it will manufacture ceremony for items that need a two-minute fix.

Pre-staging does not speed up Lane 4 *decisions*, which remain synchronous and Jesse-gated by design. This proposal is explicitly not an attempt to erode that gate — it only removes the analysis wait in front of it.

## Decision

Per-proposal checkboxes above. This note is open until A–C are dispositioned. Nothing is built until then.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-28 | Note filed from session; no loop built, no operational content modified | Claude (Opus 5) |
