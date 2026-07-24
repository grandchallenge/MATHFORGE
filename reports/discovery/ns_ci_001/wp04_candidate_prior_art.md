# NS-CI-WP04 — Candidate and prior-art audit

## Status

- Campaign: `NS-CI-001`
- Work Package: `NS-CI-WP04`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#61`
- MATHFORGE tracker: `grandchallenge/MATHFORGE#18`
- State: `PRIOR_ART_AUDIT_ACTIVE`
- Novelty claims: prohibited until this ledger is complete

## Audit objective

Normalize, source, and adversarially triage candidate restricted theorem targets before MATHSOLVE formulation. The output is a shortlist of at most three candidates, or a documented no-shortlist result.

## Required record per candidate

- candidate ID and exact family;
- domain, data class, solution class, and quantifiers;
- proposed added hypothesis;
- scaling class;
- nearest known theorem;
- primary and modern operational sources;
- source audit state;
- known counterexamples or failure regimes;
- WP01 fixture map;
- novelty disposition;
- recommendation: reject, revise, or shortlist.

## Candidate families

### NS-CI-R014-A — Dyadic frequency-envelope control

Audit whether a scale-summable shell or frequency-envelope condition yields the critical integral without merely restating Besov/Serrin regularity. Compare against classical frequency-localized regularity criteria and continuation results.

### NS-CI-R014-B — Geometric depletion

Audit quantitative alignment, coherence, or depletion hypotheses for the vorticity stretching term. Separate established geometric regularity criteria from genuinely distinct quantitative bridges to `L^4_tL^6_x`.

### NS-CI-R014-C — Concentration or sparsity

Audit conditions on the size, geometry, or intermittency of high-vorticity regions. Record whether the hypotheses are scaling-compatible and independently checkable.

### NS-CI-R014-D — Flux or commutator compensation

Audit estimates that could offset the `N^4` Galerkin or `epsilon^{-4}` mollification losses identified by WP01. Reject any proposal lacking a uniform scale-summable gain.

### NS-CI-R014-E — Compact-support extension

Audit whether known stability and approximation theorems can transfer a compact-support result to the full Fefferman rapid-decay class without assuming the critical estimate.

### NS-CI-R014-F — Symmetry or structural classes

Catalogue classical regularity results for axisymmetric, helical, two-and-a-half-dimensional, or related classes. Shortlist only a statement that is not already classical and retains explanatory leverage.

## Hard rejection rules

Reject a candidate when it:

- triggers a WP01 fixture without a new estimate;
- assumes a norm equivalent to the desired regularity;
- is already classical in the exact stated form;
- is scale-breaking without a uniform compensation mechanism;
- changes the data or solution quantifiers silently;
- relies on numerical evidence as continuum proof;
- relies on an untracked imported theorem.

## Output contract

The final audit must contain:

1. a source-backed candidate matrix;
2. route-termination records for rejected candidates;
3. at most three shortlisted candidates;
4. an explicit statement that no novelty is claimed before Referee review;
5. handoff records to MATHSOLVE and MATHCERT.
