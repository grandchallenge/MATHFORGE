# OAI-26 F003: independent primitive theta/Hecke functional-equation replication and natural high-stage capacity

**Review:** `GCL-OAI26-F003-THETA-ROOT-AND-NATURAL-HIGHSTAGE/1`  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Independent executable:** [f003_theta_gauss_highstage_adversary.py](f003_theta_gauss_highstage_adversary.py)  
**Disposition:** `F003_MOD5_ALL_NONPRINCIPAL_THETA_FE_PASS__HIGHSTAGE_CAPACITY_RESTRICTION_PROVED__FULL_ANALYTIC_HIGHSTAGE_OPEN`

## 1. Why this is independent and what it tests

The protected [prime-bin audit PR #571](https://github.com/grandchallenge/MATHFORGE/pull/571) derived the contour bound conditional on an absolute primitive L-function strip-growth estimate. The source `Hecke/StripActual.lean` obtains the strip estimate using `Hecke/Primitive.lean`'s completed L-function functional equation, normalized Gauss sum and Phragmén–Lindelöf. Those analytic foundations still need source-independent scrutiny.

This tranche tests **the actual primitive Poisson/theta normalization** using a completely separate explicit finite-field implementation and independent lattice Gaussian sums; it does not import OAI Lean code, its character constructors or any presumed functional equation. The tests are executable using Python 3 and mpmath 1.3.0, and produce exact Gaussian-integer coefficient arithmetic, 100-digit approximate theta values, and a mathematically derived Gaussian-tail majorant. No numerical run on finitely many characters establishes the theorem for all moduli. The downstream energy section reconstructs a rigorous algebraic necessary condition, not the source's complete analytic high-stage proof.

## 2. Derivation of the theta and conductor scales

Let `ω=(-1+i√3)/2`, `O=ℤ[ω]`, `N(a+bω)=a²−ab+b²`, and `c=5`. Then `N((5))=25`, `|c|=5`, and `O/(5)=𝔽₂₅`. A Gaussian theta transform appropriate to the pinned source is

```text
Theta_χ(t) = sum_{a,b in Z} χ(a+bω)
                   exp[-π (2t/(5√3)) (a²−ab+b²)].
```

The normalization `alpha_5(t)=2t/(5√3)` is exactly the specialization of `GaussianTheta.parameter c t=2t/(√3|c|)`. For `Re(s)>1` and nontrivial unit-invariant `χ`, every nonzero principal ideal is represented six times by its six Eisenstein-unit associates; Mellin integration therefore yields

```text
(1/6) int_0^∞ Theta_χ(t) t^(s−1) dt
 = [5√3/(2π)]^s Gamma(s) L(s,χ).
```

The factor `5√3/(2π)=sqrt(3*N((5)))/(2π)` is precisely `Hecke/Strip.completionScale`. This is the degree-one *complex-place* Gamma(s) normalization (the number field has one complex archimedean place), not a product of two independent Gamma(s) factors.

The paper's additive trace character is specified in `TraceCharacter.traceCharacter_eq_paperE` as `paperE(z/c)`. From the embedded Eisenstein coordinates,

```text
paperE((a+bω)/5)=exp(2πi b/5).
```

Gaussian Poisson summation then predicts

```text
Theta_χ(t) = (tau(χ)/(5t)) Theta_(χ^−1)(1/t),
tau(χ) = sum_{a,b mod 5} χ(a+bω) exp(2πi b/5).
```

The prefactor is `tau(χ)/(sqrt(N((5)))*t)`, so the root number `εχ=tau(χ)/5` must have modulus one for a primitive character. The identity for general `χ` is **not assumed or copied into the test**; both finite Gauss coefficients and theta sides are separately evaluated.

## 3. Exact Gauss sums for every nonprincipal ray character modulo 5

The residue `g=1+3ω` has multiplicative order 24 in `𝔽₂₅^×`. The six global units form the subgroup `〈g⁴〉`, giving `𝔽₂₅^× / μ₆ ≅ C₄`. Define `χ(g)=i`. Its three nonprincipal powers `χ,χ²,χ³` exhaust the nonprincipal ray characters modulo `(5)`. Since `(5)` is an inert prime ideal, these nontrivial characters have conductor precisely `(5)`; none factors through the unit modulus.

Summing `χ^k(a+bω)` over `a=0,...,4` for each fixed `b` gives the following **exact Gaussian-integer** rows (in increasing order `b=0,1,2,3,4`):

| Character | b=0 | b=1 | b=2 | b=3 | b=4 |
|---|---|---|---|---|---|
| `χ` | `0` | `2−i` | `−2+i` | `−2+i` | `2−i` |
| `χ²` | `4` | `−1` | `−1` | `−1` | `−1` |
| `χ³` | `0` | `2+i` | `−2−i` | `−2−i` | `2+i` |

For `ζ=e^(2πi/5)`, the classical exact cyclotomic identity is

`ζ+ζ⁻¹−ζ²−ζ⁻²=√5`.

Consequently

```text
tau(χ)   = √5 (2−i),    εχ   = (2−i)/√5,
tau(χ²)  = 5,           εχ²  = 1,
tau(χ³)  = √5 (2+i),    εχ³  = (2+i)/√5.
```

In all three cases `|ε|=1`. These calculations are independent finite arithmetic; the identity `χ^−1=χ³` is checked, rather than presumed from the source.

## 4. Separate lattice-theta evaluation and truncation control

For every `t=1/4,1/2,1,2,4`, the script forms finite theta sums over `|a|,|b|≤R=48`. It groups exact Gaussian-integer coefficients by exact integer norm before evaluating their exponentially decaying weights using 100 decimal digits of working precision. For each ray character, it compares independently calculated

`Theta_χ(t)` and `εχ/t * Theta_(χ^−1)(1/t)`.

It does **not** define one side from the other. Powers `χ²,χ³` additionally run at `t=1/4,1,4`.

There is an explicit analytic bound on omitted lattice terms, not merely a claim that 48 is large enough. Since

`a²−ab+b² ≥ (a²+b²)/2`,

put `c_t=πt/(5√3)`. The union bound for `max(|a|,|b|)>R` gives

```text
tail_R(t) ≤ 4 S_>(R,c_t) S_Z(c_t),

S_>(R,c) ≤ exp(−c(R+1)²)/(1−exp(−c(2R+3))),
S_Z(c) ≤ 1+2 exp(−c)/(1−exp(−3c)).
```

These follow by bounding successive square differences `(n+1)²−n²≥2R+3` above the cutoff and `(n+1)²−n²≥3` for `n≥1`. Therefore the *exact truncation error* in the theta identity is at most

`tail_R(t) + |εχ|/t · tail_R(1/t)`.

In the exact-head replay the **largest observed theta equation residual** was about `5.89×10^(-101)`; the **largest evaluated truncation majorant** over the test points was about `9.42×10^(-94)`. The values are computed with mpmath high precision; **no interval/rounding certification of mpmath** is claimed. The majorant itself follows from an elementary exact inequality; decimal values are approximations.

Hostile tests reject the wrong `tau` vs `tau/5` prefactor and wrong conjugation of the quartic root number. Thus this concretely probes the `sqrt(N((5)))` normalization, signs, complex phase, six-unit multiplicity and `t↔1/t` transformation.

## 5. What this says—and does not say—about the primitive strip estimate

The source chain is:

`TraceCharacter.normalizedGauss` → `GaussianTheta.theta_functional_equation` → `HeckePrimitive.completedL_functional_equation` → `HeckeStripActual.functional_equation_left` → `HeckeStrip.uniform_strip_bound_of_functional_equation` → `HeckeLogarithmicInput.regular_right_growth` → `HeckePrimeDyadicControl.original_disk_control` → `HeckePrimeDyadicBuffered.polynomial_bound_in_bin`.

The independent finite-ray tests independently reproduce the *theta-transform normalization* for `(5)`. They do **not** supply a second formal proof of Poisson summation, the general primitive Gauss transformation for arbitrary conductor, the global analytic continuation or the uniform functional equation.

The conductor exponent in the subsequent strip theorem remains `3/5`, because at `Re(s)=−1/10` the FE completion factor is raised to `Re(1−2s)=6/5`, and completionScale is proportional to `sqrt(Q)`. This algebraic observation was already verified in protected PR #571. The general primitive `Q^(3/5)` bound still depends on the source's genuine uniform Euler/functional-equation/strip-growth inputs.

**Conclusion of this lane:** three nontrivial characters at a fixed inert conductor furnish an unusually strong normalization adversary, but **a finite family is not a proof of universal Hecke analytic claims**.

## 6. Natural high-stage: an exact, narrow but nonempty capacity region

The source `Energy/PositiveHighSourceBound.lean` defines `PositiveHighAt` under two independent inequalities. Write

```text
m = state.width,
x = length Z X1,
y = length Z X2,
w = sum_j slot_weight_j,   w≥0,
κ≥3/4.
```

Then its high-stage preconditions include

```text
x+y+6κw ≤ m,
(5/6)m ≤ x+y+w.
```

Subtracting yields a **necessary restriction for every high-stage configuration**:

```text
(6κ−1)w ≤ m/6,
             w ≤ m/[6(6κ−1)].
```

In particular `w≤m/21` at `κ=3/4`, and `w≤m/30` at `κ=1`. A high-stage input therefore cannot allocate an arbitrary fraction of width to prime slots.

This necessary constraint is not vacuously contradictory: the exact rational values

`m=1, x=y=43/100, w=1/50, 3/4≤κ≤1`

satisfy `x+y+6κw≤1` and `5/6≤x+y+w`; at `κ=1` their left capacity totals `0.98`. A deliberately excessive `w=1/10` fails. **This is an arithmetic witness only.** It does not instantiate all `NaturalState`, conductor, mask, source-profile, `ZeroAt` and `PositiveAt` hypotheses.

### High-stage proof's actual logical dependencies

Pinned `Energy/NaturalHighStage.actual_high_stage` does not directly prove a fresh prime estimate: it composes

- `Energy/PositiveHighSourceBound.actual_high_stage_from_physical`, converting a physical high-mass bound plus a **supplied low-band estimate** into the required positive-high result;
- `Energy/PositiveHighPhysical.actual_positive_high_physical`, which in turn delegates to `Energy/CanonicalHighPhysical.actual_high_physical`, then multiple left/right source-column estimates and positive/zero child bounds;
- stage-loss and width gates to select a common exponent budget.

Inspecting the quantifiers is essential: it constructs **shared finite seminorm indices** `U` and a shared polynomial-height degree `J`, and then for each allowed base character `η₀` and ideal `Q` permits a positive constant `C` depending on `η₀,Q`. It is therefore *not a single universal numerical constant uniform over all such characters*. Whether downstream arguments preserve this distinction requires independent checking at the interface where the detector is applied.

The next genuine analytic obligation is the `Energy/CanonicalHighPhysical.actual_high_physical` left/right column estimates, **not** merely the algebraic stage budget or the already-reconstructed prime-bin contour.

## 7. Source identities and claim boundary

| Exact pinned source module | Git blob |
|---|---|
| `TraceCharacter.lean` | `ff1d1237e3dd4754aa2e432002de16b5efb2d86b` |
| `GaussianTheta.lean` | `b36fe06c170ec382eee57914062ec6ddf5970920` |
| `Hecke/Primitive.lean` | `f5a4d238a29a0528c52424263ca41db387c390a4` |
| `Hecke/StripActual.lean` | `de7a55271a7293ce2814118b685c0896a020bd3f` |
| `Energy/NaturalHighStage.lean` | `5fe54609161fba6b3f07eb7ae576929849b13ffd` |
| `Energy/PositiveHighSourceBound.lean` | `7c71b4e9b2ff377d3e86a231d1c21c54af96e37b` |
| `Energy/PositiveHighPhysical.lean` | `849ef4a7ce9282f2e759c35743765ced05ae6b55` |
| `Energy/CanonicalHighPhysical.lean` | `a07dd29bcf9bb1b88eb1a522a0f369de4a86759f` |

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI26-F003-THETA-ROOT-AND-NATURAL-HIGHSTAGE/1
SOURCE_SHA: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: MOD5_THREE_NONPRINCIPAL_GAUSS_AND_THETA_FE_REPLAY_PASS__HIGHSTAGE_CAPACITY_INEQUALITY_PROVED__GLOBAL_ANALYTIC_HIGHSTAGE_OPEN
TESTS: exact quartic log table and Gauss rows; chi1/chi2/chi3 root numbers; truncated theta at reciprocal t; explicit Gaussian tail majorants; hostile normalizations; exact Fraction high-stage capacity
CAVEAT: 100-digit computation, NOT interval numerical certification; arithmetic witness, NOT NaturalState witness; no general Hecke functional-equation theorem independently formalized
NEXT: CanonicalHighPhysical.actual_high_physical source-column analytic estimates, then actual detector uniformity
CLAIM_BOUNDARY: FAMILY003_UNRESOLVED; NO MATHCERT
```
