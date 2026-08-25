---
type: idea-seed
status: unexplored
created: 2026-08-24
tags: [idea, vault-system, drift, future]
---

# Detect retirements that never propagated

Idea seed captured 2026-08-24 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The same failure shape produced three separate defects found on 2026-08-24, so it looks structural rather than coincidental. In each case a thing was retired, the retirement was recorded in exactly one file `CLAUDE.md` excludes from session auto-load, and every surface a session actually reads kept asserting the old fact in the present tense. Gemini retired 2026-07-07 — recorded parenthetically in `01-context/workflow-map.md`, while **six** files in `07-llms/` still called its Gem the current production standard for drawing extraction. Three loops stopped 2026-08-21 — recorded in `01-context/system-workflow-reference.md`, while all three specs still read `status: active` as `type: governance`. And the `06-insights/` folder name outlived the `insights-log.md` it was named for by seven weeks.

Lint could not have caught any of them: `gem-drawing-extraction.md` carried **no `status:` field at all**, so STATUS-VOCAB had nothing to check.

**To explore:** Whether "retired somewhere, asserted live elsewhere" is mechanically detectable at all, or whether this is really a *discipline* fix — a close-out step that greps for a thing's name across the content layers whenever something is retired — rather than a tool. If mechanical: what the signal is. Candidate tells seen in all three cases are present-tense superlatives ("current", "validated", "the standard", "primary tool") and two files claiming the same role with nothing adjudicating, but both look noisy. Cheaper adjacent option: require a `status:` field on `07-llms/` notes so the existing vocabulary check can at least see them.

**Gate:** Delete if researchable now — nothing blocks it.
