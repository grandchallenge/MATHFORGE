# BSD-001 source audit — exact twist-period transport and modular-symbol rationality for WP57

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP57A-AREA-TWIST-RATIONALIZATION`.
- Protected MATHFORGE predecessor: `6c2f7c8a9a1f646ad48eb1fd13eba845343bf6dd`.
- Protected MATHSOLVE predecessor: `ae694de9c18c6c2ff3e46002bc8ed008f7b4fb01`.
- Disposition: `QUALIFIED_EXACT_TWIST_PERIOD_AND_LRATIO_RATIONALITY`.
- Claim class: source/normalization admission only; no BSD or MATHCERT promotion.

## Primary source A — Pal quadratic-twist periods

Vivek Pal, *Periods of quadratic twists of elliptic curves*, arXiv:1012.0094v2 (21 January 2011).

Primary loci inspected:

- definitions of the BSD real period and imaginary period in §1;
- Main Result 1.1, proved as Theorem 3.2;
- Proposition 2.5, defining the minimal-model scalar `tilde u` place by place;
- Corollary 2.6.

The primary PDF and rendered pages containing Main Result 1.1 and Corollary 2.6 were inspected.

Pal uses

`Omega(E) = integral_{E_min(R)} |omega(E_min)|`,

which is the same whole-real-locus minimal-differential convention as protected WP00. He defines

`Omega^-(E) = integral_{gamma^-} omega(E_min)`,

where `gamma^-` is a generator of the anti-invariant integral homology under complex conjugation.

For a square-free negative integer `d`, Main Result 1.1 gives, up to sign,

`Omega(E^d) = (tilde u/sqrt(d)) * c_infinity(E^d) * Omega^-(E)`.

Taking the positive real period and the positive absolute imaginary magnitude gives the exact positive identity

`Omega(E^d) = tilde u * c_infinity(E^d) * |Omega^-(E)| / sqrt(|d|)`.

Here `c_infinity(E^d)` is the number of connected components of `E^d(R)` and `tilde u` is the explicit minimal-model correction of Proposition 2.5.

Corollary 2.6 proves that if `d` is coprime to the minimal discriminant `Delta(E)`, then `tilde u` is a power of two, and if in addition

`d == 1 (mod 4)`,

then exactly

`tilde u = 1`.

### Selected-lane applicability

Protected WP09 chooses an imaginary quadratic field `K=Q(sqrt(D_K))` with `D_K` a fundamental discriminant, `(D_K,2N)=1`, and `2` split in `K`. Hence `D_K` is odd and

`D_K == 1 (mod 8)`,

so in particular `D_K == 1 (mod 4)` and is square-free.

The protected selected elliptic curve is semistable, so the support of its minimal discriminant equals the set of bad primes, i.e. the support of `N`. Therefore `(D_K,N)=1` gives

`gcd(D_K,Delta(E))=1`.

Thus Pal Corollary 2.6 applies with `d=D_K` and gives exactly

`tilde u = 1`.

The admitted selected-lane period transport is therefore

`Omega(E^D) = c_infinity(E^D) * |Omega^-(E)| / sqrt(|D_K|)`.

No unspecified rational or 2-power factor remains in this period transport.

## Primary source B — Cremona modular-symbol rationality

J. E. Cremona, *Algorithms for Modular Elliptic Curves*, second edition (Cambridge University Press, 1997), online corrected text supplied by the author with publisher permission.

Primary locus inspected: Chapter II, §2.8, equations (2.8.7)–(2.8.10).

Cremona proves from the Mellin transform that

`L(f,1) = - <{0,infinity},f>`.

The modular symbol `{0,infinity}` lies in rational homology. Closing the path with a Hecke operator gives formula (2.8.10)

`L(f,1)/Omega(f) = n(p,f)/(2(1+p-a_p))`,

where `n(p,f)` is an integer. Thus this quotient is rational. Cremona then identifies `L(E_f,1)=L(f,1)` and the corresponding real period of the modular elliptic curve, so

`L(E_f,1)/Omega(E_f) in Q`.

The primary PDF text and rendered pages containing (2.8.7)–(2.8.10) were inspected.

### Downstream transport to the protected twist

The source interface admitted here is the modular-symbol rationality statement for the modular curve attached to a rational newform. Protected modularity identifies the quadratic twist `E^D/Q` with the same rational newform isogeny class. Downstream MATHSOLVE may use ordinary exact isogeny/differential transport to deduce rationality for the specific WP00 whole-real-locus period of `E^D`; that transport must retain any isogeny/differential index needed for an exact numerical equality.

For WP57A the only required conclusion is that the already-defined quotient

`lambda_D := L(E^D,1)/Omega(E^D)`

lies in `Q^x` because protected WP09 gives `L(E^D,1) != 0`. This rationality does not determine its numerator, denominator, or 2-adic valuation.

## Exact downstream interface admitted after protection

MATHSOLVE may use the following bounded source statements.

1. On the protected semistable all-`2N`-split auxiliary lane,

   `Omega(E^D) = c_infinity(E^D) * |Omega^-(E)| / sqrt(|D_K|)`

   exactly, with no hidden `tilde u` factor.

2. The rank-zero twist quotient

   `lambda_D = L(E^D,1)/Omega(E^D)`

   is a nonzero rational number after exact modular/isogeny period transport.

3. The source interface does not evaluate `ord_2(lambda_D)`.

## Boundaries retained

This audit does not prove or assume:

- the rank-zero BSD formula for `E^D`;
- any equality between `lambda_D` and Tamagawa/Sha/torsion data;
- any parity, integrality, numerator, denominator, or 2-adic-unit property of `lambda_D`;
- the value or parity of the Heegner index `m_K(f)`;
- `C_f=1` or even that `C_f` is a 2-adic unit;
- fixed-2 p-adic-height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- cancellation with the protected WP54A class-number/unit or bad-prime factors;
- final WP06 quadratic normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, priority, patentability, or commercial claims.

## Provider disposition

`QUALIFIED_EXACT_TWIST_PERIOD_AND_LRATIO_RATIONALITY`

The source interface is restricted to exact period transport and rationality of the central-value/real-period quotient. It does not admit the arithmetic BSD evaluation of that rational number.
