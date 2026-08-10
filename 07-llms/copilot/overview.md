---
title: Microsoft Copilot — Overview
created: 2026-06-29
tags: [copilot, microsoft, email, outlook]
---

# Microsoft Copilot

Copilot is used primarily through Outlook (email triage and drafting) and as a reasoning layer over the Outlook folder/category architecture.

## Email architecture — three-tier model

**Tier 1: Outlook folders** — encode state (where is this email in its lifecycle?). Nine folders define the pipeline:

| Folder | Meaning |
|---|---|
| 01-Inbox-Active | Needs action |
| 02-Waiting | Sent, awaiting reply |
| 03-Proposals-Active | Open bids |
| 04-Proposals-Sent | Submitted, awaiting award |
| 05-Awarded | Award confirmed, job pending |
| 06-Execution | Job in progress |
| 07-Closed | Completed |
| 08-Reference | No action, retain |
| 09-Archive | Done, low-value |

**Tier 2: Categories** — encode meaning (what kind of thing is this?). Fourteen categories total:

- 7 lifecycle categories (Action Required, Awaiting Reply, Proposal, Awarded, Active Job, Closed, Reference)
- 6 facility roster categories (one per key customer / facility)
- 1 risk category (Flag: Risk / Review)

**Tier 3: Copilot** — the reasoning layer. Reads folder state + categories to answer questions like "what bids are pending for Valero?" or "what's outstanding from last week?" without manually searching.

## Outlook email security architecture

Deployed a 5-rule corrective architecture to fix email deliverability and sorting issues. Known gap: smtp.com in Rule 02A was flagged during design — confirm whether it's still a live gap.

## Agent creation

The concrete example built so far is the [[heater-extraction-agent]] — a Copilot-side architecture for extracting fired heater coil data from degraded engineering drawings, using SharePoint-hosted knowledge files and a separate Auditor agent pattern. Document further agent setups here as they occur.

## Sycophancy-reduction custom instructions

(Placeholder — document the custom instructions approach once finalized.)

---

## SharePoint vs. OneDrive — settled architecture

SharePoint is the primary knowledge substrate for anything that needs to be durable, shared, or agent-accessible. OneDrive is for staging and personal drafts only. Agents grounded in SharePoint can cite sources; agents grounded in OneDrive cannot be reliably shared or governed.

Full governance depth (permissions-over-prompts, oversharing risk, SharePoint Advanced Management, cleanup checklist) lives in [[chatgpt-copilot-workflow-architecture]].

**M365 Copilot's semantic index is flat, not folder-based.** It ranks retrieval on file content and filename, not path nesting — a deep, tidy folder tree buys little on its own. What actually degrades answer quality is duplicate copies of the same document (Copilot can't tell which is current and cites whichever scores higher) and volume dilution (personal/dev files that have no business being indexed still occupy and surface in the index). The retrieval lever is eviction and deduplication plus a consistent filename convention (leading `DSP#NNNNN_`/`USA#####_` token, `OLD_` supersede prefix — already the rule inside `USADeBusk\Facilities\`, worth extending to `Company\` docs), not deeper nesting. This is general M365 Copilot behavior, not verified against the DeBusk tenant specifically — confirm tenant reality before designing around it, per the Tenant-reality-first pattern below. Applies to OneDrive for Business (indexed for its owner's personal Copilot chat) — it does not change the SharePoint-is-canonical ruling above, which is about shared/governed agents. A full manual-reorg reference for Jesse's enterprise OneDrive (evict-first ordering, folder-by-folder destination table, known traps like `NNN00` sentinel quote numbers and OneDrive cloud-filter directory-move corruption) was produced 2026-07-31 and saved to `C:\Users\Jwuts\.claude\plans\i-m-organizing-my-enterprise-robust-alpaca.md` — read-only recon, nothing moved.

**Restricted SharePoint Search is not a security boundary.** It's documented as a temporary containment measure only, meant to be disabled after validation — use real permission remediation and site governance first, not this as a standing fix. Distinct from Restricted Content Discovery (a site-level discovery control, doesn't touch permissions, can't apply to OneDrive).

## Researcher and Analyst — governance scope

Researcher (deep multistep research) and Analyst (data analysis) are first-party Microsoft 365 Copilot experiences that are part of the core Copilot chat experience — they do **not** fall under agent-related admin settings. Don't assume "agent settings" governance will manage or disable these the same way it manages user-created agents.

## Agent Builder vs. Copilot Studio

Use **Agent Builder** first for simple, declarative, read-only agents — lower friction, no admin overhead, sufficient for most grounding-plus-prompt tasks. Reserve **Copilot Studio** for advanced workflows, connectors/actions, governance requirements, and production deployment. Don't start in Studio for agents that could be built in Builder.

## Daily Ops Brief Agent — design constraint

Start read-only: grounded in SharePoint, Outlook, and Teams with citations enabled, no write actions. Add write actions only after the read-only version is validated on real data. This is the proven maturation path — build the audit loop before adding automation.

## Tenant-reality-first research pattern

Before designing any Copilot feature or agent, verify what the actual tenant exposes: model picker availability, agent creation access, SharePoint grounding, connector catalog, publishing options, admin constraints. Do not design around advertised features that may be behind a license gate or admin toggle. Discovering a capability gap after building against it is expensive.

## Outlook automation maturity path

Start with simple deterministic rules: sender and topic-based routing. Mature into facility/customer/project routing only after validating rules on real messages. Don't manually categorize long-term once rules are validated — the rules should do the work. Heavy rule systems built before real-message testing consistently over-fit to expected cases and miss edge cases.

## Agent boundary

Agents may read, analyze, summarize, and draft. They may not edit SharePoint source files without explicit per-task permission. This boundary should be hard-coded in agent instructions, not left to model judgment.

## Pricing boundary

Agents and automated outputs must derive pricing only from sourced inputs. Margin and cost language is restricted to conversations with Jason, Marshall, or Travis — not surfaced in agent outputs, reports, or any document that leaves those conversations.

## Copilot Chat memory

Copilot Chat does not have durable access to prior chat history across sessions. Anything worth retaining must be copied into a SharePoint file, notebook, or explicit handover prompt before the session ends. Do not rely on Copilot Chat to remember context from a previous conversation.

## Structured output preference

For multi-item status, comparisons, and project tracking: prefer ini/yaml-style or tabular structured output over verbose Markdown prose. Structured output is scannable, diff-able, and copy-pasteable into downstream tools. Default to this format whenever output will be reviewed quickly or reused.

---

# Verified Copilot mechanics — 2026-08-10

Established against Microsoft Learn during the Furnace Decoking knowledge-base design session. Version-sensitive; re-verify before relying on the numbers. Docs: [semantic indexing](https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot), [agent knowledge sources](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge).

## Three surfaces, and only two take instructions

The single most confusing thing about this ecosystem, and the source of a session's worth of talking past each other:

| Surface | What it is | Instruction field | Scope |
|---|---|---|---|
| **Copilot in SharePoint** — the right-hand "Ask a question about this site" panel | First-party, built in, not user-created | **None.** It says so itself. | Whole site, fixed |
| **SharePoint agent** — a `.agent` file you create | User-created; editor has Identity / Sources / **Behavior** | **Yes** — Behavior holds welcome message, starter prompts, instructions | Whatever you point it at |
| **M365 Copilot desktop/web app** | Tenant-wide chat | Custom instructions | Everything your account can reach — **not scopable** |

`.agent` files land in `Site Assets > Copilots` when created from the site homepage, or in the current library folder when created from a library. When the site panel offers to store "site instructions" or "reusable skills" as files, that is the retrieved-as-knowledge anti-pattern, not a real instruction field — Microsoft's declarative-agent guidance says instructions belong in the instruction field because knowledge content is not trusted instruction content.

## `.md` is not an indexed file type

Semantic index supported types: **doc/docx, pptx, pdf, aspx, one**, plus connector data. Agent Builder embedded files add **.txt, .html, .xls/.xlsx**. **Markdown appears in neither list.**

A SharePoint agent may still *open* a `.md` file when it enumerates a library — direct file access and semantic retrieval are different paths, which is why an agent will claim it "reads .md fine." The failure mode is the dangerous one: content that looks loaded but never ranks in retrieval. **Convert vault notes to `.docx` or `.pdf` before uploading**, and strip YAML frontmatter on export so the columns are the only copy of the schema.

## Column metadata is a real retrieval signal — but only when scoped

Direct from the docs: *"associated column metadata can be incorporated as signals during retrieval when a query is scoped to a specific library or folder,"* and attaching a library or folder means grounding *"uses the library's column metadata alongside file content to constrain and rank results."*

This is the fact that makes a column schema worth building **and** confines its value to the scoped-agent case. It buys nothing for a broad desktop-app query. Two conditions: documented as available on the web experience, and the site must stay searchable (`Site settings > Search and offline availability`). This supersedes nothing in the flat-index note above — folder *nesting* still buys nothing; *columns* do.

## Limits and cadence

Per agent: **100** SharePoint files/folders/sites · **50** OneDrive files · **1** SharePoint list · **20** uploaded embedded files · 4 public URLs · 5 Teams chats. Selecting a site does **not** include its lists — a list must be added by its own URL. A list caps at 20,000 items and 50 MB raw text.

Indexing: new documents on a site accessible to **two or more users index daily**; updates to already-indexed documents are immediate. Run any retrieval eval the next day, not the same afternoon.

## Agent Builder cannot block fabrication

The **"Only use specified sources"** toggle *prioritizes* rather than blocks — Microsoft states plainly that Agent Builder can't fully block general AI knowledge and that stricter control requires **Copilot Studio**. So a fabrication probe in an eval is a calibration measurement, not a pass/fail on the platform, and persistent leakage is the documented trigger to evaluate Studio.

Also: if **Restricted SharePoint Search** is ever enabled tenant-wide, SharePoint stops working as a knowledge source entirely.

## No API path exists

The MCP registry has **no SharePoint, Microsoft Graph, M365, OneDrive, or Outlook connector** (searched 2026-08-10, zero results). Reaching the tenant programmatically is not available; browser automation via Chrome integration is the only route — see [[code]].

## Furnace Decoking site — as-found

`usadebusk.sharepoint.com/sites/FurnaceDecoking` · private group, Jesse owner, **Jason Harman, Travis Trenholm, James Lee** members (all Edit via the Members group). Libraries as of 2026-08-10: `Copilot Knowledge` (43 items, unexplained), `Knowledge Vault` (21 items, a throwaway test build), `Documents` (empty), `Site Assets` (10), `Site Pages` (4). An admin policy applies **Deny: Add and Customize Pages** on top of Full Control, which likely takes Copilot Pages off the table here and proves tenant policy is in play that Jesse doesn't control.

**Pricing boundary note:** Jason and Travis are inside the Jason/Marshall/Travis cost-basis circle; **James Lee is not.** Jesse ruled the site 100% trusted on 2026-08-10, so this is a sanctioned exception rather than a violation — recorded so a future drift run doesn't read it as one.

**Build plan:** `~/.claude/plans/create-a-new-session-effervescent-papert.md` — seven phases, library-scoped SharePoint agent, vault stays canonical as a one-way projection.
