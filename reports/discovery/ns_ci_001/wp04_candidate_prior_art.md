# NS-CI-WP04 — Candidate and prior-art audit

## Status

- Campaign: `NS-CI-001`
- Work Package: `NS-CI-WP04`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#61`
- MATHFORGE tracker: `grandchallenge/MATHFORGE#18`
- State: `INITIAL_PRIOR_ART_TRIAGE_COMPLETE_A2_BOUNDARY_REFINED`
- Audit date: 2026-07-23/24
- Novelty claims: prohibited
- Provisional shortlist: `NS-CI-R014-A2`, `NS-CI-R014-D1`, `NS-CI-R014-E1`
- Claimed-proof diversion: `grandchallenge/MATHFORGE#20`

This pass identifies established theorem families, terminates generic candidates already covered by prior art, and replaces them with three exact candidate statements for MATHSOLVE and MATHCERT review. The shortlist is provisional: it is not a novelty determination or Referee selection.

## Source ledger

| Source ID | Work | Role | Audit state |
|---|---|---|---|
| `WP04-S-A1` | Cheskidov–Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944; DOI `10.1007/s00021-014-0167-4` | whole-space definition of `Lambda`; low-mode criterion `f`; pointwise `Lambda^2 lesssim f lesssim Lambda^(5/2)`; regularity for `Lambda in L^(5/2)_t`; universal `Lambda in L^1_t` | primary theorem and proof text extracted |
| `WP04-S-A2` | Bradshaw–Grujić, *Frequency Localized Regularity Criteria for the 3D Navier–Stokes Equations*, arXiv:1501.01043; DOI `10.1007/s00205-016-1069-9` | frequency-localized LPS refinements | primary source audited |
| `WP04-S-A3` | Cheskidov–Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611 | high-frequency Littlewood–Paley vorticity criterion | primary source audited |
| `WP04-S-A4` | Cheskidov–Peng, *An optimal upper bound on the determining wavenumber for 3D Navier–Stokes Equations*, DOI `10.1007/s00030-026-01232-0` | 2026 forced-torus determining-wavenumber result; relevant vocabulary but different object, domain, forcing, and theorem role | primary source scoped; not an A2 match |
| `WP04-S-B1` | Constantin–Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789 | foundational vorticity-direction criterion | primary metadata and theorem role audited |
| `WP04-S-B2` | Beirão da Veiga–Berselli, *On the regularizing effect of the vorticity direction in incompressible viscous flows*, DOI `10.57262/die/1356060864` | quantitative vorticity-direction refinement | primary source identified |
| `WP04-S-B3` | Berselli, *On the vorticity direction and the regularity of 3D Navier–Stokes equations*, DOI `10.1088/1361-6544/ace096` | recent small-jump/discrete-direction refinement | primary source audited |
| `WP04-S-C1` | Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, arXiv:1111.0217; DOI `10.1088/0951-7715/26/1/289` | one-dimensional sparseness criterion | primary source audited |
| `WP04-S-C2` | Albritton–Bradshaw, *Remarks on sparseness and regularity of Navier–Stokes solutions*, arXiv:2110.02187; DOI `10.1088/1361-6544/ac62de` | alternate proof of sparse-solution regularity and adversarial analysis of scaling-gap claims | primary source audited |
| `WP04-S-D1` | Kato–Ponce, *Commutator estimates and the Euler and Navier–Stokes equations*, DOI `10.1002/cpa.3160410704` | commutator substrate; not by itself a critical-integrability theorem | primary source audited |
| `WP04-S-E1` | Chemin–Gallagher, *Wellposedness and Stability Results for the Navier–Stokes Equations in R3*, arXiv:math/0611044; DOI `10.1016/j.anihpc.2007.05.008` | stability mechanisms for selected global classes; does not supply the universal compact-support extension bridge | primary source audited |
| `WP04-S-E2` | Bahouri–Chemin–Gallagher, *Stability by rescaled weak convergence for the Navier–Stokes equations*, arXiv:1310.0256 | warns that unrestricted weak stability would be strong enough to imply global regularity | primary source audited |
| `WP04-S-F1` | Ukhovskii–Yudovich and Ladyzhenskaya axisymmetric results, as recorded in the operational literature | classical global theory for no-swirl or otherwise restricted axisymmetric regimes | classical theorem family audited |
| `WP04-S-F2` | Shahmurov, *Global Regularity for Axisymmetric Navier–Stokes Flows with Swirl*, arXiv:2606.07869v1 | recent claim of arbitrary-swirl global regularity | claim identified; correctness not audited or accepted |
| `WP04-S-F3` | Shahmurov, arXiv:2605.01875 and arXiv:2605.09797 | related first-threshold and full-system global-regularity claims | claim family identified; correctness not audited or accepted |

## Candidate dispositions

### `NS-CI-R014-A` — generic dyadic or frequency-envelope control

**Disposition: REPLACE BY EXACT CANDIDATE `A2`.**

Frequency-localized LPS, Besov, dissipation-wavenumber, and high-frequency vorticity criteria are established in `WP04-S-A1` through `A3`. A generic statement that frequency-envelope control implies regularity is therefore neither source-normalized nor plausibly novel.

The useful gap in `WP04-S-A1` is exact. For the low-mode coefficient

```math
f(t)=\|\omega_{\le Q(t)}(t)\|_{B^0_{\infty,\infty}},
```

the source proves, when `Lambda(t)>1`,

```math
\Lambda(t)^2\lesssim f(t)\lesssim\Lambda(t)^{5/2}.
```

It then concludes regularity from `f in L1_t`, obtains this from `Lambda in L^(5/2)_t`, proves `Lambda in L1_t` for every Leray–Hopf solution, and explicitly describes the remaining task as filling the gap between `L1` and `L^(5/2)`.

Under Navier–Stokes scaling,

```math
\Lambda_\lambda(t)=\lambda\Lambda(\lambda^2t),
```

so `integral Lambda(t)^2dt` is invariant.

#### Replacement candidate `NS-CI-R014-A2`

For the Cheskidov–Shvydkoy whole-space dissipation wavenumber, determine whether

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
f\in L^1(0,T),
```

or by another equation-specific route,

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
\int_0^T\|u(t)\|_6^4dt<\infty.
```

The first implication feeds the source's low-mode regularity theorem; the second feeds the WP02 LPS theorem directly.

A targeted search over exact phrases, arXiv records, publisher pages, and dissipation/determining-wavenumber citations located the established `L^(5/2)` theorem and later determining-wavenumber results, but no exact whole-space `Lambda in L2_t` criterion. `WP04-S-A4` concerns a different forced-torus determining wavenumber and does not close A2. This negative search result is a bounded audit statement, not a novelty claim.

#### Adversarial obstruction

The source inequalities alone cannot close A2. Set abstractly

```math
\Lambda(t)=t^{-9/20}
```

on `(0,1)`. Then `Lambda^2=t^(-9/10)` is integrable, while the permitted upper envelope `Lambda^(5/2)=t^(-9/8)` is not. Thus

```text
Lambda in L2_t + source pointwise bounds
```

does not imply `f in L1_t` without additional Navier–Stokes structure.

A separate elementary low-frequency estimate yields products of the form

```math
\Lambda^2\|u\|_2^2\|\nabla u\|_2^2.
```

Both `Lambda^2` and the energy dissipation density may be in `L1_t`, but their product need not be. The exact scalar fixture is included in `tests/test_ns_ci_wp04_candidate_fixtures.py`.

**WP01 clearance:** avoids reversed time inclusion, hidden compact-support restriction, and fixed-resolution overclaim. Active risks are multiplication of unrelated `L1` coefficients, covert use of uniform `H1`, and circular conversion to an established Besov/LPS criterion.

**Recommendation:** PROVISIONAL LEAD, pending exact-source concordance and a new weighted frequency estimate.

### `NS-CI-R014-B` — generic geometric depletion of vortex stretching

**Disposition: REJECT GENERIC FORM.**

Vorticity-direction coherence and related geometric depletion criteria form an established line from Constantin–Fefferman through Beirão da Veiga–Berselli and later refinements. A candidate stated only as “geometric depletion implies regularity” is classical or underspecified.

A future revision would need a distinct quantitative inequality whose conclusion is the critical integral and whose hypothesis is demonstrably outside the established criteria.

**WP01 termination:** already-classical theorem family; unspecified geometry risks hidden regularity and nonlocal unverifiability.

### `NS-CI-R014-C` — generic concentration or sparsity control

**Disposition: REJECT GENERIC FORM.**

One-dimensional sparseness of intense regions is already a regularity criterion (`WP04-S-C1`), and `WP04-S-C2` supplies both an alternate proof and an explicit warning against overclaiming that available a priori sparseness estimates close the scaling gap.

**WP01 termination:** classical criterion plus direct adversarial warning against scaling-gap promotion.

### `NS-CI-R014-D` — generic flux or commutator compensation

**Disposition: REPLACE BY EXACT INTERFACE CANDIDATE `D1`.**

Kato–Ponce estimates and Littlewood–Paley methods provide analytic substrate, but no audited source proves the exact uniform compensation required to neutralize WP01's `N^4` Galerkin or `epsilon^-4` mollification losses.

#### Replacement candidate `NS-CI-R014-D1`

Let `u^N=P_{<=N}u` and

```math
\Pi_N(t)=\left\langle P_{\le N}((u\cdot\nabla)u),-\Delta u^N\right\rangle.
```

Seek an independently checkable, scale-uniform shell-flux hypothesis implying constants `theta<1` and `a in L1(0,T)`, independent of `N`, such that

```math
\Pi_N(t)
\le \theta\nu\|\Delta u^N\|_2^2
   +a(t)\|\nabla u^N\|_2^2.
```

The displayed inequality is only an interface. The theorem-grade target must state a strictly independent shell-flux or commutator hypothesis; otherwise D1 is tautological.

**WP01 clearance:** directly targets cutoff and mollification losses. Main rejection risks are defining `a` through `||u||_6^4`, hiding uniform `H1`, or permitting constants to depend on `N`.

**Recommendation:** PROVISIONAL SHORTLIST WITH FORMULATION DEBT.

### `NS-CI-R014-E` — generic compact-support extension

**Disposition: REPLACE BY CONDITIONAL BRIDGE `E1`.**

Compact support is dense in standard initial-data topologies, but density alone does not identify an arbitrary Leray–Hopf solution after passage to the limit. Unrestricted weak stability would be exceptionally strong; `WP04-S-E2` warns against an automatic density argument.

#### Replacement candidate `NS-CI-R014-E1`

Prove the following conditional extension principle:

> If smooth compactly supported divergence-free approximants of a fixed Schwartz datum generate global strong solutions satisfying an `L4_tL6_x` bound uniform in the approximation index in an explicit topology, then every Leray–Hopf solution from that Schwartz datum has the same finite-time critical-integrability conclusion.

The proof obligations are compactness, lower semicontinuity, preservation of the equation and initial trace, production of one strong limit, and weak–strong uniqueness. The uniform bound and quantifier order must be explicit; pointwise finiteness for each approximant is insufficient.

**WP01 clearance:** directly resolves compact-support drift. Main risk is hiding global stability equivalent to the original theorem.

**Recommendation:** PROVISIONAL SHORTLIST AS BRIDGE FALLBACK.

### `NS-CI-R014-F` — symmetry or structural classes

**Disposition: REJECT GENERIC FORM; OPEN CLAIM TRIAGE.**

No-swirl axisymmetry and several exact symmetry classes are classical and too remote from the full theorem to serve as `R014` without a distinct bridge.

Recent 2026 preprints claim arbitrary-swirl axisymmetric and broader global regularity. They are unreviewed in this programme and potentially problem-changing. They are routed to `grandchallenge/MATHFORGE#20`, which requires cylindrical-weight, near-axis, boundary-term, compactness, quantifier, and full WP01 review. They are not accepted prior art and do not change the campaign status.

## Provisional shortlist handoff

| Candidate | Exact target | Leverage | Main blocker |
|---|---|---|---|
| `A2` | critical `Lambda in L2_t` implies the low-mode criterion or finite `L4_tL6_x` | high | source bounds allow a nonintegrable `Lambda^(5/2)` envelope; a new weighted frequency estimate is required |
| `D1` | independent shell hypothesis implies uniform compensated enstrophy inequality | high | no non-tautological hypothesis has been supplied |
| `E1` | uniform compact-support bound extends to Schwartz data and every Leray–Hopf solution | medium | topology, global compactness, and uniformity must be exact |

MATHSOLVE should score these three candidates and expose their proof DAGs. MATHCERT should verify A2 scaling, D1 cutoff covariance and coefficient scaling, and E1 quantifier order.

## Route-termination records

- `B-GENERIC`: terminated as established geometric-regularity family.
- `C-GENERIC`: terminated as established sparseness-regularity family with documented scaling-gap caution.
- `F-GENERIC`: terminated as classical or low-leverage symmetry family.
- `F-CLAIM-2026`: neither accepted nor rejected; diverted to claimed-proof audit `#20`.

## Claim boundary

This audit does not establish novelty, prove any shortlisted implication, accept the 2026 claims, or authorize numerical evidence as continuum proof.