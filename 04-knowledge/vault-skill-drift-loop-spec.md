---
type: governance
status: active
source_authority: primary
created: 2026-07-07
last_reviewed: 2026-07-07
review_after: 2026-10-07
related:
  - [[vault-capture-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[knowledge-system-governance]]
  - [[estimating-actuals-rollup]]
tags: [knowledge-system, agent-loop, skill-drift, governance]
---

# Vault Skill-Drift Loop Spec

The fourth loop. [[vault-capture-loop-spec]] files and harvests into the vault; this loop closes the return path — it checks whether the deployed skills at `~/.claude/skills/` still agree with vault truth and with each other, and packages any drift as a ready-to-merge proposal. Skills are the only layer every session loads: knowledge that reaches a skill compounds automatically, knowledge stranded in a vault note compounds only when someone remembers to look.

Origin: the 2026-07-06 harness judgment audit found the fieldpm skill had drifted since March — contradicting three newer skills on pig-type definitions, L/C/R handling, and receipt scope — and it took a full multi-agent audit to notice. This loop is the standing, cheap version of that audit.

## Loop Name

Vault Skill-Drift Loop

## Trigger

Scheduled monthly (1st of the month, ~3 AM local) via `mcp__scheduled-tasks`. Runbook prompt: `~/.claude/scheduled-tasks/vault-skill-drift-loop/SKILL.md`. Heartbeat tracked by `tools/vault_health.py` under the `skill-drift:` commit prefix (31-day cadence).

## Scope

Reads: every `SKILL.md` and reference file under `~/.claude/skills/`; vault knowledge layers (`04-knowledge/`, `06-insights/`, `07-llms/`, `08-systems/`); `04-knowledge/estimating-actuals-rollup.md`; the two CLAUDE.md files; git log of the config repo since the last run; **the agent memory directory** (`~/.claude/projects/C--Users-Jwuts-obsidian-work/memory/` — index + topic files), audited as a drift surface only, never edited by this loop.

Writes:

- One review note per run in `06-insights/` (`YYYY-MM-DD-skill-drift-review.md`, `review_type: skill-drift`) — or a clean no-op report when nothing drifted.
- When findings exist: a proposal branch in the config repo (`~/.claude`), named `drift/YYYY-MM`, containing the proposed skill edits as commits, pushed to origin. **Never merged by the loop.** Jesse reviews the review note, then merges or discards the branch.

Never edits skills on `main`. Never touches vault operational content, pricing values, or SOP values directly — proposed changes to those live only on the unmerged branch and take effect only when Jesse merges.

## What counts as drift

1. A vault note (or the actuals rollup) contradicting a skill's stated fact, value, or path.
2. Two skills contradicting each other (the audit's fieldpm-vs-equipment class).
3. A skill referencing a file, folder, plugin, tool, or workflow that no longer exists.
4. A correction applied to one home of a fact while a pointer or restatement elsewhere still carries the old version.
5. An agent-memory file asserting state the vault, skills, or filesystem contradict (retired tools still listed as live, renamed files, "not yet done" claims with completion evidence in git). Memory findings are *flagged only* — the review note recommends a `/consolidate-memory` pass; this loop never edits memory files itself.

## Ceremony Level

Low for detection, zero authority for application. Every proposed edit is a diff Jesse can read in one sitting; the review note quotes the exact current line and the exact proposed line with the evidence for why. Lane 4 content (pricing, safety, SOP values, domain truth) may appear in proposals — flagged as Lane 4 in the note — but only a merge by Jesse applies it.

## Loop Steps

1. `git -C ~/.claude fetch` and confirm a clean working tree on `main`; stop if ambiguous.
2. Read all skills; read vault layers changed since the last `skill-drift:` heartbeat (git log date-bounded); read the actuals rollup.
3. Detect drift per the four classes above. Quote exact lines — no finding without a quote (audit discipline).
4. If nothing found: write nothing, commit nothing, report a clean no-op, stop.
5. Write the review note in `06-insights/`: per finding — severity, file:line, current text, proposed text, evidence, lane classification. Decision checkboxes for Jesse. Apply Log empty.
6. Create branch `drift/YYYY-MM` from `main` in the config repo, apply the proposed edits, commit (one commit per skill touched, staged-file count checked), push the branch. Do not open a PR automatically and do not merge.
7. Run `py -3 tools/vault_lint.py` (0 errors required), then commit and push the vault review note: `skill-drift: <YYYY-MM> — N findings, branch drift/YYYY-MM` (or no commit on a no-op). The `skill-drift:` prefix is the heartbeat.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read skills, vault, config-repo git log | Read-only. |
| One review note per run in `06-insights/` | Standard template; every finding quoted. |
| Create + push a `drift/YYYY-MM` branch in the config repo | Proposals only; never merge; never touch `main`. |
| Commit/push the vault review note | `skill-drift:` prefix, staged-count discipline. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Editing anything on the config repo's `main` | The whole point is propose-only. |
| Merging or deleting any branch | Merging is Jesse's act; branch deletion is hard-banned vault-wide. |
| Changing vault content beyond the review note | Other loops own the vault layers. |
| More than one drift branch outstanding | If last month's `drift/` branch is unmerged, fold new findings into a fresh review note but flag the stale branch instead of stacking a second one. |

## Stop Conditions

Stop and report when: config-repo working tree is dirty or mid-operation; a prior `drift/` branch is unmerged (report findings, flag the backlog, skip branch creation); a finding requires domain knowledge the loop cannot verify from files (list it as an open question in the review note rather than proposing a guess).

## Success Criteria

A successful run either delivers a review note + branch that lets Jesse apply a month of skill corrections in one merge, or cleanly reports the skills are in sync. Proposing an edit without quoted evidence, touching `main`, or letting proposal branches accumulate unmerged without flagging are failures.
