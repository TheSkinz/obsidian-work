---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-21
review_after: 2026-11-21
related:
  - "[[idea-generator-owns-marked-spans-not-layout]]"
  - "[[2026-08-17-triage-job-report-generator-layout-gaps]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, gated, fieldpm, job-report, generator]
---

# Idea Research — The Generator Owns Marked Spans (gated, not researched)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-21. Two unexplored idea-seeds share
the oldest `created:` date of 2026-08-17 —
[[idea-generator-owns-marked-spans-not-layout]] and
[[idea-stated-justifications-are-unmeasured-claims]]. This one carries an explicit `**Gate:**` line,
so per the loop spec's step-3 rule its gate was settled from files before any research. It is shut.
The run closed the gate here and moved to the next seed rather than spending the research cycle.

## The gate

The seed states it in two halves: *"the cheap write-guard landed first (see the triage note). This
only earns a design cycle if that guard proves insufficient — a second edit-loss, or a decision that
re-rendering delivered documents should be routine."* Both halves must fail for the seed to open.
Neither has.

## Evidence the gate is shut

**1. The write guard landed and is verified in the live renderer.** `render_job_report.py:577` reads
`if os.path.exists(out) and not force:` and exits rather than writing; `--force` is parsed out of
argv at line 566, the usage string at line 561 names it, and the module docstring at line 17 states
its intent — *"--force overrides, and is for replacing a file you have checked carries no hand
edits."* This is the exact three-line shape the triage's execute item 1 briefed, at the write site,
not a convention. [[2026-08-17-triage-job-report-generator-layout-gaps]] records it verified four
ways plus a live replay of the 2026-08-16 invocation against the delivered USA26041 docx, which
refused and left the file byte-identical (`ab8e30e0…`).

**2. No second edit-loss has occurred.** The 2026-08-16 clobber is the only one on record —
`change-log.md:178` carries it as the ⚠ process failure of the USA26041 build. No vault commit since
2026-08-17 touches a job report render, and no inbox note, review note or change-log row since
records a re-render over a hand-edited document. There has been no *first opportunity* for a second
loss: no job report has been compiled since the guard landed.

**3. No decision has been made that re-rendering delivered documents should be routine.** The
opposite is standing policy — USA26041's config is a text mirror only and carries a
DO-NOT-RE-RENDER banner naming the three structural hand edits the generator cannot reproduce
(inline images with no Images section, a merged Pigs Used table, a `Decoking Analysis:` lead-in).
The triage's own close-out line is explicit: the park *"stays gated behind a second edit-loss, which
the write guard now makes considerably less likely."*

## Interpretation

**Gated — not researched.** The gate is verifiably shut on all three of its conditions, from files
alone, and the seed's own reasoning for why it should stay shut still holds: the cheap fix makes
overwriting *impossible*, which is a strictly weaker but strictly cheaper answer than making
overwriting *safe*. Design work on the marker/splice mechanism only becomes worth its cost once
"impossible" is the wrong answer — i.e. once someone actually wants to re-render over a delivered
file. Nobody does yet.

Worth noting for whenever it does re-open: the seed's own "To explore" already contains the cheaper
alternative it should be tested against — a prose sidecar the renderer reads narrative bodies from,
which gets the same protection with no marker machinery and no python-docx bookmark round-trip risk.
That is the comparison the design cycle should start from, not the marker scheme on its own.

## Recommended Action

**Park.** No action needed. The seed flips to `status: gated` and keeps its existing
`revisit-trigger:`, which is already carried in the health dashboard's dormant-trigger registry
(`50-dashboards/health.md:53`) in the correct event form — checked at the step the condition names,
which is the next `/report` render over an existing file.

## Decision

- [ ] Approved — leave gated
- [ ] Un-gate and research now anyway
- [ ] Drop the seed
- [ ] Needs more source material

## Apply Log

| Date | Action | By |
|---|---|---|
|  |  |  |
