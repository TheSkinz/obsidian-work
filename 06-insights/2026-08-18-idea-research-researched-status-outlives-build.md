---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-18
review_after: 2026-09-18
related:
  - "[[2026-08-15-idea-researched-status-outlives-the-build-it-gated]]"
  - "[[2026-07-05-idea-research-self-obsolescence-detection]]"
  - "[[2026-07-22-idea-research-pig-load-list-generator]]"
  - "[[vault-idea-loop-spec]]"
  - "[[vault-consolidation-loop-spec]]"
tags: [review, knowledge-system, idea-research, loops, status, lint]
---

# Idea Research — `status: researched` Outlives the Build It Was Gating

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-18. Oldest unexplored seed:
`2026-08-15-idea-researched-status-outlives-the-build-it-gated.md`. Three seeds share a `created:`
date of 2026-08-15; the 2026-08-17 run already resolved that tie by git first-commit time and
recorded the order (frozen-baselines 18:45:27, this seed 20:03:51, smart-pig 22:34:39). The
frozen-baselines seed was researched on the 17th, so this one is next by the same ordering.

**Gate check.** The seed's `**Gate:**` line reads "None — researchable now." Nothing to settle;
proceeded directly to research. The only other unexplored seed of the same date
(`idea-smart-pig-report-as-cleaning-verification`) states a live gate — a second vendor report — and
was not touched, since gate-settling is only owed on the seed a run actually picks.

## Evidence

**1. This vault already shipped the answer to this exact question once, from a sibling seed.**
`archive/idea-self-obsolescence-detection.md` (created 2026-06-30, now `status: complete`) asked
"what signals obsolescence," and its disposition records what landed: the `REVIEW-OVERDUE` and
`SUPERSEDED` lint rules in `tools/vault_lint.py`, with the semantic reversal-detector parked. The
`SUPERSEDED` rule's own docstring describes its design choice in one line — it is "a cheap
structural check standing in for a hard semantic problem," and it fires on a *human-set declaration*
(`superseded_by:`) rather than trying to infer whether a note was actually replaced
(`tools/vault_lint.py:506`). That is the same problem shape as this seed, already solved once, and
the precedent says: do not detect the build, detect the declaration.

**2. The seed's first proposal — a disk check for the artifact each seed names — does not
generalize to the current population.** I read all five seeds now sitting at `status: researched`
and asked what a "does the thing this describes now exist?" pass would see:

| Seed | Names a path? | What a path-exists check sees |
|---|---|---|
| `idea-rollup-per-rig-coilset-grain` | `tools/estimating_rollup.py`, `04-knowledge/estimating-actuals-rollup.md` | present since before the seed — both are the *subject*, not the deliverable |
| `idea-job-sheet-third-instance-no-migration` | `04-knowledge/_canonical-job-sheet.md` | present since before the seed |
| `2026-08-15-idea-frozen-baselines-...` | none | nothing to check |
| `2026-08-15-idea-rollup-rig-in-column-is-mixed-method` | `tools/estimating_rollup.py` | present since before the seed; deliverable is a change *inside* it |
| `idea-job-report-generator-layout-gaps` | none (a table shape inside an existing renderer) | nothing to check |

Zero of five name a new artifact whose appearance would flip the status. Every live deliverable is
an edit inside a file that already exists, which is precisely the case a path-existence check is
blind to. The three seeds the retirement sweep caught *did* name new artifacts — a lint rule code,
a new concept note, two new scripts — so the check fits the retrospective sample and is silent on
the live one. That is the classic shape of a detector validated only on the cases that motivated it.

**3. Even on the historical sample the check would have scored 2 of 3, not 3 of 3.** The
job-report generator's artifacts are not in the vault: `extract_ticket_breakdown.py` and
`render_job_report.py` live at `~/.claude/skills/usadebusk-fieldpm/scripts/`. A vault-local disk
check cannot see them, and the idea-research loop is barred from reading skills as a write target
anyway.

**4. The inverse direction the seed flagged is real, and one instance is sitting in the vault
right now.** `archive/idea-pig-load-list-generator.md` carries `status: complete`. Its own closing
text is honest about what happened: the shared rollup script shipped as `tools/pig_usage_rollup.py`,
and "the pig *load list* generator itself — per-project 1/8" load lists for the field — was not
built and is not closed by this." So a seed rests at a terminal status with its titular deliverable
unbuilt; agent memory independently records the load list as not yet built. Two things make this
direction worse than the one the seed was written about: the note is in `archive/`, which is in
`SKIP_SCAN` (`tools/vault_lint.py:110`), so no lint rule can ever reach it — and it got there via
the Terminal-Note Sweep, which is doing exactly what it is supposed to. The researched-but-built
failure at least stays visible in `00-inbox/`; this one is filed away and structurally unmonitored.

**5. "Whoever lands the build flips the seed" is not a convention here — it is a precedent of
one.** Across all fifteen archived idea-seeds, exactly one
(`idea-self-obsolescence-detection`) carries a Disposition blockquote recording what was and was
not built. All fifteen do carry a terminal status, so seeds *do* get closed eventually — but two
carry values outside `ALLOWED_STATUS` (`executed`, `spec-complete`), which nothing flags because
`archive/` is skipped. The closing act is happening; the recording of *what* closed is not.

**6. External prior art splits into three families, and the popular one is the wrong instrument.**

- **Time-based staleness automation** — GitHub's stale-issue action, Jira's
  [close-after-X-days-in-status rule](https://support.atlassian.com/automation/kb/automatically-close-issues-that-have-been-in-the-same-status-for-x-days/),
  Zendesk's [stale-ticket automations](https://www.eesel.ai/blog/zendesk-automation-close-stale-tickets) —
  all close on *inactivity*. That is the wrong signal here. The three seeds the sweep caught were
  not inactive; they were finished. An inactivity rule would have closed them for the wrong reason
  and would equally have closed the ones still genuinely awaiting a ruling, which is the outcome
  the Terminal-Note Sweep's allowlist was written to prevent.
- **Path-existence linting** — [`agents-lint`](https://github.com/giacomo/agents-lint) checks
  whether paths referenced in `AGENTS.md`/`CLAUDE.md` still resolve and reports "path does not
  exist." The vault already runs this shape as `POINTER-DEAD` (`tools/vault_lint.py:897`),
  deliberately narrowed to `02-facilities` and rated a warning. The seed's disk check is its mirror
  image, and evidence 2 says the mirror has nothing to reflect on the current population.
- **Provenance-anchored drift** — [Fiberplane's Drift](https://fiberplane.com/blog/drift-documentation-linter/)
  binds a documentation claim to a code symbol at a specific commit and asks whether the bound code
  has changed since. This is the family that would actually work here, because it detects edits
  inside existing files — where five of five live deliverables sit. The cost is that every seed
  would have to declare its anchor, which is a new authoring burden on the seed template.
- **Transition-as-byproduct** — the cheapest and best-proven mechanism. GitHub
  [auto-closes a linked issue](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests)
  when a PR or commit containing `Fixes #123` merges to the default branch; `adr-tools` makes the
  same move with [`adr new -s N`](https://github.com/npryce/adr-tools), which writes the new record
  *and* rewrites the old one's status in a single command, specifically to prevent ADR status rot.
  Neither asks anyone to remember a second step — the state transition rides along with an action
  the author is already taking. All three of this vault's failures were landed by sessions that had
  the seed open, so a keyword in the commit message is the one place the reminder would have been
  in the right hands at the right moment. The hook point exists: `check_diff_rules` already inspects
  staged diffs (`tools/vault_lint.py:826`).

## Interpretation

**Sound problem, wrong proposed instrument — and the seed's own last bullet turned out to be the
bigger finding.**

The problem is real and recurs: three instances in two months, plus the fourth I found in the
inverse direction. But the seed's leading proposal, a pass over `researched` seeds asking "does the
thing this describes now exist," is a retrospective fit. It scores 0/5 on the population it would
run against today and 2/3 on the sample that motivated it, because the vault has moved from "seeds
that ask for a new script" to "seeds that ask for a change inside an existing one." Building it
would produce a check that stays quiet and reads as reassurance.

The seed's third bullet — flip it at the other end — is right about the mechanism and wrong that it
"needs no machinery." Evidence 5 shows the unaided version is already the status quo and already
fails; evidence 6 shows the fix everyone else converged on is not asking harder, it is making the
transition a byproduct of the landing commit. That is a real design, but it is bigger than the
observed 3-in-2-months rate justifies right now.

What the rate does justify is naming the periodic reconciliation as somebody's job. The honest
baseline the seed states — "a periodic sweep already works" — is correct; the 2026-08-15 sweep found
all three. It found them *by accident*, on an ad-hoc pass commissioned for something else. The
consolidation loop runs monthly on the 15th, already reads across the whole vault, and its cadence
matches the observed 17–26 day exposure. Making this a named pass there costs a spec edit and no
code. The idea-research loop structurally cannot own it — it touches only the seed it is currently
researching, by its own scope rule.

On the seed's fourth bullet: `researched` is overloaded, but adding a fourth status only helps if
something sets it, which is the same dependency that failed. Do not extend the vocabulary. Two
archived seeds are already carrying invented statuses nothing validates.

The finding I would rank first is not in the seed's proposal list at all. It is the inverse case in
evidence 4: a seed at a terminal status, archived, with its named deliverable never built, in a
folder no lint rule scans. That is one confirmed instance and I did not sweep for others.

## Recommended Action

**Bounded one-shot investigation, plus one rejection and one present-tense correction.** In order:

1. **Reject the disk check as the seed scopes it.** 0/5 on the live population. If it is built at
   all, it should be built the Drift way — a declared anchor per seed — not a bare path-exists pass,
   and not before item 2 has run twice.
2. **Add "reconcile seed status against what actually landed" as a named pass in the consolidation
   loop spec** (monthly, 15th, already vault-wide). Two directions, not one: `researched` seeds
   whose work has landed, *and* archived terminal seeds whose work has not. The second direction
   must read `archive/` explicitly, since `SKIP_SCAN` hides it from every lint rule. Spec edit only,
   no code.
3. **Park the commit-keyword mechanism** (`closes [[idea-slug]]` in a vault commit message, checked
   by `check_diff_rules`) until the consolidation pass has run twice and demonstrably missed
   something. It is the design with the strongest external precedent and it is still machinery for
   a rate a monthly sweep covers.
4. **Correct `archive/idea-pig-load-list-generator.md` now, separately from all of the above** —
   `status: complete` contradicts the note's own closing paragraph. This is a present error, not a
   design question, and it needs a status ruling from Jesse rather than a loop; this loop is barred
   from editing it. Two out-of-vocabulary statuses in `archive/` (`executed`, `spec-complete`) are
   worth the same one-line pass.

## Decision

- [x] Approve as scoped — reject 1, spec-edit 2, park 3, correct 4
- [ ] Approve item 2 only (name the pass), defer the rest
- [ ] Build the disk check anyway
- [ ] Park the whole thing — the ad-hoc sweep is good enough
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
