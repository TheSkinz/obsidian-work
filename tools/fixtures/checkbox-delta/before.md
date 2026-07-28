---
type: review
status: superseded
review_type: proposal
created: 2026-06-26
---

# Fixture: CHECKBOX-DELTA pair

An already-closed review note. `status: superseded` is what arms the rule: the
gate is the status in the BEFORE revision, not the after. Closing a review note
legitimately means ticking its boxes and setting the status in one edit — that
is the workflow. A record that was already closed changing its mind is not.

This pair is byte-identical except for a single character: proposal C's
`Approved` box is empty here and ticked in `after.md`. Nothing else differs, so
WORD-DELTA loses nothing across the pair, which is exactly the point — the two
rules cover different failures and neither shadows the other.

Note the repeated `Approved` labels. Comparison must be positional, because a
label-keyed map would collapse these three into one.

## Proposed Change

### A. First option

- [x] Approved
- [ ] Rejected

### B. Second option

- [ ] Approved
- [x] Rejected

### C. Third option

- [ ] Approved
- [ ] Rejected
