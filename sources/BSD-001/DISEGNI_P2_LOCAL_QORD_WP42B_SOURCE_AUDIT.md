# BSD-001 source audit — exact split-`2` ordinary local toric factor in Disegni

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP42B-DISEGNI-P2-LOCAL-QORD`.
- Protected MATHFORGE predecessor: `ab5e1c4d429bb36cce9927e62bcee5279870dec7`.
- Protected MATHSOLVE predecessor: `3463858d6281bcc2030d11f7f9af76c9f9097ff9`.
- Primary source: Daniel Disegni, *The universal p-adic Gross–Zagier formula*, Invent. Math. 230 (2022), 509–649, author PDF `https://disegni-daniel.perso.math.cnrs.fr/univ.pdf`.
- Exact source loci: Appendix A.1, equation (A.1.2); Appendix A.3, Definition/Equation (A.3.3), Proposition A.3.4 and its proof, especially the split case.
- Disposition: `QUALIFIED_EXACT_SPLIT_P_ORDINARY_LOCAL_FACTOR`.
- Claim class: source/local-normalization admission only; no global `Q^ord`, BSD, or certification promotion.

## Source lock

The public author PDF was inspected through its searchable text layer and the relevant Appendix A.3 pages were also rendered successfully as page images. The page containing (A.3.3) and Proposition A.3.4 displays the defining formula, and the following page displays the proof normalization and split-case calculation. This audit binds the public PDF identity and exact equation/proposition locators. It does not claim an independently recomputed byte digest.

## Downstream question

Protected MATHFORGE WP41B and protected MATHSOLVE WP41 reduce the selected p-adic Gross–Zagier normalization to the ordinary factor

`Q^ord`.

Disegni Lemma 4.3.3 decomposes that global factor into local terms. The first local question is:

> At the selected prime `p=2`, where the protected auxiliary quadratic field is split and the elliptic curve has good ordinary reduction, what is the exact source-normalized ordinary local toric factor for the canonical ordinary vectors?

This audit addresses only that local factor.

## Source definition of the ordinary local factor

Appendix A.3.3 defines, for a refined local representation `Pi=pi tensor chi`, a local measure `dt`, and ordinary vectors,

`Q^ord_dt((f1 tensor f2)/(f3 tensor f4))`

` := mu^+(j_v) * vol^circ(H'_v,dt) * (f1 tensor f2)/(f3 tensor f4)`,                 `(A.3.3)`

where

`mu^+ = chi_v * (alpha |.|) o N_{E_v/F_v}`

is the character acting on the positive ordinary line.

Appendix A.1, equation (A.1.2), specifies in the split case

`j_v=(-1_w,1_{w^c})`.

Therefore

`N_{E_v/F_v}(j_v)=-1`.

## Canonical vector and measure normalization

In the proof of Proposition A.3.4, Disegni chooses the local measure

`dt = |D_v|^{-1/2} d^x_{psi_E} z / d^x_psi y`

and states explicitly that this gives

`vol^circ(H'_v,dt)=1`.

He also takes

`f1=f3=f_pi`,

`f2=f4=f_pi^vee`,

with the canonical ordinary Kirillov vectors of (A.3.1). For these vectors the ratio appearing in (A.3.3) is exactly one.

Hence under this source normalization,

`Q^ord_{v,dt}(canonical ratio)=mu^+(j_v)`.                         `(L)`

## Split place with trivial character and unramified refinement

Assume now:

1. `E_v/F_v` is split;
2. `chi_v=1`;
3. the refinement character `alpha:F_v^x -> L^x` is unramified.

Because `j_v=(-1,1)`, one has `N(j_v)=-1`. Since an unramified character is trivial on `O_{F_v}^x`,

`alpha(-1)=1`.

Also `|-1|_v=1`, and the trivial `chi_v` contributes one. Therefore

`mu^+(j_v)=1`.

Substituting into `(L)` gives the exact identity

`Q^ord_{v,dt}(canonical ratio)=1`.                               `(P2-local)`

No unit ambiguity appears in this equality.

## Applicability to the protected selected prime `2`

The source statement above is conditional on the three local hypotheses. Downstream protected campaign data supply them at the selected place:

- protected WP09 chooses `K/Q` with `2` split;
- the selected Hecke character is trivial;
- the selected elliptic curve has good reduction at `2`, so `2` does not divide its conductor and its local automorphic representation is unramified; the ordinary refinement is the unramified refinement associated with the protected unit root.

Thus MATHSOLVE may specialize `(P2-local)` to the selected `v=2` lane.

## Measure-scaling firewall

The equality `(P2-local)` is tied to Disegni's local measure normalization used in Proposition A.3.4, for which `vol^circ=1`.

A global factorization of `Q^ord` uses a decomposed adelic measure. If a different local scalar multiple of `dt_2` is chosen as part of that global decomposition, the local factor scales accordingly and the compensating scalar must be retained elsewhere in the global measure ledger.

Therefore this audit admits:

`Q^ord_{2,dt_2^can}=1`

for the canonical source-normalized local measure and vectors.

It does **not** admit a measure-independent statement that the `2`-component of every decomposition equals one.

## Exact downstream interface

After protection, MATHSOLVE may use:

1. For the selected split `p=2`, trivial-character, good-ordinary unramified refinement and Disegni's canonical Appendix-A.3 measure/vectors,

   `Q^ord_{2,dt_2^can}=1`.

2. Consequently,

   `ord_2(Q^ord_{2,dt_2^can})=0`.

3. Any rescaling needed to match a chosen global adelic measure must be recorded as a separate explicit measure factor and may not be discarded.

## Refined D2c consequence

The selected good-ordinary `2`-adic ordinary toric factor is closed in canonical local normalization. The remaining D2c valuation debt lies in:

- global/local measure reconciliation;
- split bad primes `ell|N`;
- any auxiliary finite places in Disegni's `Sigma` and `Sigma'`;
- the remaining vector and local-L normalization terms;
- the archimedean/global normalization where it enters `Q^ord`.

No statement about their valuations is admitted here.

## Claim firewall

This audit does not prove:

- global `Q^ord=1` or `ord_2(Q^ord)=0`;
- that an arbitrary local measure at `2` gives factor one;
- that bad-prime or global measure factors are units;
- equality of this local factor with a Tamagawa, Bockstein, regulator, or WP00 term;
- fixed-`2` height nondegeneracy;
- an analytic determinant generator at height one `(2)`;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.