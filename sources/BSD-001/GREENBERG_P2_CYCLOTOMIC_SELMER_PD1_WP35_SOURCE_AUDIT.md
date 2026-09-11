# BSD-001 source audit — Greenberg literal-p=2 cyclotomic Selmer cotorsion and finite-submodule exclusion

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP35-P2-CYCLOTOMIC-SQUARE-PRESENTATION`.
- Protected MATHFORGE baseline: `075b91647c22e12aeb0888496966da162db1d771`.
- Protected MATHSOLVE baseline: `9708080c76eb118232d2afb497e2c4803498224d`.
- Primary source inspected: Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv `math/9809206v1` (1998), later in Lecture Notes in Mathematics 1716 (1999), 51–144.
- Exact interfaces inspected: Theorem 1.5, the classical Kummer-Selmer definition in §2, Lemma 4.6 and the p=2 real-place discussion in §4, Propositions 4.9, 4.12, 4.13, and Proposition 4.14.
- Disposition: `QUALIFIED_P2_CLASSICAL_CYCLOTOMIC_SELMER_PD1_INPUT`.
- Claim class: source/applicability evidence only; no main-conjecture equality, analytic generator, Bockstein/regulator normalization, BSD theorem, or certification.

## Exact downstream question

Protected MATHSOLVE WP21 gives the exact primitive classical Kummer control sequence

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`

for

`X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`.

WP21 explicitly left open whether `X_infty` is a torsion projective-dimension-one `Lambda=Z_2[[Gamma]]` module admitting the square presentation required by protected WP20.

The source question is therefore:

> Does Greenberg's cyclotomic classical Selmer theory provide, literally at `p=2` over the totally real cyclotomic tower of `Q`, both cotorsionness of the classical Selmer group and exclusion of proper finite-index Lambda-submodules under the selected no-rational-2-power-torsion hypothesis?

The answer is yes, with the bounded interfaces below.

## Classical Selmer object matches the protected primitive Kummer object

Greenberg §2 defines `Sel_E(M)` from Kummer theory for an elliptic curve over an algebraic extension `M`. In the duality discussion preceding Proposition 4.14 he identifies the classical local condition with

`L_v = Im(kappa_v)`

for every place in a finite set containing the primes above `p`, the archimedean places, and bad-reduction places. He then records

`S_M(F)=Sel_E(F)_p`

for `M=E[p^infinity]` with these Kummer local conditions.

This is the same classical primitive Kummer local-condition convention used by protected WP21: no Greenberg strict, relaxed, or imprimitive condition is substituted in Proposition 4.14.

## Literal p=2 treatment of the real places

The source does not silently discard real places at `p=2`.

In the proof architecture for Lemma 4.6, Greenberg notes that an archimedean place splits completely in `F_infty/F`. When `p=2` and `F_v=R`, the local Kummer quotient can be nonzero and is identified from

`H^1(R,E[2^infinity]) ~= E(R)/E(R)_con`,

of order `1` or `2`. At infinite level the corresponding local module can be

`Hom(Lambda/2Lambda,Z/2Z)`.

The proof of Lemma 4.6 then treats these `p=2` archimedean factors separately rather than assuming divisibility as in the odd-prime case.

Likewise the proof of Proposition 4.9 explicitly identifies the failure of finite `2`-cohomological dimension caused by real places and repairs the argument using the maps to the products of `H^2(F_v,-)` over `v|infinity`. The source concludes the relevant global cohomology statement for all primes `p`, and Proposition 4.12 explicitly records its distinct `p=2` outcome.

Therefore the real-place-safe machinery used by Proposition 4.14 is genuinely developed at `p=2`; the proposition is not an odd-prime statement being silently specialized.

## Theorem 1.5 — cotorsion at p=2

Greenberg states the Kato–Rohrlich theorem as follows: if `E/Q` is modular, `E` has good ordinary or multiplicative reduction at `p`, and `F/Q` is abelian, then

`Sel_E(F_infty)_p`

is `Lambda`-cotorsion.

The theorem statement contains no odd-prime restriction. The paper's ambient setup takes `p` to be any prime and separately tracks the `p=2` archimedean phenomena described above.

For BSD-001 we specialize to

- `F=Q`;
- `p=2`;
- the protected selected class, which has good ordinary reduction at `2`;
- modularity of elliptic curves over `Q`.

Hence the source permits downstream use of

`Sel_E(Q_infty)_2` is `Lambda`-cotorsion,

and therefore its Pontryagin dual `X_infty` is a finitely generated torsion `Lambda`-module.

This source interface is structural only. It does not supply the missing height-one `(2)` analytic characteristic-ideal equality; protected Kato source audits continue to govern that separate D1c boundary.

## Proposition 4.14 — no finite Lambda submodule on the dual

Greenberg Proposition 4.14 states:

If `Sel_E(F_infty)_p` is `Lambda`-cotorsion and `E(F)_p=0`, then `Sel_E(F_infty)_p` has no proper `Lambda`-submodules of finite index.

Again, the proposition statement has no odd-prime hypothesis. Its proof invokes the preceding real-place-safe machinery and the twisted classical Selmer groups, and so remains literal at `p=2`.

Protected WP21 proves on the selected residual `S_3` branch that

`E(Q)[2^infinity]=0`

(and even `E(Q_infty)[2^infinity]=0`). Thus Proposition 4.14 applies with `F=Q`, `p=2`.

Pontryagin duality converts a proper finite-index submodule of the discrete Selmer group into a nonzero finite `Lambda`-submodule of its compact dual. Consequently downstream may use:

`X_infty` has no nonzero finite `Lambda`-submodule.

## Downstream commutative-algebra consequence

The source itself need not state projective dimension one. Once the two source-qualified facts above are combined with standard commutative algebra over

`Lambda ~= Z_2[[T]]`,

the following is an internal downstream deduction:

1. `Lambda` is a regular local ring of dimension `2`.
2. `X_infty` is finitely generated and torsion, so `dim_Lambda X_infty <= 1`.
3. A nonzero `H^0_m(X_infty)` would be a nonzero finite `Lambda`-submodule; Proposition 4.14 excludes this. Thus a nonzero `X_infty` has depth `1`.
4. Auslander–Buchsbaum gives `pd_Lambda X_infty=1`.
5. A finite free resolution therefore has the form

   `0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`,

   because `X_infty` has `Lambda`-rank zero.

The zero-module edge case has the trivial square presentation.

This is exactly the structural square-presentation input contemplated by protected WP21/WP20. The arithmetic specialization still must carry the protected finite control kernel `C_E^vee`; the source does not make that kernel disappear.

## Exact source boundary

This audit admits only:

- the classical Kummer-Selmer identity of the source object;
- literal-`p=2` cotorsionness in the selected `Q`/good-ordinary setting via Greenberg Theorem 1.5;
- literal-`p=2` Proposition 4.14 under `E(Q)[2^infinity]=0`;
- hence exclusion of finite `Lambda`-submodules in `X_infty`.

It does not admit or prove:

- a height-one `(2)` main-conjecture equality;
- an integral analytic determinant generator;
- equality of a source p-adic L-function generator with a determinant of the square presentation;
- vanishing of `C_E^vee`;
- a p=2 Bockstein/regulator comparison;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- the WP31 finite twisted-reciprocity exponent;
- `BSD-R2-A1`;
- novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Provider conclusion

Greenberg's original cyclotomic theory supplies the structural p=2 input that WP21 left open. The selected primitive classical Selmer dual is a finitely generated torsion `Lambda`-module with no nonzero finite `Lambda`-submodule. Standard regular-local commutative algebra can therefore promote it downstream to projective dimension one and a square finite-free presentation.

The remaining specialization defect is not hidden: it is exactly the already protected kernel `C_E^vee` from WP21 and must be retained in the WP20 first-Fitting factor.

**Disposition:** `QUALIFIED_P2_CLASSICAL_CYCLOTOMIC_SELMER_PD1_INPUT`.