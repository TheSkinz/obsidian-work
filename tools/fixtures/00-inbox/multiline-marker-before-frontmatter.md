<!-- vault-loop: operational — fixture for the multi-line leading-comment parse. -->
<!-- vault-prestaged: RESOLVED 2026-09-08 — this block is deliberately several lines long.
     The pre-staging loop wrote markers in exactly this shape, and the 2026-07-29
     frontmatter_start() fix only skipped comments that opened and closed on a single
     line, so everything below was invisible to every frontmatter rule. -->
---
type: note
status: not-a-real-status
created: 2026-09-08
tags: [fixture]
---

# Multi-line marker before frontmatter

Fixture for `frontmatter_start()`. A **multi-line** `<!-- vault-prestaged: -->` block
above the fence used to make this note's entire frontmatter invisible, so the bogus
`status:` above went unreported. STATUS-VOCAB firing here is the regression test.

The live instance was `00-inbox/2026-07-24-parallel-friction-factor-deferred.md`, which
carried `status: resolved` under a nine-line block and was reported STATUS-MISSING. The
false warning was the lesser half: the Terminal-Note Sweep keys on status through this
same parser and must skip what it cannot read, so the note could never be swept.

Companion to `marker-before-frontmatter.md`, which covers the single-line case. Keep both
— they fail differently, and the single-line fixture passed throughout the period this one
was broken.
