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

(Placeholder — add validated patterns here as they accumulate. Format: pattern name, when to use, example prompt skeleton.)

## Anti-patterns

(Placeholder — add observed failure modes here. Format: what goes wrong, why, what to do instead.)

## Decision rules

(Placeholder — add rules for choosing between approaches, e.g., when to use a Gem vs. a one-off prompt, when to use structured vs. free-form output.)
