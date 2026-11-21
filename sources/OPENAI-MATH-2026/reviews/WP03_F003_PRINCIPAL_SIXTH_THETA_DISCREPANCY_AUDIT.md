# OAI-26 F003 — exact principal sixth-power theta discrepancy and sharp origin obstruction

**Assignment:** GCL-OAI26-F003-PRINCIPAL-SIXTH-DISCREPANCY/1  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Predecessor:** MATHFORGE PR #582; protected admission must be read back before this separate tranche is admitted.  
**Disposition:** `PRINCIPAL_SIXTH_POWER_LOCAL_CRITICAL_DISCREPANCY_EXACT__ZERO_MODE_CANCELLATION_PROVED__ORIGIN_BARRIER_SHARP__GLOBAL_CHILD_ENERGY_OPEN`  
**Authority:** mathematical reconstruction; new special-case identities not independently Lean-elaborated; no MATHCERT.

## 1. Actual principal sixth-power pair

Fix a source-supported good maximal Eisenstein prime \((p)\), \(q=N((p))>1\), and positive exponents \(c<d\) with **both \(6\mid c\) and \(6\mid d\)**. The normalized actual Gauss row `gaussRow(p^e,z)` is \(g_e(z)=q^{-e/2}\texttt{sexticGauss}(p^e,z)\). This is the real **principal-larger-power** case excluded from the nonprincipal square-root completion of PR #581.

Pinned `Detector/Sextic.lean:actualSextic_pow_eq_one_iff` (blob `7637e778920da530c04b8ca5dea16dfcede93bf1`), `Detector/GaussValuation.lean:primePowerGauss_at_pow_principal` (blob `6a36e548dcdcd3ea39d326e5351c15c5db11619b`), `Detector/LocalPhysical.lean:sexticGauss_prime_power` (blob `e936163fe9fc53cc0f3538331701fb4203a3fb62`) yield

\[
g_e(z)=q^{e/2-1}
\begin{cases}
q-1,&p^e\mid z,\\
-1,&p^{e-1}\mid z,\ p^e\nmid z,\\
0,&p^{e-1}\nmid z.
\end{cases}
\qquad (6\mid e).
\tag{P1}
\]

All values are real. The source `ballProfile` is denoted \(\Phi\), with \(\Phi(0)=1\), \(\Phi\ge0\), \(\Phi(x)=0\) on \(x\ge2\), and smooth.

## 2. Exact two-scale lattice discrepancy identity

Define, for every \(t>0\),

\[
H_\Phi(t):=\sum_{z\in O}\Phi(N(z)/t),\qquad
T:=K/q^{d-1}.
\]

The mixed actual-source row kernel is \(\mathcal P_{d,c}(\Phi,K):=\sum_{z\in O}g_d(z)\overline{g_c(z)}\Phi(N(z)/K)\).

Insert the **exact** Gauss row values (P1). Since every contributing \(z\) is divisible by \(p^{d-1}\), put \(z=p^{d-1}u\). At \(p\nmid u\) the product is \(-(q-1)q^{(c+d)/2-2}\); at \(p\mid u\) the product is \((q-1)^2q^{(c+d)/2-2}\). As \(N(p)=q\) and \(u=pv\) runs exactly over multiples of \(p\), one obtains

\[
\boxed{\displaystyle
\mathcal P_{d,c}(\Phi,K)=
(1-q^{-1})q^{(c+d)/2-1}
\left[q\,H_\Phi(T/q)-H_\Phi(T)\right].}
\tag{P2}
\]

This simplifies PR #580's E2 exactly. It is valid for any radial cutoff with convergent sums, including the genuine smooth \(\Phi\), and any \(K>0\). The coefficient contains no untracked unit, conductor, or extra lattice-covolume factor.

**Zero-mode cancellation:** pinned `GaussSum/SexticRadialPoisson.lean:actual_radial_paper_poisson_trace` (blob `d06abef7f561b28392ed3a27e0c58227e5493c37`) applied with unit period gives, for \(G_\Phi=\texttt{paperRadialFourier}(\Phi)\),

\[
H_\Phi(t)=t\sum_{h\in O}G_\Phi(tN(h)).
\]

Therefore

\[
\boxed{\displaystyle
qH_\Phi(T/q)-H_\Phi(T)=
T\sum_{h\in O\setminus\{0\}}
\left[G_\Phi(TN(h)/q)-G_\Phi(TN(h))\right].}
\tag{P3}
\]

The \(h=0\) terms cancel **identically**: both lattice counts have exactly the same continuous leading area term. This is the single-pair geometric counterpart of the full distinct-ideal zero-Fourier cancellation already proved in pinned `Moments/SecondDiagonal` and admitted PR #579.

## 3. Uniform principal critical estimate, and its sharp obstruction

For fixed smooth compact \(\Phi\), standard norm-ball counting gives \(0\le H_\Phi(t)\le C_\Phi(1+t)\) for all \(t>0\). Therefore, if \(T\le q\),

\[
|qH_\Phi(T/q)-H_\Phi(T)|\le C_\Phi q.
\]

For \(T\ge q\), since the \(h=0\) term has canceled in (P3), arbitrary Schwartz decay implies, for each fixed integer \(B\ge3\),

\[
|qH_\Phi(T/q)-H_\Phi(T)|
\le C_{B,\Phi}\,T(q/T)^B
= C_{B,\Phi}\,q(q/T)^{B-1}.
\]

Consequently

\[
\boxed{\displaystyle
|\mathcal P_{d,c}(\Phi,K)|
\le C_{B,\Phi}\,q^{(c+d)/2}
\min\left(1,\left(\frac{q}{T}\right)^{B-1}\right),
\quad T=K/q^{d-1},\quad c<d,\ 6\mid c,d.}
\tag{P4}
\]

This closes the **local principal pure-prime-power critical-radius estimate** for every \(T>0\), including the interval where low-radius origin and large-radius Poisson bounds meet.

**Exact low-radius barrier.** If \(2T\le1\), all nonzero Eisenstein lattice elements have norm at least one, so \(H_\Phi(T/q)=H_\Phi(T)=1\). Thus

\[
\boxed{\displaystyle
\mathcal P_{d,c}(\Phi,K)=(1-q^{-1})^2q^{(c+d)/2}
\ne0\qquad(2K\le q^{d-1}).}
\tag{P5}
\]

This is a matching-order lower witness to (P4), uniform in the prime norm \(q\). Thus there is **no per-pair prime-norm power saving** for all principal sixth-power pairs and all positive radii. Such a saving can only come after charging the actual coefficients, conductors and allowed radii or exploiting cancellations across pairs. This observation does **not** refute the full seven-eighths theorem, whose source has additional hypotheses.

## 4. Updated exact local critical dichotomy

Combining with admitted PR #581:

- For \(6\mid c<d,\ 6\nmid d\), the critical pair is a nonprincipal short sextic character sum, bounded by uniform \(O(\sqrt q)\) after smooth completion and with exact unit-orbit annihilation when norms differ modulo 36.
- For \(6\mid c<d,\ 6\mid d\), the critical pair is the explicit signed lattice discrepancy (P2). Its Fourier zero mode cancels, but its **lattice-origin contribution** persists and has optimal size \(q^{(c+d)/2}\).
- For \(6\nmid\min(c,d)\), unequal-prime-power Gauss row products are pointwise zero (admitted PR #579).

The **local pure-prime-power critical regime is now analytically bounded in all three cases**, under the pinned genuine source definitions. This is not the full global main/error energy proof: composite CRT phases, cross-prime sectors within the six unit eigenspaces, the coefficient-weighted number of surviving pairs, source `ZeroAt`/`PositiveAt`, radius/height/mesh, and the four seeded Gaussian powers remain.

## 5. Evidence discipline

The companion `f003_principal_sixth_theta_discrepancy_adversary.py` exactly checks P2 by two **independently implemented** finite expressions: a direct prime-power Gauss valuation pair sum over actual Eisenstein integer representatives, and the difference \(qH(T/q)-H(T)\). It checks rational radial **step profiles** and the origin limit for many permissible q and T, plus the coefficient normalization. Step-profile computations are *not* replays of the smooth source `ballProfile` or of infinite Poisson; the universal source result comes from the analytic reconstruction above.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-PRINCIPAL-SIXTH-DISCREPANCY/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
SOURCE INPUTS: exact principal prime-power Gauss table; primitive lattice Poisson
MATH PROOF: P2 exact signed theta difference; P3 exact cancellation of
 continuous zero Fourier mode; P4 uniform principal critical bound;
 P5 low-radius sharp origin barrier
NEW LEAN ELABORATION: NOT PERFORMED
ALL LOCAL PRIME-POWER CRITICAL CASES: MATH BOUNDS RECONSTRUCTED
COMPOSITE SHARP MAIN/ERROR CHILD ENERGY: OPEN
SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
