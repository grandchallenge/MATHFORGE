# OAI-26 F003 — classical finite-order Hecke/ray-character bridge and exact finite witnesses

**Assignment:** `GCL-OAI26-F003-HECKE-CLASSICAL-RAY-DICTIONARY/1`  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Previous protected formal scope and replay:** [F003 Hecke #145 statement review](WP03_FAMILY003_HECKE_145_FORMAL_SCOPE_CORRECTION.md); [F003 zeta #199 recovered dual replay](WP01_F003_ZETA199_RECOVERED_DUAL_REPLAY.md); source-locked [WP05 portfolio](WP05_CANONICAL_372_FAMILY_VERDICTS.json).  
**Disposition:** `CLASSICAL_RAY_CLASS_REDUCTION_EXPLICIT__FORMAL_STANDARD_HECKE_EQUIVALENCE_UNPROVED`. This is a mathematical correspondence argument, not an additional verified analytic zero-free theorem.

## A precise mathematical reduction

Let `K=Q(ζ₃)`, `O=Z[ζ₃]`, and let `𝔪⊂O` be a nonzero integral modulus. The imaginary quadratic ring `O` is Euclidean for the norm, hence its ideal class group is trivial. There are no real places and therefore no narrow-sign constraints. The standard ray-class exact sequence for finite moduli reduces to

```text
Oˣ → (O/𝔪)ˣ → Cl_𝔪(K) → Cl(K) → 1,
                                   Cl(K)=1.
```

Thus the ray-class group is isomorphic to the quotient `(O/𝔪)ˣ / image(Oˣ)`. Its finite-order complex character group is the group of characters of `(O/𝔪)ˣ` that are **trivial on the image of global units**.

Every continuous finite-order Hecke idele-class character is trivial on the connected complex archimedean component, factors through a finite ray class group for some conductor, and is therefore represented by residue data for some `𝔪`. Conversely, a unit-trivial residue character produces a finite-order ideal character on ideals coprime to `𝔪`, extended by zero on noncoprime integral ideals. This is the standard character-theoretic reason for the `unit_trivial` field.

### Correspondence with exact pinned definitions

The upstream `lean/OAI/NumberTheory/DirichletL/Hecke/Family.lean` (Git blob `3d87da47cd57f0a4f11859c654e3e3202a519100`) defines `K := CyclotomicField 3 ℚ`, `O := RingOfIntegers K`, and

```lean
structure Character where
  modulus : Ideal O
  modulus_ne_bot : modulus ≠ ⊥
  residue : MulChar (O ⧸ modulus) ℂ
  unit_trivial : ∀ u : Oˣ, residue (Ideal.Quotient.mk modulus (u : O)) = 1
  period : ℕ
  period_pos : 0 < period
  period_mem : (period : O) ∈ modulus
```

The `Character.ofResidue` constructor produces the period field using the cardinality of the finite quotient. This auxiliary period changes how the lattice sums are written; it is **not** a second independent Hecke character parameter.

The upstream `lean/OAI/NumberTheory/DirichletL/RayOrthogonality.lean` has a specific bridge:

```lean
abbrev rayCharacters := characters (globalUnits M)
theorem mem_rayCharacters_iff (χ : MulChar (A ⧸ M) ℂ) :
  χ ∈ rayCharacters M ↔ IdealCharacter.UnitInvariant M χ
```

And `lean/OAI/NumberTheory/DirichletL/Hecke/RayFamily.lean` (blob `5d7d3f9ca263d8165393e4b35b3c4dc1354565f7`) defines `character (χ : rayCharacters M) := Character.ofResidue M ... χ.val ...`, and proves exact agreement of its ideal coefficients with `RayOrthogonality.idealCharacter`. The PID instance is explicitly `IsCyclotomicExtension.Rat.three_pid K`. These are strong **internal** model bridges, but the complete comparison to a separately defined standard Hecke idele-class character has not been compiled as a theorem.

### Analytic identification and its precise proof obligation

The upstream `lean/OAI/NumberTheory/DirichletL/Hecke/IdealBridge.lean` (blob `bcb15758326db111dd0b007b79a58103a4fa659e`) proves, for `Re(s)>1`,

```lean
theorem LFunction_eq_ideal_tsum (χ : Character) {s : ℂ} (hs : 1 < s.re) :
  LFunction χ s = ∑' I : Ideal O, idealTerm χ s I
```

where `idealTerm` is the ideal-character coefficient divided by `N(I)^s`. The proof identifies the coordinate lattice sum with **six times** the ideal Dirichlet series, using the six units of `O`, then divides by six. This factor is essential: forgetting it would change the analytic function's normalization (though not its zeros).

Consequently, for a standard finite-order Hecke character `ψ` represented by `χ` under the ray-class dictionary, the standard Hecke `L(s,ψ)` and the formal `HeckeFamily.LFunction χ s` have the **same absolutely convergent ideal series** for `Re(s)>1`. If both are given their usual meromorphic continuations on a common connected domain, the identity theorem extends equality to that domain; at a principal pole `s=1`, the nonvanishing theorem explicitly excludes the pole. In particular, choosing an imprimitive modulus only removes finitely many Euler factors, and one must compare the *same* imprimitive Hecke L-function, not silently substitute the primitive one.

This proves a **classical conditional dictionary** using the standard ray-class correspondence, analytic continuation and uniqueness. It does **not** independently prove that the standard ray-class correspondence and analytic continuation assumptions are encoded and checked by the upstream formal theorem: the exact Lean proof objects mapping *all* traditionally formulated finite-order Hecke characters into `HeckeFamily.Character` and transporting their global analytic L-functions have not been identified.

## Exact-rational finite quotient adversary

The independent [finite-character witness](f003_ray_character_finite_witness.py) is standalone Python with no Lean dependencies. For positive integer moduli `𝔪=(n)`, enumerate `O/(n)` as pairs `a+bω`, with multiplication `ω²=-ω-1`. Its unit criterion is `gcd(a²-ab+b²,n)=1`. The global units are `±1, ±ω, ±(1+ω)`; their image has six elements except for small quotient collisions.

| `n` | Unit count in `(O/(n))ˣ` | Global-unit image | Ray character count |
| ---: | ---: | ---: | ---: |
| 2 | 3 | 3 | 1 |
| 3 | 6 | 6 | 1 |
| 5 | 24 | 6 | 4 |
| 7 | 36 | 6 | 6 |
| 11 | 120 | 6 | 20 |

The count is the order of the quotient group `(O/(n))ˣ / image(Oˣ)`, which also equals the number of complex characters of that finite abelian quotient. A hostile case deliberately **drops** the global-unit-trivial condition at `n=5`: it would produce 24 instead of four candidate characters and is rejected. This independently demonstrates why the source's unit-trivial condition is mathematically necessary. It does **not** establish the ray-class theorem for arbitrary ideals or any nonvanishing estimate.

## Referee boundary and actionable next formal target

The standard mathematics supplies a clear route from the Lean *residue-character presentation* to ordinary finite-order Hecke L-functions over the Eisenstein field. The source now explicitly formalizes several **internal** legs of this route, including the finite quotient characters, ideal coefficients and equality with the ideal Dirichlet series in the convergent half-plane. The remaining external semantic bridge has two separate obligations:

1. Provide a theorem-level equivalence or surjection from **standard finite-order Hecke characters**, with conductor and infinity-type conventions, onto the represented `RayOrthogonality.rayCharacters`/formal `Character` data (modulus possibly enlarged), with equality of integral-ideal coefficients.
2. Establish an exact theorem relating the formal `HeckeFamily.LFunction` analytic continuation to the independently specified classical Hecke L-function, not merely their common half-plane Dirichlet series, including imprimitive Euler factors and the principal pole convention.

Neither step is an additional seven-eighths **analytic inequality**: both are *model fidelity* statements. Even if these bridges are proved, the extraordinary seven-eighths analytic proof warrants separate independent mathematical scrutiny of the 7,061-module energy/detector chain and the manuscript's claim of novelty.

**Conclusion:** `CLASSICAL_RAY_CLASS_REDUCTION_EXPLICIT__FORMAL_STANDARD_HECKE_EQUIVALENCE_UNPROVED`; no counterexample found in finite residue models, no MATHCERT certification, and no promotion of the entire Family 003 to `VERIFIED_WITHIN_EXPLICIT_SCOPE`. Reuse already verified index145 Hecke and index199 zeta Lean+Comparator receipts rather than repeating expensive runs.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-F003-CLASSICAL-RAY-HEKE-BRIDGE
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: CLASSICAL_RAY_CLASS_REDUCTION_EXPLICIT__FORMAL_STANDARD_HECKE_EQUIVALENCE_UNPROVED
EVIDENCE: Family.lean 3d87da47cd57f0a4f11859c654e3e3202a519100; RayFamily.lean 5d7d3f9ca263d8165393e4b35b3c4dc1354565f7; IdealBridge.lean bcb15758326db111dd0b007b79a58103a4fa659e; existing corpus indexed 145/199 technical receipts
REPLAY: FINITE_INTEGER_MODULI_2_3_5_7_11_EXACT_UNIT_QUOTIENTS; HOSTILE_UNIT_OMISSION_DETECTED; HISTORICAL_LEAN_AND_COMPARATOR_REUSED
UNRESOLVED: standard finite-order Hecke character type/conductor equivalence; global analytic continuation equality; independent analytic proof validity
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
