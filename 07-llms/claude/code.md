---
title: Claude Code
created: 2026-06-29
tags: [claude, claude-code, tooling]
---

# Claude Code

Claude Code is Anthropic's official CLI for Claude — an interactive agent that runs in the terminal and operates directly on the local filesystem and git repo. It is distinct from claude.ai chat; it has tool access (read, write, bash, grep, etc.) and executes tasks rather than discussing them.

## How I use it

Primary interface for all implementation work: writing vault notes, building and updating skills, running git operations, generating documents, and anything that touches files. The split is: **chat = decisions, Code = execution**. See [[chat]] for the chat-side counterpart.

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
- File write on Windows uses PowerShell-style paths. Bash tool uses POSIX syntax inside Git Bash — path mismatches can cause silent failures if mixing shells. See [[windows-config]] for the OneDrive KFM redirection trap and shell-path details.
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

For Fable-5-era Claude, over-prescriptive, step-enumerated prompts measurably reduce output quality — stating the goal and constraints outperforms scripting the conversation turn-by-turn. (See [[prompt-engineering]] for the broader prompting principles this reinforces.) Separately, a fresh-context verifier subagent catches problems that self-critique on the same context misses; delegate red-teaming to a separately-spawned agent rather than asking the acting agent to audit its own recommendation.

Applied when building the `idea-triage` skill (2026-07-02): SKILL.md states goals/constraints rather than scripting the triage conversation, and the red-team pass against "execute" verdicts runs as a spawned subagent, never inline self-review.

Source: Claude Code session 6601b270, 2026-07-02.

## Naive exact-match scoring can manufacture a false signal

When building a programmatic evaluator for LLM output (not an LLM judge — a deterministic field-matching scorer), a strict-equality rule for anything that "looks numeric" will fail correct extractions that include a natural-language unit (e.g. model output `"22 dollars"` against a reference value `"22"`). A first read of the aggregate scores looked like a real capability gap between two models; auditing every individual failure showed 100% were this same formatting artifact, not a wrong value. Fix: for a bare-numeric reference value, pull the numeric core out of the candidate string and compare that instead of the whole string; treat hyphens and spaces as equivalent for text-field comparisons (e.g. "two-year" vs "two years").

General rule: when an aggregate score contradicts expectations (especially "the more capable model did worse"), audit the actual failing cases before trusting the number — a scoring bug looks identical to a real finding until you check.

Source: Claude Code session 9a0789df, 2026-07-06 (`leverage` repo thesis experiment, see [[self-improving-systems]]).

## Undocumented `tasks/` directory

`C:\Users\Jwuts\.claude\tasks\` contains four UUID-named folders with numbered `.json` files and `.lock` files. This looks like internal session/agent task-queue plumbing rather than anything user-authored, and it isn't referenced in either CLAUDE.md or the vault governance doc. Not confirmed broken — just unexplained. Treat as safe to ignore until something depends on understanding it.

Source: Claude Code session (harness audit), 2026-07-07.

## Auto mode and allow-list pruning pull in opposite directions

`permissions.defaultMode: "auto"` auto-saves approvals as you work, which is the same mechanism that lets a project's `settings.local.json` allow list grow unbounded over time. A 2026-07-19 audit found `obsidian-work/.claude/settings.local.json` had grown to 61 allow rules; 7 were live hazards rather than clutter — `Bash(git checkout *)` (matches `git checkout -- .`, same loss class as the already-banned `reset --hard`), `Bash(python -c ' *)` / `Bash(python -)` (unrestricted code execution), `Bash(pip install *)` (arbitrary PyPI package install+run), a `cat "...settings.json" 2>/dev/null *` rule with a trailing wildcard after a redirect (so `; <anything>` appends cleanly), and `Read(//c/Users/Jwuts/**)` (whole user profile — SSH keys, browser data, any `.env` on the machine). Eighteen more were dead one-offs (job-specific commit messages, path-specific `ls -R` probes, git verbs already covered by checked-in project settings). Separately, `~/.claude/settings.json` had `Bash(git fetch:*)`, which reads as read-only but permits arbitrary code execution via `--upload-pack='<cmd>'` and `ext::` remote URLs — this is why Claude Code's own vetted read-only git set excludes it.

Pruning is not a fix, it's a reset of a counter that climbs again under auto mode — the audit's own doctor pass watched `Bash(npm view *)` get auto-added mid-session by a version lookup. An over-pruned rule just costs a re-approval prompt (no data loss), so pruning aggressively is low-risk. Re-check the rule count periodically (this audit set a 2026-09-19 re-check date for `obsidian-work`); if it's back near 60 with hazardous wildcards among the entries, auto mode costs more in permission drift than it saves in prompts.

Source: `/doctor` pass, 2026-07-19.

## Skill description length is a per-session token cost, and a stale job-specific banner is worse than none

A skill's `description:` field is resident in every session's skill listing regardless of whether the project is relevant — length there is a real, ongoing token cost, not a one-time authoring cost. A 2026-07-19 audit found `usadebusk-fieldpm`'s description carrying a job-specific "ACTIVE for USA26038... re-dormant at demob" banner at 769 characters (~196 tokens), the longest of any skill's description. The same audit found the skill's usage counter at zero lifetime (absent from `skillUsage` in `~/.claude.json`, no `Skill` dispatch for it in the 50 most recent transcripts) despite nine days into the job it names as active — an unresolved open question (real workflow gap vs. workflow happening outside Claude Code) rather than a confirmed bug. The actionable lesson independent of that question: a job-specific ACTIVE banner needs its own demob trigger, since a stale banner pointing a live-job routing hint at a finished job is worse than a plain dormant one-liner, and reverting it recovers most of the token cost too.

Source: `/doctor` pass, 2026-07-19.

## Links

- Config repo: https://github.com/TheSkinz/claude-config
- Vault CLAUDE.md: `C:\Users\Jwuts\obsidian-work\CLAUDE.md`
