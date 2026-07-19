---
type: concept
tags: [workflow, quotes, jobs]
---

# Quote Lifecycle

This covers what happens when a quote is decided — won or lost — and how to create a job record when one is awarded. The front half — RFQ arrival through proposal submission — is [[rfq-intake-protocol]].

---

## Numbering Convention

- **Quotes:** DSP##### format — DSP + YYNNN (e.g., DSP26058)
- **Jobs:** USA##### format — USA + YYNNN (e.g., USA26001)
- **Facility ID** (for Dataview joins): Client-City-State string (e.g., Marathon-Garyville-LA) — must match exactly

---

## On Decision

Open the DSP##### quote note and update these frontmatter fields:

| Field | If Won | If Lost |
|---|---|---|
| `status` | `awarded` | `lost` |
| `awarded-as` | USA##### job number | leave blank |
| `lost-reason` | leave blank | short phrase (e.g., `price`, `competitor`, `no award`) |
| `date-decided` | YYYY-MM-DD | YYYY-MM-DD |

The `_pipeline.md` Dataview queries pull on `status` automatically — no manual dashboard update needed. Once the frontmatter is saved, the quote moves from Open Quotes to the correct section.

---

## The Three Field-Document Types

Three documents carry a job, and the distinction is what keeps each one trustworthy. Confirmed on USA26038, 2026-07-11.

The **job sheet** is static, created at bid-win from the quoted work-up. It is crew-facing and printable, and it holds the quoted resource plan plus how to key service receipts against it. It never carries actuals, status, or timeline. Schema authority: [[_canonical-job-sheet]]; template: `templates/_job-sheet-template.md`.

The **heater card** is persistent. It holds the heater's fixed physical facts plus actuals accumulated across every job on that unit. Schema authority: [[_canonical-heater-card]].

The **job report** is post-job. It carries the timeline and actuals for one job — what really happened, who was really there, real hours. This is where quoted-versus-actual gaps live.

The quoted resource plan and the mobilized crew routinely differ (USA26038 quoted 12 people, sent 10). That gap is a job report finding. Correcting a job sheet to match what happened destroys the only record of what was sold.

---

## If Awarded: Create the Job Sheet, Record on the Heater Card(s)

There is no standalone job note — the `03-jobs/` folder is retired and jobs dissolve into the heater card(s) they touch. On award, set `awarded-as: USA#####` on the source quote so the link carries forward; the operational record then accrues on each heater card as the job runs.

Create the job sheet at bid-win from `templates/_job-sheet-template.md`, saved as `02-facilities/<Client>/<City-ST>/<USA#####>-job-sheet.md` alongside that site's heater cards. Build it from the quoted work-up, not from any later revision — the billing math and section rules are canonical in [[_canonical-job-sheet]].

The heater card is the operational record. Job-level commercial data (revenue, cost, margin, crew) lives in the file estate, not the vault.

---

## After Award: active-jobs.md

Move the quote row from Pending/Bidding to Awarded/Pre-Execution in `01-context/active-jobs.md`. Update it again when the job mobilizes (move to Active) and when it completes (move to Recently Completed).

---

## Job Closeout

When the job completes, record the actuals on each heater card the job touched:

- Add the `## Job History` row (Job #, quote, dates)
- Fill the `## Task Durations` actuals row (elapsed hours, Rigs, Stand-By, Total — actuals only)
- Add the `### USA##### — Month Year` narrative under `## Field Notes`

Commercial close (revenue, cost, margin against the final ticket breakdown) is handled in the file estate, not the vault.
