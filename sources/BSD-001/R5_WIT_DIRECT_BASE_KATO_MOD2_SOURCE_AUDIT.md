# BSD-001 R5-WIT source audit — direct bottom Kato class mod-2 detector

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#242`.
- Downstream operation: `grandchallenge/MATHSOLVE#282` (`BSD-R5-WIT`).
- Exact downstream candidate entering this audit: `grandchallenge/MATHSOLVE@660524d86f383c9e5859514c8f83d88470dd87ed`.
- Protected MATHFORGE base: `42248fffff5e6d091b5ba209ccd969a6ce6b6700`.
- Claim class: bounded source/applicability evidence only.

## 1. Exact downstream query

Protected WP60T supplies, for every admitted rank-one Euler system `c`,

`kappa_m(c)_1 = c_Q mod 2^m`.

Protected R5-PRIM finite detection requires only one nonzero legitimate finite cyclotomic residual Kato/Kolyvagin image.

At `m=1`, a direct proof

`c_Q^Kato mod 2 != 0`

would therefore give the downstream finite residual witness without using the normalized Kurihara/local-dual-exponential coordinate.

The source question is narrow:

> Is there an admitted theorem that proves integral mod-`2` nonvanishing of the bottom Kato Euler-system class on the selected analytic-rank-one, good-ordinary anomalous literal-`p=2` lane?

Characteristic-zero nonvanishing of the Beilinson–Kato class is not sufficient unless its comparison factor is controlled integrally at `2`.

## 2. Protected Kato literal-2 inputs remain available

Existing protected provider records are retained.

### 2.1 Integral Kato classes

`sources/BSD-001/KATO_P2_HEIGHT_ONE_WP17B_SOURCE_AUDIT.md` records that Kato Theorem 12.6 supplies integral Euler-system generators at literal `p=2`.

This gives an integral class to reduce modulo two. It does not prove that the reduction is nonzero.

### 2.2 Literal-2 cyclotomic explicit reciprocity

`sources/BSD-001/R5_RECIP_P2_MAZUR_TATE_KATO_AMENDMENT.md` records that Kurihara–Otsuki explicitly use the relevant Kato cyclotomic explicit-reciprocity mechanism at literal `p=2`.

For the trivial character,

`exp^*(z_Q)`

is proportional to `L(E,1)`. On the selected analytic-rank-one lane `L(E,1)=0`, so this particular scalar evaluation cannot detect `z_Q mod 2`.

The already-protected R5-RECIP derivative construction is the integral finite-character/derivative remedy. R5-WIT has now tested that normalized coordinate on its admitted finite cohort; this source audit does not reinterpret those computations.

## 3. Bertolini–Darmon–Venerucci 2022

Primary source:

Massimo Bertolini, Henri Darmon, Rodolfo Venerucci, *Heegner points and Beilinson–Kato elements: A conjecture of Perrin-Riou*, Advances in Mathematics 398 (2022), 108172, DOI `10.1016/j.aim.2021.108172`.

The source fixes an elliptic curve with semistable reduction at an **odd prime** `p` in the opening paragraph. Theorem A is likewise stated for semistable reduction at an odd prime.

In analytic rank one the theorem compares the localization of the Beilinson–Kato element with the square of the logarithm of a non-torsion rational point, up to a nonzero rational scalar.

This is strong characteristic-zero nonvanishing information at the primes in its scope. It is not a literal-`p=2` theorem, and its equality only up to a nonzero rational scalar would in any event require an independent integral `2`-adic valuation analysis before implying mod-`2` indivisibility.

**Disposition:** `BDV_PERRIN_RIOU_COMPARISON_ODD_P_ONLY_FOR_CURRENT_QUERY`.

## 4. Burungale–Skinner–Tian–Wan 2024

Primary source:

Ashay Burungale, Christopher Skinner, Ye Tian, Xin Wan, *Zeta elements for elliptic curves and applications*, arXiv:`2409.01350` (current source screened for this operation).

The source's general notation states that throughout `p>=3` is an odd prime, with some individual results possibly extending further only when explicitly indicated.

The introduction records the ordinary analytic-rank-one Perrin–Riou comparison literature with `p>2`, and the paper's own good-reduction Perrin–Riou theorem is stated for `p>=5`.

Its principal zeta-element theorem over an imaginary quadratic field assumes `p` does not divide `2N`, which also excludes literal `p=2`.

The paper therefore does not supply the selected direct literal-`2` bottom-class indivisibility theorem.

**Disposition:** `BSTW_ZETA_AND_PERRIN_RIOU_RESULTS_DO_NOT_COVER_LITERAL_P2_DIRECT_DETECTOR`.

## 5. Previously protected finite derivative/Fitting screen

`sources/BSD-001/FINITE_LEVEL_KATO_DERIVATIVE_P2_WP60E_SOURCE_AUDIT.md` already records:

- Burns–Kurihara–Sano's finite-level derivative/Fitting setup fixes odd `p`, with the concrete containment requiring `p>3`;
- the BKS Mazur–Tate determinant route excludes `p=2` in its stated hypotheses;
- Chan-Ho Kim's refined finite-level results assume odd `p`, with key structural results requiring `p>=5`.

Those results cannot be repurposed as a literal-`2` primitive base-class theorem.

## 6. What the audited sources do and do not prove

The audited source estate supports all of the following:

1. the bottom Kato class exists integrally at literal `2`;
2. the selected protected finite Kato derivative has first component equal to the reduction of that bottom class;
3. Kato cyclotomic explicit reciprocity itself has a genuine literal-`2` interface;
4. at analytic rank one the trivial-character explicit-reciprocity scalar vanishes;
5. powerful Beilinson–Kato/Heegner rank-one comparisons prove characteristic-zero nonvanishing in odd-prime settings.

It does **not** currently supply:

`c_Q^Kato mod 2 != 0`

on the selected good-ordinary anomalous rank-one literal-`2` lane.

Nor does it supply a comparison
`c_Q^Kato = u * Kummer(P)`
with `u in Z_2^x` in the selected normalization, which would be sufficient after an independent nondivisibility check on `P`.

## 7. Exact bounded source boundary

Record the downstream source boundary

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.

Potential source-level discharge routes include:

1. a literal-`2` Perrin–Riou/Beilinson–Kato theorem with an integral unit comparison on the selected anomalous ordinary lane;
2. an exact direct computation of a legitimate localization/evaluation of `c_Q^Kato mod 2`;
3. a literal-`2` primitive Kato/Kolyvagin-system theorem implying the same bottom-class nonvanishing;
4. a different finite residual Kato/Kolyvagin component whose nonvanishing is source-admitted and compatible with protected R5-PRIM finite detection.

## 8. Non-exhaustiveness and firewall

This audit is not a theorem that no literal-`2` direct detector exists. It records the exact applicability of the protected source estate and the specifically screened current rank-one comparison sources.

It does not establish R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification.
