# RH-R031 — Prior-art audit for the half-line Berry–Keating realization

- Campaign: `RH-001`
- Provider tracker: `grandchallenge/MATHFORGE#253`
- Exact Forge base: `88c4f1b13bb818948fe7595d0d6cdb994a6fd162`
- Protected predecessor audit: `grandchallenge/MATHFORGE@da746ee38823e408321b9e417649f5b837ec5627`
- Audit date: 2026-09-18
- Scope: exact operator-class source/prior-art audit only
- Novelty / priority / RH / certification claims: none

## Exact class

The audited operator is the half-line Berry–Keating dilation generator

[
H_{BK}^{+}f=-ileft(x f'(x)+rac12 f(x)ight)
]

on `L^2((0,∞),dx)`, initially on `C_c^∞(0,∞)` and then closed to its self-adjoint dilation-generator realization.

The normalization is the raw spectral parameter `E`. No bounded transform of `E`, no finite spectral sample, and no change of Hilbert space is included in this exact class.

## Source result

The source record is not open frontier mathematics.

1. Sebastian Endres and Frank Steiner, *The Berry–Keating operator on L²(R_>,dx) and on compact quantum graphs with general self-adjoint realizations*, Journal of Physics A 43 (2010) 095204, DOI `10.1088/1751-8113/43/9/095204`.
   - For the half-line realization, the paper proves purely continuous spectrum.
   - It explicitly concludes that this realization cannot furnish a Hilbert–Pólya operator whose eigenvalues are the nontrivial zeta-zero parameters.
   - For compact quantum graphs it obtains discrete spectra, but the Weyl asymptotics still do not match the Riemann-zero counting law.

2. Fabio Bagarello and Sergiusz Kużel, *On the Berry-Keating Operator*, Complex Analysis and Operator Theory 20 (2026), article 135, DOI `10.1007/s11785-026-01990-w`, published 2026-07-07.
   - The self-adjoint dilation-generator realization is reviewed with its generator domain.
   - The restriction to `L²(R_+)` is unitarily equivalent to the momentum operator on `L²(R)`.
   - Its spectrum is Lebesgue spectrum of multiplicity one.
   - The paper states that these standard `L²` realizations therefore cannot qualify as the hypothetical Hilbert–Pólya operator.

The 2026 source confirms that the 2010 obstruction remains the current exact status of this class.

## Exact unitary reduction

Define

[
(Wf)(y)=e^{y/2}f(e^y),qquad yinmathbb R.
]

Then `W : L²((0,∞),dx) -> L²(R,dy)` is unitary because

[
int_{mathbb R}|e^{y/2}f(e^y)|^2dy
=int_0^infty |f(x)|^2dx.
]

On `C_c^∞`,

[
W H_{BK}^{+}W^{-1}=-i,rac{d}{dy}.
]

Thus the closure of the half-line Berry–Keating operator is unitarily equivalent to the standard self-adjoint momentum operator with domain `H¹(R)`.

Consequences:

- the minimal half-line operator is essentially self-adjoint;
- the closed realization is self-adjoint;
- `σ(H_BK^+)=R`;
- the spectrum is purely absolutely continuous / Lebesgue of multiplicity one;
- the point spectrum is empty.

## Contract consequence

This class passes the predecessor theorem's mandatory **unboundedness** condition, but it fails the stronger exact Hilbert–Pólya spectral contract.

Two distinctions are material:

1. **Spectral containment is too weak for an unbounded candidate.** Because `σ(H_BK^+)=R`, every real zero ordinate is contained in the spectrum. This fact by itself carries no zeta information.
2. **Eigenvalue correspondence fails.** The point spectrum is empty, so there is no discrete eigenvalue sequence to identify with the positive zero ordinates, with or without multiplicity.

Therefore the exact half-line `L²(R_+)` Berry–Keating realization is eliminated as a raw-ordinate Hilbert–Pólya candidate.

## Smallest proof-quality successor

A Solve-native theorem may safely record the exact unitary conjugation and derive the spectral-type obstruction:

`RH-R031-BK-HALFLINE-LEBESGUE-001`.

The proof should not be represented as novel. Its campaign value is to sharpen the operator contract after `RH-R030`:

[
	ext{unbounded} 
otRightarrow 	ext{useful discrete spectrum}.
]

A later route that modifies the Hilbert space, boundary conditions, graph topology, or operator is a **different operator class** and requires a fresh source audit before selection.

## False-proof firewall

- Do not treat `σ(H)=R` and containment of all ordinates as a spectral realization of the zeros.
- Do not promote generalized eigenfunctions to `L²` eigenvectors.
- Do not infer zeta-zero real-part information from self-adjointness when the spectral parameter is already real.
- Do not transfer a result from a compact interval or compact quantum graph back to the full half-line realization.
- Do not treat discrete truncation spectra as matching the Riemann zeros without checking their counting asymptotics.

## Audit disposition

`SOURCE_STATUS_CONFIRMED__SOLVE_TARGET_ADMISSIBLE_AS_KNOWN_NO_GO`

The exact half-line Berry–Keating class is suitable for a bounded Solve tranche whose purpose is contract sharpening and proof replay, not discovery or novelty.
