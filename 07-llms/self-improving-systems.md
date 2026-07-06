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

## What's planned: capture loop

A loop that polls `00-inbox/`, proposes how to file or process each item, and waits for confirmation before writing. The key design constraint is **propose-don't-commit**: the agent suggests actions, the human approves, and only then does the write happen. This prevents automated logic errors from silently corrupting vault state.

This is explicitly a "not yet built" item — the architecture is designed, the motivation is clear, but it hasn't been wired up.

## References evaluated

- **jaredrhod/ai-memory-vault** — explored this repo as a reference for automated memory management patterns
- **sam-illingworth/audit-setup** (GitHub Claude Code skill) — implements a four-step configuration review pattern for auditing a tool/platform setup. Surfaced while researching the recurring "cold-start tax" problem (re-deriving optimal setup/config/patterns each time a new tool or platform is adopted). Found to already cover much of that need, which is why the resulting decision favored a lightweight dossier template (`templates/_setup-scout-template.md`) over building new harness/skill infrastructure, gated by a two-pilot trial before any skill/loop conversion.
- (Placeholder — add other repos, videos, or articles evaluated as this area develops)

## Broader pattern

The general loop structure: observe (read current state) → propose (generate suggested action) → confirm (human approval gate) → execute (write/commit) → report (log what changed). Skipping the confirm step is the failure mode that turns a useful tool into an unpredictable one.

Related: [[cowork]], [[code]]
