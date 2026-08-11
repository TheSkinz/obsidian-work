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

**The site panel is not read-only — corrected 2026-08-10.** The "no instruction field" column above still holds, but treating that surface as question-and-answer only is wrong. Asked in plain language, it deleted a document library, created a new one with a description, added twelve columns with exact choice values, and built three filtered/grouped views — all verified afterward against the REST API, all correct. Two behaviours worth knowing: it renders its **own in-page confirmation card** for destructive actions rather than the native browser dialog (which the Chrome integration cannot dismiss, so the panel is the *easier* path for automation, not the harder one), and for non-destructive changes it **commits first and offers an undo card after** — a card with a Save button next to it may describe work already done. Verify against the API rather than reading the chat transcript.

`.agent` files land in `Site Assets > Copilots` when created from the site homepage, or in the current library folder when created from a library. When the site panel offers to store "site instructions" or "reusable skills" as files, that is the retrieved-as-knowledge anti-pattern, not a real instruction field — Microsoft's declarative-agent guidance says instructions belong in the instruction field because knowledge content is not trusted instruction content.

## `.md` is not on the documented list — but it works in this tenant

**Corrected 2026-08-10 by direct test. The earlier ruling on this page said to convert vault notes to `.docx` before uploading. That was wrong for this tenant and has been reversed.**

The documentation still excludes markdown. The semantic index supported-types table (page revision 2026-04-23) lists **doc/docx, pptx, pdf, aspx, one** plus connector data, and Agent Builder embedded files add **.txt, .html, .xls/.xlsx**. Markdown is in neither. The same page, however, describes the tenant index as "generated from text-based SharePoint Online files," which is broader than its own table — markdown falls in that gap.

**The test.** `TEST-A.md` and `TEST-B.docx` were uploaded to the Furnace Decoking `Documents` library with byte-identical content apart from a unique calibration token in each (ORANGE-7 and INDIGO-4). Both were retrievable roughly 75 minutes after upload, well inside the documented daily cadence for new files. Two surfaces, both passing:

- **M365 Copilot app** (tenant index) returned both tokens and named both files. Asked a content question with no filename and no token, it answered correctly and cited `TEST-A.md` — the markdown file — over the identical `.docx`.
- **Library-scoped SharePoint agent** (sources set to one library, prioritize-sources on, default Behavior) returned both tokens in a table with a working link per file, and used both files as inline citations on a content question.

**What this does not establish.** Both files held identical content, so citing markdown proves it is reachable and citable, not that it *ranks* against a larger corpus of differing documents. Retest at volume when the full load lands, and convert only if markdown degrades there.

**Contrary external evidence, still live.** A Microsoft Tech Community thread running May–August 2026 reports `.md` files in SharePoint libraries being neither retrievable nor citable — but for **Copilot Studio** agents, which is a different product from a SharePoint agent. Treat markdown support as unproven if Copilot Studio is ever adopted; that migration could silently break the knowledge layer. Microsoft is separately expanding markdown across the stack: native `.md` editing in SharePoint and OneDrive went GA 2026-04-21, and Copilot Notebooks added `.md` grounding rolling out early August 2026.

**Standing ruling:** upload vault notes as `.md`, no conversion step. Still strip YAML frontmatter on export so the library columns remain the only copy of `status` and `review_after`.

## Column metadata is a real retrieval signal — but only when scoped

Direct from the docs: *"associated column metadata can be incorporated as signals during retrieval when a query is scoped to a specific library or folder,"* and attaching a library or folder means grounding *"uses the library's column metadata alongside file content to constrain and rank results."*

This is the fact that makes a column schema worth building **and** confines its value to the scoped-agent case. It buys nothing for a broad desktop-app query. Two conditions: documented as available on the web experience, and the site must stay searchable (`Site settings > Search and offline availability`). This supersedes nothing in the flat-index note above — folder *nesting* still buys nothing; *columns* do.

## Driving SharePoint through the Chrome integration — operating notes

Learned by doing on 2026-08-10, building the `Knowledge` library end to end. Recorded here rather than in a session plan file because Jesse expects to build workflows, agents, and Power Automate flows on this tenant eventually. There is no API path — the MCP registry has no SharePoint/Graph/M365 connector — so browser automation is the only route and these are its rules.

**Verify through the REST API, never the UI and never a chat transcript.** Navigate the browser straight to these and read the XML:

```
/_api/web/lists?$select=Title,ItemCount&$filter=Hidden eq false
/_api/web/lists/getbytitle('X')/items?$select=FileLeafRef,<columns>
/_api/web/lists/getbytitle('X')/fields?$select=Title,InternalName,TypeAsString,Choices&$filter=Hidden eq false and ReadOnlyField eq false and CanBeDeleted eq true
/_api/web/lists/getbytitle('X')/views?$select=Title,ViewQuery,DefaultView,Hidden
```

Append `&$expand=Owner` with `Owner/Title` for person columns. `_ExtendedDescription` — the Description column — is **not** queryable as an item property and errors the whole request; verify it visually in a list view instead.

**Prefer the Copilot panel to clicking.** It built a library, twelve columns with exact choice values, and three filtered views in two prompts, with zero drift. Instruct it *"use these exact names and values verbatim, do not paraphrase, reword, or add values I have not listed"* and it complies. Then audit via the API — see the commits-before-undo behaviour noted above.

**Native browser confirm dialogs block the Chrome extension completely.** Screenshots time out, keypresses don't reach them, and only Jesse can clear one. Classic `_layouts` pages throw them; the Copilot panel renders its own in-page confirmation card, which is clickable. That alone makes the panel the better automation surface, not just the faster one.

**Classic `_layouts/15/ViewEdit.aspx` does not save** against a modern library here — it returned "View does not exist" and committed nothing. Read-only and simple-write classic pages are fine: `srchvis.aspx` (search visibility), `listgeneralsettings.aspx` (Quick Launch, name, description), `listedit.aspx` (library delete).

**Agent-created libraries are not added to Quick Launch.** Fix at `listgeneralsettings.aspx?List={guid}` → Navigation → Yes. The Copilot panel builds the data model well and the presentation layer inconsistently — it also skipped column formatting.

**`read_page` truncates on SharePoint's enormous column dropdowns.** Use `find` with a specific natural-language query to get element refs, then `form_input`.

**Tabs die between turns.** Call `tabs_context_mcp` with `createIfEmpty:true` and re-navigate; no state is lost.

**Do not diagnose from a freshly-created item's row in a view.** A new file appeared in `Review Overdue` carrying no date, which read as the filter matching nulls — a real bug if true. It wasn't; the list was rendering a just-created item before the filter re-queried. Re-check before concluding.

## Column metadata fires — eval Q1 passed 2026-08-10

The question the whole column schema was built to answer, tested and answered the same night the library was built. Two files in the `Knowledge` library on the same topic, contradicting on one checkable number: `MANUAL-09_Phase-II-Mechanical-Decoking` (Status `active`, max pig OD = governing tube ID + 0.250 in) and a deliberately falsified sibling `…-Rev-A` (Status `deprecated`, Confidence `low`, + 0.500 in). Filenames deliberately gave nothing away.

Asked for the maximum pig OD, the agent returned 0.250 with the correct worked example and volunteered *"Source used: MANUAL-09_Phase-II-Mechanical-Decoking.md (Status: active)."* Asked whether any other document gave a different figure, it named Rev-A, cited its `deprecated` status and `low` confidence, ruled it non-authoritative, and declined to state Rev-A's figure without opening the file.

So the agent **retrieves competing documents, reads their column values, and discriminates on them.** Column metadata is a live retrieval and ranking signal on a library-scoped agent, not decoration. The contingency the build plan carried — move Status into the document body as a plain header line — is not needed.

**Bound on the claim.** Rev-A's Description column read "Contains a deliberate factual error in the pig OD ceiling," written as a safety guard for human readers. The agent cited Status, Confidence *and* Description together, so this proves the column *set* discriminates, not Status in isolation. A future test wanting to isolate Status should use a neutral Description. Single run; the plan calls for a second the following day.

**Surface note.** The agent answered correctly when tagged inside the M365 desktop app, including on iPhone. The *same agent* invoked through the SharePoint in-site Copilot panel returned "it looks like I can't chat about this" and, earlier, hung indefinitely. The agent, its instructions, and the index are all fine — the in-site panel is the unreliable surface for custom agents. Run evals from the desktop app.

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
