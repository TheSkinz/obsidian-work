---
title: Prompt Engineering
created: 2026-06-29
tags: [prompt-engineering, llm, patterns]
---

# Prompt Engineering

Principles and patterns for getting reliable, high-quality output from LLMs. This is a living document — add patterns as they're validated and anti-patterns as they're encountered.

## Key principles landed on

**Specify format upfront.** LLMs default to whatever format feels natural for the content type. If you need a table, a numbered list, prose paragraphs, or JSON — say so in the prompt. Post-hoc reformatting requests add a round trip and often don't fully converge.

**Name the failure mode you're preventing.** Telling a model what you don't want (e.g., "no bullet points in prose sections") is as important as telling it what you do want. Models optimize for helpfulness, which means common patterns get over-applied unless they're explicitly excluded.

**Provide the output exemplar when quality matters.** For recurring structured outputs (heater cards, proposals, SOPs), the fastest path to correct format is a real example from the vault. Abstract descriptions of structure are interpreted differently each time; a concrete example is unambiguous.

**One ambiguity → one clarifying question, upfront.** Don't start generating and then ask mid-output. If something is unclear, ask before starting. This is especially true for documents that have a fixed format — a wrong-format first draft wastes more time than a short question.

**LLMs cannot reliably audit their own output.** This is the confabulation finding from [[gem-drawing-extraction]] but it applies universally: asking a model to check its own work produces confident explanations of what it *should* have done, not accurate descriptions of what it *did* do. Human review or a separate model pass is the only reliable check.

## Pattern catalog

**Dependency-tree interview pattern** (analyzed via the `grilling` skill from aihero.dev, not built here). A clarifying-questions instruction degenerates into either a wall of questions or premature agreement unless it's constrained by two specific splits: (1) primitive vs. wrapper — one battle-tested interrogation skill that thin, purpose-specific wrappers invoke, so the technique isn't reinvented per use case; (2) verify vs. ask — the agent checks anything it can confirm itself from available context and only asks about genuine decisions. On top of that: one question at a time (not a batch), the plan modeled as a dependency tree so an early answer reshapes later questions, every question shipped with the agent's own recommended answer (so obvious ones get rubber-stamped and only real disagreements slow things down), and a hard gate — no implementation until shared understanding is confirmed. Candidate fit for USADeBusk work: locking an RFQ/heater-card scope or an SOP's decision branches before drafting, both dependency-tree-shaped problems where premature agreement is the known failure mode.

Source: Claude Code session f4df43ad, 2026-07-09.

**Concrete negative constraints beat vague ones — name the model's specific attractor states, not the general failure.** Comparing two published skill-design approaches (the `Superpowers` plugin's process-forcing-function skills — TDD red-green-refactor, stop-and-diagnose-after-N-failures, brainstorm-before-code — against `anthropic-skills:frontend-design`'s two-pass plan-then-critique workflow) surfaced a distinction that generalizes: Superpowers guards against *process* failure (jumping to code, patching symptoms) by inserting a checkpoint at the exact point the model wants to skip ahead. `frontend-design` guards against *output homogeneity* — a harder problem, because the model doesn't experience mode collapse as a failure, it feels like taste — by forbidding its own specific attractor states by exact coordinates (e.g. blocking the hex code `#F4F1EA` with serif+terracotta, not just "avoid generic design"). "Be original" is a worthless instruction because the model already believes it's complying; a negative constraint only works when violating it is mechanically detectable (a hex code you can grep for, a phrase you can find). This vault's `01-context/output-preferences.md` already applies the technique for text register (no bullets in prose, no preamble, no closing summary — named, checkable attractor states). The caveat: hex-code-style blocklists are maintenance-bearing, not durable — once a specific pattern is widely blocked, the model's distribution moves elsewhere and the list needs a refresh; this differs from process-forcing-function rules like "write the failing test first," which don't decay the same way.

Checked against `usadebusk-estimating` (2026-07-20) on the hypothesis that proposal voice was a candidate for this treatment: it isn't. Every proposal section (opening paragraph, closing statement, disclaimer) is a literal fixed string in the skill's Section Templates, not open-ended model prose — the "extensive experience" disclaimer text this note originally flagged as a drift risk is itself the hardcoded template wording (`SKILL.md` Section 4), not something the model generates. The technique only applies where the model actually writes free text, and the estimating skill has no such surface today. Revisit only if a free-prose section (e.g. a cover letter or executive summary) gets added to the proposal template.

Source: Claude Code session a28ed43f, 2026-07-20; corrected same-day after checking the skill file directly.

## Anti-patterns

(Placeholder — add observed failure modes here. Format: what goes wrong, why, what to do instead.)

## Decision rules

**Evidence governance, not just extraction rules.** For any multi-step extraction or research task, track source family, revision/as-built status, contradiction chains, dependency chains, and calculation confidence alongside the extracted values. This prevents unsupported assumptions from silently becoming treated as facts downstream. The principle generalizes beyond heater drawing extraction — it applies to any workflow where intermediate outputs feed later decisions.

**Pre-Execution Audit pattern.** For multi-step documents or scripts, include an explicit audit section that assesses assumptions and logical flaws before generation begins, not after. Catching a bad assumption at the start costs one short exchange; catching it in a finished document costs a rewrite.

**Keep facts, assumptions, recommendations, and risks structurally separate.** In technical or decision-oriented outputs, these categories should be visually and structurally distinct — not interleaved in prose. A reader should be able to scan for assumptions without reading the full document.

**Test on real data before scaling.** Validate extraction rules or automation logic on actual examples, audit the failures, update the rules, then expand. Heavy automation built before rules are validated is low-ROI and often reduces quality relative to a manual process. The right order: real data → audit loop → rule update → scale.
