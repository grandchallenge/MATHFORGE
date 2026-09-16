# BSD-001 source audit — Kataoka–Sano basic Euler-system architecture and literal-p=2 replay

## 1. Purpose

This audit records the exact source architecture in Takenori Kataoka and Takamichi Sano, *On Euler systems for motives and Heegner points*, Journal of the Association for Mathematical Research 2(2) (2024), especially Theorems 3.17 and 3.20 and the finite-level diagram in §3.4.

It is used only to define the downstream literal-2 replay obligation for BSD-001. The published theorem assumes `p>=5`; this audit does not delete or weaken that hypothesis.

## 2. Published theorem and basicness reformulation

Kataoka–Sano Theorem 3.17 assumes Hypotheses 3.1, 3.12, 3.13, 3.14, 3.16, rank `r>=1`, and `p>=5`, and concludes that every Euler-system class `c_{L_infty}` admits a preimage in the inverse determinant line.

Theorem 3.20 reformulates the substantive Euler-system statement: under the same hypotheses except weak Leopoldt Hypothesis 3.1, every Euler-system image is **basic**, meaning that at each finite zero-dimensional coefficient ring it lies in the image of the determinant map.

Thus weak Leopoldt is not part of the basicness assertion needed for one-sided determinant membership.

## 3. Exact finite-level proof architecture

For

`R_{m,n}=A/p^m[Gal(L_n/K)]`,
`T_{m,n}=T tensor_A R_{m,n}`,

Kataoka–Sano reduce basicness to a commutative diagram

`Euler systems -> Kolyvagin systems -> exterior-bidual H^1`

with lower path

`det^{-1}_{R_{m,n}} RΓ -> Stark systems -> Kolyvagin systems`.

The proof requires the following substantive components.

### 3.1 Determinant-to-Stark component

Theorem 3.25 identifies the Stark-system module with the determinant line. Its proof uses:

1. existence of sufficiently many `large` auxiliary square-free products, via Lemma 3.22 / BSS Lemma 3.9 and Hypothesis 3.14;
2. Proposition 3.23, which uses Hypotheses 3.12 and 3.13 plus Poitou–Tate duality to give a finite-free presentation and the determinant identification.

### 3.2 Stark-to-Kolyvagin regulator

Theorem 3.28 is the BSS Theorem 5.2(i) regulator isomorphism. It is the displayed location in the proof where `p>=5` is repeated explicitly. The proof reduces the required BSS Hypothesis 4.2 to the same large-prime/core-vertex input.

### 3.3 Euler-system derivative

Theorem 3.29 is the BSS Corollary 6.13 derivative operator. It requires the Euler-system tower, `H^0(L,T/p)=0`, and the Frobenius injectivity condition corresponding to BSS Hypothesis 6.11.

Once these three components exist, the finite diagram proves that the Euler-system class is basic.

## 4. Published small-prime obstruction

The source theorem remains a `p>=5` theorem.

The proof of the authors' general sufficient criterion for Hypothesis 3.14(iii) uses a scalar-center argument depending on the existence of a nontrivial scalar in `SL_a(Z/p^m)`; their displayed argument assumes `(a,p-1) != 1`. For the elliptic rank-two representation at `p=2`, this route is unavailable.

Moreover, Theorem 3.28 imports the BSS regulator theorem with its own small-prime localization/core-vertex restrictions.

Therefore the source may not be specialized literally to `p=2`.

## 5. Protected selected-lane replacements now available

The following protected MATHSOLVE results post-date the original BSD source screens and are relevant to replaying the proof rather than citing it literally.

1. **WP60M**: the formal finite-level H3.2(iii) vanishing is false, but its unique nonzero defect class is uniformly excluded from every selected modified primal and dual Selmer group by the fixed odd multiplicative local condition. This supplies selected-class restriction injectivity and coefficient reduction without asserting formal H3.2(iii).
2. **WP60R**: selected literal-2 large-prime/localization/core-graph and Hypothesis-4.2 replacements, followed by the selected BSS Theorem 5.20/5.2 regulator replay over `Z/2^m`.
3. **WP60S**: selected literal-2 inverse-limit Stark/Kolyvagin replay over the base `2^m` coefficient tower.
4. **WP60T**: selected literal-2 BSS Theorem 6.12/Corollary 6.13 Euler-system derivative and Corollary 6.15 finite application, with Hypotheses 6.1, 6.7, and 6.11 checked directly.
5. **WP32**: the real-place literal-2 comparison cone has zero alternating `Z_2` determinant valuation, but no canonical unit-level trivialization is claimed.
6. **WP35**: the selected primitive cyclotomic complex admits the required finite-free square `Lambda` presentation.
7. **WP60A-A1**: after localization at the height-one prime `(2)`, determinant membership of the Kato class is exactly the one-sided Fitting inequality called R5-LIFT; determinant generator status is the distinct primitivity equality.

These facts remove the previously identified **base-coefficient** small-prime obstructions. They do not automatically prove the corresponding statements over `R_{m,n}`.

## 6. Exact equivariant replay obligation

For BSD-001 take `K=L=Q`, `L_infty=Q_infty`, and

`R_{m,n}=Z/2^m[Gamma_n]`, `Gamma_n=Gal(Q_n/Q)`.

A literal-2 replay of Kataoka–Sano Theorem 3.20 must establish at every `m,n`:

1. `R_{m,n}` is the local zero-dimensional Gorenstein coefficient ring required by the Stark/Kolyvagin formalism;
2. the selected residual module remains the irreducible `E[2]` module;
3. a fixed `tau` gives `T_{m,n}/(tau-1)T_{m,n}` free rank one over `R_{m,n}`;
4. the false formal H3.2(iii) condition is replaced on the **actual modified Selmer groups** by an equivariant analogue of the WP60M exclusion and coefficient-reduction argument;
5. sufficiently many large auxiliary products exist and the selected core vertices give the needed finite freeness over `R_{m,n}`;
6. the Stark-to-Kolyvagin regulator is an isomorphism over `R_{m,n}` by a genuine equivariant lift of WP60R, not by base-ring citation;
7. the Kato Euler system has the selected derivative in the equivariant Kolyvagin module, with first component equal to the finite-layer Kato class;
8. all constructions are compatible in `m,n` so that the determinant preimages pass to the cyclotomic inverse limit.

For the fixed odd multiplicative inertia element used by WP60M, the cyclotomic `2`-extension is unramified at that odd prime. Thus the group-ring factor is fixed by this `tau`, and the rank-one quotient condition is expected to reduce to the already protected primitive-unipotent quotient on `T_2(E)`. This observation is a downstream proof obligation, not a provider theorem.

## 7. Local and archimedean caution

Kataoka–Sano work in an odd-prime framework. At literal `2`, real-place cohomology and good-ordinary local control cannot be discarded automatically.

Protected WP32 shows only that the real-place correction has zero net `2`-adic determinant valuation. Protected WP23 records a genuine finite good-ordinary local-control defect at `2`.

A downstream R5-LIFT proof must therefore show that these corrections either:

- are already incorporated in the global determinant complex used by the basic-element map; or
- contribute only factors that are units after localization at the height-one prime `(2)`; or
- are explicitly retained in the determinant/Fitting comparison.

No cancellation may be assumed from valuation heuristics alone at the finite group-ring level.

## 8. Source disposition

`KATAOKA_SANO_BASIC_EULER_ROUTE_ADMITTED_AS_PROOF_ARCHITECTURE_WITH_LITERAL_P2_EQUIVARIANT_REPLAY_REQUIRED`.

The source architecture materially sharpens the downstream problem: R5-LIFT can be closed by proving a selected literal-2 version of Theorem 3.20 over the cyclotomic coefficient rings, without first proving weak Leopoldt and without proving determinant primitivity.

## 9. Claim firewall

This source audit does **not** establish:

- literal-2 Kataoka–Sano Theorem 3.20;
- `MISSING_P2_EQUIVARIANT_CYCLOTOMIC_DETERMINANT_STARK_KOLYVAGIN_REPLAY`;
- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- R5-LIFT or R5-PRIM;
- D2d or BSD-R2-A1;
- novelty, priority, or MATHCERT certification.
