---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-21
review_after: 2026-08-21
related:
  - [[idea-portfolio-revival-pass]]
  - [[vault-idea-loop-spec]]
tags: [review, knowledge-system, idea-research, project-hygiene, leverage-repo]
---

# Idea Research — One-Shot Portfolio Revival Pass

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Four idea-seeds were `unexplored` in `00-inbox/`: this one, `idea-pig-load-list-generator`, `idea-workup-to-proposal-generator` (all `created: 2026-07-19`), and `idea-lint-lock-heater-schema` (`created: 2026-07-20`). The three 2026-07-19 seeds tie on frontmatter date; last night's run (`2026-07-20-idea-research-hardened-extraction-corpus-vision-arm.md`) resolved the tie against a same-commit sibling by first-commit timestamp, so this run applied the same rule: `git log --follow` on each candidate shows first-commit times of 19:30:24 (this seed, commit `557fbd3`), 21:22:20 (pig-load-list, `2aeb7b9`), and 22:29:56 (workup-to-proposal, `a18ad92`). This seed is oldest by that measure.

## Evidence

**Internal — the seed's own inventory is already partially stale, which is the strongest evidence for its premise.** Checked all five items the seed names as "started-and-parked work":

1. **Shift-Delta job-cost tracker** — confirmed genuinely parked, not stale. The plan file `~/.claude/plans/the-daily-email-only-cached-cupcake.md` exists and matches memory (`project-shift-delta-tracker`): spec-clean, back-tested against 3 real jobs (2026-07-09), unbuilt.
2. **`leverage` repo's five queued build packets** — **all five are already built**, and the queue folder doesn't know it. `packets/queued/` still lists `build-atp-validator.yaml`, `build-extraction-gate.yaml`, `build-gate-runner.yaml`, `build-decision-scripts.yaml`, `build-thesis-experiment.yaml`. Direct filesystem check: `gates/exec/atp-valid/` exists (atp-validator, built), `gates/exec/extraction-v1/` exists (extraction-gate, built), `gates/runner.py` exists (gate-runner, built), `decisions/intake.py` + `decisions/resolve.py` exist with passing test files (decision-scripts, built), `experiments/thesis/run.py` + full item/reference corpus exist (thesis-experiment, built — and per `project-leverage-repo` memory, it ran on 2026-07-06). `packets/done/` is empty — the convention to move a completed packet there was apparently never followed, so the queue silently drifted 100% stale with no signal.
3. **Knowledge Loop OS sessions C, D, F** — no independent vault artifact found for these; the only record is `project-knowledge-loop-os` memory (13 days old, self-flagged as point-in-time, not verified this run). Genuinely open per that source, but unconfirmed against current state — exactly the kind of claim the seed's own pass would need to re-verify rather than trust.
4. **Three vault git stashes from Fable-branch experiments** — **gone.** `git stash list` returns empty in both the vault repo and the `leverage` repo. Memory (`project-knowledge-loop-os`) still lists them as "awaiting Jesse's review before dropping" as of 2026-07-07. Either they were already resolved and the memory was never updated, or they were dropped without the review the note says was pending — either way, another instance of the tracked-list-vs-reality gap this idea is designed to catch.
5. **"Stalled" thesis experiment** — ran to completion 2026-07-06 (`experiments/thesis/run.py`, full 30-item corpus with references, per `project-leverage-repo` memory and last night's review note). "Stalled" is accurate only in the narrower sense that no decision was ever recorded on what the (inconclusive) result means for the infrastructure bet — the run itself isn't pending.

Net: of five inventoried items, two (leverage packet queue, vault stashes) have already drifted from their last-known state within the 2-16 day window since they were last touched, without anyone noticing. This directly confirms the seed's own worry in "To explore" — "anything written down today is stale the moment a packet gets built or killed" — as an observed fact, not a hypothetical.

**Internal — the 90-day `leverage` prune rule (cited in the seed) does not yet apply.** `tasks/PROMOTION.md`: "a task with no runs in 90 days is a prune candidate." Last commit `d9bf723`, 2026-07-02 — 19 days dormant as of this run, well short of the threshold (~2026-09-30, same checkpoint last night's review note flagged for the sibling extraction-corpus idea).

**Internal — the decision-queue has headroom to absorb this as line items rather than a standalone note.** `50-dashboards/decision-queue.md`: 0 open rows as of 2026-07-20, cap is 10. The seed's own "To explore" question — whether output belongs in the queue as individual rows instead of a standalone note — is answerable now: capacity exists either way.

**External — practitioner consensus across two unrelated disciplines converges on exactly the seed's own caution.** GTD's Someday/Maybe-list literature: the list itself isn't the failure mode, *skipping the periodic review* is — "those who abandon GTD typically don't fail at capturing or organizing, they stop reviewing... without regular review, your project list becomes a graveyard of good intentions" (facilethings.com, super-productivity.com). Agile backlog-grooming literature independently lands on the same split the seed proposes: treating refinement as a one-time event is a named antipattern, but a bounded *quarterly cleanup pass* run alongside (not instead of) any ongoing discipline is explicitly endorsed practice ("a quarterly backlog cleanup can archive items untouched for 6+ months... meant to complement, not replace, ongoing grooming" — hellopm.co, developerexperience.io). Both traditions reject "no review ever" and "build a standing engine" as the two failure extremes, and land in the same middle the seed already proposes: bounded, recurring-but-cheap, human-adjudicated.

## Interpretation

**Sound, and the research surfaced evidence the seed didn't have yet: the drift is already happening, not hypothetical.** The seed correctly identifies that a written list goes stale fast; checking it this run found two of five items already out of sync with reality since last touched (14-16 days for the stashes, 2-19 days for the leverage queue). That raises the cost of *not* doing the pass soon, but doesn't argue for an engine — the external research is unambiguous that a bounded, infrequent, human-checked pass is the correct middle ground between "never review" and "build a standing recovery system," which is exactly what the seed already proposed and explicitly warned against over-building.

One correction to the seed's own framing: the "stalled thesis experiment" already ran (2026-07-06); what's actually stalled is the decision about what its inconclusive result means, not the experiment itself. And the leverage-repo item has a cheaper fix available right now than a full portfolio pass would deliver: moving the five already-built packets from `packets/queued/` into `packets/done/` (or deleting the stale queue entries) fixes the single most concrete piece of drift found this run, independent of whether the broader one-hour pass ever happens.

## Recommended Action

**Bounded one-shot investigation, as the seed itself specifies** — run the ~1-hour pass over memory, `INDEX.md`, and the repos, producing a ranked revive/complete/kill list. Two refinements based on this run's findings: (1) do the cheap mechanical fix first and separately — reconcile `leverage/packets/queued/` against what's actually built (move or delete the five stale entries) and resolve or drop the three vault stashes — since both are now confirmed-stale and don't need the full pass to act on; (2) route the pass's output as individual decision-queue rows rather than a standalone note, since the queue has full headroom (0/10) and a standalone output note is itself exactly the kind of parked artifact the seed warns about creating.

## Decision

- [ ] Build now — run the full portfolio pass immediately
- [ ] Approved with edits — do the cheap leverage/stash cleanup now, defer the full pass
- [ ] Park — revisit at a later checkpoint
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
