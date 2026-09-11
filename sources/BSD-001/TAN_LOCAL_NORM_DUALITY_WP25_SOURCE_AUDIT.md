# BSD-001 source audit — Tan local Galois cohomology / universal-norm duality

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP25-LOCAL-UNIVERSAL-NORM-REPRESENTATION`.
- Protected Forge baseline: `ade028d30e1dc3328a2270dcf6108064a6a8c8d0`.
- Downstream protected MATHSOLVE baseline: `eac82bf2809ff70317a3542a58247e6a11299bc0`.
- Primary source: Ki-Seng Tan, *A generalized Mazur's theorem and its applications*, Transactions of the American Mathematical Society 362 (2010), no. 8, 4433–4450, DOI `10.1090/S0002-9947-10-05042-7`.
- Exact source interface: §2.3, Theorem 6, Lemma 2.3.2, Corollary 2.3.3.
- Full-text identity inspected: author-uploaded published article carrying the AMS volume/page/DOI metadata.
- Disposition: `QUALIFIED_LOCAL_GALOIS_COHOMOLOGY_NORM_DUALITY`.
- Claim class: source/applicability admission only; no BSD or MATHCERT promotion.

## Exact downstream query

Protected MATHSOLVE WP24 defines a basis-independent finite character image

`rho_E := len_Z2 im(chi_P|K_loc)`

for a saturated rank-one Mordell-Weil generator `P`. Protected WP21–WP23 identify each ambient local factor by

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

The WP25 source question is therefore exact:

> Is the local Galois cohomology group `H^1(Gal(L/K),A(L))` canonically Pontryagin-dual, through the same local Tate pairing used in WP24, to the exact norm quotient of the dual abelian variety, including infinite Galois extensions and without an odd-prime restriction?

## Theorem 6 — local Tate duality

Tan §2.3 defines the local pairing from the Poincare biextension and the invariant map of the local Brauer group. Theorem 6 states that for an abelian variety `A/K` and its dual `B/K`,

`H^1(K,A)`

with its discrete topology and

`B(K)`

with its compact topology are Pontryagin dual under this local pairing.

This theorem is a characteristic-zero local duality statement in the number-field local situations used by BSD-001. It is not an ordinary-reduction theorem and does not impose an odd auxiliary prime.

## Lemma 2.3.2 — restriction and norm are adjoint

For a finite Galois extension `L/K`, Tan records the exact compatibility

`<res(xi), Q>_L = <xi, N_{L/K}(Q)>_K`.

The proof uses compatibility of local invariants with corestriction and the Galois equivariance of the local pairing.

Thus the annihilator of the kernel of local restriction is exactly the local norm subgroup on the dual abelian variety. No `p`-adic unit ambiguity occurs in this statement.

## Corollary 2.3.3 — exact norm-duality interface

Tan then states:

For **any Galois extension** `L/K`, the discrete group

`H^1(Gal(L/K),A(L))`

and the compact group denoted

`B(K)/N_{L/K}(B(L))`

are Pontryagin dual through the local pairing.

For an infinite Galois extension, the source defines the latter compact group as the projective limit

`lim_F B(K)/N_{F/K}B(F)`,

where `F` runs through the finite intermediate Galois extensions. The cohomology group is the corresponding direct limit

`colim_F H^1(Gal(F/K),A(F))`.

The proof reduces to finite `F/K`: inflation-restriction identifies the local Galois cohomology group with the kernel of

`H^1(K,A) -> H^1(F,A)`,

and Lemma 2.3.2 plus local Tate duality identifies its exact annihilator with `N_{F/K}B(F)`.

This is precisely the finite/infinite norm-duality interface needed by WP25.

## Prime range and the selected `p=2` use

The corollary itself is not an odd-prime theorem. Its statement is for a Galois extension of local fields, and its proof uses only local Tate duality, restriction/corestriction, and norm adjointness.

This matters in two distinct BSD-001 local situations:

1. at the good-ordinary place `v=2`, take `K=Q_2` and the local cyclotomic `Z_2`-extension;
2. at an odd bad prime `ell`, take `K=Q_ell` and the local completion of the global cyclotomic `Z_2`-extension, which protected WP22 proves is an unramified `Z_2`-extension.

Although the broader paper often uses the letter `p` for the residue characteristic in its ordinary-reduction applications, Corollary 2.3.3 does not require the Galois extension to be a `Z_p`-extension for that residue prime. Its proof applies to arbitrary Galois `L/K`. Therefore using a pro-`2` extension of `Q_ell` for odd `ell` is within the literal corollary rather than a specialization of an ordinary `p=ell` theorem.

No statement in this admitted interface requires `2` to be invertible or assumes `p>2`.

## Elliptic self-dual specialization

For an elliptic curve `E`, the canonical principal polarization identifies the dual abelian variety with `E`. Therefore Tan's interface gives, for every selected local cyclotomic extension `F_infty/F`,

`H^1(Gal(F_infty/F),E(F_infty))^vee
 ~= lim_n E(F)/N_{F_n/F}E(F_n)`.

The right side is the source-defined projective-limit norm quotient. This audit does **not** yet replace that projective limit by

`E(F)/(intersection_n N_{F_n/F}E(F_n))`.

That replacement is a downstream theorem obligation. Protected WP22–WP23 finiteness is expected to imply eventual stabilization of the nested finite-layer norm quotients, but that deduction belongs to MATHSOLVE.

## Compatibility with the WP24 character

WP24's character is defined using the same product local Tate pairing:

`chi_P(z)=<z,loc(t_P)>_loc`.

Under Tan's local duality, evaluation of the `v`-component against the local compact Kummer class of `P` is therefore evaluation against the corresponding class of `P` in the local projective-limit norm quotient.

This audit admits that pairing compatibility. It does not determine the order of the class of `P` in any local norm quotient.

## Provider conclusion

Tan Corollary 2.3.3 supplies the exact local theorem interface required for WP25:

`local control cohomology  <->  exact projective-limit norm quotient`,

with finite-layer restriction/norm adjointness and arbitrary Galois extensions built into the source statement.

It applies literally to the selected `Z_2` local cyclotomic extensions, both at `2` and at odd primes.

**Disposition:** `QUALIFIED_LOCAL_GALOIS_COHOMOLOGY_NORM_DUALITY`.

## Claim firewall

This audit does not establish:

- stabilization of the finite-layer norm subgroups;
- an ordinary quotient by the intersection of norm images before such stabilization is proved;
- the order of the saturated generator in any local norm quotient;
- a value of `rho_E`;
- an equality of `rho_E` with a regulator, height, Bockstein scalar, or analytic factor;
- D1a, D1c, or D2;
- the selected exact BSD equality;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
