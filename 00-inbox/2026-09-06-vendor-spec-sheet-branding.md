---
type: review
status: open
review_type: knowledge-gap
source_authority: session
confidence: high
created: 2026-09-06
review_after: 2026-12-06
related:
  - "[[equipment-library]]"
tags: [branding, vendor-documents, proposals, equipment]
---

# Putting the USADebusk logo on a manufacturer's spec sheet — what's fine and what isn't

A coworker asked on 2026-09-06 for the USA DeBusk logo on the Waterous CMU pump spec sheet, to
show that Trimax pumpers use Waterous pumps. The vault has no recorded answer to that question —
a grep for `nominative`, `trademark`, `co-brand`, `third-party document` and `vendor literature`
returns nothing — and it will be asked again, because every unit we build has purchased
components in it.

## The short answer

**Naming the manufacturer is fine.** Truthfully identifying a component supplier in our own
material is ordinary and protected. USADebusk already does it: `usadebusk-sop/SKILL.md:86` puts
"Waterous Pump" in the canonical flow path that goes into customer-facing SOPs.

**Re-branding their document is the part that creates a problem.** Their spec sheet is their
copyrighted work, and putting our logo on a page that already carries theirs produces a document
where a reader cannot tell who published it. That is true regardless of intent, and it is
gratuitous, because writing our own page costs about an hour.

**Facts are not copyrightable; expression is.** Lifting the model designation, the performance
ratings and the materials of construction onto a USADebusk sheet is fine. Lifting their layout,
prose, cutaway illustration or performance-curve graphics is not.

## The pattern that works

A USADebusk cover page — our logo, what the equipment is, a spec table naming the component and
its ratings — with the manufacturer's sheet behind it **unmodified**. Says the same thing, our
branding, no ambiguity, and it survives being forwarded on its own. Built as HTML → headless
Chrome `--print-to-pdf` → `pypdf` merge; the working example from this session is in the session
scratchpad, not the vault (Jesse: one-off).

Add a footer line naming the mark and disclaiming affiliation. A disclaimer does not cure a real
infringement, but it removes the ambiguity that would create one here.

## The Waterous-specific wrinkle worth remembering

Waterous's CMU sheet is titled **"SPECIFICATIONS: DECOKING/DESCALING: CMU"** and its opening line
markets the pump to "the pigging market." They publish it *for* firms doing what we do. Naming
them is the intended use of that literature, not a liberty taken with it.

That will not be true of every vendor document. It happens to be true of this one, and it is why
this particular case was the easy version.

## What would change the answer

Everything above assumes internal or single-customer distribution and no dealer agreement, which
is where we sit with Waterous (Jesse, 2026-09-06). Two things would change it:

- **Public distribution** — website, catalog, trade show. Manufacturers monitor that, and a
  permission request first is worth the email.
- **An existing dealer / distributor / OEM agreement.** If one exists it almost certainly contains
  a trademark-use clause that answers the whole question outright, and it governs over any of
  this. Check for one before reasoning from first principles.

Most OEMs also run co-branding or dealer-literature programs and will often say yes to a
co-brandable sheet if asked. That is the route that gets the original request granted outright.
