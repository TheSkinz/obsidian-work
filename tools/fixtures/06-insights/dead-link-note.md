---
type: review
status: open
---

# Dead link fixture

This links to [[no-such-note-xyz-fixture]], which exists nowhere.
Lint must flag DEAD-LINK on this file.

A link inside a code fence must NOT be flagged:

```text
[[also-nonexistent-but-fenced]]
```
