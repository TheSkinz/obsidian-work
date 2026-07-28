---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-07-28
review_after: 2026-10-28
related:
  - [[code]]
  - [[command-reference]]
  - [[cowork]]
tags: [claude, claude-design, design-system, reference]
---

# Claude Design

Anthropic Labs' prompt-driven visual tool — designs, prototypes, slides, one-pagers.
It matters here only because it has a real Claude Code integration, and because the
question "can I get at this from Claude Code" has now been answered once and shouldn't
need re-researching.

> **Provenance & freshness.** Verified 2026-07-28 against the Anthropic announcement,
> the Claude help center's *Get started with Claude Design*, and the live `DesignSync`
> tool schema in a Claude Code session. Beta / research preview, so treat the feature
> set as a dated snapshot — re-verify against the docs before relying on specifics.
> Follows the durable-capture convention in [[code]].

## What it is

A web and desktop product at `claude.ai/design`, also reachable from the Claude Desktop
sidebar. No mobile. Powered by Opus 4.7. Included on Pro, Max, Team, and Enterprise at
no extra cost, drawing on normal subscription limits rather than a separate meter.
Default-off for Enterprise, where an admin has to enable it in organization settings.

You hand it descriptions, screenshots, documents, or a codebase; it produces working
prototypes or slides; you iterate through conversation, inline comments, and direct
canvas edits. Export targets include Canva, PDF, PPTX, and HTML.

## The Claude Code integration

Two directions, and they are separate mechanisms.

**Handoff (design → code).** The Export button in Claude Design packages the work into a
bundle and sends it to Claude Code Web or a local coding agent. The point is that the
coding session continues from the actual design rather than reconstructing it from a
screenshot.

**`/design-sync` (two-way, on demand).** Run inside a Claude Code session. It pulls a
design system into the repo, or pushes components you built in Claude Code back into
Claude Design as reusable elements. It leans on the existing claude.ai login — sessions
without one use `/design-login` for a dedicated design authorization — and it lists only
the design-system projects you have write permission on.

Design systems themselves can be imported into Claude Design from a GitHub repo, a Figma
file export, or a raw upload of CSS variables, design-token JSON, or Storybook config.
Once one is attached, everything generated afterward inherits its colors, typography,
spacing, and component vocabulary, which is the stated defense against generic-looking
AI output drifting across projects.

## Mechanics worth knowing before running it

The sync is deliberately not a wholesale replace. It runs a `list → finalize_plan →
write/delete` sequence: you read the remote file list, lock an explicit set of paths to
be written and deleted plus the local directory uploads may read from, and only then can
writes happen. Anything outside that approved path list is rejected. That makes it safe
to point at a repo without worrying it will flatten the remote project, and it means the
review step is a real gate rather than a formality.

One-way door: a project's type is fixed at creation. Pushing to an ordinary project will
never convert it into a design system, so verify the target reads
`PROJECT_TYPE_DESIGN_SYSTEM` before pushing.

`/design-sync` and `/design-login` are harness built-ins — as of 2026-07-28 there is no
design plugin installed, no `design-sync` entry in `~/.claude/skills/`, and no
`~/.claude/commands/` directory. That matches the rule stated in [[command-reference]]:
native built-ins live in the binary, not in `~/.claude`, so a config grep will never
confirm one exists. Check the docs instead.

## Relevance to this vault

Low, and worth saying plainly so it doesn't get picked up as a tool looking for a job.
Claude Design is a UI and front-end design-system product. It does nothing for markdown,
and nothing for USADebusk deliverables — proposals, SOPs, and heater cards are governed
by `04-knowledge/sops/sop-formatting-standard.md` and the brand standards in
`usadebusk-core`, not by a component library.

The one plausible future use is a browser-based internal tool, the Shift-Delta Tracker
being the only candidate on the board. If that ever gets built as a web UI rather than in
Power Platform, a synced design system would keep its screens consistent with USADebusk
brand standards without re-specifying them each session. Until then there is nothing in
this repo to sync — it has no component library.
