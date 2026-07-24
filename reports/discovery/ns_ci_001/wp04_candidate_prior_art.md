# NS-CI-WP04 — Candidate and prior-art audit

## Status

- Campaign: `NS-CI-001`
- Work Package: `NS-CI-WP04`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#61`
- MATHFORGE tracker: `grandchallenge/MATHFORGE#18`
- State: `INITIAL_PRIOR_ART_TRIAGE_COMPLETE`
- Audit date: 2026-07-23/24
- Novelty claims: prohibited
- Provisional shortlist: `NS-CI-R014-A2`, `NS-CI-R014-D1`, `NS-CI-R014-E1`

This pass identifies established theorem families, terminates generic candidates already covered by prior art, and replaces them with three exact candidate statements for MATHSOLVE and MATHCERT review. The shortlist is provisional: it is not a novelty determination or Referee selection.

## Source ledger

| Source ID | Work | Role | Audit state |
|---|---|---|---|
| `WP04-S-A1` | Cheskidov–Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944; DOI `10.1007/s00021-014-0167-4` | defines the dissipation wavenumber `Lambda`; proves regularity for `Lambda in L^(5/2)_t`; proves `Lambda in L^1_t` for every Leray–Hopf solution | primary source extracted |
| `WP04-S-A2` | Bradshaw–Grujić, *Frequency Localized Regularity Criteria for the 3D Navier–Stokes Equations*, arXiv:1501.01043; DOI `10.1007/s00205-016-1069-9` | frequency-localized LPS refinements | primary source audited |
| `WP04-S-A3` | Cheskidov–Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611 | high-frequency Littlewood–Paley vorticity criterion | primary source audited |
| `WP04-S-B1` | Constantin–Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789 | foundational vorticity-direction criterion | primary metadata and theorem role audited |
| `WP04-S-B2` | Beirão da Veiga–Berselli, *On the regularizing effect of the vorticity direction in incompressible viscous flows*, DOI `10.57262/die/1356060864` | quantitative vorticity-direction refinement | primary source identified |
| `WP04-S-B3` | Berselli, *On the vorticity direction and the regularity of 3D Navier–Stokes equations*, DOI `10.1088/1361-6544/ace096` | recent small-jump/discrete-direction refinement | primary source audited |
| `WP04-S-C1` | Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, arXiv:1111.0217; DOI `10.1088/0951-7715/26/1/289` | one-dimensional sparseness criterion | primary source audited |
| `WP04-S-C2` | Albritton–Bradshaw, *Remarks on sparseness and regularity of Navier–Stokes solutions*, arXiv:2110.02187; DOI `10.1088/1361-6544/ac62de` | alternate proof of sparse-solution regularity and adversarial analysis of scaling-gap claims | primary source audited |
| `WP04-S-D1` | Kato–Ponce, *Commutator estimates and the Euler and Navier–Stokes equations*, DOI `10.1002/cpa.3160410704` | commutator substrate; not by itself a critical-integrability theorem | primary source audited |
| `WP04-S-E1` | Chemin–Gallagher, *Wellposedness and Stability Results for the Navier–Stokes Equations in R3*, arXiv:math/0611044; DOI `10.1016/j.anihpc.2007.05.008` | stability mechanisms for selected global classes; does not supply the universal compact-support extension bridge | primary source audited |
| `WP04-S-E2` | Bahouri–Chemin–Gallagher, *Stability by rescaled weak convergence for the Navier–Stokes equations*, arXiv:1310.0256 | shows why unrestricted weak stability would be strong enough to imply global regularity; supplies a warning against an automatic density argument | primary source audited |
| `WP04-S-F1` | Ukhovskii–Yudovich and Ladyzhenskaya axisymmetric results, as recorded in the operational literature | classical global theory for no-swirl or otherwise restricted axisymmetric regimes | classical theorem family audited |
| `WP04-S-F2` | Shahmurov, *Global Regularity for Axisymmetric Navier–Stokes Flows with Swirl*, arXiv:2606.07869v1, submitted 2026-06-05 | recent claim of arbitrary-swirl global regularity | claim identified; correctness not audited or accepted |
| `WP04-S-F3` | Shahmurov, arXiv:2605.01875 and arXiv:2605.09797 | related first-threshold and full-system global-regularity claims | claim family identified; correctness not audited or accepted |

## Candidate dispositions

### `NS-CI-R014-A` — generic dyadic or frequency-envelope control

**Disposition: REPLACE BY EXACT CANDIDATE `A2`.**

The generic family is crowded. Frequency-localized LPS, Besov, dissipation-wavenumber, and high-frequency vorticity criteria are established in `WP04-S-A1` through `A3`. A generic statement that frequency-envelope control implies regularity is therefore neither source-normalized nor plausibly novel.

The useful unresolved gap in `WP04-S-A1` is precise:

```text
all Leray–Hopf solutions: Lambda in L^1_t
known sufficient criterion: Lambda in L^(5/2)_t
scale-critical exponent for Lambda: 2
```

Indeed, under Navier–Stokes scaling, `Lambda_lambda(t)=lambda Lambda(lambda^2 t)`, so `integral Lambda(t)^2 dt` is invariant.

#### Replacement candidate `NS-CI-R014-A2`

For the Cheskidov–Shvydkoy dissipation wavenumber `Lambda(t)`, determine whether

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
u^{-3}\int_0^T\|u(t)\|_6^4\,dt<\infty
```

for a Leray–Hopf solution on `R^3`.

This is strictly weaker than the known `L^(5/2)_t` sufficient condition on a finite interval, is scaling-critical, and does not assume the target norm. No exact `L^2_t` implication was located in the audited sources or targeted search pass. That absence is not a novelty claim.

**WP01 clearance:** avoids reversed time inclusion, hidden `H^1`, compact-support drift, and fixed-resolution overclaim. Main risk is circular conversion of `Lambda in L^2` into a Besov or LPS norm already equivalent to regularity.

**Recommendation:** PROVISIONAL SHORTLIST.

### `NS-CI-R014-B` — generic geometric depletion of vortex stretching

**Disposition: REJECT GENERIC FORM.**

Vorticity-direction coherence and related geometric depletion criteria form an established line from Constantin–Fefferman through Beirão da Veiga–Berselli and later refinements. A candidate stated only as “geometric depletion implies regularity” is classical or underspecified.

A future revision would need a new quantitative inequality whose conclusion is the critical integral itself and whose hypothesis is demonstrably weaker than existing direction-coherence criteria.

**WP01 termination:** already-classical theorem family; unspecified geometry risks hidden regularity and nonlocal unverifiability.

### `NS-CI-R014-C` — generic concentration or sparsity control

**Disposition: REJECT GENERIC FORM.**

One-dimensional sparseness of intense regions is already a regularity criterion (`WP04-S-C1`), and `WP04-S-C2` supplies both an alternate proof and an explicit warning against overclaiming that available a priori sparseness estimates close the scaling gap.

A new candidate must not infer criticality merely from asymptotic derivative order or numerically observed sparsity.

**WP01 termination:** classical criterion plus direct adversarial warning against scaling-gap promotion.

### `NS-CI-R014-D` — generic flux or commutator compensation

**Disposition: REPLACE BY EXACT INTERFACE CANDIDATE `D1`.**

Kato–Ponce estimates and Littlewood–Paley methods provide the analytic substrate, but this audit found no source proving the exact uniform compensation required to neutralize WP01's `N^4` Galerkin or `epsilon^-4` mollification losses.

#### Replacement candidate `NS-CI-R014-D1`

Let `u^N=P_{<=N}u` and define the resolved enstrophy-production term

```math
\Pi_N(t)=\left\langle P_{\le N}((u\cdot\nabla)u),-\Delta u^N\right\rangle.
```

Audit whether an independently checkable, scale-uniform shell-flux hypothesis can yield constants `theta<1` and `a in L^1(0,T)`, independent of `N`, such that

```math
\Pi_N(t)
\le \theta\nu\|\Delta u^N\|_2^2
   +a(t)\|\nabla u^N\|_2^2
```

for almost every `t` and every `N`.

The displayed inequality itself is only an interface: by Grönwall it yields a uniform `H^1` estimate and hence the WP02 continuation route. The theorem-grade target must state a strictly weaker shell-flux or commutator hypothesis that implies this interface; otherwise the candidate is tautological.

**WP01 clearance:** directly targets cutoff and mollification losses. Main rejection risk is replacing the target by an equally strong enstrophy bound or allowing `a(t)` to encode `||u||_6^4`.

**Recommendation:** PROVISIONAL SHORTLIST, formulation incomplete.

### `NS-CI-R014-E` — generic compact-support extension

**Disposition: REPLACE BY CONDITIONAL BRIDGE `E1`.**

Compact support is dense in standard initial-data topologies, but density alone does not identify an arbitrary Leray–Hopf solution after passage to the limit. Unrestricted weak stability would be exceptionally strong; `WP04-S-E2` explains why a general version would imply global regularity through rescaling examples.

#### Replacement candidate `NS-CI-R014-E1`

Prove a precise extension principle of the form:

> If every smooth compactly supported divergence-free datum has a global strong solution satisfying an `L^4_tL^6_x` bound uniform under approximation of a fixed Schwartz datum in an explicitly named topology, then every Leray–Hopf solution from that Schwartz datum satisfies the same finite-time critical-integrability conclusion.

The proof obligations are compactness, lower semicontinuity, preservation of the equation and initial trace, production of one strong limit, and weak–strong uniqueness to identify every Leray–Hopf solution. The uniform bound and topology must be explicit; pointwise finiteness for each approximant is insufficient.

**WP01 clearance:** directly resolves compact-support drift instead of silently promoting it. Main risk is hiding global stability equivalent to the original theorem.

**Recommendation:** PROVISIONAL SHORTLIST as a bridge theorem, not as the principal regularity mechanism.

### `NS-CI-R014-F` — symmetry or structural classes

**Disposition: REJECT GENERIC FORM; OPEN CLAIM TRIAGE.**

No-swirl axisymmetry and several exact symmetry classes are classical and too remote from the full theorem to serve as `R014` without a distinct bridge. Axisymmetric flow with arbitrary swirl remains the historically difficult near-axis case in the established literature.

A June 2026 preprint, arXiv:2606.07869v1, claims global regularity for arbitrary swirl, with related broader claims in arXiv:2605.01875 and arXiv:2605.09797. These claims are recent, unreviewed in this programme, and potentially problem-changing. They must be routed through claimed-proof triage and the WP01 false-proof atlas before candidate selection. They are not accepted prior art and are not evidence that the axisymmetric-swirl problem is closed.

**Recommendation:** generic F rejected; `F-CLAIM-2026` routed to separate adversarial audit.

## Provisional shortlist handoff

| Candidate | Exact target | Leverage | Main blocker |
|---|---|---|---|
| `A2` | critical `Lambda in L^2_t` implies finite `L^4_tL^6_x` | high | derive a new frequency-to-critical-integral estimate below the known `L^(5/2)` criterion |
| `D1` | shell-flux/commutator hypothesis implies uniform compensated enstrophy inequality | high | formulate a non-tautological, scale-uniform observable hypothesis |
| `E1` | uniform compact-support bound extends to the full Schwartz data class and every Leray–Hopf solution | medium | make topology and uniformity strong enough for passage to the limit but weaker than global regularity |

MATHSOLVE should formulate and score these three candidates. MATHCERT should verify the scaling of `A2`, the uniformity/interface logic of `D1`, and the implication/quantifier structure of `E1`.

## Route-termination records

- `B-GENERIC`: terminated as established geometric-regularity family.
- `C-GENERIC`: terminated as established sparseness-regularity family with documented scaling-gap caution.
- `F-GENERIC`: terminated as classical/remote symmetry family.
- `F-CLAIM-2026`: not terminated or accepted; diverted to claimed-proof audit.

## Claim boundary

This audit does not establish novelty, prove any shortlisted implication, accept the 2026 axisymmetric-swirl claims, or authorize numerical evidence as continuum proof.