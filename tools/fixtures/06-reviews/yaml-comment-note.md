---
type: insight
unit: 010 Brut #1
source: DSP #26035 Some Quote March 2026.pdf (quoted)
verified: convection confirmed. Not field-verified: launcher elevation
safe-because-quoted: "DSP #26035 Some Quote March 2026.pdf"
safe-because-no-space: DSP#26035 Some Quote March 2026.pdf
safe-because-url: https://example.com/path
safe-because-time: 08:30 start
last-updated: 2026-07-27
tags: [fixture]
---

# YAML comment truncation fixture

Trips YAML-COMMENT twice: `unit` truncates to `010 Brut` and `source` truncates
to `DSP`, because an unquoted ` #` opens a YAML comment.

The two `safe-*` keys must NOT fire — they are the control cases. Quoting is
the fix; closing the space is the other way out but is not what the rule asks
for.
