# CLAUDE.md — Vault Entry Point

**Scope.** USADebusk operational knowledge, expanding to include personal and LLM-knowledge layers. The vault is no longer USADebusk-only — treat new top-level domains as expected, not anomalies.

**Session startup.** Read `01-context/` before responding — every file except `system-workflow-reference.md` and `workflow-map.md`, which are reference and history (how the system fits together; paused/retired-project status), not per-response context: load those two on demand when a task actually needs them. Load `02-facilities/` and `04-knowledge/` on demand only when named. Do not auto-load `archive/`, `templates/`, or `tools/`. Check `50-dashboards/health.md` and surface any red (FAIL) rows — a lint error or an overdue loop heartbeat — before starting other work; if it shows review notes awaiting decision, mention them and offer to walk through them (Jesse doesn't track triggers — the dashboard is how pending work reaches him). `INDEX.md` is a generated one-line-per-note map of the vault — consult it before claiming something isn't in the vault.

**Session close-out.** When Jesse says he's "closing out" (or wrapping up, done for the day), run this routine without being asked for specifics: (1) commit and push any uncommitted vault/config work per lane conventions; (2) drop any unfiled durable finding, loose end, or idea into `00-inbox/` as a quick note (ideas use `templates/_idea-seed-template.md`, `status: unexplored`) — rough is fine, the capture loop routes it; (3) if a real decision was made this session, one line in `change-log.md`; (4) tell him in one short block what was committed, what was filed, and anything left open. He should never need to remember a command — this phrase is the command.

## Folder structure (post-cleanup)

Folder layout is discoverable from `ls` and `INDEX.md`. Only the non-obvious parts are recorded here.

- `tools/` — vault automation scripts. Generators: `vault_lint.py` (rule set defined by and authoritative from the script itself — no count here to drift), `vault_health.py` → `50-dashboards/health.md`, `vault_index.py` → `INDEX.md`, `estimating_rollup.py` → `04-knowledge/estimating-actuals-rollup.md`, `pig_usage_rollup.py` → `04-knowledge/pig-usage-rollup.md` and `coil_geometry_audit.py` → `04-knowledge/coil-geometry-audit.md` (both run on demand — neither is wired to a loop, so re-run before citing). The coil audit answers which heater cards carry geometry complete enough to work from, and names what blocks the rest; it separates *the customer never supplied it* from *nobody filled the card in* from *the value is there but is not a plain number*, including per-circuit columns answered at heater scale. Checkers: `baseline_staleness.py` (regression fixtures; `--verbose` on demand), `config_frontmatter_lint.py` (the config repo, not this one), `sharepoint_export.py` (projects notes to the SharePoint library). `fixtures/` is the lint self-test corpus — a new lint rule requires a fixture there.
- `06-reviews/` — loop output: review notes, triage notes, and audit evidence, one dated file per adjudication. Mostly closed (48 of 66 `resolved` as of the 2026-08-24 rename), so it is an archive of decisions already made, not a knowledge layer to read for content. Named `06-insights/` until 2026-08-24, after a running `insights-log.md` that was itself archived 2026-07-06 — if you meet the old name anywhere, it is stale.
- `07-llms/` — how the LLM tools themselves behave: Claude Code release facts, Copilot, Grok. Not USADebusk domain content.
- `08-systems/` — the non-vault systems Jesse operates in, principally the Outlook/M365 record. Read it from the system before trusting it; both tiers of that document were fabricated once.
- `09-interests/` — personal, non-USADebusk. Expected, not an anomaly.
- `apps/` — self-contained browser tools, no build step and no server: open the `.html` directly. Two of them. `pig-tracker/` is live, and its `buildGeometry()` (`pig-tracker.html:393`) is **cited by approved unexecuted work** — grep for `pig-tracker.html` before moving or renaming it, because nothing lints repo-relative paths. `rig-diagram/` is **back-test evidence under a standing do-not-use ruling** (`06-reviews/2026-08-16-backtest-rig-diagram-layout-engine.md`) — not a path, not to be wired to heater cards; its domain content lives at `04-knowledge/rig-diagram-corpus.md`. The two PDFs beside it are its proofs and stay put.
- `archive/` — **gitignored.** Notes here are not all in git history, so a file in `archive/` may exist only on disk. Never treat deletion from `archive/` as recoverable without checking `git ls-files` first.

Root-level files: `change-log.md` (decisions-only log), `INDEX.md`, `Identity.md`. `03-jobs/` and `05-projects/` are gone. Do not reference or recreate them — job actuals now live inside heater cards.

## Schema authority

`04-knowledge/_canonical-heater-card.md` is the exemplar. `templates/_heater-template.md` derives from it. All heater cards conform to it.

The Task Durations table is actuals-only; its column set and conventions live in the exemplar (mirrored in the `usadebusk-vault-ingest` skill). Do not restate the columns here — the prior inline copy had already drifted out of sync (it was missing the `Condition` column).

## Output

The universal formatting rules live in global CLAUDE.md; `01-context/output-preferences.md` holds only the vault-specific session-mode and behavior elaboration. The **SOP formatting standard** has one canonical home: `04-knowledge/sops/sop-formatting-standard.md` — not here and not in a skill. The `usadebusk-sop` skill governs SOP *content* and explicitly defers formatting to that file; anything else that mentions SOP formatting points at it.
