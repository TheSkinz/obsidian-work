# 15. Passivation on Stainless Metallurgy

**Layer:** 04-knowledge/manual
**Source:** `~/.claude/skills/usadebusk-sop/SKILL.md` (SOP Variant B), [[industry-foundation]]
**Manual:** [[00-manual-index]]

---

## 15.1 Applicability

Stainless steel coils are uncommon in this service. Where one is encountered, the mechanical decoking procedure is unchanged: the same launchers, receivers, pigs, progression, and completion criteria apply.

What changes is that a passivation step normally follows mechanical cleaning, to restore the passive oxide layer on the cleaned surface, and that water chemistry becomes a controlled variable.

## 15.2 Scope boundary

Passivation is customer scope. The customer performs it, provides the soda ash, and performs the mixing. USADebusk does not supply the soda ash, mix the solution, or perform the passivation.

The governing method is set by the customer's own specification, not inferred from metallurgy. Facility specifications differ, and a customer's requirement may reference an industry standard such as NACE SP0170 or may be facility-specific. The requirement is read from the customer's bid instructions or specification rather than assumed.

Two consequences follow from that, and both cut against assumption. A stainless coil may carry a passivation method other than the default. And a coil that is not stainless may still require soda ash treatment where the customer's specification calls for it across a package.

## 15.3 What it consists of

Where passivation follows cleaning, the customer circulates a soda ash solution through the coil, monitoring pH throughout, followed by a final rinse to neutral before closeout.

| Parameter | Specification |
|---|---|
| Solution | Soda ash, customer-supplied and customer-mixed |
| Target pH during circulation | 10.0 or above, monitored throughout |
| Circulation velocity | 1–2 ft/s |
| Final condition | Flushed to neutral pH before closeout |
| Governing specification | Customer specification, which may reference NACE SP0170 |

Where a nitrogen purge forms part of the customer's specification, the source of the nitrogen is confirmed in planning.

## 15.4 Water chemistry

Chloride content is the controlled variable on stainless work, and it governs the water used for mechanical cleaning as well as for passivation.

| Limit | Value |
|---|---|
| Fresh solution chloride | 250 ppm maximum |
| Spent solution chloride | 500 ppm maximum |
| Verification before fill | Below 0.5 ppm |

Facility firewater is avoided by default on stainless work because of chloride content. It is permitted only where the facility has tested its hydrant supply and confirmed acceptable chloride levels. The water source is confirmed before the job SOP is written, and is never assumed.

This is also the most common reason filtration is elected on stainless work: where the supply is a produced low-chloride water rather than a hydrant, conserving it through a closed loop matters. That remains a facility election, not an automatic inclusion. Section 12 covers it.

## 15.5 Interface with the decoking scope

For planning purposes, stainless metallurgy affects three things in the USADebusk scope and nothing else. The water source and its chloride verification must be settled before mobilization. Filtration is more likely to be elected. And the job schedule must accommodate the customer's passivation activity between mechanical completion and closeout.

Metallurgy is recorded per coil section, since mixed configurations exist, most often carbon steel convection with a stainless radiant section.

---

Previous: [[14-ancillary-smart-pig-support]] · Next: [[16-documentation-and-deliverables]]
