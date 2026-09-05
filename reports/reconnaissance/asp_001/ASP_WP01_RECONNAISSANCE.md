# ASP-WP01 — Exact finite product-space reconnaissance

**Campaign candidate:** `ASP-001`  
**Work Package:** `ASP-WP01`  
**Owning pillar:** MATHFORGE  
**Issue:** `grandchallenge/MATHFORGE#111`  
**Implementation branch:** `research/asp-wp01-finite-harness`  
**Exact base:** `ed8a65410336489ea5646808265c44f5387bebb8`  
**Status:** realization candidate; promotion closed  

## Purpose

This work package supplies an exact finite ground-truth laboratory for the proposed Adaptive Spectral Peeling (ASP) programme. It confronts the finite product-space invariants behind the proposed theory before any approximate learner, adaptive optimizer, benchmark-scale experiment, or mathematical certification route is introduced.

The laboratory is intentionally exhaustive and small. Its purpose is not scalability. Its purpose is to make incorrect structural claims easy to falsify.

## Fixed contract

The governing contract is MATHFORGE issue #111. Acceptance conditions were recorded before realization. This report does not amend them after observing results.

WP01 is restricted to finite **uniform** product measures. Coordinates may have different finite cardinalities. Each coordinate uses an explicit real orthonormal basis: the constant function plus scaled Helmert contrasts. The tensor-product basis therefore supports Boolean and mixed categorical domains without encoding a categorical variable into an arbitrary collection of bits.

Excluded from WP01:

- nonuniform product measures;
- continuous coordinates;
- approximate spectral estimation from partial samples;
- adaptive query selection;
- confidence-envelope learning;
- branch-and-bound ASP-C;
- large-scale hyperparameter optimization;
- novelty, theorem, or certification claims.

## Candidate invariants under confrontation

### T1 — restriction transport

For a restricted coordinate set `R`, fixed value `z_R`, and residual basis index `beta`, WP01 checks by complete enumeration that the spectral coefficient recomputed on the restricted function equals the folded coefficient obtained from the full spectrum and the fixed-coordinate basis values.

### T2 — boundary influence identity

For degree cutoff `d`, WP01 computes the full spectral tail, restricts each coordinate to every possible value, recomputes each restricted spectrum, averages the residual tail exactly under the uniform coordinate measure, and checks that the decrement equals the level-`d+1` influence of that coordinate.

### T3 — deterministic tail envelope

For every enumerated nontrivial restriction, WP01 computes the actual sup-norm error of the degree-`d` restricted spectral truncation and checks it against the assignment-independent weighted spectral `l1` envelope.

### T5 sanity — interaction width

The laboratory forms the primal interaction graph induced by retained spectral supports and computes exact treewidth by exhaustive elimination-order search for at most eight active variables. Known path and clique fixtures provide independent finite sanity checks.

## Implementation surface

- `domains/adaptive_spectral_peeling/finite_lab.py`
- `domains/adaptive_spectral_peeling/replay_wp01.py`
- `tests/test_adaptive_spectral_peeling_wp01.py`

The implementation uses Python standard-library facilities only. No Forge CI dependency is added.

The deterministic replay command is:

```bash
python domains/adaptive_spectral_peeling/replay_wp01.py
```

The tests are reached by ordinary Forge CI through:

```bash
python -m unittest discover -s tests -v
```

## Author-side preflight

Before opening the candidate PR, the authoring environment executed the WP01 test module and deterministic replay. This is a **preflight only**; it is not repository CI evidence and is not an independent verification.

Observed preflight results at tolerance `1e-10`:

| Check | Observation |
| --- | ---: |
| WP01 unit tests | `10/10` passed |
| mixed-basis orthonormality max error | `2.220446049250313e-16` |
| spectral reconstruction max error | `8.326672684688674e-17` |
| T1 restrictions enumerated | `23` |
| T1 coefficient comparisons | `72` |
| T1 max error | `2.220446049250313e-16` |
| T2 max error | `1.3877787807814457e-17` |
| T3 max residual minus envelope | `3.3306690738754696e-16` |
| T3 largest actual residual | `0.491426817037558` |

The small positive T3 residual-minus-envelope value is floating-point roundoff at approximately machine precision and remains four orders of magnitude inside the declared `1e-10` numerical tolerance.

## Adversarial crossed regimes

WP01 deliberately avoids a benchmark suite in which all forms of structure improve together.

### High boundary influence / zero branch margin

A Boolean objective containing only a strong `x_0 x_1` interaction gives level-2 influence `4.0` at the selected coordinate while both coordinate branches have the same exact minimum. This directly falsifies any rule that treats high peeling influence as evidence for which branch value is safe to retain.

### Large branch margin / zero boundary influence

A strong first-order `x_0` term produces branch margin `3.0` while level-2 influence is exactly zero. Margin and spectral peeling value are therefore not interchangeable.

### Small L2 tail / larger weighted-l1 envelope

Twenty cubic Boolean terms of magnitude `0.02` produce

- `tau_2 = 0.08944271909999159`;
- weighted optimization-safe envelope `= 0.4`.

This fixture makes the norm mismatch visible even in a tiny exact domain.

### Low width / high width

Pairwise interactions on a six-variable path give exact treewidth `1`. Pairwise interactions on the six-variable clique give exact treewidth `5`, while both remain degree-2 spectral objectives. Degree alone therefore does not determine exact surrogate-solver complexity.

## Council pre-review matrix

This matrix records the authoring-side obligations prepared for Confrontation. It is not an independent Council disposition.

| Office | WP01 finding / obligation |
| --- | --- |
| Purpose Minder | Purpose is finite disconfirmation of the ASP structural core before learner-scale work. |
| Axiomatist | Assumptions are explicit: finite uniform product measure, real tensor-product orthonormal basis, exhaustive finite arithmetic subject to declared tolerance. |
| Possibility Minder | Alternatives preserved: direct bit encoding; generic categorical contrasts; abandoning spectral peeling if restriction identities or norm separations fail. WP01 selects categorical contrasts only for the bounded finite laboratory. |
| Cartographer | Dependencies separated into spectral transport, influence, tail norm, interaction width and margin. No one quantity is allowed to proxy for all others. |
| Formalist | T1/T2/T3 are executable invariants. Acceptance/disconfirmation thresholds were fixed in issue #111. |
| Grammarian | `tail_energy` denotes squared L2 tail norm; reported `tau2` is its square root. `weighted_l1_tail_envelope` is an optimization-safe upper envelope, not an observed sup-norm error. |
| Experimentalist | Deterministic seeds, complete enumeration and crossed adversarial regimes are present. |
| Adversary | Required failures include influence/margin conflation, L2/L-infinity conflation, low-degree/low-width conflation, mixed-cardinality basis failure and seed nondeterminism. |
| Verifier | Author-side tests pass locally; exact-head GitHub CI remains required and has not yet been substituted by this preflight. |
| Composer | Replay, library and tests expose one coherent bounded artifact with no bespoke workflow. |
| Mechanist | Exact treewidth is intentionally capped at eight vertices to prevent an exploratory exact routine from being mistaken for a scalable solver. |
| Steward | Scope excludes the learner, ASP-C, scale benchmarks and continuous/nonuniform domains; no new CI dependency or infrastructure lane is created. |
| Amanuensis | Stable IDs, exact base, issue, branch, commands, scope and residual frontier are recorded here. |
| Archivist | Failed CI/replay evidence must remain in issue/PR history; a later corrected head must not reuse stale exact-head evidence. |
| Referee | **UNRESOLVED — must be a fresh non-author review bound to the final exact candidate head.** |

## Source and novelty boundary

The originating conceptual line includes Hazan, Klivans and Yuan, *Hyperparameter Optimization: A Spectral Approach* (`arXiv:1706.00764`), together with standard Fourier/Efron-Stein product-space analysis, submodular coverage, and treewidth-based variable elimination. WP01 makes no novelty determination.

The broader ASP-WP00 theorem synthesis remains candidate research material. Finite verification here cannot prove T1–T7, establish general sample complexity, or substitute for a mathematical certification route.

## Contact record contract

GitHub CI is the first repository-level contact capable of defeating the present realization. A valid contact record for WP01 must identify:

- exact candidate commit;
- workflow run and job identity;
- whether the ordinary Forge reconnaissance job completed;
- WP01 unit-test outcome;
- any failure from existing Forge validators or unrelated repository drift;
- whether the failure is attributable to ASP-WP01 or pre-existing infrastructure;
- residual uncertainty.

A new candidate head invalidates prior exact-head contact evidence.

## Promotion boundary

Even if CI is green, the only permissible WP01 conclusion at this stage is:

`FINITE_RECONNAISSANCE_CONSISTENT_WITH_ASP_CORE__INDEPENDENT_REFEREE_PENDING`

A green run does **not** establish:

- mathematical proof of T1–T7;
- global optimization correctness of ASP-C;
- data-driven tail certification;
- sample-complexity improvements;
- superiority over Harmonica or Bayesian optimization;
- novelty or priority;
- MATHSOLVE eligibility;
- MATHCERT certification;
- MATH-PROGRAMME campaign activation;
- publication or commercial authority.

## Residual frontier

If WP01 survives exact-head CI and independent review, the next implementation work package should be **ASP-WP02 — Spectral Scout**: partial-sample coefficient/influence estimation measured against WP01 exact truth, with structural recovery targets rather than exact coefficient recovery.

The parallel theory frontier remains **T8**: obtain useful data-driven upper certificates on unresolved optimization-relevant spectral tails without paying the full cost of global uniform reconstruction.
