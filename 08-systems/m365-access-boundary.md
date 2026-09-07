---
type: reference
status: active
created: 2026-09-07
verified: 2026-09-07
tags: [systems, m365, sharepoint, outlook, copilot, access-boundary, governance]
related:
  - "[[company-context]]"
  - "[[rfq-intake-protocol]]"
  - "[[outlook-email-architecture]]"
  - "[[overview]]"
---

# The M365 access boundary

**Company policy tightened 2026-09-07 to block third-party tools from company systems. Claude Code has no access to the M365 tenant.** Jesse still has full access and uses it daily; it is simply no longer something a session can route through.

## What is cut

SharePoint online — including the Furnace Decoking site and its `Knowledge` library — Outlook mail, the Copilot panel and Copilot Studio, Microsoft Graph, Teams. **Every route, not just the API ones.** `07-llms/claude/code.md` recorded on 2026-08-10 that Chrome integration was "exactly one working path" to authenticated M365 apps; that path is closed too. There is nothing left to try, and a session that goes looking is burning turns on a dead end.

## What is not cut

**The local OneDrive mirror.** `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\<Client>\<Client City ST>\` with its `Bids\`, `Jobs\`, `Reference\` and `_History\` subfolders reads normally, because it is a folder on Jesse's disk rather than a call to Microsoft. This matters more than it sounds: it is the tree `rfq-intake-protocol` already mandates for `## Source Files` paths, it is where all 14 recorded bid/job pointers under `02-facilities/` point, and it is what `POINTER-DEAD`, the health dashboard's Bid-folder column, `presend_gate.py` and `backtest_workup.py` resolve against. **None of that changed.**

The distinction is the whole boundary: **a synced file on local disk is readable; the tenant it came from is not.**

## The working pattern

Jesse pulls, a session reads what he hands over. He opens SharePoint or Outlook himself, exports or screenshots or copies what is needed, and brings it into the conversation. A session's job is to use it, reason about it and record it — never to reach for it.

Two pieces of prior work got this right before it was forced, and they are the model:

- `06-reviews/2026-07-23-idea-research-workup-to-proposal-generator.md` concluded on its own that the deciding artifacts "live in SharePoint/OneDrive, outside what this loop or the vault currently ingests" and resolved to have Jesse pull them.
- `~/.claude/plans/handover-sharepoint-copilot-phase5-6.md` states plainly: *"Jesse runs the evals, not the session. Claude cannot reach the M365 desktop app… The session's job is to score them against the criteria below, not to run them."*

## What this does not change

**SharePoint is still canonical-of-record** for job documents and proposal workups (Jesse's ruling, 2026-07-22). That is unchanged and correct. What changed is that canon is now only reachable through him. The vault remains the index; the file estate remains the store; the recorded path remains the only pointer.

`tools/sharepoint_export.py` also still works — it is stdlib-only and writes to `_OUTPUTS/sharepoint/` inside the vault, so it never touched the tenant. It renders the projection; uploading it was always Jesse's manual step and still is. What it can no longer support is any claim about whether the live library matches, which is why its drift-prevention promise was withdrawn the same day.

## What was killed by this

Recorded so nobody re-plans it: **DQ-016** (the SharePoint projection drift check — its settled design was "REST-read live library content," which is now precisely impossible), the **M365/SharePoint operating skill** proposed in `idea-sharepoint-projection-drift-check`, the remaining items in `2026-08-10-sharepoint-kb-build-open-items` (recon, an Agent Builder declarative agent, heater cards as a SharePoint List, Copilot Studio), and four tenant-side plan files. The Chrome/REST operating manual in `07-llms/copilot/overview.md` is history rather than procedure.

⚠ **One content risk survives the closure.** `2026-08-11-outlook-doc-three-copies` records that an unmaintained `.docx` inside the tenant may hold the **only copy of five email-security rule bodies**. Closing that note does not retrieve them. If those rules matter, Jesse is the only one who can pull that file.

## Why this is written down rather than assumed

The vault has twice diagnosed the failure this note prevents: the 2026-08-20 architecture audit named *"check at the next M365 session"* as **"a note to a reader who never arrives,"** and six event-shaped triggers were retired 2026-08-21 for never having fired. A boundary that lives only in a session's head produces exactly that — parked work waiting on an event that cannot happen. The boundary is stated in `01-context/company-context.md` because that file loads every session; this note is the detail behind it.
