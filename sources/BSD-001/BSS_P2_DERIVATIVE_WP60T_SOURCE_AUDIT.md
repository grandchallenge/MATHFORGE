# BSD-001 source audit — BSS Theorem 6.12 derivative interface at literal `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#217`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#250` (`BSD-WP60T`).
- Initial protected MATHFORGE base: `da746ee38823e408321b9e417649f5b837ec5627`.
- Initial protected provider admission: `637c842c90c51bc3a832862c5bff7e68659fdcad`.
- Constitutional authority at issuance: `grandchallenge/INTELLECT@f042220f3bed7cb7b5069256e8f6305c850c0628`.
- Protected finite BSS replay authority: `grandchallenge/MATHSOLVE@245860ce3d7307a505e48b4165be0850327f996a` (WP60R).
- Protected inverse-limit completion authority: `grandchallenge/MATHSOLVE@b0854bb7770296b610b655753bc62b27365b27bb` (WP60S completion receipt).
- Primary source A: David Burns, Ryotaro Sakamoto, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448v1.
- Primary source B: Kazuya Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290, DOI `10.24033/ast.639`.
- Prior provider records consumed here:
  - `sources/BSD-001/BSS_P2_CORE_VERTEX_WP60F_SOURCE_AUDIT.md`;
  - `sources/BSD-001/KATO_P2_HEIGHT_ONE_WP17B_SOURCE_AUDIT.md`.
- Claim class: bounded source/dependency admission only. Mathematical replay remains a MATHSOLVE responsibility; mathematical certification remains a MATHCERT responsibility.

## Exact downstream question

Protected WP60F distinguished BSS II Theorem 6.12 from the `p>3` Fitting-control chain but stopped short of admitting Theorem 6.12 at literal `p=2`, because the article introduction summarizes results under an odd-prime convention and the rank-one proof cites Mazur–Rubin.

WP60T requires the exact source-level answer to three questions:

1. Does the operative §6 construction and proof of Theorem 6.12 impose any intrinsic odd-prime condition beyond Hypotheses 6.1, 6.7 and 6.11?
2. If a literal-`2` derivative is constructed, where exactly does the explicit `p>3` assumption in Corollary 6.15 enter?
3. Can the derivative-prime set used in §6.3 be restricted to the exact selected level-`m` auxiliary-prime set already controlled by protected WP60R?

A separate source question is whether Kato supplies an integral Euler-system input at `p=2`, without confusing Euler-system existence with the unavailable height-one-`(2)` main-conjecture divisibility.

## Source A — operative BSS §6 hypotheses

### A1. Section 6 resets the prime variable to an arbitrary prime

BSS II §6.1 begins by fixing a number field `K` and then states: `Let p be a prime number.` It defines the coefficient field over `Q_p`, the Gorenstein order, the representation `T`, and the abelian pro-`p` extension `Kcal/K` in this setup.

This operative section-level setup is broader than the simplified introductory summary, which fixes an odd prime for exposition.

**Disposition:** `BSS_SECTION_6_OPERATIVE_SETUP_ALLOWS_ARBITRARY_PRIME_P`.

### A2. Exact Hypothesis 6.1

BSS Hypothesis 6.1 requires, for every finite `F` in the chosen abelian pro-`p` extension:

1. `H^1(O_{F,S(F)},T)` is reflexive over the corresponding group ring;
2. `H^0(F,T)=0`.

Remark 6.2 states that, because the coefficient order is Gorenstein, the first condition is equivalent to freeness of the same `H^1` group over the coefficient DVR `O`.

No odd-prime condition is added in this statement.

**Disposition:** `BSS_HYPOTHESIS_6_1_HAS_NO_INTRINSIC_ODD_PRIME_CLAUSE`.

### A3. Exact Hypothesis 6.7

BSS Hypothesis 6.7 requires `Kcal` to contain every auxiliary field `K(q)` for `q` outside `S`, together with a `Z_p^d`-extension in which no finite place splits completely. Remark 6.8 identifies this as part of the classical Euler-system field setup.

Section 6.1 separately requires all infinite places of `K` to split completely in `Kcal`. This is part of the mathematical tower-construction obligation; it is not an odd-prime clause in Hypothesis 6.7 itself.

**Disposition:** `BSS_HYPOTHESIS_6_7_HAS_NO_INTRINSIC_ODD_PRIME_CLAUSE`.

### A4. Exact derivative-prime condition and Hypothesis 6.11

In §6.3 BSS defines its derivative prime set `P` by imposing, among other conditions, the rank-one Frobenius quotient

`Acal/(Fr_q-1)Acal ~= R`.

Hypothesis 6.11 then requires

`Fr_q^(p^k)-1`

to be injective on `T` for every `q in P` and every `k>=0`.

The source explicitly says this condition corresponds to an assumption in Mazur–Rubin Theorem 3.2.4. No additional parity condition on `p` is inserted here.

**Disposition:** `BSS_DERIVATIVE_PRIME_INTERFACE_IS_STATED_UNIFORMLY_IN_P`.

## Source A — Theorem 6.12 proof dependency

### A5. Displayed theorem

BSS Theorem 6.12 assumes exactly Hypotheses 6.1, 6.7 and 6.11 and concludes that the constructed derivative family satisfies the finite-singular relation and therefore defines a Kolyvagin system.

Corollary 6.13 packages the construction as the canonical higher Kolyvagin derivative map from Euler systems to Kolyvagin systems.

Neither displayed result adds `p>2`, `p` odd, `p>3`, Hypothesis 3.2(iii), Hypothesis 4.7(iii), or the infinite H3 condition.

**Disposition:** `BSS_THEOREM_6_12_DISPLAYED_DEPENDENCIES_ARE_6_1_6_7_6_11_ONLY`.

### A6. Rank-one proof and the Mazur–Rubin citation

BSS §6.5 states that when `r=1` Theorem 6.12 can be proved using the argument of Mazur–Rubin Theorem 3.2.4; BSS then states that the method of that proof applies in its more general setting. Immediately afterwards BSS says that throughout §6.5 it assumes Hypotheses 6.1, 6.7 and 6.11.

The source therefore uses Mazur–Rubin as a proof method, not as an additional package of unstated running hypotheses. The operative BSS proof section itself specifies the assumptions under which the rank-one argument is being replayed.

The subsequent rank-reduction argument for general `r` is likewise carried out under those three hypotheses.

This source fact resolves the uncertainty retained by WP60F: the §6.5 proof interface does not import an additional intrinsic odd-prime hypothesis merely because the historical rank-one method is attributed to Mazur–Rubin.

**Disposition:** `BSS_612_RANK_ONE_PROOF_IMPORTS_METHOD_NOT_EXTRA_ODD_PRIME_HYPOTHESIS`.

### A7. Scope of this admission

The preceding conclusion does not by itself prove Hypotheses 6.1, 6.7 or 6.11 for the selected elliptic representation. Those are mathematical obligations for WP60T. It also does not assert that every theorem elsewhere in BSS II extends to `p=2`.

In particular, the small-prime localization and core-vertex restrictions in §§3 and 5 remain exactly as recorded by WP60F, except where protected WP60G–WP60R supply selected literal-`2` replacements.

## Source A — Corollary 6.15 and the prime-set interface

### A8. The explicit `p>3` clause belongs to the Fitting-control composition

Corollary 6.15 explicitly assumes `p>3`. Its proof, however, consists of applying Theorem 5.2(ii) and (iii), together with the identity that the initial Kolyvagin component is the Euler-system class.

Thus the source itself localizes the Fitting conclusion to the already-separated Theorem 5.2 control layer. It does not identify the `p>3` clause as an additional requirement of the derivative construction.

Protected MATHSOLVE WP60R has already replayed the selected finite-level Theorem 5.2(ii),(iii) conclusions at literal `2` by replacing the small-prime localization/core-vertex inputs. Whether that protected replacement can be composed with a WP60T derivative remains a downstream theorem question, but no further source-level `p>3` mechanism is hidden in the proof of Corollary 6.15.

**Disposition:** `BSS_COROLLARY_6_15_P_GT_3_DEPENDENCY_IS_THEOREM_5_2_CONTROL_LAYER`.

### A9. Selected `E=F=K=Q` prime-set specialization

Section 3.1.2 defines

`K_M := K(mu_M,(O_K^x)^(1/M)) K(1)`

and the finite auxiliary field

`K(A)_M := K(A) K_M`.

Its prime set consists of primes whose Frobenius in `Gal(K(A)_M/K)` is conjugate to the selected element `tau`. The source immediately records that every such prime splits completely in `K_M` and satisfies

`A/(Fr_q-1)A ~= R`.

Section 6.3 defines the derivative prime set by exactly these two displayed properties for the induced module `Acal`, and explicitly states that this derivative set contains the §3.1.2 set when Hypothesis 3.2(ii) holds for `Acal`.

For the selected BSD application `K=F=Q`. Since `Q` has class number one, `K(1)=Q`; hence the auxiliary choice `E=Q` is allowed in §6.3. With this choice

`Acal = A_F = A = E[2^m]`.

Protected WP60R retains the selected Hypothesis 3.2(ii) rank-one quotient interface at every finite level. Therefore the exact WP60R level-`m` auxiliary-prime set is a subset of the §6.3 derivative-prime set.

BSS Remark 6.16 separately states that, even when the §6.3 set is smaller than the set used for a different induced module `A_F`, the downstream Stark/Kolyvagin theory may be run on any positive-density subset of the derivative set for which the Lemma 3.9-type Chebotarev choice is available. Protected WP60R provides precisely such positive-density localization choices on its exact level-`m` set.

Accordingly, no new literal-`2` localization or core-graph theorem is required merely to compose the derivative with the protected WP60R Theorem 5.2 replacement.

**Disposition:** `BSS_LITERAL_P2_SELECTED_DERIVATIVE_PRIME_SET_COMPATIBLE_WITH_WP60R`.

## Source B — Kato Euler-system existence versus height-one control

### B1. Existing protected provider admission

Protected WP17B already records that Kato's integral theory at `p=2` must be split carefully:

- Kato Theorem 12.6 supplies a concrete integral submodule generated by Kato Euler-system classes;
- Kato's all-height-one main-conjecture divisibility clauses that would control the height-one prime containing `2` require `p != 2` and therefore remain unavailable.

The existence of an integral Euler system and the missing height-one-`(2)` Fitting divisibility are different assertions.

### B2. Consequence for WP60T

The BSS derivative construction consumes an Euler system. It does not require the Euler system to have already established the main-conjecture/Fitting divisibility that the Kolyvagin-system argument is intended to produce.

Accordingly, the admitted Kato integral Euler-system classes can serve as an Euler-system input to a selected literal-`2` BSS derivative replay without importing Kato's unavailable height-one-`(2)` theorem.

This admission does not establish that the resulting Kato-derived Kolyvagin system is a basis or primitive at `(2)`, and it does not compute the cyclotomic `mu` contribution.

**Disposition:** `KATO_LITERAL_P2_EULER_SYSTEM_INPUT_AVAILABLE_WITHOUT_HEIGHT_ONE_2_PROMOTION`.

## Combined provider disposition

The exact source uncertainty retained after WP60F is retired:

`MISSING_SOURCE_AUTHORITY_FOR_LITERAL_P2_BSS_612_DERIVATIVE_DEPENDENCY_SURFACE`

is replaced by the bounded provider interface

`BSS_LITERAL_P2_DERIVATIVE_SOURCE_DEPENDENCIES_ADMITTED`.

The admitted facts are:

1. BSS §6 is formulated for an arbitrary prime `p`;
2. Theorem 6.12 and Corollary 6.13 depend on Hypotheses 6.1, 6.7 and 6.11 only in their operative proof section;
3. the rank-one Mazur–Rubin citation does not add an unstated odd-prime hypothesis to that BSS proof interface;
4. Corollary 6.15's explicit `p>3` dependence is through the Theorem 5.2 Fitting-control layer;
5. for the selected `E=F=K=Q` specialization, the exact WP60R finite-level auxiliary-prime set is an admissible positive-density subset of the §6.3 derivative-prime set;
6. Kato supplies an admitted integral Euler-system input at `p=2`, while height-one-`(2)` divisibility and primitivity remain unavailable.

## Claim firewall

This source audit does **not** establish:

- Hypothesis 6.1 for the selected elliptic representation;
- Hypothesis 6.7 for a particular selected Euler-system tower;
- Hypothesis 6.11 for the selected derivative-prime set;
- BSS Theorem 6.12 or Corollary 6.15 at literal `2`;
- full BSS Hypothesis 3.2(iii), Hypothesis 4.7, Hypothesis 4.7(iii), or infinite H3;
- Kato height-one-`(2)` Fitting divisibility;
- Kato/Kolyvagin primitivity at `(2)`;
- `R5-LIFT`, `R5-PRIM`, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
