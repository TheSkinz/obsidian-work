# CLAUDE.md — Vault Entry Point

**Scope.** USADeBusk operational knowledge, expanding to include personal and LLM-knowledge layers. The vault is no longer USADeBusk-only — treat new top-level domains as expected, not anomalies.

**Session startup.** Read every file in `01-context/` before responding. Load `02-facilities/` and `04-knowledge/` on demand only when named. Do not auto-load `archive/`, `templates/`, `_RAW/`, `_COMPILED_WIKI/`, or `_OUTPUTS/`. Check `50-dashboards/health.md` and surface any red (FAIL) rows — a lint error or an overdue loop heartbeat — before starting other work.

## Folder structure (post-cleanup)

- `00-inbox/` — capture and triage
- `01-context/` — auto-loaded by Cowork: `active-jobs`, `company-context`, `equipment-fleet`, `estimating-approach`, `output-preferences`, `workflow-map`
- `02-facilities/` — heater cards and facility overviews, canonical schema
- `04-knowledge/` — concepts, equipment, SOPs
- `06-insights/` — session insights and reviews
- `07-llms/` — LLM platforms, tools, best practices (per-platform + cross-platform)
- `08-systems/` — hardware, software, OS config, dev environment
- `09-interests/` — personal topics, research interests, non-work knowledge
- `50-dashboards/`
- `archive/`, `templates/`

`03-jobs/` and `05-projects/` are gone. Do not reference or recreate them — job actuals now live inside heater cards.

## Schema authority

`04-knowledge/_canonical-heater-card.md` is the exemplar. `templates/_heater-template.md` derives from it. All heater cards conform to it.

Task Durations table (actuals only) — full spec lives in the exemplar and the `usadebusk-vault-ingest` skill:

`Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total`

## Output

Formatting and session-mode rules live in `01-context/output-preferences.md`. The **SOP formatting standard** has one canonical home: `04-knowledge/sops/sop-formatting-standard.md` — not here, not in a skill, not in `AGENTS.md`. The `usadebusk-sop` skill governs SOP *content* and explicitly defers formatting to that file; anything else that mentions SOP formatting points at it.
