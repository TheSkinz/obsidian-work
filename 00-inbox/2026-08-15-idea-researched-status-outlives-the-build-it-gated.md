---
type: idea-seed
status: researched
created: 2026-08-15
related:
  - "[[2026-08-18-idea-research-researched-status-outlives-build]]"
  - "[[2026-08-15-retirement-sweep-what-else-has-outlived-its-reason]]"
  - "[[idea-lint-lock-heater-schema]]"
  - "[[idea-job-report-generator]]"
  - "[[idea-business-normal-register]]"
tags: [idea, vault-system, knowledge-system, loops, status]
---

# `status: researched` survives the build it was gating, and nothing notices

**Gate:** None — researchable now.

The 2026-08-15 retirement sweep found **three seeds that had been built or landed but were still
filed `status: researched`**, and it found them by accident rather than by any check:

| Seed | Filed | Actually |
|---|---|---|
| [[idea-lint-lock-heater-schema]] | researched, 2026-07-20 | `DURATIONS-HEADER` live at `tools/vault_lint.py:496` with fixture T-200 |
| [[idea-business-normal-register]] | researched, 2026-07-29 | landed as `04-knowledge/concepts/business-normal-facts.md`, ruled 2026-08-15 |
| [[idea-job-report-generator]] | researched, 2026-07-21 | built the same day — `extract_ticket_breakdown.py` + `render_job_report.py` behind `/report` |

**Why this is structural rather than sloppiness.** `researched` is written by the Vault Idea
Research Loop and means precisely "the loop finished and Jesse has not decided." Nothing else in the
system ever revisits it. The Terminal-Note Sweep is *explicitly forbidden* from touching it — for a
good reason, since sweeping it would silently discard a pending decision — so once a seed is
`researched`, the only thing that can move it is a person remembering. A seed whose build then
lands has no path back out, and it sits indefinitely reading as an open ask.

The cost is not storage. It is that the inbox's pending-decision population is **wrong in the
direction that hides work**: a reader scanning for what still needs deciding sees three items that
need nothing, which is exactly the noise that buried the real items this sweep was commissioned to
find. The job-report generator sat that way for 25 days having been built on day one.

**Note the near-miss in the template.** `templates/_idea-seed-template.md` already warns that "a
gated seed with no `revisit-trigger:` is an idea you will lose" — the same failure shape, caught for
`gated` and not for `researched`. [[idea-llm-navigable-vault-map]] was the `researched` variant of
it, parked with no wake condition and invisible for three weeks.

## To explore

- **Is the cheap check a disk check?** Most of these seeds name their own artifact — a script path, a
  lint rule code, a destination note. A pass over `researched` seeds asking "does the thing this
  describes now exist?" would have caught all three in seconds. What fraction of seeds name a
  checkable artifact, and what does the check do about the ones that do not?
- **Whose job is it?** Candidates: the idea-research loop (but it only touches seeds it is
  researching), the consolidation loop (right cadence, already reads across the vault), the capture
  loop (already normalizes frontmatter, but Lane 1 and this is a status *ruling*), or a periodic
  sweep like this one. The honest baseline is that a periodic sweep already works — the question is
  whether three instances in two months justifies anything cheaper.
- **Or is the fix at the other end?** Whoever lands a build flips the seed. That is free, needs no
  machinery, and fails exactly the way this failed — it depends on remembering, and all three of
  these were landed by sessions that had the seed open.
- **Is `researched` doing too much work as a single value?** It currently conflates "researched, awaiting
  a ruling," "ruled and building," and "built, nobody updated this." A distinct status for the third
  case is additive schema (Lane 3) but it only helps if something sets it.
- **Check the inverse before designing anything:** are there seeds at a *terminal* status whose work
  never actually landed? That is the more dangerous direction and this sweep did not look for it.

Cross-cutting — it affects whether the inbox can be trusted as a list of what is actually open,
which every session's triage depends on.
