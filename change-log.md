# Change Log
**Purpose:** Append-only record of vault updates. One line per change.
**Format:** Date | File(s) changed | What changed | Trigger

---

| Date | File(s) | Change | Trigger |
|---|---|---|---|
| 2026-04-25 | Vault root | Initial vault scaffolding created | Session: vault build execution |
| 2026-04-25 | CLAUDE.md | Created — agent entry point, output preferences, SOP formatting standard, Insight Loop | Session: vault build execution |
| 2026-04-25 | 01-context/* | Created output-preferences.md, workflow-map.md, estimating-approach.md, active-jobs.md | Session: vault build execution |
| 2026-04-25 | 04-knowledge/sops/sop-formatting-standard.md | Created — SOP formatting standard derived from 3 completed production SOPs | Session: vault build execution |
| 2026-04-25 | 05-projects/* | Created system-prompt stubs for all 4 Claude Projects | Session: vault build execution |
| 2026-04-25 | .claudeignore | Created | Session: vault build execution |
| 2026-05-21 | skills/usadebusk-vault-ingest/SKILL.md | Updated skill: CND job routing, collision suffix logic, revised-proposal overwrite, field-report merge, DSP# correction table, auto-subfolder creation, client list 28→32 (Formosa, PBF, Suncor, Westlake added) | Session: dry-run + ingest |
| 2026-05-21 | 05-projects/sales-proposals/* | 18 proposals ingested; 12 new client subfolders created (Cenovus, Valero, HF-Sinclair, PBF, Formosa, Flint-Hills, P66, CITGO, Westlake, Suncor, ONEOK, Hunt) | Session: ingest pipeline |
| 2026-05-21 | 03-jobs/Marathon/USA25058.md | Field reports merged: 37-B-1, 41-B-1, 43-B-1 LEP (Oct 2025) appended under ## Field Reports | Session: ingest pipeline |
| 2026-05-21 | 03-jobs/Valero/USA26002.md | Field report merged: HC-H-002 (Jan 2026) appended under ## Field Reports | Session: ingest pipeline |
| 2026-05-21 | 00-inbox/CND25004.md | Syncrude Fort McMurray job report held in inbox — client not scaffolded | Session: ingest pipeline |
| 2026-06-06 | 00-inbox/2026-06-06-refineries-migration.md | Session log created — Desktop\Refineries migration (73 files, 30 folders, 24 client sites) | Session: file migration |
| 2026-06-06 | 06-insights/insights-log.md | Entry added — Desktop\Refineries migration complete | Session: file migration |
| 2026-05-21 | skills/usadebusk-vault-ingest/SKILL.md | v3: DSP dissolution into per-heater cards, document type detection order, tube geometry conflict detection, truck-level hour splitting, city-state normalization, heater card template | Session: adversarial audit |
| 2026-05-21 | 02-facilities/ExxonMobil/Baytown-TX/PS8_F802-CrudeHeater/SOP-DCK-F802-001.md | Created — F-802 execution SOP ingested as companion doc to heater card | Session: ingest |
| 2026-05-21 | 03-jobs/ExxonMobil/USA26022.md | Change order / overage detail merged under ## Field Reports | Session: ingest |
| 2026-05-21 | 02-facilities/ExxonMobil/Baytown-TX/PS8_F802-CrudeHeater/F-802.md | ## Field Notes added — USA26022 actuals, standby causes, filter press / crane lift flags for future bids | Session: ingest |
| 2026-05-21 | skills/usadebusk-vault-ingest/SKILL.md | v4: markitdown[docx] fix, SOP companion routing, client facility doc routing (facility level only), expanded doc_type values | Session: skill refinement |
| 2026-06-20 | 02-facilities/Marathon/Garyville-LA/Unit-210_1403A-Vac/210-1403A.md | Reshaped to canonical Heater Card Schema (engineering geometry encoding + config rollup + quarantined Job Options); metallurgy set Stainless, config Individual Passes; original archived to archive/ | Session: default-assumption audit |
| 2026-06-20 | 02-facilities/ExxonMobil/Baytown-TX/PS8_F802-CrudeHeater/F-802.md | Reshaped to canonical Heater Card Schema; filtration/smart-pigging moved to quarantined Job Options; config set Looped at Radiant outlets; original archived to archive/ | Session: default-assumption audit |
| 2026-06-26 | 00-inbox/CND25004.md -> 03-jobs/Syncrude/CND25004.md | Routed confirmed Syncrude CND25004 report; created Syncrude Fort McMurray facility scaffold; preserved CND25002 body-field warning | Codex knowledge-system pilot |
| 2026-06-26 | 03-jobs/Syncrude/CND25004.md -> 02-facilities/Syncrude/Fort-McMurray-AB/7-2-F-1.md | Created draft source-derived heater scaffold and candidate canonical update review; no facts promoted to reviewed status | Codex knowledge-system pilot |
| 2026-06-26 | 04-knowledge/vault-agent-loop-spec.md | Created manual Vault Review Loop spec with approval boundaries and stop conditions | Codex knowledge-system pilot |
| 2026-06-27 | 00-inbox/Final Heater Card Output — H-2421.md -> 02-facilities/HF-Sinclair/Artesia-NM/H-2421.md | Created approved draft/source-derived H-2421 heater card with uncertainty preserved; source note left in inbox | Codex Vault Review Loop |
| 2026-06-27 | 04-knowledge/vault-agent-loop-spec.md | Updated Vault Review Loop trigger to Monday and Friday mornings at 8:00 AM America/Chicago; retained manual on-demand command | Codex schedule update |
| 2026-06-27 | .gitignore; 04-knowledge/vault-source-of-truth.md; 04-knowledge/vault-agent-loop-spec.md | Set canonical vault path to `C:\Users\Jwuts\obsidian-work`; added conservative Git ignore rules for Obsidian Sync + private Git setup | Vault migration to Obsidian Sync + private Git |
| 2026-06-29 | 03-jobs/* and 05-projects/* (deleted); 02-facilities/* overviews; CLAUDE.md; AGENTS.md; INDEX.md; 50-dashboards/knowledge-review-dashboard.md; 04-knowledge/_canonical-heater-card.md, concepts/quote-lifecycle.md, vault-agent-loop-spec.md; templates/_facility-template.md | Decommissioned 03-jobs and 05-projects; converted [[USA]]/[[CND]] wikilinks to plain text; preserved 3 orphan DSPs (no source_file) to 00-inbox/preserved-dsps/; cleaned stale folder references (facility Job History dataview → static pointer, load-on-demand lists, dashboard FROM clauses, exemplar folder-structure note, quote-lifecycle workflow) | Vault consolidation — jobs/DSPs re-ingest later from prepared sources |
