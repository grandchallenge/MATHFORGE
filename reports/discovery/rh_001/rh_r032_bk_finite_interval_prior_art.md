# RH-R032 — Prior-art audit for finite-interval Berry–Keating realizations

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#255
- Exact Forge base: a6a2e7d65adef8eaf977d77bbacbd05786d7da47
- Protected predecessor Solve state: grandchallenge/MATHSOLVE@e7be48323953c653694f5824eb6c1738c0b63654
- Audit date: 2026-09-18
- Scope: exact finite-interval operator-class source/prior-art audit
- Novelty / priority / RH / certification claims: none

## Exact class

Fix \(0<a<b<\infty\). On \(L^2([a,b],dx)\) consider

\[
H_{BK}=-i\left(x\frac{d}{dx}+\frac12\right).
\]

Under

\[
(Wf)(y)=e^{y/2}f(e^y),
\qquad
\alpha=\log a,\quad \beta=\log b,
\]

this class is unitarily equivalent to the momentum operator

\[
P=-i\frac{d}{dy}
\]

on the finite interval \([\alpha,\beta]\).

The self-adjoint extensions are the \(U(1)\) family

\[
g(\beta)=e^{i\theta}g(\alpha),
\qquad \theta\in[0,2\pi),
\]

equivalently

\[
\sqrt b\,f(b)=e^{i\theta}\sqrt a\,f(a).
\]

Let

\[
L=\beta-\alpha=\log(b/a)>0.
\]

No energy-dependent endpoint, changing interval, graph topology, extra potential, rigged space, or nonlocal spectral rule is included in this exact class.

## Source status

This class is already inside established Berry–Keating operator literature.

1. Sebastian Endres and Frank Steiner, *The Berry–Keating operator on L²(R_>,dx) and on compact quantum graphs with general self-adjoint realizations*, Journal of Physics A 43 (2010) 095204, DOI 10.1088/1751-8113/43/9/095204.
   - The paper classifies self-adjoint Berry–Keating realizations on compact quantum graphs.
   - It derives discrete spectra, trace formulae, and Weyl asymptotics.
   - Its no-go theorem compares the linear compact-graph Weyl law with the Riemann-zero counting law and excludes these compact-graph realizations as exact zeta-zero spectra.

2. Fabio Bagarello and Sergiusz Kużel, *On the Berry-Keating Operator*, Complex Analysis and Operator Theory 20 (2026), article 135, DOI 10.1007/s11785-026-01990-w.
   - The current review confirms the full-line / half-line continuous-spectrum obstruction.
   - It explicitly recalls the compact-quantum-graph route and the established no-go result for reproducing the nontrivial zeta zeros.

The proposed single finite interval is the one-edge, fixed-geometry specialization of the compact class. Its exact spectrum can be derived directly and is simpler than the general graph theorem.

## Exact single-interval spectrum

For an eigenfunction \(g(y)=Ce^{iky}\), the quasi-periodic boundary condition gives

\[
e^{ik\beta}=e^{i\theta}e^{ik\alpha},
\]

hence

\[
e^{ikL}=e^{i\theta}.
\]

Therefore

\[
k_n=\frac{\theta+2\pi n}{L},
\qquad n\in\mathbb Z.
\]

The spectrum is a two-sided arithmetic progression. For positive eigenvalues, the counting function satisfies

\[
N_\theta(T)
=
\#\{n:k_n>0,\ k_n\le T\}
=
\frac{L}{2\pi}T+O(1).
\]

Changing \(\theta\) translates the arithmetic progression but cannot change the linear leading growth. Changing the fixed interval changes only the constant \(L/(2\pi)\).

## Comparison with the protected zeta-zero interface

The Riemann–von Mangoldt interface used by RH-001 has

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\left(\frac{T}{2\pi e}\right)
+O(\log T).
\]

Thus

\[
\frac{N_\zeta(T)}{T}
=
\frac{1}{2\pi}\log T+O(1)
\to\infty,
\]

whereas

\[
\frac{N_\theta(T)}{T}
\to \frac{L}{2\pi}.
\]

No fixed \(a,b,\theta\) can therefore make the finite-interval eigenvalue multiset equal to the positive nontrivial-zeta ordinate multiset, even asymptotically.

This mismatch precedes all questions about individual level fitting.

## Exact campaign consequence

The finite interval repairs the half-line failure of discreteness but immediately fails the required counting law.

The route now has the following obstruction chain:

\[
\text{bounded operator}
\;\Rightarrow\;
\text{spectral range too small},
\]

\[
\text{unbounded half-line Berry–Keating}
\;\Rightarrow\;
\text{continuous spectrum / no point spectrum},
\]

\[
\text{fixed finite-interval Berry–Keating}
\;\Rightarrow\;
\text{discrete spectrum but linear counting}.
\]

The zeta-zero target requires a discrete realization with \(T\log T\) leading count.

## Boundary against false escape routes

The following changes are not counterexamples to this audit because they leave the exact class.

- Make \(a\), \(b\), or \(L\) depend on the spectral cutoff \(T\).
- Use an energy-dependent boundary condition.
- Add a potential or nonlocal operator.
- Replace one interval by a graph with changing topology or energy-dependent geometry.
- Fit finitely many low levels while ignoring the asymptotic count.
- Apply a nonlinear transform to the eigenvalues.

Any such route needs its own exact source audit and must show that one fixed self-adjoint operator is being defined.

## Smallest Solve successor

A Solve-native theorem may safely record the exact spectrum and counting mismatch as

RH-R032-BK-FINITE-INTERVAL-WEYL-001.

This is known no-go mathematics, not a novelty claim. Its campaign value is to promote the Riemann–von Mangoldt growth law to a mandatory spectral-design test before any level-by-level fitting.

## Audit disposition

SOURCE_STATUS_CONFIRMED__FIXED_FINITE_INTERVAL_CLASS_FAILS_COUNTING_LAW

The exact class is admissible for bounded Solve replay and elimination.
