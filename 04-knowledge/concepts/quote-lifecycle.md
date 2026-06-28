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

## If Awarded: Create the Job Note

1. Use the template at `templates/usa-job-template.md` (Ctrl+P → Insert Template in Obsidian)
2. File location: `03-jobs/[Client]/[USA#####].md`
   - Example: `03-jobs/Marathon/USA27001.md`
3. Set `quote: DSP#####` in the job note frontmatter to link back to the source quote
4. The `awarded-as: USA#####` field you set on the DSP note links forward

The job note is the operational record for the job from award through closeout. It collects execution dates, revenue, cost, crew, and post-job notes.

---

## After Award: active-jobs.md

Move the quote row from Pending/Bidding to Awarded/Pre-Execution in `01-context/active-jobs.md`. Update it again when the job mobilizes (move to Active) and when it completes (move to Recently Completed).

---

## Job Closeout

When the job completes, update the USA##### note:

- Set `status: complete`
- Fill in `date-end`
- Confirm `revenue`, `cost`, and `margin` match the final ticket breakdown

The `_revenue.md` dashboard pulls from `03-jobs` WHERE `status = "complete"` — it populates automatically once status is set.
