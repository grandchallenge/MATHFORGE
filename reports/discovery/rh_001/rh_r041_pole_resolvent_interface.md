# RH-R041 — Pole rank-one split and scalar parity-resolvent interface

Campaign: RH-001
Provider tracker: grandchallenge/MATHFORGE#272
Exact branch base: grandchallenge/MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a
Protected full-operator parity substrate: grandchallenge/MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d
Protected finite CCM substrate: grandchallenge/MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b
Audit date: 2026-09-18
Claim class: source interface + admissible elementary operator reduction
RH / novelty / priority / certification claims: none

## 1. Primary source

Alain Connes, Caterina Consani, Henri Moscovici,
Zeta Spectral Triples, arXiv:2511.22755.

Relevant exact source statements:

- equation (3.10): QW = W_{0,2} - W_R - sum_p W_p;
- equation (3.11): W_{0,2}(F) = Fhat(i/2) + Fhat(-i/2);
- equation (3.19): on the localized Hilbert space the pole contribution
  to the quadratic form is

  2 Re( fhat(i/2) overline{fhat(-i/2)} );

- Lemma 4.1 / equation (4.2): the finite W_{0,2} matrix has rank two
  and the displayed closed rational/hyperbolic form.

The protected R036/R037 audits already bind the localized Hilbert space,
inversion symmetry, canonical self-adjoint representation, and the exact
finite parity decomposition.

## 2. Centered logarithmic coordinates

Put

a = log lambda,  x = log u in [-a,a].

The multiplicative Haar measure becomes dx.

Define

C(x) = cosh(x/2),  S(x) = sinh(x/2).

Then C is even and S is odd.

For the source Fourier convention,

fhat(i/2) = integral f(x)e^{x/2} dx,
fhat(-i/2) = integral f(x)e^{-x/2} dx.

Using e^{x/2}=C+S and e^{-x/2}=C-S, write

c_f = integral f C,
s_f = integral f S.

Then

2 Re((c_f+s_f) overline{(c_f-s_f)})
= 2|c_f|^2 - 2|s_f|^2.

Therefore the source pole term is exactly the bounded rank-two operator

R = 2|C><C| - 2|S><S|.

This is the full-operator counterpart of the source finite rank-two matrix statement.

## 3. Exact parity split

Let A_lambda be the full localized Weil operator from the protected R036 substrate.

Set

B_lambda = A_lambda - R.

Because R is bounded and self-adjoint, B_lambda is self-adjoint on the same
operator domain as A_lambda.

Both A_lambda and R commute with parity, hence so does B_lambda.

Let B_{lambda,+} and B_{lambda,-} be its parity restrictions. Because C is
even and S is odd,

A_{lambda,+} = B_{lambda,+} + 2|C><C|,

A_{lambda,-} = B_{lambda,-} - 2|S><S|.

No Perron, inertia, nodal, or positivity-improving theorem is needed for this algebra.

## 4. Source-independent odd-sector resolvent criterion

Let

mu = epsilon_+(lambda) = min sigma(A_{lambda,+}).

Assume only the pole-localization condition

mu < beta_-(lambda),
beta_-(lambda) := inf sigma(B_{lambda,-}).

Then

T := B_{lambda,-} - mu I

is strictly positive and has bounded inverse.

Define

m_o(mu) =
<S,(B_{lambda,-}-mu I)^{-1}S>.

The odd shifted operator is

A_{lambda,-} - mu I = T - 2|S><S|.

In form language,

T - 2|S><S|
=
T^{1/2}
(I - 2|T^{-1/2}S><T^{-1/2}S|)
T^{1/2}.

The middle rank-one operator has eigenvalue

1 - 2||T^{-1/2}S||^2
=
1 - 2m_o(mu)

on span(T^{-1/2}S), and eigenvalue 1 on its orthogonal complement.

Therefore

A_{lambda,-} - mu I > 0
iff
2m_o(mu) < 1.

Since

A_{lambda,-} - mu I > 0
iff
epsilon_-(lambda) > mu,

one obtains the exact scalar criterion

mu < inf sigma(B_{lambda,-})
implies
[
epsilon_+(lambda) < epsilon_-(lambda)
iff
m_o(mu) < 1/2
].

At equality m_o(mu)=1/2 the odd shifted operator has a zero mode, so the
parity gap closes. If m_o(mu)>1/2, the odd sector lies below mu.

Thus the scalar margin

Delta_H(lambda)
=
1/2 - m_o(epsilon_+(lambda))

is an exact signed parity-order parameter whenever pole localization holds.

### Quantitative lower bound

Let

d(lambda)
=
inf sigma(B_{lambda,-}) - mu
>
0.

For every odd-sector form vector f,

|<S,f>|^2
=
|<T^{-1/2}S,T^{1/2}f>|^2
<=
m_o(mu)<Tf,f>.

Therefore

<(A_{lambda,-}-mu)f,f>
=
<Tf,f>-2|<S,f>|^2

is bounded below by

(1-2m_o(mu))<Tf,f>
>=
(1-2m_o(mu))d(lambda)||f||^2.

Consequently, whenever m_o(mu)<1/2,

epsilon_-(lambda)-epsilon_+(lambda)
>=
(1-2m_o(mu))
[
inf sigma(B_{lambda,-})-epsilon_+(lambda)
].

Equivalently,

g(lambda)
>=
2 Delta_H(lambda) d(lambda).

This turns certified lower bounds on the two scalar margins into a
certified lower bound on the full parity gap.

The converse signs are also explicit.  For the trial vector
f=T^{-1}S,

<(A_{lambda,-}-mu)f,f>
=
m_o(mu)(1-2m_o(mu)).

Hence m_o(mu)>1/2 forces epsilon_-(lambda)<mu.  At m_o(mu)=1/2,

(A_{lambda,-}-mu)T^{-1}S=0,

while the rank-one form factorization is nonnegative, so
epsilon_-(lambda)=mu exactly.

## 5. What this reduction does not require

The criterion above does not require:

- B_{lambda,+} to have exactly one negative eigenvalue;
- B_{lambda,-} > 0;
- a positivity-improving semigroup for B_lambda;
- a Perron theorem;
- nonzero overlap with every base eigenvector;
- a secular-root theorem for the even sector;
- global operator monotonicity of a Loewner symbol.

Those are additional hypotheses appearing in adjacent 2026 literature.
They are not needed for the bounded odd-sector comparison once
epsilon_+(lambda) and the pole-localization inequality are given.

## 6. Secondary prior-art reconstruction

Zenodo is not reachable from the present runtime.

An independent literature repository contains mirrored publication PDFs
and extracted full text for three Breno Andrade notes:

- A scalar Herglotz criterion for the even-simplicity hypothesis in the
  localized Weil quadratic form, DOI 10.5281/zenodo.20694588;
- The pole term is the only obstruction to Perron structure in the localized
  Weil quadratic form, DOI 10.5281/zenodo.20682834;
- A Loewner/operator-monotone framework for the even-simplicity problem in
  the Connes–Consani–Moscovici spectral triple,
  DOI 10.5281/zenodo.20737111.

Exact mirror commit:
Malaeu/chen_q3@02e786a7d58f23cc06bd21df783dc162e03efe36.

The mirror reading card records publication-PDF SHA-256 values:

- 20694588:
  b6ae873e851b0a4c381c36160f258d2bfdd40bd031f0a66cdf536d6de6692ffe;
- 20682834:
  4e0de4780905f407f318f2e9bf6b1aebc7770505f13ef25ab955d761f734676a;
- 20737111:
  390e3346a8964bf11e5b9919dfd4494e026673d4889907c747e18d59940ac312.

This is reconstruction provenance, not independent primary-byte verification by GCL.

## 7. Prior-art overlap and rejection boundary

The reconstructed Herglotz paper states essentially the same scalar odd
resolvent inequality, but packages it with stronger structural assumptions:

- B_e has exactly one negative eigenvalue;
- B_o > 0;
- sector bottoms are represented as first roots of two secular equations.

Its conclusion explicitly leaves

m_o(epsilon_+) < 1/2

open for general cutoff.

The independent mirror audit identifies unpaid hypotheses in that stronger
formulation:

1. Perron simplicity of a pole-free ground does not by itself prove the
   claimed inertia of both parity restrictions.
2. A rank-one resolvent has a pole at a base eigenvalue only if the
   perturbation vector has nonzero spectral weight there.
3. Strict positivity cannot be inferred from a non-strict endpoint inequality
   at equality.
4. The arithmetic Loewner symbol lies outside the global operator-monotone
   regime of the adjacent Loewner paper.

Accordingly, this package imports none of those stronger claims.

## 8. Relation to the R040 small-a route

The R040 candidate audit records Suzuki's theorem that, for sufficiently
small a=log lambda>0, the full localized Weil ground state is simple and even.

Combined with protected RH-R036, this gives a strict parity gap in a nonempty
small-a regime.

On any parameter value where that strict gap is already known, the
pole-localization hypothesis required above is automatic. Indeed,

B_{lambda,-}
=
A_{lambda,-}+2|S><S|
>=
A_{lambda,-}

in form order, so

inf sigma(B_{lambda,-})
>=
epsilon_-(lambda)
>
epsilon_+(lambda).

Thus the proved Suzuki regime starts inside the domain of the scalar
resolvent criterion, and the corresponding Herglotz margin is strictly
positive there.

The scalar criterion therefore identifies an exact continuation variable:

Delta_H(lambda)
=
1/2
-
<S,(B_{lambda,-}-epsilon_+(lambda))^{-1}S>.

Suzuki separately proves continuity of the unrestricted lowest eigenvalue
lambda_a as a function of a. That theorem alone does not establish
continuity of the pole-free odd spectral bottom or of Delta_H. A continuation
argument must prove the needed sector/resolvent continuity rather than infer
it from continuity of the global minimum.

This package does not prove continuity or positivity of Delta_H beyond the
small-a regime.

## 9. Smallest admissible Solve successor

The next bounded theorem-development target is:

RH-R041-ODD-HERGLOTZ-GAP-CRITERION-001.

Solve may prove from the primary CCM pole functional and standard rank-one
operator algebra:

For fixed lambda>1, let mu=epsilon_+(lambda). If

mu < inf sigma(B_{lambda,-}),

then

epsilon_+(lambda) < epsilon_-(lambda)

if and only if

<S,(B_{lambda,-}-mu)^{-1}S> < 1/2.

This theorem must not assert:

- pole localization for all lambda;
- even-sector simplicity for all lambda;
- positivity of the scalar margin for all lambda;
- any imported inertia theorem from the secondary Andrade source;
- RH.

## 10. Continuation frontier

After the scalar criterion is protected, continuation has two explicit
obligations.

H1 — pole localization:

epsilon_+(lambda) < inf sigma(B_{lambda,-}).

H2 — positive Herglotz margin:

Delta_H(lambda) > 0.

A continuation theorem in lambda can then work directly with these two margins.

There is also an immediate bounded Solve target suggested by Suzuki's proof
of continuity of the unrestricted lower bound.  After scaling to the fixed
interval [-1,1], Suzuki writes the closed form as an a-independent closed
part plus an a-dependent bounded-form part, uses compact embedding for lower
semicontinuity, and uses fixed test vectors for upper semicontinuity.

The same proof architecture is parity compatible:

- the scaled even and odd subspaces are fixed closed subspaces;
- the form commutes with parity;
- parity projections preserve the form core;
- an L2 limit of even (respectively odd) minimizers remains even
  (respectively odd).

This supports the bounded Solve target

RH-R042-PARITY-BOTTOM-PARAMETER-CONTINUITY-001:

prove separately that

a -> epsilon_+(e^a)
and
a -> epsilon_-(e^a)

are continuous on (0,infinity), and hence

g(a)=epsilon_-(e^a)-epsilon_+(e^a)

is continuous.

This statement should be proved in Solve rather than attributed to Suzuki:
Suzuki proves continuity of the unrestricted minimum and explicitly notes
that earlier parity-restricted continuity assertions lacked full details.

If R042 is proved, let I be the connected component adjacent to a=0 on which
g(a)>0.  Suzuki plus R036 makes I nonempty.  If its finite right endpoint a_*
exists, continuity forces g(a_*)=0.

Combined with the R041 criterion, a loss of the gap at such a boundary can
occur through one of two exact interfaces:

1. pole localization closes:
   inf sigma(B_{a_*,-}) = epsilon_+(a_*); or
2. pole localization remains strict and the Herglotz margin closes:
   Delta_H(a_*) = 0.

Thus the all-a continuation problem can be split into two scalar/spectral
failure modes instead of treated as an undifferentiated parity theorem.

The next provider task is primary-authority acquisition of the Andrade notes
and an audit of whether their Loewner/Herglotz formulas yield effective
derivative or monotonicity bounds for H1/H2.

## 11. Disposition

PRIMARY_POLE_SPLIT_CONFIRMED__ODD_HERGLOTZ_GAP_INTERFACE_ADMISSIBLE__STRONGER_SECONDARY_INERTIA_CLAIMS_NOT_IMPORTED

The parity-gap frontier has an exact scalar interface under one explicit
pole-localization hypothesis.

RH remains open.
