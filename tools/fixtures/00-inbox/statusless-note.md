---
type: note
created: 2026-09-07
tags: [fixture]
---

# A finished note with no status field

Fixture for `check_status_missing()` (STATUS-MISSING). The frontmatter above is
valid and parses cleanly — it simply has no `status:` key, which is the whole
defect. **Do not "fix" it by adding one; the absence is the fixture.**

A note in this state can never be swept out of `00-inbox/`, however finished it
is. The Terminal-Note Sweep keys on `status` and a parser that sees none must
skip rather than guess. That rule is correct and this fixture does not challenge
it — what it proves is that the resulting permanent invisibility is now detected
rather than discovered by accident, which is how the original four were found on
2026-07-29 after two of them had sat five weeks.

STATUS-VOCAB does not cover this: it fires on a status outside the vocabulary,
and an absent status is not a value.
