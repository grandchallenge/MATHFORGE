# F003 — uniform square-root completion of the genuine sextic radial critical sum

**Assignment:** GCL-OAI26-F003-SEXTIC-CRITICAL-COMPLETION/1  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Predecessor:** protected MATHFORGE PR #580, main `d21cb310f42ed7b059a51e1df6cb3e7dfff44e39`  
**Disposition:** `NONPRINCIPAL_PRIME_POWER_CRITICAL_RADIAL_SQRT_CANCELLATION_MATHEMATICAL_PROOF__COMPOSITE_GAUSSIAN_CHILD_ENERGY_OPEN`  
**Authority and limitation:** MATHFORGE bounded mathematical reconstruction, not an independently Lean-elaborated theorem, MATHCERT, or complete seven-eighths proof.

## 1. Actual character and source radial transform

Let \((p)\) be any supported good maximal Eisenstein prime ideal with \(p\ne0\), \(\mathrm{goodLambda}\notin (p)\), residue characteristic different from 2 and \(q=N((p))>1\). The pinned `Detector/Sextic.lean:actualSextic_pow_eq_one_iff` ensures the actual local \(\chi=\mathrm{actualSextic}((p))\) has exact order 6. Fix integer \(r\) with \(6\nmid r\) (use its residue \(1,\dots,5\)). Let \(\psi=\chi^r\), a genuinely nonprincipal multiplicative character of the finite residue field extended by zero to nonunits. Let \(\Phi=\texttt{CenteredMomentFirstAmplificationChoice.ballProfile}\), which is smooth compactly supported, real, nonnegative, at most 1, equals 1 for \(0\le x\le1\), and vanishes for \(x\ge2\). Define

\[
S_\psi(t)=\sum_{u\in O}\psi(u)\,\Phi(N(u)/t),\qquad t>0.
\]

This is precisely the incomplete sextic radial sum occurring in the critical nonprincipal larger-exponent primal identity (E1) of PR #580, up to complex conjugation. It is not an auxiliary one-dimensional character sum.

**Exact pinned inputs:**

- `GaussSum/SexticRadialPoisson.lean:actual_radial_paper_poisson_trace` (blob `d06abef7f561b28392ed3a27e0c58227e5493c37`), provides full periodic-lattice Poisson with the correct \(K/q\) and **source paperRadialFourier** argument \(KN(h)/q\).
- `Detector/HighRowsSharpScalar.lean:primeGauss_actual_pow_norm` (blob `62fc662a897ef22d6fea987e7df7a5990127afe4`) proves \(|\tau(\chi^r;1)|=\sqrt q\) for \(r\in\{1,\ldots,5\}\), with genuine finite primitive trace.
- `GaussSum/SexticRadialPoisson.lean` and `Detector/PrimePower.lean` give finite Gauss frequency change of variables; the unit-gate characterization is `CubicSieve/CutoffOrders.lean:actualSextic_unit_euler` (blob `f913c9856cfa3939f6d2339b839271002186bbfb`).
- `Poisson/RadialFourier.lean` (blob `aa523f187da7bab91ce9000682ee730ec8ddd478`) supplies rapid decay of the fixed transform \(G_\Phi=\texttt{paperRadialFourier}(\Phi)\), independently reconstructed in admitted PR #576.

## 2. Exact finite Fourier-completion identity

Finite Fourier transform of the actual nonprincipal \(\psi\) on \(O/(p)\) with primitive quotient trace satisfies

\[
\widehat\psi(h)=\sum_{x\bmod p}\psi(x)\,\texttt{quotientTrace}(p)(hx)
=\overline{\psi(h)}\,\tau_\psi,
\quad\text{where } \tau_\psi=\widehat\psi(1),\quad |\tau_\psi|=\sqrt q,
\]

including \(h=0\) since \(\psi(0)=0\). Therefore, by the pinned exact Eisenstein Poisson formula, for **every** \(t>0\),

\[
\boxed{\displaystyle
S_\psi(t)=\frac{t}{q}\tau_\psi
\sum_{h\in O}\overline{\psi(h)}
G_\Phi\left(\frac{tN(h)}q\right).
}
\tag{F1}
\]

The \(h=0\) term vanishes exactly: \(\psi(0)=0\). Note that one **must not** insert an extra \(2/\sqrt3\): it is already included in the definition of \(G_\Phi\).

## 3. Uniform square-root cancellation for all radii

Put \(\vartheta=t/q\). Since \(G_\Phi\) is a Schwartz radial Fourier transform, for any fixed integer \(B\ge3\) there is \(D_B>0\), depending on the fixed source cutoff only, such that

\[
|G_\Phi(x)|\le D_B(1+x)^{-B}\quad\text{for every }x\ge0.
\]

The Eisenstein lattice \(\mathbb Z[\omega]\), with \(N(a+b\omega)=a^2-ab+b^2\), has a universal counting bound
\(\#\{u:N(u)\le X\}\le C(1+X)\).
Dyadic shell summation implies, uniformly in \(\vartheta>0\),

\[
\sum_{h\in O\setminus\{0\}}(1+\vartheta N(h))^{-B}
\le C_B
\begin{cases}
\vartheta^{-1},&0<\vartheta\le1,\\
\vartheta^{-B},&\vartheta\ge1.
\end{cases}
\tag{F2}
\]

For small \(\vartheta\), split \(\vartheta N(h)\le1\) and dyadic shells beyond; for large \(\vartheta\), use \(\vartheta^{-B}\sum_{h\ne0}N(h)^{-B}\). Both constants are independent of \(p\), \(\psi\), \(r\), \(q\), \(t\).

Use (F1), \(|\tau_\psi|=\sqrt q\) and (F2). Thus

\[
\boxed{\displaystyle
|S_\psi(t)|\le
C_{B,\Phi}\sqrt q\,
\min\left(1,\left(\frac qt\right)^{B-1}\right),
\qquad t>0,\ B\ge3 .
}
\tag{F3}
\]

This is a **smooth two-dimensional square-root completion bound with no logarithmic loss**, for the actual sextic character, uniformly over all permissible primes and nonprincipal powers. It does not depend on a hypothetical zero-free region or on `ZeroAt`/`PositiveAt`.

An independent direct count using the *actual* compact support gives

\[
|S_\psi(t)|\le C_\Phi t\quad(t>0):
\]

for \(t\le1/2\) the sum vanishes since \(\psi(0)=0\) and \(N(u)\ge1\) for \(u\ne0\); for \(t>1/2\), the source cutoff restricts to \(N(u)<2t\), with \(O(1+t)=O(t)\) lattice points. Combine the two:

\[
\boxed{\displaystyle
|S_\psi(t)|\le
C_{B,\Phi}\min\left(
t,\sqrt q,\sqrt q(q/t)^{B-1}
\right),\qquad t>0,\ B\ge3.
}
\tag{F4}
\]

This is a strict improvement over the trivial \(O(t)\) for \(\sqrt q\ll t\lesssim q\) and gives arbitrarily fast decay for \(t\gg q\). If the global-unit selection \(6\nmid r(q-1)/6\) holds, then \(S_\psi(t)=0\) identically for all \(t\), a stronger exact statement from PR #580.

## 4. Transfer to the exact nonprincipal prime-power Gaussian mixed pair

Using the **genuine source-specific E1 identity** from admitted PR #580 with \(1\le c<d\), \(6\mid c\), \(6\nmid d\), \(t=K/q^{d-1}\), and the true prime-field Gauss norm \(|\tau(\chi^d;1)|=\sqrt q\), obtain

\[
\boxed{\begin{aligned}
|\mathcal P_{d,c}(\Phi,K)|
&\le C_{B,\Phi}(1-q^{-1})q^{(c+d-1)/2}
\min\left(t,\sqrt q,\sqrt q(q/t)^{B-1}\right)\\
&\le C_{B,\Phi}\,q^{(c+d)/2},
\qquad K>0 .
\end{aligned}}
\tag{F5}
\]

For \(t\ll\sqrt q\) one has an additional factor \(t/\sqrt q\), while for \(t\gg q\) there is arbitrary-order decay in \(t/q\). In the previously unresolved local \(p^6/p^7\) critical interval \(1/2<t<q\), the short sextic character sum is now bounded uniformly by \(C_\Phi\sqrt q\) (and by \(C_\Phi t\) for smaller t).

**Crucial limitation:** this closes the **local pure-prime-power nonprincipal critical sum** under smooth radial cutoff; it does **not** yield the full `CanonicalMainGaussian.actual_main_gaussian_from_bands` and `CanonicalErrorGaussian.actual_error_gaussian_from_bands` sharp four seeded factors. In particular, composite `sourceGenerator` columns, CRT phases, multiplying the total number/weights of pairs, nested conductor gates, and the \(6\mid d\) *principal larger-power* origin/lattice-discrepancy case remain. The analytic bound (F5) could even be too large after summing all pairs; it must not be silently installed as a sharp global inequality. No seven-eighths claim follows from (F5) alone.

## 5. Adversarial exact evidence and claim status

The committed no-dependency adversary `f003_sextic_radial_completion_adversary.py` represents sixth roots **exactly as Eisenstein integer pairs** and \(q\)-th roots as formal polynomials modulo \(\Phi_q(T)=1+\cdots+T^{q-1}\). For \(q=7,13,19,31,37\) (all prime, \(q\ne3\)) it independently checks \(|\tau(\chi^r)|^2=q\) and **all** finite-field frequency-scaling identities, across the nonprincipal sixth powers, using no floating-point values. It also checks bounded Eisenstein lattice tail comparators and compact-ball integer bounds. The latter are finite positive samples **not proofs of the infinite tail**; the rigorous dyadic argument is §3.

The repository evidence distinguishes:
- **pinned formal source:** finite Gauss norm, primitive Poisson, exact actual local source inputs;
- **independent mathematical derivation:** F1–F5 completion/critical estimates;
- **finite exact test:** arithmetic/cyclotomic consistency only;
- **still open:** original composite high-conductor main/error child-energy inequalities and all end-stage theorem certification.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-SEXTIC-CRITICAL-COMPLETION/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
MATH PROOF: exact completed sextic radial identity; universal O(sqrt(q)) 
 nonprincipal short character sum; O(min(t,sqrt(q))) compact variant;
 high-radius arbitrary decay; local p^6/p^7 critical nonprincipal bound
SOURCE LEAN: finite prime Gauss norm and periodic Poisson already proved
NEW LEAN ELABORATION OF F3–F5: NOT PERFORMED
COMPOSITE CHILD ENERGIES: OPEN
FAMILY003 SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
