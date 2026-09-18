# RH-R040 — Small-\(a\) simple-even closure and quantitative parity-transfer audit

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#270
- Exact Forge base: a11c6dedede09af6f3c67c5eec337941b73d4d3a
- Audit date: 2026-09-18
- Scope: current exact literature relevant to the full Weil parity gap and Galerkin tail
- RH / novelty / priority / certification claims: none

## 1. Primary sources

### Suzuki — actual localized Weil operator

Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096v2, 17 August 2026; manuscript version dated
24 August 2026.

The source studies the localized Weil form on \(L^2(-a,a)\) and its
canonical self-adjoint operator \(A_a\).

Under

\[
x=\log u,\qquad a=\log\lambda,
\]

this is the CCM localized operator on

\[
L^2([\lambda^{-1},\lambda],d^*u),
\]

since \(d^*u=du/u=dx\), and inversion \(u\mapsto u^{-1}\) becomes
parity \(x\mapsto-x\).

### Groskin — finite dictionary and archimedean tail

Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail
order for the truncated Weil quadratic form*, arXiv:2607.02828v3,
August 2026.

Exact source repository:
\`akivag613/connes-cvs-@9881eeb02ceb9f7c94e65c0eaaa2a3e81e3e7aaf\`.

### Groskin — sine Loewner boundary splitting

Akiva Groskin, *Bulk trace laws and algebraic boundary interaction for the
sine Loewner operator*, September 2026.

Exact source repository:
\`akivag613/connes-cvs-@9881eeb02ceb9f7c94e65c0eaaa2a3e81e3e7aaf\`.

## 2. Suzuki closes the first CCM missing condition on a nonempty regime

Suzuki proves that for sufficiently small \(a>0\), the lowest eigenvalue
\(\lambda_a\) of the **full localized Weil operator** \(A_a\):

- is positive;
- is simple;
- has an even eigenfunction.

The source gives

\[
\lambda_a
=
\log\frac1a+\mu_1-\log(2\pi)+\psi(2)-1+O(a)
\]

for some \(\mu_1>0\).

This is not a finite-matrix surrogate.

## 3. Mechanism

After scaling to \((-1,1)\), Suzuki obtains

\[
R(a,v)
=
\log\frac1a-(2A+1)
+
\frac{\mathcal L(v)}{\|v\|^2}
+
O(a)
\]

for \(0<a<\tfrac12\log2\).

The limiting closed form \(\overline{\mathcal L}\) is an irreducible
Dirichlet form with positive jump kernel proportional to \(1/|x-y|\).
Its semigroup is positivity improving. Hence its lowest eigenvalue is
simple and has a positive eigenfunction.

Perturbation theory preserves this lowest-eigenvalue multiplicity for
sufficiently small \(a\). Since \(A_a\) commutes with parity and its
ground eigenfunction has fixed sign, the ground eigenfunction is even.

This is a valid full-operator positivity-improving mechanism and is
materially distinct from the rejected R038 finite-shift Krein–Rutman
argument.

## 4. Consequence for protected RH-R036

RH-R036 proved that, for fixed \(\lambda>1\), the following are
equivalent:

1. the full ground eigenvalue is simple and even;
2. the lowest even eigenvalue is simple and
   \[
   \epsilon_+(\lambda)<\epsilon_-(\lambda).
   \]

Suzuki proves condition 1 for all sufficiently small

\[
a=\log\lambda>0.
\]

Therefore:

\[
\boxed{
\exists a_0>0\;\forall\,0<a<a_0:
\quad
\epsilon_+(e^a)<\epsilon_-(e^a)
}
\]

and the lowest even eigenvalue is simple on the same interval.

Equivalently, there exists \(\lambda_0>1\) such that the first CCM
simple-even missing condition is discharged for every

\[
1<\lambda<\lambda_0.
\]

This is a genuine full-operator parity-gap theorem on a nonempty regime.

## 5. The theorem is not yet effective at the R039 points

Suzuki states "for sufficiently small \(a>0\)" and does not extract an
explicit numerical \(a_0\) sufficient for simplicity/evenness.

The displayed Rayleigh expansion is valid under

\[
a<\frac12\log2,
\]

but this is not itself proved to be the simplicity threshold; the final
multiplicity step uses an \(O(a)\) perturbation without an explicit
constant compared against an explicit limiting spectral gap.

For R039,

\[
\lambda^2=c\in\{13,14\},\qquad
a=\frac12\log c,
\]

so

\[
a_{13}\approx1.28247,\qquad
a_{14}\approx1.31953.
\]

These are outside even the displayed small-\(a\) expansion interval
\(a<\tfrac12\log2\approx0.34657\).

Thus R039 and Suzuki currently occupy different parameter regimes.

## 6. Groskin's \(B_T\) theorem controls a different limit

The finite Guinand–Weil paper fixes \(c\) and Galerkin dimension \(N\)
and controls the auxiliary archimedean integration cutoff \(T\).

It proves an enclosure of the form

\[
\lambda_j(Q_T^{\rm tot})
<
\lambda_j(Q_\infty)
\le
\lambda_j(Q_T^{\rm tot})+B_T,
\]

with

\[
B_T
\sim
\frac{(2N+1)\rho}{\pi^2T}\log T.
\]

This is rigorous and useful, but the limit is

\[
T\to\infty
\quad\text{at fixed \(N\)}.
\]

The R037/R039 obligation is the already cutoff-free Galerkin limit

\[
N\to\infty.
\]

Therefore \(B_T\) does not bound

\[
|\epsilon_{\pm,N}-\epsilon_\pm|.
\]

It validates cutoff-free finite assembly but does not supply the missing
\(N\)-tail certificate.

## 7. Sine-Loewner parity splitting does not transfer automatically

The September sine-Loewner paper studies a different compressed operator
\(\mathcal K_\tau\), its half-line boundary operators, and nonzero
central-gap eigenvalue clusters.

For a fixed isolated half-line gap eigenvalue \(\alpha\), its centered
finite-interval eigenvalues satisfy

\[
\lambda_{\rm even}
=
\alpha+c_\alpha|\eta|^2L^{-\gamma}+o(L^{-\gamma}),
\]

\[
\lambda_{\rm odd}
=
\alpha-c_\alpha|\eta|^2L^{-\gamma}+o(L^{-\gamma}).
\]

For \(\eta\neq0\), this gives nonzero leading even–odd splitting.  The
source interval-certifies \(\eta\neq0\) for one phase-zero mode.

But this is not RH-R036.

The sine-Loewner theorem concerns:

- operator \(\mathcal K_\tau\);
- a cluster approaching a nonzero central-gap boundary eigenvalue;
- spatial interval length \(L\to\infty\);
- boundary-state interaction.

The CCM problem concerns:

- localized Weil operator \(A_a\);
- the bottom of even and odd spectra;
- fixed \(a\);
- Galerkin dimension \(N\to\infty\).

No theorem in the audited source identifies these operators or limits,
nor transfers the boundary splitting to

\[
\epsilon_-(a)-\epsilon_+(a).
\]

The paper also states that nonzero amplitude is certified for its
phase-zero mode; arbitrary-phase / every-gap nonvanishing is not proved.

The sine-Loewner theorem is therefore an adjacent mechanism, not a
parity-gap transfer theorem for CCM.

## 8. Adjacent scalar-resolvent literature

The current audited bibliography records June 2026 work by Breno Wilson
de Andrade Silva on:

- Loewner/operator-monotone structure for CCM even-simplicity;
- a scalar Herglotz criterion for localized-Weil even-simplicity;
- a rank-one-per-parity pole-term decomposition.

Those theorem bodies are not part of the present exact-source corpus.
This audit therefore records their bibliographic relevance but imports
no mathematical claim from them.

They are a high-priority source-acquisition target for continuation in
\(a\).

## 9. Updated parameter geometry

The first CCM obstruction now has three regimes.

### Regime S — proved small \(a\)

For some non-explicit \(a_0>0\):

\[
0<a<a_0
\Longrightarrow
\begin{cases}
\text{global ground simple and even},\\
\epsilon_+(a)<\epsilon_-(a).
\end{cases}
\]

### Regime F — controlled finite evidence

At

\[
a=\frac12\log13,\quad\frac12\log14,
\]

R039 has high-precision positive finite gaps through \(N=12\), with no
\(N\)-tail certificate.

### Regime U — continuation gap

Between the proved small-\(a\) regime and the R039 points, there is no
audited theorem preserving the simple-even ground state or strict parity
ordering.

That is now the smallest structural gap.

## 10. Smallest next target

The highest-value route is:

\[
\boxed{\text{make Suzuki's small-\(a\) theorem effective and continue it in \(a\)}}
\]

A bounded programme is:

1. bound the first spectral gap of the limiting positivity-improving
   operator \(T\);
2. replace the source \(O(a)\) perturbation by an explicit norm/form bound;
3. obtain a concrete \(a_0\);
4. source-audit and use scalar Herglotz / rank-one parity criteria to
   continue the margin through \(a\)-intervals;
5. isolate prime-power thresholds explicitly rather than assume global
   smoothness.

This attacks the full operator directly. RH-R037 remains the finite
certification layer.

## 11. Admissible Solve successor

The immediate bounded theorem is:

\`RH-R040-SMALL-A-PARITY-GAP-001\`.

Using Suzuki's exact small-\(a\) theorem, the exact coordinate relation
\(a=\log\lambda\), and protected RH-R036, Solve may prove:

> There exists \(\lambda_0>1\) such that for every
> \(1<\lambda<\lambda_0\), the full localized Weil operator has a simple
> lowest even eigenvalue and a strict even-below-odd parity gap.

This does not determine \(\lambda_0\).

## 12. Audit disposition

SMALL_A_FULL_PARITY_GAP_CONFIRMED__ARCH_T_CUTOFF_CERTIFIED__SINE_LOEWNER_SPLITTING_AUXILIARY__EFFECTIVE_CONTINUATION_OPEN

The first CCM missing condition is closed on a nonempty small-\(a\)
parameter regime. The open frontier is quantitative continuation from
that regime.

RH remains open.
