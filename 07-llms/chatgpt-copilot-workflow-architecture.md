---
type: source
status: draft
source_authority: secondary
confidence: medium
created: 2026-06-30
source_date: 2026-06-30
source_owner: ChatGPT deep research
related:
  - [[chatgpt/overview]]
  - [[copilot/overview]]
tags: [chatgpt, copilot, microsoft-365, sharepoint, agent-architecture, ai-workflow, source]
---

# ChatGPT + Microsoft 365 Copilot — Workflow Architecture Operating Manual

## Origin

ChatGPT deep-research report, delivered as `deep-research-report.md` on `C:\Users\Jwuts\OneDrive\Desktop`, ingested 2026-06-30. Not yet reviewed against live tenant behavior — treat every claim below per its stated Evidence class (documented capability / tenant-admin-dependent / preview-rolling-out / inference-recommendation), per [[knowledge-system-governance]]'s source hierarchy (AI summary/unreviewed import — never canonical without review). This note extends and cross-links the existing [[chatgpt/overview]] and [[copilot/overview]] notes rather than duplicating them; where this report repeats guidance already recorded there, the shorter existing note remains the quick-reference version and this is the full-depth backing source.

## Executive recommendation

The best default setup for a solo power user is a **combination**, anchored by a **ChatGPT Project** as the long-running command center, with **normal chats inside that project** for ongoing design work, **scheduled tasks** for recurring monitoring, and **selective use of a Custom GPT or Skill only after repeated patterns stabilize**. Projects are the strongest fit for persistent context because they keep chats, files, instructions, and project memory together; Custom GPTs are better for reusable packaged behavior across contexts; Skills are reusable workflows but are still beta and currently do not sync across products; Scheduled Tasks are designed for reminders, recurring runs, and change monitoring rather than for being the primary workspace.

**Recommended project name:** **AI Workflow Architecture Command Center**. That name is specific enough to keep future chats on-scope and broad enough to cover ChatGPT, Microsoft 365 Copilot, connectors, agents, automation design, governance, and platform comparisons. **Evidence class:** inference based on how ChatGPT projects are meant to organize long-running work and maintain targeted project context. (Note: [[chatgpt/overview]] already records a canonical project — "AI Workflow & Agent Architecture Lab" — covering nearly identical scope; reconcile the two names rather than running parallel projects.)

**Recommended first five chats inside the project:**
- **Platform capability ledger** for "what exists now" across ChatGPT, Microsoft 365 Copilot, Copilot Chat, Agent Builder, Copilot Studio, SharePoint agents, connectors, and tasks.
- **Tenant verification tracker** for licenses, admin controls, billing model, and governance checkpoints.
- **SharePoint knowledge architecture plan** for site/library design, naming, permissions, cleanup, and grounding quality.
- **Workflow pattern lab** for test cases, prompts, outputs, failure modes, and pass/fail notes.
- **Release notes watch** for tracking changes in OpenAI and Microsoft documentation and deciding when to refresh assumptions.
This structure matches the strengths of project memory and lets you separate stable operating knowledge from experiments and change tracking.

**Recommended files and artifacts to upload into the project:** a one-page operating charter; a tenant facts sheet; a decision log; an approved terminology glossary; a workflow catalog; a prompt style guide; current screenshots or exported notes of tenant-specific UI; and a "current-state vs preview" register. Keep it lean, because project files are plan-limited and performance is better when context is selective rather than bloated. ChatGPT projects support PDFs, spreadsheets, docs, images, and pasted text; file count limits vary by plan, and only 10 files can be uploaded at once.

**Recommended decision log structure:** use one entry per decision with these fields: date, question, current decision, evidence class, official source citation, tenant dependency, preview status, assumptions, risks, retest trigger, and owner. The most useful rule is to require every operational decision to be tagged as either **documented capability**, **tenant/admin-dependent**, **preview/rolling-out**, or **inference/recommendation**. That prevents a common failure mode: mixing a glossy announcement, a partial rollout, and a real tenant configuration into one false "fact." Microsoft explicitly notes that Copilot features roll out gradually within a tenant.

**Recommended low-friction default path:**
Start with **ChatGPT Project + web research + uploaded tenant notes + two Scheduled Tasks**. Add a **Custom GPT** only when your workflow instructions have stabilized and you want reusable packaging outside the project. Add a **Skill** only if you are on Business/Enterprise-style plans and a reusable workflow genuinely needs to be installed and reused; otherwise it adds governance overhead with limited personal benefit. Use **Microsoft 365 Copilot Agent Builder** only after your tenant and SharePoint knowledge architecture are verified. Move to **Copilot Studio** only when you need broader publishing, multistep workflows, custom integrations, lifecycle management, or stronger admin controls.

## ChatGPT project setup

**Current documented capability:** ChatGPT Projects are smart workspaces for long-running work. They support grouped chats, uploaded reference files, project-specific instructions, project memory, built-in tools, and selected connected apps. Project instructions override your global custom instructions inside the project. If you create the project with **project-only memory**, chats can reference other conversations inside that project but not conversations outside it. If you do not choose project-only memory at creation time, you cannot retrofit it later; you must create a new project.

**Best-practice project instructions:** keep the project instructions short, procedural, and auditable. The instructions should tell ChatGPT to separate documented facts from inference, identify tenant-dependent questions, prefer current official documentation, flag previews and rolling rollouts, avoid relying on model self-identification, and maintain a running assumptions ledger. This recommendation follows OpenAI's project-instruction model and Microsoft's agent-instruction guidance, which both emphasize focused, explicit direction rather than sprawling prose.

A practical starter instruction set is: "Act as my research and architecture copilot for ChatGPT and Microsoft 365 Copilot workflows. Separate documented capability, UI behavior, admin dependency, preview status, and inference. Prefer official docs updated within 12 months. Maintain a change log. Flag stale assumptions, license dependencies, rollout uncertainty, and security/governance risks. When I ask for workflow design, return platform choice, prerequisites, data sources, storage location, permissions, failure modes, and tests." **Evidence class:** inference/recommendation grounded in project instruction behavior and Microsoft instruction design guidance.

**How chats, files, memory, apps, and tasks interact:** project chats inherit the project's instructions and file context, and ChatGPT prioritizes project chats and files when you ask within the project. You can add files directly, save useful responses back into project sources, and use connected apps in project chats. Supported app links that can be added as project sources currently include Google Drive files/folders and Slack channels; apps can also be invoked from the tools menu in project chats. Scheduled Tasks, by contrast, are managed from a separate Scheduled page, have plan-based limits, can monitor for changes, and do not support GPTs. OpenAI's current help docs do not clearly document project-specific task scoping, so treat tasks as **adjacent automations**, not as part of project memory.

**Known limitations:** chats created with a GPT cannot be moved into a project; Projects inherit workspace restrictions, so if a workspace disables memory, deep research, voice, or other tools, they are disabled in projects too; project upload counts are plan-limited; and because product models change over time, continuing older conversations may not reproduce earlier behavior exactly. If you use Business or Enterprise features, app availability, permissions, and write actions may also depend on workspace admin settings.

**What should live inside the project:** durable research threads, decision records, current operating assumptions, workflow designs, source copies or notes you want ChatGPT to reuse, and structured tenant verification notes. **What should not live inside the project:** sensitive materials you do not want repeatedly referenced, temporary one-off explorations, large dumps of redundant files, outdated screenshots without dated labels, or whole instruction systems that belong in a reusable GPT or Skill instead of a single project. This is an inference, but it comes directly from the way Projects use accumulated context and memory.

**How to avoid stale project assumptions:** keep a "last verified" line in the project charter; maintain one chat called **Current assumptions and unknowns**; store every product/tenant claim with an evidence class; and rerun verification when release notes, licensing, or admin settings change. Microsoft's own release notes emphasize gradual tenant rollout, and OpenAI's own help content now changes quickly enough that unversioned screenshots go stale fast.

## Microsoft 365 Copilot capability map

**Copilot Chat:** Microsoft 365 Copilot Chat is included with eligible Microsoft 365 licenses and is the entry point into the Microsoft 365 Copilot experience. It is primarily grounded in web data, not organizational content, unless the user explicitly supplies files/content, uses Copilot Chat in Outlook, uses open content in supported app scenarios, or invokes an agent grounded in tenant data. It also provides enterprise data protection for prompts and responses at no extra cost, shown in the UI with a green shield. **Implication:** use Copilot Chat for broad rollout, web-grounded ideation, lightweight agent access, and low-friction entry; do not assume it behaves like full Microsoft 365 Copilot across all work data.

**Microsoft 365 Copilot app and full Microsoft 365 Copilot:** Microsoft 365 Copilot brings real-time responses that can include internet-based content and work content the user is authorized to access, and it delivers those responses inside app-specific contexts. **Implication:** for Outlook, Teams, Word, Excel, PowerPoint, and SharePoint workflows that depend on work context and semantic grounding, the full Copilot add-on remains the higher-fidelity option. Microsoft also states that chat behavior in Word, Excel, and PowerPoint varies by tenant configuration and license, which means screenshots or demos from another tenant are not enough.

**Agent Builder:** Agent Builder in Microsoft 365 Copilot is the fast, no-code path to build declarative agents using natural language, the Configure tab, or templates. Microsoft positions it for quick, straightforward projects and small-team scenarios. Your Microsoft 365 Copilot license includes the agents you build there, and those agents do not consume tenant Dataverse storage. Admins can control whether Agent Builder is available. **Implication:** use Agent Builder first for internal FAQ, role-based assistants, or scoped knowledge helpers when the audience is you or a small team and the logic is not complex. (Already recorded as settled guidance in [[copilot/overview]].)

**Declarative agents:** Declarative agents customize Microsoft 365 Copilot through **instructions, actions, and knowledge** while running on the same Microsoft 365 Copilot orchestrator and trusted AI services. Microsoft's instruction guidance is unusually important here: keep instructions inside the agent's actual instruction field, not in SharePoint documents, because knowledge content is not trusted instruction content and can be sanitized or manipulated; Microsoft also warns that model behavior can shift over time as newer GPT versions are introduced. **Implication:** treat the instruction field as configuration, not prose storage; version it deliberately.

**Copilot Studio agents:** Copilot Studio is a graphical, low-code platform for agents and agent flows with broader connectors, tools, workflows, deployment options, analytics, and lifecycle controls. Microsoft's comparison guidance says Agent Builder is for individuals or small teams, while Copilot Studio is for department, organization, or external-customer scenarios and for advanced capabilities such as multistep logic, approvals, branching workflows, custom integrations, and broader publishing. Makers need access to a Copilot Studio environment, and licensing can come from Microsoft 365 Copilot, pay-as-you-go, Copilot Credits, or standalone Copilot Studio paths depending on the scenario.

**Connectors, tools, and actions:**
- **Copilot connectors** ingest external content into Microsoft Graph, where it is semantically indexed and made available to Copilot for natural-language retrieval and citations. **Evidence class:** current documented capability.
- **Tools** in Copilot Studio let agents interact with external systems and perform actions in response to user requests or autonomous triggers. **Evidence class:** current documented capability.
- Microsoft's latest "what's new" pages show that **tool groups**, richer workflows, copying agents from Microsoft 365 Copilot into Copilot Studio, request-information workflow pauses, Agent Registration API, Copilot policy API, and interactive UI widgets are either new or preview features rather than long-established baseline capabilities. **Evidence class:** preview or rolling out.

**Researcher and Analyst:** Researcher is a built-in Microsoft 365 Copilot agent for deeper, multistep research across web and work content, producing structured, source-cited reports. Analyst is the built-in data-analysis agent. Microsoft's admin documentation says Researcher and Analyst are first-party Microsoft experiences that coexist with agents but are part of the core Copilot chat experience and do **not** fall under agent-related settings. **Implication:** governance teams should not assume that "agent settings" will disable or manage these the same way they manage user-created agents. **(New — not previously recorded in [[copilot/overview]].)**

**App-by-app workflow implications:**
Outlook is the strongest low-friction M365 entry point for triage because Copilot Chat in Outlook can access user mail, calendar, meetings, chats, and limited files within defined boundaries. Teams and SharePoint are strong collaborative surfaces because agent sharing and discovery now show up there, including SharePoint-originated agents. SharePoint agents are stored as `.agent` files in Site Assets/Copilots or in the current library folder, which turns governance of "content" and governance of "agents" into one problem. Word, Excel, and PowerPoint are powerful end-user destinations, but behavior varies by tenant and license, so workflow testing must include the destination app rather than only the authoring UI.

## SharePoint and OneDrive knowledge architecture

Treat **SharePoint as the core knowledge substrate** for Microsoft 365 Copilot and many internal agents, not as a generic file bucket. Microsoft's own security, privacy, and grounding architecture is explicit: Copilot and the Semantic Index respect the same user-based access boundaries already present in the tenant. That means retrieval quality, security, and user trust all depend on the quality of your SharePoint structure, permissions, naming, ownership, and cleanup. (Consistent with the existing "settled architecture" note in [[copilot/overview]]; this section adds the governance/permissions depth that note doesn't yet have.)

**SharePoint vs OneDrive boundary:** OneDrive for work or school is private by default unless the user chooses to share; it is best used for personal drafts, staging, scratch work, and files that are not yet ready to become shared organizational knowledge. SharePoint is the better home for collaborative, authoritative, team-owned material and for documents that should ground organizational agents or repeatable Copilot workflows. Microsoft's support content also notes that when a different team needs ownership, content can be moved from OneDrive to SharePoint. **Evidence class:** current documented capability plus inference/recommendation.

**Best-practice structure for Copilot and agents:** organize by **business domain or repeatable workflow**, not by individual employee or ad hoc folder sprawl. Prefer a stable site per function or program, a dedicated library per knowledge domain, and clear ownership rules. Use focused libraries and reasonably sized, current documents rather than giant dumping grounds. Microsoft's declarative-agent guidance says "relevance over quantity," recommends using SharePoint for structured/static knowledge, and explicitly says agents perform better when files are reasonably sized, focused, current, and accurate.

**Permissions matter more than prompts:** permissions on sites, libraries, folders, and files directly affect what Copilot and SharePoint agents can retrieve. Microsoft says the agent's responses depend on each user's permissions to the agent's data sources; if a user can access the agent but not the underlying site or library, the response will omit restricted content. Microsoft also recommends correcting broken permission inheritance on libraries and folders as part of the Copilot data-foundation work. **Evidence class:** current documented capability.

**Oversharing risk is the central SharePoint risk:** Microsoft's readiness guidance for Copilot explicitly says to prevent accidental oversharing in SharePoint and OneDrive, use data access governance reports, adjust sharing settings, and restrict access to sensitive content. Data access governance reports are designed to find sites with potentially overshared or sensitive content. **Implication:** do not deploy internal Copilot agents on top of a messy SharePoint estate and hope that prompt wording will save you.

**Restricted Content Discovery and Restricted SharePoint Search:** these are not the same thing. Restricted Content Discovery is a site-level control for limiting discovery of high-risk SharePoint sites in organization-wide search and Microsoft 365 Copilot-style discovery while permissions are being fixed; it does not change permissions and cannot be applied to OneDrive sites. Restricted SharePoint Search is explicitly documented as a **temporary measure**, not a security boundary, and Microsoft says it should be disabled after validation because long-term use harms user experience. **Recommendation:** prefer real permission remediation plus site governance first; use these as interim containment only. **(New — not previously recorded in [[copilot/overview]].)**

**SharePoint Advanced Management matters:** Microsoft's current licensing and governance materials make SAM materially relevant to Copilot deployment. Microsoft documents site ownership policies, inactive site policies, data access governance reports, AI insights for report interpretation, the SharePoint Admin Agent, and reports on agents created across SharePoint and OneDrive sites. A Microsoft 365 Copilot license also lists SharePoint Advanced Management among included capabilities. **Evidence class:** current documented capability; **tenant/admin-dependent** because actual usage still requires roles and admin configuration.

**Recommended cleanup checklist before deploying Copilot agents:** confirm site owners; eliminate ownerless sites; identify inactive sites; remediate broken inheritance; review sharing links and overly broad member access; archive or relabel stale/duplicate files; standardize file names; separate source-of-truth libraries from scratch libraries; and review reports for oversharing hotspots. Microsoft's site ownership policy and inactive-site policy documentation support the ownership and lifecycle pieces directly. **Evidence class:** inference/recommendation built from current governance guidance.

**Recommended repeatable pattern for workflow agents:**
- SharePoint site per business capability or program.
- Library per knowledge domain.
- Controlled set of approved source files or lists.
- Narrow, clear permissions at the site or library level rather than deep folder exceptions.
- A published "authoritative" library separate from a working-drafts area.
- OneDrive as short-lived prepublication staging, not long-term grounding.
This pattern is not a verbatim Microsoft template, but it aligns closely with Microsoft's guidance on selective knowledge, SharePoint grounding, site ownership, and permission integrity.

## Tenant verification and agent design best practices

**Tenant verification checklist:**
- **License baseline:** verify whether users have only an eligible Microsoft 365 license for Copilot Chat, or a full Microsoft 365 Copilot add-on license. Copilot Chat is included for eligible Microsoft 365 licenses; Microsoft 365 Copilot requires an add-on on top of qualifying base plans.
- **Agent economics:** if users are not Microsoft 365 Copilot licensed but need agents grounded in tenant data through Copilot Chat, verify pay-as-you-go or Copilot Credits for those scenarios. Tenant-data agents in Copilot Chat are metered and off by default for those users.
- **Agent Builder availability:** verify that admins allow the "Create an agent" entry point and that the relevant users have access.
- **Copilot Studio authoring:** verify environment access, maker permissions, and the right licensing path.
- **SharePoint/OneDrive/Teams/Outlook access:** verify that the target users can actually access the content you expect the agent to use. Copilot respects existing permissions; no agent grants new privileges.
- **Publishing and sharing permissions:** verify organization settings for sharing, allowed agent types, user access, and whether sharing requires admin approval.
- **Audit, DLP, retention, Purview:** verify auditing is enabled, DLP posture is reviewed, and retention settings for Copilot interactions are intentional.
- **Admin roles:** verify AI Administrator for Copilot controls, and SharePoint Advanced Management Administrator where SAM/SharePoint Admin Agent capabilities are needed.

**Native Copilot prompt workflow:** best for fast ad hoc work in Outlook, Teams, Word, Excel, PowerPoint, and the Microsoft 365 Copilot app. The setup cost is lowest, and governance is mostly inherited from tenant permissions and app controls. The risk is inconsistency, weak repeatability, and user confusion about what Copilot can see in each surface. Testing should compare the same prompt across the actual destination apps, because Microsoft documents app- and license-dependent differences.

**Agent Builder declarative agent:** best for internal knowledge assistants, project FAQ bots, onboarding agents, and role-targeted helpers where the audience is an individual or a small team. Setup is simple: choose **New agent**, describe it, or use Configure/template mode, then add focused knowledge and prompts. Risks include overscoped knowledge, poor instructions, and hidden license mismatches for users. Testing should include the built-in test chat, edge cases, and real app surfaces. Microsoft's own best-practice docs explicitly say to test in multiple apps and validate outputs against source material.

**Copilot Studio agent:** best for multistep business processes, approvals, custom integrations, external publishing, line-of-business workflows, or anything that needs lifecycle management and stronger administration. Setup should start with environment/access checks, then knowledge, tools/actions, and channel/publishing decisions. Risks include connector complexity, unsupported action patterns, metered cost, and governance fragmentation across admin centers. Testing should include authentication, consequential-action confirmation flows, logging, and channel-specific behavior. Known issues remain for some Power Automate action behaviors and custom metadata retrieval patterns.

**ChatGPT Project workflow:** best for design thinking, cross-platform comparisons, prompt refinement, and maintaining a living architecture dossier. Setup is very fast and requires no tenant admin. Risks are stale internal assumptions, source sprawl, and mixing "assistant memory" with actual platform truth. Testing is qualitative: require source-backed answers, keep a dated assumptions log, and periodically challenge the project with "what changed since last review" prompts using current official documentation.

**ChatGPT Custom GPT:** best when a workflow has stabilized enough to deserve a reusable packaged front end outside the project. GPTs support instructions, knowledge, capabilities, apps, actions, and version history. Risks are drift between the GPT and the project's current operating manual, plus the fact that GPT-originated chats cannot simply be moved into a Project afterward. Use this only after your operating patterns are mature.

**ChatGPT Skill:** best for repeatable, shareable work patterns that need consistent execution and may include instructions, examples, and code. Because Skills are still beta, plan-limited, and do not yet sync across products, they are a secondary optimization rather than the default home for this use case. Use them only when you already know the workflow is worth formalizing. **(New — not previously recorded; [[chatgpt/overview]] doesn't currently flag the beta/no-cross-product-sync caveat.)**

**Scheduled Task:** best for daily briefs, weekly release-note checks, and monitoring tasks. Tasks can remember previous runs, check for changes, and notify only when something meaningful happens. They are available on web and mobile for Plus, Pro, Business, and Enterprise users, have hourly frequency limits, and do not support GPTs. They are the right layer for "watch and notify," not for complex event-driven automation.

**Connector-based workflow:** in Microsoft 365, use connectors when you need external enterprise content indexed into Microsoft Graph and discoverable through Copilot; in ChatGPT, use apps when you want search, deep research, sync, or actions from connected systems. The biggest design decision is whether you need **retrieval only** or **retrieval plus writes/actions**. In either platform, admin settings and permissions determine what is actually available.

## Recommended workflow library

**Daily operations brief:** best platform is **ChatGPT Scheduled Task** for external product/news monitoring and **Microsoft 365 Copilot / Researcher** for internal work-content synthesis. Store reference documents and stable operating materials in SharePoint; keep personal notes in OneDrive until they are team-relevant. Required permissions are read access to the target sites and mail/calendar access if you want work context. Main failure modes are stale assumptions, preview features showing up in one tenant but not another, and overreliance on one source. Test with "no changes," "minor change," and "major policy update" scenarios.

**Outlook and email triage:** best platform is **Microsoft 365 Copilot / Copilot Chat in Outlook**. Use mailbox plus a SharePoint library of response standards or policy references. Store shared templates and approved guidance in SharePoint; keep personal draft replies in OneDrive until finalized. The main risks are lexical-only context in some Copilot Chat scenarios, accidental use of stale templates, and permission mismatches for shared mailboxes or files. Test cases should include urgent mail, ambiguous mail, missing attachment, and policy-conflict mail.

**Teams meeting recap:** best platform is **Microsoft 365 Copilot in Teams**, with SharePoint as the archive for meeting outputs. Store recurring meeting playbooks, decisions, and follow-up trackers in SharePoint lists or libraries; keep working notes in OneDrive if they are still personal. Required permissions are meeting/chat visibility plus access to the project site. Risks are incomplete context if the meeting artifacts are not captured consistently and duplicate notes across Teams, OneDrive, and SharePoint. Test on a recorded meeting, an unrecorded meeting, and a meeting with restricted follow-up files.

**SharePoint knowledge assistant:** best platform is **Agent Builder first**, moving to **Copilot Studio** if you need stronger controls or actions. The storage architecture should be a dedicated SharePoint site or library with clean ownership, narrow permissions, authoritative documents, and a defined publication process. Files grounding the agent should live in SharePoint, not in OneDrive staging. Risks are oversharing, broken inheritance, stale documents, and licensing gaps for users. Test with questions whose answers are known, with users of different permissions, and with one intentionally stale file to make sure the assistant does not surface obsolete material.

**Proposal and quote drafting assistant:** best platform is **ChatGPT Project** for design and iteration, then **Agent Builder** or **Custom GPT** depending on whether the center of gravity is inside Microsoft 365 or ChatGPT. Store approved boilerplate, product facts, pricing guardrails, and case studies in SharePoint; keep in-progress drafts in OneDrive until they are reviewed or approved. Required permissions should separate source materials from confidential pricing. Risks are hallucinated claims, outdated case studies, and accidental retrieval of wrong-region pricing. Test with missing data, competitor comparison, and red-team requests for unsupported claims.

**Project-risk extractor:** best platform is **Copilot Studio** if you need multistep evaluation or actions, otherwise **ChatGPT Project** plus manual review is sufficient. Use a SharePoint site for project documents, RAID logs, contracts, and governance references. Keep personal annotations in OneDrive until they become part of formal project records. Risks are implicit assumptions, incomplete source coverage, and false confidence from elegant summaries. Test with contradictory documents and with role-based permission differences to ensure the agent does not expose restricted risk material.

**File and document summarizer:** best platform depends on location. If the documents are already in Microsoft 365 and permission-controlled, use **SharePoint agents** or **Copilot in SharePoint**. If the work is cross-platform or comparative, use **ChatGPT Project**. Put durable source documents in SharePoint; use OneDrive for transient review packets. Risks are unsupported file types, giant files, duplicate versions, and poor naming. For SharePoint agents, file-type support is documented and still expanding, so test the exact file types you plan to use.

**Cross-tool research workflow:** best platform is a **combination**: ChatGPT Project for external platform comparison and synthesis, Microsoft 365 Researcher for internal-plus-web research, and Copilot Studio only if the workflow must become automated. Store official docs, product decisions, and approved screenshots in SharePoint once they become team assets; keep personal scans and rough notes in OneDrive. The main risk is confusing public vendor claims, current docs, and tenant-specific reality. Test with the same research question in both systems and compare citations, source freshness, and permission scope.

## Governance, maintenance, and implementation plan

**Governance and risk model:** the biggest risks are permission drift, overshared SharePoint content, stale source files, overbroad retrieval, and user confusion between "ChatGPT with connected apps," "Copilot Chat," and "full Microsoft 365 Copilot." Hallucinated citations and model self-reporting are secondary risks, but they matter most when documentation is thin or the feature is rolling out. In Microsoft 365, the official security boundary is still the user's actual permissions, not an agent prompt. In ChatGPT, apps and company knowledge also respect existing permissions and workspace controls.

**When to avoid automation:** avoid automation for consequential actions that change records, send external communications, or rely on unstable knowledge sources until you have explicit confirmation flows, audit visibility, and a tested exception path. Microsoft's declarative-agent guidance is clear that consequential actions must be designed carefully; Microsoft's known issues page also flags gaps around some actions and response behaviors. **Evidence class:** documented capability plus inference/recommendation.

**Maintenance and update strategy:** monitor these official sources at minimum: OpenAI Help Center pages for Projects, Apps, SharePoint app, GPTs, Skills, and Scheduled Tasks; OpenAI release notes; Microsoft 365 Copilot release notes; Microsoft 365 Copilot developer/extensibility "what's new"; Copilot Studio "what's new"; Microsoft 365 admin docs for agents; SharePoint Advanced Management docs; and Purview audit/compliance docs. Run a **weekly scan** for release-note deltas, a **monthly assumptions review**, and a **quarterly deep re-audit** of your workflow architecture. Trigger an immediate re-audit when licenses change, pay-as-you-go is enabled, a new agent is published, SharePoint permissions are remediated, or a feature graduates from preview.

**How to record UI changes:** maintain a dated screenshot and note log with fields for date, tenant, user role, screen, exact label seen, and "matches docs yes/no." This matters because Microsoft explicitly rolls features out gradually to subsets of users within a tenant before broader expansion. Separate **current operating state** from **preview watchlist** and from **historical announcements**.

**When to use Deep Research versus normal web search inside the project:** use deep research when the question cuts across multiple official sources, requires citations, or needs a fresh decision memo. Use normal web search for isolated checks such as "is this control now GA?" or "did this help article change last week?" This is an inference, but it aligns with OpenAI's own distinction between app-backed search, deep research, sync, and project use.

**Day one plan:** create the ChatGPT Project with project-only memory if available; load only a small starter pack of documents; create the five initial chats; add the project instruction set; start one tenant verification checklist and one SharePoint cleanup checklist; and create two Scheduled Tasks, one for OpenAI changes and one for Microsoft changes.

**First week:** verify tenant licensing, AI Administrator access, Agent Builder availability, Copilot Studio access path, pay-as-you-go status, and SharePoint governance reports. Test one native Copilot workflow, one Agent Builder agent, and one ChatGPT Project workflow against the same real-world use case. Capture what worked, what was tenant-dependent, and what failed.

**First month:** clean up the highest-risk SharePoint sites, confirm ownership policies or inactive-site policies, publish one narrow-scope knowledge assistant, and freeze one reusable drafting pattern into either a Custom GPT or a Skill if the repetition is proven. Do not broaden scope until permissions, naming, and source freshness are under control.

**Long-term rhythm:** one weekly release-note scan; one monthly decision-log review; one quarterly architecture re-audit; and a separate preview register so experimental features never silently become part of your standard operating assumptions. This is the simplest durable mechanism for staying current without turning the system into a full-time documentation job.

## Source appendix

**Projects in ChatGPT** — OpenAI Help Center — **Use:** project memory, instructions, sources, limits, sharing, and inherited workspace controls.

**Scheduled Tasks in ChatGPT** — OpenAI Help Center — **Use:** recurring tasks, monitoring tasks, limits, availability, and task/app behavior.

**Apps in ChatGPT** — OpenAI Help Center — **Use:** apps terminology, search, deep research, sync, and action patterns.

**GPTs in ChatGPT** and **Creating and editing GPTs** — OpenAI Help Center — **Use:** Custom GPT scope, components, knowledge, actions, and version history.

**Skills in ChatGPT** — OpenAI Help Center — **Status:** beta and plan-dependent — **Use:** reusable workflows, availability, admin controls, and limitations.

**SharePoint app in ChatGPT** and **Company knowledge in ChatGPT** — OpenAI Help Center — **Status:** current but workspace-dependent — **Use:** SharePoint OAuth vs sync, RBAC, company knowledge behavior, and app-based retrieval.

**Minimum requirements for Microsoft 365 Copilot Chat** and **Overview of Microsoft 365 Copilot Chat** — Microsoft Learn, 2026 — **Use:** Copilot Chat eligibility, license requirements, web grounding, and entry-point positioning.

**What is Microsoft 365 Copilot?** — Microsoft Learn, 2026 — **Use:** full Copilot work-content grounding and app-context behavior.

**Choose between Agent Builder in Microsoft 365 Copilot and Copilot Studio** — Microsoft Learn, November 18, 2025 — **Use:** primary decision framework for Agent Builder versus Copilot Studio.

**Agent Builder in Microsoft 365 Copilot** and **Build agents with Agent Builder** — Microsoft Learn, April/May 2026 — **Use:** governance, data storage, UI behavior, and builder flow.

**Declarative Agents for Microsoft 365 Copilot** and **Write effective instructions for declarative agents** — Microsoft Learn, 2026 — **Use:** instructions, actions, knowledge, instruction limits, and prompt-governance guidance.

**Copilot Studio overview**, **Add tools to custom agents**, and **Copilot Studio licensing** — Microsoft Learn, 2026 — **Use:** advanced agent capabilities, tools/actions, billing, and zero-rated Microsoft 365 Copilot scenarios.

**Data, Privacy, and Security for Microsoft 365 Copilot** and **Microsoft 365 Copilot data protection architecture** — Microsoft Learn, 2026 — **Use:** permissions boundary, semantic index, encryption, storage, and auditing.

**Get ready for Microsoft 365 Copilot with SharePoint Advanced Management**, **Data access governance reports**, **Restricted Content Discovery**, **Restricted SharePoint Search**, **Create a SharePoint site ownership policy**, and **Manage inactive sites using inactive site policies** — Microsoft Learn, 2026 — **Status:** tenant-dependent — **Use:** oversharing remediation, discovery controls, ownership, and lifecycle management.

**Audit logs for Copilot and AI applications** and **Use Microsoft Purview to manage data security and compliance for Microsoft 365 Copilot and Copilot Chat** — Microsoft Learn, 2026 — **Use:** auditing, retention, and compliance posture.

## Open questions and limitations

Some Microsoft extensibility pages require authorization to view fully, and UI behavior can differ by tenant, role, license, geography, and rollout stage. Microsoft's own release notes explicitly say Copilot capabilities roll out gradually to subsets of users within a tenant. For that reason, the most reliable operating posture is to treat anything not verified in your tenant as **tenant/admin-dependent** or **preview/rolling-out**, even when it is officially documented. The original report notes it did not rely on forum posts, vendor blogs, or model self-reporting to establish core capability claims.

## Follow-Up

- [ ] Reconcile project name: "AI Workflow Architecture Command Center" (this report) vs. "AI Workflow & Agent Architecture Lab" (already recorded in [[chatgpt/overview]]) — pick one.
- [ ] Fold the two "(New —...)" callouts above (Researcher/Analyst governance scope, Restricted SharePoint Search caveat) into [[copilot/overview]] as short additions.
- [ ] Fold the Skills beta/no-cross-product-sync caveat into [[chatgpt/overview]].
- [ ] Verify tenant-dependent claims against the actual DeBusk tenant before treating any of them as settled.
