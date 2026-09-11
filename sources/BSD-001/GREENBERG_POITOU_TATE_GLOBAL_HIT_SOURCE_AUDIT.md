# BSD-001 source audit — Greenberg Poitou-Tate/Cassels global-local incidence at `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP24-GLOBAL-HIT-POITOU-TATE-CHARACTER`.
- Protected Forge baseline: `e6f025896532021a84edf05b54034edc9834a022`.
- Downstream protected MATHSOLVE baseline: `e27d53e0e1198da5c335e66be3d3ceea2e94acf8`.
- Primary source: Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:`math/9809206v1`, §§3–4, especially the general Cassels/Poitou-Tate discussion immediately preceding Proposition 4.13 and the elliptic specialization following it.
- Disposition: `QUALIFIED_P2_PRIMITIVE_POITOU_TATE_GLOBAL_LOCAL_INCIDENCE`.
- Claim class: source/applicability admission only; no BSD or MATHCERT promotion.

## Exact downstream query

Protected WP23 closes every ambient local-control calculation. The actual primitive specialization defect remains

`C_E := im(loc_Q) intersect K_loc`,

with `K_loc` now a finite explicitly measured subgroup of the primitive local quotient target.

The downstream question is therefore not whether the ambient kernels are known. It is:

> Which elements of the finite ambient kernel are hit by global cohomology, and can that incidence be represented exactly by Poitou-Tate duality against the rank-one compact self-dual Selmer direction?

The source interface required is narrower than a main conjecture or control theorem. It is the exact orthogonality statement for global images and the exact dual description of the cokernel of primitive global localization.

## Prime range

Greenberg's paper fixes `p` as any prime in its cyclotomic setup. The general Cassels/Poitou-Tate construction in §4 is stated for a discrete module

`M ~= (Q_p/Z_p)^d`

and its dual lattice

`T^* := Hom(M,mu_{p^infinity})`.

The statements used here do not impose `p` odd. In particular, the discussion giving the perfect local pairing, global orthogonal-complement relation, and exact cokernel duality appears before Proposition 4.13 without an odd-prime restriction. The later elliptic specialization takes

`M=E[p^infinity]`,

`T^*=T_p(E)`

by the Weil pairing, again without adding `p>2`.

Accordingly this source interface is admissible literally at `p=2`; it is not an odd-prime theorem being specialized.

## General local conditions and local duality

Let `Sigma` contain the primes above `p`, the archimedean primes, and all primes needed for the ramification of `M`. For each `v in Sigma`, Greenberg takes a divisible subgroup

`L_v subset H^1(F_v,M)`

and defines the Selmer group

`S_M(F) = ker(H^1(F_Sigma/F,M)
              -> product_v H^1(F_v,M)/L_v)`.

He defines

`T^* := Hom(M,mu_{p^infinity})`

and lets

`U_v^* subset H^1(F_v,T^*)`

be the orthogonal complement of `L_v` under the perfect local Tate pairing

`H^1(F_v,M) x H^1(F_v,T^*) -> Q_p/Z_p`.

Thus the product local conditions

`L := product_v L_v`,

`U^* := product_v U_v^*`

are exact orthogonal complements in the product of local cohomology groups.

## Global orthogonality

Let

`G := im(H^1(F_Sigma/F,M) -> P)`,

`G^* := im(H^1(F_Sigma/F,T^*) -> P^*)`,

where `P` and `P^*` are the corresponding local products.

Greenberg states, as the Poitou-Tate input, that

`G` and `G^*`

are orthogonal complements under the product of local Tate pairings.

For the global-to-local quotient map

`gamma : H^1(F_Sigma/F,M) -> P/L`,

its cokernel is

`P/(G L)`.

Taking orthogonal complements therefore gives the exact Pontryagin-dual identification

`coker(gamma)^vee ~= G^* intersect U^*`.

This is the source statement needed downstream. It is exact; it is not merely a corank bound.

## Compact dual Selmer interpretation

Greenberg defines the compact Selmer module

`S_{T^*}(F)
 = ker(H^1(F_Sigma/F,T^*)
       -> product_v H^1(F_v,T^*)/U_v^*)`.

By definition, its localization image is exactly

`G^* intersect U^*`.

Consequently the exact source interface may be written as

`coker(gamma)^vee
 ~= im(S_{T^*}(F) -> P^*)`.

Greenberg separately notes that the rank of `S_{T^*}(F)` equals the corank of the corresponding discrete dual Selmer group, but no finiteness of the discrete Selmer group is required for the exact image/cokernel identity above.

This distinction matters for BSD-001 because the protected selected class has Mordell-Weil rank one, so its primitive discrete `2`-primary Selmer group is not finite.

## Elliptic classical-Kummer specialization

Greenberg explicitly records the classical elliptic specialization:

- `M=E[p^infinity]`;
- `L_v=Im(kappa_v)` for the classical Kummer maps;
- `T^*=T_p(E)` by the Weil pairing;
- the dual local condition is again the classical Kummer/self-dual elliptic condition.

Therefore at `p=2` the quotient target

`H^1(Q_v,E[2^infinity])/Im(kappa_v)`

is the same primitive classical-Kummer quotient used by protected MATHSOLVE WP21–WP23.

The source does not replace the Kummer condition at `2` by a Greenberg ordinary condition.

## What the source does and does not supply in rank one

The source supplies the exact general identity

`coker(gamma)^vee
 ~= im(S_{T_2(E)}(Q) -> P^*)`

for the primitive self-dual Kummer structure.

It does **not**, by itself, identify the compact Selmer module with `E(Q) tensor Z_2`. That downstream identification must be proved from the protected finite-level Kummer exact sequences and finiteness of `Sha(E/Q)`.

It also does not, by itself, prove localization injectivity for that compact Selmer module. Downstream may prove this by identifying the kernel with the `2`-adic Tate module of the finite `Sha`, hence zero.

Finally, it does not evaluate the resulting character on `K_loc`; it only gives the exact duality framework in which that evaluation is the sole global-local incidence datum.

## Qualified downstream composition

Subject to the protected internal facts

- `rank E(Q)=1`;
- `#E(Q)_tors` is odd;
- `Sha(E/Q)` is finite;
- the compact primitive self-dual Selmer module has no residual `T_2 Sha` term;

this source permits downstream construction of a saturated generator

`t_P in S_{T_2(E)}(Q) ~= Z_2`

and a character on the primitive local quotient

`chi_P(z) := <z,loc(t_P)>_loc in Q_2/Z_2`.

Because the source identifies the global localization image as the annihilator of the localized compact Selmer image, the expected downstream consequence is

`im(gamma) = ker(chi_P)`

on the primitive local quotient, and hence

`C_E = K_loc intersect im(gamma)
     = ker(chi_P|K_loc)`.

This final specialization is a downstream theorem obligation, not a source-audit promotion.

## Provider conclusion

Greenberg's general Cassels/Poitou-Tate framework provides a literal `p=2`, classical-Kummer, self-dual elliptic source interface for the exact global-local incidence problem. Its exact content is the orthogonality of global images and

`coker(gamma)^vee ~= G^* intersect U^*`.

It does not require the rank-one discrete Selmer group to be finite and therefore is suitable for the selected BSD branch.

**Disposition:** `QUALIFIED_P2_PRIMITIVE_POITOU_TATE_GLOBAL_LOCAL_INCIDENCE`.

## Claim firewall

This audit does not establish:

- `C_E=K_loc`;
- a value for the image order of the rank-one character on `K_loc`;
- a regulator or height formula for that image order;
- a primitive cyclotomic perfect determinant realization;
- an analytic determinant generator at height one `(2)`;
- the WP20 Bockstein/WP00 normalization;
- the selected exact BSD equality;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
