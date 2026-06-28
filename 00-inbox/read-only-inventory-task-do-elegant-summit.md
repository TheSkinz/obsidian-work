# Claude / AI System Configuration Snapshot

**Generated:** 2026-06-11 · **Machine:** Windows 11, user `Jwuts` · **Mode:** read-only inventory (nothing modified)

> **Superseded (partial) 2026-06-15:** Sales & Proposals project dissolved; proposal authority relocated to `usadebusk-estimating` skill (config-repo commit `025578c`). Lines 118, 122, 187, 192 of this snapshot describe the prior state and are now stale. All other content reflects 2026-06-11 state.

This is a deliverable report, not an implementation plan. The task is fully read-only and complete as written below. No system changes are proposed.

---

## 1. Global CLAUDE.md

**`C:\Users\Jwuts\.claude\CLAUDE.md`** — EXISTS (66 lines). This is the deployed global instruction file, loaded every session. Full contents:

Sections: Who I Am · How Claude Should Work With Me · Output Formatting · Session Mode Inference · Vault Reference · Skills · Hard Constraints · Model Behavior · Goal-Driven Execution.

Key content: Identity (Jesse, PM/field supervisor, USADeBusk; DSP#=quotes, USA#=awarded, format YYNNN). Behavior rules (push back, ask one clarifying question before building, verify approach, stop after two same-class failures, flag more-efficient paths). Output formatting (concise, no bullets in prose, no excessive headers, no emojis, no preamble/summary). Session-mode inference (Research/Brainstorming/Implementation/Writing). Vault reference (vault CLAUDE.md governs formatting, system prompts govern behavior). Skills routing table. Hard constraints (don't modify finalized docs, git commits autonomous, anything touching `C:\Users\Jwuts\USADEBUSK\` needs confirmation, config repo `github.com/TheSkinz/claude-config`). Model behavior (medium default, high for complex, never xhigh unless asked). Goal-driven execution (convert imperatives to verifiable goals).

**Other CLAUDE.md files found (15 total across the machine):**

| Path | Role |
|---|---|
| `.claude\CLAUDE.md` | **Primary deployed global** (above) |
| `claude-config\CLAUDE.md` | Repo source — **DRIFTED**: shorter/older, missing Output Formatting, Session Mode Inference, Vault Reference, Model Behavior sections and the config-repo line. Last CHANGELOG entry 2026-05-12. |
| `OneDrive\obsidian-usadebusk\CLAUDE.md` | Vault entry point (see §4) |
| `claudeworkspace\obsidian-usadebusk\CLAUDE.md` | Duplicate vault copy |
| `obsidian-usadebusk\CLAUDE.md` | Duplicate vault copy |
| `OneDrive\Documents\obsidian-usadebusk\CLAUDE.md` | Duplicate vault copy |
| `OneDrive\Documents\obsidian-usadebusk1\CLAUDE.md` | Duplicate vault copy (note `1` suffix) |
| `OneDrive\Desktop\AI Workflow and Master Docs\CLAUDE.md` | Separate workspace |
| `OneDrive\Desktop\Active Work\CLAUDE.md` | Separate workspace |
| `OneDrive\Documents\GitHub\MassGen\CLAUDE.md` | Unrelated project |
| `claudeworkspace\claude-obsidian\CLAUDE.md` | Plugin workspace |
| `claude-config\... / .claude\plugins\... / .grok\... / .codex\...` | Plugin/cache copies (obsidian marketplace) |

There are **at least 5 copies of the USADeBusk vault** on this machine (OneDrive, OneDrive\Documents x2, claudeworkspace, bare `obsidian-usadebusk`). This is a sync/source-of-truth hazard worth resolving separately.

---

## 2. Claude Code Config

**`C:\Users\Jwuts\.claude\settings.json`** — EXISTS. Full contents:

```json
{
  "enabledPlugins": {
    "document-skills@anthropic-agent-skills": true,
    "claude-obsidian@claude-obsidian-marketplace": true
  },
  "extraKnownMarketplaces": {
    "anthropic-agent-skills": { "source": { "source": "git", "url": "https://github.com/anthropics/skills.git" } },
    "claude-obsidian-marketplace": { "source": { "source": "github", "repo": "AgriciDaniel/claude-obsidian" } }
  },
  "theme": "dark",
  "agentPushNotifEnabled": true
}
```

- **MCP servers:** none user-configured. `~/.claude.json` has `"mcpServers": {}` (empty). The MCP servers visible at runtime (computer-use, Claude_in_Chrome, Claude_Preview, ccd_*, mcp-registry, scheduled-tasks, etc.) are injected by the Claude desktop/Cowork app environment, not from your config files.
- **Custom commands:** `.claude\commands\` does **not exist** — no user-defined slash commands. All slash commands available (`/code-review`, `/loop`, `/schedule`, `/verify`, etc.) come from installed plugins, not local definitions.
- **Hooks:** `.claude\hooks\` does **not exist**. No user hooks in `settings.json`. (Plugin-level hooks exist inside `.claude\plugins\...\hooks\hooks.json` for the obsidian and official marketplaces, but you have not authored any.)
- **Subagents:** none defined by you. Agent meta-files under `.claude\projects\...\subagents\` are runtime session artifacts, not configured agents.
- **Permissions:** no `permissions` block in `settings.json` — running on defaults.
- **Plugins enabled:** `document-skills` (Anthropic agent skills) and `claude-obsidian`. Two extra marketplaces registered (anthropics/skills, AgriciDaniel/claude-obsidian). Plus the official marketplace cache holds many external plugin definitions (asana, github, linear, playwright, discord, telegram, etc.) — registered/cached but not enabled.

---

## 3. Skills

**Deployed at `C:\Users\Jwuts\.claude\skills\`** (8 skill files):

| Skill | Present | Frontmatter version line? |
|---|---|---|
| usadebusk-core | ✅ | No version line — frontmatter is `name` + `description` only |
| usadebusk-equipment | ✅ | No version line |
| usadebusk-estimating | ✅ | No version line |
| usadebusk-fieldpm | ✅ | ✅ present (loads from a binary/zipped SKILL — listed in runtime skill registry) |
| usadebusk-ops | ✅ | No version line |
| usadebusk-sop | ✅ | No version line |
| usadebusk-vault-ingest | ✅ | No version line |
| adversarial-review | ✅ | (utility skill, not USADeBusk) |

**The six core USADeBusk skills are all present** (core, equipment, estimating, fieldpm, ops, sop), plus a 7th USADeBusk skill: **usadebusk-vault-ingest**. A parallel copy of these skills lives in `claude-config\skills\` (the git repo source) — note that copy is **missing `usadebusk-vault-ingest`**, so the repo and deployed `.claude\skills` have drifted.

**No skill carries a `version:` line in frontmatter.** Versioning is tracked externally in `claude-config\CHANGELOG.md` (only one entry: 2026-05-12). Section headers per skill:

- **usadebusk-core:** Company Identity · Brand Standards · Document Numbering · What Furnace Decoking Is · Core Terminology · Fired Heater & Tube Knowledge · Customer-Side Contacts (Typical)
- **usadebusk-equipment:** TriMax Pumper Unit · Filter Press · 4×3 Centrifugal Pump · Pig Launchers/Receivers · Pig Types · Hoses & Connections · Support Equipment · Dual Pumper Configuration
- **usadebusk-estimating:** Primary Estimating Drivers · Duration Model · Pricing Structure · Baseline Rate Table · Cost Categories · Heater Card Format · RFQ Intake · Proposal Document Structure · Estimation Workup Tool · DSP# Assignment · Submission Platforms · Customer Types
- **usadebusk-sop:** Full Decoking Sequence · Flow Path · Looped Circuit · Cleaning Completion Criteria · Smart Pig/ILI · SOP Document Structure · Operating Parameters Table · SOP Variants · Required Inputs · Pre-Execution Technical Package · Process Flow Diagram Output · Jumper Spool Documentation · Role Boundaries · Behavior Rules
- **usadebusk-ops:** Service Receipt · Ticket Breakdown File · Receipt Extraction Process · Plant Down Time (PDT) · Invoice Readiness Check · Job Filing
- **usadebusk-vault-ingest:** Dependencies · Purpose · Environment Setup · Commands · Vault Schema · City-State Naming · Document Type Detection · DSP Ingestion Logic · Tube Geometry Conflict Detection · Heater Card Template · Routing Inference · Collision & Revision Handling · Frontmatter Template · Dry-Run Output · Confidence Scoring · Conversion Rules · Failure Modes · Behavior Rules

---

## 4. Obsidian Vault

**Root: `C:\Users\Jwuts\OneDrive\obsidian-usadebusk`** — EXISTS.

**Folder-by-folder count (.md files, recursive):**

| Folder | Count |
|---|---|
| 00-inbox | 3 |
| 01-context | 6 |
| 02-facilities | 60 |
| 03-jobs | 106 |
| 04-knowledge | 9 |
| 05-projects | 29 |
| 06-insights | 1 |

**03-jobs: 106 notes. 02-facilities: 60 notes.**

### Full dump — `01-context\` (auto-loads every session)

**`output-preferences.md`** — Governs formatting (authority: this file governs formatting, system prompts govern behavior). Response formatting: concise by default, no bullets in prose, no excessive headers, no emojis, no preamble/summary, no hedged disagreement. Session-mode inference: Research / Brainstorming / Implementation / Writing-editing / Spreadsheets. Pre-build rules: confirm terminology, verify environment, ask one clarifying question on ambiguity, stop after two same-class failures, flag more-efficient paths, maintainability > error handling. Uncertainty handling. Document output points to CLAUDE.md SOP standard.

**`company-context.md`** — Source: Master Reference Module 1. Identity (USADeBusk / USA DeBusk / DeBusk Services Group; Furnace Decoking; Deer Park TX base). Key people (Jesse jutsey@usadebusk.com; Jason VP). Document numbering (DSP# YYNNN quotes / USA# job). Commercial defaults (T&M + Mob/Demob lump sum ~95%; third-party markup 10% baseline, some 5%; ARIBA/GED/email). Brand standards table (Arial; H1 13pt bold #222222 with gold #FCC30A border; H2 11pt #FCC30A; body 10pt #555555; table header fill #222222; alt row #F7F7F7; callout #FFFBE6).

**`estimating-approach.md`** — Source: Sales & Proposals system prompt v2.0 + usadebusk-estimating skill. Commercial structure (T&M execution / Lump Sum mob-demob; markup contract-specific). Duration calculation (baseline 100 ft/hr per pass; adjust for coker/crude/pitch/hard fouling/tight ID; rig-in 6h, rig-out 6h, smart pig 4h; 12-hr shifts, pigging 24/7). Equipment profile (1x/2x/3x TriMax table). Pricing rules. Proposal document structure (12–16 pages, 14-section order; doc number DSP##### YYYY-MM).

**`equipment-fleet.md`** — Frontmatter `type: context`. Home base Deer Park TX. Pumping units table: TriMax 1–6 (Triple Pumpers, each paired with Support 1–6, travel as a set); Double 1–2 (Sea-Can Double Pumpers, overseas/special ~1x/year). Mob distance measured from Deer Park unless staged.

**`workflow-map.md`** — Active projects (Obsidian Vault Build — active, 43 facilities scaffolded, Marathon Garyville built, DSP26058 ingested). Paused/deferred (LLM KB/Wiki, Git version control, iPhone shortcut, SOP→diagram pipeline, Gemini CLI adapter). Claude Projects deployed (Sales & Proposals v2.0, Technical Docs v2.1, Operations & Admin v2.0, Field Execution). Open architecture decisions. Recently completed (Valero Port Arthur USA26025, Outlook email security, Claude architecture 6 skills, GDrive architecture).

**`active-jobs.md`** — Active: none. Recently completed: USA26025 Valero Port Arthur. Awarded/pre-execution: none. Pending/bidding: DSP26058 Marathon Garyville $508,518.10 (valid through 2026-11-12); DSP26039 ExxonMobil Baytown $76,873.00 (valid through 2027-04-07).

### Filenames — `04-knowledge\` (9)
concepts: estimating-pricing.md · field-operations.md · industry-foundation.md · process-flow.md · quote-lifecycle.md · equipment: equipment-library.md · pricing: _cost-model.md · Rate Reference.md · sops: sop-formatting-standard.md

### Filenames — `05-projects\` (29)
system-prompts: field-execution · operations-admin · sales-proposals · technical-docs (each `system-prompt.md`). operations-admin also has onedrive-company-structure.md, onedrive-facilities-structure.md. sales-proposals has _pipeline.md, _revenue.md plus DSP proposal files by client: Cenovus DSP25113 · CITGO DSP25012 · ExxonMobil DSP25084/DSP26005/DSP26012/DSP26039 · Flint-Hills DSP26006 · Formosa DSP25156 · HF-Sinclair DSP25142 · Hunt DSP24144 · Marathon DSP24021/DSP25021/DSP26019/DSP26058/DSP26058-r2 · ONEOK DSP25079 · P66 DSP25135 · PBF DSP25141 · Suncor DSP25099 · Valero DSP25138 · Westlake DSP25103.

### Filenames — `06-insights\` (1)
insights-log.md

---

## 5. Cowork Instructions

**Not recoverable from disk as readable instructions — UI-only, capture manually.**

Searched all `*owork*` paths. What exists on disk: `cowork-gb-cache.json`, `cowork-clientdata-cache.json`, `cowork-enabled-cli-ops.json`, and log files. The `cowork-gb-cache.json` contains only GrowthBook **feature flags** (experiment toggles like `tengu_*`), not your Global or Folder Instructions. No file on disk holds the text of Cowork Global Instructions or Folder Instructions. **Capture these manually from the Cowork UI** if you want them inventoried.

---

## 6. Duplication Scan — the Context-Tax Map

Every instruction/context block that appears in more than one context-loading surface. Surfaces compared: deployed global `CLAUDE.md`, `claude-config\CLAUDE.md`, vault `CLAUDE.md`, the six `01-context\` files, USADeBusk skill bodies, `04-knowledge\`, `05-projects\` system-prompts.

**A. Output formatting rules** (concise / no bullets in prose / no excessive headers / no emojis / no preamble-summary / direct correction) — **3+ places, near-verbatim:**
- global `CLAUDE.md` § Output Formatting
- vault `CLAUDE.md` § Output Preferences
- `01-context\output-preferences.md` § Response formatting

**B. Session-mode inference** (Research / Brainstorming / Implementation / Writing) — **3 places:**
- global `CLAUDE.md` § Session Mode Inference
- vault `CLAUDE.md` § Output Preferences > Session modes
- `01-context\output-preferences.md` § Session mode inference

**C. Working-style / pre-build rules** (push back, ask one clarifying question first, verify approach, two-failures-then-stop, flag more-efficient path) — **4 places:**
- global `CLAUDE.md` § How Claude Should Work With Me
- `claude-config\CLAUDE.md` § How Claude Should Work With Me (subset)
- vault `CLAUDE.md` § Output Preferences > Before building anything
- `01-context\output-preferences.md` § Pre-build rules + Uncertainty handling

**D. Identity + document numbering** (Jesse PM; DSP#=quote / USA#=job; YYNNN) — **4 places:**
- global `CLAUDE.md` § Who I Am
- `claude-config\CLAUDE.md` § Who I Am
- `01-context\company-context.md` § Document numbering
- `usadebusk-core` skill § Document Numbering

**E. Skills routing table** (load usadebusk-core + domain skill) — **2 places, identical:**
- global `CLAUDE.md` § Skills
- `claude-config\CLAUDE.md` § Skills

**F. Brand standards** (Arial; gold; charcoal #222222; table header fill; alt rows) — **4 places — AND A CONFLICT:**
- `01-context\company-context.md` § Brand standards — gold = **#FCC30A**
- vault `CLAUDE.md` § SOP Formatting Standard — gold = **#F5A623**
- `usadebusk-core` skill § Brand Standards
- `04-knowledge\sops\sop-formatting-standard.md`
⚠ The two gold hex values disagree (#FCC30A vs #F5A623). One is wrong. Pick a single source of truth.

**G. Commercial defaults / estimating model** (T&M + lump-sum mob-demob ~95%; markup 10%/5%; 100 ft/hr; rig-in/out 6h) — **4–5 places:**
- `01-context\estimating-approach.md`
- `01-context\company-context.md` § Commercial defaults
- `usadebusk-estimating` skill § Duration Model / Pricing Structure
- `04-knowledge\concepts\estimating-pricing.md` (by title)
- `05-projects\sales-proposals\system-prompt.md` (estimating-approach.md cites it as a source)

**H. Proposal document structure** (12–16 pages, section order) — **3 places:**
- `01-context\estimating-approach.md` § Proposal document structure
- `usadebusk-estimating` skill § Proposal Document Structure
- `05-projects\sales-proposals\system-prompt.md`

**I. SOP formatting / structure** — **4 places, one explicitly marked superseded:**
- vault `CLAUDE.md` § Document Output: SOP Formatting Standard (governing)
- `04-knowledge\sops\sop-formatting-standard.md`
- `usadebusk-sop` skill § SOP Document Structure
- `05-projects\technical-docs\system-prompt.md` (vault CLAUDE.md explicitly calls this "aspirational" / replaced)

**J. Authority / conflict-resolution rule** ("vault wins on formatting, system prompts win on behavior") — **3 places:**
- global `CLAUDE.md` § Vault Reference
- vault `CLAUDE.md` § Conflict Resolution
- `01-context\output-preferences.md` header (Authority line)

**K. Equipment / TriMax configuration** — **4 places:**
- `01-context\equipment-fleet.md`
- `01-context\estimating-approach.md` § Equipment profile
- `usadebusk-equipment` skill
- `usadebusk-estimating` skill (config table)

**L. Job status / active-work tracking** — **2 places, overlapping:**
- `01-context\workflow-map.md`
- `01-context\active-jobs.md`
Both track USA26025, DSP26058, DSP26039 — the "recently completed / pending" lists overlap.

**Highest-tax items:** A, B, C, D, F, G each repeat 3–4× across global CLAUDE, vault CLAUDE, and 01-context — meaning your formatting + behavior + identity + commercial rules load two-to-three times every USADeBusk session. The 01-context files themselves cite the skills/system-prompts as their "Source," confirming the duplication is by-derivation, not accident. Consolidating to one canonical location per rule (with the others pointing to it) would cut the per-session context tax materially.

---

## Gaps / Couldn't Access

- **Cowork Global/Folder Instructions:** not on disk in readable form (UI-only). Manual capture required.
- **Skill versions:** no `version:` line in any skill frontmatter; `claude-config\CHANGELOG.md` has a single entry (2026-05-12), so per-skill version history is effectively untracked.
- **Config drift, unverified direction:** deployed `.claude\CLAUDE.md` is fuller than `claude-config\CLAUDE.md` repo source, and `.claude\skills` has `usadebusk-vault-ingest` while `claude-config\skills` does not. Which is canonical is undetermined from files alone.
- **Vault copies:** 5+ copies of `obsidian-usadebusk` exist across OneDrive / Documents / claudeworkspace. Only the OneDrive root was dumped (per request); the others were not compared for divergence.
- **04-knowledge / 05-projects file *contents*:** listed by filename only (per request); overlap claims G–K for those files are inferred from titles + the explicit "Source:" citations in the 01-context files, not a full line-by-line diff.
- **`usadebusk-fieldpm` skill body:** loads from a packaged/zipped SKILL in the runtime registry; its section headers were not extracted from the deployed `.claude\skills` copy (only its presence and frontmatter were confirmed).
