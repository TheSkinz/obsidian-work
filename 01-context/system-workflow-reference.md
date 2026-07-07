# System Workflow Reference
**Layer:** 01-context — loads every session
**Purpose:** How the vault + skill system actually works, in one place: the five loops, which skill triggers on what, and how to add or ingest things manually. Read this when you forget how a piece fits together — it's not a status tracker (see [[workflow-map]] for that). **You don't need to remember any triggers:** four loops run on schedules, and every session starts by reading `50-dashboards/health.md`, which surfaces anything awaiting you.

---

## The Five Loops

| Loop | Trigger | Scope | What it does | Ceremony |
|---|---|---|---|---|
| **Capture Loop** | Scheduled, Mondays ~8am local (`vault-capture-loop`) | `00-inbox/` routing + session-transcript harvest → `07-llms/`, `08-systems/`, `09-interests/`; refreshes `INDEX.md` + health dashboard | Files what you dropped in the inbox, harvests durable findings from recent Claude Code sessions. Never touches operational content. | Low — runs unattended, no approval gate. |
| **Agent / Review Loop** | On-demand only — you say "run the Vault Review Loop" | Operational core: `02-facilities/`, `04-knowledge/`, pricing/SOP/safety/field-execution content | Picks one item, writes a review/contradiction/question note with a Decision checklist. Never edits canonical content without your approval. | High — manual, you're present, propose-only. |
| **Idea Research Loop** | Scheduled, nightly ~2am local (`vault-idea-research-loop`) | `00-inbox/*.md` with `type: idea-seed` only | Picks one unexplored idea, researches prior art / power-user solutions, writes findings as a review note in `06-insights/`. Never builds, never decides. | Low — unattended, but only ever proposes. |
| **Skill-Drift Loop** | Scheduled, 1st of month ~3am (`vault-skill-drift-loop`) | Reads `~/.claude/skills/` + vault; writes one review note + a `drift/YYYY-MM` config-repo branch | Detects skills contradicting vault truth, each other, or reality; packages fixes as an unmerged proposal branch. You merge or discard. | Low detection, zero application authority — propose-only. |
| **Consolidation Loop** | Scheduled, 15th of month ~3am (`vault-consolidation-loop`) | `07-llms/`, `08-systems/`, `09-interests/` + regenerates INDEX.md, actuals rollup, health | Merges duplicate notes, rewrites append-piles into clean articles, links orphans — the iterative-rewriting half of the wiki strategy. | Low — Lane 1 only, archive-never-delete, bounded per run. |

Full specs: [[vault-capture-loop-spec]], [[vault-agent-loop-spec]], [[vault-idea-loop-spec]], [[vault-skill-drift-loop-spec]], [[vault-consolidation-loop-spec]].

**Why five, not one:** they differ on two axes — how risky the content is (content layer vs. operational core vs. speculative vs. skills) and how much judgment the write requires (mechanical filing vs. approval-gated change vs. bounded research vs. propose-only detection). The capture loop fills the vault; the consolidation loop keeps it a wiki instead of a log pile; the skill-drift loop is the return path that pushes vault truth back into the skills every session loads.

---

## Skill Trigger Map

Skills live at `~/.claude/skills/`, no separate deploy step. `usadebusk-core` loads alongside every other one below.

| Skill | For | Trigger words / task types | Load alongside |
|---|---|---|---|
| **usadebusk-core** | Foundational context for any USADeBusk task | Any proposal, SOP, estimating, field ops, or technical-doc question; furnace decoking, pigging, fired heaters | Always, with any other skill below |
| **usadebusk-equipment** | Physical equipment specs | Pig sizing, launcher/receiver sizing, hose connections, TriMax pumper, filter press specs, hardware selection | usadebusk-core |
| **usadebusk-estimating** | Proposals, pricing, bids | New RFQ, bid package, scope pricing, heater card development, mob/demob, TA scope, emergency decoke | usadebusk-core |
| **usadebusk-fieldpm** | Field project management — **dormant** (reactivates on job mobilization) | `/setup`, `/extract`, `/log`, `/email`, `/status`, `/report`; service receipts, shift notes, payroll, job progress | usadebusk-core; usadebusk-equipment mid-job if pig sizing comes up |
| **usadebusk-ops** | Field ops admin/paperwork | Service receipts, ticket breakdowns, invoice prep, field documentation | usadebusk-core |
| **usadebusk-sop** | Procedures and SOPs | Writing a procedure, pre-execution package, process flow diagram; decoking sequence, pig travel path | usadebusk-core, usadebusk-equipment |
| **usadebusk-vault-ingest** | Document ingestion | `/convert`, `/ingest`, `/dry-run`; converting DOCX/PDF into the vault | usadebusk-core |
| **adversarial-review** | High-fidelity multi-agent review | "adversarial review", production or security-sensitive code review | Standalone |
| **idea-triage** | Brain-dump triage | "brain dump", "/triage", pasting an unstructured mix of ideas to disposition (execute / test / park / kill) | Standalone |

**Ideal invocation timing:** load `usadebusk-core` at the start of any USADeBusk-flavored session, add the domain skill as soon as the task's shape is clear (don't wait until you're deep into it — skills change how the early exploration gets framed too).

---

## Manual Ingestion Flow

1. Drop a `.md` file into `00-inbox/` any time — no formatting requirements beyond reasonable frontmatter if you have it.
2. The Capture Loop picks it up on its next scheduled run (Monday mornings) and applies the three-outcome model: clear home in an existing note → appended and cited; folder exists but no matching note → new note created; nothing fits → left in inbox with a routing comment, reported to you.
3. If an item is operational (pricing, SOP, safety, heater-card facts), the Capture Loop always leaves it in `00-inbox/` and defers — it never routes operational content itself. Bring it up in a session and ask for the Review Loop if you don't want to wait.
4. Don't want to wait for Monday? Just ask in a session — "ingest what's in the inbox" runs the same routing logic on demand.

---

## Idea-Seed Flow

1. Drop a new idea using [[_idea-seed-template]] (`templates/_idea-seed-template.md`) into `00-inbox/`, `status: unexplored`.
2. The Idea Research Loop picks up the oldest unexplored seed on its nightly run, researches it, and writes a review note in `06-insights/` with an evidence-backed recommendation (sound / trap / premature / already covered).
3. The seed's own `status` flips to `researched` with a link to the review note — check `06-insights/` for anything new after a night's run.
4. You make the call: check the Decision boxes in the review note (approve / park / reject / needs more research). The loop never decides for you, and never builds anything itself even if the verdict is "sound."
