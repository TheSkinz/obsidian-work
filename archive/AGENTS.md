# AGENTS.md — USADeBusk Vault Entry Point
**Last updated:** 2026-04-25
**Vault scope:** USADeBusk industrial services only. Jesse Utsey, Project Manager / Field Supervisor.

---

## Session Startup Protocol

Every session: read all files in `01-context/` before responding. Total target: under 2,000 words.

Load on-demand only when named:
- `02-facilities/[Client-City-State]/` — when a specific facility is referenced
- `04-knowledge/` — when technical depth is needed (equipment specs, SOP structure, process theory)

Never load `archive/`, `attachments/`, or `templates/` automatically.

---

## Output Preferences

These rules govern all output. They do not require re-stating in conversation.

**Formatting**
- Concise by default. Full length only when task quality requires it.
- No bullet points in explanations, reports, or prose documents. Write in sentences and paragraphs.
- No excessive headers. Use headers for navigation, not decoration.
- No emojis unless Jesse uses them first.
- Lists are acceptable only when the content is genuinely enumerable (equipment lists, section sequences, step-by-step procedures).

**Tone and communication**
- Direct. Correct errors explicitly — hedged disagreement is not useful.
- No preamble restating the question. No closing summary restating the answer.
- Flag problems immediately. Do not wait to be asked.

**Session modes — infer from context, do not ask to confirm**
- Research: Direct recommendation first, then alternatives with trade-offs.
- Brainstorming: Direct recommendation first, then alternatives from different angles.
- Implementation: Verify approach before generating output. Confirm data model, environment, or architecture before building. If "done" is undefined, ask.
- Writing/editing: Match Jesse's voice and intent. Flag when a draft works against its own goal.

**Before building anything**
- Confirm exact terminology for domain-specific names before writing code or files.
- Verify target environment before writing rendering or visual output code.
- Two consecutive failures for the same class of reason: stop and diagnose before attempting again.

---

## Document Output: SOP Formatting Standard

The SOP formatting standard has one canonical home: **`04-knowledge/sops/sop-formatting-standard.md`**. It governs SOP layout, title block, page layout, section structure, and tables. Do not maintain a second copy here — this file previously embedded a partial duplicate, which is exactly the kind of drift the standard exists to prevent. Read the canonical file when producing an SOP; the `usadebusk-sop` skill governs SOP content and defers formatting to that same file.

---

## Insight Loop

When a realization surfaces that an existing method is improvable:

1. Drop a note in `00-inbox/` tagged `type: insight`
2. Run `/ingest` — Codex reads it, identifies which docs it touches, cross-references against prior decisions
3. Codex writes proposed revision to `output/` with a plain summary of what changes and why
4. Jesse approves, modifies, or rejects
5. On approval: Codex writes updated file to correct location, moves old version to `archive/` with timestamp
6. One-line entry added to `change-log.md`: date / what changed / trigger

Constraint: each `/ingest` cycle covers one item. No batching.

---

## Conflict Resolution

- Vault wins on output preferences and document formatting
- System prompts win on behavior, role, and tone
- When vault content and a system prompt conflict on formatting: vault wins
- When something in this file is ambiguous: ask one clarifying question, do not generate output

---

## What Not to Read

Mirrors `.claudeignore`:
- `archive/` — deprecated, reference only
- `attachments/` — raw files, not processed knowledge
- `templates/` — blank scaffolds, not content
