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

This note governs the self-improving knowledge workflow for the USADeBusk vault. It extends the existing `CLAUDE.md` insight loop without replacing the current folder structure, heater-card schema, or job/proposal templates.

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

### Contradiction Handling

When two notes disagree, create a contradiction note with the exact claims and source links. Do not resolve by averaging, summarizing away the conflict, or picking the newer note unless the source hierarchy supports it.

### Retrieval Feedback

When a question is answered poorly, create a question note. Record the expected sources, what was retrieved, what was missed, and what metadata/link/template change would improve retrieval next time.

### Stale Review

Use `review_after`, `last_reviewed`, and `status: stale` to build review queues. A stale note is not wrong; it is due for verification.

### Idea Research

Speculative ideas (`type: idea-seed` in `00-inbox/`) get bounded, unattended web research on a nightly schedule rather than sitting until someone manually revisits them. One seed per run, findings land as a review note in `06-insights/`, the seed's status flips to `researched`. Never decides, never builds. See [[vault-idea-loop-spec]].

## First Pilot Scope

For the first phase, apply this only to new review notes, new source notes, unresolved contradictions, and dashboard views. Do not mass-edit existing job, facility, heater, or proposal notes until the review loop is proven.
