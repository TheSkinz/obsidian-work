---
type: concept
tags: [workflow, quotes, jobs]
---

# Quote Lifecycle

This covers what happens when a quote is decided — won or lost — and how to create a job record when one is awarded.

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

## If Awarded: Record on the Heater Card(s)

There is no standalone job note — the `03-jobs/` folder is retired and jobs dissolve into the heater card(s) they touch. On award, set `awarded-as: USA#####` on the source quote so the link carries forward; the operational record then accrues on each heater card as the job runs.

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
