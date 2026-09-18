# BSD-001 R5-WIT source audit — exact modular-symbol computation interface

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#236`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#282`.
- Protected entering MATHFORGE: `aeb6588785e70bb7477cdcf44b018c150674c8e4`.
- Downstream protected R5-RECIP completion anchor: `grandchallenge/MATHSOLVE@9c9bd9077f8b269277366c7ee81dcdcd7f701217`.
- Claim class: bounded software/source interface only.

## PARI/GP interface

The downstream reconnaissance uses PARI/GP 2.15.4, specifically `msfromell` and `mseval`.

The official PARI/GP 2.15.4 User's Guide and stable modular-symbol reference specify:

1. `msfromell(E,1)` returns the exact plus modular symbol `x^+` attached to `E/Q`.
2. `x^+` is normalized by `Omega^+ = E.omega[1]`, the positive real period obtained by integrating the Néron differential on the connected component of `E(R)`.
3. The complex modular symbol is normalized as
   `F = x^+ Omega^+ + x^- i Omega^-`.
4. In particular,
   `x^+([0]-[infinity]) = L(E,1)/Omega^+`.
5. `mseval(M,s,[a,b])` evaluates the exact rational modular symbol `s([b]-[a])`.

Version-specific documentation:
`https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.15.4/users.pdf`.

Stable modular-symbol reference:
`https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_symbols.html`.

For the protected controls `53a1` and `203b1`, the downstream exact discriminants are negative, hence `E(R)` is connected. Therefore the PARI connected-component period is the same real-period normalization used by the protected R5-RECIP plus symbol on these controls. Path orientation changes only sign and is irrelevant modulo two.

This audit admits PARI only as an exact rational modular-symbol evaluation interface. It does not import any PARI theorem about Kato classes or nonvanishing.

## External Kurihara reference implementation

Alexandru Ghitza's public repository

`aghitza/kurihara_numbers@1674b964c39c2db5b92f39d10ac707de86694d88`

contains a Sage/eclib implementation of the standard odd-prime Kurihara-number algorithm.

The repository is admitted only as an algorithmic cross-reference for:

- construction of Kolyvagin-prime sets;
- plus modular-symbol summation;
- discrete logarithm factors;
- square-free derivative indices.

It is **not** a literal-`p=2` implementation. Its `check_prime(E,p)` routine explicitly rejects `p==2`. No odd-prime correctness or theorem statement is silently specialized to two.

## Literal-2 reduction used downstream

Protected R5-RECIP, not this audit, is the mathematical authority for

`Delta_n^(2) = 2^t_2 * delta_tilde_n`.

On the protected `t_2=1` controls this becomes

`Delta_n^(2)=2*delta_tilde_n`.

For a prime `ell` with `I_ell subseteq 2 Z_2`, the parity of a discrete logarithm modulo `ell` is independent of primitive-root choice: it is one exactly on nonsquares. Thus a downstream mod-two probe may replace the discrete-log parity factor by the Legendre/Kronecker nonsquare indicator. This elementary reduction is to be checked downstream and is not imported from the external code.

## Reproducibility boundary

A theorem-grade downstream witness must bind:

- the exact elliptic-curve model;
- PARI/GP version 2.15.4 or a separately reviewed equivalent implementation;
- exact rational `mseval` outputs;
- the Kolyvagin-prime congruences and `I_n`;
- the protected R5-RECIP normalization;
- the exact finite index `n`.

A broad numerical scan is discovery evidence only. A nonzero candidate must be replayed by a minimal deterministic certificate before theorem promotion.

## Admitted provider conclusion

`PARI_2_15_4_EXACT_PLUS_MODULAR_SYMBOL_INTERFACE_ADMITTED_FOR_R5_WIT_RECONNAISSANCE`.

The Ghitza repository is architecture-only at literal two.

## Claim firewall

This audit does not establish:

- a nonzero finite Kurihara witness;
- residual Kato/Kolyvagin nonvanishing;
- `R5-RES` or `R5-PRIM`;
- `D2d` or `BSD-R2-A1`;
- correctness of an unreviewed downstream script;
- novelty, priority, public certification, or MATHCERT certification.
