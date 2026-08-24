---
type: governance
status: active
source_authority: primary
created: 2026-07-07
last_reviewed: 2026-07-29
review_after: 2026-10-29
related:
  - [[vault-capture-loop-spec]]
  - [[vault-skill-drift-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[vault-prestaging-loop-spec]]
  - [[knowledge-system-governance]]
tags: [knowledge-system, agent-loop, consolidation, governance]
---

# Vault Consolidation Loop Spec

The fifth loop, and the one that makes this a wiki rather than a log pile. The capture loop creates and appends; nothing else revisits. This loop periodically rewrites the content layer toward current-best-understanding: merging near-duplicates, converting append-accumulated notes back into clean declarative articles, and linking orphans so knowledge stays discoverable. This is the iterative-rewriting half of the wiki strategy the vault is named for.

Origin: the 2026-07-07 compounding review — lint's ORPHAN check surfaced 18 unlinked notes on day one, and the append-heavy capture pattern guarantees more without a standing counter-force.

## Loop Name

Vault Consolidation Loop

## Trigger

Scheduled monthly (15th of the month, ~3 AM local — offset from the skill-drift loop's 1st) via `mcp__scheduled-tasks`. Runbook prompt: `~/.claude/scheduled-tasks/vault-consolidation-loop/SKILL.md`. Heartbeat tracked by `tools/vault_health.py` under the `vault-consolidate:` prefix (31-day cadence).

## Scope

Operates on the content layers only: `07-llms/`, `08-systems/`, `09-interests/`. These are Lane 1 in full per [[knowledge-system-governance]].

Also does generated-file housekeeping vault-wide: reruns `tools/vault_index.py`, `tools/estimating_rollup.py`, and `tools/vault_health.py` at the end of every run so INDEX.md, the actuals rollup, and the dashboard never go stale for more than a month.

Never touches: `02-facilities/` (**no loop owns it** — the capture loop refuses it too; since the 2026-07-06 facility-data ruling it is Lane 1 for an interactive session, corrected here 2026-07-29), `04-knowledge/` canonical content, `06-reviews/` review-note bodies (Jesse's decision records — naming/frontmatter normalization only, content never), `01-context/`, pricing/SOP/safety content anywhere, skills.

**Scope vs. the orphan metric — measured 2026-07-29.** This loop's link pass and its "ORPHAN count down" success criterion are scoped to 07/08/09, but the vault's 12 current ORPHAN warnings break down as 6 in `04-knowledge/`, 5 in `06-reviews/`, and **1** in `09-interests/`. Eleven of twelve are unreachable by the loop meant to drive the number down, so a run can succeed on its own terms while the dashboard figure barely moves. Read the metric per-folder, not as a total, and do not treat a flat orphan count as this loop failing. Whether `04-knowledge/` and `06-reviews/` orphans should get a linking owner at all is an open question, not a defect — several are deliberately-terminal review notes that nothing will ever naturally link to.

## Ceremony Level

Low. Merging and rewriting within 07/08/09 is Lane 1 (reversible — the loser is archived via `git mv`, never deleted; git history holds every prior wording). Anything ambiguous — two plausible merge directions, content whose home is unclear, a note that might be operational — is left in place and listed in the run report instead of acted on.

## Loop Steps

**Run ledger (every run, first and last action):** Before anything else, update `50-dashboards/.loop-runs.json` (local, gitignored — create if missing): set this loop's entry (`vault-consolidation-loop`) to `{"fired": "<now, UTC ISO-8601>", "completed": null, "result": "running"}`, merging without touching other loops' entries. As the run's very last action — after the final push, or immediately on deciding the run is a no-op or hitting a fatal problem — set `completed` to now and `result` to `committed`, `no-op`, or `error: <one line>`. Use Write/Edit tools, never shell editors. `tools/vault_health.py` reads this file to tell a dead scheduler from a quiet loop; a run that skips it surfaces as a monitoring FAIL.

1. Run `py -3 tools/vault_lint.py` and collect the current ORPHAN and DEAD-LINK findings for 07/08/09.
2. **Merge pass (max 3 merges per run):** find near-duplicate notes covering the same topic; fold the weaker into the stronger (preserving any unique facts and source attributions), `git mv` the emptied loser to `archive/`, update inbound links. When merge direction is ambiguous, skip and report.
3. **Rewrite pass (max 3 notes per run):** notes that have accumulated appended fragments (trailing "Update:" blocks, contradictory paragraphs, session-note stubs) get rewritten as a single declarative article in present tense. Never drop a fact or a source line; never rewrite text Jesse wrote himself — agent-harvested content only.
4. **Link pass (unbounded):** give orphaned 07/08/09 notes real inbound links from the notes that should reference them; fix dead links with unambiguous targets. A note that has no natural linking neighbor after a genuine attempt is a candidate for archive — propose in the run report, do not archive unilaterally on first sight.
5. **Seed-status reconciliation pass (added 2026-08-21, report-only):** check whether an idea seed's recorded status still matches what actually landed, in **both** directions. Forward: a seed at `status: researched` whose work has since been built — the status outlived the build and now hides finished work in the pile. Inverse: a seed at a *terminal* status whose work was never built — `archive/idea-pig-load-list-generator.md` is the live example, sitting at `status: complete` while its own closing paragraph says the load-list generator "was not built and is not closed by this," which is exactly how a future session concludes a tool exists when it does not. **The inverse direction must read `archive/` explicitly** — `SKIP_SCAN` hides that folder from every lint rule, so nothing else looks there. Report mismatches in the run report; do not restatus a note unilaterally, since a status is a claim about work rather than a formatting question. This replaced a proposed per-seed disk check, which scored 0 of 5 against the live population.
6. Regenerate: `py -3 tools/vault_index.py`, `py -3 tools/estimating_rollup.py`, `py -3 tools/vault_health.py`.
7. `py -3 tools/vault_lint.py` — 0 errors required; the run should reduce (never increase) the ORPHAN count.
8. Commit and push touched paths only: `vault-consolidate: <YYYY-MM> — N merged, M rewritten, K linked`. The `vault-consolidate:` prefix is the heartbeat. Use Edit/Write tools for all content changes, never `sed -i` (known-unreliable in this environment).

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Merge near-duplicates within 07/08/09 | Max 3 per run; loser archived via `git mv`, never deleted. |
| Rewrite agent-harvested notes declaratively | Max 3 per run; no fact or source dropped; never Jesse's own words. |
| Add/repair wikilinks across 07/08/09 | Unbounded; this is the compounding work. |
| Normalize frontmatter and filenames to convention | Includes undated files in dated folders. |
| Rerun the three generators + lint | Generated files are the sanctioned overwrite exception. |
| Commit/push touched paths | `vault-consolidate:` prefix, staged-count discipline. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Deleting anything | Archive only, ever. |
| Touching 02-facilities, 04-knowledge canon, 06-reviews bodies, 01-context, skills | Other loops and lanes own them. |
| More than 3 merges + 3 rewrites per run | Keeps each run reviewable in one git diff sitting. |
| Merging notes whose content conflicts | A contradiction is a finding, not a merge — report it; the skill-drift loop or a session resolves it. |

## Stop Conditions

Stop and report when: a merge would lose information it cannot carry over; content in scope turns out to be operational; lint errors appear that the run did not introduce; git state is ambiguous.

## Success Criteria

A successful run leaves the content layers measurably tidier — ORPHAN count down, duplicates merged, index fresh — with a diff Jesse can skim in two minutes. Silent deletions, meaning changes during rewrite, or a growing orphan count across runs are failures.
