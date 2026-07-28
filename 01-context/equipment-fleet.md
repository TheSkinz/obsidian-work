---
type: context
---

# Equipment Fleet
**Layer:** 01-context — loads every session

---

## Home Base

Deer Park, TX — all US equipment stages here unless assigned to a job.

## Pumping Units

| Unit ID  | Type                  | Paired Support | Notes                                 |
| -------- | --------------------- | -------------- | ------------------------------------- |
| Trimax 1 | Trimax Triple Pumper  | Support 1      | Travel as a set                       |
| Trimax 2 | Trimax Triple Pumper  | Support 2      | Travel as a set                       |
| Trimax 3 | Trimax Triple Pumper  | Support 3      | Travel as a set                       |
| Trimax 4 | Trimax Triple Pumper  | Support 4      | Travel as a set                       |
| Trimax 5 | Trimax Triple Pumper  | Support 5      | Travel as a set                       |
| Trimax 6 | Trimax Triple Pumper  | Support 6      | Travel as a set                       |
| Double 1 | Sea-Can Double Pumper | None           | Special/overseas jobs only — ~1x/year |
| Double 2 | Sea-Can Double Pumper | None           | Special/overseas jobs only — ~1x/year |

## Filtration

| Qty | Type | Notes |
| --- | ---- | ----- |
| 3 | Trailer-mounted filter press | All three are the same model. Specs in `04-knowledge/equipment/equipment-library.md` (the spec sheet on file is Press #1); canonical in `usadebusk-equipment`. |

A fourth press can be rented, but the complications make it a last resort USADebusk avoids — never plan or price a rental as the fallback when the fleet is committed (Jesse, 2026-07-25). This table records what exists, not what is free: availability across concurrent jobs is Jesse's logistics call and is deliberately not tracked in the vault.

## Notes

Mob distance for any job is measured from Deer Park, TX unless a unit is already staged elsewhere.

**Sea-Can Double Pumper build (Double 1, Double 2).** The fleet name "Sea-Can Double Pumper" and the `usadebusk-equipment` skill's "single 48' trailer" describe the same unit, not a discrepancy: it is a single 48' trailer with a sea-can shipping container retrofitted onto the bed, and the two engine/pump/valve assemblies are housed inside that container. Two independent pump assemblies (left = pump 1, right = pump 2; no center), cleaning two circuits simultaneously. The distinguishing invariant vs. the Trimax is assembly count (two vs. three) and the absence of a center assembly. Detail lives in the `usadebusk-equipment` skill (resolved per Jesse, 2026-07-01).
