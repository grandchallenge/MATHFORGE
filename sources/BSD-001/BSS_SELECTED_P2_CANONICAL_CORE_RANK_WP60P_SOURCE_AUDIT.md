# BSD-001 source audit — selected literal-2 canonical cartesianness and core rank one

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#205`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `2b29c3aa57d9f11f01fefc43690391a2d67f137e`.
- Protected MATHSOLVE anchor: `c8e81d262d4da1a36b312f017443777a4c7888db`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source: Barry Mazur and Karl Rubin, *Kolyvagin Systems*, Memoirs AMS 168 (2004), no. 799; especially Definition 1.1.4, hypothesis (H.6), Lemma 3.7.1, Example 4.1.12, Definition 5.2.4, and Theorem 5.2.15.
- Protected predecessor source interface: `sources/BSD-001/BSS_SELECTED_P2_CANONICAL_COISOTROPY_WP60O_SOURCE_AUDIT.md`.
- Disposition: `SELECTED_P2_MR_BSS_CANONICAL_STRUCTURE_CARTESIAN_CORE_RANK_ONE`.
- Claim class: bounded source/applicability evidence only.

## Exact downstream query

Protected MATHSOLVE WP60N proves characteristic-two residual core-graph connectivity under the following structural hypotheses on the residual canonical Selmer structure:

1. residual self-duality;
2. the protected residual restriction-injectivity interface;
3. cartesianness;
4. core rank one;
5. residual coisotropy.

Protected MATHFORGE WP60O now supplies item 5 for the exact Mazur–Rubin/BSS canonical structure on `T_2(E)` and `E[2]`.

This audit checks items 3 and 4 at literal `p=2`.

## 1. Cartesian means Mazur–Rubin hypothesis (H.6)

Mazur–Rubin Definition 1.1.4 defines a local condition to be **cartesian** on a category of quotients when propagation along injections recovers exactly the induced local condition.

Their hypothesis `(H.6)` says that, at every place in the Selmer support, the local condition is cartesian on the quotient category `Quot_R(T)`.

This is the same structural property required by the residual core-vertex bookkeeping used downstream. It is not a separate numerical hypothesis.

## 2. The canonical structure is cartesian on all finite quotients

Mazur–Rubin Lemma 3.7.1 gives a sufficient criterion over a discrete valuation ring: if each local quotient

`H^1(Q_v,T) / H^1_F(Q_v,T)`

is torsion-free, then the induced Selmer structure on every quotient `T/m^k T` satisfies `(H.6)`.

Immediately after that lemma, the source records the two canonical local cases needed here:

- for the Bloch–Kato finite local condition, the local quotient is torsion-free;
- for the unrestricted local condition, the criterion is automatic.

Most decisively, Mazur–Rubin Example 4.1.12 states that if `T=T_0 tensor R` is induced from a free module over a discrete valuation ring, then the canonical Selmer structure `Fcan` induced from `T_0` satisfies `(H.6)` by Lemma 3.7.1.

Apply this with

`R=Z_2`, `T_0=T_2(E)`.

Therefore the canonical structure propagated to every quotient

`T_2(E)/2^k T_2(E)=E[2^k]`

is cartesian. In particular the residual canonical structure on `E[2]` is cartesian.

Record

`SELECTED_P2_MR_BSS_CANONICAL_RESIDUAL_STRUCTURE_IS_CARTESIAN`.

No odd-prime assumption is used in this cartesian conclusion. The source's general chapters explicitly include `p=2`; in particular Proposition 2.3.5 is stated as the relevant global-duality formula adapted to include `p=2`.

## 3. Exact canonical core-rank formula

Mazur–Rubin Definition 5.2.4 defines the integral core rank `chi(T)` to be the common core rank of the finite quotients `T/m^kT`. Thus once the integral canonical core rank is computed, the residual quotient `E[2]` has the same core rank.

Mazur–Rubin Theorem 5.2.15 states for the canonical Selmer structure:

`chi(T*)=0`

and

`chi(T,Fcan)
 = rank_R(T^-)
   + corank_R H^0(Q_p,T*)`,

where `T^-` is the minus submodule for complex conjugation.

The proof invokes Proposition 2.3.5, which the source explicitly says has been adapted to include `p=2`. Hence this formula is available at literal `p=2`; it is not merely an odd-prime elliptic-example statement.

## 4. Apply the formula to `T=T_2(E)`

### 4.1 Minus rank

For an elliptic curve over `Q`, complex conjugation acts on

`V_2(E)=T_2(E) tensor Q_2`

with determinant `-1`. Since the operator has order two, it is semisimple over `Q_2` with eigenvalues `+1` and `-1`. The two-dimensional representation therefore has one-dimensional minus eigenspace.

Intersecting that eigenspace with the lattice gives

`rank_Z2 T_2(E)^- = 1`.

This remains valid at `2`; it does not require dividing by two inside the lattice.

### 4.2 Local invariant corank

Under the Weil pairing,

`T_2(E)^* = Hom(T_2(E),mu_{2^infinity})`

identifies with the discrete module `E[2^infinity]`.

Therefore

`H^0(Q_2,T_2(E)^*) = E(Q_2)[2^infinity]`.

The torsion subgroup of the local elliptic-curve group `E(Q_2)` is finite. Hence its `2`-primary torsion subgroup is finite and has `Z_2`-corank zero:

`corank_Z2 H^0(Q_2,T_2(E)^*) = 0`.

No selected good-ordinary hypothesis is needed for this finiteness statement.

### 4.3 Core rank

Theorem 5.2.15 now gives

`chi(T_2(E),Fcan)=1+0=1`.

By Definition 5.2.4 the same core rank is carried by every finite quotient. In particular

`chi(E[2],Fcan)=1`.

Record

`SELECTED_P2_MR_BSS_CANONICAL_RESIDUAL_CORE_RANK_ONE`.

The conclusion is structural. It does not use analytic rank one and in fact holds for any elliptic curve over `Q` for which the exact canonical Selmer setup is under consideration.

## 5. Combined provider disposition

The exact Mazur–Rubin/BSS canonical residual structure on selected `E[2]` is therefore:

- cartesian;
- core rank one.

Together with protected MATHFORGE WP60O, it is also residually coisotropic.

Thus the structural applicability hypotheses left explicit in protected MATHSOLVE WP60N are source-verified on the selected canonical lane.

Record the combined provider disposition

`SELECTED_P2_MR_BSS_CANONICAL_STRUCTURE_CARTESIAN_CORE_RANK_ONE`.

A downstream MATHSOLVE operation may combine this interface with protected WP60N, WP60O, WP60J, WP60M, WP60G, and WP60H to promote selected residual core-graph connectivity, subject to exact protected-state readback of those inputs.

## Claim firewall

This audit does not establish:

- BSS Theorem 5.20, Theorem 5.2, Theorem 5.25, or Corollary 6.15 at literal `p=2`;
- that every proof step of the published odd-prime Fitting-control theorem has been repaired;
- formal global BSS Hypothesis 3.2(iii), which remains false as protected at finite level;
- the protected infinite BSS H3 condition, which remains false;
- Kato/Fitting divisibility at the height-one prime `(2)`;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
