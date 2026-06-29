# CLAUDE.md — USADeBusk Vault Entry Point
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

SOPs are the primary document type. The following describes actual production SOPs — not aspirational structure.

**Title block (every SOP)**
- Gold label: "MECHANICAL DECOKING OF" (or job-specific variant)
- Large bold heater name/title
- Italic subtitle: "Operational SOP | USADeBusk | [Facility]"
- 2×4 header grid table: Project / Heater / Document No. / Revision // Contractor / Document Type / Prepared By / Date
- Header table: dark charcoal fill on label rows, white text, bold

**Page layout**
- Font: Helvetica throughout (Arial acceptable as fallback for DOCX generation)
- Running header: document number right-aligned, subtitle below (lighter weight)
- Footer: "DeBusk Services Group | Deer Park, TX" left, page number right
- Color scheme: gold (#FCC30A) for section divider rules and subsection headers; charcoal/black for body text and primary table headers
- US Letter, 1" margins

**Section structure — derived from completed SOPs**
Section numbering and order adapt to job complexity. Baseline structure:
1. Purpose and Scope (includes Heater & Coil Specifications table)
2. Safety and PPE Requirements (includes configuration subsections: launcher/receiver, water supply, TriMax allocation when running a second TriMax)
3. System Configuration (equipment list table)
4. Operating Parameters (table: tube IDs, footage, cleaning medium, pressure range, max pig OD, completion criteria)
5. Pig Progression Sequence (table: stage / pig OD / type / purpose)
6. Procedure (phase-based subsections: Rig-In, Mechanical Decoking, Smart Pig if applicable)
7. Flow Test Procedure (BEFORE baseline + AFTER post-cleaning; GPM controlled constant)
8. Completion and Demobilization (dewater, depressurize, rig-out, waste management)
9. Definitions (two-column table)

Additions for ExxonMobil / major operator jobs: Phase I flush section, Phase III Smart Pig section, written approval gate before rig-out.

**Tables**
- Header row: dark charcoal fill, white text, bold
- Body rows: white background
- Callout boxes for critical warnings (border accent with ⚠ symbol)

**What this replaces**
This vault definition governs actual SOP production — it supersedes the earlier aspirational SOP structure from the now-retired Claude Projects system prompts. The system prompt governs behavior and role boundaries; this file governs output format.

---

## Insight Loop

When a realization surfaces that an existing method is improvable:

1. Drop a note in `00-inbox/` tagged `type: insight`
2. Run `/ingest` — Claude reads it, identifies which docs it touches, cross-references against prior decisions
3. Claude writes proposed revision to `output/` with a plain summary of what changes and why
4. Jesse approves, modifies, or rejects
5. On approval: Claude writes updated file to correct location, moves old version to `archive/` with timestamp
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
