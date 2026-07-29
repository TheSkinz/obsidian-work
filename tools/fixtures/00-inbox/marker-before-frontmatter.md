<!-- vault-loop: operational — fixture for the leading-comment frontmatter parse. -->
---
type: note
status: not-a-real-status
created: 2026-07-29
tags: [fixture]
---

# Marker before frontmatter

Fixture for `frontmatter_start()`. A capture-loop marker on line 1 used to make
this note's entire frontmatter invisible to every frontmatter rule, so the bogus
`status:` above went unreported. STATUS-VOCAB firing here is the regression test.
