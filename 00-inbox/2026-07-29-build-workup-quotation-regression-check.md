<!-- vault-loop: operational — config-repo (~/.claude) build task wiring backtest_workup.py into the fixture-replay guard, Lane 4 estimating scope. Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-11-prestaged-backtest-workup-fixture-mapping.md -->
---
type: note
status: resolved
created: 2026-07-29
closed: 2026-08-15
tags: [inbox, estimating, tooling, build-task]
---

# Wire backtest_workup.py into the fixture-replay guard

> **Closed 2026-08-15** by the retirement sweep — bookkeeping only, no new decision. This note carried no `status` field, which is what kept it invisible to the Terminal-Note Sweep (see [[2026-07-29-statusless-notes-invisible-to-the-sweep]]); `status: resolved` added here. Ruled as DQ-011: **no hook change.** The load-bearing unknown resolved no — f1 and f6 are *conversation* fixtures, replay prompts pasted to a model, carrying no `.xlsx` and invoking no Python, so they cannot exercise the scripts and the mapping would have been a replay that proves nothing. The cited 25% miss rate was also wrong: the one cited miss (`beb24ed`) records "Not in any frozen fixture, so no replay impact" in its own commit body, and its diff is one T&C string in `render_proposal.py`, which `backtest_workup.py` never calls. Substantive-miss count over the full history is zero.

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

## Pre-send bid gate — unblocked 2026-07-29, not yet built

The half with real commercial value: read a new, unsubmitted quotation and reconcile it live
against its workup before it goes to a customer. This is where the `python-docx` direct read
belongs, since a fresh quotation has no frozen expectation to compare against.

**No longer blocked.** Jesse ruled the scope-narrowing rule on 2026-07-29 and it is written into
`usadebusk-estimating` SKILL.md under the mob/demob reconciliation rules: compare scope before
dollars — matched scope with a totals gap blocks, narrower scope re-prices at the workup's own
rates and passes with a one-line note, wider scope blocks unconditionally. Gap size is never the
instrument. Narrowing runs a few times a year, so the matched-scope path is the normal one.

Build notes when it is picked up: reuse `extract_workup.extract()` and the existing
`_is_lump_sum_gap()` mob/demob exemption rather than re-deriving either; the scope comparison
needs the quotation's task hours and heater list, which the Section 7 line descriptions carry
("[N] Rig-in | [N] Pig | [N] Smart Pig | [N] Rig-out"); invoked deliberately on one pair at
submission, never on a schedule.

This is a config-repo change (`~/.claude`), not a vault change.
