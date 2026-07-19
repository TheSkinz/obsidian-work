---
title: Microsoft Copilot — Overview
created: 2026-06-29
tags: [copilot, microsoft, email, outlook]
---

# Microsoft Copilot

Copilot is used primarily through Outlook (email triage and drafting) and as a reasoning layer over the Outlook folder/category architecture.

## Email architecture — three-tier model

**Tier 1: Outlook folders** — encode state (where is this email in its lifecycle?). Nine folders define the pipeline:

| Folder | Meaning |
|---|---|
| 01-Inbox-Active | Needs action |
| 02-Waiting | Sent, awaiting reply |
| 03-Proposals-Active | Open bids |
| 04-Proposals-Sent | Submitted, awaiting award |
| 05-Awarded | Award confirmed, job pending |
| 06-Execution | Job in progress |
| 07-Closed | Completed |
| 08-Reference | No action, retain |
| 09-Archive | Done, low-value |

**Tier 2: Categories** — encode meaning (what kind of thing is this?). Fourteen categories total:

- 7 lifecycle categories (Action Required, Awaiting Reply, Proposal, Awarded, Active Job, Closed, Reference)
- 6 facility roster categories (one per key customer / facility)
- 1 risk category (Flag: Risk / Review)

**Tier 3: Copilot** — the reasoning layer. Reads folder state + categories to answer questions like "what bids are pending for Valero?" or "what's outstanding from last week?" without manually searching.

## Outlook email security architecture

Deployed a 5-rule corrective architecture to fix email deliverability and sorting issues. Known gap: smtp.com in Rule 02A was flagged during design — confirm whether it's still a live gap.

## Agent creation

The concrete example built so far is the [[heater-extraction-agent]] — a Copilot-side architecture for extracting fired heater coil data from degraded engineering drawings, using SharePoint-hosted knowledge files and a separate Auditor agent pattern. Document further agent setups here as they occur.

## Sycophancy-reduction custom instructions

(Placeholder — document the custom instructions approach once finalized.)

---

## SharePoint vs. OneDrive — settled architecture

SharePoint is the primary knowledge substrate for anything that needs to be durable, shared, or agent-accessible. OneDrive is for staging and personal drafts only. Agents grounded in SharePoint can cite sources; agents grounded in OneDrive cannot be reliably shared or governed.

Full governance depth (permissions-over-prompts, oversharing risk, SharePoint Advanced Management, cleanup checklist) lives in [[chatgpt-copilot-workflow-architecture]].

**Restricted SharePoint Search is not a security boundary.** It's documented as a temporary containment measure only, meant to be disabled after validation — use real permission remediation and site governance first, not this as a standing fix. Distinct from Restricted Content Discovery (a site-level discovery control, doesn't touch permissions, can't apply to OneDrive).

## Researcher and Analyst — governance scope

Researcher (deep multistep research) and Analyst (data analysis) are first-party Microsoft 365 Copilot experiences that are part of the core Copilot chat experience — they do **not** fall under agent-related admin settings. Don't assume "agent settings" governance will manage or disable these the same way it manages user-created agents.

## Agent Builder vs. Copilot Studio

Use **Agent Builder** first for simple, declarative, read-only agents — lower friction, no admin overhead, sufficient for most grounding-plus-prompt tasks. Reserve **Copilot Studio** for advanced workflows, connectors/actions, governance requirements, and production deployment. Don't start in Studio for agents that could be built in Builder.

## Daily Ops Brief Agent — design constraint

Start read-only: grounded in SharePoint, Outlook, and Teams with citations enabled, no write actions. Add write actions only after the read-only version is validated on real data. This is the proven maturation path — build the audit loop before adding automation.

## Tenant-reality-first research pattern

Before designing any Copilot feature or agent, verify what the actual tenant exposes: model picker availability, agent creation access, SharePoint grounding, connector catalog, publishing options, admin constraints. Do not design around advertised features that may be behind a license gate or admin toggle. Discovering a capability gap after building against it is expensive.

## Outlook automation maturity path

Start with simple deterministic rules: sender and topic-based routing. Mature into facility/customer/project routing only after validating rules on real messages. Don't manually categorize long-term once rules are validated — the rules should do the work. Heavy rule systems built before real-message testing consistently over-fit to expected cases and miss edge cases.

## Agent boundary

Agents may read, analyze, summarize, and draft. They may not edit SharePoint source files without explicit per-task permission. This boundary should be hard-coded in agent instructions, not left to model judgment.

## Pricing boundary

Agents and automated outputs must derive pricing only from sourced inputs. Margin and cost language is restricted to conversations with Jason, Marshall, or Travis — not surfaced in agent outputs, reports, or any document that leaves those conversations.

## Copilot Chat memory

Copilot Chat does not have durable access to prior chat history across sessions. Anything worth retaining must be copied into a SharePoint file, notebook, or explicit handover prompt before the session ends. Do not rely on Copilot Chat to remember context from a previous conversation.

## Structured output preference

For multi-item status, comparisons, and project tracking: prefer ini/yaml-style or tabular structured output over verbose Markdown prose. Structured output is scannable, diff-able, and copy-pasteable into downstream tools. Default to this format whenever output will be reviewed quickly or reused.
