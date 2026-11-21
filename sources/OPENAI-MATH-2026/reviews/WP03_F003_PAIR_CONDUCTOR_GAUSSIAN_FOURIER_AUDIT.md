# OAI-26 Family 003 — pair-conductor Gaussian Fourier reconstruction

**Assignment:** GCL-OAI26-F003-PAIR-CONDUCTOR-GAUSSIAN/1  
**Pinned source:** openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a  
**Predecessor:** MATHFORGE PR #576, protected 66269878fa291e0698164a169b00932ff3d6b1cb  
**Disposition:** GENUINE_GAUSS_PAIR_CONDUCTOR_POISSON_BOUND_MATHEMATICAL_PROOF__SHARP_ALL_STAGE_CHILD_ENERGY_OPEN  
**Scope:** independent mathematical reconstruction, not Lean formalization, source modification or MATHCERT.

## 1. Source-specific objects; no surrogate polynomial

Write \(\mathcal C\) for the actual finite supported columns of any input \(s\) (including both `CanonicalMainGaussian.child` and `CanonicalErrorGaussian.errorInput`). Let \(a_I\) be the pinned `sourceGenerator` of column \(I\), and let \(N(I)=|O/(a_I)|=|a_I|^2>0\). The exact row is

\[
g_I(z)=\frac{1}{\sqrt{N(I)}}\sum_{x\in O/(a_I)}
  \chi_I(x)\,\psi_{a_I}(zx),
\]

where \(\chi_I=\texttt{supportedModulusCharacter}\), and \(\psi_{a_I}=\texttt{quotientTrace}\) is the **source's primitive additive character**, not a naïvely chosen lattice trace. Pinned `Moments/Fourier.lean:residueGauss_supported_mk`, `Moments/GaussEnergy.lean:gaussRow`, and `Detector/PhysicalPoisson.lean:sexticGauss_frequency_congr` establish this representation and periodicity. The `MulChar` vanishes at nonunits and has modulus 1 at units (`Moments/SupportedCorrelation.lean`); thus \(|\chi_I(x)|\le1\).

The input coefficients are \(c_I=\beta_I\,\texttt{heightCoeff}(s.\eta,s.t,I)\), with \(|c_I|\le|\beta_I|\); \(P_s(z)=\sum_{I\in\mathcal C}c_Ig_I(z)\) is **exactly the actual source Gauss polynomial**. Its energy is

\[
E_s(K)=\texttt{normalizedGaussSource}(s,R,\mathrm{seed},
  \texttt{ballProfile},K)
 =\frac{1}{V_s}\sum_{z\in O}|P_s(z)|^2\Phi(N(z)/K),
\]

with \(V_s=\texttt{volume}(s)>0\), \(K>0\), \(\Phi=\texttt{QuadraticInitialBound.sieveCutoff}\in[0,1]\), real, smooth, and compactly supported in \((-\infty,2)\). Here \(\phi(x)=\Phi(|x|^2)\in C^\infty_c(\mathbb R^2)\). This is not `paperRadialFourier`; the latter appears **after** Poisson summation.

## 2. Finite Plancherel and the zero-mean coprime theorem

For any supported proper nonzero \(I=(a)\), the primitive additive pairing on \(O/(a)\) is nondegenerate. Finite character orthogonality yields, **without a primitivity hypothesis on the multiplicative character**,

\[
\frac{1}{N(I)}\sum_{z\bmod I}|g_I(z)|^2
=\frac{1}{N(I)}\sum_{x\bmod I}|\chi_I(x)|^2\le1,
\quad
\frac{1}{N(I)}\sum_{z\bmod I}g_I(z)
=\frac{\chi_I(0)}{\sqrt{N(I)}}=0
\quad(N(I)>1).
\]

The second identity is explicitly restricted to *proper* \(I\), since \(\chi_I(0)=0\) then. For any two supported columns \(I,J\), form

\[
H_{IJ}:=\frac{1}{N(IJ)}\sum_{z\bmod IJ}g_I(z)\overline{g_J(z)}.
\]

Each row is periodic modulo its own ideal; reduction \(O/IJ\to O/I\) has equal-sized fibers. Cauchy–Schwarz gives \(|H_{IJ}|\le1\), and \(0\le H_{II}\le1\). If \(I,J\) are **coprime proper ideals**, CRT makes their residue coordinates independent, so \(H_{IJ}=(\mathrm{mean}\,g_I)\overline{(\mathrm{mean}\,g_J)}=0\). This is an exact orthogonality identity for the **genuine sextic Gauss rows**, not a statistical independence assumption.

For a finite family define the conductor-interaction graph: vertices are columns and an edge joins \(I\ne J\) when \(I\) and \(J\) are not coprime (or either is the unit ideal). Denote its connected components by \(\mathscr B\). On the common period \(\mathfrak q=\prod_{I\in\mathcal C}I\), the mean-square Gram matrix is positive semidefinite, diagonal entries \(\le1\), and cross-component entries zero. Consequently

\[
0\le \frac1{N(\mathfrak q)}\sum_{z\bmod\mathfrak q}|P_s(z)|^2
\le\sum_{B\in\mathscr B}\left(\sum_{I\in B}|c_I|\right)^2
\le\left(\sum_{I\in\mathcal C}|\beta_I|\right)^2.
\]

If all columns are pairwise coprime and proper, this improves to \(\sum_I|c_I|^2\le\sum_I|\beta_I|^2\). Shared conductor prime factors are the precise obstruction to unconditional full diagonalization by this route.

## 3. Pairwise-period Poisson estimate, with explicit conductor

**Lemma (independent mathematical proof).** For every \(A>0\), there is \(C_{A,\Phi}<\infty\), depending only on the *fixed* smooth bump \(\Phi\), such that for any two supported nonzero columns \(I,J\) and every \(K\ge1\),

\[
\boxed{
\left|
\sum_{z\in O}g_I(z)\overline{g_J(z)}\Phi(N(z)/K)
-c_\Phi K H_{IJ}
\right|
\le C_{A,\Phi}\,K\,N(IJ)
 \left(1+\sqrt{\frac K{N(IJ)}}\right)^{-A},
}
\]

where \(c_\Phi=\frac2{\sqrt3}\int_{\mathbb R^2}\Phi(|x|^2)\,dx\ge0\).
Importantly, **the modulus on the right is the pair conductor \(IJ\)**, not the product of all columns.

*Proof.* Put \(\Lambda=\mathbb Z[\omega]\subset\mathbb R^2\) with covolume \(\sqrt3/2\). The function \(f(z)=g_I(z)\overline{g_J(z)}\) is periodic modulo \((a_Ia_J)\Lambda\). Fourier-expand it on the finite abelian quotient \(\Lambda/(a_Ia_J)\Lambda\); there are exactly \(N(IJ)\) characters. Every normalized Fourier coefficient is bounded in magnitude by the mean \(|f|\), hence by \((\mathrm{mean}|g_I|^2)^{1/2}(\mathrm{mean}|g_J|^2)^{1/2}\le1\). Its zero-frequency coefficient is \(H_{IJ}\).

For a character represented by \(\xi\in (a_Ia_J\Lambda)^*/\Lambda^*\), lattice Poisson summation for \(\phi(x)=\Phi(|x|^2)\) gives

\[
\sum_{z\in\Lambda}\phi(z/\sqrt K)e^{2\pi i\langle\xi,z\rangle}
=\frac{2K}{\sqrt3}\sum_{\lambda\in\Lambda^*}
 \widehat\phi(\sqrt K(\lambda-\xi)).
\]

At \(\xi=0\), the term \(\lambda=0\) equals \(c_\Phi K\), and the other terms decay faster than every power of \(\sqrt K\). At \(\xi\ne0\bmod\Lambda^*\), every \(\lambda-\xi\) is nonzero in \((a_Ia_J\Lambda)^*\), so its Euclidean length is at least \(c/\sqrt{N(IJ)}\) for a universal \(c>0\) (multiplication by a nonzero Eisenstein integer is a similarity). By arbitrary-order Schwartz decay of \(\widehat\phi\) and a uniformly convergent lattice majorant, the absolute value of this twisted lattice sum is \(\le C_{A,\Phi}K(1+\sqrt{K/N(IJ)})^{-A}\). The zero-character remainder obeys the same bound. Sum at most \(N(IJ)\) Fourier coefficients of magnitude at most one. QED.

Thus the **actual source** obeys the stronger independent bound

\[
\boxed{
0\le E_s(K)\le \frac{K}{V_s}
\left[
c_\Phi\sum_{B\in\mathscr B}
\left(\sum_{I\in B}|\beta_I|\right)^2
+C_{A,\Phi}
\sum_{I,J\in\mathcal C}|\beta_I\beta_J|N(I)N(J)
\left(1+\sqrt{\frac{K}{N(I)N(J)}}\right)^{-A}
\right],\quad K\ge1.
}
\]

For pairwise coprime proper columns, replace the component sum by \(\sum_I|\beta_I|^2\). The source-specific `heightCoeff` causes **no extra growth** in this bound. It applies unchanged to the main and nested error `Input` types with their exact \(K_\mathrm{main}\), \(K_\mathrm{error}\), normalizing modulus and coefficients; no substitution of a synthetic source is made.

## 4. Quantified high-stage applicability and its limitation

Suppose \(Z>1\), \(K=Z^\rho\), and **every relevant pair** obeys \(N(I)N(J)\le Z^d\) with \(0\le d<\rho\). Then each error multiplier satisfies

\[
N(I)N(J)\left(1+\sqrt{K/[N(I)N(J)]}\right)^{-A}
\le Z^{d-A(\rho-d)/2}.
\]

Choose \(A>2(d+\gamma)/(\rho-d)\) to save at least \(Z^{-\gamma}\) per pair, **before** summing over any growing number/weight of columns. Uniformity still requires bounding \(\sum_{I,J}|\beta_I\beta_J|\) and respecting the actual `Ready` and family-character width gates.

The pinned `Moments/FirstSecondInputGates.lean:Ready` (blob `32eeccf2050a59a4c3e203405b8acc3a4725b5f1`) requires `0<K`, caps the child's volume, source radius, character conductor, puncture norm, nominal scale and frequency radius; **it does not assert** either `K>=1` or `K>N(I)N(J)` for the active column pairs. Thus the pair-period lemma genuinely covers only the `K>=1` subregime; for `0<K<1` use the earlier unconditional row-count estimate in PR #576. Nor does `Ready` force the pair-conductor gap needed for power-saving. Conversely, if \(K\lesssim N(I)N(J)\) for active correlated pairs, the displayed Poisson remainder has no power saving. It cannot be promoted to the four `seededFactors` powers, nor to the `ratioPenalty^(1/6)` natural child-energy bound merely because the theorem holds. The precise residual work is a **large pair-conductor or shared-prime** cancellation theorem at the actual `Kmain/Kerror`, together with the previous-stage `ZeroAt` and `PositiveAt` budgets and the nested `υ.modulus` gate. This identifies the mathematical gap, rather than disguising it in a period-dependent constant.

## 5. Independent adversarial limitations and source receipts

The stdlib file `f003_pair_conductor_fourier_adversary.py` checks the Eisenstein norm/trace forms, primitive-pair Fourier orthogonality on unramified finite **integer** quotient examples, equal CRT fiber counts, full finite Plancherel for unit masks, and deliberately shows the naïve trace pairing becomes degenerate modulo 3. The latter is a hostile mutation test: the source uses the corrected primitive `quotientTrace`, and no defect is claimed. The finite checks validate algebraic mechanisms, **not** the infinite-lattice Poisson estimate. The proof above is an independent mathematical derivation; Lean formalization of this stronger bound has **not** been performed.

### Source identity ledger

- `Moments/GaussEnergy.lean` — blob `200d3d5c9fb828b7bd1eb4e5a7160b10c5fd65bd`, exact `gaussRow`, `gaussEnergy`, `gaussEnergy_poisson`.
- `Moments/Fourier.lean` — blob `44f1801810a2e6dd2559fd585bafae8a2f508350`, `residueGauss_supported_mk`, `normalizedResidueGauss`.
- `Moments/SupportedCorrelation.lean` — blob `60ff9177fcd60a676148d529885c01ae12869f50`, supported multiplicative character and nonunit vanishing.
- `Detector/PhysicalPoisson.lean` — blob `e2d243d19aa9a0e35c2698d734145474107bdff2`, `sexticGauss_frequency_congr`.
- `Moments/AmplificationChildInput.lean` — blob `90d172571cce6192d42d5751618619de302acd6a`, `normalizedGaussSource`, `volume`.
- `Moments/FirstSecondInputGates.lean` — blob `32eeccf2050a59a4c3e203405b8acc3a4725b5f1`, precise `Ready` premises and their missing pair-conductor gap.
- `Moments/FirstAmplificationChoice.lean` — blob `1e7a23d2f1319bd7a025a0ee8148a577c685b52d`, `ballProfile` and positivity.
- `Energy/CanonicalMainGaussian.lean` — blob `149d54db73c4a8ca82646702cba3346c2b57c054`.
- `Energy/CanonicalErrorGaussian.lean` — blob `1239786517727b801e0553c53a672003a92c8274`.

### Claim ledger

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-PAIR-CONDUCTOR-GAUSSIAN/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
MATHEMATICAL PROOF: finite Plancherel, coprime zero-mean,
 pair-conductor Poisson asymptotic with Schwartz error,
 genuine main/error source Gaussian bound, explicit valid high-radius regime
EXACT FINITE ADVERSARY: see committed script/CHAD receipt
LEAN FORMALIZATION OF NEW LEMMA: NOT PERFORMED
HIGH-CONDUCTOR / SHARED-PRIME SHARP CHILD ENERGY: OPEN
SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
