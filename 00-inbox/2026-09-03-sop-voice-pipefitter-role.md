---
type: finding
status: open
created: 2026-09-03
tags: [inbox, sop, skills, regression, needs-ruling]
---

# Is an SOP body a customer-facing document?

Surfaced by the 2026-09-03 F4 regression replay. Referenced by that baseline's `sop_voice_OPEN` frontmatter field, which is why this note exists — the field said the question was filed here and it had not been.

## The ambiguity

`9cddfaf` (2026-08-17) added the pipefitter role boundary to `usadebusk-sop`. It says two things that pull against each other:

> Who the fitters are is the customer's call… **Call them "the customer" in customer-facing documents**; USADebusk has no contact with them and no say in the selection.

while the same commit's own procedure steps write:

> **Customer's pipe-fitters** install USADebusk pig launchers on convection inlet flanges

So the rule prescribes one voice and the worked example uses another. The question is whether an SOP body counts as customer-facing.

## What the replay did

The run chose "Customer's pipe-fitters", matching the skill's own procedure text, and carried it at all three touch points — rig-in, rig-out, and the rig-over to pass 4. That reading is accepted for the current F4 baseline and recorded there. It is not a ruling.

## Why it is low-stakes but worth closing

Nothing numeric turns on it. But SOPs do go to the customer, and the reason the rule exists is that USADebusk has no contract with and no say over whoever the facility puts on the flanges — naming them as a distinct party in a document the customer reads implies a relationship we do not have. That is a real commercial reason, not a style preference, which is why the two readings are not simply interchangeable.

Against that: "the customer" alone is genuinely less clear in a procedure step. "The customer breaks the coil flanges" reads oddly when the customer is a refinery and the actor is a pipefitting contractor holding the turnaround award.

## For Jesse — one question

In an SOP body, does the pipefitter role read **"the customer"** per `9cddfaf`'s customer-facing convention, or **"the customer's pipe-fitters"** as that same commit's procedure steps write it? A third option, if both readings are half-right: keep "the customer's pipe-fitters" in procedure steps where the actor matters, and use "the customer" everywhere the party is being named rather than instructed.

Whichever way it goes, `9cddfaf` should be amended so the rule and its own worked example agree — that mismatch is what produced the ambiguity, and it will produce it again on the next SOP.

Related: [[2026-09-03-regression-battery-findings]]
