# RH-R038 — Audit of claimed Krein–Rutman closure of the CCM simple-even step

- Campaign: RH-001
- Provider tracker: grandchallenge/MATHFORGE#268
- Exact external source: Architect-Resonance/Riemann-Hypothesis@7ba3619c2dd34aae3bc71ff8258f07cef04f5e01
- Protected predecessor audit: grandchallenge/MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b
- Audit date: 2026-09-18
- Scope: repository-level claimed proof and advertised verification surface
- Claim admission: REJECTED
- RH / novelty / priority / certification claims: not admitted

## 1. Claimed result

The external repository is titled:

"Spectral Simplicity of the Weil Quadratic Form via Krein-Rutman Positivity."

Its README states that it addresses the two missing conditions identified by Connes–Consani–Moscovici:

1. simplicity/evenness of the smallest eigenvalue of \(QW_\lambda\);
2. convergence of the eigenfunction toward the Riemann \(\Xi\) function.

The repository's stated mechanism is:

\[
QW_\lambda=A+\Pi-P,
\]

where the prime operator \(P\) is claimed to be positive, compact, and irreducible, so that Krein–Rutman supplies a simple Perron eigenvector; additional asymptotic estimates are then intended to preserve a gap for the full Weil operator.

The repository also advertises Python scripts as verification of the numerical claims underlying this route.

## 2. Evidence surface actually available

The exact source commit contains:

- README.md;
- a 12-page PDF manuscript;
- numerical scripts including:
  - krein_rutman_test.py;
  - diagonal_dominance_test.py;
  - polar_norm_scaling.py;
  - gap_convergence_N.py;
  - rayleigh_orthogonal_test.py;
  - commutator_test.py;
  - connes_exact_weil.py;
  - even_sector_scaling.py.

The connected GitHub interface exposes the manuscript PDF as an opaque binary rather than a machine-readable theorem body. Accordingly, this audit does not claim that every argument in the PDF has been independently reconstructed.

However, the repository README explicitly identifies the scripts as the verification surface for its central numerical/operator claims. That advertised surface is sufficient to determine whether the claim may supersede the protected R037 frontier.

It may not.

## 3. Krein–Rutman strong-positivity / irreducibility condition is not established

The script krein_rutman_test.py correctly states that simplicity requires more than positivity: it asks whether the operator is strongly positive / irreducible.

The script then explicitly reports:

"T is NOT strongly positive"

and observes that images of point-localized test data retain many zeros.

The script does not prove irreducibility of the continuum operator. Instead it replaces the missing theorem with:

- numerical near-rank-one behavior;
- a conjectural statement that sufficiently many prime shifts should fill support;
- an informal density argument involving logarithms of primes.

None of these is a proof of the Krein–Rutman irreducibility hypothesis on the actual Banach lattice.

Therefore the repository's own executable evidence leaves the hypothesis required for simplicity OPEN.

## 4. The compactness claim is not valid as stated

krein_rutman_test.py states that the continuum prime operator is compact because it is a finite sum of shift operators on a compact interval, and even labels such a sum "finite rank."

That implication is false.

A nonzero translation / truncated translation operator on an infinite-dimensional \(L^2\) space is generally not finite rank and is not compact merely because the spatial interval is compact.

The script itself notices that its formal kernel contains delta distributions and is not Hilbert–Schmidt, but then still asserts compactness without a valid replacement theorem.

Thus the repository has not established the compactness hypothesis required by the version of Krein–Rutman it invokes.

This is a structural proof defect, not a numerical-precision issue.

## 5. Simplicity of the prime operator does not imply simplicity of \(QW_\lambda\)

The headline route also contains an invalid implication.

Even if one granted that \(P\) had a simple top eigenvalue, it does not follow from

\[
QW_\lambda=A+\Pi-P
\]

that the ground eigenvalue of \(QW_\lambda\) is simple.

A perturbation by \(A+\Pi\) can:

- rotate eigenvectors;
- close a gap;
- create or remove degeneracy;
- change parity ordering.

To transfer a simple Perron root of \(P\) to a simple ground state of \(QW_\lambda\), one needs a quantitative perturbation theorem whose hypotheses are proved for the full operator.

The repository attempts to supply such control numerically/asymptotically, but does not establish the required uniform analytic inequalities.

Therefore "Krein–Rutman for \(P\)" is not, by itself, a proof of the CCM simple-even condition.

## 6. Numerical near-rank-one behavior is not a theorem

krein_rutman_test.py computes finite-grid singular values and concludes that the prime operator is "NEARLY RANK 1."

It then says the large numerical gap makes simplicity "effectively guaranteed."

This is not an admissible proof move.

A finite discretization with a large observed spectral gap does not prove:

- compactness of the continuum operator;
- irreducibility of the continuum cone action;
- simplicity of the exact continuum Perron root;
- persistence of that gap after adding \(A+\Pi\);
- an all-\(\lambda\) theorem.

The protected R037 theorem was introduced precisely to prevent finite spectral evidence from being promoted without a convergence/tail argument.

## 7. The density argument for support propagation is insufficient

The Krein–Rutman script suggests that irreducibility would follow because logarithms of primes are rationally independent and their linear combinations are dense.

This does not establish the required support-propagation theorem.

The actual operator uses a finite \(\lambda\)-dependent collection of prime-power shifts with positivity constraints and truncation at the interval boundary.

Even an abstract density statement for an additive group generated by logarithms of primes would not imply that a finite positive-semigroup shift operator maps every nonzero positive function into the interior of the positive cone, nor that a fixed finite power does so.

The exact cone-irreducibility property must be proved for the actual operator.

It is not.

## 8. The asymptotic gap scripts do not close the analytic gap

The scripts diagonal_dominance_test.py, rayleigh_orthogonal_test.py, polar_norm_scaling.py, and commutator_test.py perform finite-\(N\), floating-point experiments.

Examples of non-admissible promotions include:

- observing \(\sigma_2(P)\) to remain small on a finite sample;
- observing \(\|\Pi^{++}\|\) to scale approximately like \(\log\lambda\);
- observing a normalized commutator to decrease;
- observing a positive finite even-sector gap and then concluding positivity for all larger \(\lambda\).

In particular, polar_norm_scaling.py prints the assertion that because the finite gap is already positive at one sampled cutoff, "the result holds for ALL" larger cutoffs.

No monotonicity theorem or uniform analytic bound proving that implication is supplied by the script.

The evidence is exploratory, not a proof.

## 9. The finite-\(N\) convergence script is not a tail certificate

gap_convergence_N.py samples small finite truncations using NumPy double-precision eigensolvers.

It asks whether the gap appears stable as \(N\) increases.

That is useful as a diagnostic, but it does not provide:

- interval enclosures of matrix entries;
- rigorous eigenvalue enclosures;
- a quantified Galerkin tail;
- a proof that a positive limiting gap remains separated from zero.

The protected RH-R037 theorem supplies only the abstract convergence

\[
g_N(\lambda)\to g(\lambda).
\]

To conclude \(g(\lambda)>0\), one still needs a positive asymptotic lower certificate.

The external script does not provide one.

## 10. Exact conflict with the protected campaign frontier

RH-R036 proved that the CCM simple-even condition is equivalent to:

1. simplicity of the even-sector spectral bottom;
2. the strict parity gap
   \[
   \epsilon_+(\lambda)<\epsilon_-(\lambda).
   \]

RH-R037 proved:

\[
\epsilon_{\pm,N}(\lambda)\downarrow\epsilon_\pm(\lambda),
\qquad
g_N(\lambda)\to g(\lambda).
\]

The claimed Krein–Rutman route does not discharge either protected obligation:

- even-sector simplicity remains unproved at the full operator level;
- strict full parity-gap positivity remains unproved.

Therefore it does not supersede the protected route.

## 11. Smallest useful residue from the external work

The repository remains useful as exploratory prior art.

Its scripts suggest several mechanisms worth testing under GCL controls:

- strong concentration of the prime contribution in a leading even mode;
- possible sublinear growth of the polar correction in the even sector;
- possible suppression of the second prime-sector eigenvalue;
- possible stabilization of parity/even-sector gaps under truncation.

These may inform an evidence runner.

They may not be imported as theorems.

Any reuse must rebuild the matrix from the protected CCM source formulas and must use independent precision/error controls.

## 12. Disposition

CLAIMED_KREIN_RUTMAN_CLOSURE_REJECTED__R037_FRONTIER_REMAINS_LIVE

The external repository does not supply admissible proof evidence for the CCM simple-even theorem or RH.

The next campaign action remains a controlled high-precision parity-gap evidence tranche, with explicit separation between finite evidence and a rigorous tail certificate.
