---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-15
review_after: 2026-09-14
related:
  - 50-dashboards/decision-queue.md
  - knowledge-system-governance
tags: [review, knowledge-system, dashboards, decision-queue]
---

# Review — Should `decision-queue.md` merge its two differently-shaped Closed tables?

## Trigger

Pre-staging loop run 2026-08-15, processing the oldest unprocessed inbox item carrying a `vault-loop:` marker: `00-inbox/2026-08-01-decision-queue-has-two-closed-tables.md`. Three same-date candidates were skipped first as already-decided owed work (`2026-08-01-baseline-staleness-detector-owed.md`, `2026-08-01-coil-visualization-build-owed.md`, `2026-08-01-thesis-v2-rerun-owed.md` — all approved-unexecuted, no open question). This note is the next-oldest by git first-commit and, unlike those three, raises a genuine unresolved question: `50-dashboards/decision-queue.md` has carried two structurally different "closed" sections since launch, and the source note flags the ambiguity without proposing a fix.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-01-decision-queue-has-two-closed-tables.md` | Observed | Full source note. Written 2026-08-01 while closing DQ-004 and DQ-005; documents that the author had to make an uncued judgment call about which table a newly-closed row belongs in. Explicitly "no fix proposed — flagging the choice." |
| `50-dashboards/decision-queue.md` (read this run, current state) | Observed | Confirms the split is still live, unchanged since the source note was filed two weeks ago. `## Closed` (line 35) holds DQ-003, DQ-004, DQ-005 with columns `id \| opened \| closed \| source \| ask \| outcome`. Between the two tables sits `## Why the queue is empty at launch` (line 43), a prose block describing the 2026-07-05 launch state and asserting "There are no genuinely-open decisions to seed" — stale, since DQ-003 through DQ-013 have since been filed and eight rows are open today. `## Closed / expired` (line 51) holds DQ-001, DQ-002 with columns `id \| decided \| date \| by` — no `source` column, no link to the deciding note's full context, unlike the first table. |
| `04-knowledge/knowledge-system-governance.md` (grepped this run) | Observed | One mention of the decision queue (line 108): loops add a row for cross-cutting decisions in unattended runs. No convention documented anywhere for closed-row format, table placement, or the two-table split — this is genuinely undocumented, not a policy this run missed. |
| `tools/vault_lint.py` (grepped this run) | Observed | No rule inspects `decision-queue.md` structure; nothing would catch a row landing in the wrong table or the stale prose block persisting past its accuracy window. |
| Recent `git log` (checked this run) | Observed | No commit since 2026-08-01 touches `decision-queue.md`'s table structure — only content edits appending new open/closed rows (e.g. DQ-006 through DQ-013 additions). The split has not been addressed. |

## The Question

`decision-queue.md` has carried two differently-shaped closed-row tables since its 2026-07-05 launch, separated by a prose block that is now two weeks stale on its own factual claim ("no genuinely-open decisions to seed"). Should the two tables be merged into one closed-row format (and if so, which column set — the richer `source`-carrying shape or the terser `decided/date/by` shape), left as-is with an explicit placement rule added so future closures aren't a coin-flip, or is this cosmetic enough to defer without either fix?

## Proposed Change

### A. Merge into one `## Closed` table, richer format, migrate DQ-001/DQ-002

Adopt the `id | opened | closed | source | ask | outcome` shape (matches DQ-003 onward) as the single closed-row format. Backfill `opened`/`source` for DQ-001 and DQ-002 from their linked decision notes and fold them into the one table. Delete or rewrite the stale `## Why the queue is empty at launch` section, since its central claim is no longer true. Removes the ambiguity permanently and gives every closed row the same evidentiary trail, at the cost of a one-time backfill of two historical rows.

- [ ] Approved
- [x] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### B. Leave both tables, add an explicit placement rule

Keep `## Closed` for rows closed under the current process and `## Closed / expired` reserved specifically for `status: expired` rows (60-day aging per the queue's own operating rules) rather than for DQ-001/DQ-002, which read as historical bootstrap entries, not aged-out ones. Add one line to "Operating rules" stating this split explicitly. Lowest-effort fix; resolves the coin-flip without touching historical data, but leaves two column sets permanently and doesn't address the stale prose block.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected — its placement rule kept, see Decision
- [ ] Needs more research

### C. Cosmetic, no fix — update only the stale prose claim

Treat the two-table split as harmless (DQ-001/DQ-002 are historical bootstrap rows unlikely to be looked up alongside live closures) and fix only the factually-wrong sentence in `## Why the queue is empty at launch`. Leaves the placement ambiguity for the next person closing a row, which is exactly what the source note flagged as the actual risk.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's backfill for DQ-001/DQ-002 requires reconstructing an `opened` date and a `source` link from notes that predate the queue's current template — the queue's own history section notes DQ-001 and DQ-002 were "Jesse (in-session)" decisions without a filed review note in the same shape as later rows, so `source` may not resolve to a single citable note the way DQ-003 onward does; this could produce a backfilled row that looks more authoritative than the underlying record supports. Option B leaves permanent format inconsistency, which is a small but compounding readability cost every time someone scans the full closed history rather than the current row. Option C explicitly does not solve the problem the source note raised (ambiguity about where a new closure goes) and only patches the unrelated staleness the source note also flagged in passing — it resolves the easier of the two complaints and leaves the harder one exactly where it was two weeks ago.

## Decision

**Resolved 2026-08-15 (Jesse, in session). A approved with edits. B rejected as an option but its placement rule kept. C rejected.**

**A, because B and C both leave the actual complaint standing.** The source note's complaint is not that two formats look untidy — it is that closing a row required an uncued judgment call. C explicitly does not address that and fixes only the incidental staleness. B addresses it by codifying the split, which resolves the coin-flip but preserves two column sets forever and leaves the terser one without a `source` column, so half the closed history has no evidentiary trail. Merging costs a one-time edit and removes the ambiguity permanently.

**Edit 1 — no backfill.** A proposes backfilling `opened` and `source` for DQ-001 and DQ-002. The note's own risk paragraph is right that this "could produce a backfilled row that looks more authoritative than the underlying record supports," and that risk is real: neither row has a recoverable `opened` date, and DQ-001 has no filed source note at all. Both `opened` cells and DQ-001's `source` are therefore left as `-`. A blank cell that says "not recorded" is worth more than a plausible reconstruction. DQ-002's source **was** recovered — but from its own row text, which already cited `[[2026-07-22-duration-model-capture]]` inline (verified to exist), so that is transcription, not reconstruction. Both rows' original decision text is preserved verbatim in the new `outcome` column.

**Edit 2 — B's placement rule is kept, applied to the merged table.** B's useful contribution is noticing that `## Closed / expired` conflated two unrelated things: aged-out rows and historical bootstrap rows. That distinction survives the merge as an operating rule — every closed row goes to one table whatever the reason, and an expired row records that in its `outcome` rather than getting its own section. Without this the merge would just re-open the same question the first time a row ages out.

**Edit 3 — the stale section is retitled, not deleted.** A offers "delete or rewrite." Deleting loses a real record of the 2026-07-03 → 07-05 drain and the commits behind it. It is now "Launch history (2026-07-05)", rewritten to past tense, with a one-line note saying what the claim used to assert and why it stopped being true.

**The queue was also cleared in the same pass.** All nine open rows (DQ-006 through DQ-014) are the review notes ruled in this session, so they close together and the queue goes to zero. Two things carried out of that rather than buried: DQ-009's outcome records that **F6's frozen regression baseline is now stale and still needs a replay and re-promotion**, and DQ-004's owed thesis v2 re-run remains unexecuted.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Ruled and applied. Rewrote `50-dashboards/decision-queue.md`: merged `## Closed / expired` into `## Closed` on the `id \| opened \| closed \| source \| ask \| outcome` shape, migrating DQ-001 and DQ-002 with their decision text verbatim in `outcome`, `opened` blank on both and `source` blank on DQ-001. Added the one-table operating rule. Retitled the launch section and corrected its present-tense claim. Closed DQ-006 through DQ-014 with their outcomes, taking the Open table to zero rows. No decision text was rewritten and no source link was manufactured. | Claude (review queue) |

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Note filed by pre-staging loop from `00-inbox/2026-08-01-decision-queue-has-two-closed-tables.md`, after skipping three same-date owed-work items with no open question. Confirmed the split and the stale prose claim are both still live in `decision-queue.md` today, and that no lint rule or governance doc covers closed-row placement. No vault content modified beyond the source marker. | Claude (pre-staging loop) |
