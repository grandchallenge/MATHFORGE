# BSD-001 R5-RES source audit — Colmez–Wang completed cohomology at literal p=2

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#245`.
- Downstream objective: continuing `BSD-R5-RES` after completed `grandchallenge/MATHSOLVE#282`.
- Exact downstream protected head entering this audit: `grandchallenge/MATHSOLVE@89f7b57b48875990c1df499dc306920ff7419cca`.
- Protected MATHFORGE base: `3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.
- Entering source boundary:
  `MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.
- Claim class: bounded source/applicability evidence only.

## 1. Exact source and question

Primary source:

Pierre Colmez and Shanwen Wang, *Une factorisation de la cohomologie complétée et du système de Beilinson-Kato*, arXiv:`2104.09200`, author preprint listed as 2024.

Author PDF:

`https://webusers.imj-prg.fr/~pierre.colmez/KE.pdf`

The paper identifies the modular symbol `(0,infinity)`, viewed in the dual of completed cohomology, with a family object interpolating Kato's Euler system at classical points and develops an integral Kirillov model for completed cohomology.

The downstream question is narrower than that headline statement:

> On the selected good-ordinary analytic-rank-one literal-`p=2` lane, can the paper supply an integral mod-`2` detector of the bottom Beilinson–Kato class which bypasses the normalized Kurihara/local-dual-exponential coordinate?

The required downstream object is still

`c_Q^Kato mod 2 != 0`

or another legitimate finite residual Kato/Kolyvagin component whose nonvanishing implies it through the protected finite-detection interface.

## 2. A genuine literal-2 integral input is present

### 2.1 Theorem 10.1

Colmez–Wang Theorem 10.1 states that, for a non-Eisenstein maximal Hecke ideal `m`, the completed-cohomology Kirillov map is an isometry onto its image in either of two cases:

1. `p>=3` and the residual local representation is not of the form `chi direct_sum chi`;
2. **`p=2` and the residual local representation is neither irreducible nor of the form `chi direct_sum chi`.**

The proof immediately reformulates the assertion as injectivity modulo `p`.

This is not an odd-prime architecture imported by analogy. The source states a literal-`p=2` branch.

**Admitted interface:**

`COLMEZ_WANG_THM10_1_P2_KIRILLOV_MOD2_INJECTIVITY`.

It may be used downstream only after the exact selected residual representation is proved to satisfy:

- non-Eisenstein globally;
- reducible at `G_Q2`;
- non-scalar at `G_Q2`.

### 2.2 Generic integral factorization

In the introduction, Remark 0.3 states that when the maximal ideal is generic there is an integral factorization

`rho_T tensor_T Pi(rho_T^*) -> H^1[rho_T]`

rather than only an isomorphism after inverting `p`.

Section 13.4.1 defines generic to mean non-Eisenstein with residual local restriction not scalar of the form `chi tensor I`, and Theorem 13.11 constructs the corresponding integral isomorphism.

The introduction attaches an additional footnote at `p=2`: the residual local restriction must also be non-irreducible. This matches the literal-`2` hypothesis of Theorem 10.1 on which the integral argument depends.

**Admitted interface:**

`COLMEZ_WANG_GENERIC_INTEGRAL_COMPLETED_COHOMOLOGY_FACTORIZATION_WITH_P2_NONIRREDUCIBLE_CAVEAT`.

This interface concerns the completed-cohomology/Kirillov factorization. It does not by itself identify a particular mod-`2` Kato class as nonzero.

## 3. Compatibility with the selected t_2=1 lane is conditional but exact

Protected downstream R5-WIT proves on the certified `t_2=1` instances that

`E(Q_2)[2^infinity] ~= Z/2`.

Hence the local residual representation `E[2]|G_Q2` has a one-dimensional invariant subspace. In particular, it is reducible.

If it were scalar over `F_2`, then all of `E[2]` would be fixed and `E(Q_2)[2]` would have dimension two, contradicting the protected `t_2=1` local classification. Thus the selected `t_2=1` local residual shape is reducible and non-scalar.

The selected hard filter separately supplies global irreducibility of `E[2]`; downstream must bind that exact protected theorem when using this source interface. Global irreducibility supplies the non-Eisenstein residual representation required by the source.

Therefore the source hypotheses of Theorem 10.1 are **compatible with, and appear tailored to, the protected `t_2=1` selected lane**. This audit does not re-prove the downstream local-torsion or global-irreducibility theorems.

## 4. The Kato comparison is the critical scope break

### 4.1 Theorem 0.10

Theorem 0.10 states for a classical point `x`:

`loc_p(z_Iw(rho_x)) = z_(0,infinity)(rho_x) tensor zeta_B^(-1)`.

Remark 0.11 separates the proof into two cases.

- If the local characteristic-zero representation `rho_{x,p}` is absolutely irreducible, the comparison is obtained directly from explicit formulas.
- If `rho_{x,p}` is an extension of two characters, the source says the result is obtained by **analytic continuation using Theorem 0.12**.

A good-ordinary elliptic curve lies in the second, reducible characteristic-zero case.

Thus the direct irreducible-local proof of Theorem 0.10 is not the selected ordinary route.

### 4.2 Theorem 14.18 does not remove that dependence

Theorem 14.18 is the detailed chapter-14 comparison. In the reducible case its proof explicitly reduces the remaining step to producing a pair `(z,alpha)` by analytic continuation and cites Proposition 15.28.

Therefore the selected ordinary comparison still crosses Chapter 15.

### 4.3 Chapter 15 explicitly excludes p=2

Immediately after beginning the interpolation construction, the source states:

`On suppose p != 2 dans ce qui suit.`

This is not a later optional corollary. Chapter 15 is identified in the introduction as proving Theorem 0.12 after extension of scalars to `Fr(T)`.

Theorem 0.12 is exactly the analytic-continuation input used by Remark 0.11(ii) and Theorem 14.18 in the reducible case.

Therefore the paper, as written, does **not** provide a source-admitted literal-`p=2` proof of Theorem 0.10 for the selected good-ordinary reducible classical point.

## 5. Denominator removal also uses p != 2 materially

The introduction explains that Theorem 0.12 is first constructed over `Fr(T)` and then denominators are removed using Theorem 17.10.

The proof of Theorem 17.10 invokes `p != 2` explicitly: it uses that `Z_p^*` is procyclic in order to choose a generator and run the Ash–Stevens nonvanishing argument.

The paper then uses Theorem 17.10 to conclude that the interpolated Kato class has no pole and is integral.

This gives a second, exact reason not to promote the family Kato comparison at literal `2` merely from the theorem statement.

The restriction may be technically repairable — for example by replacing the single-generator argument with a literal-`2` treatment of

`Z_2^* ~= {+/-1} x (1+4Z_2)`

or by proving the selected classical specialization directly — but no such repair is proved by the audited source.

**Disposition of the full Kato comparison at the selected prime:**

`COLMEZ_WANG_REDUCIBLE_ORDINARY_KATO_SPECIALIZATION_NOT_ADMITTED_AT_LITERAL_P2_FROM_CURRENT_PROOF`.

## 6. Ash–Stevens does not by itself prove Kato indivisibility

In the proof of Theorem 17.10, the cited Ash–Stevens result is used in the following form: a closed `G(Q_S)`-stable subspace of completed cohomology annihilated by `(0,infinity)` must be zero.

This is a strong faithfulness/no-kernel statement for the modular-symbol functional on stable subspaces.

It is **not** by itself any of the following:

- a proof that the selected classical `(0,infinity)` specialization is nonzero modulo two;
- a proof that a particular selected Kato class is primitive modulo two;
- a proof that a comparison scalar is a `2`-adic unit;
- a proof of `R5_RES_ESTABLISHED`.

Any downstream use must first establish a literal-`2` integral specialization bridge from the completed-cohomology modular-symbol object to the selected Kato class.

## 7. Exact source disposition

The source supplies a materially useful new literal-`2` interface but not the complete residual witness.

Provider disposition:

`QUALIFIED_P2_COMPLETED_COHOMOLOGY_INJECTIVITY_WITH_REDUCIBLE_KATO_COMPARISON_GAP`.

The entering broad boundary

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`

is sharpened for this route to the first source-level obligation:

`MISSING_P2_REDUCIBLE_ORDINARY_COMPLETED_COHOMOLOGY_TO_KATO_INTEGRAL_SPECIALIZATION`.

More operationally, a downstream repair must establish one of:

1. a literal-`p=2` version of the Chapter-15 analytic-continuation step for the selected ordinary deformation component, together with integral denominator control;
2. a literal-`p=2` replacement for the Theorem-17.10 denominator-removal argument;
3. a direct classical proof of Theorem-0.10-type localization for the selected good-ordinary `p=2` representation that does not invoke the `p!=2` family argument.

After such a bridge is protected, a second step must still prove that the resulting residual modular-symbol/Kirillov component is nonzero on a selected instance. Theorem 10.1 and the Ash–Stevens no-kernel statement are promising inputs to that second step, but this audit does not collapse them into a pointwise indivisibility theorem.

## 8. Downstream significance

The route is genuinely different from normalized Kurihara detection:

- it works before applying the anomalous ordinary local dual-exponential scalar that killed or cancelled the previous detector;
- it has an explicit integral mod-`2` injectivity theorem at the completed-cohomology layer;
- on the protected `t_2=1` lane, its residual local representation satisfies the distinctive reducible/non-scalar shape required by the source.

Thus the route should be retained as the primary successor architecture, but only with the literal-`2` ordinary Kato specialization gap explicit.

## 9. Non-exhaustiveness and firewall

This audit is not a theorem that Colmez–Wang's comparison cannot be extended to `p=2`. It records the exact scope of the proof as currently written and isolates the first missing bridge for the selected lane.

It does not establish:

- `c_Q^Kato mod 2 != 0`;
- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- BSD-R2-A1;
- novelty or priority;
- public certification;
- MATHCERT certification.
