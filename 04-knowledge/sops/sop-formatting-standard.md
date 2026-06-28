# SOP Formatting Standard
**Layer:** 04-knowledge/sops
**Authority:** Derived from completed production SOPs (70H1 Marathon Detroit, F-901 ExxonMobil Baytown, F-802 ExxonMobil Baytown PS8). Supersedes the section structure listed in the Technical Docs system prompt.

---

## Document naming

`USAD-[Client Abbrev]-SOP-DCK-[HeaterTag]-[NNN]-REV[N]`

Examples:
- `USAD-Marathon_Detroit-SOP-DCK-70H1-001-REV0`
- `USADebusk_PS8_F-802_Decoke_SOP-DCK-F802-001_REV0`

---

## Page layout

- Font: Helvetica throughout; Arial fallback for DOCX only
- Paper: US Letter, 1" margins
- Running header: document number right-aligned, subtitle (Mechanical Decoking | [Heater] | [Facility]) below in lighter weight
- Footer: "DeBusk Services Group | Deer Park, TX" left-aligned, page number right-aligned
- Color scheme: gold (#FCC30A) for section divider horizontal rules and subsection header text; charcoal/black for body text and primary table header fills
- Punctuation: no em dashes in body text or customer-facing language

---

## Title block (page 1)

```
[Gold label, caps] MECHANICAL DECOKING OF
[Large bold] HEATER TAG / FURNACE NAME
[Italic] Operational SOP | USADeBusk | [Facility Name]

[2×4 grid table]
PROJECT          | HEATER              | DOCUMENT NO.     | REVISION
[Facility]       | [Heater tag + name] | [SOP-DCK-xxx]    | REV 0
CONTRACTOR       | DOCUMENT TYPE       | PREPARED BY      | DATE
USADeBusk        | Execution SOP       | Jesse Utsey      | [Month Year]
```

Header table: label row cells = dark charcoal fill, white bold text. Value row cells = white background, normal weight.

---

## Section structure

Sections are numbered. Subsections use decimal notation (2.1, 2.2). Order adapts to job complexity — the structure below is the baseline. Add, remove, or reorder based on what the job actually requires.

### 1. Purpose and Scope
- Opening paragraph: establishes what this SOP covers, heater tag, facility, circuit count, key configuration facts (e.g., simultaneous pigging, TriMax mode, all connections size/rating)
- **Heater and Coil Specifications table** (gold subheader): Section / Metallurgy / Tube ID / Passes (or Coils) / Footage per Pass / Circuit Configuration

### 2. Safety and PPE Requirements
- Minimum PPE bullet list (ANSI/ASTM references, site-specific requirements)
- Subsections for job-specific configuration: second TriMax allocation, launcher/receiver configuration, water supply and effluent disposal. Each subsection gets a table where applicable.

### 3. System Configuration
- Equipment list table: Item / Description / Qty
- Includes TriMax Pumpers, Support Units, Crew Trucks, Launchers, Receivers, hoses, pigs

### 4. Operating Parameters
- Table: one column per circuit when circuits have different parameters; single column when all circuits share the same parameters
- Rows: Tube ID, Total Length per Circuit, Cleaning Medium, Operating Pressure Range, Maximum Pig OD, Pig Sizing Increment, Completion Criterion (≤ 3–5 seconds per pig pass)

### 5. Pig Progression Sequence
- Table: Stage / Pig OD / Type / Purpose
- Rows: Opening pass (foam) → Progressive decoking → Line-size passes → Oversized passes → Max oversized (tube ID + 0.250")
- Max pig OD is governed by the governing tube ID (typically radiant, which is smaller)

### 6. Procedure
Phase-based subsections labeled "Phase I — [Name]", "Phase II — [Name]", etc. Not numbered within the section.

Standard phases:
- **Phase I — Rig-In**: pre-execution requirements checklist (PTW, JSA, customer-installed hardware), USADeBusk rig-in sequence
- **Phase II — Mechanical Decoking**: simultaneous circuit operation, pig loading/launching, effluent observation, sizing progression, completion trigger
- **Phase III — Smart Pig Support** (when applicable): USADeBusk propulsion role only; vendor controls inspection; written approval gate before rig-out

For ExxonMobil / major operator jobs with oily water or hydrocarbon deinventory: add Phase I — Initial Flush & Pitch/Oily Water Removal before mechanical decoking phase.

### 7. Flow Test Procedure
- BEFORE flow test (baseline, prior to first pig launch): establish target GPM, record operating PSI per circuit
- AFTER flow test (post-cleaning, after final pig pass): match BEFORE GPM, record PSI — reduction confirms cleaning effectiveness
- GPM is the controlled constant

### 8. Completion and Demobilization
- Subsections: Dewater/Depressurization/Rig-Out + Waste Management
- Depressurize via bleeder valves, confirm zero pressure before disconnecting hardware
- Waste disposal per customer environmental protocols

### 9. Definitions
- Two-column table: Term / Definition
- Include job-specific terms and abbreviations (facility-specific ones like CV Station, WNRTJ, etc.)
- Standard terms always included: Pig, Foam Pig, TC Pig, Circuit/Pass, Launcher, Receiver, Diverter, Effluent, Fig. 200, Triple Mode (when applicable), TriMax Pumper, PTW, RFWN

---

## Callout boxes

Used for critical safety or sequencing gates. Border accent (left border or full border) with ⚠ symbol, bold text. Examples:
- "CRITICAL: Oily diesel water is prohibited from entering the filter press."
- "ExxonMobil Baytown representative written approval of SteadyFlux inspection data is required before dewatering, hose disconnection, or rig-out activity begins."

---

## Controlled document footer

Last line of last page (italic, small):
"This is a controlled DeBusk Services Group procedure. These requirements apply specifically to [Heater Tag], [Facility]. Document: [Document No.]."

---

## What this replaces

The Technical Docs system prompt (v2.1) defines two variants (A and B) with a prescriptive section list. That list is aspirational. Actual production SOPs use a phase-based structure that collapses, reorders, and extends sections based on job complexity. Variant B (stainless/compliance) additions — solution chemistry, nitrogen purge protocol, references section — still apply when triggered; they layer on top of this base structure.
