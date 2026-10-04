Before starting, run bash /workspace/setup/bootstrap.sh.

# Receipt Typesetting

Typeset a filled service receipt so typed text sits on the ink lines. The form layout is shared. The words on the ticket belong to one job. Do not freehand coordinates from a full-page preview, and do not copy another job's customer, crew, hours, or receipt number.

## Where files live

- Layout only (page size, field names, x, y, line_y, max_width, font_pt, align, receipt-number cover box): `/workspace/setup/forms/<form-type>.json`. This form is `/workspace/setup/forms/debusk-service-receipt.json`. That file has no filled-in words.
- Values only: `/workspace/jobs/<USA#>/` (for this form, `receipt-values.json` in that folder). Read the job number from the user or from the job folder you were given. If it is missing, ask for it before you fill anything.
- Size and density reference for this form (match visual weight only; do not copy its words): `/workspace/setup/forms/reference/debusk-service-receipt-density-reference.pdf` and `/workspace/setup/forms/reference/debusk-service-receipt-density-reference.png`.

If the current job folder lacks a value this ticket needs, stop and ask. Never borrow it from another job, from chat memory, or from an old filled PDF.

## Field-crop map

Coordinates are PDF points, origin bottom-left. `y` is the text baseline. `line_y` is the ink line.

When the layout is missing or a line looks wrong:

1. Render the blank receipt and the density reference above at high DPI (about 200–300). Crop each field zone. Measure the blank line height and the gap to the next printed label.
2. Set font size to about 55–70% of that line height, and set the baseline so the type sits on the ink line. Write geometry back to the layout file only. Do not put job words in that file.
3. Match the density reference's visual weight. Do not copy its job words onto the ticket you are filling.

Hours sit left of the printed HRS label, with a clear gap. Shift Summary wraps on the ruled lines under the printed label, never on top of it. Cover the printed receipt number on the scan, then draw the number from this job's values.

## Fill and check

1. Load the layout from `/workspace/setup/forms/`. Load values only from `/workspace/jobs/<USA#>/`. Join them by field name.
2. Draw vector text from that join, then flatten. Shrink a field only when it would overrun `max_width`.
3. Auto-render and spot-check crops before sending: receipt number, operators plus HRS, Shift Summary, supervisor plus hours, per diem and DEF. If text clips a label, sits off the ink line, or looks thin next to the density reference, fix the layout and re-render. Do not deliver on a failed crop.

Example (USA26046) - do not reuse values: that job's words are only in `/workspace/jobs/USA26046/receipt-values.json`.
