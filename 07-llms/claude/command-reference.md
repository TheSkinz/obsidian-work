---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-07-22
review_after: 2026-10-22
related:
  - [[code]]
  - [[2026-07-20-harness-map]]
tags: [reference, claude-code, commands, skills, usage]
---

# Claude Code — Command Usage Reference

The *"which command do I reach for, and how do I fire it"* lookup. Companion to
[[2026-07-20-harness-map]] (which inventories what shapes a response) and [[code]]
(how I use Claude Code). Organized by **when you'd reach for it**, not
alphabetically. Curated to vault / USADeBusk / field work — not the full command
dump.

> **Provenance & freshness.** Built-in commands verified against
> `code.claude.com/docs/en/commands` on **2026-07-22**; CLI version observed
> 2.1.143 (Bash PATH) to ~2.1.21x (app/transcripts). Native built-ins live in the
> harness binary, **not** in `~/.claude`, so they never appear in the skills list —
> the only way to confirm one exists or check its behavior is the docs, not a
> config grep. **Re-verify anything version-sensitive (command set, flags) against
> the docs before relying on it** — this note is a dated snapshot, not a live feed.
> This is the first instance of the durable-capture convention in [[code]].

---

## 1. Keep Claude working without re-prompting

The confusable cluster. All keep a session going; they differ in **what starts the
next turn** and **what stops it**. Pick by that.

| Command | Next turn starts when | Stops when | Scope |
|---|---|---|---|
| `/goal <condition>` | Previous turn finishes | A fast model confirms the condition holds | This session only; auto-clears |
| `/loop [interval] <prompt>` | A time interval elapses | You stop it, or Claude decides it's done | This session only |
| Stop hook | Previous turn finishes | Your script or prompt decides | Persists in settings, every session in scope |
| Auto mode | (does not start turns — approves *tool calls* within a turn) | Claude judges the work done | Config |
| `schedule` / scheduled task | A cron time fires, **no open session needed** | Its own logic | Standing, runs unattended |

- **`/goal all tests in test/auth pass, or stop after 20 turns`** — set a finish
  line and walk away. A Haiku evaluator checks after each turn. `/goal` alone to
  see turns/tokens spent; `/goal clear` to cancel. It's a wrapper around a
  session-scoped Stop hook. **Does not change permissions** — to run unattended,
  pair with **auto mode**. Caveat: auto mode is the same mechanism that grows the
  allowlist unboundedly (see the 2026-07-19 doctor finding in [[2026-07-20-harness-map]]),
  so unattended `/goal` runs inherit that hygiene risk. Bound goals with an
  "or stop after N turns" clause. Requires CLI ≥ 2.1.139.
- **`/loop 30m /vault-capture`** — re-run on a clock, not to a condition. Right when
  the trigger is time ("check every 30 min"), wrong when it's a state ("until clean").
- **Scheduled tasks / `schedule` skill** — your five vault loops. Use when the work
  should run with no terminal open at all.

## 2. Vault maintenance

- **`consolidate-memory`** (skill) — cleans the `~/.claude` **memory index** (merge
  dupes, fix stale facts, prune). NOT the same as the vault's **Consolidation loop**,
  which consolidates vault *notes* (see [[vault-consolidation-loop-spec]]). Run when
  the memory index grows or a stale entry is spotted.
- **Five vault loops** — Capture, Idea-research, Consolidation (scheduled); Agent/Review,
  Skill-drift (on-demand). Status lives in `50-dashboards/health.md`; heartbeats there
  tell you if a scheduler went silent.
- **`vault_lint.py` / `vault_health.py` / `vault_index.py`** (`tools/`) — lint, health
  dashboard, INDEX regen. Run after structural vault edits.

## 3. Building deliverables

Skills auto-fire when a matching file type is the input/output; you rarely invoke by name.

- **`docx` / `xlsx` / `pdf` / `pptx`** — Word / Excel / PDF / PowerPoint. Windows
  gotcha: build with `NODE_PATH=<global>`; call `soffice.exe` directly (the skill's
  `soffice.py` wrapper crashes on Windows). See the docx memory.
- **`dataviz`** — read before writing *any* chart/graph/dashboard, in any medium.
- **`theme-factory`** — apply a consistent theme to an artifact (slides, docs, HTML).

## 4. Code / tooling quality (for `tools/*.py`)

- **`/code-review [level] [target]`** — correctness bugs + cleanup on the current diff.
  Reach for it before committing changes to the vault Python.
- **`simplify`** — reuse/simplify/efficiency pass on changed code. Quality only, not
  bug-hunting.
- **`/security-review`** — security pass on pending changes.
- **`adversarial-review`** (skill) — scored finder/adversary/referee for
  security-sensitive or production code where you want high-fidelity issue detection.

## 5. Underused native built-ins

Past my Jan-2026 cutoff — sourced from the docs, not memory. The ones worth knowing:

- **`/rewind [checkpoint|N]`** — roll **code AND conversation** back to a checkpoint.
  The real safety net for client deliverables and irreversible-ish vault edits.
- **`/context [all]`** — visualize context usage as a grid. Use when a long session
  feels heavy or eager-load is suspect.
- **`/usage`** (alias `/cost`) — session API usage/cost. You track limit-hitting closely.
- **`/effort [level|auto]`** — set model effort level; matches routing by task difficulty.
- **`/branch [name]` / `/fork [prompt]`** — split the conversation to try a bid/approach
  without polluting the main thread (`/fork` runs the copy in the background).
- **`/background [prompt]` + `/tasks` + `/status`** — detach work to a background agent
  and free the terminal. Fits idle-capacity automation.
- **`/deep-research <question>`** — fan out web searches, fetch sources, synthesize a
  cited report. Overlaps the idea-research loop for industry questions.
- **`/advisor [model|off]`** — consult a second model for guidance; suits a verification bent.
- **`/diff`** — interactive diff viewer for uncommitted changes; native alternative to
  eyeballing `git diff -w`.
- **`/btw [question]`** — quick side question that doesn't pollute the conversation.
- **`/memory`** — edit CLAUDE.md files and manage auto-memory.
- **`/rewind`**, **`/teleport` / `/desktop` / `/remote-control`** — pull/continue a
  session across terminal, desktop app, and other devices.

## 6. Harness hygiene

- **`/fewer-permission-prompts`** — scan transcripts, add an allowlist to cut prompts.
  Hazard note: hand-review each added rule — auto-mode + broad wildcards
  (`git checkout *`, `python -c ' *`, `Read(//c/Users/Jwuts/**)`) are how the allowlist
  grew dangerous in the 2026-07-19 audit.
- **`update-config`** (skill) — the way to make "**whenever X, do Y**" real. Automated
  behaviors need hooks in `settings.json` (the harness runs them), not memory/prefs.
- **`skill-creator`** — create/optimize skills and run evals on them.
- **`/init`** — generate a `CLAUDE.md` for a repo. **`/doctor`** — setup checkup.

## 7. USADeBusk domain (mostly auto-load — know they exist)

`usadebusk-core` (always, for any USADeBusk task) + `usadebusk-equipment`,
`usadebusk-estimating`, `usadebusk-fieldpm`, `usadebusk-ops`, `usadebusk-sop`,
`usadebusk-vault-ingest`. They trigger on the matching task (proposal, estimate, SOP,
field PM, receipts, doc ingest); you don't normally type them.

## 8. Explicitly skip (so you stop wondering)

The `engineering:*` set — `incident-response`, `deploy-checklist`, `standup`,
`system-design`, `tech-debt`, `testing-strategy`, `architecture`, `debug`,
`documentation` — is software-team workflow, not vault or field ops. Also `morning`
and `setup-cowork`. Named here so a picker sighting doesn't cost you a second look.
