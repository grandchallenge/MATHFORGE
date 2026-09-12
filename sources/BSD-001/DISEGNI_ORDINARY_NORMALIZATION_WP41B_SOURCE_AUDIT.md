# BSD-001 source audit — exact ordinary normalization in Disegni's p-adic Gross–Zagier formula

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP41B-DISEGNI-ORDINARY-NORMALIZATION`.
- Protected MATHFORGE predecessor: `9de5bac5a18193b9453146dd0db9dee2f34ab06a`.
- Protected MATHSOLVE predecessor: `af41471670639648db0aa96ed493333d2bf1536e`.
- Primary source: Daniel Disegni, *The universal p-adic Gross–Zagier formula*, Invent. Math. 230 (2022), 509–649, together with Appendix B containing the published correction.
- Public author PDF: `https://disegni-daniel.perso.math.cnrs.fr/univ.pdf`.
- Exact source loci: Theorem B in §1.2; equations (1.4.5)–(1.4.6); Definition 4.3.1; Lemma 4.3.3, equation (4.3.4); Proposition 4.3.4; Theorem B^ord and Lemma 7.1.2; Appendix B correction.
- Disposition: `QUALIFIED_EXACT_ORDINARY_NORMALIZATION_CANCELLATION`.
- Claim class: source/normalization admission only; no BSD or MATHCERT promotion.

## Source-access note

The author PDF was opened as a PDF and its searchable primary-source text was inspected at the exact loci above. Page-render screenshot calls for the pages containing Proposition 4.3.4 were attempted as required by the execution environment, but the screenshot backend returned an internal rendering error. The text layer remained available and supplied exact line-level formulae. This audit therefore binds the public PDF identity and exact theorem/equation locators, but does not claim a successful page-image lock or independently recomputed byte digest.

## Protected downstream starting point

Protected MATHSOLVE WP09 already proves that, for the selected all-`2N`-split auxiliary imaginary quadratic field `K`, corrected Disegni Theorem B applies literally at `p=2` to the weight-two modular representation of `E` with trivial Hecke character. It records the source-normalized identity

`height/(automorphic pairing)`

`= e_{2,infinity}(V_(pi,1))^(-1) * L'_2(V_(pi,1),0) * Q`.

The open D2c question is the exact integral contribution of the factor

`e_{2,infinity}^{-1} Q`.

This audit asks only whether Disegni's own ordinary normalization rewrites that combination exactly, before any local valuation is computed.

## Trivial-weight specialization

Disegni §1.2 states that the trivial-weight case has

`w=(0;(2,...,2))`, `l=(0;(0,...,0))`.

This is the weight-two elliptic/Heegner-point lane used by protected WP09. In this lane the algebraic coefficient representation `W` is trivial, hence

`dim W = 1`.

Equation (1.4.5) defines

`e_infinity = i^((w+l)[F:Q])`.

At trivial weight its exponent is zero, so

`e_infinity = 1`

and therefore

`e_{p,infinity}=e_p`.

For the selected campaign `F=Q`, `p=2`, so the Theorem-B interpolation factor is exactly the finite `p`-factor appearing in Proposition 4.3.4.

## Proposition 4.3.4 — exact absorption of the interpolation factor

For an ordinary representation

`Pi = pi tensor chi = Pi_infinity tensor W`,

Proposition 4.3.4 defines the ordinary operators `gamma_H'^ord` and `w_a^ord` and proves, for ordinary vectors with nonzero denominator,

`Q( gamma_H'^ord(f1) tensor gamma_H'^ord(f2)
    / (w_a^ord(f3) tensor f4) )`

`= e_p(V_(pi,chi)) * dim(W) * Q^ord((f1 tensor f2)/(f3 tensor f4)).`

In the protected trivial-weight lane, `dim(W)=1` and `e_{p,infinity}=e_p`. Hence for the source-defined special quadruple one obtains the exact identity

`e_{p,infinity}^{-1} * Q_special = Q^ord`.

At `p=2` this is

`e_{2,infinity}^{-1} * Q_special = Q^ord`.

This is equality in Disegni's normalization. It is not an equality only up to a `2`-adic unit.

## Theorem B^ord — the same cancellation in the Gross–Zagier formula

Theorem B^ord in §7.1.1 states directly that, under the same assumptions as corrected Theorem B,

`height^ord/(ordinary automorphic pairing)`

`= L'_p(V_(pi,chi),0) * Q^ord`.

There is no separate `e_{p,infinity}^{-1}` factor in this ordinary formula.

Lemma 7.1.2 proves, for non-exceptional `Pi`, that Theorem B^ord is equivalent to Theorem B. Its proof uses exactly Proposition 4.3.4 and the special quadruple above. Thus the disappearance of the interpolation factor is not an informal cancellation; it is the source's exact equivalence between the two formulae.

Protected WP09 already checks non-exceptionality in the selected good-ordinary lane, so this equivalence is compatible with the admitted application.

## Published correction

Appendix B defines `S_{p,ns}` as the `p`-adic places of `F` nonsplit in the CM extension and imposes condition `(star)`:

for every `v in S_{p,ns}`, `v` is inert and `chi_v` is unramified.

The correction states that both Theorem B and Theorem B^ord require this extra condition.

Protected WP09 chooses the auxiliary field so that `2` splits in `K`. For `F=Q`, `p=2`, the set `S_{2,ns}` is therefore empty, so `(star)` is vacuous in the selected lane. The correction does not disturb the ordinary-normalization equivalence used here.

## Lemma 4.3.3 — exact decomposition of the remaining ordinary factor

The ordinary factor is not automatically a unit. Lemma 4.3.3, equation (4.3.4), decomposes `Q^ord` into explicit source-normalized factors:

- local toric pairings `Q_{v,dt_v}` at the finite auxiliary set `Sigma'`;
- for `v in Sigma`, the measure factor `vol(E_v^x/F_v^x,dt_v)`, the local factor `L(V_(pi,chi),v,0)^(-1)`, and the indicated vector-ratio term;
- the remaining `S p infinity` vector ratio;
- the ordinary `p infinity` pairing `Q^ord_{p infinity,dt_{p infinity}}`.

Therefore the exact D2c successor is a place-by-place valuation problem for this complete product. No measure factor, bad-prime factor, vector normalization, or ordinary local term may be discarded as a unit without proof.

## Exact downstream interface admitted after protection

MATHSOLVE may use the following bounded statements for the already-protected WP09 application.

1. For source-compatible special ordinary test vectors in the selected trivial-weight lane,

   `e_{2,infinity}^{-1} Q_special = Q^ord`.

2. Equivalently, the corrected ordinary Gross–Zagier formula is

   `height^ord/(ordinary pairing) = L'_2 * Q^ord`.

3. The remaining ordinary factor `Q^ord` has the exact decomposition of Disegni Lemma 4.3.3 / (4.3.4).

4. No conclusion is admitted yet about `ord_2(Q^ord)` or about any individual local factor being a `2`-adic unit.

## Refined D2c boundary

The former broad boundary

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`

is narrowed to

`MISSING_P2_DISEGNI_QORD_LOCAL_FACTOR_VALUATIONS`.

The explicit interpolation factor itself no longer needs to be valued separately once the source-compatible ordinary test-vector normalization is used; it is absorbed exactly into `Q^ord`.

## Claim firewall

This audit does not prove:

- `Q^ord` is a `2`-adic unit;
- any value for `ord_2(Q^ord)`;
- cancellation of Tamagawa, period, Manin, isogeny, measure, or bad-prime factors not present in Proposition 4.3.4;
- equality of the p-adic height with the WP00 Neron–Tate regulator;
- fixed-`2` height nondegeneracy;
- an analytic determinant generator at height-one `(2)`;
- the final quadratic descent to `Q`;
- `BSD-R2-A1`;
- MATHCERT certification, theorem novelty, or priority.