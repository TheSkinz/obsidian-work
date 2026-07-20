---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-07-20
review_after: 2026-10-20
related:
  - [[project-harness-audit-2026-07]]
  - [[project-vault-five-loop-system]]
  - [[project-usadebusk-claude-arch]]
tags: [reference, harness, knowledge-system, skills, config]
---

# Harness Map — 2026-07-20

Complete inventory of every surface that shapes a response before a prompt is
typed, built from live recon (not inference) of `~/.claude` and the vault.
Baseline for future harness-hygiene passes. Prompted by the "I Overbuilt My AI
Harness" video (youtu.be/PDJfciNhyHU) — six-rule framing applied to this setup.

Verification basis: `find`/`grep` across `~/.claude/skills`, `~/.claude/plugins`,
`settings.json`, memory dir, and `01-context/` on 2026-07-20. Sizes in chars.

## 1. The whole system, one screen

| Surface | Where | Loads when | Weight | Type |
|---|---|---|---|---|
| Global CLAUDE.md | `~/.claude/CLAUDE.md` | Every session, every project | ~4 KB | Prose |
| Vault CLAUDE.md | `obsidian-work/CLAUDE.md` | Every session in this vault | ~2.6 KB | Prose |
| Memory index | `…/memory/MEMORY.md` | Every session (this project) | 32 entries | Prose |
| **01-context/** (7 files) | `obsidian-work/01-context/` | **Every session — "read every file before responding"** | **21 KB** | Prose (eager) |
| 9 skills | `~/.claude/skills/` | On-demand / description-triggered | 4.5–24 KB each | Prose (deferred) |
| Stale skill snapshot | app-side (account-level, NOT on disk) | Surfaced every session in listing | ~18 shadow rows | Prose (dead) |
| git-guard hook | `~/.claude/hooks/usadebusk-git-guard.mjs` | Every Bash call (PreToolUse) | — | **Lock** |
| Permissions | `settings.json` | Every tool call | 9 allow / 11 deny | **Lock** |
| vault_lint.py | `obsidian-work/tools/` | Loop runs / manual | 9 rules | **Lock** |
| Health dashboard | `50-dashboards/health.md` | Read at session start | FAIL rows | **Lock-ish** |
| 4 scheduled loops | `~/.claude/scheduled-tasks/` | Cron (Mon / nightly / monthly) | — | Automation |

Skill body sizes (`~/.claude/skills/`, chars): adversarial-review 18810,
idea-triage 4502, usadebusk-core 14074, usadebusk-equipment 9820,
usadebusk-estimating 23276, usadebusk-fieldpm 13141, usadebusk-ops 5328,
usadebusk-sop 15618, usadebusk-vault-ingest 24322.

01-context per file (chars): system-workflow-reference 7431, output-preferences
3826, estimating-approach 2672, workflow-map 2409, equipment-fleet 1923,
company-context 1486, active-jobs 1255. Total 21002.

## 2. Locks vs. prose — the distinction that carries weight (video rule 5)

Real teeth already in place (a machine enforces, can refuse): the git-guard
hook, the 11 deny-permissions, `vault_lint.py`'s 9 rules, the `superseded_by:`
frontmatter convention, health-dashboard FAIL gating.

Prose (polite reminders, no enforcement): both CLAUDE.mds, all 32 memories, all
9 skill bodies, all of 01-context.

Rule-5 candidates — prose that could become a lock:
- **"Check staged file count before every commit"** (global CLAUDE.md) — a yes/no
  machine check living as a reminder. A PreToolUse hook on `git commit` could
  enforce it instead of relying on the model remembering.
- **Heater-card Task-Durations column order** — if `vault_lint.py` does not already
  assert the exact `Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over |
  Rig-Out | Stand-By | Total` header, that is the highest-value lock to add
  (see collision #3 below).

## 3. Rule collisions — one rule, several homes (video rule 3)

The real drift risk. Each row is a single rule living in 2+ places that can fall
out of sync.

| Rule | Homes | Status |
|---|---|---|
| Output/formatting prefs | Global CLAUDE.md "Output" §  +  `01-context/output-preferences.md`  +  vault CLAUDE.md pointer | Overlapping prose; two authorities |
| Git authority/bans | Global CLAUDE.md "Git guard" §  +  "Vault commit/push authority" §  +  the hook  +  `knowledge-system-governance.md` policy | 4 homes: 2 prose + 1 lock + 1 doc |
| Heater Task-Durations schema | `_canonical-heater-card.md` (exemplar)  +  vault CLAUDE.md (inlines the columns)  +  `usadebusk-vault-ingest` skill | Triple — CLAUDE.md says "full spec lives in the exemplar and the skill," then restates it anyway |
| Estimating / condition-matched actuals | `feedback-condition-matched-actuals` memory  +  `usadebusk-estimating` skill  +  `01-context/estimating-approach.md` | 3 homes across memory / skill / eager |
| fieldpm ↔ ops receipt boundary | live fieldpm desc + live ops desc (agree, cross-reference — good)  vs.  stale app-side snapshot (has neither) | Live-vs-dead, not live-vs-live |

Positive example to replicate: the **SOP formatting standard**. Vault CLAUDE.md
names one home (`04-knowledge/sops/sop-formatting-standard.md`) and makes every
other mention a pointer. That is rule 3 done right.

## 4. Eager-load audit (video rule 4)

`01-context/` (21 KB) is read on every session regardless of task. A pure
estimating question still pulls in `equipment-fleet.md`, `active-jobs.md`, and
`system-workflow-reference.md` (7.4 KB, the largest). Strongest
demote-to-on-demand candidates: `system-workflow-reference.md` +
`workflow-map.md` (~10 KB combined) — reference material, not per-response
context.

## 5. The stale app-side snapshot (verified, not on disk)

`grep obsidian-usadebusk` across `~/.claude` hits only history/plans/paste-cache
— never a live skill or config file. The only on-disk plugin,
`document-skills@anthropic-agent-skills`, is `enabledPlugins: false`. Therefore
the `anthropic-skills:usadebusk-*` rows in the skill listing come from
account-level skills uploaded through the Claude web/desktop app, not from
`~/.claude` or `settings.json`. Confirmed on-disk frontmatter matches the *bare*
listing exactly; the `anthropic-skills:` text is the older pre-boundary version.

This was open item #1 from [[project-harness-audit-2026-07]] (logged 2026-07-06).
**RESOLVED 2026-07-20.** Located at claude.ai › Settings › Capabilities › Skills
(the "Author: You" rows — 9 uploads: 7 usadebusk-*, adversarial-review,
idea-triage; the fieldpm upload was dated 3/25/26, matching the stale-party date
from the July audit). Jesse deleted all nine; live `~/.claude/skills/` copies are
untouched. **Confirmed** in a fresh session (2026-07-20): no `anthropic-skills:*`
duplicates remain; the seven auto-invocable skills show as bare local names.

Side finding worth keeping: the two command-only skills — `idea-triage` and
`usadebusk-vault-ingest`, both carrying `disable-model-invocation: true` locally —
correctly drop OUT of the fresh session's model-invocation listing (they invoke by
command: `/idea-triage`, `/usadebusk-vault-ingest`). The deleted account copies
LACKED that flag, so the stale snapshot had been surfacing these two into the
model's auto-invocation surface against Jesse's intent. Deleting it restored the
command-only behavior — the cleanup fixed a subtler override bug, not just cosmetic
duplication.

## Follow-up actions (all gated, none auto-applied)

1. ~~Clear the stale account-level snapshot in the Claude app UI.~~ **DONE 2026-07-20.**
2. ~~Heater Task-Durations: cut the inlined columns from vault CLAUDE.md.~~ **DONE
   2026-07-20** (commit `56bdb0b`). The inline copy was already stale — 10 columns,
   missing `Condition` — vs. the exemplar's and the skill's 11. Replaced with a
   pointer to the exemplar. Also fixed two more stale inline counts in the same file
   (`vault_lint.py` "7 rules" → 9). A `vault_lint.py` header-order lock remains an
   optional future enhancement (not built).
3. Output-prefs and git-authority collisions:
   - **Output-prefs DONE 2026-07-20** (commit `2d0d23f`). Jesse chose global
     CLAUDE.md as the single home; `output-preferences.md` now points up instead of
     restating the rules.
   - **Git-authority: intentionally left as-is.** The hard bans in both global
     CLAUDE.md and `knowledge-system-governance.md` are a safety summary (always
     loaded) + detail (on-demand), not harmful drift. Deduping a safety rule off the
     always-loaded surface would be a downgrade. Reviewed, no change.
4. ~~Demote `system-workflow-reference.md` + `workflow-map.md` from eager to
   on-demand.~~ **DONE 2026-07-20** (commit `56bdb0b`). Both self-describe as
   reference/history; startup rule and their Layer headers updated. ~10 KB off every
   session's eager load.
