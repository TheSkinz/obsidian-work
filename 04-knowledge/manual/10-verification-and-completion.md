# 10. Verification and Completion

**Layer:** 04-knowledge/manual
**Source:** `~/.claude/skills/usadebusk-sop/SKILL.md` (Cleaning Completion Criteria), `04-knowledge/sops/sop-formatting-standard.md` (Flow Test Procedure)
**Manual:** [[00-manual-index]]

---

A coil is declared clean against measured criteria, not against opinion. This section states how that determination is made and what evidence supports it.

## 10.1 The flow test

The flow test is a pump curve measurement taken twice on every circuit: once at rig-in before the first pig is launched, and once after the final pig pass. The comparison between them is the primary quantitative evidence the job produces.

**Method.** The circuit is run at a target flow rate and the corresponding pump speed and operating pressure are recorded. The AFTER test is run at the same flow rate as the BEFORE test, **and in the same direction.** Both tests are run as the same closed loop — blue to red by default. Reversing direction between the two tests breaks the comparison the same way changing the flow rate does.

**Flow rate is the controlled constant.** This is the whole basis of the comparison. Holding flow equal and observing the pressure required to achieve it isolates the change in resistance of the coil itself. A test run at a different flow rate than its baseline measures nothing.

**Interpretation.** A clean coil offers less resistance. At equal flow, the pressure required after cleaning is lower than the pressure required before it. The magnitude of that reduction is the measure of what the work achieved.

| Test | When | Recorded |
|---|---|---|
| BEFORE | At rig-in, before the first pig launch | Pump speed, operating pressure, flow rate, per circuit |
| AFTER | After the final pig pass, before rig-out | Pump speed, operating pressure at the same flow rate, per circuit |

> **CAUTION.** The BEFORE test cannot be reconstructed once pigging has begun. A circuit that was launched without a recorded baseline can be cleaned, but the result cannot be demonstrated quantitatively.

**A flow test measures the resistance of everything in the flow path, not just the coil.** Any restriction between the pump and the coil is read back as coil resistance and cannot be separated from it afterward. That is why §8.2 states preconditions for the baseline, and why a reading that falls outside the pattern of the other circuits on the same heater is treated as a suspect measurement rather than as a finding about the coil. Section 8.2 carries the failure modes to check.

**When a test is suspect, the flow test is what failed — not the cleaning.** Do not read a weak or erratic Δ as evidence that a circuit was cleaned less well. The completion determination does not rest on the flow test alone; see §10.2.

<!-- GRAPHIC 10-1: before/after flow test comparison. Two pressure readings at the same GPM, before and after, with the delta called out as the cleaning result. A simple paired-bar or gauge-pair treatment reads better here than a pump curve; the point is the delta at constant flow, not the curve shape. -->

## 10.2 Completion criteria

Two criteria carry the completion determination, and a third corroborates it. The first two are cumulative and each covers what the other misses.

**1. Effluent discharge duration of 3 to 5 seconds or less per pass.** As the bore opens, the effluent slug following a pig shortens. A short, sharp discharge indicates the pig is displacing little loose material.

**2. Effluent runs consistently clear.** Consistency matters as much as clarity. A single clear pass following a cloudy one is not a result; clear effluent sustained across successive passes is.

**3. Measurable pressure reduction at equivalent flow rate between the before and after flow tests — corroborating.** Where both tests are valid, this is the instrumented confirmation of what the first two criteria observed, and it is the strongest single piece of evidence the job produces for the customer. It does not, on its own, decide completion.

The first two are observed continuously through the work, across every pass, by the crew running the circuit. The third is measured twice — once at rig-in, once at the end — and either measurement can be compromised by conditions that have nothing to do with the coil (§8.2). A circuit meeting criteria 1 and 2, whose flow test is invalid or unavailable, is complete; what is lost is the quantitative demonstration, not the cleaning. A circuit failing criteria 1 or 2 is not complete regardless of what the flow test shows.

The practical consequence: **the determination is made in the field, on effluent behaviour, and the flow test confirms it afterward.** Reversing that order — treating a Δ PSI figure as the thing that declares a coil clean — puts the decision on the least reliable of the three.

## 10.3 Why all three

Each criterion alone can be satisfied by a coil that is not clean. Effluent can run clear because a pig is passing through a bore it is no longer contacting. Discharge time can shorten for the same reason. And a pressure improvement can be real while a section of the circuit remains fouled behind a partial obstruction. Together, and taken with a final pass at full permitted pig OD returning a pig in good condition, they establish that the pig has been in contact with the tube wall along the length of the circuit and that the circuit's resistance has measurably fallen.

## 10.4 Per-circuit determination

Completion is determined per circuit, not per heater. Circuits foul differently, particularly between passes with different firing exposure, and one circuit reaching criteria does not release the others. Each circuit carries its own before and after tests and its own completion record.

## 10.5 Inspection-supported jobs

Where the scope includes a smart pig or in-line inspection run, mechanical cleaning is confirmed complete before the inspection tool is introduced, because wall thickness measurement is only meaningful against a clean wall. Section 14 covers the run itself.

On those jobs the customer's written acceptance of the inspection data is required before dewatering or circuit breaking begins; rig-out follows dewatering and is not itself gated. Acceptance is given against the vendor's preliminary digital report rather than the final report, and a non-acceptance means the tool is run again rather than the job ending. Dewatering ahead of that acceptance forecloses a re-run, and the gate exists to protect against that. Section 14.6 covers the gate in full.

## 10.6 What is handed over

At completion each circuit has a before and after flow test record, the running field record of pigs run and observations made, and confirmation that the three criteria were met. Section 16 lists the full deliverable set.

---

Previous: [[09-phase-ii-mechanical-decoking]] · Next: [[11-phase-iii-rig-out-and-restoration]]
