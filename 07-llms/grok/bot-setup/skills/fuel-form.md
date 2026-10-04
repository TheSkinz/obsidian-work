Before starting, run bash /workspace/setup/bootstrap.sh.

# Fuel Form

Fill the company fuel form from one scanned fuel receipt. Produce a draft PDF only. Do not email, upload, file to SharePoint, or send it to payroll unless Jesse explicitly says to send that file. Attach the finished PDF in the reply. `/workspace` is not safe storage.

Job values live with the job, never in this skill. Read `/workspace/jobs/<USA#>/` for the current job. If JOB/CUSTOMER or EQUIPMENT/UNIT is missing there and Jesse has not given it in this request, stop and ask. Never borrow a value from another job.

## Paths

- Template: `/workspace/setup/fuel-form-template.pdf`. It has no AcroForm widgets. If this file is missing, stop and tell Jesse. Do not invent a form. Do not modify the template file.
- Signature PNG (transparent ink, from the white-background scan that worked): `/workspace/setup/jesse-utsey-signature.png`. Never use a black or unreadable image.
- Working copy directory: `/workspace/out/fuel-form/`.
- File name: `YYYY-MM-DD-<station>-<store>-fuel-form-draft.pdf`, lowercase station and store number from the receipt.

## Steps

1. Run `bash /workspace/setup/bootstrap.sh`. Use `/workspace/.venv/bin/python` and PyMuPDF. Do not modify the template file.
2. Read the receipt. Take only what is printed: date, total, station name and address, gallons, price per gallon, card last digits, and odometer when the slip prints one. Never invent dollars, gallons, dates, mileage, or a job. Check gallons times price against the printed total and use the printed total.
3. Read the current job folder `/workspace/jobs/<USA#>/` for JOB/CUSTOMER and EQUIPMENT/UNIT. If either is not in that folder and Jesse did not give it for this receipt, stop and ask.
4. Rebuild page 1 from the template every time (do not overlay a PDF that already has text). Draw Carlito 12 pt on the blank lines, not over the labels. Append every page of the receipt after the form.
5. Place the signature image only when Jesse asks for that form to be signed. On page 1 only, draw `/workspace/setup/jesse-utsey-signature.png` on the employee signature line, to the right of the label, about x 218 to 315 and y 676 to 746 (PyMuPDF, origin top-left, letter page). Keep it off the liability paragraph and inside the page. Otherwise leave the signature line blank.
6. Verify with `pdftotext -layout` and a page-1 PNG. Each filled value appears once, except the name when it is also the bill-back. Receipt pages are still attached. Attach the finished PDF in the reply. Nothing was emailed or filed.

## Field by field

Standing values, the same on every fuel form:

- NAME: Jesse Utsey
- BRANCH: DS Pigging
- Bill Back to: Jesse Utsey

From the receipt only:

- DATE: the slip date as MM/DD/YYYY.
- MILEAGE: the printed odometer. If the slip has no odometer, leave it blank and ask.
- COST: the printed sale total, after the `$` already on the form. Do not type a second dollar sign.
- COMMENTS: two short lines. Line 1 is station, store number, and address from the slip. Line 2 is product, gallons, price per gallon, and card last four from the slip.

From the current job folder `/workspace/jobs/<USA#>/`, or from Jesse in this request. If missing, stop and ask. Do not reuse another job.

- EQUIPMENT/UNIT #
- JOB/CUSTOMER: the job number and the customer and site named in that folder.

HRS stays the template's printed N/A unless the job folder or Jesse gives hours.

## Do not

- Do not touch service receipts. Ledger extracts them, Forms owns blank ones, Clerk cleans scribbled images.
- Do not forge a signature. Use only the saved PNG, and only when Jesse asks.
- Do not email or file the PDF unless Jesse says so for that file.
- Do not copy customer, job number, equipment, or dollar amounts out of the example below.

## Example (USA26046) - do not reuse values

One filled form, for illustration only:

- Receipt date 09/26/2026, odometer 13415, cost 62.63.
- Comments: Wawa #7219, 131g Breese Rd W, Lima OH 45806. Unleaded 15.431 gal at $4.059. Card ending 7255.
- EQUIPMENT/UNIT #: rental car. JOB/CUSTOMER: USA26046 Cenovus Lima, OH.
- File name: `2026-09-26-wawa-7219-fuel-form-draft.pdf`.
