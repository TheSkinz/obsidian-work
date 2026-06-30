---
title: Windows Configuration Notes
created: 2026-06-29
tags: [windows, onedrive, config]
---

# Windows Configuration Notes

## OneDrive KFM redirection trap

OneDrive Known Folder Move (KFM) silently redirects Desktop, Documents, and Videos to OneDrive-backed paths. The shell shows `C:\Users\Jwuts\Desktop` but the real path is under `C:\Users\Jwuts\OneDrive\Desktop`. Scripts and tools that use raw local paths diverge from what the shell resolves.

Practical consequence: any tool that constructs file paths from `%USERPROFILE%` may land in the OneDrive-synced tree rather than a truly local location. The vault path (`C:\Users\Jwuts\obsidian-work`) is outside the redirected folders and is not OneDrive-backed — it is managed by Obsidian Sync instead. See [[obsidian-setup]].

For any new tool or script that needs a local (non-synced) path: verify the resolved path before writing, especially for Desktop, Documents, and Videos targets.

## Shell environment

Claude Code runs Bash (via Git Bash / POSIX sh) for the Bash tool and PowerShell for native Windows operations. The two shells use different path conventions — forward vs. backslash — and mixing them in a single command chain can cause silent failures. Write paths explicitly for the target shell.

## Other config notes

(Placeholder — add Windows-specific configuration notes as they accumulate.)
