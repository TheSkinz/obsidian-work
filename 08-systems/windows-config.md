---
title: Windows Configuration Notes
created: 2026-06-29
tags: [windows, onedrive, config]
---

# Windows Configuration Notes

## OneDrive KFM redirection trap

OneDrive Known Folder Move (KFM) silently redirects Desktop, Documents, and Videos to OneDrive-backed paths. The shell shows `C:\Users\Jwuts\Desktop` but the real path is under `C:\Users\Jwuts\OneDrive\Desktop`. Scripts and tools that use raw local paths diverge from what the shell resolves.

Practical consequence: any tool that constructs file paths from `%USERPROFILE%` may land in the OneDrive-synced tree rather than a truly local location. The vault path (`C:\Users\Jwuts\obsidian-work`) is outside the redirected folders and is not OneDrive-backed — git is its sole sync/backup mechanism (Obsidian Sync retired 2026-06-30). See [[obsidian-setup]].

For any new tool or script that needs a local (non-synced) path: verify the resolved path before writing, especially for Desktop, Documents, and Videos targets.

## Shell environment

Claude Code runs Bash (via Git Bash / POSIX sh) for the Bash tool and PowerShell for native Windows operations. The two shells use different path conventions — forward vs. backslash — and mixing them in a single command chain can cause silent failures. Write paths explicitly for the target shell.

## Local document toolchain

Poppler (`pdftoppm`/`pdftotext`), LibreOffice, and Pandoc are installed user-level via winget (`oschwartz10612.Poppler`, `TheDocumentFoundation.LibreOffice`, `JohnMacFarlane.Pandoc`) and on PATH. Poppler renders PDF pages to images/text for visual verification of generated documents; LibreOffice (`soffice.exe`) converts docx/pptx/xlsx to PDF; Pandoc handles general format conversion. Verified end-to-end: docx built with python-docx → PDF via `soffice --headless --convert-to pdf` → JPEG via `pdftoppm` → visually confirmed correct.

Also: LibreOffice must fully exit between conversions — firing `soffice --convert-to` back-to-back in a shell loop silently converts only the first file or two. Drive it from Python with an explicit wait per file, not a shell loop.

Source: Claude Code session, 2026-07-20; wait-per-file gotcha confirmed 2026-07-25.

## Other config notes

(Placeholder — add Windows-specific configuration notes as they accumulate.)
