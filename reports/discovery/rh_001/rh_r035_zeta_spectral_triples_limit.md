# RH-R035 — Prior-art audit for Zeta Spectral Triples and the limiting-operator contract

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#262
- Exact Forge base: 2e66cdb836ea4228d70462f5eddca73ee91a504a
- Protected predecessor audit: grandchallenge/MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a
- Audit date: 2026-09-18
- Scope: exact source/prior-art and limiting-operator contract audit
- Novelty / priority / RH / certification claims: none

## 1. Primary source and current publication state

Primary source:

Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755 (submitted 2025-11-27), published in the EMS Series of Lectures in Mathematics in 2026.

The source proposes a spectral route to RH based on self-adjoint rank-one perturbations of the scaling operator on a finite multiplicative interval. The construction is explicitly arithmetic: at finite scale it uses the restricted Euler product / Weil quadratic form involving only primes up to the scale bound.

The source itself states that a rigorous proof of the relevant spectral convergence would establish RH and devotes its final section to the missing steps.

Accordingly, this audit treats the finite operator theorems as source results and the limiting RH conclusion as open.

## 2. Exact finite operator family

Fix \(\lambda>1\), let

\[
L=2\log\lambda,
\]

and consider the scaling operator

\[
D_{\log}^{(\lambda)}
=
-i\,u\frac{\partial}{\partial u}
\]

on

\[
L^2([\lambda^{-1},\lambda],d^*u),
\qquad
d^*u=\frac{du}{u},
\]

with periodic boundary conditions.

Let \(E_N\) be the span of the \(2N+1\) scaling eigenfunctions of smallest absolute eigenvalue, and let \(QW_\lambda^N\) be the restriction of the semilocal Weil quadratic form to \(E_N\).

Let \(\epsilon_N\) be the smallest eigenvalue of \(QW_\lambda^N\), and let \(\xi\) be a corresponding eigenvector.

Under the theorem's stated assumptions that:

- \(\epsilon_N\) is simple;
- \(\xi\) is even under \(u\mapsto u^{-1}\);
- \(\xi\) is normalized by the boundary-evaluation approximation \(\delta_N(\xi)=1\);

the source defines the rank-one perturbation

\[
D_{\log}^{(\lambda,N)}
=
D_{\log}^{(\lambda)}
-
\left|D_{\log}^{(\lambda)}\xi\right\rangle
\left\langle\delta_N\right|.
\]

The source proves self-adjointness on the direct-sum space described in its Theorem 5.10, with the induced inner product on the quotient component \(E_N' = E_N/\mathbb C\xi\).

This is an exact finite theorem conditional on the stated simple-even hypothesis.

## 3. Arithmetic input and noncircularity at finite scale

The semilocal Weil quadratic form has the explicit prime contribution

\[
-\sum_{1<n\le \lambda^2}
\Lambda(n)\langle f,T(n)f\rangle.
\]

Equivalently, only primes and prime powers with scale \(p^m\le\lambda^2\) enter the finite construction.

The source therefore satisfies an important campaign gate:

\[
\boxed{\text{finite approximants are built from prime/arithmetic data, not from a supplied list of zeta zeros}}
\]

No target ordinate appears as an adjustable boundary parameter in the finite operator definition.

This is materially stronger than the zero-specific domain tuning identified in RH-R034.

## 4. Exact finite spectral theorem

Under the simple-even hypothesis above, the source proves:

1. \(D_{\log}^{(\lambda,N)}\) is self-adjoint;
2. its regularized determinant is

\[
\det_{\mathrm{reg}}
\left(D_{\log}^{(\lambda,N)}-z\right)
=
-i\,\lambda^{-iz}\widehat{\xi}(z);
\]

3. \(\widehat{\xi}(z)\) is entire;
4. all zeros of \(\widehat{\xi}\) are real;
5. those zeros coincide with the spectrum of \(D_{\log}^{(\lambda,N)}\).

Thus each admitted finite approximant has a real spectral set generated through self-adjointness rather than by post-selecting complex roots.

The exact source result is finite-\((\lambda,N)\). It is not yet a theorem that these spectral sets equal the nontrivial zeta-zero ordinates.

## 5. Numerical convergence evidence

The source reports high-precision numerical agreement between the low spectrum of \(D_{\log}^{(\lambda,N)}\) and the low positive ordinates of the nontrivial zeta zeros.

The abstract and numerical section state that the observed spectra approach the zeta-zero ordinates as \(N,\lambda\to\infty\).

The source also studies the regularized determinants and the strategy of normalizing them so that they converge toward the Riemann \(\Xi\) function.

For the governed campaign, these are:

- strong numerical and analytic route evidence;
- not yet exact spectral convergence;
- not yet an admitted RH proof.

No probability-of-coincidence or numerical-accuracy statistic is used as proof evidence in this audit.

## 6. The limiting-operator boundary

The family

\[
D_{\log}^{(\lambda,N)}
\]

changes with \(\lambda\) and \(N\).

The source does not yet prove a theorem of the form:

\[
D_{\log}^{(\lambda,N)}
\longrightarrow
D_\infty
\]

in a specified operator topology for one limiting self-adjoint operator \(D_\infty\), together with spectral convergence sufficient to identify

\[
\sigma_{\mathrm{pt}}(D_\infty)
=
\{\gamma:\zeta(\tfrac12+i\gamma)=0\}
\]

with the protected multiplicity convention.

Instead, the paper explicitly states that rigorous convergence of the spectra as \(N,\lambda\to\infty\) would establish RH.

Therefore the exact current status is:

\[
\text{self-adjoint prime-built approximants}
+
\text{very strong numerical convergence evidence}
\neq
\text{proved limiting Hilbert–Pólya operator}.
\]

This is the controlling campaign boundary.

## 7. The two missing steps named by the source

Section 8 of the source identifies two essential missing steps.

### 7.1 Simple-even ground state for the full semilocal Weil form

To pass from finite truncations to the full \(QW_\lambda\) framework, the source states that one must prove that the smallest eigenvalue of \(QW_\lambda\):

- is simple;
- has an even eigenvector \(\xi_\lambda\).

Existence of a smallest eigenvalue is available from the source's operator-theoretic results, but the simple-even property remains to be proved.

This is not a cosmetic regularity issue. It is the hypothesis needed to deploy the finite rank-one self-adjoint construction in the intended limiting framework.

### 7.2 Control of the approximating vector \(k_\lambda\)

The source constructs a candidate approximation \(k_\lambda\) motivated by prolate/Sonin analysis.

The second missing theorem is to show that \(k_\lambda\) approximates the true minimal eigenvector \(\xi_\lambda\) sufficiently strongly to justify convergence of the zeros of

\[
\widehat{\xi_\lambda}
\]

toward the nontrivial zeta-zero ordinates.

This is the step that must turn numerical spectral proximity into a rigorous zero-convergence theorem.

## 8. Regularized-determinant route

The finite theorem gives

\[
\det_{\mathrm{reg}}
\left(D_{\log}^{(\lambda,N)}-z\right)
=
-i\,\lambda^{-iz}\widehat{\xi}(z).
\]

The source's limiting strategy is to control these determinants and show, after suitable normalization, convergence to the Riemann \(\Xi\) function.

This is analytically attractive because locally uniform convergence of entire functions, combined with appropriate nondegeneracy / Hurwitz control, can transfer information about zeros.

But the source does not yet prove the determinant convergence needed for an RH conclusion.

Therefore:

\[
\text{finite determinant identity}
\quad\text{is proved;}
\]

\[
\text{normalized determinant convergence to }\Xi
\quad\text{is a live target.}
\]

## 9. Campaign classification

| Gate | Result |
|---|---|
| prime/arithmetic input independent of zero list | passes |
| finite operator/domain fixed for each \((\lambda,N)\) | passes |
| self-adjoint finite approximants | passes under simple-even hypothesis |
| finite spectra real | passes |
| finite determinant formula | passes |
| low-zero numerical agreement | strong evidence |
| one fixed limiting self-adjoint operator | not established |
| rigorous spectral convergence to all zero ordinates | not established |
| simple-even property for full \(QW_\lambda\) | open |
| \(k_\lambda\to\xi_\lambda\) strong enough for zero convergence | open |
| normalized determinant convergence to \(\Xi\) | open |
| RH implication | not admitted |

## 10. False-proof firewall

Reject the following moves.

1. **Finite approximation to exact spectrum.** High-precision agreement for many low zeros is not equality of the complete spectrum.
2. **Family-to-operator substitution.** A sequence/family of self-adjoint operators is not automatically one limiting self-adjoint Hilbert–Pólya operator.
3. **Numerical convergence to spectral convergence.** Plots and high-precision tables do not prove convergence in an operator or spectral topology.
4. **Finite self-adjointness to limiting self-adjointness.** Self-adjointness of every finite approximant does not by itself establish self-adjointness or even existence of a limit.
5. **Simple-even assumption suppression.** The source's finite theorem assumes a simple-even minimal eigenvector; the global simple-even step remains an explicit missing theorem.
6. **Determinant heuristic promotion.** A proposed convergence of regularized determinants to \(\Xi\) is not an identity until the convergence theorem is proved.
7. **Real approximating zeros to RH.** Real zeros of the finite approximating entire functions do not prove that every zero of \(\Xi\) is real without the required limiting argument.
8. **Numerical probability as proof.** A small estimated chance of accidental agreement is route evidence, not mathematical proof.

## 11. Smallest Solve successor

A bounded Solve-native result may record the exact campaign advance as

RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001.

Positive component:

- current literature now provides zero-list-independent, prime-built, self-adjoint spectral approximants with exact real spectra and a finite regularized-determinant formula;
- this removes the target-dependent domain defect of RH-R034 at finite scale.

Negative / frontier component:

- the source has not yet produced the rigorous limiting operator/spectral convergence theorem needed for a Hilbert–Pólya realization;
- its own two named missing steps are the simple-even theorem for \(QW_\lambda\) and sufficiently strong \(k_\lambda\)-to-\(\xi_\lambda\) control;
- determinant convergence to \(\Xi\) remains a live route, not a proved identity.

After Solve records this result, the next substantive research target should be one of the source's two missing theorems rather than another unrelated spectral model.

## 12. Audit disposition

PRIME_BUILT_SELFADJOINT_APPROXIMANTS_CONFIRMED__RIGOROUS_LIMIT_CONVERGENCE_OPEN

This is the strongest audited spectral route in the current RH-001 sequence. It is not an admitted RH proof or a completed Hilbert–Pólya construction.
