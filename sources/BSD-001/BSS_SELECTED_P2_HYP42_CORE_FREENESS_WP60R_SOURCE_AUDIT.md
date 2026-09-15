# BSD-001 source audit — literal-2 cartesian core-vertex freeness for WP60R

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#207`.
- Downstream operation: `grandchallenge/MATHSOLVE#243` (`WP60R`).
- Protected MATHFORGE base: `280646bf69cba8fbb77ba47eb97dda0fb495baa6`.
- Protected MATHSOLVE anchor: `83046d8e227003d277196b25dd7f17bbf5ec717b`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Protected predecessor: `sources/BSD-001/BSS_SELECTED_P2_CANONICAL_CORE_RANK_WP60P_SOURCE_AUDIT.md`.
- Primary cross-check: Ryotaro Sakamoto, *The theory of Kolyvagin systems for p = 3*, Lemma 3.7.
- Underlying protected Mazur–Rubin interfaces: cartesianness on finite quotients and the p=2-compatible global-duality/core-rank formula admitted by WP60P.
- Claim class: bounded source/applicability interface only.

## Exact downstream query

BSS II Hypothesis 4.2 requires a modified Selmer structure for which the dual modified Selmer group vanishes and the corresponding primal group is free of the expected rank over the finite coefficient ring.

Protected WP60P already proves, at literal `p=2`, that the exact canonical structure on every quotient

`A_m := E[2^m]`, `R_m := Z/2^m`

is cartesian and has core rank one. WP60R needs the additional algebraic implication

`dual modified Selmer = 0  =>  primal modified Selmer is free of the modified core rank`,

plus the corresponding coefficient-reduction identification.

The issue is whether this implication is itself small-prime-sensitive.

## 1. Sakamoto Lemma 3.7 separates the algebraic interface from p=3 localization

Sakamoto Lemma 3.7 is stated for a cartesian Selmer structure over a zero-dimensional Gorenstein local ring. For pairwise coprime modification ideals `a,b,c`, it records three algebraic facts:

1. the modified structure is cartesian and its core rank changes by `nu(a)-nu(b)`;
2. if the modified dual Selmer module vanishes, the modified primal Selmer module is free over the coefficient ring of rank equal to that modified core rank;
3. the fixed residual-to-full coefficient injection identifies the residual modified Selmer module with the maximal-ideal torsion of the full modified Selmer module.

The proof of these statements cites the general cartesian/core-vertex machinery. It does not invoke the later p=3 localization results used in Sakamoto §§5–6 to prove useful-prime and graph-connectivity statements.

Accordingly, Lemma 3.7 is useful here only as an exact dependency cross-check. This audit does **not** import Sakamoto's p=3 localization theorems to literal `p=2`.

## 2. Literal-2 reconstruction from already protected interfaces

The required freeness implication can be reconstructed on the selected literal-2 lane without the p=3 localization machinery.

Let `F'` be any BSS canonical modification on `A_m` obtained from the protected cartesian canonical structure. Protected WP60P supplies cartesianness on every finite quotient. The standard propagation rules preserve cartesianness under the finite/transverse/full/zero modifications used by the BSS core-vertex formalism.

Assume

`H^1_{F'^*}(Q,A_m^*(1)) = 0`.

Cartesian coefficient reduction identifies the residual primal group with the `2`-torsion of the full primal group:

`H^1_{F'bar}(Q,E[2]) ~= H^1_{F'}(Q,A_m)[2]`.

The dual analogue and the assumed full dual vanishing give residual dual dimension zero. Hence the residual primal dimension is exactly the modified core rank `r'`.

The p=2-compatible global-duality length formula admitted in the protected Mazur–Rubin interface gives, when the dual group vanishes,

`length_Rm H^1_{F'}(Q,A_m) = m r'`.

A finite `R_m=Z/2^m`-module whose `2`-torsion has `F_2`-dimension `r'` and whose `R_m`-length is `m r'` must be free of rank `r'`: writing the module as a direct sum of cyclic `Z/2^{e_i}` modules, the first condition says there are exactly `r'` summands and the length condition forces every `e_i=m`.

Therefore

`H^1_{F'}(Q,A_m) ~= R_m^{r'}`.

This argument is characteristic-two algebra. It uses cartesianness, coefficient reduction, and the protected p=2 global-duality formula; it does not use BSS Lemma 3.9, Sakamoto Lemma 5.2/Corollary 5.5, or any odd-prime covering argument.

## 3. Application to the selected canonical lane

Protected WP60P gives the unmodified selected canonical core rank

`chi(Fcan)=1`

on every `A_m`. For BSS auxiliary modifications the usual core-rank bookkeeping gives the corresponding modified rank. In particular, whenever the modified dual Selmer group vanishes, the preceding reconstruction proves the exact freeness clause required by BSS Hypothesis 4.2 for that finite coefficient level.

Record

`SELECTED_P2_CARTESIAN_CORE_VERTEX_FREENESS_AVAILABLE`.

Together with the protected WP60M coefficient-reduction interface, this supplies the algebraic Hypothesis-4.2 freeness layer needed by downstream WP60R once WP60R constructs the required dual-zero modified vertex using literal-2 auxiliary primes.

## 4. Boundary retained

This audit does not itself prove existence of the required dual-zero auxiliary modification. That is a localization/core-vertex construction and remains a downstream WP60R obligation.

It also does not repair formal BSS Hypothesis 3.2(iii), which protected WP60K/WP60M show is false globally above the residual level. The freeness argument needs only cartesian coefficient reduction on the actual modified Selmer modules and the protected p=2 global-duality interface.

## Provider disposition

`SELECTED_P2_CARTESIAN_CORE_VERTEX_FREENESS_AVAILABLE`.

The exact downstream meaning is:

> For every selected finite coefficient module `E[2^m]` and every BSS canonical modification, dual modified Selmer vanishing implies that the primal modified Selmer module is free over `Z/2^m` of rank equal to its modified core rank; residual coefficient reduction identifies the residual group with the full group's 2-torsion.

This interface is independent of the p=3-specific useful-prime/connectivity theorems.

## Claim firewall

This audit does not establish:

- existence or connectivity of literal-2 BSS core vertices at every finite coefficient level;
- full formal BSS Hypothesis 3.2(iii);
- BSS II Theorem 5.20, Theorem 5.2, Theorem 5.25, or Corollary 6.15 at literal `p=2`;
- the height-one `(2)` Kato/Fitting divisibility;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
