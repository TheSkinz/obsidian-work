---
title: Self-Improving Systems
created: 2026-06-29
tags: [automation, ai-loops, capture-loop, knowledge-systems]
---

# Self-Improving Systems

The concept: automated agent loops that audit, ingest, prune, and improve a knowledge base (or workflow) over time — without requiring per-task human initiation. The knowledge base gets better as a side effect of using it, rather than requiring dedicated maintenance sessions.

## What's been prototyped

**Codex inbox experiment** — tested an automated inbox processing loop that classified and routed raw inputs. Demonstrated feasibility of the capture-then-propose model but wasn't deployed to production.

**Cowork scheduled task (1pm work brief)** — the first real deployed loop. Not a self-improving system in the full sense, but it's the foundation: an agent that runs on a schedule, reads vault state, and produces output. See [[cowork]] for details.

**`leverage` repo thesis experiment (2026-07-02 through 2026-07-06)** — a pre-registered test of the Verification Layer's core claim: does a cheap model + executable gate + feedback-driven retry approach frontier-model quality on structured extraction, at much lower cost? Ran the full 30-item corpus live against `claude-fable-5` (frontier) and `claude-haiku-4-5-20251001` (cheap) with real pricing. Result: **inconclusive** — all three conditions (frontier-1-shot, cheap-1-shot, cheap+gate+retry) hit 100% pass rate, so the corpus had no headroom to show whether the gate+retry loop adds value over the cheap model alone. Cost-wise, cheap-model conditions ran at roughly 0.1x the cost per correct output of the frontier model. Notably, a first pass at the full run looked like the frontier model performed far worse than the cheap model (0.795 vs 0.962 pass@1) — auditing every failure showed 100% were a scoring-rule blind spot (the matcher required exact string equality whenever a value looked numeric, so "22 dollars" failed against a reference "22" even though the extraction was correct), not a real capability gap. Lesson for any programmatic LLM-output evaluator: audit failures before trusting an aggregate score, especially when a result contradicts prior expectations — a stricter-than-intended matcher can manufacture a false signal. Next step per the experiment's own design: a harder corpus is needed to actually test the claim; more items at the current difficulty won't help.

## What's planned: capture loop

A loop that polls `00-inbox/`, proposes how to file or process each item, and waits for confirmation before writing. The key design constraint is **propose-don't-commit**: the agent suggests actions, the human approves, and only then does the write happen. This prevents automated logic errors from silently corrupting vault state.

This is explicitly a "not yet built" item — the architecture is designed, the motivation is clear, but it hasn't been wired up.

## References evaluated

- **jaredrhod/ai-memory-vault** — explored this repo as a reference for automated memory management patterns
- **sam-illingworth/audit-setup** (GitHub Claude Code skill) — implements a four-step configuration review pattern for auditing a tool/platform setup. Surfaced while researching the recurring "cold-start tax" problem (re-deriving optimal setup/config/patterns each time a new tool or platform is adopted). Found to already cover much of that need, which is why the resulting decision favored a lightweight dossier template (`templates/_setup-scout-template.md`) over building new harness/skill infrastructure, gated by a two-pilot trial before any skill/loop conversion.
- **8-agent GitHub skill-discovery pipeline** (Scout → Filter → Reader → Workflow Extractor → Skill Score → Skill Generator → Reviewer → Publisher, gated by human PR review) — evaluated 2026-07-12, **not adopted**. The vault already covers the pattern's useful parts at single-operator scale: doc-before-code reading order is already the norm, deterministic checks before LLM judgment are already implemented (`tools/vault_lint.py`'s 7 rules, `tools/vault_health.py`), and human-approves-the-output is already how skill/SOP changes get made. Standing up a multi-agent GitHub-scanning pipeline would add discovery/triage overhead without solving a real bottleneck here — skills aren't scarce, time to use them is.
- (Placeholder — add other repos, videos, or articles evaluated as this area develops)

## Broader pattern

The general loop structure: observe (read current state) → propose (generate suggested action) → confirm (human approval gate) → execute (write/commit) → report (log what changed). Skipping the confirm step is the failure mode that turns a useful tool into an unpredictable one.

Related: [[cowork]], [[code]]
