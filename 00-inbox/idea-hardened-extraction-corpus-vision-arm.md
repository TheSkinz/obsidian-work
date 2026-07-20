---
type: idea-seed
status: researched
created: 2026-07-19
related:
  - [[2026-07-20-idea-research-hardened-extraction-corpus-vision-arm]]
tags: [idea, vault-system, future, extraction, evaluation]
---

# Hardened extraction corpus + vision arm for the thesis experiment

Idea seed captured 2026-07-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The `leverage` repo's pre-registered experiment (cheap model + gate + retry vs frontier, on structured extraction) came back inconclusive on 2026-07-06 because the corpus was too easy — all three conditions hit 100%, so there was no headroom to measure whether the gate-and-retry loop adds anything. The design's own registered next step is a harder corpus, and it explicitly notes more items at the current difficulty won't help. Separately, the corpus is text-only while the actual extraction pain is vision: heater-drawing BOM tables, OCR-degraded GA drawings, conflicting tube counts. A harder corpus with a vision arm would turn "which extraction work can I safely hand to a cheap model" from a guess into a measured answer — and that question gets more valuable, not less, now that frontier access is metered.

**To explore:** Whether the experiment is worth reviving at all, given the repo has been dormant since 2026-07-02 and two of its layers never fired — reviving a stalled experiment may be the same trap as building a new meta-system. If it is worth reviving: what makes an extraction item genuinely hard rather than just fiddly (conflicting sources, absent required fields, distractor numbers, unit ambiguity); whether real drawing snippets can be used without leaking customer-identifying detail into a test corpus; what a vision arm costs in harness work, since `DESIGN.md` declares the corpus single-task-family text extraction and the backends embed source text in prompts, so images need a new item format and a pre-registration amendment; and whether the frontier condition can still be run economically at post-window API pricing, or whether any frontier baseline has to come from captures frozen during the access window.
