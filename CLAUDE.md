# CLAUDE.md — Vault Entry Point

**Scope.** USADeBusk operational knowledge, expanding to include personal and LLM-knowledge layers. The vault is no longer USADeBusk-only — treat new top-level domains as expected, not anomalies.

**Session startup.** Read every file in `01-context/` before responding. Load `02-facilities/` and `04-knowledge/` on demand only when named. Do not auto-load `archive/`, `templates/`, or `tools/`. Check `50-dashboards/health.md` and surface any red (FAIL) rows — a lint error or an overdue loop heartbeat — before starting other work; if it shows review notes awaiting decision, mention them and offer to walk through them (Jesse doesn't track triggers — the dashboard is how pending work reaches him). `INDEX.md` is a generated one-line-per-note map of the vault — consult it before claiming something isn't in the vault.

## Folder structure (post-cleanup)

- `00-inbox/` — capture and triage
- `01-context/` — auto-loaded by Cowork: `active-jobs`, `company-context`, `equipment-fleet`, `estimating-approach`, `output-preferences`, `system-workflow-reference`, `workflow-map`
- `02-facilities/` — heater cards and facility overviews, canonical schema
- `04-knowledge/` — concepts, equipment, SOPs
- `06-insights/` — session insights and reviews
- `07-llms/` — LLM platforms, tools, best practices (per-platform + cross-platform)
- `08-systems/` — hardware, software, OS config, dev environment
- `09-interests/` — personal topics, research interests, non-work knowledge
- `50-dashboards/`
- `archive/`, `templates/`
- `tools/` — vault automation scripts: `vault_lint.py` (7 rules incl. ORPHAN), `vault_health.py` → `50-dashboards/health.md`, `vault_index.py` → `INDEX.md`, `estimating_rollup.py` → `04-knowledge/estimating-actuals-rollup.md`

Root-level files: `change-log.md` (decisions-only log), `INDEX.md`, `Identity.md`. `03-jobs/` and `05-projects/` are gone. Do not reference or recreate them — job actuals now live inside heater cards.

## Schema authority

`04-knowledge/_canonical-heater-card.md` is the exemplar. `templates/_heater-template.md` derives from it. All heater cards conform to it.

Task Durations table (actuals only) — full spec lives in the exemplar and the `usadebusk-vault-ingest` skill:

`Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total`

## Output

Formatting and session-mode rules live in `01-context/output-preferences.md`. The **SOP formatting standard** has one canonical home: `04-knowledge/sops/sop-formatting-standard.md` — not here and not in a skill. The `usadebusk-sop` skill governs SOP *content* and explicitly defers formatting to that file; anything else that mentions SOP formatting points at it.
