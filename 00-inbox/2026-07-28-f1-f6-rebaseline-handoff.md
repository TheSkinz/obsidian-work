---
type: note
status: open
created: 2026-07-28
tags: [regression, estimating, handoff, open-item]
---

# F1 / F6 re-baseline handoff

Deliberately not attempted 2026-07-28 — it is a merits review of a 14-section proposal
against three un-replayed rule changes, which needed a fresh session rather than the tail
of a long one. Full detail in `~/.claude/regression/runs/claude-opus-5/f1-firewater-ruleswrite-2026-07-28.md`.

**F1's frozen output is stale.** It sits at config commit `c973ed4`; three substantive
`usadebusk-estimating` commits have landed since, none replayed against it:

- `7eeb891` (2026-07-25) — land the total on a whole shift (Jesse's ruling)
- `e5a2031` (2026-07-28) — customer-supplied bid form handling
- `589fb1e` (2026-07-28) — firewater framing fix

The verification run produced $62,192 / 48 project hours against the baseline's $61,085 / 46.
The 48 is `7eeb891` firing correctly (44 raw, landed up to the shift boundary), so the drift
is the baseline being behind, not a model regression.

**F6 is behind too.** It also maps to estimating, and `7eeb891` is squarely a duration rule.

## What the next session has to do

1. Replay F1 against HEAD, judge on the merits, per the README sequence — replay, judge,
   patch, re-run, re-cut from the passing run. Then the same for F6.
2. **Confirm an unverified fix landed.** The 589fb1e firewater rewrite over-corrected: it
   removed the flag framing *and* dropped the "1½" does not provide sufficient volume"
   rejection clause that diff key 10 requires. Patched same-day (commit `0f058dd`) by
   stating what the Section 8 line contains rather than how briefly to write it — but that
   patch has never been replayed.
3. **Ruling needed from Jesse — the parallel-friction allowance.** Currently unsourced. The
   baseline used 25%, the verification run chose 15% and argued it from HF-0012. Worth
   roughly $1,100 on this fixture. Decide 15%, 25%, or a stated range, and whether it
   becomes a written rule or stays judgment.
4. Update diff key 10's wording in F1's frozen frontmatter — it still says "per the
   firewater trigger", naming a rule that no longer exists under that name.

## Why this keeps happening

Two of three fixtures checked today had stale baselines, both the same way: a rule shipped,
some fixtures got replayed, one didn't. `hooks/usadebusk-fixture-replay-guard.mjs` (built
2026-07-28) catches the case where *nothing* was replayed. It cannot catch F1's case, where
a replay happened but the rule landed afterward. See [[2026-07-28-replay-ordering-discipline]].
