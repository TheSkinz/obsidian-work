---
type: idea-seed
status: unexplored
created: 2026-08-20
tags: [idea, vault-system, future]
---

# Derive eval questions from real failures, not a priori

Idea seed captured 2026-08-20 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `04-knowledge/knowledge-system-evaluation-questions.md` holds ten questions written on 2026-06-26 and last run 2026-07-23, where they **passed**. Five days after that pass, the Syncrude 7-1F-1 card was still carrying a heater footage wrong by a factor of eight — the single most-used number on the card — and it stayed wrong for another month while three separate review passes reasoned downstream of it. So the eval passed a vault that was materially broken in exactly the area the eval covers. KS-002's own pass criterion is "does not infer heater facts from jobs alone," which is precisely the failure that occurred, and the question still did not surface it. That suggests the question set is testing whether the *rules* can be recited rather than whether the *data* is right, and that a question set designed a priori will keep missing the failures that actually happen.

**To explore:** Whether the eval should be regenerated from the vault's own correction history — every time a real error is found and fixed, a question is derived from it and added to the set, so the eval grows to cover the failure modes this vault demonstrably has rather than the ones someone imagined at the start. Open questions: does that make the set monotonically grow until it is too expensive to run, and what retires a question; whether a question derived from a fixed error is trivially passable afterwards (the fix is now in the vault, so retrieval succeeds — meaning the question tests nothing going forward unless it is phrased against the *class* rather than the instance); whether the set should be split into recite-the-rule questions and check-the-data questions, since only the second kind would have caught Syncrude; and whether "pass" should require citing the source note and verifying it still says what the answer claims, which is the adversarial grading rule already written into the 2026-08-20 audit brief.

Related: [[2026-08-20-vault-architecture-audit-evidence]], [[2026-08-20-syncrude-geometry-per-pass-misread]], [[2026-07-23-retrieval-eval-run]].
