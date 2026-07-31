---
type: idea-seed
status: researched
created: 2026-07-28
related:
  - "[[2026-07-31-idea-research-replay-ordering-discipline]]"
tags: [idea, vault-system, regression, future]
---

# Replay-ordering discipline instead of a smarter detector

Idea seed captured 2026-07-28 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Two of three fixtures checked on 2026-07-28 had stale frozen baselines,
and both went stale the same way — a rule shipped, some fixtures got replayed, the one that
owned the rule didn't. The `usadebusk-fixture-replay-guard` hook built the same day catches
the case where nothing was replayed that day, but it structurally cannot catch the other
shape: F5's rule landed at 19:56 on 2026-07-25 after F5 had already been replayed at 13:33,
so a same-day check sees a replay and passes. The fix may be a workflow convention rather
than a better detector — replay last, then commit the run and the rule together in one
commit, so "was this replayed after the edit" becomes visible in the commit itself.

**To explore:** Whether the convention is actually followable in practice, given that a
replay can fail and force a skill patch, which then needs another replay — the loop has to
terminate somewhere and the last iteration is the one that must be co-committed. Whether
co-committing makes the CO-COMMIT gate variant viable after all; it measured a 100% fire
rate against history precisely *because* the convention wasn't being followed, so adopting
the convention could collapse that rate and make the sharper detector usable. What it costs
when a replay is expensive (F1 is a 14-section proposal, ~67k subagent tokens) and the edit
is small. Whether a lighter version — recording the config commit hash in the run file's
frontmatter, so staleness is checkable by comparison rather than by date — gets most of the
benefit for none of the workflow change.

**Gate:** Do not spend a research cycle until F1 and F6 have actually been re-baselined (see
[[2026-07-28-f1-f6-rebaseline-handoff]]) — that exercise is the natural place to find out
whether the convention survives contact with an expensive fixture, and doing it first gives
this idea real evidence instead of a hypothesis.
