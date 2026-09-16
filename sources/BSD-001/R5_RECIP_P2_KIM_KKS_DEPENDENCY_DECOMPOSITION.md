# BSD-001 R5-RECIP source audit — literal-p=2 Kim/KKS dependency decomposition

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#228`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#278`.
- Protected entering MATHFORGE: `7da3f07248b5d8cf3d0bd1e57e9d8b7f5b78d063`.
- Protected entering MATHSOLVE: `24081fcc1b212d33dd865cc5512a837b8101faf1`.
- Parent theorem boundary: `MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`.
- Claim class: source/dependency architecture only.

Primary sources inspected:

1. Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, final manuscript dated 2025-05-12, especially §1.4 and §3, including Lemma 3.3, Proposition 3.10, Theorem 3.11, Lemma 3.12 and Proposition 3.13. Source locator: `https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf`.
2. Chan-Ho Kim, Myoungil Kim, Hae-Sang Sun, *On the indivisibility of derived Kato's Euler systems and the main conjecture for modular forms*, Selecta Math. 26 (2020), Paper 31, especially §§7.3–7.4 / Theorem 7.5. Source locator: `https://arxiv.org/pdf/1709.05780`.
3. Kęstutis Česnavičius, *The Manin constant in the semistable case*, Compos. Math. 154 (2018), already admitted by protected BSD-001 WP58 source record.
4. Robert Pollack, *On the p-adic L-function of a modular form at a supersingular prime*, especially Remarks 5.3–5.5, used only to distinguish bounded/integral modular-symbol normalization from the formal `1/2` notation; it is not imported as a good-ordinary literal-2 theorem.

## 1. Kim Theorem 3.11 has three logically distinct layers

Kim Theorem 3.11 is stated for `p>=5`, surjective residual representation and Manin constant prime to `p`. In the source normalization it proves

`xi o exp^*_{omega_E} o loc^s_p(kappa_n^Kato) = u * p^t * delta_tilde_n`

in `Z_p/I_n Z_p`, with `u` a unit and

`p^t = #E(Q_p)[p^infinity]`.

The proof is not a single indivisible odd-prime argument. It separates into:

1. a local integral Bloch–Kato lattice / torsion-coefficient map (`§3.1–§3.4`, notably Lemma 3.3 and Proposition 3.10);
2. Kato explicit reciprocity followed by Kolyvagin differentiation;
3. a modular-symbol/Kurihara derivative identity imported from KKS.

For literal `p=2`, these layers must be replayed independently rather than importing the printed `p>=5` theorem.

**Disposition:** `KIM_RECIPROCITY_SPLITS_INTO_LOCAL_LATTICE_DERIVATIVE_AND_PERIOD_LAYERS`.

## 2. The first local restriction occurs already at p>2

Kim Lemma 3.3, in the good-reduction case, assumes `p>2` and identifies the dual-exponential image lattice as

`#E(F_p) / p^(1+t) * Z_p`,

where `t=length_Zp(E(Q_p)[p^infinity])`.

Thus the literal-2 problem is not merely the `p>=5` Kolyvagin-system hypothesis printed in Theorem 3.11. There is a genuinely local integral issue one step earlier.

The proof of Lemma 3.3 computes this image from the Kummer lattice / formal logarithm and local duality. The formula itself explicitly tracks all local `p`-power torsion.

Protected MATHSOLVE WP60B has independently proved on the selected good-ordinary literal-2 lane that

`log_{omega_E}(E_1(Q_2)) subset 4 Z_2`.

This is exactly the local datum that must replace the ordinary odd-prime shallow-log computation. Whether it reproduces Kim's same lattice formula at `p=2` after accounting for formal rational `2`-torsion is a downstream theorem question, not a source claim.

**Disposition:** `KIM_LEMMA_3_3_REQUIRES_LITERAL_P2_LOCAL_LATTICE_REPLAY`.

## 3. KKS Theorem 7.5 is not where the non-anomalous hypothesis enters

KKS Theorem 7.5 gives the Kolyvagin derivative identity for modular symbols / Kurihara numbers. Its proof expands the group-ring modular-symbol sum and uses

`(sigma_eta_l - 1) D_l = l - 1 - Tr_l`,

plus Hecke relations to eliminate lower-degree terms. The theorem is the combinatorial derivative identity used at the end of the reciprocity computation.

In the proof of KKS Theorem 1.1, the non-anomalous scalar enters later through the local/global multiplier containing

`p - a_p(f) + psi(p)`.

The source's `(NA)` condition makes this factor a `p`-adic unit. At good ordinary `p=2` with trivial character this fails automatically because `a_2` is odd.

Therefore protected WP60R/T need not reconstruct Theorem 7.5 from scratch merely because `(NA)` fails. The unresolved question is whether the local integral map and normalization extract the forced even factor while preserving a nonzero normalized residue.

**Disposition:** `KKS_DERIVATIVE_IDENTITY_SEPARABLE_FROM_NA_LOCAL_SCALAR`.

This statement is architectural. KKS as published still works in an odd-prime coefficient setting; literal-2 use requires a downstream integral replay.

## 4. The p>=5 Kolyvagin-system layer is already replaced downstream

Protected MATHSOLVE WP60M/R/S/T supplies the selected literal-2 global infrastructure needed after differentiation:

- all-level selected defect exclusion;
- characteristic-two localization, finite-singular maps and core graphs;
- rank-one Kolyvagin-system freeness and the relevant Fitting-control replacement;
- inverse-limit compatibility;
- literal-2 Kato Euler-system derivative and first-component compatibility.

Thus the generic Mazur–Rubin / Chebotarev small-prime restrictions are not the first remaining obligation for R5-RECIP.

**Disposition:** `GLOBAL_SMALL_PRIME_KOLYVAGIN_LAYER_ALREADY_REPLACED_ON_SELECTED_LANE`.

## 5. Manin/differential normalization is already a 2-unit, but plus-symbol integrality still requires an exact replay

Protected MATHFORGE WP58 admits Česnavičius's semistable theorem: for the optimal quotient in the selected semistable isogeny class, the optimal Manin constant is exactly `+-1`, including at `2`.

Protected MATHSOLVE WP58A then chooses a minimum-degree isogeny from the optimal curve to the selected curve and proves that this isogeny has odd degree from irreducibility of the selected `E[2]`. Hence its differential scalar `C_f` is a `2`-adic unit.

This removes one possible even Manin/differential factor from the selected normalization.

It does **not**, by itself, authorize treating the formal `1/2` appearing in odd-prime plus modular-symbol formulas as a unit. At `p=2` the integral `+/-` decomposition of modular-symbol / relative-homology lattices must be handled before a Kurihara number can be reduced modulo `2`.

Kim §1.4 uses the real Néron period and states p-integrality of the normalized modular symbols under its running `p>=5`, residual, and Manin assumptions. Pollack's discussion likewise shows that Néron-period modular symbols can have bounded denominators and that a factor `2` is genuinely visible in integral normalization. Neither source, as used here, supplies the selected good-ordinary literal-2 plus-symbol integrality theorem directly.

**Disposition:** `MANIN_SCALAR_2UNIT_PROTECTED_PLUS_MODULAR_SYMBOL_P2_INTEGRALITY_REQUIRES_REPLAY`.

## 6. Kato explicit reciprocity is not the identified small-prime blocker

The protected BSD source stack already admits integral Kato Euler-system classes at literal `2`, and WP60T constructs their selected finite derivatives. Kim's own discussion notes Kato explicit reciprocity as applying to the first Kato class without imposing a blanket odd-prime restriction in the rank-zero statement.

This audit therefore does not identify the existence of Kato's explicit reciprocity law itself as the first new literal-2 obstacle. The unresolved issue is the exact integral lattice/period normalization through which that law is reduced modulo `2` and differentiated.

**Disposition:** `KATO_RECIPROCITY_NOT_CURRENTLY_IDENTIFIED_AS_FIRST_P2_BLOCKER`.

No stronger source claim is made.

## 7. Exact downstream decomposition

The parent boundary

`MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`

now decomposes into two concrete theorem obligations.

### R5-RECIP-LOCAL

Prove the selected literal-2 analogue of Kim Lemma 3.3 / Proposition 3.10:

1. determine the exact kernel and image of the formal logarithm on `E_1(Q_2)`;
2. retain `t_2=length_Z2(E(Q_2)[2^infinity])`;
3. compute the exact free Kummer lattice in `E(Q_2)`;
4. derive the exact dual-exponential image by local Tate duality;
5. construct the torsion-coefficient reduction map compatible with protected WP60T classes.

### R5-RECIP-SYMBOL

Prove an integral literal-2 plus modular-symbol/Kurihara normalization compatible with the protected optimal-composite parametrization:

1. no use of `1/2` as a unit;
2. exact comparison with the real Néron/canonical period;
3. preserve the protected `C_f in Z_2^x` transport;
4. prove the KKS derivative identity in the resulting literal-2 integral quotient.

If both obligations close, the remaining source architecture is sufficient to attempt the selected normalized finite reciprocity identity by combining them with WP60T.

## 8. Source-level disposition

`QUALIFIED_REPLAY_ARCHITECTURE_LOCAL_AND_PLUS_SYMBOL_P2_REPLAYS_ISOLATED`.

The source screen no longer supports treating `p>=5` as a monolithic obstruction. The exact remaining small-prime work is local lattice/torsion normalization plus integral plus-modular-symbol normalization. The global Kolyvagin derivative machinery has already been replaced on the selected lane.

## Claim firewall

This audit does not establish:

- Kim Lemma 3.3, Proposition 3.10, or Theorem 3.11 at `p=2`;
- KKS Theorem 7.5 as an integral literal-2 statement;
- literal-2 plus modular-symbol integrality;
- a normalized nonzero Kurihara witness;
- `MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`;
- residual Kato/Kolyvagin nonvanishing;
- R5-RES or R5-PRIM;
- D2d or BSD-R2-A1;
- novelty, priority, public certification, or MATHCERT certification.
