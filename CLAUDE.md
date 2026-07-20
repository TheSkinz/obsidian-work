# CLAUDE.md — Vault Entry Point

**Scope.** USADeBusk operational knowledge, expanding to include personal and LLM-knowledge layers. The vault is no longer USADeBusk-only — treat new top-level domains as expected, not anomalies.

**Session startup.** Read every file in `01-context/` before responding. Load `02-facilities/` and `04-knowledge/` on demand only when named. Do not auto-load `archive/`, `templates/`, or `tools/`. Check `50-dashboards/health.md` and surface any red (FAIL) rows — a lint error or an overdue loop heartbeat — before starting other work; if it shows review notes awaiting decision, mention them and offer to walk through them (Jesse doesn't track triggers — the dashboard is how pending work reaches him). `INDEX.md` is a generated one-line-per-note map of the vault — consult it before claiming something isn't in the vault.

**Session close-out.** When Jesse says he's "closing out" (or wrapping up, done for the day), run this routine without being asked for specifics: (1) commit and push any uncommitted vault/config work per lane conventions; (2) drop any unfiled durable finding, loose end, or idea into `00-inbox/` as a quick note (ideas use `templates/_idea-seed-template.md`, `status: unexplored`) — rough is fine, the capture loop routes it; (3) if a real decision was made this session, one line in `change-log.md`; (4) tell him in one short block what was committed, what was filed, and anything left open. He should never need to remember a command — this phrase is the command.

## Folder structure (post-cleanup)

Folder layout is discoverable from `ls` and `INDEX.md`. Only the non-obvious parts are recorded here.

- `tools/` — vault automation scripts: `vault_lint.py` (7 rules incl. ORPHAN), `vault_health.py` → `50-dashboards/health.md`, `vault_index.py` → `INDEX.md`, `estimating_rollup.py` → `04-knowledge/estimating-actuals-rollup.md`

Root-level files: `change-log.md` (decisions-only log), `INDEX.md`, `Identity.md`. `03-jobs/` and `05-projects/` are gone. Do not reference or recreate them — job actuals now live inside heater cards.

## Schema authority

`04-knowledge/_canonical-heater-card.md` is the exemplar. `templates/_heater-template.md` derives from it. All heater cards conform to it.

Task Durations table (actuals only) — full spec lives in the exemplar and the `usadebusk-vault-ingest` skill:

`Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total`

## Output

Formatting and session-mode rules live in `01-context/output-preferences.md`. The **SOP formatting standard** has one canonical home: `04-knowledge/sops/sop-formatting-standard.md` — not here and not in a skill. The `usadebusk-sop` skill governs SOP *content* and explicitly defers formatting to that file; anything else that mentions SOP formatting points at it.
