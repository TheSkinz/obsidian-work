<!-- vault-loop: operational — document storage/canonical-location question for a live customer-facing form. Capture loop cannot rule on it. -->
---
type: note
status: open
created: 2026-08-17
tags: [loose-end, document-management, sharepoint, forms]
---

# The change order form has no canonical home, and the superseded copy sits beside it

A coworker needed a fillable Word change order form on 2026-08-17. One was built as REV001 and saved
to `Desktop\Revamped Docs\USADeBusk_Change_Order_Form_REV001_EDITABLE.docx`, with the logo extracted
from the source PDF so it carries the real asset rather than a placeholder. All ten checkboxes are
Word content controls, verified clickable. The build technique is recorded in
[[windows-config]]; this note is about where the file lives, which is unresolved.

**The vault has no change order template at all** — only narrative mentions inside job notes. A
`.docx` form does not belong in `templates/`, which is markdown note scaffolding, so creating one
there would be the wrong fix. The likely right home is SharePoint alongside the other job forms with a
pointer note in the vault, matching how job docs and workups are already indexed by path. That is a
storage-convention call, not a capture-loop call.

**A superseded copy is adjacent to the new one.** `OLD_USADebusk Blank Change-order.docx` is still in
the same Desktop folder. Anyone browsing that directory can grab the pre-REV001 layout by mistake.
Deleting or moving it is a file operation this loop does not perform.

Both items were raised in-session and left undecided.

Source: Claude Code session `1f31f1dc`, 2026-08-17.
