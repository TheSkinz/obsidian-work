---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-24
review_after: 2026-08-24
related:
  - [[idea-lint-lock-heater-schema]]
  - [[vault-idea-loop-spec]]
tags: [review, knowledge-system, idea-research, lint, already-covered]
---

# Idea Research — Lint Lock on Heater-Card Task-Durations Schema

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Two idea-seeds were `unexplored` in `00-inbox/`: this one (`created: 2026-07-20`) and `idea-llm-navigable-vault-map` (`created: 2026-07-23`). This one is oldest by frontmatter `created` date, so it was processed this run per the one-item selection rule.

## Evidence

**Internal — the idea is already built, same day it was captured.** `tools/vault_lint.py` already contains a `DURATIONS-HEADER` rule (lines 366-403) that does exactly what the seed proposes: it anchors on the `## Task Durations` heading (not on any token like `Rig-In`, which also appears in cost/rate tables and prose — the seed's own worry, addressed directly), reads the first table row beneath it, and fails any file whose header doesn't match the canonical column set. `git log` shows the rule was added in commit `b7f5df3`, "Add DURATIONS-HEADER lint rule (harness-map rule-5 lock)," timestamped 2026-07-20 20:02:14 — the same calendar day this idea-seed was created, and citing the same harness-map rule-5 principle ("hard rules need hard checks") the seed itself invokes. A failing fixture exists at `tools/fixtures/02-facilities/TestClient/Test-City-TX/T-200.md`, which explicitly omits the trailing `Condition` column and is annotated "Lint must flag DURATIONS-HEADER on this file" — this is the "failing-then-passing fixture per the Lane 3 lint-rule convention" the seed asked for, and it fires in `vault_lint.py --self-test`.

**The seed's three open questions are each answered by the code as shipped:**
1. *Scope — 02-facilities only, or any file that inlines the columns?* Answered as the broader option: `check_durations_header` iterates over every collected note in the vault, not just `02-facilities/`, so it would have caught the CLAUDE.md drift directly, exactly as the seed hoped.
2. *Severity — warning or error?* Answered as warning (`DURATIONS-HEADER` is not in `ERROR_CODES`), consistent with the file's stated policy that a header fix is "a to-do, not a stop-the-line."
3. *How to read the canonical header without hard-coding it (parse the exemplar at runtime)?* **Not** answered the way the seed asked — the shipped version hard-codes `DURATIONS_HEADER` as a tuple in `vault_lint.py` (lines 103-106), with a code comment acknowledging the tradeoff explicitly: "the exemplar is the human-facing authority; this tuple is the machine-checked copy... if the schema ever changes, change it in the exemplar and here in the same commit." This is a manual-sync policy, not the runtime-parse-from-exemplar design the seed's "To explore" section asked about.

**External — the manual-sync tradeoff is a known, named failure mode, but the field's own fix is heavier than this vault's scale needs.** A search on schema/validator drift (skippednote.dev, "Verification schema drift in agent code checks") describes the general problem: when a schema and its checker are authored separately, they become "two separate policies with similar names," and the mismatch surfaces only after effort has been spent trusting an artifact that was actually invalid. That is the exact risk the vault_lint.py comment flags and accepts. The field's fix (linkml's schema-linter, Atlas's migration-lint, Skeema) is to parse the schema definition file directly at check time — plausible here too, since the exemplar is already a well-defined markdown table the same `split_table_row` helper could read. But those tools operate at a scale (multi-service schemas, database migrations) where hand-sync realistically drifts unnoticed for a long time; this vault's exemplar changes rarely (one column added in the last several months) and both files sit in the same repo, so a drift would surface at the next commit touching either one, not silently over months.

## Interpretation

**Already covered — fully, not partially.** The core ask (machine-checked lock, heading-anchored, broad scope, warning severity, fixture-backed) shipped same-day as the idea-seed, apparently in the same working session that produced the harness-map note the seed cites, and the idea-seed was simply never marked `researched`/closed afterward. The one sub-question left genuinely open — hard-coded tuple vs. runtime-parsed-from-exemplar — is a real design choice, not an oversight, and the code's own comment shows it was made consciously with the tradeoff named. Given the exemplar's low change frequency and single-repo colocation, hard-coding with an explicit "change both in the same commit" comment is a reasonable, cheap choice at this vault's scale; runtime-parsing would remove the last bit of manual-sync risk but adds parsing-fragility risk (the exemplar's own table format would become load-bearing input to the linter, not just documentation) for a schema that has drifted exactly once in the vault's history.

## Recommended Action

**Drop as a build item — it's done.** No further building needed. Optionally, if Jesse wants the hard-coded-vs-runtime-parsed question closed rather than left as an accepted tradeoff, that's a small, separate one-shot (read `_canonical-heater-card.md`'s Task Durations header at lint time instead of the `DURATIONS_HEADER` tuple) — cheap, but not required; the current state already satisfies the seed's core goal of turning the schema from a prose reminder into a machine-checked lock.

## Decision

- [ ] Approved — close as already-built, no action
- [ ] Approved with edits — also do the runtime-parse refactor
- [ ] Park
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
