---
type: idea-seed
status: researched
created: 2026-09-03
tags: [idea, job-report, fieldpm, writing, needs-ruling]
---

# Job-report summaries are not good enough yet

Idea seed captured 2026-09-03 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

> **BOTH HALVES ARE NOW ANSWERED. The structure half was back-tested 2026-09-03 and the three-move shape below was FALSIFIED — see "Structure half — back-tested and answered" at the foot of this note before reading the To-explore list, which is preserved as the question that was asked, not as live work.** The shape awaiting Jesse's ruling is **two moves, the second optional**. Nothing is written into `usadebusk-fieldpm/references/report-structure.md`.

**Jesse's own words, 2026-09-02:** *"I'm still not fully happy with any of the job report summaries we do. At some point in the future we need to figure out how we can perfect it, but this will do for now."* Said after four rounds of revision on the CAD26001 Project Summary, so this is not about one bad paragraph — it is about the class.

**Tentative read:** every generated table in the job report is solved; the prose is the one part still hand-fought each time. The CAD26001 rounds are the evidence and are worth reading before designing anything, because each correction names a failure mode rather than a preference:

- *"You don't 'carry to completion on effluent return'"* — invented phrasing that reads like jargon and means nothing to a reader.
- *"Sounds like you're describing the SOP"* — narrating **how the work is done** instead of reporting **what happened**. "Each circuit was pigged until the return water ran clear" became "each circuit was pigged until clean."
- *"No reason to reassert the technical data of the furnace. They know their own furnace"* — restating what the data table already carries, to an audience that owns the asset.
- *"Why even mention that flow tests are recorded before and after? Remove it."* — describing the report's own contents inside the report.
- *"Stop putting specific types of pig names"* and *"no reason to go into that much detail"* — operator-level granularity in a document for engineers and metallurgists.

**The through-line worth testing:** the failures are all the same shape — writing for a reader who does not know the plant, when the actual reader owns it. The summary's job may be much smaller than it has been written as: what was done, what was found, what it means for the next run.

**To explore:**
- Is there a house structure a summary should always follow, or is per-job judgement the point? A three-move shape (scope executed → condition found → what it means next) would be testable against the delivered USA26038, USA26041 and CAD26001 reports.
- Should any of this become skill content in `usadebusk-fieldpm`, or is a worked exemplar enough? The generator spec already owns tables and layout; prose is deliberately the PM's.
- **Back-test before building** (standing rule): reconcile any proposed shape against at least two structurally different delivered reports before it governs anything.
- Who is the reader of record? CAD26001 went to Syncrude reps — metallurgists and engineers. Confirm that generalises before designing for it.

**Gate:** none. Researchable now — the delivered reports and this session's revision trail are the corpus.

**Terminology half CLOSED 2026-09-03; structure half BACK-TESTED AND ANSWERED the same day — see the foot of this note. It is not open work; it is one ruling away from done.** [[2026-09-03-fouling-terminology-vocabulary]] carries the rulings and they are applied (DQ-030, closed same day). It settled the vocabulary, a **report scope rule written directly against the five corrections above**, and the reader question — answered as **one vocabulary vault-wide**, not a per-audience split. Jesse's ruling on that is the load-bearing input to what remains: *"the issues I've had with the job reports were more about verbosity and related concerns."* Four of the five corrections above are about **how much was said**, not which words; the fifth is an invented coinage. So the structure question is the remaining lever, and it is the bigger one.

### Handoff for the structure session

**Read first:** this note's five corrections, verbatim · `usadebusk-fieldpm/references/report-structure.md` § Prose Rules — six scope rules shipped 2026-09-03, which are the constraint any structure has to satisfy · [[2026-09-03-fouling-terminology-vocabulary]], so settled ground is not relitigated.

**Corpus — must be two structurally different delivered reports**, per the standing back-test rule:
- `02-facilities/HF-Sinclair/Artesia-NM/USA26038 Job Report.pdf` — delivered golden master, two heaters, one plugged pass, no smart pig on H-20
- CAD26001 Syncrude 7-1-F-1 — eight looped coils, smart-pigged, and **the report Jesse revised four times**. Not in the vault; open it from the OneDrive job folder
- `usadebusk-fieldpm/back-test/report_input_usa26041.py` and `report_input_usa25025.py` if a third shape is wanted

**The trap:** the answer is probably that summaries should be *shorter*, and a three-move shape can easily become a template that makes them longer by giving every job three headings to fill. The 2026-09-03 corollary applies — an observation nobody made is absent from the document, never reported as absent. A shape requiring all three moves on every job reintroduces the defect just banned.

**What settles it:** rewrite both delivered summaries under the proposed shape and compare against what shipped. **If it does not visibly shorten CAD26001's summary, it is the wrong shape.**

**~~Also open, and separate work:~~ CLOSED 2026-09-03.** `extraction-format.md` instructed the extractor to read a receipt's `Clean ID` as "maximum pig size run". The audit ran: **no corrupted value exists.** All nine `Clean ID` occurrences under `02-facilities/` are bores, each either matching its card's design ID or sitting *below* the largest pig that card records as run — arithmetically impossible under the pig-size reading. There is also no persisted extraction output to audit at all: `/extract` emits into the chat thread and nothing writes it to disk, so the only ingestion path is `usadebusk-vault-ingest` into those same nine rows. Three wording residuals were fixed (vault `f77690e`). The one live remnant of the wrong definition is `~/.claude/regression/frozen/f3-extract-output.md` — reported, not touched.

---

## Structure half — back-tested and answered, 2026-09-03

**The three-move shape is falsified.** "What it means next" appears in **none** of the four summaries in the corpus. Requiring it would add a move to every job, which is exactly the trap named above, and it cannot pass the falsifier — CAD26001 is already move one alone, so a three-move shape could only make it longer.

**The shape that survives: two moves, the second optional** (Jesse's ruling, 2026-09-03).

- **Move 1, always** — scope executed: what was performed, for whom, when, and the equipment arrangement that made it possible.
- **Move 2, only when it exists** — what the job found that the customer did not already know. **No deviation, no second paragraph**, which is why CAD26001 correctly has one. And **move 2 is a pointer, not a paragraph** — one sentence. USA26038's plugged Pass 4 tube is already in the H-20 `result`, but on a two-heater report a reader scanning the summary cannot tell which heater carried the surprise, so the defining event earns a sentence, never a paraphrase of equal length.

The cleanliness result and its joint basis move **out** of the summary into the per-heater `Decoking Analysis:` narrative, where `usadebusk-sop:102` can be satisfied without bloating the summary.

### The corpus, measured

| Report | Status | Shipped | Under the shape | Δ |
|---|---|---|---|---|
| CAD26001 Syncrude 7-1 F-1, 8 looped coils | delivered, 4 revision rounds | 106 w / 1 ¶ | 77 w / 1 ¶ | −27% |
| USA26038 HF Sinclair H-19/H-20, emergency | delivered, golden master | 139 w / 3 ¶ | 84 w / 2 ¶ | −40% |
| USA26041 ExxonMobil F-501, triple mode | delivered | 258 w / 4 ¶ | 119 w / 2 ¶ | **−54%** |
| USA25025 CHS McPherson, 9 heaters / 17 days | built REV 0, **never issued** | 105 w / 2 ¶ | not rewritten | — |

CAD26001 shortens, so the falsifier passes.

### The mechanism the back-test actually found

**The verbosity is structural duplication, not word choice.** USA26041's ¶2 restates its heater `result` nearly verbatim, its ¶3 opening restates the `callout` nearly verbatim, and its ¶4 restates the Stand-By Summary table's three causes. **Roughly 155 of its 258 words already live elsewhere in the same document.** USA26038's ¶2 does the same and is *worse than its own table* — the table carries four stand-by rows totalling 74 hours, the paragraph mentions two.

CAD26001 was already the shape. Its condition-found content sits in the heater `result` where it belongs, which is why it survived four rounds of cutting at one paragraph. Naming the shape does not change it; it stops the next report rebuilding the bloat.

### Two gaps found along the way

- **`report-structure.md:184-189` is the entire spec for this section** — a four-item content checklist generalised from USA26038 specifically, with no move order, paragraph count or length budget. The constraint layer (its § Prose Rules, lines 240-312) is dense; the structure layer is empty. That gap is what this note was opened against.
- **`usadebusk-fieldpm/SKILL.md:224-228`'s `/report` prompt never asks for the Project Summary at all.** It elicits the per-heater `result` and the flow sheets. Nothing in the workflow prompts the one piece of prose this note is about.

Also worth one line: **USA26041's heater `result` states "confirmed the clean" with no final pig size**, which now fails `usadebusk-sop:102`. The summary carried the 4.75" figure; the shape moves it to where the rule wants it.

### Status

**Propose-only — awaiting Jesse's ruling.** Nothing is written into `usadebusk-fieldpm/references/report-structure.md`. `render_job_report.py:552-563` iterates `project_summary` strings straight into paragraphs with no validation, so adopting this is a writing rule, not a code change — no generator work either way. The three rewrites themselves are in the 2026-09-03 session transcript; regenerate them from the shape rather than hunting for them.

Related: [[CAD26001-job-sheet]], the delivered CAD26001 report, and `usadebusk-fieldpm/references/report-structure.md`.
