<!-- vault-loop: no home yet, candidate for [sharepoint-kb-open-items] -->
<!-- vault-prestaged: skipped — already covered by [[07-llms/copilot/overview.md]]; build proceeded past this note (blocking markdown-vs-docx test passed 2026-08-10, Project Stage already dropped-with-trigger per the build plan, recon items 3-6 resolved by the agent build and tranche A/B loads). Remaining recon items 1 (verify Search and offline availability = Yes) and 2 (identify the 43 Copilot Knowledge items) are simple lookups, not decisions. -->
---
type: note
status: inbox
source_authority: primary
confidence: high
created: 2026-08-10
tags: [copilot, sharepoint, knowledge-system, open-items]
---

# SharePoint Knowledge Base — open items at 2026-08-10 close-out

Design session settled the architecture and wrote the build plan. Nothing has been built on the site yet. Verified Copilot mechanics were filed into [[overview]] (`07-llms/copilot/`); this note carries only what is still open.

**Plan:** `~/.claude/plans/create-a-new-session-effervescent-papert.md` — seven phases. Library-scoped SharePoint agent over one curated library; vault stays canonical as a one-way projection; Copilot's own proposed 10-folder standard was rejected (it duplicated the vault with no source hierarchy and put agent instructions in a knowledge library).

## Blocking test — start the clock first

**Markdown vs .docx retrieval.** Docs say `.md` is not an indexed file type; the SharePoint agent claims it reads markdown fine. Both can be true — direct file access and semantic retrieval are different paths. Save one vault note twice into a library as `TEST-A.md` and `TEST-B.docx`, identical content plus a unique nonsense token in each, wait 24 h (new docs on a multi-member site index daily), then query each token.

Both found → skip the converter entirely. Only B → every vault note converts to `.docx` on export and Phase 7 needs a real converter in `tools/`.

## Recon not yet done

Needs an interactive session with Chrome integration connected, or screenshots:

1. `Site settings > Search and offline availability` — must be **Yes** or column-metadata grounding does not work at all
2. What the 43 items in `Copilot Knowledge` are
3. `Site Assets > Copilots` — existing experimental `.agent` files and their configured scopes
4. `Knowledge Vault` column **types** (choice vs text — the agent gave names only)
5. **Does the document-library Copilot button offer "Create an agent"?**
6. **If so, the agent editor's Identity / Sources / Behavior sections**

5 and 6 are the ones that matter. Everything else in the plan is verified or cheap to correct; the instruction field is the one assumption still resting on documentation rather than on this tenant — and documentation already proved wrong once this session, on markdown.

## Open decision

Whether `Project Stage` belongs in the column set. Dropped from the spec because it is job lifecycle rather than note lifecycle, but if the library is ever meant to hold job-linked material (workups, quote notes, job sheets) it goes back and the schema changes more than it appears.

## Deferred, with triggers

- **Heater cards as a SharePoint List** — after Phase 5 passes. Hard limit of **1 list per agent**, so it is heater cards *or* actuals, not both.
- **Agent Builder declarative agent** — when the agent needs to reach Outlook mail or Teams. SharePoint agents cannot.
- **Copilot Studio** — if eval fabrication probes fail and Behavior instructions do not fix it. Only tier that can hard-block general knowledge.
- **OneDrive eviction** (~2,361 junk files, `~/.claude/plans/i-m-organizing-my-enterprise-robust-alpaca.md`) — independent; improves the desktop app, does nothing for a scoped agent.
