# OAI-26 F003 — independent reconstruction of `polynomial_bound_in_bin`

**Assignment:** `GCL-OAI26-F003-PRIME-BIN-RECONSTRUCTION/1`  
**Immutable manuscript/Lean source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Exact target:** `lean/OAI/NumberTheory/DirichletL/Hecke/PrimeDyadicBuffered.lean`, Git blob `6f062526af17ca3a95453cd646704aef305160b0`.  
**Independent executable:** [f003_prime_bin_contour_adversary.py](f003_prime_bin_contour_adversary.py).  
**Scope:** reconstruct a *conditional* analytic theorem. This does not independently establish a global seven-eighths zero-free half-plane or validate the subsequent energy induction.

## 1. What is being bounded?

Let `K=ℚ(ω)`, `O=ℤ[ω]`. For a nonprincipal Hecke character `χ` with ideal coefficients `aχ(I)`, define the von Mangoldt-type coefficient `bχ(I)=Λ_K(I)aχ(I)`. In `Re(s)>1`, absolute convergence of the ideal Euler product supplies

`Fχ(s)=−Lχ'(s)/Lχ(s)=∑_{I≠0} bχ(I)N(I)^(−s)`.

For a smooth complex-valued weight `W` supported in `[α,β]⊂(0,∞)`, a scale `D≥1`, and real `σ,ν`, the pinned normalized prime polynomial is

`Pχ(W,D,σ,ν)=D^(−1/2)∑_{I≠0} bχ(I) W(N(I)/D)(N(I)/D)^(−σ−iν)`.

Since `W` is compactly supported away from zero, only finitely many ideals contribute for each fixed `D`. Write `M_W(s)=∫₀^∞W(x)x^(s−1)dx` and `δ=σ+iν`. Fourier/Mellin inversion, first at `r=2−σ`, gives

```
Pχ = (1/2π) ∫_{−∞}^{∞}
          M_W(r+it) D^(r+it+δ−1/2) Fχ(r+it+δ) dt.
```

This matches the source's `PrimeDyadic.polynomial_mellin` and `PrimeDyadicContour.integrand`. The sign `−L'/L` matters: its residue at a zero is **negative**, not positive.

## 2. The zero-free rectangle is conditional, not supplied by this theorem

Fix `0<e<10⁻³`, `0.51≤a≤1`, `T>2`, `i∈ℕ`; put

```text
H     = (3i+2)T,
Hmax  = 3(i+1)T,
ℓ     = a+8e−σ,
r     = 2−σ,
V     ≥ 0,
|ν|+V ≤ H.
```

The precise hypothesis is

`zeroMaximum(χ_family,Hmax)<a+2e`.

Here `zeroMaximum` enumerates all zeros of the **finite nonprincipal** family in the compact set `0.51≤Re(s)≤1, |Im(s)|≤Hmax`, plus the sentinel `0.51`. The sentinel prevents an undefined maximum if no zeros are present. It is not a claimed zero.

**Lemma 1 (disk exclusion).** For every family member and every `|t|≤H`, the disk

`B(2+it, 2−a−2e)`

has no zeros of its `Lχ`.

**Independent proof.** Any point `z` in the disk satisfies `Re(z)>a+2e≥0.51`. Also,

`|Im(z)|≤|t|+(2−a−2e)<H+T=Hmax`

because `2−a−2e<1.49<T`. If `Re(z)>1` then the absolutely convergent Euler product ensures `Lχ(z)≠0`. Otherwise `Re(z)≤1` and a zero would be among the finite family zeros defining `zeroMaximum`, contradicting `zeroMaximum<a+2e<Re(z)`. The strict margin is essential. ∎

**Lemma 2 (rectangle containment).** For any `s` with `ℓ≤Re(s)≤r` and `|Im(s)|≤V`, its translated point `z=s+δ` satisfies `a+8e≤Re(z)≤2` and `|Im(z)|≤|ν|+V≤H`. The point `z` is at distance

`|2−Re(z)|≤2−a−8e`

from `2+i Im(z)`, hence is in the **smaller** closed disk used for the derivative bound. Therefore the entire closed translated rectangle is zero-free.

At `a=1`, the left edge is still strictly left of the right edge because `8e<0.008<1`. The source's `PrimeDyadicBuffered.hlr` and `translated_rectangle_mem` are the formal counterparts. ∎

**What if zeros are present?** Let `ρ` be an interior zero of multiplicity `m`. Near `ρ`, `−L'/L(s)=−m/(s−ρ)+O(1)`; the translated integrand has residue

`Res = −m M_W(ρ−δ) D^(ρ−1/2)`.

Its contribution to the original normalized prime polynomial when moving the contour left is **that residue**, with the sign just shown. A pole of order `p` instead contributes `+p M_W(ρ−δ) D^(ρ−1/2)`. Nonprincipal `Lχ` is entire in the formal source, so the pole case is excluded by `χ.residue≠1`. The source **does not bound** these residues in `polynomial_bound_in_bin`; its hypothesis excludes them completely. One must not quietly apply this conditional lemma to a bin where the zero-maximum condition fails.

## 3. Uniform logarithmic derivative: how `B` depends on the family

The source defines

`complexity(χ,t)=2·N(modulus χ)·(3+|t|)^2`,

`binCost(B,χ,H)=B log(complexity(χ,H))+localBound(1/2) log N(rad(modulus χ))`.

Its `PrimeDyadicControl.buffered_rectangle_control` furnishes a **single constant** `B=B(e)≥0`, independent of `χ`, `i`, `T`, `a` and the cardinality of the finite family, satisfying in the translated rectangle

`|−Lχ'(z)/Lχ(z)| ≤ binCost(B,χ,H)`.

Here is the standard independent reconstruction of the analytic mechanism:

**Primitive case.** Center at `c=2+it` and set

```text
R0=2−a−2e,  R1=2−a−3e,
R2=2−a−4e,  R3=2−a−8e.
```

The outer disk `B(c,R0)` is zero-free by Lemma 1. A holomorphic logarithm `g=log Lχ` therefore exists on this disk. Its additive `2πiℤ` ambiguity is fixed by matching the Euler-product logarithm on an inner disk `|z−c|≤0.49`. The source bounds this inner logarithm by an absolute `A`.

The other essential analytic input is a **uniform polynomial-growth estimate** on the disk `|z−c|<R1`,

`|Lχ(z)|≤Q^M`, with `Q=complexity(χ,t)`,

and a universal `M` after the permitted primitive conductor normalization. This invokes `HeckeLogarithmicInput.regular_right_growth` and its strip/functional-equation inputs. Importantly, **zero-freeness alone does not give this growth estimate**.

It follows that `Re(g)≤M log Q`. Borel–Carathéodory on `R1` to `R2` gives a bound of the form

`|g(z)|≤A_0(e,A,M) log Q` on `|z−c|≤R2`,

where the pinned implementation takes `A_0=(4M+4A)/e`. Cauchy's derivative estimate on a disk of radius `2e` about `z` (which lies within `R2` whenever `|z−c|≤R3`) gives

`|Lχ'(z)/Lχ(z)|=|g'(z)|≤A_0 log Q/(2e)`.

Thus the primitive bound has `B(e)=2(M+A)/e²` for this choice of constants. The exact numerical value is not important; its independence from `χ` is.

**Imprimitive case.** The source reduces `χ` to a primitive `ψ` and writes, on `Re(s)>0`,

`Lχ(s)=Lψ(s)·∏_{𝔭|m}(1−aψ(𝔭)N𝔭^(−s))`.

Each added factor is nonzero in this half-plane because `|aψ(𝔭)N𝔭^(−s)|<1`. Taking logarithmic derivatives and using the triangle inequality adds at most

`localBound(1/2)∑_{𝔭|m}log N𝔭 = localBound(1/2)log N(rad m)`

on `Re(s)≥1/2`. Primitive conductor norm does not exceed the imprimitive norm. This is exactly the `radical` correction in `binCost`, not an invisible constant.

**Uniformity verdict.** The quantifier structure is sound: one absolute `B(e)` precedes an arbitrary finite family, and the explicit `χ`-dependent conductor and height terms remain inside `binCost`. There is no factor `|ι|` because the argument bounds **each family member individually** after using a common zero-maximality hypothesis.

**Important evidentiary limit:** the contour/Borel–Carathéodory argument is independently reconstructed above. The precise primitive strip growth theorem and functional-equation inputs establishing `|Lχ|≤Q^M` are *read from the pinned source*, not independently reproduced from all classical Hecke analytic foundations here. Without that input, the character-uniform derivative conclusion would not follow. The adversary includes the hostile zero-free family `L_k(s)=exp(k(s−2))` with arbitrarily large `|L_k'/L_k|=k`, which demonstrates the necessity of growth control.

## 4. Four sides and the exact boundary coefficients

For `r=2−σ`, `ℓ=a+8e−σ`, and `V≥0`, the independent contour identity, using the parametrization `dz=i,dt` on vertical lines, is

```
∫_{−V}^V f(r+it)dt
 = ∫_{−V}^V f(ℓ+it)dt
   + i[∫_ℓ^r f(x−iV)dx − ∫_ℓ^r f(x+iV)dx]
```

when no zeros lie within the closed rectangle. Here `f(s)=M_W(s)D^(s+δ−1/2)Fχ(s+δ)`. The right-hand original infinite line is the finite right segment plus its two tails.

Because `W` is smooth and compactly supported away from zero, `M_W` is entire. Writing `x=e^u` makes `M_W(c+it)` the Fourier transform of a smooth compactly supported function in `u`. Repeated integration by parts gives, for every `n`,

``\
|M_W(ℓ+it)|≤C₂/(1+|t|)^2;
|M_W(x+it)|≤C_n/(1+|t|)^{n+2}
\``

uniformly for `x∈[ℓ,r]`. The source takes `C₂,C_n≥0` as explicit hypotheses and supplies them later from `PrimeLogProfile.uniform_mellin_decay`; at this theorem layer they are *not* silently manufactured.

Let `Kχ=binCost(B,χ,H)`. Then:

**Left vertical.** The `1/2π`-normalized contribution has norm at most

`(1/(2π))·π C₂ D^(a+8e−1/2) Kχ`,

because `(1+|t|)^2≥1+t²` and `∫_{ℝ}(1+t²)^{-1}dt=π`.

**Two horizontal joins.** Each has length `r−ℓ=2−a−8e>0`. The source bounds their combined unnormalized contribution by

`2·C_n D^(3/2) Kχ·(r−ℓ)/(1+V)^n`.

This uses `D≥1` to replace `D^(x+σ−1/2)` by its maximum `D^(3/2)` for `x≤r`. The source's `|2−a−8e|` is equal to the positive width.

**Right tails.** At `Re(s+δ)=2`, the Euler series supplies `|Fχ|≤eulerBound(2)`, independent of the character. Since

`∫_{|t|>V}(1+|t|)^{−n−2}dt = 2(n+1)^{−1}(1+V)^{−n−1} ≤ π(1+V)^{−n}`,

the unnormalized tails are bounded by

`π·C_n D^(3/2)eulerBound(2)/(1+V)^n`.

Combine these, remembering the `1/(2π)` Mellin normalization:

```
|Pχ| ≤ 1/(2π) [
  π C₂ D^(a+8e−1/2) Kχ
  + 2(r−ℓ) C_n D^(3/2) Kχ/(1+V)^n
  + π C_n D^(3/2) eulerBound(2)/(1+V)^n
].
```

**This is the precise source theorem.** The factors `1/(2π)`, `π`, `2(r−ℓ)`, and the half-power `D^(−1/2)` are consistent. There is no dropped zero contribution under the zero-maximum hypothesis. When the hypothesis is false, the correct formula has extra residues as in §2.

## 5. Exact independent adversary

The standalone script performs four kinds of adversarial tests:

1. **360 exact rational cases** for `a,e,T,i,σ`, including the outer/inner disk radii, `6e` buffer, `Hmax−H=T` margin, translated edges, half-power exponents and strict endpoints.
2. **Uniformity monotonicity cases** with different conductor norms, radical norms and heights; plus a hostile zero-free family with unbounded logarithmic derivatives to prove that zero location alone is insufficient.
3. **Complex contour quadrature at 55 decimal digits**, using a synthetic entire Gaussian Mellin-like test factor and the toy meromorphic family `L(s)=(s−ρ)^m`. These are deliberately **not** actual Hecke L-functions or compactly supported Mellin weights; they isolate the residue calculus and orientation independently of the OAI source.
4. **Hostile singularities:** one interior zero, a double zero (twice the residue), and a pole (opposite residue sign). The no-zero case has residual about `1.7×10^{-57}`; a single interior zero forces a substantial nonzero term, `−1.59479−0.16420i`. The pole and double-zero cases agree with residue theory at the stated precision.

The synthetic quadrature validates the contour manipulation, not uniform Hecke analytic number theory. Exact fractions validate only the explicit geometric and exponent inequalities. The source's `B` bound still depends on the genuine primitive growth theorem.

## 6. Referee verdict and next obligation

| Layer | Verdict | Rationale |
| --- | --- | --- |
| Mellin normalization and coefficient sign | **PASS (independently reconstructed)** | Euler logarithmic derivative and Fourier/Mellin inversion |
| Zero-window containment and disk geometry | **PASS (exact rational + proof)** | `a+2e` cutoff, `a+8e` contour and `T>2` height gap |
| Zero residues and multiplicity | **PASS (analytic + adversarial)** | Conditional hypothesis genuinely eliminates all terms; hostile cases exhibit missing residues otherwise |
| Four-sided contour and constants | **PASS (independent derivation)** | `π,2(r−ℓ),π` and `D^{−1/2}` retained |
| Primitive-to-imprimitive radical correction | **PASS conditional on established character/factor model** | Euler factors nonzero for positive real part; explicit log-radical cost |
| Uniform primitive logarithmic derivative | **CONDITIONAL / NOT INDEPENDENTLY SOURCE-FULLY CERTIFIED** | Borel–Carathéodory/Cauchy reconstructed; primitive strip growth/functional-equation bound requires separate independent validation |
| Seven-eighths zero-free theorem | **UNRESOLVED** | The bin lemma assumes a zero-maximum condition, and later global energy construction remains unverified independently |

**Next mathematical target:** `Hecke/LogarithmicInput.regular_strip_bound` (its `HeckePresentation.uniform_strip_bound` and `HeckePrincipalStrip.uniform_source_normalized_strip_bound` inputs), including degree-two gamma-factor normalization, conductor exponent `3/5`, nonprincipal/principal conventions and uniformity in vertical height. The next most consequential independent investigation after that is the global energy high-stage mechanism, because `polynomial_bound_in_bin` is conditional and does not itself provide a zero-free bin.

**Disposition:** `F003_PRIME_BIN_CONTOUR_AND_ZERO_ACCOUNTING_INDEPENDENT_PASS__PRIMITIVE_GROWTH_AND_GLOBAL_ANALYTIC_ENERGY_OPEN`.  
**Claim boundary:** no independently certified seven-eighths zero-free theorem; no MATHCERT.
