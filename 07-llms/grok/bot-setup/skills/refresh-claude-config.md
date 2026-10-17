# Refresh claude-config

1. Read the repo's main branch through the GitHub connector: the latest commit sha (list_commits, 1 result), then that commit's tree, recursively (get_git_tree). From the root tree, note the tree sha of `skills` and the blob sha of `CLAUDE.md`. The expected set is every blob under `skills/` plus `CLAUDE.md`.
2. Build a fresh copy in /workspace/claude-config.new, deleting any leftover there first. Fetch each text blob with get_file_contents at the commit sha. If a file in the current copy has a `git hash-object` equal to the blob sha, you may copy that file instead.
3. Binary blobs (images, docx and so on): download each with DownloadFile (user-Onedrive) from GrokBot-Backup/setup/claude-config-assets/<same repo path> into the same relative path. Put any binary with no asset copy on an "unmatched" list for the reply; never skip one silently.
4. Check: the file count in claude-config.new, not counting `skills/synced/`, equals the expected set, and every file's `git hash-object` equals its blob sha. If either check fails, stop, keep the old copy, and report.
5. Leave `skills/synced/` alone: neither copy nor delete it. It's Claude Code's own claude.ai account sync, which regenerates itself and is deliberately gitignored. If the current copy has `skills/synced/`, move it into claude-config.new/skills/synced/ just before the swap so it survives unchanged. For any other files in the current copy that aren't in the repo, list them in the reply.
6. Swap atomically: move /workspace/claude-config to /workspace/claude-config.old, then claude-config.new to claude-config. Confirm ~/.claude/skills and ~/.claude/CLAUDE.md resolve (`readlink -e`). Only then run `rm -rf claude-config.old`; if the links don't resolve, move .old back.
7. Write /workspace/setup/claude-config-sha.txt with exactly these lines:
   commit=<commit sha>
   skills_tree=<tree sha of skills>
   claude_md_blob=<blob sha of CLAUDE.md>
   copied=<YYYY-MM-DD HH:MM CDT>
8. Upload it right away with UploadFile (user-Onedrive, path GrokBot-Backup/setup, overwrite true).
9. Reply using the Handoff reply skill, with the sha file contents, the file counts, any unmatched binaries, and any extra files listed.

Write no tokens anywhere, and create no routines.
