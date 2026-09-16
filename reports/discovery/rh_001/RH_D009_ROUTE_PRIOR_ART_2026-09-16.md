# RH-D-009 — Route-specific prior-art and claimed-proof audit

**Campaign:** `RH-001`  
**Gate:** `RH-D-009 — PRIOR_ART`  
**Audit date:** 2026-09-16  
**Protected base:** `e4c6b668d28afa5f7557e6fddf31eb105a69a4a8`  
**Purpose:** bounded source audit for the candidate bridge nodes actually under consideration for `RH-R030`  
**Novelty / priority claims:** prohibited

## Claim boundary

This audit does not prove RH, certify a new zero range, establish novelty, or accept an online claimed proof. It settles only the source/prior-art question needed to choose a first Solve-native restricted target. Negative search statements below mean only that the bounded searches described here did not locate a stronger matching theorem.

The authoritative protected theorem substrate remains the MATH-PROGRAMME WP02 ledger. This record adds current route-specific source facts that post-date its 2026-07-25 moving-frontier audit.

## Current source additions

### `RH-D009-S-01` — compact-window Weil positivity

Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law*, arXiv:2608.24827v2, revised 2026-09-02.

Primary locator: `https://arxiv.org/abs/2608.24827v2`; HTML full version: `https://arxiv.org/html/2608.24827v2`.

Exact source facts used here:

- Theorem 1.1 fixes a one-stroke geometric-side reduction for every fixed support window `[-L,L]`.
- Its Weil symbol contains every prime power with `log n < 2L`; the prime-comb mass is `A_L = sum_{log n < 2L} 2 Lambda(n)/sqrt(n)`.
- If `beta* = log(T#/2pi) - 1/T# - A_L > 0`, positivity is reduced to one explicit Legendre-basis matrix plus explicit super-exponentially small tail/coupling bounds.
- Theorem 1.2 certifies `Q(f) >= 8.9e-18 ||f||_2^2` for every real even `f` supported in `[-0.8,0.8]`; the parity argument extends positivity to arbitrary complex test functions on that support.
- Section 7 retracts an earlier support-`2.38` (`L=1.19`) certification claim. The invalid step replaced the required worst-case prime-comb upper envelope by a per-prime quantity with the wrong inequality direction. The exploratory matrix computation is retained only as evidence, not a theorem.
- The source explicitly warns that ordinary float64 evaluation can create spurious negative eigenvalues in this cancellation-dominated problem.

Publication state: current arXiv v2 preprint. The result is source-current evidence for route selection; this record does not treat arXiv posting as independent certification.

### `RH-D009-S-02` — 2026 spectral no-go frontier

Douglas F. Watson and Tiziano Valentinuzzi, *Spectral-Dimension Obstructions for Operators with Superlinear Counting Laws*, *Bulletin des Sciences Mathématiques* 211 (2026), 103824, DOI `10.1016/j.bulsci.2026.103824`; arXiv:2604.00052.

The paper derives the heat asymptotics forced by Riemann-zero counting and excludes broad operator families whose spectral-dimension / heat-trace asymptotics are incompatible, including the compact finite-dimensional elliptic-geometric corner and the paper's single-valuation arithmetic-kernel class. It does not close Hilbert-Pólya generally.

## Candidate dispositions

### Candidate A — `RH-T-050`: density estimate -> sharper prime-distribution bridge

**Disposition:** reject for `RH-R030` in this tranche.

The protected ledger already records the published Guth-Maynard 2026 zero-density exponent. The same source develops prime-distribution consequences. A generic theorem of the form "the new density estimate implies a shorter prime interval / sharper prime-error consequence" is therefore source-adjacent prior art rather than a clean missing bridge. A future target would need a quantitatively distinct consequence with an exact theorem gap, not a repackaging of the published application.

False-proof firewall: a density estimate still permits exceptional off-line zeros and cannot be promoted to RH.

### Candidate B — `RH-T-120`: Nyman-Beurling-Baez-Duarte finite approximation advance

**Disposition:** reject for immediate selection.

Integer-dilation strengthenings and quantitative approximation questions are established research terrain, while protected debt `RH-D-003` still leaves parameterization and real/complex span conventions non-composable. Selecting a new approximation-rate theorem before discharging that exact semantic debt would make the target boundary unstable.

False-proof firewall: small finite-dimensional approximation error is not closure membership; no finite approximation may be represented as the full criterion.

### Candidate C — `RH-T-200`: Hilbert-Pólya no-go theorem for natural operator classes

**Disposition:** reject the generic candidate as current prior art.

The 2026 Watson-Valentinuzzi paper already supplies a structural heat-trace / spectral-dimension obstruction for broad natural operator classes. A new `RH-R030` framed only as excluding compact elliptic geometric operators, single-valuation kernels, or another class already covered by that asymptotic mismatch would duplicate known work. `RH-D-007` also remains: no candidate operator currently satisfies the full self-adjointness, complete-spectrum, and trace-regularization contract.

False-proof firewall: numerical spectral resemblance, spacing agreement, or a partial spectrum is not an operator theorem.

### Candidate D — `RH-T-160` via `RH-T-100`: full compact-window Weil positivity just beyond the current certified frontier

**Disposition:** select for Solve scoring, with an exact post-frontier window.

The September 2026 source changes the route frontier materially: every target at `L <= 0.8` is already covered by its certified theorem. A bounded search on 2026-09-16 over exact phrases for full-window Weil positivity, support `1.61` / `1.62`, and `L=0.805` did not locate a theorem extending the all-test-function unconditional positivity result beyond `L=0.8`. This is not a novelty claim.

The first arithmetic discontinuity above the certified frontier is

`L_5 = (1/2) log 5 = 0.804718956...`.

Accordingly the smallest clean rational window immediately across that threshold is

`L = 161/200 = 0.805`.

At this window the active prime powers change from `{2,3,4}` to `{2,3,4,5}`. This gives an exact, falsifiable bridge rather than an arbitrary larger decimal window.

**Recommended restricted target shape:** prove unconditional non-negativity of the exact Zhu/Weil geometric quadratic form for every complex `f in L^2(R)` with `supp f subset [-161/200,161/200]`, while retaining every pole, archimedean, and prime-power term and the exact parity treatment.

Why this is narrower than RH: Weil positivity on one fixed compact support window is only a finite fragment of the all-support criterion. It does not imply positivity at any larger support and does not imply `RH-T-000`.

## Claimed-proof audit on the selected route

The route-relevant claimed-proof issue is internal to `RH-D009-S-01`: an earlier draft claimed a certified result at `L=1.19`. The current v2 retracts it. The first invalid implication is explicit: the proof needed a uniform upper bound on the prime comb to obtain the lower envelope for the Weil symbol, but substituted a quantity that bounds the comb in the wrong direction. The current Lemma 3.2 restores the worst-case constant `A_L` and shows that no pointwise bound can improve it.

This failure is adopted as an `RH-R030` fixture:

> Any certificate that replaces `A_L` by a smaller phase-dependent or per-prime quantity must prove the required inequality direction uniformly in frequency. Numerical positivity of the resulting finite matrix is otherwise non-probative.

## False-proof firewall for Candidate D

The selected route must reject all of the following as target completion:

- positivity on finitely many test functions or one finite subspace without a certified tail/coupling argument;
- omission of the newly active `n=5` prime term;
- float64 eigenvalue signs near the spectral floor;
- a positive even-sector matrix without the odd-sector contract for the claimed complex class;
- an uncontrolled quadrature or basis truncation;
- any inference from one fixed support window to all supports;
- any claim that a numerical exploratory matrix is itself a theorem.

## RH-D-009 disposition

For the four bridge families actually considered in this tranche:

- density-to-primes: not selected; source-adjacent published territory;
- Nyman-Beurling approximation: not selected; semantic debt precedes a stable target;
- spectral no-go: generic version not selected; 2026 prior art already occupies the natural obstruction class;
- Weil compact-window positivity: source frontier advanced to `L=0.8`; the exact next candidate is placed at `L=161/200`, immediately beyond the prime-5 threshold.

**Gate result:** `RH-D-009_ROUTE_SPECIFIC_AUDIT_COMPLETE_FOR_RH-R030_SELECTION`.

This gate result authorizes target selection only. It does not certify the target, establish novelty, or promote any mathematical claim.
