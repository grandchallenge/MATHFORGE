# BSD-001 source audit — Greenberg primitive good-ordinary local control at `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP23-GOOD-ORDINARY-P2-LOCAL-CONTROL`.
- Protected Forge baseline: `5acfbb327552e8608ab5c3ff3278d7ca45b39879`.
- Downstream protected MATHSOLVE baseline: `4a649ace4e513871c84c6fbe11c2a16885fcc386`.
- Primary source: Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:`math/9809206`, submitted 18 September 1998; published in *Arithmetic Theory of Elliptic Curves* (Cetraro, 1997), Lecture Notes in Mathematics 1716, Springer, 1999, pp. 51–144, DOI `10.1007/BFb0093453`.
- Primary-source identity used for theorem text: arXiv `math/9809206v1`.
- Source sections audited: §2, especially Propositions 2.2, 2.4, 2.5; §3, especially the definition of `H_E(M_eta)` and Lemma 3.4.
- Disposition: `QUALIFIED_P2_PRIMITIVE_GOOD_ORDINARY_LOCAL_CONTROL`.
- Claim class: source/applicability admission only; no BSD or MATHCERT promotion.

## Exact downstream query

Protected MATHSOLVE WP21 defines, for the cyclotomic `Z_2`-extension and the primitive classical-Kummer local condition,

`K_v := H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`

as the ambient kernel of the local restriction map on the primitive Kummer quotient. Protected WP22 computes every odd-prime `K_ell`. The remaining local obligation is

`MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`.

The source question is therefore exact and narrow:

> Does Greenberg's local control calculation literally include `p=2`, use the classical Kummer quotient rather than an assumed Greenberg replacement, and compute the order of the base-level good-ordinary local restriction kernel at `2`?

## Prime range

The source begins with a cyclotomic `Z_p`-extension for `p` **any prime**. Section 2 fixes a prime `p` and defines the classical Kummer map

`kappa_M : E(M) tensor (Q_p/Z_p) -> H^1(M,E[p^infinity])`

and the classical `p`-primary Selmer local quotient

`H^1(M_eta,E[p^infinity]) / Im(kappa_eta)`.

The source does not impose `p>2` in the statements of Propositions 2.2, 2.4, 2.5, or Lemma 3.4. Its proof of the local cohomology input explicitly treats the `p=2` case and later states that the duality argument used there works at `p=2`. The paper also treats `p=2` separately in the nearby nonsplit multiplicative case, confirming that `p=2` is not silently excluded from the local section.

Accordingly, no odd-prime specialization is required for the good-ordinary local theorem admitted here.

## Classical Kummer condition is literal

Greenberg defines

`H_E(M_eta) := H^1(M_eta,E[p^infinity]) / Im(kappa_eta)`

in §3, where `kappa_eta` is the classical local Kummer homomorphism defined in §2.

Thus the local object in Lemma 3.4 is the primitive classical-Kummer quotient itself. It is not defined by first replacing the Kummer image with the ordinary connected-etale/Greenberg image.

This distinction is decisive for BSD-001 because protected WP06/WP07 prohibit identifying finite-level Kummer and Greenberg local conditions at `2` without proof.

## Finite-level Kummer-versus-ordinary discrepancy

For good ordinary reduction at a prime `v|p`, Greenberg defines the connected ordinary subgroup

`C_v = ker(E[p^infinity] -> E_tilde[p^infinity])`

and the induced map

`lambda_eta : H^1(M_eta,C_v) -> H^1(M_eta,E[p^infinity])`.

Proposition 2.2 identifies the classical finite-level Kummer image with the maximal divisible subgroup of `Im(lambda_eta)`.

Proposition 2.5 strengthens this to the exact finite quotient

`Im(lambda_eta) / Im(kappa_eta) ~= E_tilde(m_eta)_p`,

where `m_eta` is the residue field and the subscript `p` denotes the `p`-primary subgroup.

Therefore the finite-level Kummer/ordinary discrepancy is not discarded as a unit. Its exact `p`-power order is retained.

## Infinite cyclotomic level

Proposition 2.4 applies to a Galois local extension whose Galois group contains an infinite pro-`p` subgroup and whose inertia subgroup has finite index. Greenberg immediately notes that a completion of the cyclotomic `Z_p`-extension at a prime above `p` satisfies these hypotheses.

At that infinite level the theorem gives

`Im(kappa_infty) = Im(lambda_infty)`.

Hence the finite-level discrepancy of Proposition 2.5 is precisely one component of the finite-to-infinite primitive local control kernel; it is not present at infinite level.

## Lemma 3.4 — exact local restriction-kernel order

Greenberg defines, for a prime `v` of the base field and a prime `v_n` above it,

`r_{v_n}: H_E((F_n)_{v_n}) -> H_E((F_infty)_eta)`.

Lemma 3.4 states for good ordinary reduction at `v|p` that

`#ker(r_{v_n}) = #E_tilde(f_{v_n})_p^2`.

The proof factors the kernel into two exact pieces:

1. the finite Kummer-versus-connected-ordinary image quotient, of order `#E_tilde(f_{v_n})_p` by Proposition 2.5;
2. the restriction kernel on the connected-ordinary quotient, again of the same order, computed by inflation-restriction on the finite residue-field `p`-primary subgroup.

This is an exact order formula, not a boundedness-only conclusion.

## Concordance with protected WP21

Protected WP21 works with the local quotient arising from the classical Kummer exact sequence and identifies its finite-to-cyclotomic restriction kernel with

`H^1(Gamma_v,E(F_infty,w))[p^infinity]`.

Greenberg's `H_E(M_eta)` is the same classical Kummer quotient. Therefore, after setting `F=Q`, `p=2`, `n=0`, `v=2`, the source's `ker(r_v)` is the same ambient primitive local restriction kernel denoted `K_2` in WP21.

No equality between finite Kummer and Greenberg local conditions is being assumed in making this identification; Greenberg's proof explicitly measures their finite discrepancy before passing to the infinite level.

## Specialization to the selected BSD branch

For the cyclotomic `Z_2`-extension of `Q`, the prime `2` is totally ramified, so the residue field at every finite layer remains `F_2`. Thus Lemma 3.4 at the base layer gives

`#K_2 = #E_tilde(F_2)[2^infinity]^2`.

Protected MATHSOLVE WP07 proves for the selected good-ordinary branch that

`a_2 in {+1,-1}`

and

`#E_tilde(F_2)=3-a_2 in {2,4}`.

Hence the full reduction group is already 2-primary and the source interface yields

`#K_2 = (3-a_2)^2`,

so

`len_Z2(K_2^vee) = 2 ord_2(3-a_2)`.

This equals `2` when `a_2=+1` and `4` when `a_2=-1`.

Protected WP07 independently proves

`ord_2(1-alpha^(-1)) = ord_2(3-a_2)`

for the 2-adic unit root `alpha`. Consequently the above local-control length numerically equals the valuation of the normalization-specific squared factor `(1-alpha^(-1))^2` whenever that factor is present. This audit does **not** assert that any particular analytic determinant uses that normalization; that remains a separately source-bound D1c question.

## Applicability exclusions and non-results

This admitted theorem interface does not require:

- residual `p`-distinguishedness;
- a main conjecture;
- a `p`-adic Gross-Zagier theorem;
- Kato's all-height-one integral divisibility;
- a global localization-surjectivity statement;
- equality of the globally hit subgroup `C_E` with the full ambient local product.

It does not compute the WP21 global-hit subgroup

`C_E = im(loc_Q) intersect K_loc`.

It therefore closes only the ambient place-2 local-kernel input, not the whole D1b control defect.

## Provider conclusion

Greenberg's primary-source local control theorem is admissible at `p=2` for the selected good-ordinary branch and uses the exact primitive classical-Kummer quotient required by WP21. At base level over `Q_2` it supplies the exact ambient local-kernel order

`#K_2 = (3-a_2)^2`.

**Disposition:** `QUALIFIED_P2_PRIMITIVE_GOOD_ORDINARY_LOCAL_CONTROL`.

The next substantive mathematical boundary after downstream composition is

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

## Claim firewall

This audit does not establish:

- `C_E = K_2 x K_bad`;
- surjectivity of global localization onto any ambient local kernel;
- a primitive cyclotomic perfect determinant realization;
- the analytic determinant generator at height one `(2)`;
- the WP20 Bockstein/WP00 normalization;
- the full selected-family BSD equality;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
