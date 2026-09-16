# BSD-001 source audit — Castella–Sano determinant descent and Kato-system primitivity

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#223`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#267` (`BSD R5-PRIM`).
- Protected MATHFORGE entering base: `de2c83c2c440ac357b183b9e1018e9f69c58e1d9`.
- Protected MATHSOLVE R5-LIFT completion: `50308cf34782f14fdb0421beea915311cef20bf3`.
- Constitutional authority: `grandchallenge/INTELLECT@f042220f3bed7cb7b5069256e8f6305c850c0628`.
- Source: Francesc Castella and Takamichi Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, arXiv:2601.14504 (2026), author manuscript `https://web.math.ucsb.edu/~castella/Kurihara.pdf`.
- Source state audited: author manuscript accessed 2026-09-16.
- Claim class: source/dependency architecture only; no literal-`p=2` theorem promotion and no certification.

## Downstream question

Protected MATHSOLVE now proves the literal-`p=2` determinant **membership** statement at the cyclotomic height-one prime `(2)` (`R5-LIFT`). The remaining R5 obligation is **primitivity**:

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Protected WP60A-A1 has reduced this to equality rather than one-sided divisibility. If `z=aP` in the localized rank-one first-cohomology line, then membership is

`v_2(a) >= length(H^2)`,

while determinant-generator status is

`v_2(a) = length(H^2)`.

The present audit asks what the 2026 Castella–Sano proof contributes to this exact distinction and which parts of its proof architecture can be meaningfully replayed after the protected literal-2 replacements.

## 1. The source makes integrality and primitivity separate statements

Section 2.2 reformulates Kato's cyclotomic main conjecture in determinant language. Its Conjecture 2.2.2 asks for a **basis** of the inverse determinant line mapping to the imprimitive Kato zeta class. Proposition 2.2.3 identifies this with equality of characteristic ideals.

Remark 2.2.4 then isolates the upper-bound divisibility: it is exactly the assertion that the inverse image of the Kato zeta class is **integral**, i.e. belongs to the determinant lattice.

This distinction matches the protected downstream split exactly:

- determinant integrality/membership = `R5-LIFT`;
- determinant basis/generator status = `R5-PRIM`.

The source therefore supplies a highly relevant proof architecture for the remaining frontier but does not make primitivity automatic from integrality.

**Source disposition:** `EXACT_INTEGRALITY_VS_BASIS_SPLIT`.

## 2. Proposition 2.3.1 is a determinant descent calculation

For a cyclotomic character specialization `alpha` sufficiently close to the trivial character and with nonzero specialized first Kato component, Proposition 2.3.1 identifies the image of the specialized inverse determinant lattice in rank-one cohomology.

The proof proceeds by:

1. a rank-one/finite-dual-Selmer consequence of Mazur–Rubin's Kolyvagin-system structure theorem;
2. Poitou–Tate duality;
3. local Tate duality;
4. an exact determinant calculation of `H^1` against finite `H^2` and the strict dual Selmer group.

The resulting lattice is the cohomology line multiplied by an explicit finite factor built from local `p`-power torsion and the strict dual Selmer order.

Corollary 2.3.2 then compares a determinant **basis** with the Kato first component and Euler factors to obtain an exact divisibility-index formula.

The determinant manipulation and Poitou–Tate/local-duality calculation are not, by themselves, a source of an additional odd-prime restriction. The source is globally written for odd `p`, and the rank-one/strict-Selmer input it invokes comes from an odd-prime Mazur–Rubin theorem; literal-2 applicability therefore still requires an independent replay.

For downstream R5-PRIM, this is a proof architecture, not a theorem interface.

**Source disposition:** `DETERMINANT_DESCENT_ARCHITECTURE_RELEVANT_P2_REPLAY_REQUIRED`.

## 3. Kato Kolyvagin systems and the exact primitivity index

Section 2.1 constructs Kato's derived Kolyvagin system `kappa^Kato` and its cyclotomic Lambda-adic analogue. The source defines the minimal divisibility index `M_infty(kappa)` across derivative components.

Theorem 2.1.4 states, for `p>3`, the exact Kolyvagin-structure formula

`length(strict dual Selmer)
 = ind_p(first Kato component) - M_infty(kappa^Kato_Lambda(alpha))`.

This is the key arithmetic separation between the divisibility already forced by the dual Selmer module and **extra divisibility of the Kato Kolyvagin system itself**.

Combining this formula with the determinant descent calculation shows that determinant basis status is equivalent to an exact value of the Kato-system minimal divisibility index after the explicit local factors are accounted for.

In the source's normalization this value is

`M_infty(kappa^Kato_Lambda(alpha))
 = ord_p(#E(Q_p)[p^infinity]) + ord_p(Tam(E))`.

The source then transports this value back to the untwisted Kato system by specialization congruence and rigidity.

This is the most important interface for downstream R5-PRIM: **primitivity is a normalized Kato-Kolyvagin-system divisibility-index equality, not a consequence of rank-one freeness.**

**Source disposition:** `R5_PRIM_REDUCES_TO_NORMALIZED_KATO_KOLYVAGIN_PRIMITIVITY_INDEX`.

## 4. Theorem 2.1.4: source restriction and protected replacement relevance

Theorem 2.1.4 assumes `p>3` and cites Mazur–Rubin Theorem 5.2.12 for the strict-Selmer/divisibility-index formula.

The protected MATHSOLVE literal-2 stack already contains structurally relevant replacements:

- WP60M: selected all-level defect exclusion and coefficient reduction without reinstating false formal H3.2(iii);
- WP60R: literal-2 finite Kolyvagin-system rank-one freeness, core-vertex projection isomorphisms, and Fitting equality for a **basis** Kolyvagin system;
- WP60S: inverse-limit compatibility;
- WP60T: selected literal-2 Kato derivative and first-component identity;
- R5-LIFT: literal-2 determinant membership over the cyclotomic group-ring tower.

These protected results mean the source's `p>3` invocation of the generic Kolyvagin-system structure theorem is not, by itself, a reason to stop the downstream proof. MATHSOLVE can and must replay the exact divisibility-index formula from its already-protected literal-2 interfaces.

This audit does **not** assert that such a replay is automatic or already proved.

**Source disposition:** `MR_STRUCTURE_P_GT_3_IS_A_REPLAY_OBLIGATION_NOT_A_FINAL_SOURCE_BARRIER`.

## 5. Proposition 2.1.5 rigidity: source restriction and protected replacement relevance

Proposition 2.1.5 assumes `p>3` and proves that the minimal divisibility index can be computed after restricting to arbitrarily deep auxiliary-prime sets. Its proof replaces prime factors one at a time using a residual localization prime, Kolyvagin finite-singular relations, global reciprocity, and a nondegenerate local Tate pairing.

The protected MATHSOLVE WP60R theorem was built precisely to replace the characteristic-two localization/core-graph failures of the published odd-prime machinery. It proves selected literal-2 pairwise localization, injective families, dual killing, connected core graphs, and the required finite-singular isomorphisms.

Accordingly, the source's `p>3` rigidity proposition identifies another exact replay obligation rather than an independent final obstruction. The downstream proof must show that the protected WP60R localization package implies the same invariance of the minimal divisibility index on the selected literal-2 auxiliary-prime sets.

**Source disposition:** `RIGIDITY_P_GT_3_REPLAYABLE_IN_PRINCIPLE_FROM_PROTECTED_LOCALIZATION_STACK`.

## 6. Theorem 2.1.3 is a separate analytic bridge

Theorem 2.1.3 assumes `p>3`, residual surjectivity, and `p`-indivisibility of the Manin constant. It gives the explicit-reciprocity comparison between Kato derivative components and Kurihara's modular-symbol quantities `delta_n`, including the local factor `#E(Q_p)[p^infinity]`.

This theorem is used to identify

`M_infty(kappa^Kato)`

with

`M_infty(delta) + ord_p(#E(Q_p)[p^infinity])`,

and hence to rewrite Kato-system primitivity as the refined Kurihara equality

`M_infty(delta)=ord_p(Tam(E))`.

For downstream R5-PRIM this analytic bridge is **optional** if MATHSOLVE proves the normalized Kato-system divisibility-index equality directly. It becomes mandatory only if the proof is routed through Kurihara modular-symbol nonvanishing/refined Kurihara quantities.

No protected source currently authorizes Theorem 2.1.3 at literal `p=2`.

**Source disposition:** `KURIHARA_EXPLICIT_RECIPROCITY_P_GT_3_OPTIONAL_ANALYTIC_BRIDGE`.

## 7. Theorem 2.1.2 supplies nontriviality, not primitivity

Theorem 2.1.2 proves nonvanishing of a sufficiently close nontrivial cyclotomic specialization of the first Kato component using Kato's explicit reciprocity law and Rohrlich nonvanishing.

Even in the source's odd-prime setting, this gives only **nontriviality** of the Kato Kolyvagin system. It does not say that the system is a basis or that its normalized minimal divisibility index has the primitive value.

Downstream MATHSOLVE must therefore not replace R5-PRIM by a bare nonvanishing statement for the first Kato class.

**Source disposition:** `NONTRIVIALITY_STRICTLY_WEAKER_THAN_PRIMITIVITY`.

## 8. How Theorem A proves basis status

Theorem A assumes `p>3` and identifies a refined Kurihara equality with the determinant form of the Iwasawa main conjecture.

In the direction relevant to primitivity, the proof performs the following chain:

1. refined Kurihara equality;
2. explicit reciprocity and rigidity convert it to the exact normalized value of `M_infty(kappa^Kato_Lambda(alpha))`;
3. the Kolyvagin structure theorem converts that to the exact index of the specialized first Kato component;
4. the determinant descent calculation shows that the specialized inverse zeta element is a determinant **basis**;
5. a specialization/basis criterion promotes this to a Lambda-basis of the cyclotomic determinant line.

The source therefore supports the downstream strategy of attacking R5-PRIM through a normalized Kato-Kolyvagin primitivity index, while also showing exactly why determinant membership alone is insufficient.

## 9. Exact downstream source interface

Subject to an independent MATHSOLVE literal-2 replay of the structure and rigidity steps, the source architecture supports the following reduction target:

`R5-PRIM`

is reduced to proving that the protected selected Kato-derived Kolyvagin system has **no extra common factor of `2` beyond the already-explicit local/Selmer determinant factors**.

Equivalently, after transporting the protected local corrections into the exact MATHSOLVE normalization, one must prove the exact normalized minimal-divisibility equality for the Kato system. At finite level, protected WP60R suggests an equivalent formulation: the normalized Kato-derived Kolyvagin system must be a basis of the rank-one selected Kolyvagin-system module, equivalently have a primitive component at a selected core vertex.

The source does not itself prove this literal-2 statement.

Recommended downstream boundary name:

`MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

If downstream elects the modular-symbol route, an additional bridge is required:

`MISSING_P2_KURIHARA_EXPLICIT_RECIPROCITY_REFINED_NONVANISHING_BRIDGE`.

## 10. Source-level applicability disposition

The 2026 Castella–Sano paper materially sharpens the R5-PRIM proof architecture, but its stated theorems are not literal-2 interfaces:

- the paper fixes an odd prime in the Kurihara section;
- Theorems A, 2.1.3, 2.1.4 and Proposition 2.1.5 use `p>3` in the relevant chain;
- Theorem 2.1.3 also assumes the Manin-constant condition;
- determinant main-conjecture Conjecture 2.2.2 is itself stated for odd `p`.

However, two of the three `p>3` proof dependencies — the Kolyvagin structure formula and rigidity/localization mechanism — align directly with theorem families already replayed at literal `2` in protected MATHSOLVE. They must be re-derived from those exact protected interfaces rather than cited from Castella–Sano/Mazur–Rubin.

The remaining independent arithmetic content is the actual normalized Kato-system primitivity equality. The Kurihara explicit-reciprocity theorem is a separate possible witness/route to that equality, not a prerequisite for stating it.

**Disposition:** `QUALIFIED_R5_PRIM_DETERMINANT_DESCENT_ARCHITECTURE_WITH_LITERAL_P2_KATO_PRIMITIVITY_GAP`.

## Claim firewall

This source audit does not establish:

- any literal-`p=2` extension of Castella–Sano, Mazur–Rubin, Kato, Kim, Kurihara, or Burns–Kurihara–Sano;
- `MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`;
- a literal-2 Kurihara explicit reciprocity theorem;
- a literal-2 refined Kurihara theorem;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- MATHCERT certification.

It supplies source architecture and a precise downstream proof obligation only.
