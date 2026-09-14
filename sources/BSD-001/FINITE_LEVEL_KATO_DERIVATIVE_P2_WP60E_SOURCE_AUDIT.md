# BSD-001 source audit — finite-level Kato-derivative / Mazur–Tate literal-`p=2` applicability

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#190`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Protected MATHSOLVE anchor: `76dc727be85052933a986cedd83ab056d9890240`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Disposition: `ODD_PRIME_ONLY_FINITE_LEVEL_KATO_DERIVATIVE_ROUTE_DOES_NOT_CLOSE_LITERAL_P2_R5`.
- Claim class: bounded source/applicability audit only.

## Exact downstream query

Protected WP60A-A1 identifies determinant membership at the cyclotomic height-one prime `(2)` with the missing one-sided Fitting divisibility

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

Protected Kato audit WP17B establishes that Kato's original ordinary theorem controls height-one primes away from `(2)` at `p=2`, while the all-height-one clauses that would include `(2)` assume `p != 2`.

WP60E therefore asks one narrow question: do the finite-level Kato-derivative, determinantal-zeta, Mazur–Tate, or refined Fitting results of Burns–Kurihara–Sano or Chan-Ho Kim furnish a genuinely integral theorem at literal `p=2` that bypasses the missing cyclotomic `(2)` exponent?

## Source A — Burns–Kurihara–Sano, derivatives of Kato's Euler system

Primary source:

David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404v2; published in the Journal of the Mathematical Society of Japan.

### Global prime convention

The paper fixes an **odd prime** `p` at the beginning of the introduction before defining its Kato zeta elements, Bockstein regulators, finite-level Fitting objects, and cyclotomic constructions.

Thus its general setup is not stated for literal `p=2`.

### Finite-level Fitting containment

The concrete finite-level containment used to derive the order-of-vanishing result is even narrower. Theorem 1.3 assumes

`p > 3`.

Section 3 traces this to Proposition 3.3, where the finite-level Fitting containment for the Darmon derivative of Kato's zeta element again assumes

`p > 3`.

The proposition places the evaluated derivative in

`Fitt^0_{Z_p[G]}(H^2(O_{F,S},T))`

under its stated hypotheses, but the theorem is not a literal-`p=2` result.

### Rank-one leading-term discussion does not remove the prime restriction

In analytic rank one the Generalized Perrin–Riou Conjecture simplifies to a leading-term/logarithm identity. This simplification does not supply a new integral finite-level Fitting theorem at `p=2`; it is a reformulation of the conjectural/equivalent leading-term statement inside a paper whose `p`-adic framework is fixed at an odd prime, while the proved finite-level Fitting containment uses `p>3`.

**Disposition:** `FINITE_LEVEL_FITTING_CONTAINMENT_REQUIRES_P_GT_3`.

## Source B — Burns–Kurihara–Sano, Mazur–Tate follow-up

Primary source:

David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system and the Mazur-Tate Conjecture*, arXiv:2103.11535v1; published in IMRN.

The paper develops determinantal zeta elements and a Selmer-complex proof of a `p`-primary Mazur–Tate implication. Its standing Hypothesis 2.2 requires

`p` does not divide

`6 m N * #(E(Q)_tors) * Tam(E) * product_{ell|pmN} #E^ns(F_ell)`.

The factor `6` alone excludes `p=2` and `p=3`.

Consequently, the determinantal-zeta and Fitting calculations proved under Hypothesis 2.2 cannot be specialized to the selected literal `p=2` lane.

This exclusion is structural at the level of the stated hypotheses; no downstream cancellation or selected residual-surjectivity argument licenses removing it.

**Disposition:** `MAZUR_TATE_DETERMINANTAL_ROUTE_EXPLICITLY_EXCLUDES_P_2`.

## Source C — Chan-Ho Kim, refined applications of Kato's Euler systems

Primary source:

Chan-Ho Kim, *Refined applications of Kato's Euler systems for modular forms*, arXiv:2203.12157v4.

The current arXiv version fixes an **odd prime** `p` at the beginning of the article.

Its finite-level Mazur–Tate/Fitting Theorem 1.3 assumes `p` is an odd prime. Its main Kolyvagin-system / main-conjecture structural Theorem 1.5 assumes

`p >= 5`.

The paper therefore gives strong integral finite-layer Fitting information, but not at literal `p=2`.

**Disposition:** `REFINED_FINITE_LAYER_FITTING_RESULTS_REQUIRE_ODD_P_OR_P_GE_5`.

## Comparison with the protected R5 boundary

These papers are highly relevant architecturally because they show that derivatives of Kato's Euler system, determinantal zeta elements, finite-layer Coleman maps, and Mazur–Tate elements can encode Fitting information at finite level.

However, the exact proved interfaces located here do not repair the selected prime-two defect:

- Burns–Kurihara–Sano's first finite-level Fitting containment requires `p>3`;
- their determinantal Mazur–Tate follow-up excludes `p=2` through Hypothesis 2.2;
- Chan-Ho Kim fixes odd `p`, with key structural results requiring `p>=5`.

Therefore none of these admitted interfaces supplies either

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`

or

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Nor do they furnish a direct finite-level primitive Kummer/Fitting theorem at literal `p=2` that bypasses the cyclotomic height-one `(2)` exponent.

## Exact bounded conclusion

The finite-level derivative/Mazur–Tate candidate route screened in WP60E does **not** reopen R5 at literal `p=2`.

Record the bounded source boundary

`MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

This is subordinate to, and does not replace, the protected R5 boundaries. It identifies the missing interface that would be needed to turn the otherwise relevant finite-level architecture into a selected-lane theorem.

A future candidate reopens this route only if it supplies an integral theorem at literal `p=2`, or an independent proof that removes the cited odd-prime hypotheses while retaining the exact Fitting and local-condition statements.

## Non-exhaustiveness

This audit is not a claim that no literal-`p=2` finite-level derivative theorem can exist. It records the exact applicability of the three specifically screened primary-source frameworks. It does not authorize a literature-exhaustiveness claim.

## Claim firewall

This audit does not establish:

- the missing height-one-`(2)` Fitting divisibility;
- determinant primitivity at `(2)`;
- a finite-level primitive Kummer/Fitting theorem at `p=2`;
- vanishing of the relative `mu` invariant;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
