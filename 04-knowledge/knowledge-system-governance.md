---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-07-06
review_after: 2026-10-05
tags: [knowledge-system, governance]
---

# Knowledge System Governance

This note governs the self-improving knowledge workflow for the USADebusk vault. It extends the existing `CLAUDE.md` insight loop without replacing the current folder structure, heater-card schema, or job/proposal templates.

## Operating Principle

The vault improves through reviewable proposals, not silent rewrites. Agents may inspect, summarize, compare, and propose. Canonical notes change only after approval when the change affects customer-facing content, pricing, safety, field execution, SOPs, or source hierarchy. **Heater-card/facility facts are excluded as of 2026-07-06** — see the Delegated Autonomy Policy's facility-data note.

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

This table is the human-facing core set. The full machine-enforced vocabulary (including review outcomes like `resolved`, `superseded`, `expired`) lives in `tools/vault_lint.py` (`ALLOWED_STATUS`) and is checked on every lint run — that script is the authority for what passes, this table is the guidance for what to reach for.

## Agent Permissions

| Action | Allowed? | Rule |
|---|---|---|
| Create review notes | Yes | Use templates and cite source notes. |
| Suggest tags, links, and properties | Yes | Put suggestions in a review note first when uncertain. |
| Update inbox/source notes | Yes, with care | Preserve raw evidence and original wording. |
| Update canonical knowledge | Approval required | Applies to SOPs, pricing, proposals, safety, and field execution. **Heater-card/facility facts are excluded as of 2026-07-06** — see the Delegated Autonomy Policy's facility-data note below. |
| Delete notes | No | Archive or mark deprecated unless Jesse explicitly approves deletion. |
| Merge conflicting claims | No, except heater-card/facility facts (see facility-data note below) | Create a contradiction note instead. |

## Delegated Autonomy Policy

Four lanes. Every agent action belongs to exactly one. Commit-subject prefixes make the lane visible in `git log`: `[auto]`, `[exp]`, `[default]`, `[gated]`. When unsure which lane applies, act one lane more conservative. This policy refines the ceremony gradient above — it does not replace the Source Hierarchy, the human-gate on operational truth, or the three loops.

**Git note (updated 2026-07-06 — supersedes the 2026-06 "gated" git policy below):** Commit and push are now delegated to the agent's judgment for content-lane work (Lanes 1-3), following each lane's own commit-prefix and staged-file-count discipline. This intentionally reopens what the original policy called "the silent-git-mutation hole" — Jesse reviewed that tradeoff on 2026-07-06 and decided the friction of gating every commit outweighed the risk, given the hard bans below still hold. The prior rule was in `CLAUDE.md`/session instructions, not enforced by tooling, and had been causing cross-session friction (constant re-confirmation, uncommitted work piling up across sessions).

**What stays hard-gated regardless of lane:** force-push, rewriting/amending existing commits, `git reset --hard`, deleting branches, and any push to a shared/customer-facing remote beyond Jesse's own `origin`. Lane 4 (domain truth, irreversibles) still requires an explicit in-session ask before the *content* change is made, independent of the commit/push question — an agent should never promote draft→verified or edit pricing/safety/SOP content unasked, regardless of how freely it can commit.

**Facility-data note (added 2026-07-06):** `02-facilities/` heater cards were designed for a compounding-repeat-heater workflow Jesse doesn't actually have — most bids are first-time heaters with no prior-job library to accumulate onto, and nothing downstream (no skill, no live Claude bid session) currently reads a populated card. Jesse's real-world practice is to infer missing data and use personal judgment rather than chase it down, and confirmed that never hurts his workflow. Heater-card/facility content (Tube Geometry, Connection Info, Task Durations, Job History, facility rate tables — the full card, not just drafting) is now **Lane 1 in full**, including correcting existing facts and resolving discrepancies between sources: capture what's reasonably known using the Source Hierarchy for judgment calls, note a real gap in one line, and move on. No contradiction note, no confidence-tier/verified-gate ceremony, no escalation to Lane 4, unless the card is actively feeding a specific pending bid or customer-facing document *right now* — that's the one case worth double-checking before something wrong goes out the door. The intended future use is repeat-project reference and periodic mining for `usadebusk-estimating`/`usadebusk-core` skill improvements — both are occasional-use, not something to proactively chase precision for.

### Lane 1 — Auto-act (reversible, low-risk: just do it)

**May:** file any inbox item to its home, including operational documents → **draft** heater cards (`status: draft`, `verified: never`, source linked) — drafting is reversible, only *verification* is truth; create/append/refactor notes in `07-llms/`, `08-systems/`, `09-interests/`; fix dead wikilinks with an unambiguous target; normalize frontmatter to schema; file source documents to their home and link them (the `90-sources/` provenance layer is planned — Session B); reorganize a note's internal layout to its schema; `git mv` demonstrably superseded duplicates and generated files to `archive/`; **create, correct, or resolve discrepancies in any `02-facilities/` heater-card or facility-file content** (see facility-data note above — this is the one Lane-1 carve-out that includes correction/promotion, not just drafting).

**Must not:** change the *meaning* of any operational fact **outside `02-facilities/`**; touch pricing, rates, safety, or SOP content values **outside `02-facilities/`**; promote draft → verified **outside `02-facilities/`**; delete anything; rewrite Jesse's own words in his notes; sweep unrelated files into commits.

**Logging:** `[auto]` commit prefix; the diff is the log. No change-log entry.
**Validation:** `tools/vault_lint.py` passes after the change; staged-file count verified before any commit.
**Escalate when:** two plausible homes with different meanings; content contradicts an existing verified fact (→ add to the card's `## Open Flags` and continue — never merge); action would be hard to reverse.

### Lane 2 — Auto-experiment (technical design choices: let tests decide, not Jesse)

**May:** for any technical question (storage format, index structure, script design, schema field format, naming/linking conventions, lint implementation), define measurable success criteria *first*, build competing options in a branch or `tools/fixtures/`, run the comparison, adopt the winner when adoption is reversible, and record method + result + loser in `08-systems/experiments/` (one note per experiment, created on first use).

**Must not:** experiment on domain truth (an experiment can decide how heater data is *stored*, never what a heater's tube ID *is*); let experimental artifacts leak into canonical folders before validation; use external paid services or install heavyweight dependencies; leave a failed experiment's debris outside its branch/note.

**Logging:** `[exp]` commit prefix + the experiment note (criteria, options, result, decision).
**Escalate when:** the winning design implies a Lane 4 change (top-level restructure, breaking schema change) — the experiment note then feeds a Lane 3/4 proposal instead of being self-adopted.

### Lane 3 — Propose-with-default (medium risk: apply the default, make reverting trivial)

**Mechanic (no waiting):** choose the recommended default, **apply it immediately in the same session**, and record it as a one-line entry in `change-log.md` with a stated revert path. It stands unless Jesse objects whenever he next encounters it. Jesse's attention is spent only on disagreement, never on approval.

**May:** create a new subfolder inside an existing domain; add an *additive* schema/frontmatter field; merge two clearly-overlapping knowledge notes (keep both originals in `archive/`); introduce or adjust a template; add a lint rule (must ship with a failing-then-passing fixture — no fixture, no rule); archive a content note that appears obsolete but isn't a duplicate.

**Must not:** batch many unrelated defaults into one commit; apply defaults to domain truth, pricing, safety, SOP values, or customer-facing content; remove or rename *existing* schema fields (that's Lane 4).

**Logging:** `[default]` commit prefix + one change-log line: date | what | default chosen | revert path.
**Escalate when:** Jesse reverts twice in the same area — that area is demoted to Lane 4 and the demotion is recorded here (the policy learns).

### Lane 4 — Human-gated (domain truth and irreversibles: ask, in-session)

**Scope:** promoting any fact draft → verified; editing verified pricing/rates/safety/SOP/customer-facing content; resolving contradictions between sources; true deletion of anything; top-level folder restructuring or renumbering; breaking schema changes (removing/renaming fields across notes); changes to the hard constraints or to this policy itself; anything visible outside the repo (emails, customer docs, publishing).

**Mechanic:** ask synchronously in-session and wait. In unattended runs, do not apply — instead **add a row to the decision queue** (`50-dashboards/decision-queue.md`) for a cross-cutting decision, or an **Open Flag** on the affected card for a card-local operational fact, so it surfaces at point of use. Never apply a Lane 4 change without Jesse's explicit approval.

**Logging:** `[gated]` commit prefix + change-log entry recording Jesse's decision and rationale.

### Area → lane map

| Area | Lane | Notes |
|---|---|---|
| Inbox filing (all domains) | 1 | Operational docs file as **drafts**, not deferred. |
| Heater-card / facility operational facts | 1, in full | Draft, correct, and resolve discrepancies freely — no verify-gate, no contradiction note (see facility-data note above). Escalate only if a card is actively feeding a pending bid/customer document right now. |
| Personal / LLM / systems knowledge (07, 08, 09) | 1 | Zero ceremony. |
| Codebase (`tools/`) | 2 | Design by experiment; new lint rules via Lane 3; hard-constraint enforcement via Lane 4. |
| Schema changes | 3 additive / 4 breaking | Additive field = default-applied; rename/remove = ask. |
| Folder restructuring | 3 within-domain / 4 top-level | New subfolder = default; new/renamed top-level = ask. |
| Source / provenance handling | 1 | Sources are immutable once filed; only additions allowed. |
| Git commit / push | 1-3, per the lane of the content committed | Own changes only, lane prefix, staged-count check; never force-push or rewrite history (see Git note above, updated 2026-07-06). |
| Archival | 1 duplicates+generated / 3 content notes | Always `git mv`, never delete. |
| Deletion | 4, always | And even then archive is the default answer. |

## Core Loops

### Inbox Processing

Process one item at a time. Identify note type, source authority, related facility/job/heater/proposal, candidate tags, and whether the item should become a source note, review note, or canonical update.

`00-inbox/` is a **capture scratchpad with a manual sweep, not a router** — see `01-context/system-workflow-reference.md` for the flow and vault `CLAUDE.md` for the close-out steps.

### Three-Outcome Routing Model

**Moved here 2026-09-08 from `vault-capture-loop-spec.md`, which is retired.** The logic is unchanged; only its trigger is gone. It runs when a session routes a finding at write time, not on a schedule.

| Outcome | Action |
|---|---|
| Clear home in an existing note | Append the content; cite source. |
| Folder exists but no matching note | Create the new note in that folder. |
| Nothing fits | Leave in `00-inbox/`, add top-of-file comment `<!-- vault-loop: no home yet, candidate for [topic] -->`, and report it. |

If `00-inbox/` holds 3+ untagged notes on one theme with no existing home, propose a hub note (suggested filename, target folder, one-line scope). Propose only — do not create the hub or move items without approval.

**What the `<!-- vault-loop: -->` marker means now, and what it no longer means (2026-09-08).** It was the Pre-Staging Loop's only input queue: the loop read marked notes and turned each into an evidence-backed proposal. That loop was disabled 2026-08-21 and its spec retired, so **nothing reads the marker any more.** It still has two live jobs, both passive — it records that a note was *triaged and deliberately parked* rather than overlooked, and `tools/vault_health.py` excludes marked notes from the inbox age metric and from `Sweepable now` on that basis. Keep writing it, for those two reasons. Do not write it expecting anyone or anything to come back to the note: **a marked note waits for Jesse or for a session he asks, and for nothing else.**

A marker is a hold, and **a hold is a promise to release it when its condition is discharged** — nothing checks that you did. This session's own handover note sat `resolved` yet invisible to `Sweepable now`, because its marker still read *"needs Jesse in session"* after he had decided. When the reason for a marker is gone, strike the marker in the same pass.

Two things belong in `00-inbox/` by design and are **not** routing failures: idea seeds, which the idea flow owns, and operational/Lane 4 content, which needs Jesse's call. A document that has no home *yet* — an unknown client, a folder that does not exist — is the third, and is the folder's original job: `change-log.md`, 2026-05-21, *"Syncrude Fort McMurray job report held in inbox — client not scaffolded."*

### Terminal-Note Sweep

**Moved here 2026-09-08 from `vault-capture-loop-spec.md`, which is retired.** This is the vault's only drain and it had been specified inside a `status: deprecated` document since the capture loop stopped on 2026-08-21 — which is the mechanical reason removal ceased: 54 notes left `00-inbox/` in the 29 days before the shutdown and 1 in the 18 days after. Its trigger is now **close-out step 4** in vault `CLAUDE.md`; the rules below are unchanged.

Move any `00-inbox/` file whose `status` is in this **exact allowlist** to `archive/`:

`executed` · `resolved` · `complete` · `superseded` · `spec-complete` · `closed-unactioned` · `deprecated` · `expired`

**The rule this list is derived from** (DQ-029, ruled 2026-09-07). A terminal status means the note will not change again. It does **not** follow that the note should leave `00-inbox/`, and that distinction is the whole question:

- **Sweepable — finished and filed.** The commitment is closed and whatever mattered lives somewhere else now. The eight statuses above.
- **Not sweepable — finished but still load-bearing.** `awarded` and `lost` are live commercial outcomes people search for by facility and job; a lost bid's reasoning is exactly what gets re-read when the customer comes back. `decided-blocked` and `approved-blocked` mean *decided, and waiting on something else* — the decision is closed but the work is not, and burying it loses the only visible trace that something is pending.

**Deriving the allowlist from `TERMINAL_STATUS` in `tools/vault_lint.py` directly is wrong** and this is why: it would sweep all four of those. The two lists are deliberately different, not drifted, and anything that syncs them mechanically re-introduces the defect.

Rules that make this safe, all of them applying to every note type:

- **Never sweep `researched` or `unexplored`.** `researched` means research is done but *Jesse has not decided*; `unexplored` is a seed nobody has needed yet. The prohibition is written on status, not type, so a `researched` note of any type is protected.
- **Status must be read with the loop markers in mind.** A `<!-- vault-loop: -->` or `<!-- vault-prestaged: -->` comment sits *above* the frontmatter fence. `tools/vault_lint.py`'s `frontmatter_start()` handles this — including multi-line comment blocks, fixed 2026-09-08 — so use that behavior rather than a fresh line-0 check. A parser that silently sees no status must **skip**, never sweep.
- **Never rename.** Inbound **wikilinks** resolve by basename and `vault_lint.py` includes `archive/` in its resolution set, so a plain move keeps them green. Renaming breaks them.
- **A move does not protect backticked *path* references, and nothing lints them.** DEAD-LINK only reads `[[wikilinks]]` and POINTER-DEAD only reads absolute source paths, so a swept file's path references dangle silently. After any sweep, grep the moved basenames across the vault and convert **live** references to wikilinks. Do not touch references inside `change-log.md` or dated `06-reviews/` notes — those state where a file was at the time, and history is not rewritten.
- **Never sweep a note carrying `revisit-trigger:`** — that field is a live dormant trigger regardless of the note's status.
- Status values outside the allowlist are left alone and reported, not guessed at.

**Only sweep a file `git ls-files` already shows as tracked.** `archive/` is listed in `.gitignore`, and `.gitignore` governs only *untracked* files: a tracked note stays tracked when moved (git records a rename), so its history survives, but a file that was **never committed** becomes invisible to git the moment it lands there. An untracked file is left in place and reported.

**`git add` after `git mv`, never before.** `git mv` moves the *index entry* rather than re-adding from the working tree, so an edit made before the move stays unstaged and the rename records as `R100` against pre-edit content. That produced a wrong commit on 2026-09-08.

### Contradiction Handling

When two notes disagree, create a contradiction note with the exact claims and source links. Do not resolve by averaging, summarizing away the conflict, or picking the newer note unless the source hierarchy supports it.

### Struck-Down Flags

The mirror case: a flag raised and then ruled not-a-finding. The reasoning gets written where the next reader will land, at one of three tiers by how far the fact generalizes — point-of-use vault note when it is job-specific, skill guardrail when the shape recurs across any future job, assistant memory when it is a rule about evaluating facts rather than a fact. See [[business-normal-facts]], which holds the convention in full plus the register of the facts themselves.

### Retrieval Feedback

When a question is answered poorly, create a question note. Record the expected sources, what was retrieved, what was missed, and what metadata/link/template change would improve retrieval next time.

### Stale Review

Use `review_after`, `last_reviewed`, and `status: stale` to build review queues. A stale note is not wrong; it is due for verification.

### Idea Research

Speculative ideas (`type: idea-seed` in `00-inbox/`) get bounded web research: one seed per run, findings land as a review note in `06-reviews/`, the seed's status flips to `researched`. Never decides, never builds. See [[vault-idea-loop-spec]].

**This runs on demand, not on a schedule (corrected 2026-09-08).** The nightly Idea Research Loop that used to trigger it was stopped 2026-08-21 and nothing replaced it, so seeds accrue in `00-inbox/` until a session is asked to research one. The research logic is unchanged; only its trigger is gone. Loop status is authoritative in [[system-workflow-reference]], never here.

## Architecture Audit

An evidence pass over every loop, tool, lint rule, dashboard metric and structural convention — what each has
actually caused, measured from git rather than from inspection — is at
[[2026-08-20-vault-architecture-audit-evidence]] (2026-08-20). Verdicts are Jesse's and are recorded as a
column in that note. Its headline finding: the 2026-08-15 sweep cleared the review pile to zero and the queue
to two, and both were back at ten within five days, because three loops fire daily and the only clearing
resource is Jesse. Re-run the same method rather than re-deriving one.

## First Pilot Scope

For the first phase, apply this only to new review notes, new source notes, unresolved contradictions, and dashboard views. Do not mass-edit existing job, facility, heater, or proposal notes until the review loop is proven.
