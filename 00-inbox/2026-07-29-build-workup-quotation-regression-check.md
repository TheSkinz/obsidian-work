---
type: note
created: 2026-07-29
tags: [inbox, estimating, tooling, build-task]
---

# Build — post-script-edit quotation-vs-workup regression check

Approved with edits by Jesse 2026-07-29. Decision and full scope:
[[2026-07-27-idea-research-quotation-workup-reconciliation-check]].

Extend `~/.claude/skills/usadebusk-estimating/scripts/backtest_workup.py`, or add a thin sibling
sharing `extract_workup.extract()`, so the quotation-vs-workup diff runs after any edit to
`usadebusk-estimating/scripts/*`. Mirrors the `~/.claude/regression/` fallback-battery pattern —
event-triggered on change, never scheduled.

Implementation constraints from the research:

- Read the quotation's tables via `python-docx` directly wherever a `.docx` source exists.
  `render_proposal.py` emits native `doc.add_table(...)` tables, so the cells are readable from
  the zip/XML with no render step. Reserve PDF text extraction for docx-less legacy submissions.
  Do not reintroduce the LibreOffice `soffice --convert-to` step — it needs a per-file wait and
  silently drops files on back-to-back calls.
- Reuse the mob/demob lump-sum exclusion (`_is_lump_sum_gap()`) and the multi-block-per-page
  summation logic already in `extract_workup.py`. Do not re-derive them.
- Known-good pairs to assert against, all reproduced exactly by the existing back-test:
  DSP26071.2 $60,287.42 · DSP26085 $40,477.08 · DSP26068.1 $112,642.23.

Out of scope for this build: the pre-send bid-submission gate stays manual until the
DSP26026-style scope-narrowing rule exists. Carried as the review note's `revisit-trigger`.

This is a config-repo change (`~/.claude`), not a vault change.
