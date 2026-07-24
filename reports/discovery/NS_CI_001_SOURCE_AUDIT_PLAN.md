# NS-CI-001 source, status, and false-proof audit plan

## Identity

- Parent programme tracker: `grandchallenge/MATH-PROGRAMME#55`
- MATHFORGE issue: `#14`
- Campaign: `NS-CI-001`
- Owning pillar: MATHFORGE
- State: source and correspondence audit substantially complete; false-proof and restricted-target work pending

## Corrected target under audit

For a Leray–Hopf solution of the unforced three-dimensional incompressible Navier–Stokes equations on `ℝ³`, arising from every smooth divergence-free datum satisfying Fefferman's rapid-decay condition, determine whether

```math
∫₀ᵀ ‖u(t)‖_{L⁶(ℝ³)}⁴dt<∞
```

for every finite `T>0`.

The compact-support version is retained as the restricted lane `NS-CI-R-COMPACT`. It must not be silently promoted to the full official data class.

## Discovery contract

Provider results, abstracts, bibliographic databases, preprints, and search-engine summaries are evidence only. A mathematical statement enters the programme claim ledger only after its source, hypotheses, domain, and solution class have been reviewed. An inaccessible original theorem body is recorded as such rather than reconstructed from a later citation.

## Work streams

### F0 — source ledger

Status: delivered in `reports/discovery/ns_ci_001/source_ledger.yaml`.

The ledger records:

- source identity and type;
- primary, official, reconstruction, or operational-secondary status;
- theorem location where extracted;
- data, domain, forcing, and solution classes;
- exact mixed-norm hypothesis where available;
- audit state and limitations.

### F1 — correspondence matrix

Status: delivered in `reports/discovery/ns_ci_001/hypothesis_matrix.csv`.

The matrix separates:

- `ℝ³` and `𝕋³`;
- unforced and forced equations;
- rapidly decreasing and compactly supported data;
- Leray–Hopf, strong, and smooth solution classes;
- historical theorem formulations and the modern operational interface;
- regularity, uniqueness, continuation, and global-existence conclusions.

### F2 — false-proof fixtures

Status: pending WP01.

Build minimized, exact counterexamples or diagnostics for:

1. reversed finite-measure inclusion `L²_t ⊄ L⁴_t`;
2. generic interpolation that silently assumes `L^∞_tL⁶_x` or `L^∞_tH¹_x`;
3. scale-breaking estimates whose constants diverge under concentration;
4. circular use of smoothness to establish the critical norm;
5. silent domain transfer;
6. silent promotion from compact support to the full rapid-decay class;
7. bounded Galerkin trajectories presented as continuum regularity evidence;
8. formalization of assumptions presented as formalization of the open theorem.

### F3 — current-status and claimed-proof triage

Status: official current-status determination delivered in `current_status_audit.md`.

Use the official Clay status as canonical unless an accepted resolution supersedes it. For a specific claimed solution considered by the campaign, record:

- claim source;
- review venue;
- accepted, rejected, withdrawn, or unverified status;
- published critique or institutional determination, when available;
- no amplification beyond what is required for audit.

The campaign does not maintain an exhaustive catalogue of internet claims.

### F4 — restricted-target reconnaissance

Status: blocked until WP00 governance promotion.

For each candidate restricted theorem, record:

- added hypothesis;
- why it is not equivalent to assuming regularity;
- scaling behavior;
- known prior art;
- expected proof bottleneck;
- falsification test;
- possible MATHCERT route;
- estimated analytic and computational cost.

## Audited source set

- Charles L. Fefferman, official Clay problem description.
- Jean Leray, original 1934 paper, with the Ożański–Pooley reconstruction used for operational theorem interfaces.
- Giovanni Prodi, original 1959 theorem; exponent law extracted directly.
- James Serrin, original 1962 bibliographic record; exact theorem body not extracted from the audited public endpoint.
- O. A. Ladyzhenskaya, original 1967 Russian full-text location; mathematical translation pending.
- A modern explicit theorem statement of the R3 Leray–Hopf Prodi–Serrin criterion.
- Clay's current official status page.

See `source_ledger.yaml` for exact audit states. Historical theorem-text gaps remain visible and do not invalidate the separately identified modern operational interface.

## Outputs

```text
reports/discovery/ns_ci_001/
  source_ledger.yaml                 [delivered]
  hypothesis_matrix.csv             [delivered]
  current_status_audit.md           [delivered]
  false_proof_atlas.md              [pending WP01]
  restricted_target_candidates.yaml [blocked until WP00 promotion]
  review_log.md                     [pending final Archivist pass]
```

## Audit determination

The source review found a material formulation error in the initialization: `C_c^∞(ℝ³)` is only a restricted subclass of Fefferman's official rapidly decreasing data. The canonical campaign has been corrected.

The audited operational correspondence is one-way:

```text
universal full-data L4_tL6_x integrability
 -> LPS regularity and uniqueness
 -> continuation/global smoothness
 -> Clay statement (A).
```

Bidirectional equivalence remains pending a reverse strong-class and every-Leray–Hopf correspondence audit.

## Acceptance gate

- [x] Official data class extracted.
- [x] Prodi exponent law extracted directly.
- [x] Modern operational `(4,6)` interface identified.
- [x] R3 and T3 are separated.
- [x] Compact support is classified as restricted.
- [x] Current status is dated.
- [ ] Original Leray theorem concordance completed.
- [ ] Original Serrin theorem body extracted.
- [ ] Ladyzhenskaya mathematical translation completed.
- [ ] False-proof atlas delivered.

The last four items are provenance or subsequent-WP obligations; they do not authorize mechanism generation before the parent WP00 Referee gate.

## Next executable action

Complete the Archivist review log that maps the original Leray, Serrin, and Ladyzhenskaya sources to the modern operational theorem chain. In parallel, prepare—but do not yet promote—the WP01 false-proof fixtures.