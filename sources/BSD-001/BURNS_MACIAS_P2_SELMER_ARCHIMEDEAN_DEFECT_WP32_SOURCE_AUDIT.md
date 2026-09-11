# BSD-001 source audit — Burns–Macias Castillo p=2 perfect Selmer complex and archimedean defect

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP32-P2-PERFECT-SELMER-ARCHIMEDEAN-DEFECT`.
- Protected MATHFORGE baseline: `5b07785c9ca96ec0c2003bbe3ada46c807e50882`.
- Protected MATHSOLVE baseline: `6f34bba352024d864fd83c98b0532e8c71002e24`.
- Primary source: David Burns and Daniel Macias Castillo, *On Refined Conjectures of Birch and Swinnerton-Dyer Type for Hasse-Weil-Artin L-Series*, Memoirs of the American Mathematical Society 297 (2024), no. 1482, DOI `10.1090/memo/1482`; arXiv `1909.03959v3`.
- Exact source interfaces inspected: §2.3 Proposition 2.8 and equations (17)–(20); §2.4 Definition 2.10 and Proposition 2.12; §6.1 Proposition 6.4; §10 and Appendix C.
- Secondary real-place reference used only to delimit a downstream elementary computation: J. S. Milne, *Arithmetic Duality Theorems*, real local-field discussion identifying Tate cohomology `H_T^0(G,A(C))` with `pi_0(A(R))`.
- Disposition: `QUALIFIED_P2_PERFECT_SELMER_COMPLEX_WITH_EXPLICIT_ARCHIMEDEAN_FINITE_DEFECT`.
- Claim class: source/applicability admission only; no determinant generator, Bockstein normalization, BSD, or MATHCERT promotion.

## Exact downstream question

Protected WP20 reduced the selected rank-one BSD target to two arithmetic obligations: an exact primitive rank-one determinant realization and an exact Bockstein/WP00 normalization. Existing protected screens found that nearby integral determinant/main-conjecture theorems either retain odd-prime hypotheses or lose the height-one prime `(2)`.

The present question is narrower:

> Does an existing source construct a genuinely perfect Selmer complex at `p=2` over a number field with real places, and if so, what exact finite `2`-primary defect prevents its cohomology from identifying integrally with the classical Mordell-Weil/Selmer modules needed by BSD-001?

Burns–Macias Castillo answer this precisely.

## Literal `p=2` perfect complex

In §2.3 the authors define a Nekovar-style Selmer complex

`SCS(A_F/k; X, X')`

using local Kummer conditions at finite places and a chosen archimedean lattice `X'`.

Immediately before Proposition 2.8 they define the comparison category `Mod*(Z_p[G])` to be the ordinary module category for odd `p`, but for `p=2` the quotient of `Mod(Z_2[G])` by finite `Z_2[G]`-modules.

Proposition 2.8 nevertheless gives a genuine integral perfect-complex statement before passing to that quotient:

- `SCS` belongs to `D^perf(Z_p[G])`;
- it is acyclic outside degrees `1,2,3`;
- its degree-three cohomology is canonically

  `H^3(SCS) ~= A(F)[p^infinity]^vee`.

Thus perfectness itself survives literally at `p=2`.

The loss at `p=2` occurs in the arithmetic identification of `H^1` and `H^2`, not in existence of the perfect complex.

## The exact p=2 defect is archimedean and finite

The proof of Proposition 2.8 compares `SCS` with the classical `p`-adic Selmer complex and gives the canonical long exact sequence (20).

For the present purpose its decisive terms are:

- `cok(H^0(kappa_2))`, arising from the chosen archimedean projective lattice;
- for every real place `v`,

  `H^1(k_v,T_p(A^t))`

  and

  `H^2(k_v,T_p(A^t))`.

The source states explicitly that these real-place cohomology groups vanish for odd `p` and are finite for `p=2`; `cok(H^0(kappa_2))` is likewise finite of `2`-power order.

This is why Proposition 2.8(iii) identifies `H^1` and `H^2` with the expected arithmetic modules only in the quotient category `Mod*` at `p=2`.

Definition 2.10 makes the same point geometrically: a perfect Selmer structure at an archimedean place uses a projective submodule of finite `2`-power index in the natural archimedean module. The finite index is part of the literal `p=2` data and cannot be discarded in BSD-001.

## Global perfect Selmer structure

Proposition 2.12 constructs a global complex

`CS(X) in D^perf(Z[G])`

whose `p`-adic realizations recover the local perfect Selmer complexes. It again records

`H^3(CS(X))=(A(F)_tor)^vee`

and describes `H^1` and `H^2` only modulo finite `2`-power modules at the prime `2`.

Accordingly, the source supplies a true perfect integral object suitable for determinant methods, but not an exact integral identification of its degree-two cohomology with the classical `2`-primary Selmer dual.

## Classical Selmer complex at p=2

The same distinction appears in §6.1.

Proposition 6.4 treats the classical complex `SC_2(A_F/k)` literally at `p=2` and proves:

- it is acyclic outside degrees `1,2,3`;
- under finiteness of Sha, `H^1` is the image of the injective global Kummer map;
- there is a canonical map

  `Sel_2(A_F)^vee -> H^2(SC_2)`

  with finite kernel and finite cokernel;
- `H^3` is finite.

The proof displays the real-place groups `H^j(k_v,T_2(A^t))` as the finite obstruction terms. Thus the classical complex also fails to give an exact p=2 Selmer-dual identification without evaluating those finite terms.

## Selected BSD-001 specialization

For BSD-001, take `F=k=Q`, `A=E`, and `p=2`.

The protected selected branch has irreducible `E[2]`. Therefore

`E(Q)[2]=0`.

Any rational point of order `2^r`, `r>=1`, would have a nonzero rational `2`-torsion multiple, so

`E(Q)[2^infinity]=0`.

Combining this protected arithmetic fact with Proposition 2.8(ii) gives downstream permission to conclude

`H^3(SCS)=0`

for a source-compatible Burns–Macias p=2 perfect Selmer complex attached to the selected curve.

Hence on the selected branch the source perfect complex is genuinely acyclic outside degrees `1` and `2`.

This is a substantive improvement over the generic p=2 statement. It does **not** by itself identify `H^2` with the protected primitive module `X_E`; the finite real-place comparison defect remains.

## Real-place structure available for downstream calculation

For an abelian variety over `R`, classical real local duality identifies the degree-zero Tate cohomology of `A(C)` with the real component group

`pi_0(A(R))`.

For an elliptic curve this component group has order `1` or `2`.

This permits a downstream elementary calculation of the finite groups

`H^1(R,T_2E)` and `H^2(R,T_2E)`

from the integral action of complex conjugation on `T_2E` and the topology of `E(R)`.

This audit does **not** pre-assert the result of that calculation or its exact contribution to the Burns–Macias archimedean lattice term.

## Bockstein formalism versus arithmetic height comparison

Appendix C develops an abstract Bockstein construction for a perfect two-term complex. In particular the formalism itself is ring-theoretic and applies to a complex in `D^perf(Z_p[G])` that is acyclic outside degrees `1` and `2` with the stated freeness hypotheses.

However, the arithmetic height comparison in §10 explicitly invokes Proposition 6.3 to identify the classical Selmer complex with Mordell-Weil and Selmer modules. Proposition 6.3 is the odd-prime statement. The authors separately replace it at `p=2` by Proposition 6.4, whose degree-two comparison has finite kernel and cokernel.

Therefore the source does **not** supply a literal-p=2 theorem identifying its Bockstein pairing with the exact Mazur–Tate/Nekovar height on the classical Selmer module over `Q`.

Downstream must not use Appendix C alone to bypass the real-place finite defect.

## What the source supplies to BSD-001

Downstream may use the following bounded interface after protected admission:

1. A literal-`p=2` perfect Nekovar-style Selmer complex exists over `Q`, despite the real place.
2. Its generic cohomological amplitude is `[1,3]` and

   `H^3 ~= E(Q)[2^infinity]^vee`.

3. On the protected irreducible `E[2]` branch, `H^3=0`, so the source-compatible perfect complex is a two-term perfect complex in degrees `1,2`.
4. At `p=2`, exact comparison with the classical Mordell-Weil/Selmer modules is obstructed only by explicit finite `2`-primary terms appearing in equation (20), including the real-place groups `H^1(R,T_2E)`, `H^2(R,T_2E)`, and the archimedean lattice cokernel.
5. The source's abstract Bockstein formalism does not itself evaluate those terms or identify the resulting p=2 Bockstein with the protected WP00 normalization.

## What this source does not establish

The source does not establish for the BSD-001 selected class:

- `H^2(SCS) ~= X_E` exactly;
- that the finite real-place correction vanishes;
- the exact order or map-level role of `H^1(R,T_2E)` or `H^2(R,T_2E)` in the selected complex;
- an exact comparison between the source archimedean lattice and the protected full Neron period `Omega_E`;
- a primitive-Kummer cyclotomic deformation specializing exactly to `X_E`;
- a height-one `(2)` analytic determinant generator;
- an exact p=2 Mazur–Tate/Nekovar/Bockstein regulator identity;
- D1a, D1c, or D2;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Provider conclusion

Burns–Macias Castillo materially changes the p=2 determinant frontier. The obstruction is not absence of a perfect Selmer complex. A perfect integral complex exists, and the selected residual hypothesis kills its degree-three rational-torsion term. The remaining exact comparison defect is finite, `2`-primary, and explicitly archimedean in the source comparison sequence.

This reduces the next determinant-side question to an exact real-place correction problem rather than a generic lack of p=2 perfectness.

**Disposition:** `QUALIFIED_P2_PERFECT_SELMER_COMPLEX_WITH_EXPLICIT_ARCHIMEDEAN_FINITE_DEFECT`.

## Claim firewall

This source admission changes no protected mathematical claim state. It authorizes only the bounded applicability statements above.
