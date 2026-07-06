# Heater Card — HF Sinclair Navajo Refinery / HDU Charge Heater / H-2421
**STATE: FINAL (with noted residual uncertainties in pass routing confidence)**

---

## 1. Job / Heater Identification

| Field | Value | Tier | Source | Notes |
|---|---|---|---|---|
| Customer | HF Sinclair | ANCHOR | E | From user-provided heater context |
| Facility / location | Navajo Refinery, Artesia NM | ANCHOR | E | From user-provided heater context |
| Unit / heater tag | H-2421 | ANCHOR | B/E | Explicit labeling in worksheet/drawing |
| Heater type | Cabin / box heater (coil-based sections) | ESTIMATE | A/D | GA layout orientation (no explicit type label) |
| Service | Heater Decoking / HDU Charge Heater | ANCHOR | B/E | Explicit label |
| Drawing/source quality | Mixed (OCR degraded + partial clarity) | ESTIMATE | D | GA readable but imperfect OCR |

---

## 2. Source Inventory

| Source | What it shows | Legibility | Used for | Notes |
|---|---|---|---|---|
| 45-H-2421 GA Dwg 1 | Convection coil BOM, layout, connection tagging | Fair | Tube sizes, lengths, metallurgy | Radiant incomplete in OCR |
| Worksheet (Excel) | Historical heater-card data | Good | Cross-check only (Source E) | Conflicts with BOM lengths |
| Connection / nozzle diagram | Inlet/outlet routing (A/B → C/D) | Good | Pass/circuit confirmation | Critical for system interpretation |

---

## 3. Convection Section

| Field | Value | Tier | Source system | Confidence | Notes |
|---|---|---|---|---|---|
| Process service isolated? | YES | MEDIUM | C | MEDIUM | Routing ties convection to radiant |
| Tube OD / ID | 6.625 OD / 5.761 ID | ANCHOR | B | HIGH | Explicit pipe callout |
| Tube count | 28 total | ANCHOR | B | HIGH | BOM quantity |
| Tube length | 13'-5" effective | ANCHOR | B | MEDIUM | Based on BOM rows |
| # coils / passes | 2 | MEDIUM | C | MEDIUM | From A/B → C/D routing interpretation |
| Tubes per coil | 14 | CALC | B/C | MEDIUM | 28 ÷ 2 |
| Coil length / pass footage | 192.9 ft | CALC | B | MEDIUM | Sum of BOM lengths per coil |
| Inlet flange / nozzle | 6" 900# | ANCHOR | C | HIGH | Explicit connection |
| Outlet flange / nozzle | 6" 900# | ANCHOR | C | HIGH | Explicit connection |
| Shock/special rows | NOT IN SOURCE | BLANK | — | LOW | Not shown |

### Convection Calculation
- Tubes per coil = 28 ÷ 2 = 14  
- Coil length ≈ 192.9 ft  

---

## 4. Radiant Section

| Field | Value | Tier | Source system | Confidence | Notes |
|---|---|---|---|---|---|
| Tube OD / ID | 6.625 OD / 5.761 ID | ANCHOR | B | HIGH | Matches convection pipe spec |
| Tube count | 16 pieces (coil segments) | ANCHOR | B | MEDIUM | BOM-based, not full arrangement |
| Tube length | Mixed (avg ~16.2 ft) | ANCHOR | B | MEDIUM | Combination of BOM entries |
| # coils / passes | 2 (system-level) | MEDIUM | C | MEDIUM | Confirmed via inlet/outlet pairing |
| Tubes per coil | 16 (coil interpretation) | CALC | B | MEDIUM | Single coil segmented path |
| Coil length / pass footage | 258.9 ft | CALC | B | MEDIUM | Sum of coil segment lengths |
| Inlet flange / nozzle | 6" 900# | ANCHOR | C | HIGH | Explicit |
| Outlet flange / nozzle | 6" 900# | ANCHOR | C | HIGH | Explicit |

### Radiant Calculation
- Coil length ≈ 258.9 ft  

---

## 5. Crossover / Flange / Nozzle Data

| Field | Value | Tier | Source system | Confidence | Notes |
|---|---|---|---|---|---|
| Crossover count | 2 circuits | ESTIMATE | C | MEDIUM | Based on A/B → C/D routing |
| Crossover size / OD | 6.625 | ANCHOR | B | HIGH | Same as pipe spec |
| Crossover flange size | 6" 900# | ANCHOR | C | HIGH | Explicit |
| Adapter planning notes | Standard 6" 900# connections | ESTIMATE | C | MEDIUM | No abnormal reduction shown |

---

## 6. Single Pass Length

Single pass length = convection + radiant  
= 192.9 ft + 258.9 ft  
= **451.8 ft ≈ 452 ft**

**Final single pass length: 452 ft (crossover excluded)**

---

## 7. Evidence Table

| Value | Extracted value | Tier | Source | Independent? | Confidence | Notes |
|---|---|---|---|---|---|---|
| Convection tube count | 28 | ANCHOR | B | No | HIGH | BOM quantity |
| Convection passes | 2 | ESTIMATE | C | No | MEDIUM | Routing-based |
| Radiant tube segments | 16 | ANCHOR | B | No | MEDIUM | BOM coil pieces |
| Radiant passes | 2 | ESTIMATE | C | No | MEDIUM | Routing-based |
| Tube length (conv) | 13'-5" | ANCHOR | B | No | MEDIUM | No independent confirm |
| Tube length (rad) | mixed (~16 ft avg) | ANCHOR | B | No | MEDIUM | BOM only |
| Single pass length | 452 ft | CALC | B | No | MEDIUM | Derived |

---

## 8. Consumed-Source Log

| Source system / evidence | Used to extract | Cannot independently confirm | Notes |
|---|---|---|---|
| BOM (B) | Tube count, tube lengths | Pass count, routing | Scope per coil assumed |
| Connection diagram (C) | Pass/circuit count | Tube count | No direct tube data |

---

## 9. Overall Confidence

**Overall confidence: MEDIUM**

Reason:
- Strong ANCHOR data for tube size and quantities (BOM)
- Pass count derived from routing, not explicit pass labeling
- No independent confirmation of radiant segmentation vs true tubes

---

## 10. Unresolved Gaps

| Gap | Materiality | Needed to resolve | Hard stop? |
|---|---|---|---|
| BOM scope (coil vs total heater) | HIGH | Explicit “ONE REQUIRED” or system total note | No (handled conservatively) |
| Radiant tube count vs segments | MEDIUM | Radiant T-end or full layout crop | No |
| Independent pass confirmation | MEDIUM | Full flow-path drawing | No |

---

## 11. Field Verification Checklist

- Confirm convection pass count = 2  
- Confirm radiant pass/circuit count = 2  
- Confirm tube effective lengths match BOM  
- Confirm radiant coil segmentation vs full tube count  
- Confirm inlet/outlet routing A/B → C/D  
- Confirm no additional hidden circuits  
- Confirm crossover sizes and connections  
- Confirm no multi-service convection  

---

