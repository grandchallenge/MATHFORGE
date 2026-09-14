# BSD-001 source audit — BSS minimal-core transition interface for WP60H

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#196`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `7da6813fcde7eb5f9badd7c86946f58691ed6f0d`.
- Protected MATHSOLVE anchor: `1b75a922e2779178f478124948008afdd7e26a17`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source: Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448, §§3.1 and 5.4, especially Definition 5.8, Definition 5.12, Lemmas 5.13–5.15 and Corollary 5.16.
- Disposition: `ADMITTED_BSS_MINIMAL_CORE_TRANSITION_INTERFACE`.
- Claim class: exact source/proof interface only.

## Exact downstream query

Protected MATHSOLVE WP60H reduces the literal-`p=2` four-bad-fiber covering problem to a possible three-term relation among four self-dually identified global cohomology classes.

To test that relation against the actual BSS core-vertex argument, downstream work needs the exact modified-Selmer transition data. This audit admits those facts only. It does not perform the downstream relation exclusion.

## Local finite and transverse conditions

For an auxiliary prime `q in P`, BSS use the finite local condition

`H^1_f(K_q,A)`

and the transverse local condition

`H^1_tr(K_q,A)`.

The finite-singular comparison construction identifies both relevant local pieces with rank-one objects over the coefficient ring. After residual reduction to the field `k`, the finite and transverse local pieces used in §5.4 are one-dimensional `k`-spaces.

For an ideal `n in N`, the modified Selmer structure `F(n)` imposes the transverse local condition at every auxiliary prime dividing `n` and the original Selmer condition at the other places. In particular,

`H^1_{F(n)}(K,A)`

is defined using the quotients by `H^1_tr(K_q,A)` for `q|n`.

The source also uses relaxed and strict variants of the Selmer condition at selected auxiliary primes. The present audit records only the exact inclusions/equalities explicitly invoked in Lemma 5.15 below and does not impose a new notation convention on them.

## Core vertices and dimensions

BSS Definition 5.8 declares `n in N` to be a core vertex when

`H^1_{F^*(n)}(K,A^*(1))=0`.

Writing

`lambda(n)=dim_k H^1_{F(n)}(K,A⊗_R k)`

and

`lambda^*(n)=dim_k H^1_{F^*(n)}(K,(A⊗_R k)^*(1))`,

Corollary 5.6 gives

`r=lambda(n)-lambda^*(n)`.

Hence a core vertex satisfies

`lambda^*(n)=0`

and

`lambda(n)=r`.

Corollary 5.11 proves:

1. a core vertex exists with `nu(n)=lambda^*(1)`;
2. every core vertex has `nu(n)>=lambda^*(1)`.

Thus a core vertex with

`nu(n)=lambda^*(1)`

is minimal with respect to the number of auxiliary prime factors.

## Graph interface

BSS Definition 5.12 defines a graph `X^0` whose vertices are core vertices.

If `n` and `nq` are core vertices, they are joined by an edge exactly when the localization map

`H^1_{F(n)}(K,A⊗k) -> H^1_f(K_q,A⊗k)`

is nonzero.

Lemma 5.13 supplies the two basic one-prime transitions:

1. if `n` is core and the finite localization map above is nonzero, then `nq` is core and the two vertices are adjacent;
2. conversely, if `nq` is core and the transverse localization from `H^1_{F(nq)}` at `q` is nonzero, then `n` is core and the two vertices are adjacent.

Lemma 5.14 proves that whenever both `n` and `nq` are core vertices, there is a path in `X^0` between them, even if the direct edge condition initially vanishes. Its proof invokes one primal and one dual simultaneous localization; protected MATHSOLVE WP60G has separately repaired the literal-`2` counting obstruction for this pairwise step under the remaining BSS hypotheses and self-duality.

## Lemma 5.15 transition data

Let `s` be positive. For each `1<=i<=s`, BSS Lemma 5.15 takes:

- a core vertex `n_i`;
- a prime `q_i|n_i`;
- `m_i:=n_i/q_i`;
- the hypothesis that `m_i` is not a core vertex.

Because `n_i` is core and `m_i` is not, Corollary 5.6 and Lemma 5.10 give exactly

`lambda(m_i)=r+1`

and

`lambda^*(m_i)=1`.

The proof also records the inclusion/equality

`H^1_{F(n_i)}(K,A⊗k)
 subset
 H^1_{F^{q_i}(m_i)}(K,A⊗k)
 =
 H^1_{F(m_i)}(K,A⊗k)`,

where the middle term is the source's relaxed-at-`q_i` modified Selmer condition. The equality is obtained by comparing dimensions through the local exact sequence whose quotient by the transverse condition has dimension one.

The key Chebotarev input in Lemma 5.15 is one prime `r in P`, not dividing any `n_i`, for which, for every `i`, both maps are nonzero:

`H^1_{F(n_i)}(K,A⊗k)
 -> H^1_f(K_r,A⊗k)`

and

`H^1_{F^*(m_i)}(K,(A⊗k)^*(1))
 -> H^1_f(K_r,(A⊗k)^*(1))`.

The source obtains such an `r` from Lemma 3.9 under the numerical condition

`2s<p`.

Since `lambda^*(m_i)=1`, each dual source space in this step is one-dimensional over `k`.

Once the common prime `r` is found, Proposition 5.7 gives

`lambda^*(m_i r)=lambda^*(m_i)-1=0`,

so every `m_i r` is core. Lemma 5.13(i) also makes every `n_i r` core, and Lemma 5.14 then supplies a path from `n_i` to `m_i r=n_i r/q_i`.

This is the exact role of the simultaneous nonvanishing step.

## Minimal-core specialization in Corollary 5.16

Corollary 5.16 takes two core vertices `n_1,n_2` with

`nu(n_1)=nu(n_2)=lambda^*(1)`.

Its proof inducts on

`lambda^*(1)-nu(gcd(n_1,n_2))`.

When the vertices differ, it chooses distinct primes `q_1|n_1` and `q_2|n_2` for the induction step. By minimality and Corollary 5.11, each

`m_i=n_i/q_i`

is not a core vertex.

It then applies Lemma 5.15 with `s=2` to obtain one common prime `r` such that

`n_1 r/q_1`

and

`n_2 r/q_2`

are core and are path-connected to `n_1` and `n_2`, respectively.

The proof uses the resulting equality

`nu(gcd(n_1 r/q_1,n_2 r/q_2))
 = nu(gcd(n_1,n_2))+1`

to close the induction.

Accordingly, the exact literal-`2` obstruction inside this proof is the common-prime simultaneous-localization step for the four source spaces

- `H^1_{F(n_1)}`;
- `H^1_{F^*(m_1)}`;
- `H^1_{F(n_2)}`;
- `H^1_{F^*(m_2)}`.

The source does not state that arbitrary chosen nonzero classes in the two primal spaces must be used; it needs each *localization map from the space* to be nonzero. Thus downstream theorem construction may choose primal witness classes strategically, provided it genuinely proves nonzero localization of each required space.

## Exact provider conclusion

The protected source interface for the WP60H relation test is:

1. minimal cores have `lambda=r`, `lambda^*=0`, and cardinality `lambda^*(1)`;
2. removing one prime from a minimal core gives a noncore `m_i` with `lambda(m_i)=r+1` and `lambda^*(m_i)=1`;
3. Lemma 5.15 needs one common auxiliary prime at which each primal space `H^1_{F(n_i)}` and each one-dimensional dual space `H^1_{F^*(m_i)}` has nonzero finite localization;
4. that common prime converts every `m_i` back to a core and supplies the path moves used by Corollary 5.16;
5. for two minimal cores the source uses `s=2`, hence four simultaneous nonvanishing requirements.

Record the disposition

`ADMITTED_BSS_MINIMAL_CORE_TRANSITION_INTERFACE`.

## Claim firewall

This audit does not establish:

- an absence or presence of a three-term relation among witness classes;
- a canonical choice of primal witness class;
- a matroid or basis-exchange structure on minimal core vertices;
- literal-`p=2` Lemma 5.15 or Corollary 5.16;
- graph connectivity at `p=2`;
- BSS Fitting control at `p=2`;
- BSS Hypothesis 3.2/H2/H3 for the selected elliptic class;
- R5-LIFT, R5-PRIM, `BSD-R2-A1`, or MATHCERT certification;
- literature exhaustiveness, novelty, or priority.
