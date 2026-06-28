## Heater Card — H-30 Charge Heater
**State:** NON-FINAL (convection tube OD/wall not anchored; geometry-derived lengths)

---

## 1. Job / Heater Identification

- Heater / Unit: H-30 Charge Heater  
- Facility: Navajo Refining Company  
- Coil Mark (Radiant): RC-A1  

---

## 2. Drawing / Source Inventory

- Radiant BOM + layout snippets (pipe segments, fittings) → Source B / A  
- Tube arrangement views (top grid + side banks) → Source A  
- Opposite-end pigging routing view → Source C  
- User confirmations:
  - Full convection grid visible  
  - Radiant process tubes = 28 (BOM interpretation) → Source E  

---

## 3. Convection Section

- Process service isolated?: UNCLEAR  
- Tubes (process): **20**  
  - Tier: ANCHOR (user-confirmed full grid)  
  - Source: E  
- Passes: **4**  
  - Tier: ANCHOR (routing-supported)  
  - Source: C + A  
- Tubes per pass: **5**  
  - Tier: DERIVED  
  - Source: Calculation  

- Tube OD / ID: **~4 in nominal (NOT IN SOURCE for coil)**  
  - Tier: ESTIMATE  
  - Source: C (flange/piping inference)

- Tube length: **~27 ft**  
  - Tier: ESTIMATE  
  - Source: D (geometry)

- Convection coil length per pass:  
```text
5 tubes/pass × ~27 ft ≈ ~135 ft/pass