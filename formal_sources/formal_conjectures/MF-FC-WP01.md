# MF-FC-WP01 — Programme Concordance Pilot

## Campaigns

- `RH-001`
- `NS-CI-001`

## Results

### RH-001

The upstream `RiemannHypothesis.riemannHypothesis` declaration is recorded as an exact human-reviewed formulation match to the Programme target. This is not a kernel theorem relating two formal definitions because MATH-PROGRAMME currently owns a source-normalized textual lock rather than a separate Lean target declaration.

### NS-CI-001

The upstream `NavierStokes.navier_stokes_existence_and_smoothness_R3` declaration states Clay alternative A. The Programme target is the universal critical-integrability statement for Leray-Hopf solutions. The recorded relationship is one-way only:

```text
NS-CI universal critical integrability
  -> continuation and regularity
  -> Clay alternative A
```

No reverse implication is admitted.

## Records

- `concordance/RH-001.json`
- `concordance/NS-CI-001.json`

## Promotion boundary

These records may supplement the existing RH and NS-CI provider manifests after MATH-PROGRAMME pins the merged MATHFORGE commit. They do not replace the existing native or retrospective coverage classification.
