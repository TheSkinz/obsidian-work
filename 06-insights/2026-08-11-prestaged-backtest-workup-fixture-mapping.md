---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-11
related:
  - "[[2026-07-29-build-workup-quotation-regression-check]]"
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
tags: [review, knowledge-system, tooling, estimating, regression]
---

# Review — Should `backtest_workup.py` script edits get a fixture-replay-guard mapping?

## Trigger

Pre-staging loop run 2026-08-11, processing `00-inbox/2026-07-29-build-workup-quotation-regression-check.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker. (Tied on filename date and git first-commit timestamp with `00-inbox/2026-07-29-syncrude-6-ft-hr-fill-flush-question.md`; broken alphabetically per the spec's fallback order having no further signal — that item remains queued for the next run.)

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-29-build-workup-quotation-regression-check.md` (read this run) | Observed | After the 2026-07-29 scope correction (see next row), the only remaining ask: `~/.claude/hooks/usadebusk-fixture-replay-guard.mjs` maps `usadebusk-estimating` SKILL.md edits to fixtures `f1`/`f6`, but nothing maps a staged edit to `usadebusk-estimating/scripts/*` (specifically `backtest_workup.py`, the already-built quotation-vs-workup reconciliation) onto a replay requirement. Explicitly flags that the hook's own back-test discipline applies: check the new mapping's fire rate over real history before assuming it's quiet, rather than adding it on faith. |
| `~/.claude/hooks/usadebusk-fixture-replay-guard.mjs:53-60,79-90` (read this run) | Observed | `SKILL_FIXTURES` maps `usadebusk-estimating` → `['f1','f6']`. `fixturesFor()` matches staged paths only against the regex `^skills\/([^/]+)\/SKILL\.md$` — a script under `scripts/` cannot match this pattern under any staged-file set. Confirms the inbox note's claim exactly: the gap is real, not stale. |
| `~/.claude/` git log, `--diff-filter=A -- skills/usadebusk-estimating/scripts/` (read this run) | Observed | 5 commits ever touched that directory: `013986c` (2026-07-24, generator build), `677d447` (2026-07-25, mob/demob fix), `a4ed96f` (2026-07-25, canonical-root fix), `beb24ed` (2026-07-27, legal-name T&C fix), `c01bc27` (2026-07-27, "house spelling" pass). |
| `~/.claude/` `git show --stat` on each of the 5 commits (read this run) | Observed | `c01bc27`'s own subject line ("style: house spelling...") matches the hook's existing `COSMETIC` regex (`house style\|house spelling`) and would not fire regardless of any new mapping — correctly excluded already. Of the remaining 4 substantive commits, only `013986c` also touched `usadebusk-estimating/SKILL.md` in the same commit (already covered today by the existing mapping); `677d447`, `a4ed96f`, and `beb24ed` touched `scripts/` alone, invisible to the current hook under any staged-file set. |
| `~/.claude/regression/runs/claude-opus-5/*` directory listing (read this run) | Observed | Of the 3 scripts-only substantive commits: `677d447` and `a4ed96f` (both 2026-07-25) have same-day `f1-*-2026-07-25*` and `f6-*-2026-07-25*` files — replayed anyway, by habit, not by any gate. `beb24ed` (2026-07-27) has no `f1` or `f6` file dated 2026-07-27 anywhere in the runs directory — a genuine miss the current hook cannot see and did not catch. |
| `usadebusk-fixture-replay-guard.mjs:17-29` (comment block, read this run) | Observed | The hook's own documented precedent: back-tested at BROAD 100%, CO-COMMIT 100%, NARROW (the adopted design) 14% (3/21) over the SKILL.md-mapped case. The scripts/* case computed this run: 3 of 4 substantive commits (75%) are invisible to today's SKILL.md-only mapping, and 1 of those 3 (33%, or 25% of all 4 substantive commits) had no same-day replay at all — a real miss, same failure mode ("forgot entirely") the hook exists to catch, on a different file pattern the mapping does not yet reach. |

## The Question

Should `usadebusk-fixture-replay-guard.mjs` gain a mapping from `usadebusk-estimating/scripts/*` (starting with `backtest_workup.py` and its sibling `extract_workup.py`) onto fixtures `f1`/`f6` — mirroring the existing `SKILL_FIXTURES` pattern — given the back-test shows a real, non-cosmetic miss (`beb24ed`, 2026-07-27) that the current SKILL.md-only mapping structurally cannot see?

## Proposed Change

**A. Add a `SCRIPT_FIXTURES` map (or extend `fixturesFor()`'s regex to also match `scripts/*.py` under a mapped skill directory) so a staged edit to `usadebusk-estimating/scripts/*` requires the same `f1`/`f6` same-day replay `SKILL.md` edits already require.** Smallest change: one new regex branch in `fixturesFor()`, reusing every other piece of the hook (cosmetic filter, sentinel escape, warn-never-block behavior) unmodified. The measured gap (1 real miss in 4 substantive commits, 25%) sits above the 14% NARROW band the hook's own comment cites as justification for the design it already ships — this is not a marginal case.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Map `scripts/*` to a narrower or different fixture set than `f1`/`f6`, on the theory that a reconciliation-script edit (`backtest_workup.py`/`extract_workup.py`) is validated by running `backtest_workup.py`'s own three-pair check directly, not by replaying the `f1`/`f6` conversation fixtures.** The hook's replay mechanism only knows how to check for a dated file in `regression/runs/<model>/`; wiring a second, different verification path (running the script and checking its exit code) would need its own runner branch rather than reusing `missingReplays()`. Larger change than A; only worth it if `f1`/`f6` replays don't actually exercise the reconciliation logic (unverified this run — would need reading what `f1`/`f6` cover to confirm or rule out).

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Leave it unmapped — the 2026-07-25 pair replayed anyway by discipline, and one miss in a 4-commit sample is too small to generalize a rate from.** Counter to this: the hook's own adopted NARROW design was itself justified on a 21-commit sample at 14%; a 4-commit sample at 25% is smaller but points the same direction, not the opposite one, and the miss (`beb24ed`) was a real rule change (legal-name text in a customer-facing T&C line) landing with zero same-day verification — exactly the failure mode the hook exists to catch, not a false positive.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

The sample is small — 4 substantive commits total, 3 scripts-only — so "25% miss rate" is one commit, not a stable statistic; a future run with more history could show the true rate is much lower (or higher). Option A's risk is scope creep in the regex: matching `scripts/*.py` broadly could pull in files that don't touch reconciliation logic at all (e.g. a future unrelated script under the same directory) and start requiring replays that don't test anything real — the mapping should name `backtest_workup.py`/`extract_workup.py` specifically rather than the whole `scripts/` glob, which the inbox note's own phrasing ("scripts/*") doesn't distinguish. Option B is the more mechanically correct fix (replay the thing that actually tests the change) but is unverified this run whether `f1`/`f6` even exercise `backtest_workup.py`/`extract_workup.py` at all — if they don't, Option A would be requiring a replay that proves nothing, which is worse than no gate. This review did not read fixtures `f1`/`f6` themselves to confirm coverage; that is the load-bearing unknown for choosing between A and B.

## Decision

*(Jesse: check one box per lettered option above.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-11 | Note filed by pre-staging loop from `00-inbox/2026-07-29-build-workup-quotation-regression-check.md`. Confirmed the gap is real by reading `fixturesFor()`'s regex directly (SKILL.md-only, cannot match `scripts/*`). Ran the back-test the inbox note itself asked for: 5 commits ever touched `usadebusk-estimating/scripts/`, 1 excluded as cosmetic by the existing filter, 3 of the remaining 4 invisible to the current mapping (no co-committed SKILL.md), 1 of those 3 (`beb24ed`, 2026-07-27) had no same-day `f1`/`f6` replay at all. No code or hook file modified — config-repo change, out of scope for this loop regardless. No vault content modified beyond the source marker. | Claude (pre-staging loop) |
