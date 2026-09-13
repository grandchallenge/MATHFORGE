# BSD-001 source audit — Cai–Shu–Tian classical Gross–Zagier normalization for WP55

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP55A-CLASSICAL-GZ-WP00-NORMALIZATION`.
- Protected MATHFORGE predecessor: `ed825fe1495c78e1bd62cfea8e747d07e13aedc9`.
- Protected MATHSOLVE predecessor: `9712ced89096a3a7cde6a8630de734423497ac2d`.
- Programme normalization anchor: `grandchallenge/MATH-PROGRAMME@a4eec4259ae6f7e12028cae1384a17ba865926e4`, BSD WP00.
- Primary source: Li Cai, Jie Shu, Ye Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory 8 (2014), no. 10, 2523–2572.
- DOI: `10.2140/ant.2014.8.2523`.
- arXiv: `1408.1733v2`.
- Exact source loci: introductory hypotheses and Theorem 1.1 on arXiv pp. 1–2; local base-change identity in §3.1; Gross–Zagier normalization comparison around Proposition 2.5 and the proof of Theorem 1.5.
- Disposition: `QUALIFIED_EXACT_CLASSICAL_GROSS_ZAGIER_SOURCE`.
- Claim class: source/provider evidence only; no BSD or MATHCERT promotion.

## Source-access and visual verification note

The arXiv v2 PDF was opened as a PDF and its searchable primary-source text was inspected. A page-render screenshot of the page containing Theorem 1.1 was also inspected. The publisher metadata was checked against the Algebra & Number Theory record and DOI.

The current execution environment did not supply an independent byte-download path for recomputing a cryptographic digest of the publisher or arXiv PDF. This admission therefore binds the bibliographic identity, DOI, arXiv version, exact theorem/proof loci, and inspected PDF text/page rendering; it does not claim an independently recomputed external-PDF SHA-256.

## Source setup over Q

The source fixes a normalized weight-two newform

`phi = sum_{n>=1} a_n q^n`

of level `Gamma_0(N)`, an imaginary quadratic field `K` of discriminant `D`, and a primitive ring-class character `chi` of conductor `c`.

The source's Heegner hypotheses are:

1. `(c,N)=1`, no prime dividing `N` is inert in `K`, and every prime `p` with `p^2|N` is split in `K`;
2. `chi([p]) != a_p` for every `p|(N,D)`.

The source defines the Rankin L-series without the archimedean Euler factor and states that the Heegner hypotheses give functional-equation sign `-1`.

## Theorem 1.1 — exact elliptic-curve formula

Let `E/Q` be the elliptic curve associated with `phi`, and let

`f : X_0(N) -> E`

be a modular parametrization sending the cusp at infinity to the identity.

For the source-defined Heegner divisor `P'_chi(f)`, Theorem 1.1 gives exactly

`L'(1,E,chi)
 = 2^{-mu(N,D)}
   * [8*pi^2 (phi,phi)_{Gamma_0(N)} / (u^2 sqrt(|D c^2|))]
   * [hhat_K(P'_chi(f)) / deg(f)]`,

where

- `mu(N,D)` is the number of prime factors of `gcd(N,D)`;
- `u=[O_c^x:Z^x]`;
- `hhat_K` is the Néron–Tate height on `E` **over K**;
- `deg(f)` is the degree of the modular parametrization.

No unspecified multiplicative constant or `2`-adic unit appears in this stated formula.

## Protected selected-lane specialization

Protected MATHSOLVE WP09 supplies an auxiliary imaginary quadratic field `K=Q(sqrt(D))` satisfying:

- `D` fundamental;
- `(D,2N)=1`;
- `2` splits in `K`;
- every prime `ell|N` splits in `K`;
- the twist has `L(E^D,1) != 0`.

For WP55A choose the conductor-one trivial ring-class character:

`c=1`, `chi=1`.

Then the Cai–Shu–Tian hypotheses specialize exactly as follows.

1. `(c,N)=1` is automatic.
2. Every prime dividing `N` is split by protected WP09, so none is inert and the stronger square-level split condition is also satisfied.
3. `(D,N)=1`, so there is no prime `p|(N,D)` and the second Heegner hypothesis is vacuous.
4. `mu(N,D)=0`.
5. `O_c=O_K`, hence

   `u=[O_K^x:Z^x]=[O_K^x:{+1,-1}]=u_K`.
6. `sqrt(|D c^2|)=sqrt(|D_K|)`.

Therefore the exact source formula in the selected lane is

`L'(1,E,1)
 = [8*pi^2 (phi,phi)_{Gamma_0(N)} / (u_K^2 sqrt(|D_K|))]
   * [hhat_K(P_K(f))/deg(f)]`,

where `P_K(f)` denotes the source's conductor-one trivial-character Heegner trace/divisor.

## Base-change L-function interface

In §3.1 the source writes, locally,

`L(s,pi,chi)=L(s,pi_K tensor chi)`,

where `pi_K` is the base-change lifting to `GL_2(K)`.

Thus in the trivial-character conductor-one specialization the finite Rankin Euler product used by Theorem 1.1 is the base-change finite L-function attached to `E/K` in the source normalization. Protected MATHSOLVE WP09 separately supplies the exact factorization used by the campaign:

`L(E/K,s)=L(E,s)L(E^D,s)`.

Since protected WP09 also has `L(E^D,1) != 0` and `ord_{s=1}L(E,s)=1`, downstream MATHSOLVE may combine the admitted classical Gross–Zagier formula with

`L'(E/K,1)=L'(E,1)L(E^D,1)`

only after binding the source's finite-L convention to the protected WP00 finite-L convention. This audit does not silently perform that downstream normalization step.

## Height-normalization warning

Theorem 1.1 explicitly labels `hhat_K` as the Néron–Tate height **over K**.

Later, in the reduction to Yuan–Zhang–Zhang, the source explicitly notes that Cai–Shu–Tian use height over `K` whereas the underlying Yuan–Zhang–Zhang formula uses height over the totally real base field `F`, together with different Haar-measure normalizations.

Therefore no downstream package may identify

`hhat_K(P_K(f))`

with the WP00 regulator `Reg_E` by notation alone. The exact base-field/height convention, the index of `P_K(f)` in the Mordell–Weil lattice, and the relation to the WP00 Néron–Tate pairing must remain explicit until proved.

## Modular-parametrization and differential scalar

Immediately after Theorem 1.1 the source states a BSD comparison as a **conjecture** and defines a positive integer `C` by

`f^* omega_0 = +/- C * 2*pi*i*phi(z) dz`

for a Néron differential `omega_0` on `E`.

This definition is useful normalization data, but the subsequent BSD comparison is not admitted as a theorem. In particular this audit does not set `C=1`, does not assume `E` is the optimal curve in its isogeny class, and does not suppress modular-degree or Manin-type factors.

## Exact downstream interface admitted after protection

MATHSOLVE may use the following bounded source statements.

1. Cai–Shu–Tian Theorem 1.1 with all displayed constants exactly as above.
2. In the protected `c=1`, `chi=1`, all-`N`-split, `(D,N)=1` lane, the source hypotheses hold and `mu(N,D)=0`, so the exact selected-lane formula is

   `L'(1,E,1)
    = [8*pi^2 (phi,phi)/(u_K^2 sqrt(|D_K|))]
      * [hhat_K(P_K(f))/deg(f)]`.
3. The source's Rankin local L-factor is the base-change L-factor `L(s,pi_K tensor chi)`; protected WP09 may be used separately for the campaign's exact factorization over `Q`.
4. The source's height is a Néron–Tate height over `K`; its conversion to the WP00 regulator is a distinct downstream obligation.
5. The differential pullback scalar `C` may be retained exactly through the source definition, but no theorem in this admission sets it to one.

## Remaining unsupported comparisons

This source admission does **not** prove any of the following:

- equality of the source's Néron–Tate height over `K` with the protected WP00 regulator;
- the exact Mordell–Weil index of the source Heegner point relative to a WP00 generator;
- exact compatibility between the source's classical Heegner point/test vector and Disegni's protected ordinary p-adic Heegner class/test vectors;
- any equality between real and p-adic heights;
- any cancellation of `u_K`, `h_K`, `sqrt(|D_K|)`, bad-prime factors, modular degree, Manin scalar, periods, regulators, Tamagawa factors, Euler factors, or WP54A `Q^ord` factors;
- a rank-zero BSD formula for the twist `E^D`;
- fixed-`2` height nondegeneracy;
- the height-one `(2)` analytic determinant generator;
- exact WP06 quadratic descent of the analytic normalization;
- `BSD-R2-A1`;
- MATHCERT certification, theorem novelty, or priority.

## Provider disposition

`QUALIFIED_EXACT_CLASSICAL_GROSS_ZAGIER_SOURCE`

The source is admitted only for the bounded exact classical derivative/Heegner-height interface and its selected-lane specialization above. The next downstream operation must construct the explicit scalar ledger to the protected WP00 quantity and retain every unresolved scalar rather than replacing it by “up to a unit”.
