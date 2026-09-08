---
type: review
status: open
review_type: contradiction
source_authority: stated
confidence: high
created: 2026-09-08
review_after: 2026-11-08
related:
  - "[[vault-agent-loop-spec]]"
  - "[[vault-capture-loop-spec]]"
  - "[[vault-prestaging-loop-spec]]"
  - "[[decision-queue]]"
  - "[[2026-08-20-vault-architecture-audit-evidence]]"
tags: [review, knowledge-system, agent-loop, governance, contradiction]
---

# The Review Loop's own spec still runs on two loops that were stopped three weeks ago

## Trigger

Selected by the monthly Vault Review Loop run of 2026-09-08. Nothing on `50-dashboards/health.md` reports FAIL, lint is at 0 errors and 8 warnings with no `DEAD-LINK`, `POINTER-DEAD`, `ROLLUP-SCALE` or `REVIEW-OVERDUE` finding, and the decision queue holds zero open rows — so the run fell through to the category the spec itself reserves for a reading agent: a claim that is well-formed and wrong.

The claim is in the spec that governs this loop. `04-knowledge/vault-agent-loop-spec.md` carries `status: active` and `source_authority: primary`, and the scheduled task reads it first as the authoritative instruction for every run. It describes the Pre-Staging Loop and the Capture Loop as live infrastructure it depends on. Both were stopped on 2026-08-21. The retirement landed in the three deprecated specs and in `01-context/system-workflow-reference.md`; it never landed here.

This is not a documentation tidy. The stale passage tells the run what its job is, and it tells it wrong — measurably so on this run, which is the evidence below.

## Source Material

| Source | Authority | What it says |
|---|---|---|
| `vault-agent-loop-spec.md:40` | primary, active | Pre-Staging "runs daily", so "on most runs the analysis step is already done and waiting" |
| `vault-agent-loop-spec.md:62` | primary, active | Inbox and the `07-llms/`/`08-systems/`/`09-interests/` layers "are owned by the Vault Capture Loop" |
| `vault-agent-loop-spec.md:64` | primary, active | "the capture loop logs its scheduled run summaries" in `change-log.md` |
| `vault-agent-loop-spec.md:128` | primary, active | Blocked without approval: "Convert this loop to an automated/unattended schedule" |
| `vault-agent-loop-spec.md:136` | primary, active | Selection Rule priority 1 is an open decision-queue row prepared by something else |
| `vault-prestaging-loop-spec.md` frontmatter + banner | primary | `status: deprecated`; "STOPPED 2026-08-21 — this loop does not run" |
| `vault-capture-loop-spec.md` frontmatter + banner | primary | `status: deprecated`; "STOPPED 2026-08-21 — this loop does not run" |
| `01-context/system-workflow-reference.md:30` | primary | "What made it obsolete is that capture stopped too, so there are no deferrals to pre-stage" |
| `01-context/system-workflow-reference.md:62` | primary | Inbox routing is on-demand now; "the routing logic ... is unchanged — only its trigger is gone" |
| `CLAUDE.md` (vault entry point), Filing at close-out | primary | "Nothing routes the inbox on a schedule — the capture loop was disabled 2026-08-21 and was not replaced" |
| `50-dashboards/decision-queue.md` `## Open` | stated | Zero open rows as of 2026-09-07 |
| `50-dashboards/health.md` (2026-09-07) | generated | Inbox 82 items; review-loop heartbeat `pending` |

**Provenance.** Every line above was read from the file today, not inferred. The three loop-spec banners and the two `01-context` lines are quoted or precisely paraphrased from their own text.

---

## Evidence — three defects, one root cause

The root cause is the 2026-08-21 loop shutdown, which was recorded in the notes describing the loops that stopped and in the workflow reference, but not in the one active spec that consumes them. That is the same failure pattern the vault has already named: a retirement lands where it is decided, not where sessions read.

**Defect 1 — the spec names a dead producer as this loop's main supply, and misstates the job as a result.** Line 40 says the analysis "is already done and waiting in `decision-queue`", and concludes that "this loop's job is increasingly to apply an approved proposal rather than to go hunting for an item." Line 62 repeats it: operational items "now arrive pre-analyzed, via the Pre-Staging Loop, as a `review_type: pre-staged` note plus a `decision-queue` row." Nothing has pre-staged anything since 2026-08-21. The queue has been at zero since 2026-09-07 and has no producer, so the "apply an approved proposal" path is not merely rare — it is unreachable, and hunting is now the only thing a run can do. The spec says the opposite of that in two places.

**Defect 2 — inbox and content-layer routing is assigned to a loop that does not run.** Line 62 says those layers "are owned by the Vault Capture Loop." Ownership of a queue by a stopped process is indistinguishable, from inside a run, from ownership by nobody, and the inbox is at 82 items. The vault's own entry point already states the replacement rule — route it when you write it, three-outcome logic unchanged, trigger gone — so the correct text exists; it just is not here. Line 64's claim that the capture loop appends scheduled run summaries to `change-log.md` is the same error in miniature.

**Defect 3 — the Blocked table forbids the schedule this loop is running on.** Line 128 blocks "Convert this loop to an automated/unattended schedule" on the reasoning that the operational core "must stay manually triggered and reviewed while present." Line 36 of the same file reverses exactly that, deliberately and with its reasoning stated: the loop is propose-only, so an unattended run writes a review note and a queue row and nothing else. The file therefore answers its own prohibition ninety-two lines earlier. Nothing is actually ambiguous about which is current — `system-workflow-reference.md:16` and this very run both confirm the monthly schedule — but a session that reads the Blocked table without reading the Trigger section will conclude the scheduled task is operating in violation of its own governance, and the natural remedy it would reach for is to stop the task.

**What makes this worth a decision rather than a silent fix.** Defects 1 and 2 are statements of fact that are false, and correcting a false statement is Lane 2 housekeeping. But the correction has a behavioral tail: if the supply line is gone, the Selection Rule's priority order is describing a world that no longer exists, and re-ranking it changes what every future run does. That part is a judgment call, not a typo, which is why this is proposed rather than applied.

---

## Proposed Action

**Proposals 1 and 2 are additive and ride together — they are corrections of provably false statements. Proposal 3 is the one real choice, and it is independent of the other two.**

### 1. Reconcile the two dead-loop dependencies (lines 40, 62, 64)

| | |
|---|---|
| **What it is** | Strike the present-tense claims that Pre-Staging runs daily and that Capture owns inbox and content-layer routing. Replace with the current state: nothing pre-stages, so a run finds its own item; inbox routing is on-demand and its rule lives in the vault `CLAUDE.md`; the routing *logic* in `vault-capture-loop-spec` is still correct and still the reference, only its trigger is gone. Keep the pre-staging paragraph's history rather than deleting it, in the same "kept because it was right at the time" form `system-workflow-reference.md:30` already uses. |
| **What it costs** | One editing pass on three passages in one file. No tooling, no lint rule, no other note moves. |
| **If nothing is done** | Every scheduled run is instructed to expect prepared work that will never arrive, and to treat hunting as the exception when it is now the whole job. This run absorbed that cost and is the first measurement of it. |

### 2. Reconcile the Blocked row against the Trigger section (line 128)

| | |
|---|---|
| **What it is** | Rewrite the row so it blocks what is actually still blocked — converting this loop to unattended operation **without** the propose-only boundary — rather than blocking the schedule itself. The row keeps its purpose; it stops contradicting line 36. |
| **What it costs** | One table row. |
| **If nothing is done** | A future session reading the Blocked table in isolation has documented grounds to disable the scheduled task. The reasoning that reversed the rule is real and stated, but it is not where that session will be looking. |

### 3. Re-rank the Selection Rule (lines 136–141)

| | |
|---|---|
| **What it is** | Priority 1 is currently "an open decision-queue row Jesse is ready to decide." With no producer and an empty queue, that rung is dead on arrival every month, and the live top rung is priority 2, the high-risk contradiction. Options: **(a)** re-rank so contradiction leads and the queue row becomes a conditional first check; **(b)** leave the order alone and add one sentence saying the queue is now filled only by this loop and by attended sessions, so priority 1 fires only when Jesse left something there; **(c)** no change — the list already degrades gracefully by falling through. |
| **What it costs** | (a) changes run behavior and should be a deliberate call. (b) is a sentence and preserves the order for whenever a producer returns. (c) is free and relies on future runs falling through correctly, which this run did. |
| **If nothing is done** | Low. This is the least urgent of the three; the fall-through works. It is raised because leaving a permanently-unreachable rung at the top of a priority list is how the next reader concludes the queue is broken rather than empty. |

**Recommendation: 1 and 2 approved as stated, and 3(b).** Proposals 1 and 2 correct statements that are false today with no judgment involved. On 3, re-ranking (a) bakes the current outage into the loop's permanent instruction, and the outage is reversible — `system-workflow-reference.md:5` records that re-enabling a stopped loop is one `enabled: true` plus a row back in `LOOP_HEARTBEATS`. A sentence costs nothing and survives that reversal intact.

## Approval Boundary

Propose only. Nothing in `04-knowledge/vault-agent-loop-spec.md` was edited by this run, and no canonical content anywhere was touched.

This item is **Lane 2** — vault structure and convention. It carries no pricing, SOP, safety, field-execution or customer-facing value, and no heater-card fact. Lane 2 questions of this shape take the recommendation above unless Jesse says otherwise; the queue row exists so the decision is visible rather than assumed.

What would make this Lane 4 and is **not** proposed here: changing what the loop is permitted to write, relaxing propose-only, or altering the approval boundaries in the Blocked table beyond the one self-contradicting row in Proposal 2.

## Risks / Open Questions

The correction is a snapshot of a reversible state. If Capture or Pre-Staging is ever re-enabled, the reconciled text becomes wrong in the other direction — which is the argument for writing Proposal 1 as history-plus-current-state rather than as a deletion, and for preferring 3(b) over 3(a).

One thing this note does not settle: whether the review loop should be doing anything about 82 inbox items. The spec says inbox content routing is not this loop's scope, and that boundary is untouched by the correction — Proposal 1 only fixes *who* owns it, not *whether this loop does*. If the answer is that nobody owns it on a schedule and that is intended, the correction should say so plainly rather than leave the reader to infer it.

Not verified: whether the `vault-capture-loop` and `vault-prestaging-loop` scheduled tasks are in fact disabled in the desktop app. The three loop specs, the workflow reference and the vault `CLAUDE.md` all state it, and the run ledger shows no firing for either since 2026-08-21, which is consistent — but that is agreement among vault notes plus an absence, not an independent read of the scheduler. The artifact that would settle it is the task list in the app.

## Decision

- [ ] **Proposal 1** — reconcile lines 40, 62, 64 (dead-loop dependencies) — approve
- [ ] **Proposal 2** — reconcile line 128 (Blocked row vs. Trigger section) — approve
- [ ] **Proposal 3** — Selection Rule: (a) re-rank / (b) add clarifying sentence *(recommended)* / (c) no change
- [ ] Reject — the spec is close enough as written
- [ ] Needs more source material

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-09-08 | Review note created. No canonical content edited. | Vault Review Loop |
