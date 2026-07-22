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

**Companion (usage side):** this note inventories what *shapes* a response;
[[command-reference]] (2026-07-22) is the "which command to reach for, when, and how
to fire it" lookup — including native built-ins like `/goal` that live in the harness
binary and never appear in the skills list.

**Visual snapshot:** `2026-07-20-harness-panel.html` (this folder) — a consolidated
one-screen panel of the same data: load sequence, composition, and the collision
ledger. Open in a browser (Obsidian reading view sanitizes its layout). Frozen
snapshot, not a live view; regenerate from this note if the harness changes. Also
published as an artifact: https://claude.ai/code/artifact/0b658200-ab6b-4943-8a4e-b9d76dc7a4b4

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
  Rig-Out | Stand-By | Total | Condition` header, that is the highest-value lock to add
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

## 6. Harness passport — core vs. delivery (added 2026-07-20, exploration session)

Cross-model porting exploration produced one organizing lens: split every surface
into a model-agnostic **core** (portable — identity, domain facts, output prefs,
the *intent* of the permission boundary) and a product-specific **delivery layer**
(how the core is injected and, crucially, *enforced*). Porting the harness to
another surface (video rule 6) means copying the core verbatim and re-authoring the
delivery — never copying the whole thing.

The locks split a second way that decides which safety survives a port:

- **Product-independent locks** — `vault_lint.py`, `estimating_rollup.py`. Pure
  scripts that run on the files regardless of which model edited them. Already
  "ported" — they don't move. The reusable principle: push enforcement into a
  script and it survives every port for free.
- **Product-coupled locks** — the git-guard hook, the permission allow/deny lists.
  Bound to the agent runtime; re-authored per product, and not every product can
  host them.

| Surface | Core / Delivery | Port note |
|---|---|---|
| Global + vault CLAUDE.md | Core (facts) in delivery (prose) | Facts port; prose style is Opus-tuned, re-author per model |
| 32 memories | Core | Portable facts; frontmatter is delivery-specific |
| 01-context/ (eager) | Core, delivered eagerly | Eager-load mechanism is product-specific |
| 9 skills | Core content, product-specific packaging | Concept ports; format re-authored |
| git-guard hook | Delivery (product-coupled lock) | Re-author per runtime |
| Permissions allow/deny | Delivery (product-coupled lock) | Intent ports; syntax differs |
| `vault_lint.py` / `estimating_rollup.py` | Delivery (product-*independent* lock) | Runs unchanged — already ported |

### Live-surface port findings (web-verified 2026-07-20)

Targets confirmed in active use: Claude Code (baseline), **Codex**, **Copilot
M365**. Local models and Gemini out of scope.

**Codex** is near-isomorphic to Claude Code. `AGENTS.md` maps ~1:1 to CLAUDE.md
(global `~/.codex/AGENTS.md` + a path-chain from git-root to cwd, closer wins);
Codex now has both **hooks** (`hooks.json` / `[hooks]` in config.toml, stable since
v0.124.0) and **skills**, so the git-guard hook and skill suite genuinely port. Two
caveats: AGENTS.md takes **no YAML frontmatter** (provenance conventions are
CLAUDE.md-only), and GPT/o-series is more literal and less tolerant of long nuanced
prose than Opus — so the prose CLAUDE.md and the eager 01-context load should
**shrink and harden into imperatives**, not copy across. The USADeBusk half of the
harness only needs porting if Codex actually touches vault/USADeBusk work; if it is
generic-coding-only, only the generic slice of global CLAUDE.md belongs in
`~/.codex/AGENTS.md`. Sources: developers.openai.com/codex (agents-md, config-reference, skills).

**Copilot M365** ports the core but none of the locks. Base Copilot has no authored
persistent system prompt; the port vehicle is a **declarative agent** built in
**Agent Builder** (no-code, in-UI) carrying instructions + knowledge grounding +
actions. What ports: identity, output prefs, the permission boundary rephrased
behaviorally ("draft, never send"), plus a genuine *gain* — Microsoft Graph
grounding against real tenant mail/files, which Claude Code lacks. What does not
port: every lock (no hooks, lint, deny-lists, or frontmatter) — enforcement
collapses to prose, and the honest design accepts that rather than faking safety
machinery. Unknown to check, not assume: whether USADeBusk IT permits building
declarative agents at all. Source: learn.microsoft.com/microsoft-365/copilot/extensibility.

## 7. Pre-write skill design checklist (added 2026-07-20)

Prevention counterpart to the skill-drift loop (which catches collisions *after*
skills exist). Before writing or materially expanding a skill, run this against the
map above — it heads off the rule-collision class in section 3:

1. **Does this rule already have a home?** Check the collision ledger (§3) and
   INDEX first. If it lives somewhere, point at it — do not restate it.
2. **Which single surface should own it?** One rule, one home (video rule 3). Skill
   body, CLAUDE.md, memory, or a lock — pick one; everything else references it.
3. **Core or delivery?** If it is a portable fact, it may belong in a memory or
   CLAUDE.md, not baked into one skill's prose.
4. **Eager or on-demand?** Skills are deferred by design — keep task-specific depth
   in the skill, not in eager 01-context (video rule 4).
5. **Could a hard rule be a lock instead of prose?** If it is a yes/no check, prefer
   `vault_lint.py` or a hook over a reminder (video rule 5).
