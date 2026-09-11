# BSD-001 source audit — Tan good-ordinary universal-norm filtration at `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP28-P2-GOOD-ORDINARY-NORM-COMPATIBILITY`.
- Protected Forge baseline: `b09faf74936611616465186c8702ea0ce6f36828`.
- Downstream MATHSOLVE frontier: WP27 candidate over protected `47365c058f4362684327bdb268d98c0981e2f001`; downstream use remains forbidden until WP27 itself is protected.
- Primary source: Ki-Seng Tan, *A generalized Mazur's theorem and its applications*, Transactions of the American Mathematical Society 362 (2010), no. 8, 4433–4450, DOI `10.1090/S0002-9947-10-05042-7`.
- Primary full text inspected: author-uploaded published article carrying the AMS volume/page/DOI metadata.
- Exact source interface: Introduction equations (1)–(3), Theorem 1, Theorem 2, and Lemma 2.7.1; Corollary 2.3.3 remains separately admitted by the protected WP25 source audit.
- Disposition: `QUALIFIED_P2_GOOD_ORDINARY_UNIVERSAL_NORM_FILTRATION`.
- Claim class: source/applicability admission only; no BSD, determinant, regulator, or MATHCERT promotion.

## Exact downstream question

Protected WP25 identifies the local universal-norm quotient

`U_2 = E(Q_2)/N_2^infinity`

with `K_2^vee`. WP27 seeks an exact two-step filtration of this finite group but deliberately does not identify its quotient coordinate with literal reduction or its submodule with a formal universal-norm quotient.

The downstream source question is therefore narrow:

> For a good-ordinary elliptic curve over `Q_2` and its totally ramified local cyclotomic `Z_2`-extension, does a literal `p=2` theorem give an exact universal-norm sequence induced by the reduction/formal-group sequence, prove that the formal norm quotient injects into the full norm quotient, and identify that norm sequence as Pontryagin-dual to the corresponding local Galois-cohomology sequence?

Tan's Theorems 1–2 answer this question affirmatively.

## Prime range and local extension

Tan's Introduction begins with a complete local field `K` having finite residue field of characteristic `p`, an abelian variety `A/K` with good ordinary reduction, and its dual abelian variety `B`.

Theorem 1 specializes further to:

- `K` a finite extension of `Q_p`;
- `L/K` a totally ramified `Z_p`-extension;
- `A/K` good ordinary.

No condition `p>2` appears. Therefore the theorem applies literally with

`p=2`, `K=Q_2`,

and `L` the completion at `2` of the cyclotomic `Z_2`-extension used in BSD-001.

Theorem 2 is stated over complete local fields with finite residue field of characteristic `p` and arbitrary `Z_p^d` extensions; again there is no odd-prime restriction.

## Reduction and formal-group exact sequence

Tan writes the reduction sequence for the dual abelian variety as

`0 -> Bhat(O_Kbar) -> B(Kbar) -> Bbar(F_Kbar) -> 0`.

For a `Z_p^d` extension `L/K`, he defines the universal norm of a group `M` by the intersection of the finite-layer norm images as the finite intermediate extensions vary.

Using surjectivity of reduction, Tan records the induced exact norm sequence

`Bhat(O_K)/N_{L/K}(Bhat(O_L))
 -> B(K)/N_{L/K}(B(L))
 -> Bbar(F_K)/N_{L/K}(Bbar(F_L))`.

Theorem 1 proves, in the totally ramified `Z_p` case, that the first arrow is injective. Hence in the present local cyclotomic setting the formal universal-norm obstruction is an actual subgroup of the full universal-norm quotient rather than merely a source for it.

## Explicit formal universal-norm quotient

Let `g=dim A` and let

`u in GL_g(Z_p)`

be Tan's twist matrix describing Frobenius on the reduction `p`-divisible torsion. Theorem 1 gives

`Bhat(O_K)/N_{L/K}(Bhat(O_L))
 ~= Gamma^g/(I-u)Gamma^g`,

where `Gamma=Gal(L/K) ~= Z_p`.

For an elliptic curve, `g=1`, so the formal universal-norm quotient is a one-dimensional finite `Z_2` quotient whenever `1-u` is nonzero.

This source audit does **not** identify Tan's scalar `u` with the protected unit root `alpha` or `alpha^(-1)`. That normalization comparison is a downstream theorem obligation if needed.

## Cohomological exact sequence

For the original abelian variety `A`, Tan records the exact cohomology sequence

`0 -> H^1(Gamma,Ahat(O_L))
   -> H^1(Gamma,A(L))
   -> H^1(Gamma,Abar(F_L))`.

Theorem 2(c) proves that the final reduction map is surjective. Thus for ramified `L/K` this becomes a short exact sequence.

Theorem 2(c) also identifies the reduction cohomology canonically as

`H^1(Gamma,Abar(F_L))
 ~= Hom(Gamma',Abar(F_K))`,

where `Gamma'` is the inertia subgroup. In the totally ramified cyclotomic local extension,

`Gamma'=Gamma`.

## Exact duality of the two sequences

Immediately before Theorem 2, Tan recalls Tate local duality and the exact identification

`H^1(Gamma,A(L))
 ~= (B(K)/N_{L/K}(B(L)))^vee`,

which is the narrower Corollary 2.3.3 interface already protected for WP25.

Tan then states that Theorem 2 makes the cohomology sequence and the universal-norm sequence exact Pontryagin duals of one another.

For ramified `L/K`, he additionally records:

- the formal universal-norm quotient injects into the full universal-norm quotient;
- the reduction universal-norm quotient is naturally the `p`-primary subgroup `Bbar(F_K)_p`;
- the cohomological reduction map is surjective.

Consequently, in the totally ramified good-ordinary case, the universal-norm sequence is the exact Pontryagin dual of

`0 -> H^1(Gamma,Ahat(O_L))
   -> H^1(Gamma,A(L))
   -> Hom(Gamma,Abar(F_K))
   -> 0`.

## Elliptic self-dual specialization at `2`

For an elliptic curve, the principal polarization identifies `A` and `B`. In the BSD-001 local setting, take

`K=Q_2`,

`L=Q_{infty,2}`,

`Gamma=Gamma_2`.

Because the extension is totally ramified, the residue field remains `F_2`.

The selected good-ordinary branch has

`#E_tilde(F_2)=3-a_2 in {2,4}`,

so the full reduction group is already `2`-primary. Therefore Tan's reduction norm quotient specializes to

`E_tilde(F_2)`

itself: at the finite layer of degree `2^n`, the norm on the unchanged residue group is multiplication by `2^n`, and the intersection of those norm images is zero for this finite `2`-group.

Thus the source permits downstream use of an exact sequence of the shape

`0 -> Ehat(2Z_2)/N_infinity(Ehat)
   -> U_2
   -> E_tilde(F_2)
   -> 0`,

where the first term denotes the formal universal-norm quotient in Tan's sense and the middle term is the full local universal-norm quotient already protected in WP25.

The map to the last term is induced by literal reduction. Hence, after downstream concordance of notation and exact protected objects, the image of a point class in the reduction quotient is represented by the reduction of that point.

## Relation to WP27 and required downstream care

This source supplies the missing compatibility theorem that WP27 intentionally does not assert.

Downstream may compare Tan's norm exact sequence with the WP27 dual filtration. However, that comparison must be proved as a map-level identification, not inferred merely because the two end groups have equal orders.

In particular, this audit does not itself prove that WP27's named groups `J_2^vee` and `D_2^vee` are Tan's formal and reduction norm terms under the exact WP27 isomorphisms. The expected comparison is supported by Tan's statement that the norm and cohomology sequences are dual, but MATHSOLVE must bind the maps and notation explicitly.

## What this source does not establish

The source does not establish:

- a splitting of the universal-norm exact sequence;
- the order of the saturated generator's image in either subquotient;
- an explicit formula for the formal universal-norm class of that generator;
- an identification of Tan's twist scalar `u` with `alpha` or `alpha^(-1)` under the protected WP07 normalization;
- a formal logarithm formula for the generator class;
- a p-adic height or Bockstein formula;
- D1a, D1c, or D2;
- the selected BSD equality;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Provider conclusion

Tan supplies a literal-`p=2`, totally ramified, good-ordinary theorem interface that upgrades the abstract local universal-norm quotient to an exact reduction/formal filtration and proves that filtration is Pontryagin-dual to the corresponding local Galois-cohomology exact sequence.

For BSD-001 this is exactly the missing source premise needed to make the first WP27 position coordinate reduction-theoretic and to isolate the remaining unknown in the formal universal-norm subgroup.

**Disposition:** `QUALIFIED_P2_GOOD_ORDINARY_UNIVERSAL_NORM_FILTRATION`.

## Claim firewall

This audit changes no protected claim state. It is source/applicability evidence only.
