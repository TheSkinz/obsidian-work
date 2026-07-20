---
type: idea-seed
status: executed
created: 2026-07-19
executed: 2026-07-19 — built as Stage 1 of the Fable-5 close-out session; suite at ~/.claude/regression/ (config repo 7d5eebd), 6 fixtures + frozen Fable-5 outputs + replay README. One-shot, no recurring loop created; the open questions in "To explore" (recurring vs on-switch, reference retirement) are answered in the README and item (d) of [[2026-07-19-fable5-closeout-handoff]].
tags: [idea, vault-system, future, skills, evaluation]
---

# Fallback-model regression battery as a recurring check

Idea seed captured 2026-07-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The nine skills were authored and exercised almost entirely under frontier models, and nothing in the system tests whether they still work when a weaker model runs them — the skill-drift loop checks skills against vault truth, never against model capability. A set of end-to-end fixtures (fixture RFQ to full proposal, ingest dry run, fieldpm extract, SOP formatting) with frozen reference outputs makes that measurable: replay a fixture on Opus, Sonnet, or Haiku, diff against the reference, and see exactly where the fallback stack degrades. Practitioner evidence suggests skills only help where the weaker model actually fails, so knowing *where* it fails is what makes any later skill hardening worth doing instead of guesswork.

**To explore:** Whether this should ever become recurring or stay a one-shot — a monthly diff run is a sixth loop for an operator whose sixth loop (the leverage metabolism layer) already starved, so the honest options may be "fold a diff check into the existing monthly skill-drift run" or "run it only when switching default models." What the diff criterion should be, since prose outputs won't match verbatim and a structural check (section presence, required fields, format conformance) is probably the only durable comparison. Whether frozen references go stale as skills legitimately change, and how a reference gets retired without silently hiding a regression. Whether the fixtures should live in the config repo alongside the skills or vault-side.
