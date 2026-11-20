# OAI-26 Family 003 — independent annular-block Fourier/Cauchy reconstruction and exact ray-pair phase spectrum

**Assignment:** `GCL-OAI26-F003-ANNULAR-REFLECTION-RAYPHASE/1`  
**Immutable upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Executable:** [f003_annular_ray_reflection_adversary.py](f003_annular_ray_reflection_adversary.py) (Python standard library; exact `fractions.Fraction`, including Gaussian-rational complex arithmetic).  
**Disposition:** `F003_ANNULAR_FOURIER_CAUCHY_AND_REFLECTION_CONDITIONAL_RECONSTRUCTION_PASS__EXACT_RAY_PHASE_FOURIER_MASS_4_PROVED__MAIN_ERROR_COLUMN_ENERGIES_OPEN`.

## 1. Precise distinction between the algebra and the analytic input

The prior [PR #574](https://github.com/grandchallenge/MATHFORGE/pull/574) independently proves the all-scale Eisenstein Möbius harmonic-mass estimate by a direct lattice count. The remaining `Moments/FirstDivisorCommonBound.actual_supported_annular_harmonic` **also** needs `actual_supported_annular_block`, which comes from `FirstPhysicalAnnularCommonBound.actual_annular_block_from_common_energy → FirstPhysicalSourceCommonBound.fixed_log_block_from_common_energy → FirstPhysicalSourceBound.physical_block_child_bound → FirstChildBound.whole_kernel_first_child_bound → ReflectedChild.whole_kernel_reflected_gauss_child_bound → Cauchy.whole_kernel_row_estimate → Smooth.whole_product_pair_separation`.

This review independently reconstructs **the conditional Fourier/Cauchy transfer, the reflected-row majorant and the live divisor cancellation**. Its substantive new finite result is an **exact ray-phase Fourier mass of 4**, improving the original (valid but crude) 256 coefficient budget by a factor of 64. The conclusion still takes the source's **actual left/right commonEnergy bounds as hypotheses** and does not prove the estimates which make those hypotheses true for natural source families.

## 2. Fourier separation of the physical annular kernel

The pinned `Moments/Smooth.lean` defines, using `R>0` and real log parameters `ρ,x,u,v`,

```text
rootWindow V(y) = V(y) / sqrt(exp(y)),

wholeKernel(R,ρ,x,u,v) =
 V0(ρ) V1(x) rootWindow(V2,u) rootWindow(V3,v)
 paperRadialFourier(W)(R exp(ρ+x−u−v)).
```

`logPhase(t,s)=exp(2πits)`; the signs are `(+,+,−,−)`, **not** four plus signs. If the four cutoffs vanish outside `[-Mj,Mj]`, put `L=M0+M1+M2+M3`. Then `ρ+x−u−v∈[-L,L]` whenever the product of cutoffs is nonzero. The rootWindow factors do not change support because `exp(y)>0`.

Here is a source-independent *conditional* smooth-log Fourier lemma: let `G:(0,∞)→ℂ` be smooth with Euler derivative seminorms bounded to arbitrary order,

`sup_{r>0} (1+r)^N |(r d/dr)^k G(r)| < ∞` for every `N,k≥0`.

Choose a fixed smooth compact cutoff `ψ=1` on `[-L,L]`, supported on `[-L−1,L+1]`. Set `h_R(s)=ψ(s)G(R exp(s))`, and let

```text
b_R(t)=∫_{s∈R} h_R(s) exp(−2πits) ds.
```

Fourier inversion gives `G(R exp(s))=∫ b_R(t) exp(2πits)dt` on `[-L,L]`. Therefore multiplying by the four windows and factorizing the exponential gives exactly the pinned separated-kernel integral with the stated four signs.

For `s∈supp(ψ)`, `R exp(s)≥e^(−L−1) R`. Each `k`th derivative `∂_s^k h_R` is a finite combination of `ψ` derivatives and `(r∂_r)^j G(R exp(s))`, so for every `N,k` it is bounded in `L1(ds)` by `C_{N,k}(1+R)^(−N)`. For `|t|≥1`, integrate by parts `k` times:

`|b_R(t)| ≤ ||h_R^(k)||₁/(2π|t|)^k`;

for `|t|≤1`, use `|b_R(t)|≤||h_R||₁`. With `k>J+1` this implies

```text
(1+R)^A ∫_R (1+|t|)^J |b_R(t)| dt ≤ C(A,J,L,G,ψ)
```

for every `R>0`; the analogous pointwise bound also holds. Importantly the constants do not depend on the column indices, their number, or any characters, though they depend on the fixed smooth windows' support and the radial transform `G`. No continuity of the four *external* cutoff values `Vj` is required for this factorization because they are factored outside the Fourier integral.

This proves the **general Fourier step under explicitly stated Euler regularity and decay**. For the pinned Hecke kernel, the required special `G=paperRadialFourier(W)` Euler-bound is a separate imported theorem `EisensteinSchwartzPoisson.paperRadialFourier_euler_bound` (the source calls it in `QuadraticSieve/IdealQuotients.lean`). That specialized radial-Fourier theorem has **not been independently rederived** here. Thus a statement that *all* analytic inputs are now fully certified would be wrong.

## 3. Independent finite-row Cauchy reconstruction

After separation, for each finite row `z` and frequency `t`, write

```text
L_z(t)=Σ_i c_(z,i) rootWindow(V2,u_i) exp(−2πit u_i),
R_z(t)=Σ_j conj(d_(z,j)) rootWindow(V3,v_j) exp(−2πit v_j).
```

There is a row phase `A_z(t)` of modulus at most one, and row cutoff `η_z` of modulus at most one. The separated row sum is

`Σ_z η_z A_z(t) L_z(t) R_z(t)`.

Its modulus is at most

`(Σ_z|L_z(t)|²)^1/2 (Σ_z|R_z(t)|²)^1/2`

by the triangle inequality and Cauchy–Schwarz, independently of any probabilistic independence between rows or of the number of rows. If the two energies are bounded for **every real** `t` by `E_L²(1+|t|)^(2JL)` and `E_R²(1+|t|)^(2JR)`, it follows that

```text
(1+R)^A |whole block|
 ≤ E_L E_R * [(1+R)^A∫(1+|t|)^(JL+JR)|b_R(t)|dt]
 ≤ C E_L E_R.
```

The pinned `ReflectedChild` and `GaussEnergy` modules take the right column at **`−z`**, not `+z`. This reflection is essential to the source's character-conjugation identity. To pass from the finite row norm to the global `Re(gaussEnergy)` bound, the radial majorant `U(||z||²/K)` must be **real nonnegative everywhere**, **at least one on the chosen rows**, and **even under `z↦−z`**. The last property is automatic from its dependence on `||z||²`; it is not automatic for an arbitrary weight. The test deliberately substitutes an asymmetric majorant and demonstrates that the reflected-energy inference fails.

The source then expands a finite coprimality/Möbius character decomposition. For every divisor with `μ(L)=0`, the contribution is zero. For every nonzero-`μ` divisor outside the supported norm window, the **right** `commonEnergy` vanishes, so the paired contribution is also zero. A live divisor uses left and right energies scaled by `1/N(L)`; hence

`windowBudget(JL,t,E1/N(L))*windowBudget(JR,t,E2/N(L)) = [windowBudget(JL,t,E1)*windowBudget(JR,t,E2)]/N(L)`.

This is the exact origin of the `1/N(L)` which the independently proved harmonic-mass theorem in PR #574 sums. It is **not** `1/N(L)^2` because each energy enters through a square root.

## 4. A new exact finite-character theorem: Fourier phase mass **4**, not just **256**

The source `RayFourExpansion` works in the residue ring `R=O/(4)` with `|R|=16`, and its tensor Fourier coefficients `pairCoeff firstPhaseTable χ ξ` are normalized by `|R×|^2` (by two applications of `unitFourierCoeff`). The **unit group has exactly 12 elements**: a residue `a+bω mod4` is invertible iff at least one coordinate is odd, because `(2)` is inert. Thus there are `16−4=12` units.

The pinned `QuadraticAllOddCRT.quadraticRayExponent` is reproduced exactly on those units by

```text
q(u)=0 : u in {(0,1),(0,3),(1,0),(1,1),(3,0),(3,3)}
q(u)=1 : u in {(1,2),(1,3),(2,3)}
q(u)=3 : u in {(2,1),(3,1),(3,2)}.
```

Multiplication is the Eisenstein rule

`(a,b)*(c,d)=(ac−bd,ad+bc−bd) mod4`.

The source's sign is

`β(u,v)=+1 iff q(uv)=q(u)+q(v) mod4; β(u,v)=−1 otherwise`.

The source also proves that `β` is multiplicative in both arguments. Independent exhaustive enumeration confirms these identities on **all 12×12×12 triples** (both left/right) and exhibits exactly **four distinct rows** of the `β` table. In other words, the homomorphism

```text
φ:G→Ĝ,   φ(u)(v)=β(u,v)
```

has image of size `4` and kernel of size `3` (specifically `{(1,0),(0,1),(3,3)}`, the cube-root-of-unity subgroup mod4).

This yields an **exact** tensor Fourier mass by finite character orthogonality. Let `N=|G|=12`; then

```text
β̂(χ,ξ)
 = N^(−2) Σ_u Σ_v β(u,v) conj(χ(u)) conj(ξ(v))
 = N^(−1) Σ_{u:φ(u)=ξ} conj(χ(u)).
```

For `ξ` outside `im φ`, the coefficient is zero. For `ξ` in the image, its fiber is one coset of `ker φ`, with three elements. The character sum on that coset is zero unless `χ` is trivial on `ker φ`; exactly `|G/ker φ|=4` characters are. For each of the `4×4=16` qualifying ordered pairs `(χ,ξ)`, the coefficient has modulus `3/12=1/4`. All others vanish. Hence

```text
Σ_χ Σ_ξ |pairCoeff(firstPhaseTable,χ,ξ)|
 = 16*(1/4) = 4  (EXACT).
```

The pinned `FirstColumns.firstPhaseTable_mass` establishes the weaker but valid `≤256` by bounding each Fourier coefficient independently and using `|R×|≤16`. The above is an **independently reconstructed sharper theorem** using the source's *actual special bicharacter*, and would allow the `256*C` in `Moments/FirstChildBound.finite_first_ray_divisor_bound` to become `4*C` **if formally integrated with an exact new phase-mass lemma**. We do **not** claim such a formal upstream replacement has already happened. No change to the main exponent follows from reducing this fixed constant.

A more general fallback, also absent from the crude source bound, is finite Fourier Parseval: for any `f:G×G→ℂ` with `|f|≤1`, normalized Parseval and Cauchy give `Σ|f̂|≤|G|=12`. The exact `4` uses the stronger bicharacter structure.

## 5. Independent exact-arithmetic adversarial replay

The `f003_annular_ray_reflection_adversary.py` script imports only Python standard libraries. It independently reconstructs the full residue ring multiplication, classifies its units, copies the **literal frozen exponent cases** from the pinned exact source, and verifies all `β(uv,w)=β(u,w)β(v,w)` and `β(w,uv)=β(w,u)β(w,v)` identities. It computes the image/kernel sizes and the rational Fourier-mass result, without importing or calling the upstream proof.

It also evaluates **101 distinct exact Gaussian-rational finite 4-frequency Fourier identities**: each synthetic finite-row kernel is calculated in two separate ways, directly from the row/column sums and from its normalized discrete Fourier separation. The exact Gaussian-rational Cauchy inequality is checked frequency by frequency. All cases pass. Deliberately using `+z` in place of the required reflected `−z` produces a different result in **all 101** cases; an asymmetric radial majorant fails a separate hostile fixture. The exact `1/N(L)` live-Möbius filtering identity is also exercised with rational square-root energies.

The cyclic 4-frequency model is explicitly **a finite algebraic analogue**, not the analytic Schwartz kernel, an independent proof of the actual radial Fourier transform or a numeric test of all Hecke characters. This distinction prevents successful synthetic tests from being mistaken for a universal analytic theorem.

## 6. Exact source identity ledger

| Pinned upstream source module | Git blob |
| --- | --- |
| `Cusp/MatrixPhases.lean` | `2809777b2ca74d934bdef1b0628712e253b2bf90` |
| `Eisenstein/ConjugateLevelAction.lean` | `ec24213c371d03f66029e804dc835e2642dff28d` |
| `GaussSum/CompletedExpansion.lean` | `d9436239ccd86ccfca3bb92468f3f4cb94603b85` |
| `Moments/FirstColumns.lean` | `b865ca1fd675873fdbe4ebd0ff0af098eb052ae7` |
| `Moments/Smooth.lean` | `8948da018370b83cb75d782d04a5916b1fb40025` |
| `Moments/Cauchy.lean` | `47efa12e5ef35955fb4bf688456508b129214b4f` |
| `Moments/ReflectedChild.lean` | `0e879090d3ca0b622179e754adfcad2c6dc30ac6` |
| `Moments/FirstChildBound.lean` | `e4450ef2085a8b6c4d37d7d1e2ac53c28f67b2e1` |
| `Moments/FirstPhysicalAnnularCommonBound.lean` | `8a1e86cc1654dca3ee1a1cf9ec7bee849f9ff7b5` |
| `Moments/FirstDivisorCommonBound.lean` | `36607a6a9a764e918f3c79898f7561a6d836cdc4` |

## 7. Further proof obligations

The independent analytic argument above assumes the radial `paperRadialFourier` transform has all Euler derivative seminorm bounds used by the Fourier separator. The source has these estimates, but a source-independent derivation from the exact normalized Gaussian/Fourier conventions remains open.

Far more importantly, Fourier/Cauchy only **transfers** two column-energy estimates. The estimates' existence for natural sources is still being supplied by the pinned `Energy/CanonicalMainHomogeneous.actual_main_homogeneous` and `Energy/CanonicalErrorHomogeneous.actual_error_homogeneous` chains, with `ZeroAt`/`PositiveAt` child inputs. They remain the substantive independent global analytic and noncircularity audit targets. The source's conditional `actual_supported_annular_block` is not to be advertised as a proof of the seven-eighths theorem.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-ANNULAR-REFLECTION-RAYPHASE/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
MATHEMATICS: full conditional Fourier-log separator derivation,
 finite-row Cauchy proof, radial reflection necessity,
 exact live Möbius/square-root normalization,
 exact ray bicharacter 4-image/3-kernel,
 exact Fourier L1 coefficient mass=4 (prior source cap 256)
EXECUTION: 12 unit enumeration, two-sided multiplicativity on all
 12x12x12 triples, 101 exact Gaussian rational DFT/Cauchy
 cases, 101 reflected-row hostile failures, radial majorant
 hostile failure, live-Mobius divisor identity; all PASS.
SCOPE: not independent radial Hecke Poisson/Euler-bound replay,
 no analytic main/error child closure, no overall 7/8 theorem.
FAMILY003: UNRESOLVED
MATHCERT: NONE
```
