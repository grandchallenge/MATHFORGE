# RH-D-009 — Route-specific prior-art audit for RH-R030

- Campaign: `RH-001`
- Provider tracker: `grandchallenge/MATHFORGE#215`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#163`
- Protected Programme theorem graph: `e764e316cf0655cbdade49e2b1faec2d0634a464`
- Protected Forge base: `e4c6b668d28afa5f7557e6fddf31eb105a69a4a8`
- Audit date: 2026-09-16
- Scope: route-specific source/prior-art audit only
- Novelty / priority claims: prohibited

## Decision

One candidate survives for immediate Solve-native selection:

`RH-R030-SPECTRAL-UNBOUNDED-001` — a bounded-operator no-go theorem for the Hilbert–Pólya route.

The candidate is not represented as novel. Its value is contract sharpening: it converts the Riemann–von Mangoldt unbounded-zero-count interface (`RH-T-030`) into an exact necessary operator property inside the Hilbert–Pólya contract (`RH-T-200`). Any operator whose spectrum contains every positive zeta-zero ordinate must be unbounded. Therefore bounded self-adjoint operators, bounded integral operators, and finite matrices cannot satisfy the exact ordinate-spectrum contract.

The other three candidate families are not selected in this tranche because their current frontiers are moving or because the proposed bounded statement risks collapsing back into an already exact RH equivalence.

## Candidate A — spectral unboundedness no-go

### Exact candidate statement

Let `Z+` be the set of positive ordinates `gamma > 0` for which there exists a nontrivial zero `rho` of the classical zeta function with `Im(rho)=gamma`. There is no bounded self-adjoint operator `A` on a complex Hilbert space such that `Z+` is contained in the spectrum of `A`.

Equivalent necessary-condition form: every Hilbert–Pólya operator satisfying the protected exact ordinate-spectrum contract must be unbounded.

### Parent nodes

- `RH-T-030` — Riemann–von Mangoldt zero-counting interface;
- `RH-T-200` — Hilbert–Pólya sufficient-route contract.

### Already known substrate

1. `RH-T-030` gives `N(T) -> infinity`; hence positive zero ordinates are unbounded.
2. The spectrum of a bounded operator lies in the closed disk of radius `||A||`; for self-adjoint `A`, it lies in `[-||A||, ||A||]`.

The target is therefore a short exact bridge between two standard theorems. No novelty claim is made.

### Current route frontier

Recent operator work confirms that the spectral route is active but unresolved:

- Fabio Bagarello and Sergiusz Kużel, **On the Berry-Keating Operator**, *Complex Analysis and Operator Theory* 20 (2026), article 135, DOI `10.1007/s11785-026-01990-w`, published 2026-07-07. The paper states that the connection of the Berry–Keating operator to RH remains not fully understood. The Berry–Keating generator is an unbounded operator, consistent with the candidate necessary condition.
- V. V. Kapustin, **Hilbert–Pólya Operators in Krein Spaces**, *Siberian Mathematical Journal* 65 (2024), 72–75, DOI `10.1134/S0037446624010087`. The construction uses a Krein-space setting and transformed spectral values `1/(s(1-s))`; it therefore does not supply the protected Hilbert-space ordinate-spectrum contract. The nonlinear transform also shows why the normalization must be locked: bounded transformed spectral values do not contradict unbounded ordinates.

### Claimed-proof audit intersecting this route

A 2026 PhilArchive/PhilPapers manuscript by Daniel Toupin claims an adelic self-adjoint operator whose spectrum is the set of imaginary parts of nontrivial zeros and then argues that reality of the self-adjoint spectrum plus functional-equation symmetry forces `Re(rho)=1/2`.

The first invalid implication is exact: `Im(rho)` is real for every complex number `rho`, independently of RH. Self-adjointness of an operator whose eigenvalue was defined to be `Im(rho)` therefore constrains no real part. Functional-equation symmetry permits off-line quartets and does not repair the implication. This is precisely the protected false-proof pattern `RH-F003` (symmetry is not location) together with `RH-F011` (a spectral correspondence must encode the correct object, not merely a partial projection).

This claimed proof does not affect the bounded-operator no-go theorem.

### Barrier and falsifier

- Barrier: none beyond the two standard inputs above.
- Smallest falsifier: exhibit a bounded operator `A` with spectral values of arbitrarily large absolute value. This is impossible by the bounded-spectrum theorem.
- Proof modality: continuum functional analysis plus the classical zero-counting theorem.
- Computational support: none required.

### Claim boundary

The no-go theorem does **not** construct a Hilbert–Pólya operator, prove self-adjointness of any candidate, identify a trace formula, establish spectral completeness, or imply RH.

### Audit disposition

`SURVIVES_FOR_SOLVE_SELECTION`.

---

## Candidate B — Nyman–Beurling–Báez-Duarte restricted approximation theorem

### Parent node

`RH-T-120`.

### Existing protected debt

`RH-D-003` already blocks composition until the parameterization and real/complex span conventions are locked.

### Current frontier change

Jongho Yang, **A Friedrichs angle between the Nyman-Beurling spaces and the Riemann hypothesis**, *Journal of Mathematical Analysis and Applications* 560(1) (2026), 130494, DOI `10.1016/j.jmaa.2026.130494`, published 2026-08-01, introduces new subspace-angle structure in the Nyman–Beurling setting. Its abstract states both an RH-conditional angle result and an additional unconditional result.

This paper post-dates the protected WP02 audit of 2026-07-25. The exact theorem text and its interaction with the protected parameter/span conventions are not yet reconstructed in Forge. Selecting a new approximation or subspace-angle bridge before that reconstruction creates an avoidable overlap/subsumption risk.

### False-proof firewall

A finite-dimensional approximation estimate cannot be promoted to closure membership without a limiting theorem. Any proposed target must keep the infinite closure obligation explicit.

### Audit disposition

`DEFER_CURRENT_FRONTIER_CHANGED`.

This is not a campaign blocker because another candidate survives.

---

## Candidate C — Li-coefficient bounded positivity mechanism

### Parent node

`RH-T-110`.

### Existing theorem frontier

The protected ledger correctly records Li's criterion: RH is equivalent to `lambda_n >= 0` for every `n >= 1`.

Masatoshi Suzuki, **Li coefficients as norms of functions in a model space**, *Journal of Number Theory* 252 (2023), 177–194, DOI `10.1016/j.jnt.2023.05.007`, gives another full equivalence: all Li coefficients arise as norms of concrete functions if and only if RH holds.

### Route assessment

A finite prefix is safe but mathematically weak unless coupled to a genuine tail mechanism. A theorem controlling the full tail risks becoming exactly the universal Li criterion. No source-current narrower analytic mechanism with a clear non-equivalent claim boundary was identified in this bounded audit.

### False-proof firewall

`RH-F012`: finite Li positivity is not the universal criterion.

### Audit disposition

`REJECT_FOR_IMMEDIATE_SELECTION__MISSING_NARROW_MECHANISM`.

No claim is made that the Li route is exhausted.

---

## Candidate D — zero-density / explicit-prime-error transport

### Parent nodes

- `RH-T-050` — zero-density estimates;
- `RH-T-100` — explicit-formula transport.

### Current frontier change

The route is moving rapidly after the WP02 audit:

- Chiara Bellotti, **An explicit log-free zero density estimate for the Riemann zeta-function**, *Journal of Number Theory* 269 (2025), 37–77, DOI `10.1016/j.jnt.2024.10.001`.
- Chiara Bellotti, **A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem**, *Bulletin of the London Mathematical Society* 58(7) (2026), DOI `10.1112/blms.70442`; arXiv `2508.02041`.
- Frederik Broucke, **On the connection between zero-free regions and the error term in the Prime Number Theorem**, *Analysis Mathematica* (version of record 2026-08-15), DOI `10.1007/s10476-026-00176-y`; arXiv `2507.13780`.
- Valeriia Starichkova, **A note on zero-density approaches for the difference between consecutive primes**, *Journal of Number Theory* 278 (2026), 245–266, DOI `10.1016/j.jnt.2025.04.007`.

These papers directly occupy the proposed bridge shape from zero-free/zero-density information to prime-distribution error terms and short intervals. A new target selected without theorem-level comparison would risk being already known or weaker than a 2026 result.

### False-proof firewall

`RH-F002`, `RH-F013`, and `RH-F017` remain active: density control is not universal zero exclusion; a near-looking prime error term is not an RH equivalent; a zero-free region near one does not squeeze zeros to the critical line.

### Audit disposition

`DEFER_CURRENT_FRONTIER_CHANGED`.

---

## Route selection recommendation to MATHSOLVE

Select Candidate A as `RH-R030-SPECTRAL-UNBOUNDED-001` with the exact contract:

> Every bounded self-adjoint operator has bounded spectrum, while the positive ordinates of nontrivial zeta zeros are unbounded by Riemann–von Mangoldt. Therefore no bounded self-adjoint operator can have spectrum containing all positive zeta-zero ordinates. Any exact Hilbert–Pólya ordinate-spectrum operator must be unbounded.

Required Solve proof obligations:

1. derive unboundedness of positive zero ordinates from `RH-T-030` without assuming RH;
2. state the bounded-spectrum theorem with the exact operator category;
3. combine them by contradiction;
4. preserve `RH-F010` and `RH-F011`: this theorem says nothing about self-adjoint domains or complete spectral equality for an unbounded candidate;
5. state explicitly that the theorem is a necessary-condition/no-go result only.

## Source / claim status

- RH itself remains open.
- No novelty or priority claim is supported.
- No candidate proof of RH reviewed here is admitted.
- This audit discharges the provider-side prior-art gate only for selecting the bounded spectral no-go target above.
- Any later strengthening of `RH-R030` requires a fresh route-specific audit.