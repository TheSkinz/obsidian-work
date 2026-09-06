---
title: RULE-FORK fixture — the agreeing half
created: 2026-09-06
tags: [fixture]
---

# RULE-FORK fixture (a)

Deliberately broken pair. This file and `process-flow.md` beside it both state the
**max pig OD** rule, and they disagree — which is the whole point.

This half carries the real, correct figure:

- Final pig size — the largest pig OD that actually passed the full circuit without
  obstruction. Maximum pig size = Clean ID + 0.250".

The other half says 0.500". A rule stated in two places that no longer agrees is the
defect RULE-FORK exists to catch — see the 2026-09-05 rig-in drift in the
`vault_lint.py` header, where `01-context/` and the config-repo skill described two
different models for 24 hours and nothing reported it.

This pair uses only vault-relative registry paths on purpose, so the fixture does not
depend on the claude-config repo being present on the machine running the self-test.
