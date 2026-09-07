# Company & Commercial Context
**Layer:** 01-context — loads every session
**Source:** Master Reference Module 1

---

## Identity

Legal/operating name: USADebusk. **House spelling of the closed form is `USADebusk`** — not `USADeBusk`, which is a dead string (Jesse, 2026-07-27; this reverses the 2026-07-12 skill-drift ruling that went the other way). The spaced form `USA DeBusk` is the legal entity name and keeps its capital B: reproduce it verbatim on customer-facing documents, contracts, and signature blocks, where `USA DeBusk, LLC` is the correct rendering of the family surname. Customer-facing on some accounts: "DeBusk Services Group," also unchanged.

**Canadian work trades as `DeBusk Services Canada`**, which has its own logo (do not rebuild it — use a `[logo]` placeholder Jesse self-replaces; see `04-knowledge/rig-diagram-corpus.md`). **This is a naming difference only.** The jobs are sold, planned, mobilized and executed exactly the same way as US work — same process, same methods, same estimating model. Different people are involved on the Canadian side, but that is staffing, not a separate operating model, and nothing about the workflow changes (Jesse, 2026-08-21).

Primary service: Furnace Decoking. Preferred terminology order: Furnace Decoking > Furnace Pigging/Decoking > Furnace Pigging.

Operating base: Deer Park, TX (corporate fleet and equipment staging). Primary markets: refineries and chemical/petrochemical plants.

## Key people

- **Jesse Utsey (jutsey@usadebusk.com):** Technical specialist — technical sales, proposal development, cost estimation, engineering-document analysis, field ops

## M365 access boundary — read before planning any work that touches company systems

**Claude Code cannot reach company SharePoint, M365, Outlook or Copilot** (company policy, tightened 2026-09-07). Not the Furnace Decoking SharePoint site, not Outlook mail, not the Copilot panel, not Graph, and not through a browser session — the Chrome-integration route recorded in `07-llms/claude/code.md` is closed along with the rest. **Do not plan work that assumes any of it, and do not propose building anything that reads or writes the tenant.**

What *is* readable: the **local OneDrive mirror** at `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\...`, which is where `rfq-intake-protocol` already tells you to record `## Source Files` paths. That has not changed and the recorded pointers still resolve.

Anything that exists only on the tenant reaches a session **because Jesse brought it** — he opens it, and hands over the file or the answer. That is the whole pattern. Ask him for it; never route around it. Full record: [[m365-access-boundary]].

## Document numbering

- **DSP#:** Quote number. Assigned at proposal stage. Format: YYNNN (e.g., DSP26001). Proposal workups filed in Jason's SharePoint folder — canonical-of-record, and **not reachable by a session**; the readable copy is whatever OneDrive has synced locally.
- **USA#:** Job number. Assigned upon award. Format: USAYYNNN (e.g., USA26001). All job execution documents filed under this number in Pigging Jobs folder on SharePoint — same boundary as above.
- **CAD#:** Job number for Canadian work (DeBusk Services Canada). Format: CADYYNNN (e.g., CAD25004, CAD26001). Same role as USA# — it is the job-number series, not a different scheme. **`CND` is not a valid prefix; there has only ever been one series and it is `CAD`** (Jesse, 2026-09-02: *"Rewrite everything. It was always supposed to be CAD. Never CND."*). **This reverses a ruling of 2026-08-21**, which held the opposite — that `CAD` was a misspelling of `CND` — and instructed sessions to convert `CAD` to `CND` at ingest. That instruction is withdrawn; **convert `CND` to `CAD` at ingest instead.** The reversal came from the company changing its position, not from a vault transcription error, so treat the 2026-08-21 entry as superseded history rather than as a mistake to explain. Expect `CND` in source documents written during the period the wrong convention was circulating.

## Commercial defaults

- Contract type: T&M on execution, Mob/Demob lump sum (~95% of jobs)
- Third-party markup: one of 5%, 10%, or 15%, set by the specific facility/project contract — no default. Always confirm before invoicing or proposing.
- Bid platforms: ARIBA, GED, or direct email per customer requirement

## Brand standards

Brand, font, type-scale, and color specs are canonical in the `usadebusk-core` skill (Brand Standards section). See there for the full spec.
