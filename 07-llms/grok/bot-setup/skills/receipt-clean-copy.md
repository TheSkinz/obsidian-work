Before starting, run bash /workspace/setup/bootstrap.sh.

1. Open the source receipt (PDF or image) and change only the values Jesse named for that receipt.
2. White out scribbles and crossed-out mistakes, then write the intended values so the form is readable for admin.
3. Leave every other field untouched. If the intended correction is ambiguous, stop and ask Jesse. Never invent a billable number, name, hours, Clean ID, pig size, or other field. Take customer, site, heater, work order, and crew from the receipt and from `/workspace/jobs/<USA#>/`. If that folder lacks a value, stop and ask. Never borrow a value from another job.
4. Save a PNG and a PDF under `/workspace/jobs/<USA#>/clean/` named `<USA#>-<Customer>-<Site>-<Heater/Unit>-<Receipt#>-<DAY|NIGHT>-<Date>-CLEAN.png` and the same basename with `.pdf`. Fill each part from the receipt and the current job folder. Attach both files in the reply.
5. Do not send the cleaned file to admin, email, SharePoint, or anyone else unless Jesse explicitly says so. Do not extract into a ticket table and do not treat the clean copy as the billing source of truth.

Example (USA26046) - do not reuse values: `USA26046-Cenovus-Lima-Vac170029-7095-NIGHT-Sept28-CLEAN.png` and `USA26046-Cenovus-Lima-Vac170029-7095-NIGHT-Sept28-CLEAN.pdf`.
