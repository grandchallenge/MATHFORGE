# RH-R033 — Prior-art audit for the cutoff-free symmetric Berry–Keating counting mechanism

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#258
- Exact Forge base: 5caba0069ab40a6c813c541c20512a4b9d981eed
- Protected Solve predecessor: grandchallenge/MATHSOLVE@f1716cde93738918e5a95e76a5a3157911f2d9b2
- Audit date: 2026-09-18
- Scope: exact operator-class and source/prior-art audit
- Novelty / priority / RH / certification claims: none

## 1. Exact audited class

The primary source is:

M. V. Berry and J. P. Keating, *A compact hamiltonian with the same asymptotic mean spectral density as the Riemann zeros*, Journal of Physics A: Mathematical and Theoretical 44 (2011) 285203, DOI 10.1088/1751-8113/44/28/285203.

The dimensionless classical Hamiltonian is

\[
H(x,p)=\left(x+\frac1x\right)\left(p+\frac1p\right).
\]

Its classical energy curves are bounded. The source quantizes the model on the positive half-axis, using the formal operator ordering

\[
\widehat H
=
\left(x+\frac1x\right)
\left(p+\frac1p\right)
\left(x+\frac1x\right),
\]

after the paper's state redefinition, with \(p=-i\eta\,\partial_x\) and the one-sided integral realization of \(1/p\). The spectral problem is represented equivalently by the integral equation (2.15) and the Schrödinger-like differential equation (2.8).

The half-line boundary data form a self-adjoint extension family indexed by an angle \(\alpha\). In the paper's transformed wavefunction \(\chi\), the boundary condition is

\[
\frac{\partial_x\chi(0)}{\chi(0)}
=
\frac1\eta e^{i\alpha}.
\]

The source states that, for each extension, the resulting operator has a discrete real spectrum. The square-integrable eigenstates decay at \(+\infty\).

This is one fixed operator realization for each fixed pair \((\eta,\alpha)\). No energy-dependent interval or cutoff is introduced.

## 2. Why this class is materially different from RH-R032

RH-R032 eliminated fixed finite-interval momentum because every such realization has

\[
N(T)=O(T).
\]

The present model changes the fixed classical geometry itself. Its closed phase-space area is

\[
A(E)
=
E\left[
K\left(1-\frac{16}{E^2}\right)
-
\mathcal E\left(1-\frac{16}{E^2}\right)
\right],
\]

with the source's elliptic-integral notation, and for large \(E\)

\[
A(E)
=
E(\log E-1)
-\frac{4\log E}{E}
+\cdots.
\]

Thus the extra logarithm arises from one fixed Hamiltonian's phase-space geometry; it is not inserted by making a boundary or interval depend on the spectral cutoff.

This is the first audited post-R032 class that passes the campaign's leading counting-mechanism gate.

## 3. Quantum self-adjointness and discreteness

The source derives the half-line hermiticity condition and states that each real \(\alpha\) specifies a different self-adjoint extension of the formal operator.

For fixed \(\alpha\):

- the eigenvalues are real;
- the eigenstates are square integrable;
- the spectrum is discrete;
- the eigenvalues are unbounded in magnitude;
- no finite spatial cutoff is used.

This clears the two earlier structural obstructions:

\[
\text{RH-R030: unboundedness required},
\]

and

\[
\text{RH-R031: point spectrum required}.
\]

It also avoids the fixed-finite-volume linear-Weyl obstruction of RH-R032.

## 4. Exact normalization used for comparison with Riemann–von Mangoldt

The source restricts the Riemann comparison to the self-adjoint extension \(\alpha=0\). It identifies

\[
E=\frac{t}{2\pi},
\qquad
\eta=\frac1{2\pi},
\]

equivalently \(l_xl_p=2\pi\hbar\).

For the Riemann zeros, the source records the smoothed counting function

\[
N_R^{\mathrm{sm}}(t)
=
\frac{t}{2\pi}
\left(
\log\frac{t}{2\pi}-1
\right)
+\frac78+\cdots.
\]

For the model eigenvalues, it obtains

\[
N_{H,\alpha=0}(t)
=
\frac{t}{2\pi}
\left(
\log\frac{t}{2\pi}-1
\right)
-
\frac{8\pi}{t}
\log\frac{t}{2\pi}
+\cdots.
\]

Therefore the first two large-\(t\) terms agree:

\[
\frac{t}{2\pi}\log\frac{t}{2\pi}
-
\frac{t}{2\pi}.
\]

The agreement is stronger than merely reproducing the growth order \(T\log T\), but it is not an exact Riemann–von Mangoldt match.

## 5. First exact mismatch

The same source explicitly states two failures.

### 5.1 Subleading smoothed-density mismatch

After the shared leading terms, the model's smoothed density differs from the Riemann-zero smoothed density. The first displayed correction terms have different forms and signs.

Thus:

\[
N_H(t)
=
N_R^{\mathrm{sm}}(t)
\]

is not an admitted identity, even at the smoothed asymptotic level beyond the leading pair.

### 5.2 Periodic-orbit / arithmetic mismatch

The source identifies a more fundamental obstruction.

For the classical Hamiltonian above, there is one primitive periodic orbit for each energy.

For the conjectural spectral dynamics associated with the zeta explicit formula, the periodic-orbit analogue is a family indexed by primes \(p\), with periods \(\log p\).

The paper states that its analysis gives no mechanism resolving this missing prime structure.

Accordingly, this exact operator class does not encode the oscillatory arithmetic term in the zero counting function.

## 6. Campaign classification

The exact class has the following governed status.

| Gate | Result |
|---|---|
| one fixed operator | passes |
| self-adjoint domain | passes for fixed extension parameter \(\alpha\) |
| unbounded spectral range | passes |
| discrete point spectrum | passes |
| leading \(T\log T\) counting | passes |
| leading linear correction | passes under the paper's Riemann normalization |
| full smoothed Riemann–von Mangoldt expansion | fails |
| prime-labelled periodic-orbit mechanism | fails / absent |
| exact raw zeta-zero spectrum | not established and explicitly not claimed by the source |
| RH implication | none |

## 7. False-proof firewall

The following moves are rejected.

1. Matching the first two asymptotic counting terms is not exact spectral correspondence.
2. A discrete real spectrum from self-adjointness does not constrain the real parts of zeta zeros unless an independently proved zero-to-eigenvalue correspondence exists.
3. The extension parameter \(\alpha\) may not be tuned separately for each eigenvalue.
4. Numerical level proximity may not replace the missing prime-orbit / fluctuation mechanism.
5. The source's use of “compact hamiltonian” refers to bounded classical orbits / the construction under study and must not be misread as a bounded-operator claim contradicting RH-R030.
6. The source itself denies an immediate zeta realization and records the subleading and prime-orbit mismatches.

## 8. Smallest Solve successor

A bounded Solve-native result may record the imported source asymptotics and prove the exact campaign comparison:

RH-R033-SYMMETRIC-BK-TLOGT-001.

The result should have a positive/negative form:

- **positive:** a fixed self-adjoint discrete operator class can pass the leading \(T\log T\) and linear-term counting gate;
- **negative:** those conditions are insufficient for a Hilbert–Pólya realization because the subleading smoothed density and prime-labelled fluctuation mechanism still fail.

The next mathematical frontier after that result is no longer “how to get \(T\log T\).” It is:

> what fixed self-adjoint spectral structure can generate the arithmetic fluctuation / prime-orbit content while preserving the already-correct smooth count?

## 9. Audit disposition

SURVIVES_LEADING_COUNT_GATE__FAILS_SUBLEADING_AND_PRIME_ORBIT_MATCH

The class is admissible as a positive-control Solve target. It is not admissible as an exact RH spectral realization.
