# BSD-001 source audit — Disegni/Cai–Shu–Tian global-measure and auxiliary-place `Q^ord` data

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP54A-GLOBAL-QORD-RECONCILIATION`.
- Protected MATHFORGE predecessor: `c1aaf027df8e03fd79783cfc8ed14c9d58632a50`.
- Protected MATHSOLVE predecessor: `c0ef44b5dca27ccb5823d1e6667899c6777db93d`.
- Primary source 1: Daniel Disegni, *The universal p-adic Gross–Zagier formula*, Invent. Math. 230 (2022), 509–649; author PDF `https://disegni-daniel.perso.math.cnrs.fr/univ.pdf`.
- Exact Disegni loci: (1.2.5), (1.2.7)–(1.2.9), Remark 1.2.2, Lemma 4.2.1, (4.3.1)–(4.3.4), Appendix A.3 equation (A.3.3) and Proposition A.3.4, Appendix A.4 equations (A.4.3)–(A.4.4).
- Primary source 2: Li Cai, Jie Shu, Ye Tian, *Explicit Gross-Zagier and Waldspurger formulae*, Algebra Number Theory 8 (2014), no. 10, 2523–2572, arXiv:1408.1733.
- Exact CST loci: §2 measure normalization, §3.1 notation and Lemma 3.1, Proposition 3.12 and its proof.
- Disposition: `QUALIFIED_EXACT_GLOBAL_MEASURE_AND_AUXILIARY_QORD_INPUTS`.
- Claim class: source/local-normalization admission only; no class-number identity, global `Q^ord` theorem, BSD, or certification promotion.

## Source-lock note

Both primary PDFs were inspected at the exact formula loci through searchable primary-source text. The CST page containing the §2 measure normalization was also rendered as a page image during this audit. Disegni's relevant Appendix-A source had already been rendered and source-locked by the protected WP42B audit; the present audit rechecks the exact textual loci needed for WP54A. No independently recomputed PDF digest is claimed.

## Downstream question

Protected WP42B fixes the selected split-`2` ordinary factor under Disegni's canonical Appendix-A.3 measure. Protected WP53A fixes the exact odd split semistable bad-prime factor under the CST local quotient measure. WP54A must now choose one legal global decomposition of Disegni's volume-one torus measure and evaluate every remaining finite, `2`, and archimedean term without hiding the compensating scalar.

This audit admits only the source facts needed for that reconciliation.

## 1. Disegni's global and local measure rules

Disegni (1.2.9) fixes local measures `dt_v` whose adelic product has

`vol(H'(Q)\\H'(A), dt)=1`.

Equation (1.2.8) and Remark 1.2.2 state that, when all local data are unramified, the normalized local toric ratio on the spherical lines equals

`vol(O_E,v^x/O_F,v^x,dt_v)`.

At `p` and infinity, (4.3.1) defines the modified ordinary volumes

`vol^circ(H'_v,dt_v)
 = vol(O_E,v^x/O_F,v^x,dt_v)/(e_v L(1,eta_v)^(-1))`,

and, for an archimedean place,

`vol^circ(H'_{v,infinity},dt_{v,infinity})
 = 2^{-[F_v:Q]} vol(H'_{v,infinity},dt_{v,infinity})`.

Equation (A.4.4) gives the archimedean ordinary term as

`Q^ord_{infinity,dt}
 = mu^+(j_infinity) * vol^circ(H'_infinity,dt) * vector_ratio`.

For the protected trivial-weight, trivial-character lane over `F=Q`, the protected WP41B/WP42B specialization has `mu^+(j)=1`; taking identical numerator/denominator source-compatible vectors makes the vector ratio exactly one. Hence downstream may specialize

`Q^ord_{infinity,dt_infinity}
 = (1/2) vol(H'_infinity,dt_infinity)`.

This is an exact source-normalized formula, not an equality up to a unit.

## 2. CST local quotient measures

CST §2 choose a global additive character, self-dual additive measures, the induced multiplicative measures, and quotient measures on `K_v^x/F_v^x`. Their product torus measure satisfies

`Vol(K^x\\K_A^x/A_F^x)=2 L(1,eta)`.

In §3.1 CST use those same local measures. For a nonarchimedean `F`, with base-field different generator `delta` and relative quadratic discriminant generator `D`, they state

`Vol(K^x/F^x) = |delta|^(1/2)`

when `K/F` is the unramified quadratic field extension, and

`Vol(K^x/F^x) = 2 |D delta|^(1/2)`

when `K/F` is ramified.

For `F=Q_ell`, `|delta|=1`.

Consequently, with the CST quotient measure:

1. if `K_ell/Q_ell` is unramified nonsplit, the valuation quotient is trivial and

   `m_ell := vol(O_K,ell^x/Z_ell^x)=1`;

2. if `K_ell/Q_ell` is ramified, the valuation quotient has two cosets, so

   `m_ell = |D_ell|^(1/2)`;

3. if `K_ell ~= Q_ell direct_sum Q_ell` is split, the quotient identifies with `Q_ell^x`; CST's multiplicative normalization has `vol(Z_ell^x)=1`, hence

   `m_ell=1`.

The second and third bullets are elementary consequences of CST's explicitly defined quotient measure; no class-number formula is used here.

## 3. Good auxiliary places: exact CST toric factors

CST Proposition 3.12 states that for a nonarchimedean local field and a nonzero vector in the one-dimensional test-vector line,

`beta(f) |D delta|^(-1/2)=1`

when the GL2 conductor exponent and toric-character conductor satisfy

`n=c=0`.

Therefore over `Q_ell`:

- for an unramified nonsplit quadratic extension, `beta_ell=1`;
- for a ramified quadratic extension, `beta_ell=|D_ell|^(1/2)`;
- on the split unramified lane, `beta_ell=1`.

Protected WP53 already admits that Disegni's finite-place `Q_{ell,dt}` equals CST's normalized `beta` when the same Haar measure and source-compatible vector line are used. Thus, under the CST measure,

`Q_{ell,dt_ell^CST}=m_ell`

at every selected finite place with `ell not| N` and `ell != 2`.

In particular, for every `ell|D_K`, since protected WP09 has `(D_K,2N)=1`, the automorphic representation is unramified and `chi=1`, so

`Q_{ell,dt_ell^CST}=ell^(-1/2)`

when the local discriminant exponent is one; more invariantly the factor is `|D_ell|^(1/2)`. The product over all discriminant primes is exactly `|D_K|^(-1/2)` for a quadratic fundamental discriminant.

No assertion is made here that this factor is a `2`-adic unit; its role must be combined with the global measure ledger downstream.

## 4. Finite quaternion ramification vanishes in the selected lane

Disegni's locally distinguished datum uses the unique local quaternion choice satisfying the source sign condition (1.2.5). CST §3.1 gives an equivalent local toric-distinction criterion and Lemma 3.1 supplies the branch needed here:

- if `K/F` is split, then `B` is split;
- if `K/F` is nonsplit and `c>=n`, then `B` is split.

For the protected BSD-001 auxiliary field:

- `2` and every `ell|N` split in `K`;
- at every finite `ell not|N`, the modular representation is unramified, so `n=0`;
- `chi=1`, so `c=0`.

Hence at every finite place either the split clause applies or `c=n=0` and the nonsplit `c>=n` clause applies. Therefore the selected locally distinguished quaternion datum is split at every finite place:

`Sigma = emptyset`.

This conclusion is source-local. It does not identify or alter the archimedean incoherent component.

## 5. Split `p=2` under the CST local measure

Protected WP42B admits, for Disegni's canonical Appendix-A.3 measure `dt_2^can`,

`Q^ord_{2,dt_2^can}=1`

and `vol^circ(H'_2,dt_2^can)=1`.

For the present global ledger choose instead the CST quotient measure at every finite place. At `F=Q`, `v=2`, `K_2/Q_2` is split, so CST gives

`vol(Z_2^x,dt_2^CST)=1`.

Disegni (4.3.1), specialized to `F=Q`, has `e_2=1`; because the quadratic character is locally trivial at a split place,

`L(1,eta_2)^(-1)=1-2^(-1)=1/2`.

Therefore

`vol^circ(H'_2,dt_2^CST)=2`.

The selected ordinary character factor `mu^+(j_2)` and canonical vector ratio are both one by the protected WP42B specialization. Hence

`Q^ord_{2,dt_2^CST}=2`.

Equivalently, `dt_2^CST=2 dt_2^can` on the one-dimensional local quotient-measure line. This is the explicit compensating scalar that WP42B deliberately left open.

## 6. Lemma 4.3.3 after the finite splitness result

Disegni Lemma 4.3.3 / (4.3.4) decomposes `Q^ord` into:

- local `Q_v` terms on the finite auxiliary set `Sigma'`;
- special finite terms over the finite ramification set `Sigma`;
- remaining vector ratios;
- the `p-infinity` ordinary term.

Section 4 above admits `Sigma=emptyset` in this selected lane. One may choose `Sigma'` disjoint from `S_p` and large enough to contain every finite nonspherical place away from `p`, in particular the primes dividing `N D_K`; the selected prime `2` is handled exclusively by the `p-infinity` ordinary factor. Outside `Sigma' union {2}` the spherical local factor is one for the CST local measure. Source-compatible pure tensors may be taken with identical numerator and denominator local vectors wherever the theorem permits, making the surviving vector ratios exactly one rather than merely units.

The only global scalar not fixed by local source formulas is therefore the archimedean formal volume required to convert the product of CST finite measures into Disegni's adelic volume-one measure. Its exact value is a downstream idelic/class-group calculation, not an admitted source statement of this audit.

## 7. Exact downstream interface

After protection, MATHSOLVE may use the following bounded statements.

1. Choose the CST quotient measure `dt_v^CST` at every finite place and a single formal archimedean scalar so that Disegni's global quotient volume is one.

2. The selected finite quaternion ramification set is empty:

   `Sigma=emptyset`.

3. For every finite good auxiliary place `ell not|2N`,

   `Q_{ell,dt_ell^CST}=m_ell`,

   with `m_ell=1` away from `D_K` and `m_ell=|D_ell|^(1/2)` at `ell|D_K`.

4. At the selected split ordinary prime,

   `Q^ord_{2,dt_2^CST}=2`.

5. At infinity in the trivial-weight lane,

   `Q^ord_{infinity,dt_infinity}
    = vol(H'_infinity,dt_infinity)/2`.

6. Protected WP53 remains in force at every odd bad prime:

   `Q_{ell,dt_ell^CST}=1+ell^(-1)` for `ell|N`.

7. No remaining scalar may be discarded as a unit. The global volume-one condition must determine the archimedean scalar exactly before a global `Q^ord` valuation is promoted.

## Refined D2c boundary

The local/source portion of

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`

is admitted. The surviving WP54A task is the exact idelic decomposition of the volume-one quotient and the resulting global multiplication of the admitted local factors.

## Claim firewall

This audit does not prove:

- the idelic class-number volume formula needed downstream;
- a global value of `Q^ord`;
- any cancellation with Tamagawa, regulator, determinant, Bockstein, or WP00 terms;
- fixed-`2` height nondegeneracy;
- D1c;
- the classical Gross–Zagier/WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, priority, patentability, or commercial claims.

**Disposition:** `QUALIFIED_EXACT_GLOBAL_MEASURE_AND_AUXILIARY_QORD_INPUTS`.
