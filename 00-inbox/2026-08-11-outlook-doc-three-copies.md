<!-- vault-loop: no home yet, candidate for [outlook-doc-reconciliation] -->
<!-- vault-prestaged: skipped — already covered; this note already carries its own `type: review` frontmatter, a specific `revisit-trigger`, and a tracked row in 50-dashboards/health.md's Revisit Triggers table gated on "next session touching Outlook, Copilot grounding, or the OneDrive eviction." That event has not occurred since 2026-08-11. Adding a duplicate decision-queue row now would pre-empt the note's own designed gating rather than wait for the trigger it specifies. -->
---
type: review
status: open
review_type: cleanup
source_authority: session
confidence: high
created: 2026-08-11
review_after: 2026-08-25
revisit-trigger: "Next session touching Outlook, Copilot grounding, or the OneDrive eviction -> read Phase 1 Outlook Operating Procedure - Reference.docx, decide which of the three folder-structure documents survives, and check whether it holds the five email-rule bodies that exist nowhere else — event: check at the next M365 session"
related:
  - "[[outlook-email-architecture]]"
  - "[[overview]]"
tags: [copilot, outlook, sharepoint, duplication, onedrive]
---

# Three copies of the Outlook folder documentation, and Copilot prefers the one nobody maintains

Found 2026-08-11 while scoring the routing eval. A tenant search for `"Sent - Pending Response"` and
`"Waiting On Others"` returns three separate documents describing the same folder system:

| Document | Where | State |
|---|---|---|
| `Phase 1 Outlook Operating Procedure - Reference.docx` | `/personal/jutsey_usadebusk_com/Documents/Microsoft Copilot Chat Files/` | Accurate, unmaintained, **this is the one Copilot cites** |
| `CONTEXT_Outlook-Routing.md` | `sites/FurnaceDecoking/Knowledge/` | Accurate as of 2026-08-11, vault-sourced and maintained by `tools/sharepoint_export.py` |
| `Folder Structure` (Copilot chat page) | `/chat/pages/…` | Unexamined |

This is the exact failure `07-llms/copilot/overview.md` already documents — duplicate copies of one
document, where Copilot cannot tell which is current and cites whichever ranks higher. The
`Knowledge` library exists partly to prevent it, and the third copy was created **by this session**,
in that library, without first checking whether the tenant already had one.

## The decision owed

Which copy survives. The `.md` is the better long-term answer because it is a one-way projection of
a vault note and stays true as things change; the `.docx` is a frozen Copilot chat artifact in a
folder that accumulates junk, accurate today with nothing keeping it so. But the `.docx` currently
outranks it, so the unmaintained copy is what actually gets read.

**Do not delete the `.docx` before reading it.** Two things may live only there:

1. **What each folder means.** Its definition of `03 Sent - Pending Response` — "sent items awaiting
   a specific reply" — was quoted by Copilot and is correct. The vault's version of those meanings
   came from Jesse verbally on 2026-08-11, not from a document.
2. **The five email security rule bodies.** The vault records only that a five-rule architecture
   exists and that smtp.com in Rule 02A is an unaudited gap. If the rules themselves are written
   down anywhere, this is the likeliest place, and it would be the only copy.

Merge anything unique into the vault note first, then supersede. The chat page needs a look too.

## Why this note exists at all

Every error in the Outlook work this session came from describing the system instead of reading it —
folder names from a stale vault note, category names from Copilot's rendering, facility categories
that were never real, and finally the existence of prior documentation. A tenant search would have
answered the last one in one call, before a line was written. **Search the tenant for existing
documentation before authoring anything into the knowledge base.**

## Also unresolved, lower priority

`CONTEXT_Outlook-Routing.md` has never been cited by Copilot across three routing evals, though it
is confirmed indexed and does surface in raw search results. Corrected content did not change that.
If it is still uncited after the reconciliation above, the honest conclusion is that it does not earn
its place for mailbox questions however accurate it is — and that matters before any further
investment in the deferred Agent Builder declarative agent, which was justified partly on this
document's behalf.
