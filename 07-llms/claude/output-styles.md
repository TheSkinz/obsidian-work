---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-08-17
review_after: 2026-11-17
related:
  - [[code]]
  - [[command-reference]]
  - [[dynamic-workflows]]
tags: [reference, claude-code, output-styles, system-prompt, subagents]
---

# Claude Code — Output Styles

An output style modifies Claude Code's **system prompt** to set role, tone, and default response
format. Captured because the vault had no coverage of the feature at all, because the widely-shared
community writeups describe a command that no longer exists, and because the subagent boundary
below is the fact that decides whether the feature is safe to use here.

Verified 2026-08-17 against `code.claude.com/docs/en/output-styles` and
`code.claude.com/docs/en/sub-agents`, on Claude Code **2.1.220**.

## The four facts that aren't guessable

**`/output-style` is gone.** It was deprecated in v2.1.73 and removed in v2.1.91. Every community
screenshot that says "run `/output-style`" predates that. The live paths are `/config` > Output
style in the terminal, or the `outputStyle` field in a settings file. In the desktop app `/config`
opens Settings > Claude Code rather than a picker menu, so on this machine it is the settings field
or the app's Settings pane.

**`keep-coding-instructions` defaults to `false`.** A custom output style silently drops Claude
Code's built-in software-engineering instructions — change scoping, comment conventions, how it
verifies work — unless the frontmatter sets it true. Nothing warns about this. Set it true for any
style that is changing *how* Claude communicates while still expecting it to code; leave it out only
when the session genuinely isn't software engineering at all.

**Output styles do not reach subagents. CLAUDE.md does.** A non-fork subagent loads every level of
the CLAUDE.md hierarchy, including `~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, and
managed policy — the built-in Explore and Plan agents being the exception, they skip it. It also
loads any skill named in the agent's `skills` field. It does **not** load the output style or the
main conversation's auto memory. A fork is the exception, because it inherits the parent's full
system prompt. This is the load-bearing fact for the vault: the six loops, `usadebusk-vault-ingest`,
and `adversarial-review` all run as subagents, so anything moved out of CLAUDE.md and into an output
style disappears from all of them, silently.

**It loads once, at session start.** Changing the style takes effect after `/clear` or in a new
session, never mid-conversation. The "switch to a gentler style when you're tired" framing that
circulates with this feature undersells that it costs a session restart.

## Placement, and why that's the whole point

Output styles are appended to the end of the system prompt, and the harness re-injects reminders to
adhere to them through the conversation. CLAUDE.md arrives as a user message *after* the system
prompt, with no reminder loop. That reinforcement is the entire marginal value of the feature over
CLAUDE.md — it is a better home for rules that decay late in long sessions, and a worse home for
anything a subagent needs.

The neighbouring mechanisms, for completeness. `--append-system-prompt` appends to the system prompt
without removing anything, for a single invocation. Agents run a separately scoped helper with its
own system prompt, model, and tools. Skills load task-specific instructions when invoked or relevant.

## Built-ins

**Default** is the standard software-engineering system prompt. **Proactive** executes immediately
and makes reasonable assumptions instead of pausing on routine decisions — stronger autonomous-
execution guidance than auto mode applies, and independent of permission mode, so permissions still
decide what runs without asking. **Explanatory** interleaves educational "Insights". **Learning**
adds `TODO(human)` markers and asks the user to write small pieces themselves. Explanatory and
Learning produce longer responses by design.

## File layout

A style is a markdown file — frontmatter plus the instructions appended to the system prompt. Three
levels: user (`~/.claude/output-styles`), project (`.claude/output-styles`), and managed policy.
Project styles load from every `.claude/output-styles/` between the working directory and the repo
root; on a name collision the one closest to the working directory wins. Plugins can ship styles in
an `output-styles/` directory, and a plugin style with `force-for-plugin` applies automatically
whenever the plugin is enabled, overriding the user's `outputStyle` setting.

Frontmatter fields are `name` (defaults to the file name), `description` (shown in the `/config`
picker), `keep-coding-instructions`, and `force-for-plugin` (plugin styles only).

## What was done here, 2026-08-17

`~/.claude/output-styles/jesse-default.md`, activated by `"outputStyle": "Jesse Default"` in
`~/.claude/settings.json` at user level rather than through `/config`, which writes to project-level
`.claude/settings.local.json` and would scope it to one repo.

It was first written as a **thin reinforcer** carrying five rules that decay late in long main-thread
sessions — no bullets in prose, no closing recap, concise by default, arrow chains for unfamiliar
sequences, direct pushback — plus an explicit line naming global CLAUDE.md and [[output-preferences]]
as authority. Session-mode inference, ask-vs-proceed, pre-build rules, and document-output rules were
**not** copied in: they live in `01-context/output-preferences.md`, they reach subagents, and
duplicating them is exactly the drift this design avoids.

**That version lasted a few hours. See the section below for what is actually live.**

A stray `C:\Users\Jwuts\.claude\.claude\settings.local.json` exists on this machine, an artifact of
running claude with cwd set to `~/.claude`. It currently holds only an accumulated permissions
allowlist. If `/config` is ever run from that directory it will write an `outputStyle` there and
shadow the user-level value.

## The reinforcer-only style was a placebo — cut to one rule the same day

Config `8afdb26` (2026-08-17) replaced all five rules with one. The file is now nine lines, shorter
than it was in its first form, and the config is smaller than before the style existed at all.

The reason it was cut is the more useful finding. **A style that restates rules already in CLAUDE.md
in a different position reinforces nothing, and the session that wrote it was the evidence.** Those
five rules were in force twice over — once in CLAUDE.md, once in the new style file — and the
conversation ran long, enumerated, and tail-heavy throughout. Placement plus a reminder loop is a real
mechanism for a rule the model would otherwise forget, but not for one it is already reading and
already not following. A reinforcer with no new instruction in it reinforces nothing.

What survived is the single rule Jesse names as the one he actually wants: end the response by naming
what is outstanding specifically enough to act on — the task, where it lives, what it costs — then the
suggested action with its reason, and close with nothing when nothing is outstanding. CLAUDE.md already
says close with forward-looking suggestions; the style adds only the specificity requirement, and gets
the reminder loop CLAUDE.md does not have. His own framing of the rest: they "sounded nice" but are
disposable if they cost anything.

**"Answer first" was considered and deliberately dropped.** It collides with the recon-before-drafting
hard constraint — a future session reading the style cold, with none of this context, could take it as
licence to lead with a confident conclusion before opening the files, which is the exact failure the
vault's epistemics exist to prevent. It could have been written as "the conclusion leads once you have
it," but a rule that needs a proviso to stop it causing the failure it was meant to avoid is not worth
its line.

**A second rule was drafted and dropped for over-firing.** "State any open decision as a question with
a recommendation" applied literally ends every turn with a question, which is the confirmation-seeking
CLAUDE.md bans. Bounding it to genuine forks — Lane 4, irreversible, a real choice — is what the
surviving rule's "when nothing is outstanding, close with nothing" clause does instead.

The general lesson, which is why this is recorded rather than just changed: **ask which single
preference actually matters before building machinery around a list of them.** A stated list read as
a specification produced five rules; the same list read as a ranking produced one, and the one was
already sufficient.

Source: Claude Code session `06a84965`, 2026-08-17; config `8afdb26`.

## Links

- https://code.claude.com/docs/en/output-styles
- https://code.claude.com/docs/en/sub-agents
