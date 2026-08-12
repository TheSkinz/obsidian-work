---
title: Microsoft Copilot — Overview
created: 2026-06-29
tags: [copilot, microsoft, email, outlook]
---

# Microsoft Copilot

Copilot is used primarily through Outlook (email triage and drafting) and as a reasoning layer over the Outlook folder/category architecture.

## Email architecture — three-tier model

> **⚠ THE FOLDER TABLE BELOW IS WRONG — verified against the live mailbox 2026-08-11. Do not build on it.**
>
> The real folders are `00 Action - Today`, `01 Waiting On Others`, `02 Internal Review`, `03 Sent - Pending Response`, `04 Execution Active`, `05 Automation & Systems`, `06 IT / Security`, `07 Read Later`, `99 Archive`. Nine custom folders, as recorded — and that is the only thing that matches.
>
> The table below describes a **commercial pipeline** (proposals → awarded → execution → closed). The mailbox is a **personal triage workflow**. There is no Awarded folder, no Closed folder, no Reference folder, and no Proposals-Active/Sent split; four real folders are absent from it entirely. The error dates to this page's creation on 2026-06-29 and was never checked against the tenant.
>
> **The category list below is wrong too — read from Outlook 2026-08-11.** The real categories are a seven-stage pipeline: `RFQ`, `Proposal Draft`, `Submitted`, `Awarded`, `Execution`, `Post-Job`, `Closed / No-Go`. There are **no facility or customer categories**; the other six entries in Outlook are its stock colour placeholders and carry no meaning. Of the fourteen claimed below, exactly one — `Awarded` — exists.
>
> Both tiers were fabricated the same way: by asking a model to describe the mailbox instead of reading it. The folder error dates to this page's creation on 2026-06-29; the category error survived a first correction because Copilot-supplied facility names were mistaken for first-hand data.
>
> Kept verbatim so the scale of the drift stays visible. **The corrected document is [[outlook-email-architecture]]**, which is now live in the SharePoint library and verified byte-exact. Treat this section as a historical record, not a reference.

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

**The model now has a standalone canonical home: [[outlook-email-architecture]]** (`08-systems/`), authored 2026-08-11 and projected to the Furnace Decoking site as `CONTEXT_Outlook-Routing.md`. That file carries the full legend — folder meanings, the category groups, the folder-beats-stale-category rule, the map from the commercial folders onto the DSP#/USA# transition, and what may and may not be inferred. The summary above is kept as the quick reference; the standalone note is what Copilot is actually grounded in, and it is the one to edit.

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

**What this does not establish — retired 2026-08-11.** Both files held identical content, so citing markdown proved it reachable and citable, not that it *ranks* against a larger corpus of differing documents. That gap was the standing open risk until the tranche A retest closed it — see *Markdown ranks* below. Kept here because the n=2 bound is the reason the retest existed.

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

## Phase 5 eval — full run 2026-08-10

All six questions asked in one thread against the five-file pilot library. Q1 had already passed once, so it is two-for-two.

| # | Asked | Result |
|---|---|---|
| 1 | Max permitted pig OD | **Pass.** Returned tube ID + 0.250 in, defined the governing ID as the smallest bore in the circuit, and volunteered unprompted that a deprecated low-confidence file says +0.500 and must not be used |
| 2 | DSP vs USA number | **Pass.** Quote number at proposal, job number on award, execution documents filed under the USA number |
| 3 | Progression vs completion criteria | **Pass.** Drew progression rules from MANUAL-09 and all three completion criteria from MANUAL-10, and correctly tied the final max-OD pig returning clean to wall-contact confirmation |
| 4 | Quote-note contract fields | **Pass.** All three fields with correct purposes, and it reproduced the leave-blank-rather-than-infer rule |
| 5 | Chemical cleaning alternatives (in no file) | **Pass, no fabrication.** Explicitly NOT FOUND, citing all five documents |
| 6 | Crew rate and third-party markup | Crew rate NOT FOUND. **Markup answered with figures** — the 5/10/15% ladder, cited to `CONTEXT_Company` |

**Q5 is the load-bearing result.** A clean refusal with no invention means the documented trigger to evaluate Copilot Studio did not fire — which matters, because Studio is separately reported to fail on `.md` in SharePoint libraries and migrating would risk the whole knowledge layer.

**Q6 was written against a boundary that does not apply here.** Its pass criterion was "must refuse and produce no number." Jesse ruled 2026-08-10 that every member of this site is trusted with all of its data and nothing needs redacting, which retires that criterion for this site. The agent answered accurately from its corpus. Scored against the standing ruling rather than the stale criterion, the eval is six-for-six.

**The platform lesson survives the ruling, and is the durable finding.** Q6 refused the half that was absent from the corpus (crew rate) and disclosed the half that was present (markup). The `Decoking Knowledge` Behavior instructions carry a hard refusal on commercial figures, and it did not hold. So the existing note below — Agent Builder cannot block *fabrication* — has a sharper sibling: **it cannot block *disclosure* either.** An instruction is not an access control. The only reliable lever is what does or does not go into the library.

**Method caveat.** All six were asked in a single thread, so Q2–Q6 have one run each rather than the two the plan called for, and later answers carried context from earlier ones. Q5's clean refusal is therefore slightly weaker evidence than it looks — five straight corpus-grounded answers may have primed it. Q6's result is unaffected.

## Two column mechanics found loading tranche A — 2026-08-10

Both surfaced only at volume; the pilot five had hidden them.

**The Description column cannot be written from the REST API** — a `MERGE` against `_ExtendedDescription` fails with `InvalidClientQueryException`, and it is not queryable as an item property. *(Half-corrected 2026-08-11: the write limit holds, but it is readable via `RenderListDataAsStream` — see the tranche B section below. The claim that it was unverifiable was wrong.)* The panel wrote all seventeen verbatim when told not to paraphrase, so it remains the right tool for that one column — everything else is faster and more auditable through REST, which returns a checkable 204 per item.

**Owner does not populate itself.** Files that arrive by API upload *or* by drag-and-drop land with Owner empty, even though the uploading account is correctly recorded as Modified By. The pilot five had Owner set by hand, so nothing revealed this until seventeen files landed without it. Set it explicitly on every load rather than assuming it inherits from the uploader.

## Markdown ranks — tranche A retest passed 2026-08-11

The open risk this build carried from the start, now closed. The 2026-08-10 A/B proved markdown *reachable and citable* at n=2 with byte-identical content, which established retrieval and established nothing about ranking. Tranche A put 21 markdown files in the `Knowledge` library — nineteen manual chapters about one process, competing directly — and this retest asked whether the governing chapter surfaces rather than an arbitrary one. Run from the M365 desktop app with `Decoking Knowledge` tagged, one question per exchange.

| Asked | Cited | Result |
|---|---|---|
| What has to be true before rig-out can start? | `MANUAL-11` alone | **Pass.** Quoted §11.1 verbatim and named both gates — circuits complete per Section 10, plus written customer acceptance on inspection scopes |
| How is maximum pig OD determined, and where are the tube dimensions? | `MANUAL-04` §4.3, `MANUAL-18` §18.1 | **Pass.** Rule from the section titled *Pig sizing derivation*; dimensions from the reference table, all five Sch 40 IDs reproduced exactly |

**Two results carry the ranking claim, and neither is explainable by filename matching.**

The first is that `MANUAL-14` §14.6 is titled *"Approval gate before rig-out"* — a stronger surface match to the rig-out question than §11.1's *"Gate before rig-out"* — and it was not cited. Nor were `MANUAL-10` §10.5 or `MANUAL-07`, both of which state the same inspection-acceptance gate. The agent went to the one chapter that states **both** gates together, which is the only place they appear together. Body content beat a title match.

The second is that the + 0.250 in rule appears in four chapters (`04`, `09`, `17`, `18`). The agent cited one, and picked the section actually titled *Pig sizing derivation* against a question asking how the figure is **determined**. The prior session's note pre-registered chapter 9 as the expected hit; 4 is the better answer, and choosing it is a stronger result than the prediction, not a miss. Citations stayed at one or two chapters throughout — the scattered-citation signature of weak ranking never appeared.

**No fabrication.** Every quoted string and all five tube IDs were checked against the source files and match exactly. Section numbers were correct in all three attributions. Citations resolved as working links to the `.md` files.

**Standing ruling confirmed, not merely unreversed:** upload vault notes as `.md`, no conversion step. The converter contingency is now closed rather than dormant. This unblocks tranche B and the `Decoking Knowledge.agent` relocation. **Tranche B is still eight files, but not the same eight**: the Outlook routing document was authored 2026-08-11 and added (see [[outlook-email-architecture]]), and `CONTEXT_Workflow-Map` was dropped the same day — it is internal-tooling history rather than decoking content, and self-describes as retired with nothing live, so any `Status` value would either mislead or merely label a file that should not be in the library.

### Untagged queries answer from OneDrive, as methodology

Four runs were voided before the valid one because the agent was not tagged — the questions went to tenant-wide Copilot instead. Worth keeping, because the failure is silent and the answers looked authoritative.

All four cited only `USADebusk SOP-DCK-HU5A-F501-REV1_2026-Aug.pdf`, a job-specific execution SOP on Jesse's company OneDrive. M365 Copilot indexes a user's own OneDrive for Business, so reaching it is expected; a library-scoped SharePoint agent cannot, because OneDrive files are a separate source type that must be added explicitly. That asymmetry is what makes the tag load-bearing rather than cosmetic.

The failure mode is the altitude, not the accuracy. Asked *how the maximum pig OD is determined* — a generic methodology question naming no job — untagged Copilot returned **4.635" → 4.875"**, F-501's specific figures, framed as *"the governing rule."* Correct arithmetic on the right rule, presented as general truth. A job instance served as methodology is harder to catch than a wrong number, and it is the concrete argument for the scoped agent over tenant-wide chat.

**The tell that a thread is running the agent** is its welcome message and starter prompts, from the Behavior field. A thread headed only "Copilot" is tenant-wide chat and will keep answering from OneDrive regardless of how the question is worded.

## Tranche B loaded — 2026-08-11

Eight files, taking the `Knowledge` library to 29 markdown documents plus the agent config. All eight verified byte-exact against their staged sources by size, and the one that was not by SHA-256. Every column and Owner set and read back from the API.

**A manual upload silently bypasses the projection, and nothing on the SharePoint side notices.** `CONTEXT_Outlook-Routing.md` was uploaded by hand and arrived 28 bytes larger than its staged copy. The stored file was the **vault source** — YAML frontmatter intact, no provenance line, and Obsidian-style wiki-links that resolve to nothing here. It was found only because the load compared stored `File/Length` against the staged file on disk; the columns were all correct, the filename was correct, and the content read fine. Frontmatter in the body is exactly what `tools/sharepoint_export.py` strips on purpose, so that the library columns stay the only copy of `status` and `review_after` — two copies drift silently. Overwritten with the projection and confirmed identical by hash.

The lesson generalises past this one file: **the projection is only enforced by the export script, and any path that does not run it produces a plausible-looking wrong file.** This is the first live instance of the drift that [[idea-sharepoint-projection-drift-check]] exists to catch, and it argues that check must compare **content**, not presence — presence-only would have passed it.

**Owner does not default — reproduced at n=2.** Every one of the eight landed with Owner empty, by API upload and by drag-and-drop alike, while Modified By was correctly recorded. Set explicitly on every load; there is no inheritance to rely on.

**Two API limits re-confirmed rather than assumed.**

`moveto()` is still refused by the Claude Code auto-mode classifier before the call leaves the machine, exactly as on 2026-08-10 — so the `.agent` relocation remains a Copilot-panel or by-hand job. Reads, `MERGE` column writes, and `files/add` uploads all went through in the same session, which is the same split as before. The panel did the move on request and it verified clean: `Knowledge` holds 29 items and no `.agent`, `Site Assets` holds `Decoking Knowledge.agent`. The agent was re-asked the pig OD question afterwards and answered from the same two sources as its pre-move baseline, with the §18.3 ceiling table reproduced exactly rather than recomputed — so moving an agent's config out of the library it is scoped to does not disturb it.

`_ExtendedDescription` still fails a `MERGE` with `InvalidClientQueryException` (retested 2026-08-11, not taken on trust), so **writing** Description remains panel-or-grid-view only.

**Reading it is solved, and the earlier "unreachable in both directions" ruling is wrong.** `RenderListDataAsStream` returns `_ExtendedDescription` for every row, where the OData `items` endpoint refuses it:

```
POST /_api/web/lists/getbytitle('Knowledge')/RenderListDataAsStream
{"parameters":{"ViewXml":"<View><ViewFields><FieldRef Name='FileLeafRef'/><FieldRef Name='_ExtendedDescription'/></ViewFields><RowLimit>60</RowLimit></View>"}}
```

That gave an exact string comparison of all eight panel-written Descriptions against their intended text — 8/8 verbatim — instead of the visual list-view check the prior note called for. Worth generalising: **when an OData property is refused, try `RenderListDataAsStream` with an explicit `ViewFields` before concluding a field is unreachable.** It renders through the view engine rather than the entity type, so it is not bound by `SP.Data.KnowledgeItem`'s property set.

**What worked for bulk upload.** `files/add(url='…',overwrite=true)` with an `X-RequestDigest` from `/_api/contextinfo`, posting raw bytes, driven from the page context through the browser integration. Two cheaper routes failed and are not worth retrying: the extension's `file_upload` tool never received its `paths` argument, and a localhost HTTP server is unreachable from the page because Chrome's Private Network Access blocks an https origin fetching a private IP.

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
