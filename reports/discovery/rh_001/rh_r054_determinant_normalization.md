# RH-R054 — Exact CCM determinant-normalization audit for Route C C0

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#298
- Parent protected audit: grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790
- Forge base: grandchallenge/MATHFORGE@782b80c8c57d4e77356d8c77c50ee1fffdcd92b8
- Scope: exact source/version and normalization audit only
- Novelty / priority / RH / certification claims: none

## 1. Immutable primary-source identity

Primary source:

Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1, submitted 2025-11-27.

This audit used the exact v1 arXiv HTML and the rendered v1 PDF.  The versioned
arXiv identifier is the immutable source identity for this packet.  Equation and
section references below are to v1.

The previous R035 provider audit correctly recorded the finite determinant
formula and the limiting convergence boundary.  The present addendum resolves
only the finer normalization question needed by MATHSOLVE Route C obligation C0.

## 2. The regularized determinant carries a source-fixed spectral-cut phase

Section 5.5 defines

[
\det_{\rm reg}(D-s)=\exp(-\zeta_D'(0;s))
	ag{5.16}
]

and explicitly notes the logarithm/spectral-cut ambiguity.  Lemma 5.8 then fixes
the convention

[
(-1)^{-z}:=e^{-i\pi z}
]

and proves, for the periodic Dirac operator with spectrum
((2\pi/L)\mathbb Z),

[
\det_{\rm reg}(D-s)=1-e^{-iLs}.
	ag{5.17}
]

The paper emphasizes that the accompanying phase factor is required for the
spectral periodicity.  Therefore the phase in the later finite determinant
formula is not a free normalization convention once the paper's spectral cut is
adopted.

## 3. Exact finite eigenvector and determinant normalization

Theorem 5.10 assumes that the smallest eigenvalue of (QW_\lambda^N) is simple
and that the corresponding eigenvector (\xi) is even.  It fixes its scale by

[
\delta_N(\xi)=1.
]

With (L=2\log\lambda), Theorem 5.10(ii), using (5.17), proves exactly

[
G_{\lambda,N}(z)
:=
\det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)
=
-i\,e^{-izL/2}\widehat\xi(z)
=
-i\,\lambda^{-iz}\widehat\xi(z).
	ag{R054.1}
]

Theorem 5.10(iii) states that (\widehat\xi) is entire, all of its zeros are
real, and those zeros coincide with the spectrum of the finite approximant.

Thus, at finite ((\lambda,N)), all of the following are source-fixed:

1. the spectral-cut convention used in the regularized determinant;
2. the eigenvector normalization (\delta_N(\xi)=1);
3. the scalar factor (-i);
4. the entire nonvanishing phase (\lambda^{-iz}=e^{-iz\log\lambda});
5. the Fourier/Mellin transform convention
   (\widehat f(z)=\int f(u)u^{-iz}d^*u).

No additional finite determinant normalization is supplied by the source.

## 4. The fixed-(\lambda) outlook uses a different limiting normalization

Section 7 is explicitly an outlook/strategy rather than a proved convergence
theorem.  For fixed (\lambda), it states the expected compact-uniform
(N\to\infty) limit as

[
-i\lambda^{-iz}\widehat\xi_\lambda(z),
]

where the full minimal eigenfunction (\xi_\lambda) is normalized by

[
\xi_\lambda(\lambda)=1.
]

This is not literally the finite condition (\delta_N(\xi)=1).  Corollary 5.6
shows that (\delta_N) approximates boundary evaluation as (N\to\infty), but
the paper does not promote the fixed-(\lambda) determinant convergence to a
theorem.

The two normalization statements must therefore remain distinct in governed
work:

- finite theorem: (\delta_N(\xi_{\lambda,N})=1);
- Section 7 limiting discussion: (\xi_\lambda(\lambda)=1).

## 5. What Section 7 does and does not fix toward (\Xi)

Section 7 next states that, as (\lambda\to\infty), the transforms
(\widehat\xi_\lambda(z)), **multiplied by suitable constants**, are expected
to converge uniformly on closed substrips of the open strip

[
|\operatorname{Im}z|<\frac12
]

to Riemann's

[
\Xi(s)=\xi\!\left(\frac12+is\right),
\qquad
\xi(w)=\frac12 w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w).
]

The rendered v1 PDF is authoritative for the absolute-value bars in the strip
statement; the HTML text extraction can omit the leading bar.

The next sentence paraphrases this as saying that the regularized determinants,
after multiplication by a factor of the form

[
e^{a+ibs},
]

converge toward (\Xi(s)).

The paper does **not** provide there:

- an explicit formula for the scalar normalization constant;
- an explicit pair (a,b) as functions of (\lambda,N);
- a proved compatibility theorem between the finite
  (\delta_N(\xi)=1) normalization and a canonical (\Xi)-normalization;
- a globally locally-uniform convergence theorem on all of (\mathbb C).

Combining the exact finite identity (R054.1) with the immediately preceding
statement that only a scalar multiple of (\widehat\xi_\lambda) is to approach
(\Xi) does, however, isolate the source-fixed (z)-dependent part: one must
remove (\lambda^{-iz}), i.e. multiply the raw determinant by the zero-free
entire factor (\lambda^{iz}) (and the fixed scalar (i)) to recover
(\widehat\xi).  What remains unfixed by the source is the scalar normalization
of that transform toward (\Xi).

This conclusion does not guess the missing scalar.

## 6. Exact normalization boundary exported to Solve

For C0 theorem development, the provider-safe source interface is therefore:

[
G_{\lambda,N}(z)
=
-i\lambda^{-iz}\widehat\xi_{\lambda,N}(z),
\qquad
\delta_N(\xi_{\lambda,N})=1,
	ag{R054.2}
]

with (\xi_{\lambda,N}) even under the source hypothesis.

Hence

[
i\lambda^{iz}G_{\lambda,N}(z)
=
\widehat\xi_{\lambda,N}(z)
	ag{R054.3}
]

is an exact source-derived phase removal by a zero-free entire multiplier.

Any further scalar fixing needed to define one canonical campaign family
(F_{\lambda,N}) is a Solve-side normalization choice/theorem and must be
proved to preserve the real-zero property.  It must not be attributed to CCM as
an explicit source normalization.

A useful additional source constraint is parity: because the admitted finite
ground vector is even under (u\mapsto u^{-1}), its logarithmic-coordinate
Fourier/Mellin transform is even in (z).  This can be used by Solve to fix the
linear exponential gauge without introducing an unsupported source constant.

## 7. Limit-strategy context, not an admitted theorem

Section 7 further defines the prolate/Sonin candidate (k_\lambda) only up to
scalar before choosing suitable normalizations, proves an (O(\lambda^{-2}))
uniform approximation for the underlying prolate functions, and proves
convergence of the corresponding Mellin transform to (\Xi) on closed
substrips of (|\operatorname{Im}z|<1/2).  Section 8 still names as missing the
theorem that (k_\lambda) approximates a scalar multiple of the true
(\xi_\lambda) strongly enough to transfer zero convergence.

Nothing in this normalization audit upgrades those source strategy statements
to determinant convergence.

## 8. Audit disposition

**EXACT_FINITE_PHASE_AND_VECTOR_NORMALIZATION_PINNED__XI_SCALAR_NORMALIZATION_UNSPECIFIED_IN_SOURCE**

The safe next action is a Solve-native C0 theorem that chooses and proves a
canonical scalar gauge after the exact phase removal (R054.3), without
attributing that scalar to the source.
