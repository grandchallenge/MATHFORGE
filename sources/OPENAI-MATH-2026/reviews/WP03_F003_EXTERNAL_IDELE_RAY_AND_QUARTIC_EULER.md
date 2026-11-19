# OAI-26 F003 — external finite-idèle ray reduction and quartic Euler-factor adversary

**Exact upstream source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Exact pinned mathlib:** `leanprover-community/mathlib4@d13f23b723b8a846827a245b89c10fc7d3f11612`.  
**Protected independent character proof:** [PR #568](https://github.com/grandchallenge/MATHFORGE/pull/568), `F003IndependentRayQuotient.lean`, protected `main@2f4f550fca0c44758f5b6f3477ab1a2783f8c230`.  
**Bounded adversary:** [f003_quartic_ray_euler_adversary.py](f003_quartic_ray_euler_adversary.py).  
**Result:** `F003_CLASSICAL_FINITE_IDELE_TO_RAY_REDUCTION_PROVED_ON_PAPER__FINITE_EULER_ADVERSARY_PASS__FORMAL_IDELE_AND_GLOBAL_L_FUNCTION_EQ_OPEN`.

## 1. The standard finite-order Hecke-character theorem

**Theorem (classical finite-order dictionary for the Eisenstein field).** Let `K=ℚ(ω)`, `ω²+ω+1=0`, `O=ℤ[ω]`, and let `ψ:C_K=𝔸_Kˣ/Kˣ → ℂˣ` be a **continuous finite-order** idèle-class character. Then `ψ` has some nonzero integral conductor modulus `𝔪`, trivial archimedean component and an associated finite character
`ρ:(O/𝔪)ˣ/image(Oˣ)→ℂˣ`. It is uniquely determined by `ψ` *at its chosen conductor and the canonical ray-class isomorphism*. For each integral ideal `I` coprime to `𝔪`, the corresponding ideal character is

```text
a_ψ(I) = ρ([a mod 𝔪])  if I=(a),
a_ψ(I) = 0              if gcd(I,𝔪)≠1.
```

This coefficient is independent of the generator `a`, since two generators differ by a global unit. Consequently the standard **imprimitive-at-𝔪** Hecke L-series is

```text
L_𝔪(ψ,s)= Σ_{I⊂O nonzero} a_ψ(I)·N(I)^(−s),
                                    Re(s)>1.
```

This is the classical theorem; the present note supplies its argument and relates it to exact pinned formal definitions. It **does not** claim the theorem is independently formalized for idèles in the pinned Lean environment.

**Proof.** (a) The connected group `K_∞ˣ=ℂˣ` maps continuously into the finite subgroup `im ψ`, which is discrete. Its image is therefore connected and finite, hence `{1}`. Thus no nontrivial infinity-type (including angular phase type) can occur for **finite-order continuous** characters.

(b) The restricted product topology on the finite idèles and continuity of `ψ` with finite image imply that `ker ψ` contains an open compact product subgroup `U(𝔪)`. At all but finitely many finite places `𝔭` this contains the full unit group `O_𝔭ˣ); at the exceptional places some sufficiently deep principal congruence subgroup `1+𝔭^{e_𝔭}O_𝔭` lies in the kernel. Taking `𝔪=∏𝔭^{e_𝔭}` gives `U(𝔪) ⊆ ker ψ`. This is precisely the finite conductor step. The conductor may be chosen minimal at each local place.

(c) The idelic ray-class identification gives
`C_K/(K_∞ˣ U(𝔪)) ≅ Cl_𝔪(K)`. Because the norm on `ℤ[ω]` is Euclidean, every fractional ideal is principal and the ordinary ideal class group `Cl(K)` vanishes. The exact ray-class sequence

```text
Oˣ → (O/𝔪)ˣ → Cl_𝔪(K) → Cl(K) → 1
```

therefore identifies `Cl_𝔪(K) ≅ (O/𝔪)ˣ / image(Oˣ)`. Hence `ψ` factors through a finite character `ρ` of the latter quotient. Since the field has no real embeddings, no narrow positivity signs enter.

(d) If a coprime ideal has two generators `a,b`, then `b=ua` for some `u∈Oˣ`. Their residues differ by `image(u)`, killed in the quotient, so the coefficient is well-defined. Multiplicativity follows from the multiplicative quotient map. For ideals not coprime to `𝔪`, the imprimitive convention is coefficient zero. `|a_ψ(I)|≤1` and `∑_{I≠0}N(I)^{−σ}=ζ_K(σ)<∞` for `σ>1`; absolute convergence of the displayed L-series follows. ∎

**What is new to GCL:** the theorem above is standard class-field/ray-class mathematics, not claimed as an original theorem. The added source-independent Lean proof in protected PR #568 formally verifies the **abstract final quotient/character equivalence** for every commutative monoid and unit subgroup, without the OAI Hecke implementation. The idelic class-field reduction in (b,c) is *still a traditional proof argument, not an imported Lean theorem*, and the analytic continuation is *not a new independent formal equivalence with a separately defined external Hecke L-function*.

## 2. The analytic comparison and the precise imprimitive caveat

The source-locked upstream `lean/OAI/NumberTheory/DirichletL/Hecke/RayFamily.lean` defines `character M ρ` and proves `idealCoeff_character` (the ideal coefficient equality). The upstream `Hecke/IdealBridge.lean` proves that its analytic `HeckeFamily.LFunction` equals the same ideal series on `Re(s)>1`; the protected [F003 three-lemma Lean bridge PR #567](https://github.com/grandchallenge/MATHFORGE/pull/567) additionally proves arbitrary valid lattice-period independence and source-internal continued-L equality.

If a standard externally specified Hecke L-function admits meromorphic continuation on a connected domain covering `Re(s)>1` and the target `Re(s)>7/8`, equality of the half-plane series gives equality of those continuations by the meromorphic identity theorem. That last clause is the **remaining formal semantics obligation**: supply the external idèle-character representation and analytic continuation in a pinned, independently interpreted model, and prove the actual map/equality there. Merely reusing the OAI `LFunction` as the "external" function would be circular.

**Imprimitive warning.** Suppose `𝔪₀ | 𝔪` and a character of conductor `𝔪₀` is instead represented modulo larger `𝔪`. The `𝔪`-series omits Euler factors for the new prime divisors of `𝔪/𝔪₀`:

```text
L_𝔪(ψ,s)=L_𝔪₀(ψ,s) · ∏_{𝔭 | 𝔪, 𝔭 ∤ 𝔪₀} (1−a_ψ(𝔭)·N𝔭^(−s)).
```

For `Re(s)>0`, each added factor is nonzero because `|a_ψ(𝔭)N𝔭^{−s}| = N𝔭^{−Re(s)} <1`. This establishes equality of zero sets on that half-plane **away from poles** for primitive and induced imprimitive conventions, but NOT equality of the analytic functions themselves. The same distinction applies to the principal character: its imprimitive L-function is `ζ_K(s)` times finitely many deletion factors, and has a pole at `s=1`.

## 3. Exact quartic adversary at modulus 5

The independent executable enumerates the finite field `O/(5)≅𝔽₂₅` as pairs `a+bω` and uses exact integer arithmetic for `ω²=−ω−1`. The pair `g=1+3ω` has multiplicative order 24. The image of `Oˣ={±1,±ω,±(1+ω)}` is the subgroup `⟨g⁴⟩` of order six. The ray quotient is cyclic of order four. Set `χ(g^k)=i^k` and `χ(0)=0`; the global-unit image is killed and nonunits are zero.

The script checks **all 625 ordered residue pairs** for multiplicativity, all 150 combinations of residue and global unit for invariance, and generator-choice invariance for representatives of inert, ramified and split prime ideals. The exact values are:

| Prime ideal generator | Ideal norm | Quartic `χ` |
| --- | ---: | --- |
| `2` (inert) | 4 | `−1` |
| `1−ω` (ramified over 3) | 3 | `−i` |
| `3+ω` (split over 7) | 7 | `i` |
| `2−ω` (conjugate over 7) | 7 | `i` |
| `5` (excluded conductor ideal) | 25 | `0` |

Checks use `(1−ω)²=−3ω` and `(3+ω)(2−ω)=7`, including the unit-invariance explanation for the coefficients at rational integers 3 and 7. The output distinguishes a prime norm of 4 from rational prime 2, a recurrent Euler-product normalization hazard.

**Concrete deletion:** inducing this character from modulus 5 to modulus 10 removes the inert prime `(2)`, whose local Euler series is
`1−X+X²−⋯ = (1+X)^{−1}` with `X=4^{−s}`. The induced factor is `1` and

```text
L₁₀(χ,s) = (1+4^(−s)) · L₅(χ,s)
```

on their common meromorphic domain, using the appropriate primitive/imprimitive conventions. The script validates polynomial coefficient cancellation through degree 30 and that `χ(2)=−1`. It also rejects (i) treating all 24 residue-unit characters as unit-trivial (only four descend) and (ii) falsely splitting the inert prime 5 into norm-five factors.

**Observed exact local execution:** `F003_QUARTIC_CHARACTER_AND_EULER_ADVERSARY_PASS`. The candidate source SHA-256 is `8eba90f71e21d2cdf605ee94e8f4ab142b6a7e46f82c0dec2c4ed4032e1a2a51`. This validates exact finite examples and Euler algebra; it is not itself a global analytic theorem or a Lean proof.

## 4. Scientific and governance boundary

The following distinct claims must not be conflated:

1. **Source-independent universal quotient-unit character equivalence** — Lean-checked and protected in PR #568.
2. **Classical finite-order idèle-to-ray reduction for K=Q(ζ₃)** — explicit standard mathematical proof supplied above; not yet separately formalized in pinned Lean.
3. **Exact source-internal analytic L-function vs its ideal series** — Lean checked in existing upstream, with explicit period/character lemmas protected in PR #567.
4. **Cross-implementation analytic continuation equivalence** — still open, requiring a separately defined external standard L-function and conductor and pole conventions.
5. **Validity of the extraordinary seven-eighths zero-free analytic estimate** — still open to independent source-level proof criticism; no source-model correspondence can by itself establish this.

**Verdict:** `CLASSICAL_IDELE_RAY_PROOF_ARGUMENT_AND_EXACT_QUARTIC_EULER_MODEL_PASS__FORMAL_IDELE_AND_ANALYTIC_EQUIVALENCE_OPEN`.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI26-F003-EXTERNAL-FINITE-IDELE-AND-QUARTIC-EULER-001
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: CLASSICAL_IDELE_RAY_REDUCTION_ON_PAPER__QUARTIC_EULER_ADVERSARY_PASS__FORMAL_EXTERNAL_L_EQUIVALENCE_OPEN
EVIDENCE: F003IndependentRayQuotient.lean protected main 2f4f550fca0c44758f5b6f3477ab1a2783f8c230; f003_quartic_ray_euler_adversary.py SHA256 8eba90f71e21d2cdf605ee94e8f4ab142b6a7e46f82c0dec2c4ed4032e1a2a51
REPLAY: EXACT_CHARACTER_625_PRODUCTS_PASS; UNIT_150_ACTIONS_PASS; NORM_AND_EULER_DELETION_DEGREE30_PASS; TWO_HOSTILE_CASES_REJECTED
UNRESOLVED: idèle-class-to-ray formal theorem; independent standard Hecke L-function analytic continuation equality; unconditional seven-eighths analytic estimates
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
