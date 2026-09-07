---
type: reference
status: active
created: 2026-09-07
verified: 2026-09-07
tags: [systems, forms, templates, change-order, sharepoint]
related:
  - "[[obsidian-setup]]"
  - "[[2026-09-07-consolidated-decision-pass]]"
---

# Company forms — where the blank templates live

Blank, reusable company forms are **files, not notes**, so they do not live in the vault. `templates/` holds markdown note scaffolding and a `.docx` does not belong there. This note is the index: it records which copy is current and where it is, the same way heater cards index job docs and workups by path.

Ruled 2026-09-07 in [[2026-09-07-consolidated-decision-pass]]. The problem it fixes is not that a form was missing — it is that several generations of one form sat side by side in a personal folder with nothing saying which to grab.

## Change order form

**Current: `USADeBusk_Change_Order_Form_REV001_EDITABLE.docx`.** Built 2026-08-17 for a coworker who needed a fillable copy. All ten checkboxes are Word content controls, verified clickable. The logo is the real asset extracted from the source PDF, not a placeholder.

| Copy | Status | Notes |
|---|---|---|
| `USADeBusk_Change_Order_Form_REV001_EDITABLE.docx` | **current** | The one to send. Fillable content controls |
| `USADeBusk_Change_Order_Form_REV001.pdf` | current, flat | Fillable PDF of the same revision |
| `OLD_USADebusk Blank Change-order.docx` | **superseded** | Pre-REV001 layout. Retire it — anyone browsing the folder can grab it by mistake, which is the whole reason this note exists |
| `USA26022_Change_Order_v2.docx` | not a blank | A filled job-specific change order under `Tools\Templates\`, not a template. Different thing that reads like the same thing |

**Location:** `OneDrive\Desktop\Revamped Docs\` for the first three; the fourth under `OneDrive\Desktop\Tools\Templates\`.

**Owed, not done (2026-09-07):** the ruling was *SharePoint plus a vault pointer*, and this note is the pointer half. The forms have **not** been moved to SharePoint yet — that is a file operation on Jesse's own OneDrive/SharePoint and is his to run, since nothing in `tools/` uploads binaries and `sharepoint_export.py` projects markdown only. Until the move happens, the paths above are the truth. Update this table when it does, and retire the `OLD_` copy in the same pass.

**Before the vault had this note**, there was no change order template recorded anywhere — only narrative mentions inside individual job notes. A grep for `REV001` returned exactly one hit, the inbox note that raised the problem.

## The ruling predates the M365 access boundary — read this before doing the move

*SharePoint plus a vault pointer* was ruled on the morning of 2026-09-07. Later the same day, company policy blocked third-party tools from company systems ([[m365-access-boundary]]). **The ruling still stands and its reasoning is unchanged** — it was always about coworkers being able to find the current form, which is what SharePoint is for and what a Desktop folder is not.

But the move now carries a cost it did not have when ruled. The forms sit in the local OneDrive tree today, which a session **can** read; SharePoint it **cannot**. Moving the only copy therefore puts them out of reach for anything Claude-side — confirming which revision is current, reading the form to answer a question about it, or noticing that a fifth generation has appeared beside the four already here. None of that was part of the ruling's purpose, so this is not a reason to reverse it, only a consequence worth knowing before it surprises someone.

**The cheap hedge, if that matters: keep a copy in the local OneDrive tree rather than moving the only one.** That is the same pattern the boundary note describes — SharePoint holds canon, the local mirror is what gets read. Jesse's call; nothing is blocked on it either way.
