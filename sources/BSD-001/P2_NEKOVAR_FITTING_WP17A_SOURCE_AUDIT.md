# BSD-001 source audit — WP17A `p=2` Selmer-complex/Fitting interfaces

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#141`.
- Protected Forge baseline: `118ae1b5c2fc2630f53000921b742c610c50db16`.
- Downstream protected MATHSOLVE baseline: `988462b215853317f7719f5795f807e12b49550b`.
- Screen date: `2026-09-08`.
- Disposition: `QUALIFIED_P2_SELMER_COMPLEX_FRAMEWORK_DIMENSION_BARRIER`.
- Claim class: bounded source/applicability evidence only; no theorem promotion or certification.

## Exact downstream query

Protected MATHSOLVE WP16B fixes the primitive classical integral invariant

`T_E := Tor_{Z_2}(Sel_{2^infinity}^{Kum}(E/Q)^vee)`

and proves

`Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

The WP17 source question is therefore no longer a broad search for a `p=2` BSD theorem. It is:

> Is there a literal `p=2` theorem, preferably over the protected WP09 imaginary quadratic field `K`, that controls this primitive rank-one dual-Selmer torsion/Fitting invariant, or an integral Selmer-complex invariant with an exact comparison to it?

This audit screens the closest modern general Selmer-complex/Euler-system framework and one useful split-`2` imaginary-quadratic comparator.

# Source A — Bullach–Burns: Euler systems and Nekovář–Selmer complexes

## Primary source

Dominik Bullach and David Burns, *On Euler systems and Nekovář–Selmer complexes*, arXiv:`2509.13894`.

Primary source inspected:

- arXiv record `2509.13894`;
- current author-hosted PDF: `https://dominikbullach.github.io/bb.pdf`.

The paper develops Euler/Kolyvagin-system machinery for Nekovář–Selmer complexes over local complete Gorenstein rings and explicitly includes characteristic `2` in parts of the abstract framework. The source is therefore materially closer to the protected WP16B invariant than the previously screened odd-prime rank-one BSD applications.

## General coefficient-ring and archimedean surface

Section 3.1 works over a local complete Gorenstein ring `R` with finite residue field of characteristic `p`.

The paper records an additional convention for characteristic `2`:

`if p = 2, then k has no real places`.

**Locator:** equation `(3.1)`, source printed p.23.

For the preferred WP09 arena this archimedean condition is compatible: the protected field `K` is imaginary quadratic and has no real places. This removes one possible obstruction but does not establish applicability of the main Euler-system theorem.

## Exact characteristic-2 hypothesis in the main abstract theorem

The decisive source condition is Hypotheses 4.14.

Hypothesis 4.14 requires, among other conditions:

1. irreducibility of the relevant residual representations;
2. an element `tau` for which the quotient by `tau-1` has dimension one;
3. vanishing of a specified `H^1` group;
4. extra disjoint-subquotient conditions when `p` is `2` or `3`;
5. Selmer-complex control hypotheses and positivity conditions;
6. compact `p`-adic analytic image conditions.

In addition, Hypothesis 4.14(ii*) states literally:

`If p = 2, then dim_K(T-bar) = 1.`

Here `K` is the residue field of the coefficient ring in the paper's notation and `T-bar` is the residual representation.

**Locator:** Hypotheses `(4.14)`, source printed p.48.

### Consequence for the selected elliptic representation

For an elliptic curve, the residual representation `E[2]` is a two-dimensional `F_2`-vector space. Protected MATHSOLVE WP12 in fact places the selected class in the surjective `GL_2(F_2) ~= S_3` residual-image branch.

Therefore a direct specialization of Bullach–Burns Theorem 4.20 to the selected `p=2` elliptic representation fails Hypothesis 4.14(ii*): the residual dimension is `2`, not `1`.

This is an exact applicability failure. It is not a claim that the proof cannot someday be extended to two-dimensional residual representations at `2`.

## Exact strength of Theorem 4.20

Theorem 4.20 assumes Hypotheses 4.14 and 4.16 together with a positivity condition on a free module quotient `Y`. Its conclusion is a determinant/Fitting **containment** for Euler-system classes after localizing at prime ideals satisfying further conditions.

**Locator:** Theorem `(4.20)`, source printed p.50.

The theorem is not, by its statement alone:

- an equality of the primitive finite `Z_2` Fitting ideal fixed in WP16B;
- an opposite pair of divisibilities;
- a primitivity theorem;
- an analytic comparison to the WP00-normalized complex derivative.

It is nevertheless a highly relevant theorem shape because it relates Euler systems, determinant lines, and Fitting data for Nekovář structures.

## Hypothesis 4.16 cannot remove the dimension barrier

Remark 4.21 states that if suitable Kolyvagin systems are already known to exist, one can avoid Hypothesis 4.16 in proving the displayed containment of Theorem 4.20.

**Locator:** Remark `(4.21)`, source printed p.50; see also Remark `(7.8)`, printed p.92.

This does **not** remove Hypothesis 4.14, and in particular does not remove Hypothesis 4.14(ii*). Existing Kolyvagin-system input therefore does not turn Theorem 4.20 into a selected `p=2`, residual-dimension-two theorem.

## Local-condition comparison remains substantive

The Bullach–Burns framework can accommodate Nekovář structures, including Greenberg-type local conditions in suitable settings. Protected WP16B, however, fixes the finite classical primitive Kummer tower and explicitly forbids identifying its local condition at `2` with a Greenberg/ordinary connected–étale condition without an exact comparison theorem.

Therefore, even if the residual-dimension obstruction were removed, a downstream application would still have to:

1. identify the exact Nekovář structure used by the theorem;
2. compare its local condition at every place above `2` with the WP16B Kummer condition;
3. compare primitive versus imprimitive conditions at bad primes;
4. compute every finite kernel/cokernel or determinant defect with its full `2`-adic length.

## Rational elliptic-curve application remains odd-prime

The paper's concrete Kato/Iwasawa application for rational elliptic curves does not supply a hidden `p=2` exception.

In §9.2 the construction of the archimedean basis is made for each **odd prime** `p`, and Theorem 9.4 begins:

`If p > 3, ...`

**Locator:** §9.2 and Theorem `(9.4)`, source printed p.128.

Thus the explicit rational-elliptic application is independently outside the selected prime.

## Bounded source conclusion for Source A

Bullach–Burns supplies:

- a modern integral Selmer-complex/Euler-system/Fitting framework;
- genuine characteristic-2 technical treatment in portions of that framework;
- a theorem shape potentially relevant to determinant/Fitting control;
- an exact source-level explanation of why the current main theorem does not directly apply to the selected `p=2` elliptic residual representation.

The exact direct obstruction is Hypothesis 4.14(ii*), not merely the fact that the later elliptic application was written for `p>3`.

**Disposition:** `P2_AWARE_FRAMEWORK_RESIDUAL_DIMENSION_EXCLUDES_SELECTED_E2`.

# Source B — Müller: split-prime `p=2` main conjecture over imaginary quadratic fields

## Primary source

Katharina Müller, *The Main Conjecture for Imaginary quadratic fields for the split prime p=2*, arXiv:`2002.05647`.

The source assumes an imaginary quadratic field in which `2` splits, constructs the unique `Z_2`-extension unramified outside one prime over `2`, and proves a main conjecture for the Galois module

`X = Gal(M/L_infinity)`,

where `M` is the maximal `2`-abelian extension of `L_infinity` ramified only at the selected prime over `2`.

Theorem 1.1 identifies characteristic ideals built from class groups, local/global units, and elliptic units.

**Locators:** introduction and Theorem `1.1` of arXiv:`2002.05647`.

## What this comparator proves

This source is useful because it shows that the combination

`imaginary quadratic field + split prime 2 + integral Iwasawa main conjecture`

is not itself structurally impossible.

Its object is nevertheless a class-field-theoretic `G_m`/elliptic-unit Iwasawa module. The CM elliptic curve appearing in the construction is used to produce elliptic units and the relevant `p`-adic `L`-function.

The theorem does **not** identify the primitive dual Selmer torsion of the selected non-CM elliptic curve, and it does not provide an exact comparison to protected WP16B's `T_E`.

**Disposition:** `POSITIVE_P2_SPLIT_IQ_WRONG_MOTIVE_FOR_SELECTED_E`.

# Joint WP17A diagnosis

The two sources sharpen the protected frontier without proving it.

1. Bullach–Burns demonstrates that modern Nekovář–Selmer/Euler-system determinant machinery can be formulated with real characteristic-2 content, but its principal abstract theorem requires residual dimension one when `p=2`. The selected elliptic representation has residual dimension two.
2. The Bullach–Burns concrete rational-elliptic application is separately restricted to `p>3`.
3. Müller proves a genuine split-`2` imaginary-quadratic main conjecture, but for a class-field/elliptic-unit module rather than the selected non-CM elliptic Selmer representation.
4. Neither source controls

   `Fitt^0_{Z_2}(Tor(Sel_{2^infinity}^{Kum}(E/K)^vee))`

   for the selected elliptic curve over the protected WP09 field `K`, nor an explicitly proved equivalent determinant invariant.
5. Neither source supplies the exact primitive-Kummer versus Greenberg/imprimitive comparison required by WP16B.
6. Neither source supplies the exact analytic comparison from such a Fitting ideal to the WP00-normalized complex derivative with every Tamagawa and descent correction retained.

## Successor-source query

Further reconnaissance should now ask only whether there is a successor theorem that removes or bypasses the Bullach–Burns Hypothesis 4.14(ii*) residual-dimension-one condition **for two-dimensional residual representations at `p=2`**, while retaining enough determinant/Fitting information and compatible local conditions to reach the WP16B invariant.

A paper that merely cites Bullach–Burns, works at odd `p`, treats a one-dimensional motive, or proves a class-field main conjecture does not answer that query.

## Provider boundary

This audit does not establish:

- impossibility of a two-dimensional `p=2` Euler/Kolyvagin-system theorem;
- impossibility of exact integral Fitting control by a different method;
- equality between Kummer and Greenberg local conditions at `2`;
- an imprimitive/primitive Tamagawa comparison;
- an exact Heegner-index formula;
- the analytic-to-algebraic Fitting equality;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.

## Provider disposition

`QUALIFIED_P2_SELMER_COMPLEX_FRAMEWORK_DIMENSION_BARRIER`

Downstream use is limited to the exact theorem shapes, characteristic-2 hypotheses, applicability exclusions, and positive wrong-motive comparator recorded above.