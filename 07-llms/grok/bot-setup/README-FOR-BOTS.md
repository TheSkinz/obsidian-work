# Orientation — read this before doing anything

You are one of several Bots on a shared cloud computer belonging to Jesse Utsey, technical
specialist at **USADebusk** (fired heater decoking and pigging, Deer Park TX).

## Where things are

| Path | What it is |
|---|---|
| `/workspace/vault` | Read-only clone of the USADebusk knowledge vault. **The authority for all domain truth.** |
| `/workspace/bids` | Working files for live bids and RFQs. |
| `/workspace/jobs` | Working files per job number (USA#). |
| `/workspace/out` | Finished artifacts staged for copy-out. Nothing is done until it leaves here. |
| `/workspace/scratch` | Disposable. Assume it will vanish. |

**Never edit anything under `/workspace/vault`.** It is a git clone and any local edit will be
destroyed by the next `git pull`. Read from it, write your outputs elsewhere.

Only `/workspace` persists. Temp directories and uncommitted state can disappear between runs, so
copy every finished artifact out to its real home and say where you put it.

## Messages between Bots are cut at 8000 characters, silently

A message you send to another Bot is truncated to the first 8000 characters with **no warning to
either of you** — measured, not guessed: a 10,232-byte payload arrived as an 8000-character prefix
and the recipient had no way to tell. The end of a long message is where conclusions, caveats and
safety boundaries usually live, so what gets dropped is exactly what matters most.

**So never hand another Bot content. Hand it a path.** Write your output to a file under
`/workspace`, then send the file path, the open questions and the next owner. That is already the
Bid Desk handoff contract and this is why it exists. If you genuinely must inline something, say how
long it is and put the conclusion first.

## How to find things in the vault

- `INDEX.md` — a generated one-line-per-note map of the whole vault. **Check it before claiming
  something isn't there.**
- `01-context/` — the standing context: `company-context.md`, `active-jobs.md`,
  `estimating-approach.md`, `equipment-fleet.md`, `output-preferences.md`. Read these early.
- `02-facilities/` — one card per heater, per facility. Physical facts plus accumulated actuals.
- `04-knowledge/` — the reference layer. `_canonical-heater-card.md` is the card schema.
  `manual/17-glossary.md` is the vocabulary authority. `sops/sop-formatting-standard.md` is the
  SOP formatting authority.
- `50-dashboards/health.md` — generated status of the whole system.

`[[double-bracket]]` links are Obsidian wikilinks; they resolve by filename, so `[[17-glossary]]`
means `04-knowledge/manual/17-glossary.md`. Use `grep -rn` to find the file.

## What Jesse is

A high-autonomy operator who does technical sales, proposals, estimating, engineering-document
analysis and field ops himself. Direct, correct answers. He does not want hand-holding, and he
does not want to be asked to confirm routine reversible things. He does want to be stopped before
anything irreversible or customer-facing.

## The one thing that gets you fired

Stating a domain number you did not read. Every rate, duration, tube count, pig size or dimension
must carry the vault file it came from. If the vault does not have it, say so and stop — do not
estimate one and present it as a fact.
