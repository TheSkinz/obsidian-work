---
title: Claude Code
created: 2026-06-29
tags: [claude, claude-code, tooling]
---

# Claude Code

Claude Code is Anthropic's official CLI for Claude — an interactive agent that runs in the terminal and operates directly on the local filesystem and git repo. It is distinct from claude.ai chat; it has tool access (read, write, bash, grep, etc.) and executes tasks rather than discussing them.

## How I use it

Primary interface for all implementation work: writing vault notes, building and updating skills, running git operations, generating documents, and anything that touches files. The split is: **chat = decisions, Code = execution**.

The vault at `C:\Users\Jwuts\obsidian-work` is the working directory. Claude Code reads `CLAUDE.md` and `01-context/` on startup to load session context automatically.

Skills drive specialized behavior. When a task touches USADeBusk work, the relevant skill(s) are loaded (via `/skill` or Cowork's auto-load). Skills live at `~/.claude/skills/`. The active set:

- `usadebusk-core` — always loaded for USADeBusk tasks
- `usadebusk-equipment`, `usadebusk-estimating`, `usadebusk-fieldpm`, `usadebusk-ops`, `usadebusk-sop` — domain-specific
- `usadebusk-vault-ingest` — converts raw docs to vault notes
- `adversarial-review`, `idea-triage` — general-purpose (non-USADeBusk) skills

(The `claude-obsidian` plugin was dropped 2026-06-30 and fully uninstalled 2026-07-06 — its skills are no longer available.)

## Config repo

`~/.claude` IS the live runtime directory — no deploy step. Config repo: https://github.com/TheSkinz/claude-config. Fetch before working on it to avoid clobbering upstream changes.

## Key workflow patterns

**Recon before drafting.** Read the actual files first; never infer or assert unverified specifics as certain. This is the rule that prevents hallucinated content in documents that look authoritative.

**Staged-count guard.** Before every commit, verify staged file count matches what was intended. One extra file staged is an easy way to commit vault noise or credentials.

**Fetch before work.** For config repo edits, pull first.

**Two-failure stop.** After two consecutive failures from the same root cause, stop and diagnose before a third attempt. Prevents spinning on a wrong assumption.

**Git guard hook.** `~/.claude/hooks/usadebusk-git-guard.mjs` blocks git mutation verbs on any command containing a `USADEBUSK\` directory path. A block there is expected — get explicit confirmation before proceeding.

## Known limitations / gotchas

- Claude Code is session-scoped; context is rebuilt each session from `01-context/` and memory. Long context is summarized automatically, but deep state from early in a session can drift.
- File write on Windows uses PowerShell-style paths. Bash tool uses POSIX syntax inside Git Bash — path mismatches can cause silent failures if mixing shells.
- Large vault glob operations can be slow; prefer targeted reads over broad auto-scans.
- Vision / image reading works but hasn't been benchmarked against Gemini for engineering drawings. See [[gem-drawing-extraction]] for current production standard.

## Underutilized capabilities

Identified in a 2026-06-23 capability review and still partly open:

- **Permissions allowlist** in `settings.json` / `settings.local.json` — pre-declaring routine read-only and path-scoped write commands removes repeated interactive prompts. This is also what lets an unattended scheduled run proceed without stalling. Partially deployed.
- **Session-transcript search** — past sessions are stored as plain JSONL under `~/.claude/projects/`. They can be searched directly (or via the `ccd_session_mgmt` MCP tool). This is the foundation of the vault capture loop's harvest step. See [[vault-capture-loop-spec]].
- **Custom slash commands** — none defined yet; repeatable multi-step workflows are candidates.

The git-guard hook recommended in the same review has since been implemented (see Key workflow patterns above).

## Dispatch vs. local sessions — collision risk

Claude Dispatch runs in an isolated cloud sandbox: no `claude-config` skills checkout, and no visibility into locally-running Claude Code sessions on the same machine. A local Code session and a parallel Dispatch run can both triage the same repo state independently and push divergent, unmerged branches without either side detecting the collision. Mitigation: `git fetch` before starting local vault work if Dispatch may have touched the repo recently.

Source: Claude Code session 04d37db4, 2026-07-05 (discovered via a git-fork reconciliation between a local session and a Dispatch run on `obsidian-work`).

## Fable 5 skill-design guidance

For Fable-5-era Claude, over-prescriptive, step-enumerated prompts measurably reduce output quality — stating the goal and constraints outperforms scripting the conversation turn-by-turn. Separately, a fresh-context verifier subagent catches problems that self-critique on the same context misses; delegate red-teaming to a separately-spawned agent rather than asking the acting agent to audit its own recommendation.

Applied when building the `idea-triage` skill (2026-07-02): SKILL.md states goals/constraints rather than scripting the triage conversation, and the red-team pass against "execute" verdicts runs as a spawned subagent, never inline self-review.

Source: Claude Code session 6601b270, 2026-07-02.

## Naive exact-match scoring can manufacture a false signal

When building a programmatic evaluator for LLM output (not an LLM judge — a deterministic field-matching scorer), a strict-equality rule for anything that "looks numeric" will fail correct extractions that include a natural-language unit (e.g. model output `"22 dollars"` against a reference value `"22"`). A first read of the aggregate scores looked like a real capability gap between two models; auditing every individual failure showed 100% were this same formatting artifact, not a wrong value. Fix: for a bare-numeric reference value, pull the numeric core out of the candidate string and compare that instead of the whole string; treat hyphens and spaces as equivalent for text-field comparisons (e.g. "two-year" vs "two years").

General rule: when an aggregate score contradicts expectations (especially "the more capable model did worse"), audit the actual failing cases before trusting the number — a scoring bug looks identical to a real finding until you check.

Source: Claude Code session 9a0789df, 2026-07-06 (`leverage` repo thesis experiment, see [[self-improving-systems]]).

## Links

- Config repo: https://github.com/TheSkinz/claude-config
- Vault CLAUDE.md: `C:\Users\Jwuts\obsidian-work\CLAUDE.md`
