# BSD-001 source audit — coisotropic core-connectivity interfaces for literal `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#200`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `54f1eaea24b35d4ca37e778786345c3622b6fd98`.
- Protected MATHSOLVE baseline: `5c65994e1b5554b47963190d959d8f9ed6433765`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source A: David Burns, Ryotaro Sakamoto, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448.
- Primary source B: Ryotaro Sakamoto, *The theory of Kolyvagin systems for p = 3*, Journal de Théorie des Nombres de Bordeaux 36 (2024), 919–946, DOI 10.5802/jtnb.1300.
- Disposition: `COISOTROPIC_CONNECTIVITY_INTERFACE_ADMITTED_WITH_CHARACTERISTIC_TWO_LOCALIZATION_GAP`.
- Claim class: bounded primary-source proof-dependency and applicability evidence only.

## Exact downstream query

Protected MATHSOLVE WP60H reduces the literal-`2` minimal-core common-prime failure to a precise residual relation: for the two primal witness classes and two one-dimensional dual classes, the bad affine fibers cover exactly when some three of the four nonzero `F_2` classes sum to zero.

Protected WP60M removes the separate finite Hypothesis-3.2(iii) restriction-injectivity obstruction at every coefficient level.

The remaining query is therefore:

> Can residual coisotropy be used to replace the BSS minimal-core `s=2` simultaneous-localization step at characteristic two, and if so, does the rest of the BSS graph-connectivity proof require any further multi-class localization theorem?

This audit admits the exact source interfaces needed to answer that question downstream. It does not itself prove a characteristic-two replacement theorem.

## Source B — residual coisotropy is an exact local inclusion

Sakamoto Definition 3.8 assumes a residual self-duality and then defines a Selmer structure `F` to be **residually coisotropic** when, after identifying the residual representation with its Tate dual,

`H^1_{F*}(K_q, Tbar) subset H^1_F(K_q, Tbar)`

for every place in the Selmer structure.

Thus the phrase is not merely a dimension condition: it is a place-by-place inclusion of dual residual local conditions into primal residual local conditions.

Sakamoto Lemma 3.11 then exploits the quotient between these structures at the places where the inclusion is strict. This is the source-supported mechanism used later in the graph argument.

**Disposition:** `RESIDUAL_COISOTROPY_IS_LOCAL_DUAL_INCLUSION`.

## Source B — the p=3 minimal-core decomposition

In Lemma 6.4, Sakamoto takes two minimal core vertices `d_i`, removes primes `q_i`, and writes `e_i=d_i/q_i`. The source obtains

`lambda(e_i)=2`, `lambda*(e_i)=1`

in core rank one. By residual coisotropy it has

`H^1_{F*(e_i)} subset H^1_{F(e_i)}`.

The dimension calculation and vanishing of the intersection with the core line then give the direct-sum decomposition

`H^1_{F(e_i)}
 = H^1_{F(d_i)} direct_sum H^1_{F*(e_i)}`.

This is the exact structural interface relevant to the protected WP60H four-class relation.

**Disposition:** `COISOTROPY_SUPPLIES_MINIMAL_CORE_PRIMAL_DUAL_PLANE_DECOMPOSITION`.

## Source B — Sakamoto's localization step is genuinely characteristic-three

The rest of Sakamoto Lemma 6.4 is not a characteristic-independent theorem.

The proof invokes two localization results from §5:

1. Lemma 5.2: for four nonzero classes over `F_3`, if their span has dimension at least three, there are infinitely many auxiliary primes where all four localizations are nonzero.
2. Corollary 5.5: any three nonzero residual classes over `F_3` can be simultaneously localized nontrivially.

Sakamoto Remark 5.3 already records a four-class failure over `F_3` in a two-dimensional configuration, and Remark 5.4 states that Lemma 5.2 is used in Corollary 5.5 and Lemma 6.4.

Protected MATHSOLVE WP60H proves the exact `F_2` analogue behaves differently: over `F_2`, four bad affine fibers cover whenever there is an odd-cardinality dependence; in particular a three-term relation can obstruct simultaneous localization even when the four classes span dimension three. Similarly, a dependent triple `c_1+c_2+c_3=0` cannot have all three nonzero in a one-dimensional `F_2` local target.

Therefore Sakamoto Lemma 6.4 and Theorem 6.7 cannot be cited unchanged as literal-`p=2` connectivity theorems.

**Disposition:** `SAKAMOTO_P3_CONNECTIVITY_NOT_DIRECTLY_PORTABLE_TO_P2`.

## Source A — the post-minimal arbitrary-core reduction is pairwise only

BSS II Lemma 5.17 (arXiv v1 numbering) starts with a core vertex `n` having more prime factors than the minimal value `lambda*(1)`. After a deterministic local-dimension argument it chooses a divisor `m=n/q` with `lambda*(m)=1`.

Its only Chebotarev use is then Lemma 3.9 applied so that two maps are nonzero at one new auxiliary prime `r`:

- a map from a nonzero primal residual Selmer space to the one-dimensional finite local space at `r`;
- a map from the one-dimensional dual residual Selmer space at `m` to its finite local space at `r`.

To make the first map nonzero it suffices to choose one nonzero primal class. Thus this call is exactly a one-primal/one-dual localization problem, not an `s=2` four-class problem.

The remainder of Lemma 5.17 is dimension bookkeeping, global duality, and pairwise path moves. Theorem 5.18 then combines this arbitrary-core reduction with minimal-core connectivity.

Accordingly, once a literal-`2` replacement for minimal-core connectivity is available, protected MATHSOLVE WP60G supplies the missing one-primal/one-dual localization interface needed to replay the arbitrary-core reduction under the same residual hypotheses.

**Disposition:** `BSS_ARBITRARY_CORE_REDUCTION_NEEDS_ONLY_PAIRWISE_LOCALIZATION`.

This is a proof-dependency statement. It does not itself execute the downstream characteristic-two proof.

## Source B — elliptic verification of coisotropy has extra arithmetic hypotheses

Sakamoto Definition 9.2 uses the canonical Selmer structure with unramified local condition away from `3` and full local cohomology at `3`.

Lemma 9.3 proves that this canonical structure is cartesian, has core rank one, and is residually coisotropic under two additional kinds of hypotheses:

- `E(Q_l)[3]=0` at the specified ramified places and at `3`;
- every bad Tamagawa factor is prime to `3`.

The proof explicitly notes that the bad-prime calculation relies critically on triviality of the `3`-parts of the Tamagawa numbers.

These hypotheses are not a theorem at literal `p=2`, and the protected selected `BSD-R2-A1` assumptions do not imply their naive `2`-adic analogues. In particular, protected WP13 allows bad primes with even Tamagawa factor, while selected good ordinary reduction at `2` does not by itself establish the required local residual-cartesian/coisotropic comparison.

Therefore Sakamoto Lemma 9.3 does not authorize the assertion that the selected literal-`2` canonical BSS structure is residually coisotropic.

**Disposition:** `SELECTED_P2_CANONICAL_COISOTROPY_NOT_VERIFIED_BY_SAKAMOTO_ELLIPTIC_APPLICATION`.

## Exact provider conclusion

The sources support the following sharpened proof architecture.

1. Residual coisotropy is strong enough to place the one-dimensional dual line inside the two-dimensional primal space obtained by deleting a prime from a minimal core. This is the exact extra structure missing from protected WP60H.
2. Sakamoto's published `p=3` proof then obtains connectivity using localization statements that are false in that form over `F_2`; it is not a ready-made literal-`2` theorem.
3. The BSS step reducing arbitrary core vertices to minimal ones needs only one-primal/one-dual localization. Protected WP60G has already repaired that type of call at literal `2` on the selected self-dual residual lane.
4. Hence a new characteristic-two **minimal-core exchange theorem under residual coisotropy** would be sufficient to repair the remaining graph-connectivity proof mechanism; no additional four-class theorem is needed after the minimal-core stage.
5. Uniform applicability to the selected elliptic class still requires a separate proof that its residual canonical structure is coisotropic, or a non-coisotropic replacement argument.

Record the downstream reopening form

`P2_BSS_COISOTROPIC_MINIMAL_CORE_EXCHANGE_THEOREM`.

If such a theorem is proved, the remaining selected applicability boundary becomes

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

## Claim firewall

This audit does not establish:

- a characteristic-two version of Sakamoto Lemma 5.2, Corollary 5.5, Lemma 6.4, or Theorem 6.7;
- residual coisotropy for every selected `BSD-R2-A1` curve;
- minimal-core or full core-graph connectivity at literal `p=2`;
- BSS Theorem 5.20, Theorem 5.2, Theorem 5.25, or integral Fitting control at literal `p=2`;
- R5-LIFT or R5-PRIM;
- `BSD-R2-A1`;
- literature exhaustiveness;
- novelty, priority, or MATHCERT certification.
