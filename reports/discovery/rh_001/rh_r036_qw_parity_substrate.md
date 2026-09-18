# RH-R036 — Source audit for Weil-form inversion and parity-gap reduction

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#264
- Exact Forge base: 564f6e2b41c9b13334bc8a5b84914a85c6b70790
- Protected predecessor audit: grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790
- Audit date: 2026-09-18
- Scope: source substrate for the first Zeta Spectral Triples missing theorem
- Novelty / priority / RH / certification claims: none

## 1. Primary source

Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755 (2025; EMS lecture-series publication announced for 2026).

The R035 audit established that the source's first explicit missing step is to prove that, for the full semilocal Weil quadratic form \(QW_\lambda\), the lowest eigenvalue is simple and has an even eigenvector.

The present audit asks only whether the source already supplies enough operator-theoretic and symmetry structure to reduce that open statement to a parity-sector problem.

## 2. Inversion symmetry

On

\[
\mathcal H_\lambda
=
L^2([\lambda^{-1},\lambda],d^*u),
\qquad
d^*u=\frac{du}{u},
\]

define the inversion involution

\[
(Jf)(u)=f(u^{-1}).
\]

Because the interval is inversion invariant and \(d^*u\) is invariant under \(u\mapsto u^{-1}\), \(J\) is a unitary involution:

\[
J^*=J,\qquad J^2=I.
\]

The source explicitly identifies a symmetry of the Weil sesquilinear form under the inversion

\[
\iota(u)=u^{-1}.
\]

Its Lemma 3.1 writes the Weil functional through the inversion-symmetrized combination

\[
\Psi(h)
=
\Psi^\#(h)+\Psi^\#(h\circ\iota).
\]

The finite-interval formula for \(QW_\lambda\) is correspondingly built from inversion-paired terms.

Source-level disposition:

\[
QW_\lambda
\quad\text{is inversion symmetric.}
\]

The exact operator commutation consequence is left to MATHSOLVE as a standard closed-form theorem; MATHFORGE does not manufacture it here.

## 3. Canonical self-adjoint operator associated with the form

The source proves that \(QW_\lambda\) is:

- lower bounded;
- lower semicontinuous;
- densely defined through the stated core.

By the representation theorem for lower-bounded closed quadratic forms, the paper associates a canonical lower-bounded unbounded self-adjoint operator

\[
A_\lambda
\]

on \(\mathcal H_\lambda\) satisfying, at form level,

\[
QW_\lambda(f,f)
=
\langle A_\lambda f,f\rangle
\]

on the appropriate operator/form domain.

This is an exact source theorem.

## 4. Discrete spectrum

The source then proves that \(A_\lambda\) has discrete lower-bounded spectrum.

Thus, for each fixed \(\lambda>1\):

- the bottom of the spectrum is an eigenvalue;
- eigenspaces have finite multiplicity;
- the spectrum can be organized variationally.

This is precisely the setting needed for a parity-sector comparison.

## 5. Source's first named missing theorem

Section 8 of the source states that a first essential missing step is to prove that the smallest eigenvalue of \(QW_\lambda\):

- is simple;
- has an even eigenvector \(\xi_\lambda\).

Existence of a smallest eigenvalue is already ensured by the discrete-spectrum theorem.

Accordingly, the open content is not existence. It is:

\[
\text{parity}
+
\text{multiplicity}.
\]

## 6. Admissible parity reduction

The source facts above support the following Solve-native reduction, subject to an exact form-symmetry-to-operator-commutation proof.

If the self-adjoint operator \(A_\lambda\) commutes with \(J\), then

\[
\mathcal H_\lambda
=
\mathcal H_{\lambda,+}
\oplus
\mathcal H_{\lambda,-},
\]

where

\[
\mathcal H_{\lambda,\pm}
=
\ker(J\mp I),
\]

and both parity subspaces reduce \(A_\lambda\).

Let

\[
\epsilon_+(\lambda)
=
\min\sigma(A_\lambda|_{\mathcal H_{\lambda,+}}),
\]

\[
\epsilon_-(\lambda)
=
\min\sigma(A_\lambda|_{\mathcal H_{\lambda,-}}).
\]

Because the spectrum is discrete and lower bounded, these minima are eigenvalues whenever the corresponding parity sector is nonzero.

Then the source's open "simple-even ground state" statement would be equivalent to:

1. the lowest even eigenvalue \(\epsilon_+(\lambda)\) is simple; and
2. the strict parity gap holds:

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

The equivalence itself is elementary once the reducing decomposition is established and is suitable for MATHSOLVE.

## 7. Why this is a material narrowing

The source phrase "prove the ground state is simple and even" packages two logically distinct obligations.

The parity reduction separates them.

### Obligation A — within-sector simplicity

Prove that the bottom eigenvalue of

\[
A_\lambda|_{\mathcal H_{\lambda,+}}
\]

has multiplicity one.

### Obligation B — cross-sector ordering

Prove

\[
\epsilon_+(\lambda)
<
\epsilon_-(\lambda).
\]

Failure modes become explicit:

- if \(\epsilon_->\epsilon_+\) but the even ground eigenspace has dimension greater than one, the source hypothesis fails by multiplicity;
- if \(\epsilon_-=\epsilon_+\), the global ground state cannot be simple because even and odd eigenvectors coexist at the bottom;
- if \(\epsilon_-<\epsilon_+\), the global ground state is odd.

This is a sharper theorem target than a generic ground-state claim.

## 8. Finite truncations

The source's finite matrices \(QW_\lambda^N\) inherit the inversion/parity structure through the symmetric basis index range \(|n|\le N\).

At finite \(N\), the same conceptual split can be implemented as even and odd blocks.

This gives a useful diagnostic:

- exact or interval-certified finite parity gaps may test the proposed mechanism;
- numerical finite gaps do not prove the full-\(QW_\lambda\) parity gap;
- convergence of finite block bottoms to the full parity-sector bottoms would itself need proof for an all-\(\lambda\) theorem.

No finite computation is promoted to the full missing theorem by this audit.

## 9. Claim boundary

This audit does **not** prove:

- that \(A_\lambda\) commutes with inversion at operator level;
- that the lowest even eigenvalue is simple;
- that \(\epsilon_+(\lambda)<\epsilon_-(\lambda)\);
- that either property holds for all \(\lambda>1\);
- the second source missing step involving \(k_\lambda\to\xi_\lambda\);
- determinant convergence to \(\Xi\);
- RH.

It only protects the source facts needed for the next bounded reduction.

## 10. Smallest Solve successor

The admissible next target is

RH-R036-QW-PARITY-GAP-REDUCTION-001.

It should prove from the protected source inputs and standard form theory:

1. inversion invariance of the closed form implies

\[
A_\lambda J=J A_\lambda;
\]

2. even and odd subspaces reduce \(A_\lambda\);

3. with discrete lower-bounded spectrum, the source's "simple-even lowest eigenvalue" condition is equivalent to:
   - simple lowest even eigenvalue;
   - strict parity gap \(\epsilon_+<\epsilon_-\).

This successor is a reduction theorem only. The parity gap remains the subsequent mathematical frontier.

## 11. Audit disposition

SOURCE_SUBSTRATE_CONFIRMED__SIMPLE_EVEN_PROBLEM_ADMITS_PARITY_GAP_REDUCTION

The first Zeta Spectral Triples missing theorem can be narrowed to a symmetry-reduced spectral problem without strengthening the source claim.
