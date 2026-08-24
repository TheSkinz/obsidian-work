---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-31
review_after: 2026-08-31
related:
  - "[[2026-07-28-replay-ordering-discipline]]"
  - "[[idea-baseline-staleness-detector]]"
  - "[[2026-07-28-f1-f6-rebaseline-handoff]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, regression, hooks]
---

# Idea Research — Replay-Ordering Discipline Instead of a Smarter Detector

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-07-31. Two `unexplored` idea-seeds
tied on `created: 2026-07-28`: `2026-07-28-replay-ordering-discipline` and
`idea-baseline-staleness-detector`. The vault's own commit history broke the tie — the former
was added at 17:08 local, the latter at 21:53 (`git log --diff-filter=A`) — so the former is
older and was processed.

**Gate check.** This seed's `**Gate:**` line reads: "Do not spend a research cycle until F1 and
F6 have actually been re-baselined ... that exercise is the natural place to find out whether
the convention survives contact with an expensive fixture." `archive/2026-07-28-f1-f6-rebaseline-handoff.md`
is marked `> **RESOLVED 2026-07-28.** Both fixtures replayed against HEAD, judged, the skill
patched on two rulings from Jesse, and both re-run clean. Config commits `ccf20ad` (replay +
judgment) and `71efec5` (rulings + patch + re-runs).` Both commits were confirmed present in
`~/.claude`'s git log. The handoff note flags one thing still open — "promotion... Neither
frozen file has been re-cut" — but that is a distinct downstream decision reserved for Jesse,
not part of the replay/judge/patch/re-run cycle the gate exists to observe. Treated as case (b):
gate met, proceed to research.

## Evidence

**1. The rebaseline exercise itself already answers the seed's central question, and the
answer is "no, not naturally."** The seed's core worry is whether "replay last, then commit the
run and the rule together in one commit" is followable when a replay fails and forces a patch,
which then needs another replay. The actual F1/F6 exercise hit exactly that shape — a friction-
allowance ruling was needed from Jesse mid-exercise, plus a patch to an over-corrected firewater
rewrite — and it resolved as **two separate commits**, not one: `ccf20ad` for the replay and
judgment, `71efec5` for the ruling, patch, and re-runs. A single careful executor working the
exact case the convention is meant to cover did not co-commit. That is a data point against the
convention's practicality, not for it.

**2. The sibling seed already proposes the "lighter version" this seed's own fourth
To-explore question asks about.** This seed asks: "Whether a lighter version — recording the
config commit hash in the run file's frontmatter, so staleness is checkable by comparison
rather than by date — gets most of the benefit for none of the workflow change." That is,
almost verbatim, the design of `idea-baseline-staleness-detector` (same inbox, same creation
date, gate: none): "for each frozen file, parse its `skills:` line for the config commit it was
cut at, run `git log <commit>..HEAD -- skills/<skill>/SKILL.md`, and report any fixture with
un-replayed commits behind it." The two seeds converge on the same mechanism from opposite
directions.

**3. External prior art confirms the mechanical approach is not just lighter, it is
ordering-immune by construction, which directly dissolves this seed's motivating failure
mode.** Researched a content-hash/commit-based staleness pattern used for an analogous problem
(prompt-drift detection in LLM pipelines): a baseline records a content fingerprint (or, by the
same logic, a commit reference) rather than a date, and staleness is re-derived by comparison at
check time — "line numbers and git SHAs are display-only, never matching inputs," precisely to
avoid the failure mode where two events on the same calendar day land in the wrong order. That
is exactly this vault's F5 incident: replayed at 13:33, rule landed at 19:56, same day, and
`hooks/usadebusk-fixture-replay-guard.mjs`'s own header names this as its documented "KNOWN
LIMITATION" — "Date granularity cannot see ordering." A commit-range check
(`git log <baseline-commit>..HEAD -- <path>`) is not a same-day/different-day question at all;
it is "did anything land after the commit the frozen file cites," which is immune to
intra-day ordering by construction — no workflow discipline required to make it correct.
[Prompt-drift staleness guide](https://docs.multivon.ai/guides/staleness)

**4. Weaker analog considered and set aside.** Kent Beck's TCR ("test && commit || revert")
is the closest known discipline-based pattern for keeping commits synchronized with
verification state, but its own literature frames it as workable mainly for fast, cheap test
suites — the discipline breaks down as verification cost rises. This seed's own text notes an F1
replay costs roughly 67k subagent tokens, which is the expensive-fixture case, not the cheap
one TCR is built for. This reinforces point 1 rather than adding new information.
[Test && Commit || Revert overview](https://www.honeybadger.io/blog/ruby-tcr-test-commit-revert/)

**5. Minor correction to the seed's own hypothesis about the CO-COMMIT gate's 100% fire
rate.** The seed guesses the CO-COMMIT variant's 100% historical fire rate is an artifact of the
convention never having been tried, and that adopting it "could collapse that rate." The
backtest script's own comment in `hooks/usadebusk-fixture-replay-guard.mjs` (lines 24–29) frames
this differently: "replays are routinely committed separately from the edit they validate, which
is normal workflow rather than a defect" — i.e., the 100% rate reflects a workflow choice already
in active, sound use elsewhere in this repo, not an unexercised convention. Point 1's evidence
(the F1/F6 exercise itself splitting into two commits) is a second, independent data point for
the same reading.

## Interpretation

**Trap — a discipline-based fix for a problem that already has a better-fit mechanical fix
sitting one seed over.** The convention this seed proposes (replay last, co-commit run and rule)
is a plausible-sounding fix, but the one real trial of the underlying exercise did not co-commit
even under careful manual execution, and a commit-range comparison (already the design of the
sibling `idea-baseline-staleness-detector` seed, and independently validated as established
practice for the identical class of problem elsewhere) closes the exact same-day-wrong-order gap
this repo's own tooling already names as its known limitation — without requiring anyone to
remember a workflow rule. Discipline-based approaches are also a documented poor fit once a
single verification step is expensive (point 4), which describes this repo's fixtures. This
seed's one piece of genuinely new content — the frontmatter config-commit field — is not new; it
is the same mechanism the sibling seed already proposes in more detail.

## Recommended Action

**Drop this seed as a standalone track.** Its live idea (record a config-commit reference,
check by comparison rather than date) should be pursued through `idea-baseline-staleness-detector`
instead, which already specifies the mechanism in more actionable detail (parse the `skills:`
line, `git log <commit>..HEAD`, surface on `50-dashboards/health.md`) and carries no gate. When
that seed is researched or built, this note's point 1 (real-world evidence that co-commit did
not happen naturally) is worth citing as a reason not to also pursue a discipline-based
convention alongside the mechanical fix — one is sufficient, and the mechanical one does not
depend on anyone remembering anything.

## Decision

- [ ] ~~Approved — pursue the replay-last / co-commit workflow convention~~
- [ ] ~~Approved with edits~~
- [x] **Drop — fold into `idea-baseline-staleness-detector` instead** (Jesse, 2026-08-01)
- [ ] ~~Needs more source material~~

Ruled together with [[2026-08-01-idea-research-baseline-staleness-detector]], which was approved
in its ordered three-step form in the same pass. Deciding them separately would have risked
approving both halves of one thing — the convention and the mechanical check close the same gap.

The deciding evidence is this note's own point 1: the F1/F6 rebaseline was the exact case the
convention exists to cover, and under careful manual execution it still split into two commits
(`ccf20ad`, `71efec5`). A convention that did not survive its first real trial is not worth
adopting alongside a mechanical check that needs no one to remember anything.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-01 | Dropped as a standalone track; `status` → `resolved` | Claude | Live idea (record a config-commit reference, check by comparison not date) carried forward into the approved baseline-staleness build. Point 1 is cited there as the reason not to also pursue a discipline-based convention alongside it. Source seed `00-inbox/2026-07-28-replay-ordering-discipline.md` closed. |
