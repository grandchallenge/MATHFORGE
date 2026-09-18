# RH-R037 — Source audit for finite parity blocks and Galerkin convergence

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#266
- Exact Forge base: 51042c94185cc9db1fa457ae40f26276747a0a4d
- Protected predecessor audit: grandchallenge/MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d
- Audit date: 2026-09-18
- Scope: finite-matrix and form-core substrate for the R036 parity-gap frontier
- Novelty / priority / RH / certification claims: none

## 1. Primary source

Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755.

R036 reduced the source's open simple-even ground-state theorem to:

1. simplicity of the lowest even eigenvalue;
2. the strict full parity gap

\[
\epsilon_+(\lambda)<\epsilon_-(\lambda).
\]

The present audit binds the exact finite-dimensional source structure needed to approximate those two sector bottoms without conflating finite evidence with the full theorem.

## 2. Increasing finite spaces

For fixed \(\lambda>1\), the source uses the orthonormal basis

\[
V_n(u)
=
U_n(\log(\lambda u)),
\qquad n\in\mathbb Z,
\]

of

\[
\mathcal H_\lambda
=
L^2([\lambda^{-1},\lambda],d^*u).
\]

For \(N\in\mathbb N\),

\[
E_N
=
\operatorname{span}\{V_n:|n|\le N\}.
\]

The union

\[
E=\bigcup_N E_N
\]

is a core for the closed semilocal Weil form \(QW_\lambda\).

The source proves that the full form lower bound is the limit of the smallest eigenvalues of the finite restrictions \(QW_\lambda^N\).

This exact unrestricted Galerkin convergence is source substrate for the sector-wise extension.

## 3. Exact finite matrix

Let

\[
T_N(\lambda)
=
\left(
QW_\lambda(V_n,V_m)
\right)_{|n|,|m|\le N}.
\]

The source proves that this is a real symmetric matrix of the form

\[
\tau_{i,i}=a_i,
\]

\[
\tau_{i,j}
=
\frac{b_i-b_j}{i-j}
\qquad(i\ne j),
\]

with

\[
a_{-j}=a_j,
\qquad
b_{-j}=-b_j.
\]

The source derives the entries from the explicit decomposition

\[
QW_\lambda
=
W_{0,2}
-
W_{\mathbb R}
-
\sum_p W_p.
\]

The components are explicitly computable:

- the \(W_{0,2}\) contribution has a closed rational/hyperbolic formula;
- the prime contribution is a finite von-Mangoldt sum over \(1<k\le e^L=\lambda^2\);
- the archimedean contribution is given by a convergent integral and explicit special-function formulas.

Thus exact or rigorously bounded finite parity calculations are mechanically available in principle.

## 4. Finite parity involution

The source defines

\[
\gamma(V_j)=V_{-j}.
\]

It proves

\[
\gamma^2=I,
\]

and, for every finite Weil matrix \(T_N(\lambda)\),

\[
T_N(\lambda)\gamma
=
\gamma T_N(\lambda).
\]

This is an exact source theorem, not an inferred numerical symmetry.

Therefore

\[
E_N
=
E_{N,+}
\oplus
E_{N,-},
\]

where

\[
E_{N,\pm}
=
\ker(\gamma\mp I).
\]

An explicit orthonormal parity basis is:

\[
V_0
\]

and, for \(1\le n\le N\),

\[
V_n^+
=
\frac{V_n+V_{-n}}{\sqrt2},
\]

\[
V_n^-
=
\frac{V_n-V_{-n}}{\sqrt2}.
\]

If a real basis is preferred for the odd sector, an immaterial factor of \(i\) may be inserted.

The finite matrix therefore decomposes exactly as

\[
T_N
=
T_{N,+}
\oplus
T_{N,-}.
\]

## 5. Source finite even-simple condition

The source defines a finite real symmetric matrix \(T\) commuting with the parity grading to be **even-simple** when:

- its smallest eigenvalue is simple;
- the corresponding eigenvector is even.

This is exactly the finite analogue of the first full-form missing theorem.

For each \(N\), let

\[
\epsilon_{+,N}(\lambda)
=
\min\sigma(T_{N,+}),
\]

\[
\epsilon_{-,N}(\lambda)
=
\min\sigma(T_{N,-}).
\]

Then finite even-simplicity is equivalent to:

- simplicity of \(\epsilon_{+,N}\);
- strict finite parity gap

\[
\epsilon_{+,N}
<
\epsilon_{-,N}.
\]

This finite equivalence is elementary once the source commutation theorem is used.

## 6. Full-form parity compatibility

The protected R036 audit binds inversion symmetry of the full form under

\[
(Jf)(u)=f(u^{-1}).
\]

On the source basis,

\[
J V_n
=
V_{-n}.
\]

Indeed, if

\[
x=\log(\lambda u)\in[0,L],
\]

then inversion sends

\[
x
\mapsto
\log(\lambda/u)
=
L-x,
\]

and

\[
U_n(L-x)
=
U_{-n}(x).
\]

Therefore the finite involutions \(\gamma\) are exactly the restrictions of the full inversion involution \(J\).

In particular:

\[
J E_N=E_N,
\]

and the finite parity sectors are the intersections

\[
E_{N,\pm}
=
E_N\cap\mathcal H_{\lambda,\pm}.
\]

This identity is the critical source bridge needed for sector-wise Galerkin convergence.

## 7. Admissible sector-wise convergence theorem

The source does not state the sector-wise convergence theorem in the exact form needed by the campaign.

However, its protected inputs support a bounded Solve proof.

Because:

- \(E=\bigcup_N E_N\) is a form core;
- \(J\) preserves the form domain and form norm;
- the parity projections

\[
P_\pm=\frac{I\pm J}{2}
\]

map \(E_N\) to \(E_{N,\pm}\);

one expects

\[
\bigcup_N E_{N,\pm}
\]

to be a form core for the restricted parity forms.

The min–max/Rayleigh principle would then give

\[
\epsilon_{\pm,N}(\lambda)
\downarrow
\epsilon_\pm(\lambda)
\qquad
(N\to\infty).
\]

This consequence should be proved in MATHSOLVE rather than attributed to the source.

## 8. What finite gaps can and cannot prove

If sector-wise convergence is established, then

\[
g_N(\lambda)
:=
\epsilon_{-,N}(\lambda)
-
\epsilon_{+,N}(\lambda)
\]

satisfies

\[
g_N(\lambda)
\to
g(\lambda)
:=
\epsilon_-(\lambda)-\epsilon_+(\lambda).
\]

Therefore:

- a positive **uniform asymptotic lower bound**

\[
\liminf_{N\to\infty}g_N(\lambda)>0
\]

would prove the full strict parity gap at that fixed \(\lambda\);

- finite positivity at one or many \(N\) does **not** by itself prove the full gap;
- finite negative values do not automatically falsify the limiting gap unless accompanied by convergence/error control;
- rigorous upper/lower bounds with certified tails can become proof-quality evidence.

The campaign should therefore demand convergence control together with any finite computation.

## 9. Source formula readiness for computation

The source provides enough explicit structure to implement a reproducible finite diagnostic.

For \(n\ne m\),

\[
q(U_n,U_m)(y)
=
\frac{
\sin(2\pi m y/L)
-
\sin(2\pi n y/L)
}{
\pi(n-m)
}.
\]

For \(n=m\),

\[
q(U_n,U_n)(y)
=
2(1-y/L)\cos(2\pi n y/L).
\]

The finite matrix is then assembled from:

\[
W_{0,2}(V_n,V_m),
\]

\[
\sum_{1<k\le e^L}
\Lambda(k)k^{-1/2}
q(U_n,U_m)(\log k),
\]

and

\[
W_{\mathbb R}(V_n,V_m).
\]

The archimedean source formula is convergent and has explicit digamma, trigamma, hypergeometric, and Hurwitz–Lerch representations.

A later evidence runner may use direct high-precision quadrature or those closed forms, provided numerical error is controlled.

## 10. Claim boundary

This audit does not prove:

- sector-wise finite-to-full convergence;
- positivity of any finite parity gap;
- positivity of the full parity gap;
- even-sector simplicity;
- any all-\(\lambda\) theorem;
- determinant convergence;
- RH.

It protects only the exact source substrate for those next steps.

## 11. Smallest Solve successor

The admissible next target is

RH-R037-QW-SECTOR-GALERKIN-001.

It should prove:

1. \(E_{N,\pm}\) increase to form cores of the parity-restricted forms;
2. finite parity bottoms decrease to the full parity bottoms:

\[
\epsilon_{\pm,N}\downarrow\epsilon_\pm;
\]

3. finite gaps converge:

\[
g_N\to g;
\]

4. any certified asymptotic lower bound

\[
\liminf_N g_N>0
\]

is sufficient for the full strict parity gap.

After that theorem is protected, a numerical/interval evidence runner becomes a mathematically controlled next action.

## 12. Audit disposition

FINITE_PARITY_BLOCKS_CONFIRMED__SECTOR_GALERKIN_REDUCTION_ADMISSIBLE

The source supplies exact finite parity structure and a full form core. The sector-wise convergence theorem remains to be proved in Solve.
