---
type: capture
status: inbox
created: 2026-07-20
tags: [capture, tooling, windows, docx-skill, infrastructure]
---

# Local toolchain expanded (Poppler, LibreOffice, Pandoc); found a Windows bug in the docx/pptx/xlsx skills' render helper

Session started from installing Poppler (`pdftoppm`/`pdftotext`), which had shown up as a failed tool call in
the CHS McPherson job report session (scanned-receipt PDFs). While at it, also installed LibreOffice and
Pandoc — LibreOffice specifically because the bundled `docx`/`pptx`/`xlsx` skills (anthropic-agent-skills
plugin) ship a render-and-verify step that shells out to `soffice`, and it wasn't on this machine at all.

All three now live on the user-level PATH (`oschwartz10612.Poppler`, `TheDocumentFoundation.LibreOffice`,
`JohnMacFarlane.Pandoc` via winget). Verified end-to-end: built a test `.docx` with python-docx, converted
to PDF with `soffice --headless --convert-to pdf`, rendered to JPEG with `pdftoppm`, visually confirmed
correct output.

## Bug found: `scripts/office/soffice.py` crashes on Windows

The skills' `run_soffice()` / `get_soffice_env()` helper (present in all three of docx/pptx/xlsx skill
folders under the anthropic-agent-skills plugin, both the plugin cache and the marketplace checkout) is
written for Linux sandboxes only — it probes `socket.AF_UNIX` to decide whether it needs an `LD_PRELOAD`
shim (compiled with `gcc` at runtime) to work around blocked Unix sockets. On Windows this throws
`AttributeError: module 'socket' has no attribute 'AF_UNIX'` immediately, before soffice ever runs — no
fallback, no except branch.

Confirmed reproducible: calling `python .../docx/scripts/office/soffice.py --headless --convert-to pdf
file.docx` on this machine crashes every time. Calling `soffice.exe` directly (bypassing the wrapper)
works fine once LibreOffice is installed and on PATH — that's the workaround in use for now.

## Why this matters

If any skill code path actually calls through `soffice.py` (rather than shelling to `soffice` directly) for
the render-and-verify step described in CLAUDE.md ("For UI or frontend changes... render and check" / the
docx skill's own render-before-done guidance), that step silently fails on Windows regardless of whether
LibreOffice is installed. Whether the skills actually invoke this wrapper in practice, versus some other
path, wasn't checked this session — only the wrapper script itself was exercised directly.

## To explore

- Confirm whether the docx/pptx/xlsx skill instructions (SKILL.md) actually route through `soffice.py` in
  normal use, or whether that's a Linux-sandbox-only code path that never fires locally.
- This is vendored plugin code (anthropic-agent-skills), not vault or claude-config content — not clear
  it's ours to patch even if it is a real bug; may be worth an upstream report rather than a local fix.
- No vault action needed unless a skill run is later observed silently skipping document verification on
  this machine — if so, this note is the reason why.
