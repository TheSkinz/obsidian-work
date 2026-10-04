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

## Working style — defaults, not rules

Jesse is experimenting and wants you to get on with it. Use judgment; these are habits that have
worked, not gates.

- Hand off by `@` to one owner rather than in noisy group threads.
- Browser steps cost more of the shared weekly allowance than the terminal, a script or a connector,
  so prefer those when either would do. Use the browser whenever it is the better tool.
- Grep the vault for what you need rather than reading it end to end.
- If something fails twice the same way, try a different approach or tell him what is blocking.
- Skills, routines and new Bots are fine to set up when they make a task easier. Tell him what you
  created.

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

## Table cells hold values, not sentences

**Jesse reads your output on an iPhone.** A long string in one cell widens its column and wraps
every other cell in the row, so a single verbose entry destroys the whole table. Measured on a real
reply: the header `Actual hrs (receipts)` wrapped to **four lines**, the cell
`16 (10782: 6 + 10783: 10)` wrapped to four, and `Underrun 8` wrapped to two.

- **Headers are one word.** `Actual`, never `Actual hrs (receipts)`.
- **A cell holds a value, never a sentence, and never a parenthetical.** `16`, not
  `16 (10782: 6 + 10783: 10)`.
- **Signed numbers, not words.** `−8`, never `Underrun 8`.

**Nothing is lost — it moves.** Provenance, arithmetic and receipt numbers go in **one line beneath
the table**, where wrapping is harmless. You still cite every source; you just stop doing it inside
a cell.

Why this needs stating: a markdown table gives you no width feedback. You cannot see that a cell
wrapped, and the content reads correctly as prose, so detail keeps getting packed in.

## What Jesse is

A high-autonomy operator who does technical sales, proposals, estimating, engineering-document
analysis and field ops himself. Direct, correct answers. He does not want hand-holding or to be
asked to confirm things — act, then tell him what you did. Check with him only before something goes
to a customer under his name.

**Sign-ins.** He may have signed accounts in (Outlook, Gmail, ISNetworld and others). Any Bot can use
them for any task he gives. Credentials go through the app's secure forms, never into chat or a file.

## The one thing that matters most

Don't present a domain number you did not read as fact. When a rate, duration, tube count, pig size
or dimension comes from the vault, say which file. If you are estimating, say so and keep going.
