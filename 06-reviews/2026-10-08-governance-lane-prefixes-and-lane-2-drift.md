---
type: review
status: for-review
review_type: stale-review
source_authority: stated
confidence: high
created: 2026-10-08
review_after: 2026-11-08
related:
  - "[[knowledge-system-governance]]"
  - "[[vault-agent-loop-spec]]"
  - "[[decision-queue]]"
tags: [review, knowledge-system, governance, delegated-autonomy, stale-review]
---

# The autonomy policy names commit prefixes nobody has used since 2026-08-24, and a Lane 2 procedure that has never run

## Trigger

Selected by the monthly Vault Review Loop run of 2026-10-08. `50-dashboards/health.md` shows no FAIL row, the decision queue holds zero open rows, and lint reports 0 errors and one warning: `REVIEW-OVERDUE` on `04-knowledge/knowledge-system-governance.md` (`review_after: 2026-10-05`, `last_reviewed: 2026-07-06`). Doing that overdue review is the item. The note is the vault's Source Hierarchy and the four-lane Delegated Autonomy Policy, so every lane-prefixed commit and every Lane 4 gate points back at it, and global `CLAUDE.md` defers to it ("using each lane's commit-prefix convention").

Changes to the policy itself are Lane 4 by the note's own scope line (`knowledge-system-governance.md:106`), so this run proposes and stops.

## Evidence

Everything below was read from the note or measured from `git log` in this run.

**1. The documented commit prefixes are dead.** The note says "Commit-subject prefixes make the lane visible in `git log`: `[auto]`, `[exp]`, `[default]`, `[gated]`" (line 66) and repeats them in each lane's Logging line (80, 90, 101, 110). The last commit using any of the four is `cd5eb2b` on 2026-08-24. The first `[Lane N]` commit is `fb59a6b`, the same day. Since 2026-08-25 the counts are `[Lane 1]` 135, `[Lane 2]` 182, `[Lane 3]` 1, `[Lane 4]` 33, and the four documented prefixes 0. `change-log.md` has no entry recording the switch, and I found no ruling that adopted it. The only other live surfaces still carrying the old strings are two test cases in `~/.claude/hooks/usadebusk-word-delta-guard.test.mjs` (lines 31 and 40), which only exercise message parsing.

**2. Lane 2 as written has run once.** The note defines Lane 2 as an experiment with success criteria set first, competing options, and "one note per experiment" in `08-systems/experiments/` (line 86). That folder does not exist. `[exp]` appears on exactly one commit in the repo's history (2026-08-16). Meanwhile `[Lane 2]` is the most-used prefix, on subjects like "Close out the Grok Bot build phase", "Consolidated decision pass applied: 12 rulings", "grok: README …" and "CND26001 job sheet — Syncrude 7-1 F-1". Those are systems notes, close-outs and a job sheet. The area map puts 07/08/09 knowledge and job/facility content in Lane 1 (lines 116–118), not Lane 2. So the prefix that is meant to show the lane is not showing it: Lane 2 has become the label for "vault housekeeping and systems work", and nothing in the policy says so.

**3. The prefix does not track the lane in 02-facilities either.** Commits touching `02-facilities/` since 2026-08-25 are `[Lane 1]` 100, `[Lane 4]` 20, `[Lane 2]` 10. Facility content has been Lane 1 in full since 2026-07-06 (line 72). Some of the 20 `[Lane 4]` are probably right, because the commit also changed a skill or a pending-bid card, which the carve-out allows. I did not audit them one by one. The point is narrower: nobody reading `git log` can tell from the prefix which lane a commit was really in, and that was the prefix's only purpose.

**4. Smaller stale claims in the same note**, recorded so one review clears them together:

| Line | Claim | State today |
|---|---|---|
| 66 | "the three loops" | Capture, Idea Research and Pre-Staging stopped 2026-08-21. The live ones are Review, Consolidation and Skill-Drift. |
| 76 | "the `90-sources/` provenance layer is planned — Session B" | No such folder. Nothing in `change-log.md` since says it is still planned. |
| 86 | `08-systems/experiments/`, "created on first use" | Never created (see 2). |
| 212–214 | "First Pilot Scope … until the review loop is proven" | The review loop has run monthly since 2026-08-21. The section describes a phase that ended. |

## Proposed Action

Recommendation: **option A**, because the convention people actually follow is internally consistent, it has been followed 351 times without trouble, and it maps one-to-one onto the policy's own lane names. Changing the doc costs one edit. Changing the habit costs every future session.

- **A. Ratify `[Lane N]` and record what Lane 2 is in practice.** Replace the four bracket prefixes with `[Lane 1]`–`[Lane 4]` on lines 66, 80, 90, 101 and 110. Add one line to Lane 2 saying the experiment procedure applies when a technical question has competing options, and that systems, tooling and governance housekeeping commits also carry `[Lane 2]`. Clear the four stale claims in the table. Set `last_reviewed: 2026-10-08` and a new `review_after`. Log it in `change-log.md`.
- **B. Ratify `[Lane N]` but tighten Lane 2 back to experiments only.** Same as A, except housekeeping and systems commits go back to `[Lane 1]` per the area map, and sessions are told so. This keeps the prefix meaningful but asks every future session to follow a distinction the last six weeks have not followed.
- **C. Revert to `[auto]`/`[exp]`/`[default]`/`[gated]`.** Not recommended. It reverses 351 commits of practice to match a document nobody was reading at commit time.

These are alternatives: pick one. Whichever is picked, the four stale-claim fixes in the table go with it. They are components, not a fourth option.

**If nothing is done:** nothing breaks. No hook or script reads the lane prefix (`vault_health.py` greps only loop prefixes such as `vault-review:`). The cost is that the governing document keeps stating a convention that is false. The next session that reads it literally will start committing `[gated]` again, which splits `git log` into two vocabularies. That is the "retirements don't propagate" pattern again: the change happened where work was done and never reached the document sessions are told to read.

## Approval Boundary

This run edited nothing in `knowledge-system-governance.md` and did not refresh its `last_reviewed`. It wrote no change-log line, because no change was applied. Line 106 makes "changes to … this policy itself" Lane 4, so A, B or C each need Jesse in session. The hook test file under `~/.claude/` is config-repo content and is cosmetic in any case. Leave it unless C is chosen.

## Risks / Open Questions

The switch to `[Lane N]` may have been ruled in a session that did not reach `change-log.md`. If Jesse remembers ruling it, A is just recording that ruling. The note should then cite the ruling and drop the "no ruling found" wording. I did not classify the 20 `[Lane 4]` facility commits individually, so finding 3 is about whether the prefix can be read, not a claim that any one of them was mislabelled.

## Decision

- [ ] A — ratify `[Lane N]`, describe Lane 2 as it is used, clear the four stale claims (recommended)
- [ ] B — ratify `[Lane N]`, restrict Lane 2 to experiments, clear the four stale claims
- [ ] C — revert to the four bracket prefixes, clear the four stale claims
- [ ] Reject — leave the note as is, and record why on this note
- [ ] Needs more source material — name the artifact

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-10-08 | Review note written, DQ-038 queued. No canonical edit. | vault-review-loop (scheduled) |
