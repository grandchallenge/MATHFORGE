# BSD-001 source audit — BSS Lemma 3.9 affine-fiber Chebotarev interface

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#194`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `eaaf7b8c660f3f07030608b3af1334ece5598586`.
- Protected MATHSOLVE anchor: `813156baf3fa57989ddce891f355e2648e99c008`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source: Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448, §3.2, Lemma 3.9 and proof.
- Disposition: `ADMITTED_BSS_LEMMA39_AFFINE_FIBER_INTERFACE`.
- Claim class: exact source/proof interface only.

## Exact downstream query

Protected WP60F identifies the foundational literal-`p=2` boundary

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

The immediate downstream theorem-construction question is whether the numerical hypothesis `s+t<p` in BSS Lemma 3.9 is indispensable in the selected one-primal/one-dual residual situation, or whether its proof can be sharpened using additional structure.

This source audit admits only the exact internal interface of Lemma 3.9 needed to answer that question. It does not perform the downstream sharpening.

## BSS setup

BSS §3.1 takes a self-injective local ring `(R,p)` with residue field `k` of characteristic `p`, a free finite-rank `R`-module `A` with continuous `G_K`-action, and Hypothesis 3.2.

Let `M` be the least power of `p` annihilating `R`, let `K(A)_M` be the extension fixed in §3.1, and let

`tau in G_{K_M}`

be the element supplied by Hypothesis 3.2(ii), so that

`A/(tau-1)A ~= R`.

The set `P` consists of primes whose Frobenius class in `Gal(K(A)_M/K)` is conjugate to `tau`.

## The injective cohomology-to-character map

For

`B in {A, A^*(1)}`,

BSS first uses Hypothesis 3.2(iii) to make restriction injective:

`Res_B : H^1(K,B)
          -> H^1(K(A)_M,B)^{G_K}
          = Hom(G_{K(A)_M},B)^{G_K}`.

It then composes with the quotient map

`B -> B/(tau-1)B`

to obtain

`f_B : Hom(G_{K(A)_M},B)^{G_K}
       -> Hom(G_{K(A)_M}, B/(tau-1)B)`.

The proof shows `f_B` is injective on the indicated equivariant Hom-space: irreducibility and the rank-one quotient imply that `(tau-1)B` contains no nontrivial `G_K`-stable submodule that can occur as the image of a nonzero equivariant homomorphism.

Thus the composite

`j_B := f_B o Res_B`

is injective on `H^1(K,B)`.

## The affine constant and bad fiber

For nonzero

`c in H^1(K,B)`,

choose a 1-cocycle representative `c_tilde : G_K -> B`. BSS defines

`a_c := -c_tilde(tau) in B/(tau-1)B`.

The source notes that `a_c` is independent of the chosen cocycle representative.

The corresponding bad subset of `G_{K(A)_M}` is

`H_c := j_B(c)^{-1}(a_c)`.

For the multiple classes appearing in Lemma 3.9, these are the sets denoted `H_i` and `H_i^*` in the proof.

Because `c` is nonzero and `j_B` is injective, `j_B(c)` is a nonzero group homomorphism. BSS therefore has

`[G_{K(A)_M}:ker(j_B(c))] >= p`.

The published numerical condition `s+t<p` is then used only at this covering step to conclude that the union of the `s+t` affine bad fibers is not all of `G_{K(A)_M}`.

## Chebotarev/localization interface

BSS chooses

`gamma in G_{K(A)_M}`

outside the union of all bad fibers and then applies Chebotarev to primes `q` whose Frobenius in the relevant finite Galois extension is conjugate to

`tau gamma`.

For a primal class `c`, the proof computes, in the canonical quotient identified with the finite local cohomology group,

`loc_q(c)
 = c_tilde(tau gamma)
 = tau c_tilde(gamma) + c_tilde(tau)
 = j_A(c)(gamma) - a_c
   in A/(tau-1)A`.

Consequently

`gamma notin H_c  =>  loc_q(c) != 0`.

The same calculation is made for a dual class in `A^*(1)`.

Thus the downstream replacement problem is exactly a covering problem for the affine fibers `H_c`: if one can prove their union is proper under a stronger structural hypothesis, the remainder of the BSS Chebotarev argument applies unchanged.

## Literal residual `p=2` specialization

In the residual case relevant to the WP60F graph argument, take

`R=k=F_2`.

Hypothesis 3.2(ii) gives

`B/(tau-1)B ~= F_2`

for both `B=A` and `B=A^*(1)`.

For every nonzero cohomology class `c`, the injective map `j_B` sends `c` to a nonzero homomorphism

`j_B(c):G_{K(A)_M}->F_2`.

A nonzero homomorphism to `F_2` is surjective, so

`ker(j_B(c))`

has index `2`, and

`H_c=j_B(c)^{-1}(a_c)`

is one of its two affine fibers. Hence every bad set in the one-primal/one-dual literal-`2` residual problem is an affine index-two fiber.

This observation does not determine whether two such fibers cover the group; that is a downstream group-theoretic question.

## Naturality exposed by the source definitions

The source constructions used above are functorial at the level needed for downstream checking:

- restriction in Galois cohomology is natural in the coefficient module;
- `f_B` is induced by the coefficient quotient `B -> B/(tau-1)B`;
- the affine constant is defined by evaluation of a cocycle at the same element `tau`.

Accordingly, a downstream proof may test compatibility with a specified `G_K`-equivariant coefficient-module isomorphism directly from these definitions. This audit does not assert the result of that test for `A` and `A^*(1)`.

## Exact provider conclusion

The part of BSS Lemma 3.9 that must be replaced at literal `p=2` is now isolated exactly:

> prove that the relevant finite collection of affine fibers
> `j_B(c)^{-1}(a_c)` does not cover `G_{K(A)_M}`.

Once such a proper-union statement is established, the source's Chebotarev and localization calculation supplies the desired simultaneous nonvanishing.

Record the source disposition

`ADMITTED_BSS_LEMMA39_AFFINE_FIBER_INTERFACE`.

## Claim firewall

This audit does not establish:

- that two affine index-two fibers never cover at `p=2`;
- a self-dual literal-`2` replacement for Lemma 3.9;
- core-vertex connectivity at `p=2`;
- the BSS Fitting theorem at `p=2`;
- the elliptic H2/H3 hypotheses;
- R5-LIFT, R5-PRIM, `BSD-R2-A1`, or MATHCERT certification;
- literature exhaustiveness, novelty, or priority.
