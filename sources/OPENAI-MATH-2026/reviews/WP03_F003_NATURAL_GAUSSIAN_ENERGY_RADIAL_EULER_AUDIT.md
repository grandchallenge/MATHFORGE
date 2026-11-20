# F003 — Independent actual Gaussian energy and radial Euler audit

**Assignment:** `GCL-OAI26-F003-NATURAL-GAUSSIAN-RADIAL/1`  
**Immutable upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Disposition:** `RADIAL_EULER_MATH_PROVED__ACTUAL_GAUSSIAN_COARSE_BOUND_PROVED__SHARP_MAIN_ERROR_CHILD_ENERGIES_OPEN`  
**Family 003:** unresolved. **MATHCERT:** none.

## 1. Precise target and source identities

The two requested targets are `Energy/CanonicalMainGaussian.lean:actual_main_gaussian_from_bands` (blob `149d54db73c4a8ca82646702cba3346c2b57c054`) and `Energy/CanonicalErrorGaussian.lean:actual_error_gaussian_from_bands` (blob `1239786517727b801e0553c53a672003a92c8274`). They are conditional on **previous-stage** `ZeroAt` and `PositiveAt`, defined by `Energy/Bands.lean` (blob `a565218399cadcd62d92fbb47313631847c1ff4f`). A `ZeroAt` bound controls `s.plainEnergy` in a fixed-modulus, bounded-width natural state. `PositiveAt` controls a live prime-annular `energy` with relative ray characters and `HeckePrimeAnnular.annularWeight`. Both have the required diagonal, profile, height and `Z^(width+epsilon)` factors.

The genuine main child is `input = child src C R0 B tau t`, with normalization modulus `R0*C` and radius `Kmain`; the genuine error child is `input = errorInput src C R0 B tau t (span{p}) k Bp upsilon v0`, normalization modulus `(R0*C)*(span{p})^k`, and radius `Kerror`, for `k in {1,6,7}`. The Gaussian theorems bound `normalizedGaussSource` by four **seeded Gaussian powers** times `mass input ^ 2`.

The actual proof chain is `CanonicalMainGaussian -> CanonicalMainUniform -> CanonicalMainPaid -> CanonicalUniformReference -> CanonicalReferencePaid`, and `CanonicalErrorGaussian -> CanonicalErrorUniform -> CanonicalErrorPaid -> CanonicalNestedReference -> CanonicalReferencePaid`, alongside `Moments/FirstSeededGaussianPower` and `Moments/FirstNestedSeededGaussianPower`. These latter lemmas sum and normalize child-energy inequalities; their successful elaboration does **not** independently derive the sharp analytic input. Both routes ultimately rely on `CanonicalReferencePaid.actual_reference_paid_source`. The nested route must hold uniformly for two successive finite subset restrictions.

## 2. Independent genuine-source Gaussian-energy inequality (coarse, not sharp)

From pinned `Moments/GaussEnergy.lean` (blob `200d3d5c9fb828b7bd1eb4e5a7160b10c5fd65bd`) and `Moments/AmplificationChildInput.lean` (blob `90d172571cce6192d42d5751618619de302acd6a`), let `Q=(original s R seed).columns`, let `beta(I)=(original s R seed).beta I`, and put

$$
P_s(z)=\sum_{I\in Q}\beta(I)h_{\eta,t}(I)g_I(z),
\qquad
g_I(z)=\frac{\mathrm{sexticGauss}(a_I,z)}{\sqrt{N(I)}}.
$$

Every `I` is supported and nonzero. `heightCoeff` has modulus at most one, and the finite Gauss sum has at most `N(I)` summands of modulus at most one. Therefore `|g_I(z)| <= sqrt(N(I))` and

$$
|P_s(z)|\le A(s;R,\mathrm{seed})
:=\sum_{I\in Q}|\beta(I)|\sqrt{N(I)}.
$$

The **actual** `ballProfile` is `QuadraticInitialBound.sieveCutoff`, not `paperRadialFourier`. It is real, nonnegative, at most one and vanishes on nonnegative arguments at least 2 (`Moments/FirstAmplificationChoice.lean`, blob `1e7a23d2f1319bd7a025a0ee8148a577c685b52d`). The Gaussian energy is `sum_z |P_s(z)|^2 ballProfile(N(z)/K)`; its real part divided by `volume(s)>0` is precisely `normalizedGaussSource`. Thus for **every actual source**, including both main and nested error children, and every `K>0`,

$$
\boxed{0\le\mathrm{normalizedGaussSource}(s,R,\mathrm{seed},\mathrm{ballProfile},K)
\le \frac{(1+4\sqrt K)^2}{\mathrm{volume}(s)}
\left(\sum_{I\in Q}|\beta(I)|\sqrt{N(I)}\right)^2.}
$$

Indeed, an active row must have `N(z)<2K`. Writing `z=a+b omega`, `2N(z)=a^2+b^2+(a-b)^2 >= a^2+b^2`; therefore `|a|,|b|<2 sqrt(K)`, with at most `(1+4 sqrt(K))^2` lattice points. This is an **analytic bound for the genuine source families**, not a finite analogue. It is **too coarse** for the seven-eighths exponent: the sum of `|beta(I)|sqrt(N(I))` carries all column/conductor costs and ignores the cancellation required for the four target seeded powers.

## 3. Independent actual radial Fourier Euler bound

Pinned `Poisson/RadialFourier.lean` (blob `aa523f187da7bab91ce9000682ee730ec8ddd478`) gives the **specific** normalization

$$
G_W(t)=\mathrm{paperRadialFourier}(W)(t)
=\frac{2}{\sqrt3}\,
\widehat{\left[z\mapsto W(|z|^2)\right]}
\left(\frac{2i}{\sqrt3}\sqrt{t}\right),\quad t>0.
$$

For the source's smooth compactly supported `Wslot`, the two-dimensional function `f(z)=Wslot(|z|^2)` is Schwartz: every derivative is a finite sum of polynomial factors times derivatives of the compactly supported `Wslot`. Ordinary Fourier integration by parts gives rapid decay of all derivatives of `hat f`. Let

$$
F(r)=\frac2{\sqrt3}\hat f\left(\frac{2i}{\sqrt3}r\right),
\quad G_W(t)=F(\sqrt t),\quad D=t\frac{d}{dt}.
$$

The restriction `F` is Schwartz on the real line. At `r=sqrt(t)`, **exactly** `D=(r/2)d/dr`; hence by induction and the Stirling number identity,

$$
D^jG_W(t)=2^{-j}\sum_{m=0}^{j}{j\brace m}\,r^m F^{(m)}(r)
\big|_{r=\sqrt t}.
$$

Each factor `sup_{r>=0}(1+r^2)^A r^m |F^(m)(r)|` is finite. Therefore **for all** integers `A,J>=0` there is a finite source-dependent constant `C(Wslot,A,J)` with

$$
\boxed{\forall j\le J,\ t>0:\quad (1+t)^A|D^jG_W(t)|\le C(Wslot,A,J).}
$$

This is the specialized radial Euler estimate previously imported by the annular log-Fourier argument, independently derived from the actual transform and constants. The Gaussian test `W(u)=exp(-pi u)` yields the normalization check `G_W(t)=2/sqrt(3)*exp(-4*pi*t/3)`. This noncompact Schwartz test is **only a check**, not the source's compactly supported profile. A separate source-independent Lean elaboration is not claimed.

## 4. Conductor, energy-loss and radius accounting

Put `q=log_Z N(p)`, `d=Mdecl-(log_Z K + log_Z N(src.eta.modulus))`, and

$$
B=2Bcap\,\varepsilon_{mask}+\varepsilon_{child}+\varepsilon_{remove}
+\frac{d+\delta+\mathrm{reserve}+\theta_{source}}6
+\frac{\theta_{clip}}3+\kappa\,\mathrm{mesh}.
$$

The **exact child envelope** expenditures are

$$
L_{main}=B+\sigma/3,\quad L_{error}(k)=B+kq,
\qquad k\in\{1,6,7\}.
$$

The source defines `errorRemoval(p,Z,k)=k q`, while `errorMoving(p,Z,6)=0` and `errorMoving(p,Z,1)=errorMoving(p,Z,7)=q`. The reference conductor inputs are `Qmain=cost*N(tau.modulus)` and `Qerror=Qmain*Z^errorMoving`. The nested error character must **additionally** satisfy `N(upsilon.modulus)<=Qerror`; the main child requires the **exact** conductor identity for `tau.modulus`. Nonzero physical blocks must satisfy the separate family-character width gate `log_Z(dyadicScale)+log_Z N(family(chi).modulus)<=Mcap`. None is automatic for an arbitrary character.

Using pinned `Moments/AmplifiedRetainedRadius.lean` (blob `f6d0c98a4212c85ac9de0c0ce7de35f519383d89`), with `x=d0-c`,

$$
\begin{aligned}
\log_Z K_{main}&=K_0+\max(x,0)+2\sigma+\delta+\mathrm{reserve},\\
\log_Z K_{error}&=K_0+\max(x-2kq+m_k,0)+\sigma+\delta+\mathrm{reserve},
\end{aligned}
$$

where `m_k` is respectively `q,0,q` and the inside-max decrements are `-q,-12q,-13q`. Under `Z>1, sigma>=0, q>=sigma/6>=0`, this independently yields **`Kerror<=Kmain/Z^sigma`**. Moving charge, removal charge, and radius are three **different** invoices.

**Hostile shortcut rejected:** `Lerror-Lmain=kq-sigma/3` can be negative for `k=1`, even under the required prime-scale condition. Take `q=sigma/6>0`: the difference equals `-sigma/6`. This is not evidence of an existing upstream bug; it invalidates an unjustified monotonicity shortcut.

## 5. Validation and decisive remaining gate

The independently authored stdlib adversary `f003_natural_gaussian_euler_adversary.py` executed **6,712 exact assertions**, including the Eisenstein norm identity on a 35x35 integer grid, seven compact-ball lattice counts, **1,080** permissible conductor/loss/radius cases across `k=1,6,7`, a hostile `k=1` loss comparison, the `k=6` moving-charge mutation and independent Gaussian Euler polynomial recurrences for degrees 0–11. This is finite supporting evidence; it is not a universal proof or a MATHCERT certificate.

The **substantive unclosed obligation** is to independently derive the *sharp* actual `childEnergy` inequalities from the preceding `ZeroAt` and `PositiveAt` estimates, with `envelopeRef`, `ratioPenalty^(1/6)`, the full `Z` exponents, the main and nested error conductor-width conditions, and the four seeded-power coefficients. In particular, reproduce the analytic argument behind `Energy/CanonicalReferencePaid.actual_reference_paid_source` for genuine source coefficients, not merely its formally stated transport. The coarse bound in §2 cannot substitute for this. Only then can the high-stage induction and full seven-eighths claim be revisited. The Family 003 theorem is **not independently proved** and **no MATHCERT certification** has been issued.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-NATURAL-GAUSSIAN-RADIAL/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
PROVED (MATHEMATICAL NOTE): exact-normalization radial Euler bound;
 genuine-source coarse Gaussian-energy bound; radius/conductor/loss identities
EXACT TESTS: 6712 PASS (1080 source-accounting parameter cases)
SHARP MAIN/ERROR GAUSSIAN CHILD ENERGIES: OPEN
FAMILY003: UNRESOLVED
MATHCERT: NONE
```
