# NS-CI-001 source, status, and false-proof audit plan

## Identity

- Parent programme tracker: `grandchallenge/MATH-PROGRAMME#55`
- MATHFORGE issue: `#14`
- Campaign: `NS-CI-001`
- Owning pillar: MATHFORGE
- State: initialized; no source claim promoted

## Target under audit

For a Leray–Hopf solution of the unforced three-dimensional incompressible Navier–Stokes equations on `ℝ³`, arising from smooth compactly supported divergence-free data, determine whether

```math
∫₀ᵀ ‖u(t)‖_{L⁶(ℝ³)}⁴dt<∞
```

for every finite `T>0`.

## Discovery contract

Provider results, abstracts, bibliographic databases, preprints, and search-engine summaries are evidence only. A mathematical statement enters the programme claim ledger only after the exact theorem text, hypotheses, domain, and solution class have been reviewed.

## Work streams

### F0 — source ledger

Create one normalized record per theorem or status source:

```yaml
source_id:
source_type:
primary_or_secondary:
bibliographic_record:
canonical_url_or_doi:
theorem_location:
domain:
forcing:
initial_data:
solution_class:
space_time_hypothesis:
conclusion:
endpoint_policy:
translation_or_notation_notes:
audit_state:
reviewer:
review_date:
```

Seed records:

- Fefferman / Clay official problem description;
- Leray weak-solution and energy framework;
- Prodi 1959;
- Serrin 1962;
- Ladyzhenskaya 1967;
- a modern authoritative local strong-theory source;
- a modern authoritative weak–strong uniqueness source.

### F1 — correspondence matrix

Separate at minimum:

- `ℝ³` versus `𝕋³`;
- unforced versus forced equations;
- Leray–Hopf, suitable weak, mild, strong, and smooth solutions;
- homogeneous versus inhomogeneous Sobolev conventions;
- open intervals, closed finite intervals, and maximal-time intervals;
- regularity, uniqueness, continuation, and global-existence conclusions.

### F2 — false-proof fixtures

Build minimized, exact counterexamples or diagnostics for:

1. reversed finite-measure inclusion `L²_t ⊄ L⁴_t`;
2. generic interpolation that silently assumes `L^∞_tL⁶_x` or `L^∞_tH¹_x`;
3. scale-breaking estimates whose constants diverge under concentration;
4. circular use of smoothness to establish the critical norm;
5. silent domain transfer;
6. bounded Galerkin trajectories presented as continuum regularity evidence;
7. formalization of assumptions presented as formalization of the open theorem.

### F3 — current-status and claimed-proof triage

Use the official Clay status as the canonical public status unless an accepted resolution supersedes it. For any claimed solution considered, record:

- claim source;
- review venue;
- accepted, rejected, withdrawn, or unverified status;
- specific published critique or institutional determination, when available;
- no amplification beyond what is needed for audit.

### F4 — restricted-target reconnaissance

For each candidate restricted theorem, record:

- added hypothesis;
- why it is not equivalent to assuming regularity;
- scaling behavior;
- known prior art;
- expected proof bottleneck;
- falsification test;
- possible MATHCERT route;
- estimated analytic and computational cost.

Candidate families are not endorsed until the source audit is stable.

## Initial source seeds

- Charles L. Fefferman, official Clay problem description: `https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`
- Giovanni Prodi, DOI `10.1007/BF02410664`
- James Serrin, DOI `10.1007/BF00253344`
- O. A. Ladyzhenskaya: `https://www.mathnet.ru/eng/znsl2228`

The Leray, local-theory, and weak–strong uniqueness entries remain to be selected and audited.

## Outputs

```text
reports/discovery/ns_ci_001/
  source_ledger.yaml
  hypothesis_matrix.csv
  current_status_audit.md
  false_proof_atlas.md
  restricted_target_candidates.yaml
  review_log.md
```

## Acceptance gate

- Every theorem claim has exact source provenance and theorem location.
- `ℝ³` and `𝕋³` statements are not merged.
- The programme can trace each imported arrow without relying on an abstract or summary page.
- False-proof fixtures are exact and reproducible.
- Current-status claims are dated.
- No discovery artifact claims universal critical integrability, global regularity, or novelty.

## First executable action

Extract and normalize the exact `(q,p)=(4,6)` hypotheses and conclusions from Prodi, Serrin, and Ladyzhenskaya, then compare them against one modern authoritative formulation. Record every mismatch before searching for mechanisms.