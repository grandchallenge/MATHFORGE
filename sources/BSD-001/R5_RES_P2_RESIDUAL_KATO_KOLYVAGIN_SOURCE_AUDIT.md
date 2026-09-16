# BSD-001 source audit — literal-p=2 residual cyclotomic Kato/Kolyvagin nonvanishing

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#225` (`BSD R5-RES`).
- Downstream theorem operation: `grandchallenge/MATHSOLVE#273` (`BSD R5-RES`).
- Protected MATHFORGE entering base: `5aef30aa64730ca777329013e1e33c03f34a6e3a`.
- Protected MATHSOLVE R5-PRIM completion: `36202d97e2cd96956c8a4aafa43941f6219776c5`.
- Constitutional/staffing authority used downstream: `grandchallenge/INTELLECT@f042220f3bed7cb7b5069256e8f6305c850c0628`, `GI-STEWARD-0003`.
- Source screen date: 2026-09-16.
- Claim class: source/dependency architecture only. No literal-`p=2` residual nonvanishing theorem, R5-RES theorem, R5-PRIM theorem, BSD theorem, novelty/priority claim, or certification is promoted here.

Primary sources audited:

1. Ashay Burungale, Francesc Castella, Giada Grossi, Christopher Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory*, arXiv:2312.09301, final 2026 version / author manuscript.
2. Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, arXiv:2203.12159, final version available in 2025–2026.
3. Chan-Ho Kim, Myoungil Kim, Hae-Sang Sun, *On the indivisibility of derived Kato's Euler systems and the main conjecture for modular forms*, Selecta Math. 26 (2020), Paper 31; current arXiv:1709.05780 version accessed 2026-09-16.
4. Ryotaro Sakamoto, *p-Selmer group and modular symbols*, Doc. Math. 27 (2022), 1891–1922, DOI `10.4171/DM/X21`.
5. Ryotaro Sakamoto, *The theory of Kolyvagin systems for p=3*, J. Théor. Nombres Bordeaux 36 (2024), 919–946, published 2025, DOI `10.5802/jtnb.1300`.

Source locators:

- `https://arxiv.org/abs/2312.09301`
- `https://arxiv.org/abs/2203.12159`
- `https://arxiv.org/abs/1709.05780`
- `https://ems.press/journals/dm/articles/13131888`
- `https://www.numdam.org/articles/10.5802/jtnb.1300/`

## Downstream question already fixed by protected MATHSOLVE

Protected `BSD-R5-PRIM` does not leave the remaining problem as a generic main-conjecture or determinant problem. It proves the exact reduction

`R5-PRIM`

`<=>`

`the inverse-limit selected Kato-derived Kolyvagin system is nonzero after reduction modulo 2 in KS_Lambda / 2`.

At the height-one prime `(2)` of `Lambda = Z_2[[T]]`, the residue field is `F_2((T))`. Therefore powers of `T` are units after localization at `(2)`. Protected R5-PRIM further proves finite detection: it suffices to exhibit a legitimate finite cyclotomic mod-2 image of the protected inverse-limit Kato/Kolyvagin class that is nonzero. A finite-level **basis** theorem is not required.

The entering theorem frontier is therefore exactly

`MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING`.

The source audit asks whether current literature supplies that theorem directly, or a finite explicit witness whose literal-2 bridge can be replayed from the protected MATHSOLVE stack.

## 1. Burungale–Castella–Grossi–Skinner: strong cyclotomic nonvanishing architecture, but odd-p and main-conjecture dependent

The paper works with an **odd** prime `p`. Its cyclotomic section proves a Beilinson–Kato analogue of Kolyvagin nonvanishing. In the good-ordinary setting, Theorem C derives nonvanishing of Kato's Kolyvagin system using:

1. nonvanishing of a first Kato class after a suitable cyclotomic specialization;
2. a divisibility-index estimate for that first class in terms of the dual Selmer group and Tamagawa factors;
3. a Kolyvagin-system bound with controlled error terms;
4. the rational cyclotomic Iwasawa Main Conjecture as an input to the divisibility-index comparison.

This is highly relevant architecture. It is not a direct literal-2 theorem for two independent reasons:

- the source fixes `p` odd;
- the cyclotomic Main Conjecture enters the proof of the key divisibility estimate.

For downstream R5-RES, importing the full cyclotomic Main Conjecture at `p=2` would not be a useful independent shortcut unless its exact logical strength is shown to be strictly upstream of, rather than equivalent to, the residual height-one `(2)` nonvanishing now under study.

**Source disposition:** `BCGS_CYCLOTOMIC_NONVANISHING_ARCHITECTURE_ODD_P_MAIN_CONJECTURE_DEPENDENT`.

## 2. Chan-Ho Kim: the blind-spot formulation matches R5-RES, but the published theorem starts at p>=5

Kim's structural theorem takes a semistable reduction prime `p >= 5` with surjective residual representation. Under the Iwasawa Main Conjecture after inverting `p`, or analytic rank at most one, it concludes that Kato's Kolyvagin system is nontrivial and determines Selmer structure through Kurihara numbers.

Conceptually, the source is particularly useful because it describes vanishing modulo a height-one prime as a **blind spot** of the Lambda-adic Kato/Kolyvagin system. Protected R5-PRIM has now identified `(2)` as exactly the height-one prime whose blind-spot status must be resolved.

However, the source does not supply the required literal-2 theorem. Its small-prime restrictions are tied to the Mazur–Rubin/Chebotarev Kolyvagin-system machinery. Sakamoto subsequently repaired part of that machinery at `p=3`, not at `p=2`.

Protected MATHSOLVE already contains substantially stronger selected-lane literal-2 replacements for this structural layer:

- WP60M: all-level selected defect exclusion without reinstating false formal H3.2(iii);
- WP60R: literal-2 localization, core graphs, finite-singular maps, rank-one Kolyvagin-system freeness and Fitting equality for basis systems;
- WP60S: inverse-limit compatibility;
- WP60T: selected literal-2 Kato derivative and first-component compatibility;
- R5-LIFT/R5-PRIM: exact height-one determinant and residual reductions.

Accordingly, Kim's `p>=5` Kolyvagin-structure restriction is **not** the first remaining R5-RES obstruction. That machinery has already been replaced on the selected lane.

**Source disposition:** `KIM_BLIND_SPOT_ARCHITECTURE_RELEVANT_SMALL_PRIME_KS_LAYER_ALREADY_REPLACED_DOWNSTREAM`.

## 3. Kim–Kim–Sun: exact finite modular-symbol witness, but a new forced p=2 ordinary obstruction appears

Kim–Kim–Sun is the most direct source architecture for the finite-detection objective.

The paper proves an explicit criterion that starts with a square-free product `n` of Kolyvagin primes and its Kurihara number `delta_tilde_n`, computed from integral modular symbols and discrete logarithms. Under the source hypotheses, if

`delta_tilde_n != 0 (mod lambda)`

for some `n`, then the derived Kato Euler system is nonzero modulo `lambda`. The key bridge is an explicit computation of the **integral image of the derived Kato classes under the dual exponential map**.

This is almost exactly the witness shape wanted by protected R5-PRIM:

`finite modular-symbol quantity nonzero mod p`

`=>`

`finite Kato derivative nonzero mod p`

`=>`

`inverse-limit Kato/Kolyvagin class not in the height-one blind spot`.

The source even gives a practical search procedure: choose Kolyvagin primes, compute `delta_tilde_n`, and continue until a nonzero residue is found.

### 3.1 Exact published restrictions

The source begins Theorem 1.1 with `p > 2` and assumes:

- `(NA)`:
  `a_p(f) != 1 (mod lambda)` and `a_p(f) != psi(p) (mod lambda)`;
- `(Im)`: residual image contains a conjugate of `SL_2(F_p)`;
- `(Tam)`: the stated tame-level/Tamagawa conductor conditions.

For an elliptic curve over `Q` with trivial nebentype and **good ordinary reduction at p=2**, ordinarity means `a_2` is a 2-adic unit, hence `a_2` is odd. Therefore

`a_2 == 1 (mod 2)`.

With trivial character, `psi(2) == 1 (mod 2)` as well. Thus the source's `(NA)` condition fails automatically on the selected good-ordinary literal-2 lane.

This is qualitatively different from the already-repaired Mazur–Rubin small-prime localization issue. It is a **local ordinary / explicit-reciprocity normalization obstruction** in the source's map from Kato derivatives to the residual modular-symbol witness.

### 3.2 Why the naive Kurihara criterion cannot simply be specialized to p=2

At `p=2`, a direct statement

`delta_tilde_n != 0 mod 2 => protected Kato derivative != 0 mod 2`

is not authorized by Kim–Kim–Sun because the integral dual-exponential comparison was proved only after imposing `(NA)`, and `(NA)` is impossible for a good-ordinary elliptic curve with trivial character at `2`.

No amount of replay of the already-protected WP60R core-graph machinery removes this particular issue: it lies in the **local explicit-reciprocity map at p**, not in global Kolyvagin-system freeness or Chebotarev localization.

**Source disposition:** `KKS_FINITE_KURIHARA_WITNESS_EXACTLY_RELEVANT_BUT_NA_FORCED_TO_FAIL_AT_GOOD_ORDINARY_P2`.

## 4. Protected p=2 local evidence shows what a correct replay must normalize

The existing protected BSD stack already records a genuine good-ordinary local correction at `2` rather than treating the local term as zero.

In particular, protected local-control work records a finite ordinary defect with Fitting factor governed by `(3-a_2)^2`; the strict local Iwasawa higher term is `T`-primary and therefore disappears only **after localization at `(2)`**. That was sufficient for R5-LIFT/R5-PRIM's height-one determinant algebra, because `T` is a unit in `Lambda_(2)`.

R5-RES is different: it asks for a **finite mod-2 witness before height-one localization**. A local factor that is harmless after inverting `T` can annihilate a naive residual dual-exponential/modular-symbol image at a finite level.

The source-first conclusion is therefore that a literal-2 replay must not try to prove the unmodified Kim–Kim–Sun theorem. It must construct or source a **normalized anomalous-ordinary residual reciprocity map** in which the forced local ordinary factor is extracted explicitly, and then prove that the normalized map remains integral and detects the protected Kato-derived Kolyvagin component modulo `2`.

This requirement is compatible with, but not already implied by, protected WP23/WP46A/R5-LIFT. Those results control the size/support of the local correction; they do not provide the missing normalized mod-2 dual-exponential/Kurihara identity.

## 5. Sakamoto: small-prime Kolyvagin repair reaches p=3, not p=2

Sakamoto's 2022 modular-symbol theorem is formulated for `p>3`. His later paper, *The theory of Kolyvagin systems for p=3*, repairs Kolyvagin-system theory in a setting previously excluded and proves Kurihara's modular-symbol conjecture for `p=3`.

This confirms that the odd-prime small-prime machinery can sometimes be repaired by a dedicated coefficient-ring analysis. It does not supply a literal-2 theorem, and it does not address the forced good-ordinary `(NA)` failure above.

For R5-RES, Sakamoto therefore supports the **methodology** of a small-prime replay but does not close the new local explicit-reciprocity boundary.

**Source disposition:** `SAKAMOTO_P3_REPAIR_METHOD_RELEVANT_NO_LITERAL_P2_RECIPROCITY_INTERFACE`.

## 6. Current source screen: no direct literal-p=2 theorem located

The bounded source screen also checked source-current good-ordinary main-conjecture and Kato/Kolyvagin nonvanishing literature through September 2026. The direct theorems located continue to assume `p>2`, odd `p`, `p>=5`, or `p>3` in the relevant good-ordinary lane.

This audit therefore does **not** identify a direct published theorem that may simply be imported to prove

`MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING`.

This is a statement about the audited route set, not a universal claim that no such theorem can exist anywhere.

## 7. Exact source-admitted finite-detection architecture for MATHSOLVE

The current sources and protected downstream stack support the following composable architecture:

1. use protected R5-PRIM finite detection to reduce inverse-limit residual nonvanishing to one finite cyclotomic mod-2 Kato/Kolyvagin component;
2. use protected WP60M/R/S/T for the literal-2 global Kolyvagin-system, derivative, finite-singular and inverse-limit layers;
3. construct a local ordinary **normalized** residual regulator/dual-exponential map at `p=2` that removes the forced anomalous factor while remaining integral;
4. prove a normalized literal-2 explicit-reciprocity identity comparing the selected Kato derivative component with a finite modular-symbol/Kurihara-type quantity;
5. exhibit or prove nonvanishing of that normalized finite quantity on the selected lane;
6. conclude the finite Kato/Kolyvagin component is nonzero, hence close R5-RES by the protected finite-detection theorem.

Steps 1 and 2 are already protected theorem interfaces. Step 3–4 is the first new source/theorem boundary. Step 5 is downstream arithmetic once that bridge is available.

## 8. Recommended exact downstream boundary

The first independent new theorem/source obligation is:

`MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`.

Required content of that theorem:

- selected good-ordinary elliptic curve over `Q` at `p=2` with the protected irreducible/surjective residual lane;
- a finite cyclotomic/Kolyvagin level compatible with protected WP60T derivatives;
- an explicitly normalized local ordinary map that accounts for the forced anomalous factor at `2`;
- an integral mod-2 comparison between a protected Kato-derived class and a computable modular-symbol/Kurihara-type quantity;
- a proof that nonzero normalized analytic residue implies nonzero protected Kato/Kolyvagin residue;
- exact compatibility with corestriction / finite-layer detection used by R5-PRIM.

A theorem satisfying this interface would make the finite arithmetic witness route composable. It would **not by itself** prove R5-RES unless the normalized residual quantity is also shown nonzero on the selected lane.

## 9. Source-level disposition

`QUALIFIED_REPLAY_ARCHITECTURE_WITH_P2_ANOMALOUS_ORDINARY_RECIPROCITY_GAP`.

The literature gives a strong finite modular-symbol/Kurihara witness architecture, and protected MATHSOLVE already replaces most odd-prime Kolyvagin-system structural dependencies. The first genuinely new literal-2 dependency is the normalized anomalous-ordinary explicit-reciprocity bridge identified above.

## Claim firewall

This audit does **not** establish:

- a literal-`p=2` extension of Burungale–Castella–Grossi–Skinner, Chan-Ho Kim, Kim–Kim–Sun, Sakamoto, Mazur–Rubin, Kato or Kurihara;
- `MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`;
- nonvanishing of any normalized Kurihara quantity on the selected BSD lane;
- `MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING`;
- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- public certification or MATHCERT certification.

It admits a proof architecture and isolates the first exact literal-2 source/theorem obligation only.
