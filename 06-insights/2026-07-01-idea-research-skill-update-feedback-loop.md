---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-01
review_after: 2026-08-01
related:
  - [[idea-skill-update-feedback-loop]]
  - [[vault-idea-loop-spec]]
  - [[knowledge-system-governance]]
tags: [review, knowledge-system, idea-research, skills]
---

# Idea Research — Skill-Update Feedback Loop

## Trigger

First run of the Vault Idea Research Loop. Three `idea-seed` notes were queued in `00-inbox/`, all created 2026-06-30 with identical frontmatter `created` dates. Tiebreak used filesystem mtime (no git history yet for any of the three — none had been committed). `idea-skill-update-feedback-loop.md` had the oldest mtime (17:00:15, vs. 17:00:19 and 17:00:23 for the other two), so it was picked as the oldest of the batch.

## Evidence

**Internal — the problem is already real, not hypothetical.** `00-inbox/2026-06-30-skill-naming-cleanup.md`, written the same night as this idea-seed, documents a live instance of exactly the drift this idea describes: `usadebusk-vault-ingest`'s SKILL.md still described the retired OneDrive vault path (`C:\Users\Jwuts\OneDrive\obsidian-usadebusk`), superseded 2026-06-27 by the canonical `C:\Users\Jwuts\obsidian-work` per [[vault-source-of-truth]]. It was caught by manual read, not by any automated check — no mechanism currently watches for vault-truth-vs-skill-content drift. Confirmed by reading [[knowledge-system-governance]] and [[vault-agent-loop-spec]]: both govern drift *within* the vault (contradictions between notes, staleness via `review_after`) but neither has scope over `~/.claude/skills/`. `ls ~/.claude/skills/` shows no self-audit or drift-check skill among the seven installed USADeBusk skills.

**External — this is a solved problem in the Claude Code ecosystem, not a novel one.** Web search turned up an active genre of installable Claude Code skills built specifically for this class of problem:

- [CAI Drift Check](https://mcpmarket.com/tools/skills/cai-drift-check) — scans documentation, compares metadata against git commit history for the source files it describes, and sorts results into a prioritized three-tier staleness system.
- [Context Drift Detector (ctx-drift)](https://mcpmarket.com/tools/skills/context-drift-detector) — dual-layer check: structural (dead file paths, missing references) plus semantic (outdated conventions), aimed at preventing an agent from acting on stale context.
- An "Agent Instruction Audit" pattern (surfaced via search, not independently verified past the summary) that specifically audits `AGENTS.md`/`CLAUDE.md` and nested agent-guidance files for staleness, duplication, and **AGENTS/CLAUDE mirror drift** — the closest direct analogue to "skill content drifting from vault truth."
- [claude-memory-health](https://github.com/alexknowshtml/claude-memory-health) — a comparable pattern one layer over: audits a `MEMORY.md` index for bloat, orphans, broken links, and staleness, and can autonomously demote stale entries. Not the same target (memory index vs. skill files) but the same shape of solution, and notable because it's the same kind of file this session's own auto-memory system uses.
- A general `staleness_check.py ./my-skill/ --check-deps --check-drift` pattern showed up independently across multiple listings, suggesting "staleness/drift check as a skill sub-command" is becoming a convention, not a one-off.

**Adjacent architectural pattern.** Broader search on "avoid prompt/doc sync drift" surfaced the `AGENTS.md`-as-single-source-of-truth convention (used by OpenAI Codex, Sentry, Airflow, Temporal, Cloudflare Workers SDK, Coder repos per [this piece](https://medium.com/codandotv/agents-md-a-single-source-of-truth-for-any-ai-in-your-repo-ce1d0d7ea918)). That pattern avoids drift by generating from one file rather than syncing two — but it doesn't map cleanly onto this vault's shape, where the vault (knowledge, facts) and the skills repo (`~/.claude/skills/`, behavior) are deliberately separate git repos serving different purposes. The idea-seed's actual ask — propose a skill *diff* when a vault fact changes — is a cross-repo propagation problem, which none of the tools found above solve directly; they detect drift within a single repo/file tree, not vault-repo-changed → skill-repo-should-change.

## Interpretation

**Already partially covered, with one real gap identified.** The general problem — "agent instruction files silently drift from the truth they're supposed to reflect" — is a known, actively-tooled problem with several off-the-shelf Claude Code skills addressing it. This idea-seed is sound (not a trap, not premature) and is proven necessary by the skill-naming-cleanup incident found in this same inbox. But it is not fully "already covered": every tool found audits staleness *within* a single tree (skills auditing themselves, or memory auditing itself). None of them span two repos and propose that a change in repo A (`obsidian-work`) should produce a proposed diff in repo B (`~/.claude/skills/`). That specific cross-repo propagation mechanic is the part of this idea-seed that would need original design work; the staleness-*detection* half of it likely does not need to be built from scratch.

## Recommended Action

Bounded one-shot investigation, not a build. Before designing anything: (1) install or trial one of the existing staleness-audit skills (Agent Instruction Audit pattern or CAI Drift Check look closest) against `~/.claude/skills/` as a manual, on-demand check — this alone might close most of the gap the skill-naming-cleanup incident exposed, with zero custom build. (2) Only if that leaves the cross-repo propagation need unmet, scope a narrow addition — a manual, propose-only step (matching this vault's low-ceremony-but-not-silent norm) that flags "vault note X changed, skill file Y references the same fact, go check it" — rather than automated skill-repo edits, which would cross this loop's own hard boundary against ever touching `~/.claude/skills/`.

## Decision

- [ ] Build now
- [ ] Bounded one-shot investigation (trial an existing staleness-audit skill against `~/.claude/skills/`)
- [ ] Park
- [ ] Drop

## Apply Log

| Date | Action | By |
|---|---|---|
| | | |
