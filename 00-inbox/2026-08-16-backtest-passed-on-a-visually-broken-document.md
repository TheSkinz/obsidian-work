---
type: idea-seed
status: researched
created: 2026-08-16
related:
  - "[[2026-08-19-idea-research-backtest-visually-broken-document]]"
tags: [idea, back-test, validation, generator, cross-cutting, future]
---

# A back-test that only checks numbers reports PASS on a visually broken document

Idea seed captured 2026-08-16 for a future exploration session. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** the job-report generator's README claimed it "reproduces the shipped USA26038
report exactly," and its back-test agreed. Measuring the output against the shipped PDF on
2026-08-16 found it had **never drawn a single table border** (Word's default table style draws
none and the renderer never wrote `w:tblBorders`) and **never drawn the gold rules bracketing the
KPI band**. Both defects shipped in every report the generator produced, through a back-test that
reported PASS, because the back-test only ever compared extracted numbers. The generator was
right about 207 operating hours and wrong about what the page looked like, and only the numbers
were being asked. This connects to [[feedback-backtest-before-build]] — that rule says reconcile
a spec's model against real artifacts to exact match, and the gap here is *what counts as the
match surface*.

**To explore:** what is the cheapest visual assertion that would have caught this? The detection
that actually worked was mechanical and reusable — rasterize page 1 with `pdftoppm`, scan for
full-width horizontal features, and compare their count, colour and vertical positions against the
shipped reference. That is a handful of lines and no image-diffing library. Should it become a
standing part of the generator's back-test, and does the same "assert the artifact, not just the
arithmetic" idea apply to the other document generators (the workup-to-proposal transfer step)?
Also worth deciding: how much visual drift is acceptable before a back-test should fail, given
LibreOffice and Word rasterize slightly differently.

**Gate:** None — researchable now.
