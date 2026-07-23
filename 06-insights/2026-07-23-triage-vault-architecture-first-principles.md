---
type: triage-note
status: for-review
source_authority: inferred
confidence: medium
created: 2026-07-23
review_after: 2026-08-23
related:
  - knowledge-system-governance
  - 2026-07-19-rate-model-grain-review
  - 2026-07-20-harness-map
tags: [triage, knowledge-system, vault-architecture, brainstorm]
---

# Triage — Vault Architecture First-Principles Exploration

Propose-only brainstorm session (2026-07-23, Fable 5) on the knowledge system's own structure. Design layer read in full before proposing: [[knowledge-system-governance]], [[workflow-map]], [[system-workflow-reference]], the health dashboard, all four `tools/` scripts, and prior art across [[2026-07-19-rate-model-grain-review]], [[2026-07-20-harness-map]], [[2026-07-09-idea-research-context-packet-builder-skill]], [[rfq-intake-protocol]], [[knowledge-system-evaluation-questions]], [[vault-source-of-truth]], and the current inbox seeds. Nothing was built; this note records the dispositions.

## Central finding

The vault has strong machinery for **state** — status vocabulary, `review_after`, loop heartbeats, lint locks, generated dashboards — and none for **conditions**. Every time the system defers something, it records a wake-up condition in prose that nothing will ever evaluate: the rate-history rollup deferred at "~12 quote notes" ([[rfq-intake-protocol]] open questions), the contract-note type rejected with revisit trigger "first bid under a multi-year agreement" ([[2026-07-19-rate-model-grain-review]] §C), the context-packet builder parked on "real mobilization friction," and quote validity dates living only in body prose. `review_after` → REVIEW-OVERDUE is the one trigger that got mechanized, and it works. The generalization — a dormant-condition ledger — is the missing primitive, and it matches how Jesse actually operates: he doesn't track triggers; the dashboard is how pending work reaches him.

## 1. Trigger registry (dormant-condition ledger) — EXECUTE

A generated `## Dormant triggers` section on the health dashboard, sourced from a new additive `revisit-trigger:` frontmatter field on parked seeds and deferred/rejected review items, plus a one-time sweep of the four known prose triggers. Countable conditions (quote-note count vs. the rollup's threshold of 12) get script-checked in `vault_health.py`; event-shaped conditions (first multi-year bid) get tagged with the workflow step that should check them, and [[rfq-intake-protocol]] gains one line: check intake-scoped triggers. Red-teamed: the kill case is a meta-registry nobody feeds, but the feeding already happens — the idea-triage skill mandates parks record triggers, review notes already record them in prose — and two real triggers have gone dark since July 18–19. Survives at minimal scope: a health.py section plus a field convention, not a new tool or loop. Lane 3.

**Execution brief:** In `vault_health.py`, scan non-terminal notes for `revisit-trigger:`; render one row each (source note, condition, machine-checkable, fired). Implement the quote-count check first. Backfill `revisit-trigger:` onto [[idea-context-packet-builder-skill]], the rate-grain review §C, and the rollup deferral. Add the intake-check line to [[rfq-intake-protocol]]. Same GENERATED discipline as the rest of the dashboard.

## 2. Commercial pipeline vitals — EXECUTE

The vault knows nothing about the future: quotes expire silently and awarded work approaches with no lead-time signal. Verified against DSP26039: quote frontmatter already carries `date-submitted`, `date-execution`, `status: pending` — only `valid-through` lives in body prose. So this is roughly thirty lines in `vault_health.py` plus one additive frontmatter field backfilled onto the three or four existing quote notes. Red-teamed against the premature-structure precedent (rate rollup deferred at four notes): a rollup needs mass to be useful, but expiry and horizon checking is per-item and useful at n=1, and the manual table is already dropping data (DSP26080's "Valid Through: Not recorded"). This is the one category the cross-cutting-over-project-detail preference exempts — live commercial exposure. Lane 3.

**Execution brief:** Add `valid-through:` to quote frontmatter; backfill from body text. In `vault_health.py`: for pending quotes, flag past-validity (FAIL row) and validity-within-30-days; for quotes with `date-execution` within 90 days, render an informational "coming up" row. Shares a chassis with idea 1 — one build session covers both.

## 3. Retrieval-eval run — TEST

The five loops all maintain content; nothing measures whether the system answers well. The measurement layer exists on paper — [[knowledge-system-evaluation-questions]] defines ten questions with pass criteria, and governance defines the `type: question` feedback note — but zero question notes exist and the evals have never been run. **Test:** one fresh session answers all ten KS/USA questions cold, graded against the note's own pass criteria. **Criterion:** two or more failures → fold a quarterly eval pass into the consolidation loop's spec (a pass, not a sixth loop — the loop set is right); zero or one → retrieval isn't the constraint at this vault size, record that and stop. **Deadline:** within two weeks, well before the eval note's own `review_after` (2026-09-26).

## 4. LLM-navigable vault map (INDEX description hooks) — PARK

`INDEX.md` is titles-only; the harness already proves one-line description hooks drive relevance decisions at two other layers (MEMORY.md, skill descriptions). Parked rather than tested because the right shape is an open research question with real prior art to mine (Obsidian power users: MOCs vs. per-note descriptions vs. generated summaries), and because idea 3 gates it — zero retrieval failures would mean this solves a problem that doesn't exist. Seed filed: [[idea-llm-navigable-vault-map]].

## 5. POINTER-DEAD estate-path check — TEST

The vault-as-index-over-file-estate boundary is enforced only by prose ("an unrecorded path is how a bid trail goes cold"). DEAD-LINK covers wikilinks; nothing verifies that recorded OneDrive paths still resolve. Red-teamed hard: this re-couples a vault check to one machine's filesystem right after [[vault-source-of-truth]] deliberately de-hardcoded machine paths, and OneDrive Files-on-Demand placeholder behavior under `os.path.exists` is unverified. **Test:** a 30-minute spike — do cloud-only placeholders resolve sanely, and does skip-if-root-missing make the rule silently portable? **Criterion:** both yes → warn-only lint rule with fixture (no fixture, no rule); either no → kill, the intake-protocol convention stays the only guard. **Deadline:** next tools-touching session.

## 6. Staged-file-count PreToolUse hook — EXECUTE (carried, not novel)

The top rule-5 lock candidate from [[2026-07-20-harness-map]] §2, still unbuilt: a yes/no machine check living as CLAUDE.md prose. The git-guard hook is the exact precedent. Config-repo work, gated per the harness map's own framing — listed here so it stops being an orphaned follow-up.

## 7. Contract/rate-profile object — KILL (duplicate)

Adjudicated 2026-07-19: [[2026-07-19-rate-model-grain-review]] §C, rejected by Jesse — no multi-year agreement is live on his accounts and quote-grain `rate-basis` covers every current case. Re-proposing would re-litigate a decided question without new information; its revisit trigger moves into the idea-1 registry.

## 8. Customer/contact (CRM) layer — KILL

Relationship data belongs to the Outlook three-tier plus Copilot architecture; the vault indexes facts, not relationships, and the one real signal (which departments send work) is already covered by the optional `department` field approved in the rate-grain review §D.

## 9. Schema-as-data single source — KILL

The Task-Durations schema's exemplar/template/lint-tuple/skill homes are a deliberate two-home sync with a lock; the schema changed once in a month. Generator machinery would cost more than the drift risk it removes at this change rate.

## 10. Lane-3 revert detector — KILL

The governance clause "Jesse reverts twice → demote the area to Lane 4" has no detection mechanism, but the triggering event is rare, semantic revert detection from diffs is unreliable, and Jesse notices his own reverts. Ceremony without payoff.

## 11. Full estate reverse-index — KILL

Sweeping OneDrive/SharePoint for unindexed files is unbounded policing of an estate the vault deliberately doesn't own — the automation shape already rejected. Idea 5, if its test passes, covers the observed failure mode at a fraction of the cost.

## 12. Memory↔vault dedupe structure — KILL (duplicate)

The overlap is real but already owned by the consolidate-memory skill and the harness map's collision ledger. No new structure.

## Tally

**3 execute / 2 test / 1 park / 6 kill.** Pursue first: trigger registry, then commercial pipeline vitals (same `vault_health.py` chassis — one build session covers both), then the retrieval-eval run (nearly free, and it gates the parked idea 4).

## Decision

- [x] Build ideas 1 + 2 (trigger registry + pipeline vitals) — approved by Jesse and built same session, 2026-07-23
- [ ] Build idea 6 (staged-count hook, config repo — gated)
- [x] Run test 3 (retrieval-eval session) — ran cold 2026-07-23, 10/10 pass, 0 failures. Criterion → **stop**: retrieval isn't the constraint at this vault size. Idea 4 stays parked (gate not met). See [[2026-07-23-retrieval-eval-run]].
- [x] Run test 5 (OneDrive placeholder spike) — ran same session; both criteria passed, POINTER-DEAD rule built with fixture
- [ ] Reject / adjust any of the above (note which)

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-23 | Note filed from brainstorm session; seed [[idea-llm-navigable-vault-map]] created; nothing built, no canonical content modified | Claude (Fable 5) |
| 2026-07-23 | Jesse approved building in-session. Ideas 1+2 applied: `vault_health.py` gains Commercial pipeline + Dormant triggers sections and two metric rows; `valid-through:` backfilled on all six quote notes (DSP26030 normalized to `type: quote, status: pending`); `revisit-trigger:` backfilled on the three known prose triggers; intake-check line added to [[rfq-intake-protocol]] | Claude (Fable 5) |
| 2026-07-23 | First run caught real exposure: DSP26030 expired 49 d ago with outcome unrecorded (standing FAIL row until resolved); rollup trigger reads 6 of 12 quote notes | Claude (Fable 5) |
| 2026-07-23 | Test 5 executed, both criteria passed; POINTER-DEAD rule added to `vault_lint.py` (warn-only, base-gated, runtime fixture; self-test 11 rules). First run: 4 of 6 recorded source paths dead (estate reorg `Desktop\` → `Desktop\Facilities\`). DSP26080 re-pointed — its estate folder carried a trailing U+00A0, renamed off (OneDrive) — 3 warnings stand as the re-pointing to-do | Claude (Fable 5) |
| 2026-07-23 | Test 3 (retrieval-eval) ran cold in a fresh session: all 10 KS/USA questions answered against pass criteria, 10/10 pass, 0 hard failures. Two shallow passes flagged (USA-005 stale-lead-paragraph risk; KS-004 scan-not-lookup). Criterion (≤1 failure) → stop; no sixth loop, no quarterly pass. Idea 4 stays parked. Eval note `last_reviewed` → 2026-07-23. Result note [[2026-07-23-retrieval-eval-run]] filed | Claude (Opus 4.8) |
