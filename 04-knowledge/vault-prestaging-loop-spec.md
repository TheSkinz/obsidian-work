---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-07-28
last_reviewed: 2026-07-28
review_after: 2026-10-28
related:
  - [[vault-capture-loop-spec]]
  - [[vault-agent-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[knowledge-system-governance]]
  - [[2026-07-28-deferred-operational-prestaging-review]]
tags: [knowledge-system, agent-loop, pre-staging, governance]
---

# Vault Pre-Staging Loop Spec

The sixth loop, and the one that closes the system's throughput gap. [[vault-capture-loop-spec]] files and harvests but **defers** anything operational; [[vault-agent-loop-spec]] is the only consumer of those deferrals and fires **only when Jesse says so**. The result measured on 2026-07-28: transcript dispositions running 41 `defer` to 9 `harvested`, 16 inbox notes carrying the defer marker, and a decision queue sitting at 0 of its cap of 10. The analysis machinery was idle while the input pile grew.

This loop does not close that gap by deciding anything. It closes it by **preparing** decisions so Jesse arrives to approve or reject rather than to read and analyze.

The distinction the whole design turns on: **deciding is Lane 4 and stays with Jesse; preparing the decision is not.**

Approved 2026-07-28 via [[2026-07-28-deferred-operational-prestaging-review]], proposals A, B and C, all approved without edits.

## Loop Name

Vault Pre-Staging Loop

## Trigger

Scheduled daily at ~06:00 local (`0 6 * * *`) via `mcp__scheduled-tasks`, task id `vault-prestaging-loop`.

**The 06:00 slot is deliberate and ordered.** The Capture Loop fires at ~05:00 and is what *applies* the defer markers this loop reads. Running an hour behind it means each pre-staging run sees the current day's deferrals rather than yesterday's. Both sit before working hours, which is itself a lesson paid for on 2026-07-28: the capture loop's first daily run at 08:00 collided with a live session holding staged renames in one of its own commit paths.

## Scope

Reads:

- `00-inbox/*.md` carrying the `<!-- vault-loop: -->` defer/no-home marker — the only input queue this loop watches.
- Whatever vault context an item needs to be understood (`02-facilities/`, `04-knowledge/`, quote notes, prior review notes) — **read-only, always**.

Writes:

- One review note per run in `06-insights/`, `review_type: pre-staged`.
- One row in `50-dashboards/decision-queue.md`.
- A `<!-- vault-prestaged: <review-note-filename> -->` marker on the processed inbox item, so it is never reprocessed.

**Explicitly not in scope:** files with `type: idea-seed` belong to [[vault-idea-loop-spec]] and are skipped here even if they carry a defer marker. Two loops must never process the same item.

Never writes `02-facilities/`, `04-knowledge/` canonical content, pricing, SOPs, safety, field-execution, customer-facing content, or heater-card facts. Its entire output is proposals. If it finds itself wanting to *fix* something, that is the signal it has exceeded scope — it writes the proposal and stops.

## Ceremony Level

Low to run, high in what it refuses to do. Every run either produces exactly one proposal artifact or cleanly no-ops. Nothing it writes is a decision.

## The Two Hard Bounds

**Bound 1 — the decision-queue cap.** Governance already pauses proposal-generating loops at 10 open rows. That cap is this loop's throttle and no new mechanism is added: count `status: open` rows in `50-dashboards/decision-queue.md` before doing anything, and if the count is **10 or more, no-op immediately** and record why. The failure mode is self-limiting — a runaway loop fills ten slots and halts. This is the specific reason the design is bounded-propose-only rather than the unbounded policing pattern Jesse rejected on 2026-07-03.

**Bound 2 — one item per run, oldest first.** Matching the Idea Research Loop's proven shape rather than batch-processing a backlog. Keeps each run cheap, keeps output reviewable, and means a bad pass damages one note instead of sixteen. At the 2026-07-28 pile of 16 and a daily cadence, the backlog clears in roughly two weeks unattended.

## Loop Steps

**Run ledger (every run, first and last action):** Before anything else, update `50-dashboards/.loop-runs.json` (local, gitignored — create if missing): set `vault-prestaging-loop` to `{"fired": "<now, UTC ISO-8601>", "completed": null, "result": "running"}`, merging without touching other loops' entries. As the run's very last action — after the final push, or immediately on deciding the run is a no-op or hitting a fatal problem — set `completed` to now and `result` to `committed`, `no-op`, or `error: <one line>`. Use Write/Edit tools, never shell editors. This loop no-ops often (full queue, empty pile), so the ledger is the only signal separating "nothing to do" from "scheduler died."

1. **Queue check first.** Count `status: open` rows in `50-dashboards/decision-queue.md`. At 10 or more, record a no-op with reason `queue-full` and stop. Do not read the inbox, do not pick an item.
2. Scan `00-inbox/*.md` for items carrying `<!-- vault-loop: -->` and **not** carrying `<!-- vault-prestaged: -->`. Skip anything with `type: idea-seed`. If none remain, record a clean no-op and stop — do not manufacture work.
3. Pick the **oldest** candidate by filename date prefix, falling back to `created` frontmatter, falling back to git first-commit date.
4. **Triage before drafting — the skip disposition.** Read the item and classify it:
   - **Execution correction** — a concrete fix with an obvious right answer and no open question (the worked example: `2026-07-24-dsp26085-submitted-wrong-quote-number.md` is a correction to make, not a decision to weigh). Mark it `<!-- vault-prestaged: skipped — execution correction, needs doing not deciding -->`, add **no** queue row and **no** review note, and report it in the run summary so it surfaces as a to-do rather than a decision. Then return to step 3 for the next-oldest candidate; skips do not count against the one-item budget.
   - **Already covered** — the answer already exists. Same treatment, marker reason `already covered by [[note]]`.

     **Search implementation, not just prose — this is the failure the first run hit (2026-07-28).** That run searched `knowledge-system-governance.md`, found nothing, and proposed building a content-vs-formatting diff gate that had shipped the day before as lint rule `WORD-DELTA` plus a PreToolUse hook. A governance document is where a policy would be recorded, not where a tool lives. Before writing "genuinely unaddressed," check all four: `04-knowledge/` and `06-insights/` prose, **`tools/`** (grep the lint rules and scripts), **`~/.claude/hooks/`**, and **recent `git log`** — a thing built in the last week is exactly what a knowledge doc will not mention yet.

     When a partial match turns up, do **not** silently drop the item. Write the note with the existing mechanism cited and the proposal narrowed to the genuine remaining gap — a partially-solved problem usually has a sharper question in it than an unexamined one.
   - **Genuine open question** — proceed to step 5.

   This step exists because the alternative is manufacturing ceremony: sixteen review notes for items where several need a two-minute fix is worse than sixteen raw inbox notes, because each one carries an implied claim of analysis.
5. Gather context read-only and draft the review note in `06-insights/`, filename `YYYY-MM-DD-prestaged-<slug>.md`, using the standard review-note template: Trigger, Source Material (a real table with real citations — every row must point at a file actually read), The Question, Proposed Change (each option carrying its own `Approved / Approved with edits / Rejected / Needs more research` checkboxes), Risks and Counter-Arguments, Decision, Apply Log.

   **Frontmatter is mandatory and load-bearing:** `review_type: pre-staged`, `source_authority: inferred`, `status: open`. A pre-staged note is an *unreviewed inference*, and without these a future session may read a machine-drafted Source Material table as settled vault truth.
6. Append one row to `50-dashboards/decision-queue.md`: `id` = next monotonic `DQ-NNN` (scan the whole file, including closed and expired rows, for the highest existing number; never reuse), `opened` = today, `source` = link to the new review note, `ask` = the one-line question, `risk` = tier per the queue's own rule (`high` for pricing, SOP, safety, field-execution, customer-facing or heater-card facts; `med` for structure, schema or convention; `low` for reversible content), `status` = `open`. Update the "N open rows" line beneath the table.
7. Mark the source inbox item with `<!-- vault-prestaged: <review-note-filename> -->`. Do not otherwise edit its content, and do not move or delete it — routing it remains the Capture Loop's or Jesse's call.
8. Run `python tools/vault_lint.py` (use `py -3` if `python` is not on PATH); it must report **0 errors** before committing. Warnings are acceptable.
9. Commit and push only this run's touched paths (the review note, `decision-queue.md`, the marked inbox item). Commit message `vault-prestage: <YYYY-MM-DD> — pre-staged <slug>` (or `— skipped N, no candidates` when a run only skipped). **The `vault-prestage:` prefix is this loop's heartbeat**, read by `tools/vault_health.py`. Because the loop is silent whenever the queue is full or the pile is empty, health tracks it at a monitoring cadence of 30 days, not its daily run cadence — a FAIL means the scheduler died, not that one day was quiet. Keep the prefix exact. No `change-log.md` entry: that file is decisions-only, and the run record lives in the commit message.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read any vault note | Read-only, always. |
| Create one review note per run in `06-insights/` | Standard template; `review_type: pre-staged`, `source_authority: inferred`, `status: open` mandatory; every Source Material row must cite a file actually read. |
| Append one row to `50-dashboards/decision-queue.md` | One per run; monotonic id; never edit or close an existing row. |
| Add a `<!-- vault-prestaged: -->` marker to an inbox item | Comment only; no content change. |
| Run `tools/vault_lint.py` before committing | Pre-commit gate; must be 0 errors. |
| Commit and push this run's touched paths | Per step 9. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Writing `02-facilities/`, `04-knowledge/` canonical content, pricing, SOP, safety, field-execution, customer-facing content, or heater-card facts | This loop proposes; it never applies. Owned by [[vault-agent-loop-spec]]. |
| Checking, closing, or editing any decision-queue row | Closing a row is human-gated. The loop only ever appends. |
| Processing more than one item per run | Bound 2. Skips and no-ops do not count. |
| Adding a queue row when the queue is at or over cap | Bound 1. The cap is the throttle. |
| Deleting, moving, or rewriting an inbox item | Routing belongs to the Capture Loop; disposal belongs to Jesse. |
| Processing a `type: idea-seed` file | Owned by [[vault-idea-loop-spec]]. Two loops must never touch one item. |
| Editing any skill file under `~/.claude/skills/` | Out of scope entirely. |

## Stop Conditions

Stop and report when: the decision queue is at or over cap (no-op, this is success); no unprocessed candidates remain (no-op, also success); an item cannot be understood without information the vault does not contain (mark it `<!-- vault-prestaged: skipped — insufficient context -->` and report, do not guess); the same failure class occurs twice; or git working-tree state is ambiguous (conflicts, detached state, **or a concurrent session mid-edit** — the 2026-07-28 collision is why this is listed).

## Success Criteria

A successful run either produces one well-evidenced proposal that lets Jesse decide without re-deriving the analysis himself, or cleanly reports there was nothing to do. Both are success.

Failures: a review note whose Source Material cites files it did not read; a recommendation phrased as a decision; more than one item processed; a queue row added past cap; any write to operational content; or ceremony manufactured for an item that needed a two-minute fix.

## What This Loop Deliberately Does Not Do

It does not speed up Lane 4 **decisions**, which remain synchronous and Jesse-gated by design. It removes the analysis wait *in front of* the gate; it does not touch the gate. Any future change that lets this loop apply its own proposals is a different proposal requiring its own approval, and should be read with suspicion.
