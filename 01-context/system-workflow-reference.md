# System Workflow Reference
**Layer:** 01-context — load on demand (reference, not per-response context)
**Purpose:** How the vault + skill system actually works, in one place: the loops, which skill triggers on what, and how to add or ingest things manually. Read this when you forget how a piece fits together — it's not a status tracker (see [[workflow-map]] for that). **You don't need to remember any triggers:** every session starts by reading `50-dashboards/health.md`, which surfaces anything awaiting you.

> **Three loops were stopped on 2026-08-21** — capture, idea-research and pre-staging. Their rows below are kept with a STOPPED marker rather than deleted, because the reasoning is worth having. See [[2026-08-20-vault-architecture-audit-evidence]]. In short: those three generated roughly two decisions a day at a ~53% effect rate against a clearing rate of one session every two to four weeks, and they read `01-context/` in 1 of 85 runs — they were proposing without knowing the active jobs. Their scheduled tasks are **disabled, not deleted**; re-enabling one is a single `enabled: true` plus its row back in `LOOP_HEARTBEATS` in `tools/vault_health.py`.
>
> **What still runs:** consolidation (monthly, 15th), skill-drift (monthly, 1st), and the review/agent loop on demand. What replaced the stopped loops is not another loop — it is defect-triggered checks that stay silent unless something is actually wrong: the lint rules, `ROLLUP-SCALE`, and the `Open decisions not in the queue` health row.

---

## The Loops

| Loop | Trigger | Scope | What it does | Ceremony |
|---|---|---|---|---|
| **Capture Loop** — **STOPPED 2026-08-21** (task disabled; it had become a net producer, last run ingesting 1 and harvesting 2) | ~~Scheduled, daily ~5am local~~ (`vault-capture-loop`) | `00-inbox/` routing + session-transcript harvest → `07-llms/`, `08-systems/`, `09-interests/`; refreshes `INDEX.md` + health dashboard | Files what you dropped in the inbox, harvests durable findings from recent Claude Code sessions. Never touches operational content. | Low — runs unattended, no approval gate. |
| **Agent / Review Loop** | On-demand only — you say "run the Vault Review Loop" | Operational core: `02-facilities/`, `04-knowledge/`, pricing/SOP/safety/field-execution content | Picks one item, writes a review/contradiction/question note with a Decision checklist. Never edits canonical content without your approval. | High — manual, you're present, propose-only. |
| **Idea Research Loop** — **STOPPED 2026-08-21** (task disabled; largest ask producer, 54% effect). Seeds still accrue in `00-inbox/`; research one on demand when it matters | ~~Scheduled, nightly ~2am local~~ (`vault-idea-research-loop`) | `00-inbox/*.md` with `type: idea-seed` only | Picks one unexplored idea, researches prior art / power-user solutions, writes findings as a review note in `06-reviews/`. Never builds, never decides. | Low — unattended, but only ever proposes. |
| **Pre-Staging Loop** — **STOPPED 2026-08-21** (task disabled; 53% effect, same context blindness) | ~~Scheduled, daily ~6am local~~ (`vault-prestaging-loop`) | `00-inbox/` items carrying the defer marker → review note in `06-reviews/` + a `decision-queue.md` row | Prepares the decisions the Capture Loop defers, so you arrive to approve/reject rather than to read and analyse. Proposes only; never writes operational content. | Low — unattended, bounded by the 10-row queue cap, one item per run. |
| **Skill-Drift Loop** | On-demand only — you say "run the Skill-Drift Loop" (schedule disabled 2026-07-19) | Reads `~/.claude/skills/` + vault; writes one review note + a `drift/YYYY-MM` config-repo branch | Detects skills contradicting vault truth, each other, or reality; packages fixes as an unmerged proposal branch. You merge or discard. | Medium — manual, because its run needs config-repo branch/commit/push authority that is deliberately not pre-granted. |
| **Consolidation Loop** | Scheduled, 15th of month ~3am (`vault-consolidation-loop`) | `07-llms/`, `08-systems/`, `09-interests/` + regenerates INDEX.md, actuals rollup, health | Merges duplicate notes, rewrites append-piles into clean articles, links orphans — the iterative-rewriting half of the wiki strategy. | Low — Lane 1 only, archive-never-delete, bounded per run. |

Full specs: [[vault-capture-loop-spec]], [[vault-agent-loop-spec]], [[vault-idea-loop-spec]], [[vault-prestaging-loop-spec]], [[vault-skill-drift-loop-spec]], [[vault-consolidation-loop-spec]].

**Why they were six, and why they are now three (2026-08-21).** The six differed on two axes — how risky the content is (content layer vs. operational core vs. speculative vs. skills) and how much judgment the write requires (mechanical filing vs. approval-gated change vs. bounded research vs. propose-only detection). That reasoning was sound and is not what failed. What failed is that three of them spoke on a **timer** rather than on a **defect**, so they produced asks whether or not there was anything worth asking: roughly two decisions a day at a ~53% effect rate, against a clearing rate of one session every two to four weeks. One clearing session bought five days.

The distinction that replaced "how risky is the content" is **defect-triggered versus schedule-triggered.** Everything that stays silent unless something is actually wrong — the lint rules, the pre-send gate, the commercial-pipeline row, the skill-drift loop — runs at a 90–100% effect rate. Everything that fires on a clock runs at about half that. The surviving loops are the ones that either clear work (review, consolidation) or stay quiet until they find something (skill-drift).

**The pre-staging rationale, kept because it was right at the time (2026-07-28).** Capture deferred everything operational and the review/agent loop — the only consumer of those deferrals — fired only when Jesse said so, so the analysis machinery sat idle while the pile grew. Pre-staging closed that gap without touching the Lane 4 gate: deciding stays with Jesse; preparing the decision does not. That logic held. What made it obsolete is that capture stopped too, so there are no deferrals to pre-stage.

**Monitoring rule:** every run — scheduled or manual — writes the run ledger (`50-dashboards/.loop-runs.json`, local) as its first and last action, and a manual pass of a scheduled loop must use the loop's exact heartbeat commit prefix (`vault-consolidate:`, not `[auto]`) — otherwise the run is invisible to `vault_health.py` and the dashboard reports a loop failure that didn't happen, or misses one that did.

---

## Skill Trigger Map

Skills live at `~/.claude/skills/`, no separate deploy step. `usadebusk-core` loads alongside every other one below.

| Skill | For | Trigger words / task types | Load alongside |
|---|---|---|---|
| **usadebusk-core** | Foundational context for any USADebusk task | Any proposal, SOP, estimating, field ops, or technical-doc question; furnace decoking, pigging, fired heaters | Always, with any other skill below |
| **usadebusk-equipment** | Physical equipment specs | Pig sizing, launcher/receiver sizing, hose connections, Trimax pumper, filter press specs, hardware selection | usadebusk-core |
| **usadebusk-estimating** | Proposals, pricing, bids | New RFQ, bid package, scope pricing, heater card development, mob/demob, TA scope, emergency decoke | usadebusk-core |
| **usadebusk-fieldpm** | Field project management — **dormant** (reactivates on job mobilization) | `/setup`, `/extract`, `/log`, `/email`, `/status`, `/report`; service receipts, shift notes, payroll, job progress | usadebusk-core; usadebusk-equipment mid-job if pig sizing comes up |
| **usadebusk-ops** | Field ops admin/paperwork | Service receipts, ticket breakdowns, invoice prep, field documentation | usadebusk-core |
| **usadebusk-sop** | Procedures and SOPs | Writing a procedure, pre-execution package, process flow diagram; decoking sequence, pig travel path | usadebusk-core, usadebusk-equipment |
| **usadebusk-vault-ingest** | Document ingestion | `/convert`, `/ingest`, `/dry-run`; converting DOCX/PDF into the vault | usadebusk-core |
| **adversarial-review** | High-fidelity multi-agent review | "adversarial review", production or security-sensitive code review | Standalone |
| **idea-triage** | Brain-dump triage | "brain dump", "/triage", pasting an unstructured mix of ideas to disposition (execute / test / park / kill) | Standalone |

**Ideal invocation timing:** load `usadebusk-core` at the start of any USADebusk-flavored session, add the domain skill as soon as the task's shape is clear (don't wait until you're deep into it — skills change how the early exploration gets framed too).

---

## Manual Ingestion Flow

1. Drop a `.md` file into `00-inbox/` any time — no formatting requirements beyond reasonable frontmatter if you have it.
2. **Nothing picks it up on a schedule any more** (capture stopped 2026-08-21). Say "ingest what's in the inbox" in a session and the same three-outcome routing logic runs on demand: clear home in an existing note → appended and cited; folder exists but no matching note → new note created; nothing fits → left in inbox with a routing comment, reported to you. The routing logic lives in [[vault-capture-loop-spec]] and is unchanged — only its trigger is gone.
3. If an item is operational (pricing, SOP, safety, heater-card facts), routing still leaves it in `00-inbox/` and defers — it never routes operational content itself. Ask for the Review Loop to take it up.
4. The inbox is now a pile you work through when you choose rather than one a loop churns nightly. That is the intended change: it was growing 21 → 54 *while* a daily loop ran against it, because the loop harvested more than it filed.

---

## Idea-Seed Flow

1. Drop a new idea using [[_idea-seed-template]] (`templates/_idea-seed-template.md`) into `00-inbox/`, `status: unexplored`.
2. The Idea Research Loop picks up the oldest unexplored seed on its nightly run, researches it, and writes a review note in `06-reviews/` with an evidence-backed recommendation (sound / trap / premature / already covered).
3. The seed's own `status` flips to `researched` with a link to the review note — check `06-reviews/` for anything new after a night's run.
4. You make the call: check the Decision boxes in the review note (approve / park / reject / needs more research). The loop never decides for you, and never builds anything itself even if the verdict is "sound."
