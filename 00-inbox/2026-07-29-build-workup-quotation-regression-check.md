---
type: note
created: 2026-07-29
tags: [inbox, estimating, tooling, build-task]
---

# Wire backtest_workup.py into the fixture-replay guard

**Scope reduced 2026-07-29, before any code was written.** This note originally called for
building a quotation-vs-workup reconciliation check. Recon found
`~/.claude/skills/usadebusk-estimating/scripts/backtest_workup.py` **already is that check** — its
expected values are the submitted quotation side, read from the submitted PDFs, and `check()`
asserts line items, grand total, Pricing Summary box, and that lines sum to total, exiting
non-zero on divergence across all three pairs. Nothing to build there. Decision and full
reasoning: [[2026-07-27-idea-research-quotation-workup-reconciliation-check]].

## What is actually left

`~/.claude/hooks/usadebusk-fixture-replay-guard.mjs` maps `usadebusk-estimating` to fixtures `f1`
and `f6` — the estimating-judgment fixtures. Nothing maps a staged edit to
`usadebusk-estimating/scripts/*` onto `backtest_workup.py`, so editing the extractor does not
prompt a replay of the suite that covers it. Add the mapping and a runner branch.

The hook's own back-test discipline applies: it was gated at a 14% fire rate deliberately, so
check the new mapping's fire rate over real history rather than assuming it is quiet.

## Deliberately not in scope

The **pre-send bid gate** — reading a new, unsubmitted quotation and reconciling it live against
its workup. That is the half with real commercial value, and it is where the `python-docx` direct
read belongs, since a fresh quotation has no frozen expectation. It stays blocked on the
DSP26026-style scope-narrowing rule. Carried as the review note's `revisit-trigger`.

This is a config-repo change (`~/.claude`), not a vault change.
