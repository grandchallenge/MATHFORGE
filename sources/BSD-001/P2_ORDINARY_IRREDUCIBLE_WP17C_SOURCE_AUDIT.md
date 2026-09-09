# BSD-001 source audit — `p=2` ordinary irreducible-residual screen

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#146`.
- Protected Forge baseline: `b41df439902f15de69a851e48f3526a6ee90758a`.
- Downstream protected MATHSOLVE baseline: `988462b215853317f7719f5795f807e12b49550b`.
- Disposition: `QUALIFIED_P2_ORDINARY_IRREDUCIBLE_SOURCE_GAP`.
- Claim class: bounded source/applicability evidence only; no theorem-nonexistence, BSD, or certification promotion.

## Exact downstream target

Protected WP16B fixes

`T_E := Tor_{Z_2}(Sel_{2^infinity}^{Kum}(E/Q)^vee)`

and proves exactly

`Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

Protected WP08 and WP17B identify the cyclotomic height-one `(2)` / relative-`mu` component as the unresolved integral piece in the Kato ordinary lane.

Protected WP12 places every selected curve in the residual branch

`E[2]` irreducible with image `GL_2(F_2) ~= S_3`.

This audit asks whether the strongest nearby `p=2` results actually reach that branch.

# Source A — Bertolini–Longo–Venerucci anticyclotomic main conjectures

## Primary source

Massimo Bertolini, Matteo Longo, Rodolfo Venerucci, *The anticyclotomic main conjectures for elliptic curves*, arXiv:`2306.17784v2` (5 February 2026), subsequently published in *Mathematische Annalen* (2026).

The abstract says that the paper treats rational elliptic curves over anticyclotomic extensions when `p` is good ordinary or supersingular. The operative hypotheses are narrower.

Hypothesis 1.1(1) states:

`The rational prime p is >= 5 and does not divide N.`

Remark 1.2 then explains that `p` is assumed odd as customary and, to quote the needed literature, the paper requires `p > 3`.

**Locator:** Hypothesis 1.1 and Remark 1.2, arXiv v2 printed pp.2–3.

Therefore the 2026 anticyclotomic main-conjecture theorem is not a selected `p=2` theorem. Its general theorem shape is highly relevant to the protected WP09 imaginary-quadratic arena, but it cannot be specialized to `p=2` by deleting Hypothesis 1.1(1).

**Disposition:** `ANTICYCLOTOMIC_MAIN_CONJECTURE_P_GE_5`.

# Source B — Kramer nonzero `mu_2` families

## Primary source

Kenneth Kramer, *Elliptic curves with non-trivial 2-adic Iwasawa mu-invariant*, Acta Arithmetica 90 (1999), 173–182, DOI `10.4064/aa-90-2-173-182`.

Kramer recalls Greenberg's criterion: if `E` admits a rational cyclic isogeny

`phi_n : E -> E'`

of degree `2^n` whose kernel satisfies specified local conditions at `2` and infinity, then the 2-adic Iwasawa invariant satisfies

`mu_2(E) >= n`.

Kramer constructs semistable families using rational points on `X_0(2^n)` for `1 <= n <= 4`.

A rational cyclic `2^n`-isogeny has a Galois-stable cyclic kernel. Its unique subgroup of order `2` is therefore Galois-stable. Consequently `E[2]` contains a one-dimensional `F_2` Galois submodule: the residual representation is reducible.

Hence Kramer's positive nonzero-`mu_2` constructions demonstrate that the height-one `(2)` contribution is genuine, but they do not produce a counterexample in the protected WP12 irreducible/surjective `S_3` branch.

**Disposition:** `NONZERO_MU2_CONSTRUCTION_RESIDUALLY_REDUCIBLE`.

# Source C — Lin–Yin 2026 `Z_2`-extension mu work

## Public source status

Zichao Lin, joint work with Mulun Yin, public seminar abstract: *On Iwasawa mu-invariants for Selmer groups over Z_2-extensions*, Morningside Center of Mathematics, 23 July 2026.

The public abstract assumes from the outset that `E[p]` is reducible as a `G_Q`-representation. It then focuses on `p=2`, gives an upper-bound result for `mu`, and states a classification of `mu=0` or `1` under the additional assumption that `E[4]` is reducible.

No primary preprint containing a theorem statement was identified in this bounded screen. Accordingly this record uses the seminar abstract only as current reconnaissance; it does not promote an unpublished theorem beyond the words of that abstract.

The explicit reducibility assumption places this work outside the selected WP12 `S_3` branch.

**Disposition:** `CURRENT_P2_MU_RECONNAISSANCE_REDUCIBLE_BRANCH_ONLY`.

# Source D — Chakravarthy irreducible-residual mu work

## Primary source

Adithya Chakravarthy, *The Iwasawa mu-invariants of Elliptic Curves over Q*, arXiv:`2408.07826v2`.

The paper states Greenberg's `mu=0` conjecture in the form:

- `p` is an **odd** prime of good ordinary reduction;
- `E[p]` is irreducible;
- conjecturally `mu(E)=0`.

The current arXiv v2 explicitly records that the previous claim of `mu=0` for almost all primes contained a mistake. The corrected abstract/result is only

`mu <= 1 for all but finitely many good ordinary primes p`.

This asymptotic theorem concerns variation over primes and does not furnish a theorem at the fixed selected prime `p=2`. More importantly, the irreducible-residual Greenberg conjecture invoked in the paper is itself stated for odd `p`.

**Disposition:** `IRREDUCIBLE_RESIDUAL_MU_THEORY_ODD_P_NOT_SELECTED_P2`.

# Source E — Deng–Li finite-layer `Z_2` Mazur–Tate work

## Primary source

Li-Tong Deng and Yong-Xiong Li, *Elliptic curves with rank one and nontrivial 2-part of Tate Shafarevich groups over the Z_2-extension of Q*, arXiv:`2603.14234` (March 2026).

This paper is materially relevant because it works integrally over the cyclotomic `Z_2`-tower and uses finite-layer Mazur–Tate elements, Heegner-point congruences, and an equivariant Coates–Wiles argument.

Its chosen base elliptic curve, however, has conductor `243`, satisfies `a_2=0`, and has good **supersingular** reduction at `2`. The main result constructs an explicit curve/twist family with rank-one behavior over the tower and infinite 2-primary Tate–Shafarevich group over `Q_infinity`.

The paper is therefore evidence that genuinely integral finite-layer methods at `p=2` are viable. It does not state a uniform primitive-Kummer Fitting theorem for arbitrary good-ordinary selected curves, and its local condition belongs to the supersingular branch rather than WP16B's selected ordinary setting.

**Disposition:** `P2_FINITE_LAYER_METHOD_POSITIVE_SUPERSINGULAR_WRONG_LOCAL_BRANCH`.

# Joint diagnosis

The screened source classes separate cleanly:

1. **Selected residual branch:** `E[2]` is two-dimensional irreducible/surjective `S_3`.
2. **Known positive nonzero-mu constructions:** Kramer uses rational `2^n`-isogenies and hence reducible `E[2]`.
3. **Current 2026 p=2 mu classification reconnaissance:** Lin–Yin explicitly assumes reducible `E[2]` and additionally reducible `E[4]` for its stated classification.
4. **Irreducible-residual mu=0 programme:** Chakravarthy's formulation of Greenberg's conjecture remains an odd-prime statement; its corrected v2 does not determine the fixed `p=2` selected invariant.
5. **Closest anticyclotomic full main conjecture:** Bertolini–Longo–Venerucci requires `p >= 5`.
6. **Direct finite-layer p=2 technology:** Deng–Li demonstrates a live Mazur–Tate/Heegner route but on the supersingular branch and as an existence/family result, not a uniform selected Fitting theorem.

Thus none of these screened interfaces proves either

`mu_2(selected E)=0`

or the stronger exact identity needed for

`Fitt^0_{Z_2}(T_E)`.

This does **not** establish that a theorem does not exist. It establishes that the named plausible bypasses screened here do not supply it.

## Source-level frontier

The bounded source debt is now:

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

There are two substantively different ways forward:

1. prove or find literal `p=2` height-one `(2)` / `mu` control on the selected irreducible/surjective branch, followed by the exact WP16B local/specialization comparisons; or
2. bypass cyclotomic `mu` and construct a finite-level primitive Kummer/Mazur–Tate/determinant theorem directly for the WP16B invariant.

The second route is now especially worth experimental reconnaissance because Deng–Li shows that finite-layer integral `p=2` Mazur–Tate methods are technically viable, even though their theorem is supersingular and non-uniform.

## WP18 implication

WP18 can now test selected good-ordinary `S_3` curves directly. The diagnostic questions should include:

- observed `mu_2` and `lambda_2` where rigorous database computations exist;
- stabilization of `s_n(E)` where finite Selmer data can be obtained;
- primitive Mazur–Tate element valuations at finite `2`-power layers;
- whether any discrepancy correlates with WP13 even-Tamagawa/residual-conductor-drop data;
- whether the finite-layer analytic element appears to encode `Fitt^0(T_E)` without first solving the cyclotomic height-one `(2)` problem.

Any such computation remains observation, not proof.

## Claim firewall

This audit does not prove:

- `mu_2=0` for irreducible or surjective `E[2]`;
- existence or nonexistence of a missing `p=2` theorem;
- equality between ordinary/Greenberg and primitive Kummer local conditions;
- primitive/imprimitive Tamagawa comparison;
- a finite-layer Mazur–Tate Fitting identity in the selected class;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
