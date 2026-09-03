---
type: note
status: inbox
created: 2026-09-03
tags: [inbox, owed, CAD26001, job-report, regression, schema]
---

# Open items left by the CAD26001 job-report session

Three items. None blocks anything today. The CAD26001 job itself is closed — report delivered, actuals on [[7-1-F-1]], both repos pushed (`049ce65`, config `320324f`).

Separate from [[2026-09-02-session-open-items]], which is the prior session's list and still stands.

## 1. Regression debt — F3 joins the queue

`~/.claude/regression/README.md` rule 2: after a substantive edit to any skill, replay the fixtures that load it **before the edit is trusted.**

This session made four additive changes and three bug fixes to `usadebusk-fieldpm/scripts/render_job_report.py` (`compact`, `section_order`, `pigs_override`/`_total`, `footer`/`logo_height`; plus fixed-table-layout, `keep_together` on all table builders, `h2` chaining). **Fixture F3 (`f3-receipt-input.md` / `f3-extract-output.md`) loads fieldpm and is now owed.**

Jesse ruled 2026-09-02 that the replay gets its own session rather than riding along. **Total owed is now F1, F2, F3, F4, F6.**

Mitigating, but not a substitute for replay: every new key defaults to prior behaviour, and this was verified by rendering CAD26001 with `footer` and `pigs_override` stripped — the footer reverted to Deer Park and the pig table to the workbook's raw sizes. `assert_structure --self-test` passes. What is *not* covered is the two US fixtures' own workbooks, which are not on this machine, so no US report was actually re-rendered.

## 2. Does the job-sheet PDF pattern survive?

`CAD26001-job-sheet.pdf` was **retired** 2026-09-02 (Jesse): it was eight days behind its HTML, including the reversed loop location, and there is no renderer in `tools/` to regenerate it faithfully.

That makes CAD26001 the exception. `04-knowledge/_canonical-job-sheet.md` and `templates/_job-sheet-template.md` both still prescribe HTML → PDF, and USA26038 and USA26040 both still carry PDFs — **which are exposed to exactly the same drift**, since nothing regenerates or lints them either.

Three ways it could go, and it is a schema decision, so Jesse's:
- Retire the PDF everywhere; the HTML is the printable and prints fine from a browser.
- Keep the pattern and add a generator to `tools/` so the PDF is reproducible rather than hand-made.
- Keep the pattern and add a lint rule that fails when a job-sheet `.html` is newer than its `.pdf`.

The third is cheapest and catches the actual failure. Doing nothing leaves two more stale PDFs nobody is watching.

## 3. DQ-017's queue row is out of date

The row defers the migration/tooling half of the heater-card schema bundle until "there are two cards of structured data instead of one."

CAD26001 delivered the **first populated `## Coilset Durations` section** — two rows on [[7-1-F-1]], TM5 and TM6, and the ft/hr answer the section was built to produce (124 / 144 against CAD25004's single-circuit 124). That is one card and one job, so the stated precondition is **arguably still unmet**, which is why Jesse scoped it out of the close-out.

What is owed is a status update, not a close: the row still reads as though nothing has landed. The remaining bundle — Pig Specs `Condition` column, vault-stats two tracks, the Rig-In mixed-method problem, the `Condition` split, the outlier-recording convention, and the rig-out mirror rule gated on it — is untouched.
