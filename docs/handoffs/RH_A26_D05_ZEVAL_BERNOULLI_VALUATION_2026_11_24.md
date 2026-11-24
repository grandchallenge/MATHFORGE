# RH-A26 D05 — exact zEval Bernoulli valuation bridge

**Disposition:** independent conventional proof of the genuine zEval theorem under the explicit classical inputs below. Strengthens its two divisibilities to an exact valuation identity and an explicit precision threshold. No original Lean replay, exact foundational correspondence, exceptional branch, or RH/GRH certification.

## Source identities (reopened from pinned intake)

Paths relative to original lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties:

| Module | SHA-256 |
|---|---|
| PrimitiveFrobeniusFixed/ZeNorm.lean | f6bb5faff7c24c765cefd6d64f469ebdef9f7107cd1638043ed79ed55a01b658 |
| PrimitiveFrobeniusFixed/GenBUnits.lean | ab280a72e0c867f744af8f5e6839c6485e034b9f3f3cc0d0fe388095100a0893 |
| PrimitiveFrobeniusFixed/IsAdmissiblePrimeListNil.lean | 4a5b83a90871ef58923fddc1c12ae6d3f5ddff7339747c1493a1dd17c758f433 |
| PrimitiveFrobeniusFixed/PrimCase.lean | 7a267aaec723dbe9b97c01e9d92e35756f1d63e02fef2b8a5ead2ce9983b0ab3 |
| StickelbergerElements/SamePrimesMulPow.lean | 524c32ae0db2a97d32cc581c62b8ef6e372891696873d56ff97d8040ddb216e9 |
| StickelbergerElements/StickelbergerBernoulliCoeffExpansionModDenominat.lean | d6e48abd6b19f13d309d6caca11dd46842c17a93771673d72ec267d17fd62d9e |
| GaloisLibrary/BernoulliNumbers/GeneralizedBernoulliChangeLevel.lean | a169be8e9be2eb658c0a1961e07476798b398c9160956322e891077272646dd5 |
| GaloisLibrary/BernoulliNumbers/BNzany.lean | 2e1f8730d2386532e11e486f5c91623691e2caa156ae9c101787ac57bc0a0c30 |
| GaloisLibrary/BernoulliNumbers/BNzC.lean | 6323f3653aef7dc264b925879819620dc9a24e66baf8990434b10b725453899c |
| GaloisLibrary/BernoulliNumbers/MapGenBChar.lean | 7a84fd98752f7b2a310001da8a8f3dcb7447f967173d5bbdf28f3025d6a51129 |

## 1. Exact target

Let l be odd prime, O the source coefficient DVR finite over Z_l, embedded in PadicAlgCl l. Use additive valuation v with v(l)=1 and v(0)=infinity; divisibility of elements in O is equivalent to comparison of their valuations. The normalized DVR valuation is v_O=r*v, r=v_O(l)>0. This is the standard extension of the l-adic valuation to the finite coefficient field. It gives the norm/divisibility implications in ze_norm.

Let psi be a primitive Dirichlet character at f, e>=1, k=e+1, and psi(-1)=(-1)^k. Set alpha=(chi_l^e dirG(psi))^(-1), with chi_l the l-adic cyclotomic character in O. Assume some g has alpha(g)-chi_l(g) a unit. No prime-to-l order assumption on psi is needed for zEval itself. The latter is used in prim_case's separate ramification argument.

For P_k=product of primes <= k+1, the source uses D=dk(k)=2kP_k and a=alN(k,psi)=f P_k B_(k,psi) in O, not the ordinary imprimitive sum at a raised modulus. Set T=B_(k,psi)/k. For every a0!=0 in O the target is m,b,F=N0*l^m, N0=f/l^v_l(f), lifts sigma_t of (Z/F)^*, with Dat and b<F, such that z=zVal(alpha,sigma,b) satisfies a0*z | l^m and z | a. The argument below establishes v(z)=v(T), for every sufficiently large m and ANY choice of lifts sigma once b is selected from the same fixed g. It also establishes T in O; the source does not require this before the proof.

Imported foundations: classical von Staudt–Clausen (as in PR #604), finite cyclotomic Galois surjectivity and compatibility of its character reductions, finite coefficient DVR valuation law, and the ordinary Fourier series of Bernoulli polynomials and Euler product in the absolutely convergent half-plane. Nonvanishing can be derived below with a finite Fourier argument, rather than assuming a p-adic L-function result. No imported zCong, zEval, count, NuSys or generalized Bernoulli level-change theorem is needed.

## 2. Nonzero primitive value and raising the level

The values of psi are roots of unity or zero, so they generate a finite algebraic number field over Q. Embed that field into C; the rational Bernoulli polynomial and character sums are preserved injectively. To see B_(k,psi)!=0 for k>=2 and matching parity, use
    B_k(x)=-k!/(2 pi i)^k sum_(n!=0) exp(2 pi i n x)/n^k.
For primitive psi the finite Fourier sum A(n)=sum_(t mod f) psi(t) exp(2 pi i nt/f) equals psi^(-1)(n) A(1), with inverse character extended by zero. For unit n this follows by reindexing. For nonunit n, choose p|gcd(n,f); the character is nontrivial on the kernel of unit reduction from f to f/p (otherwise it factors at smaller conductor by surjectivity, contradicting primitivity). Some unit u in this kernel has psi(u)!=1 and n*u=n mod f; reindexing forces A(n)=0. Parseval gives sum_n |A(n)|^2=f*phi(f), hence |A(1)|^2=f. This includes f=1 with A(1)=1, using its one residue and trivial character. With parity, the positive and negative Fourier terms agree; thus
    B_(k,psi) = -2 k! f^(k-1) A(1)/(2 pi i)^k * L(k,psi^(-1)).
The absolutely convergent Euler product at k>=2 is nonzero: the sum of absolute local perturbations p^(-k) converges, each factor is nonzero, and the tail product has convergent logarithm. The constant is nonzero. Therefore B_(k,psi) and T are nonzero in the original field. This reconstructs the needed k>=2 portion of b_nzany without importing its more delicate k=1 case.

For F a multiple of f let chi be the induced character (zero on nonunits of F). For any prime p, the Bernoulli distribution identity
    sum_(j=0)^(p-1) B_k((x+j)/p)=p^(1-k) B_k(x)
follows by summing the generating functions t exp(xt)/(exp(t)-1), or comparing their coefficients. For raising a modulus H to pH, sum over all lifts of each residue first, then remove multiples of p. If p|H they were already excluded; otherwise the removed sum, by writing the argument as p times a residue at H, is p^(k-1) psi_H(p) B_(k,psi_H). Thus
    B_(k,chi)=B_(k,psi) prod_(p|F,p not|f)(1-psi(p)p^(k-1)).
If F=N0*l^m, m>=v_l(f), its only possible new prime is l. Since e>=1 and |psi(l)|_l<=1, 1-psi(l)l^e is a unit (also if psi(l)=0). Hence v(T_F)=v(T), T_F=B_(k,chi)/k. This proves the source ze_gen on the actual levels, including when l already divides f. It is an equality of valuations, not necessarily of ordinary Bernoulli values.

## 3. Pointwise rational identity with the actual denominator

Write C_F(u)=F^(k-1) B_k(u/F)/k. Bernoulli expansion gives
    C_F(u)=u^k/(kF)-u^e/2+F/(kP_k)*R_F(u),
where R_F(u) is the integer sum over j=2..k of binom(k,j)(P_k B_j) F^(j-2) u^(k-j). The integrality of P_k B_j follows from the classical Bernoulli denominator theorem, including B_0=1, B_1=-1/2, odd j>1 zero, and positive even j squarefree denominator with p-1|j. Thus the formula is precisely the source coefficient expansion with 2F/D.

Fix b and u unit residues in [1,F-1], and set j=floor(bu/F), y=bu-Fj the unit representative. Because y!=0,
    th(F,b,u)=2j-(b-1).
Indeed floor(b(F-u)/F)=b-j-1. By binomial expansion y^k=(bu)^k-k(bu)^e F j+F^2 A, and y^e=(bu)^e+F C, for integers A,C. Substituting in the expression
    E=b^e th(F,b,u) u^e+2 C_F(y)-2 b^k C_F(u)
gives cancellation of the terms in j and b:
    E = F*[2A/k - C + 2(R_F(y)-b^k R_F(u))/(kP_k)].
Multiplying by D=2kP_k proves D E belongs to F Z (explicit integer quotient 4P_k A-D C+4(R_F(y)-b^k R_F(u))). This is the genuine pointwise congruence of GenBUnits. The denominator and sign are essential; dropping D without further hypotheses is not justified.

## 4. Weighted congruence, then exact valuation

Multiply the pointwise identity by chi(bu) and sum over unit u. Multiplication by b permutes the unit residues. With
    S=sum_(u in units mod F) th(F,b,u) u^e chi(u),
    V=b^e chi(b), U=chi(b)b^k-1,
the result is
    D*(V S - 2 U T_F) in F O.
The reason is that the first sum is V*S, the second is 2*T_F after reindexing, and the last is -2 b^k chi(b)*T_F. Nonunits of F contribute zero. This directly proves zCong, with valuation at least m, and does not require dividing by a possible nonunit D in O.

Choose m>=max(1,v_l(f)) and take b to be the least representative of the cyclotomic action of the fixed g mod F. Then b is a unit, b<F, and cyclotomic surjectivity supplies arbitrary lifts sigma_t of each unit residue. For each t, chi_l(sigma_t)=t mod l^m, and dirG(psi)(sigma_t)=psi(t) exactly. Hence alpha(sigma_t)^(-1)=t^e psi(t) modulo l^m O. Since psi(t)=chi(t) on units, the actual zVal satisfies
    z-S in l^m O.
This also proves the source congruence independently of the choice of lifts. For an element fixing mu_F, alpha=1 mod l^m; for a lift of -1, alpha=-1 mod l^m since (-1)^e psi(-1)=-1. Together with odd l, the choice of N0, m>=1, and the fixed unit witness, these are ALL Dat fields, including notCyc. No continuity of alpha into a discrete infinite ring is asserted.

The same fixed witness ensures U is a unit: write u_g=alpha(g)^(-1). Then
    U = psi(b)b^k - 1 = u_g chi_l(g)-1 mod l^m O.
The latter equals -u_g (alpha(g)-chi_l(g)), a unit, and l^m lies in the maximal ideal. V is also a unit since b and chi(b) are units. 2 is a unit because l odd. This gives the exact place where the exceptional condition matters.

Now for the given a0!=0 choose ANY integer
    m>=max(1,v_l(f)),   m>v(a0)+v(D)+v(T).
All RHS quantities are finite because T!=0 and D!=0, and v(a0), v(D)>=0. The weighted congruence implies
    v(V S - 2 U T_F)>=m-v(D)>v(T).
If v(x-y)>v(y) in a nonarchimedean field, v(x)=v(y), by applying the ultrametric inequality in both directions. Since 2,U,V units and v(T_F)=v(T), it follows v(S)=v(T). Since v(z-S)>=m>v(T), the same argument gives
    v(z)=v(T).
Thus T belongs to the valuation ring O of its coefficient field, since z in O and T in that field. This integrality is a consequence, not an extra hypothesis. All estimates hold for every allowed choice of lifts and m above the threshold. In the source multiplicative norm, the strict inequality is |l^m|<|a0| |D| |T|; this is exactly the choice used in ZeNorm.

## 5. Both required divisibilities and the sharper valuation gap

As m>v(a0)+v(D)+v(T), v(a0*z)=v(a0)+v(T)<m. Therefore a0*z | l^m in O. In particular z!=0. This is the required witness for EACH nonzero a0, with no uniform finite m asserted across unbounded v(a0).

The source quantity a=f P_k B_(k,psi)=f P_k k T. The integer multiplier f P_k k has nonnegative valuation, so v(z)<=v(a) and z | a. More precisely
    v_O(a)-v_O(z)=v_O(f P_k k).
This gives exact loss bookkeeping: the conservative denominator multiplier and k account for the entire difference. The counting mechanism from PR #605 with the genuine NuSys from PR #606 yields length ShT(a0)<=v_O(z)=v_O(T) for every nonzero a0, given Rec and the normalizer/unit/ramification conditions of prim_case. The torsion-layer transfer then gives the same bound on the full ShaU. To claim the full primitive nonexceptional branch under only its original hypotheses, the actual primRam character-conductor hypotheses must also be independently audited (not asserted here on the strength of the preceding calculation). This is strictly sharper than the source's v_O(a) bound, on that branch and subject to the remaining inputs.

## 6. Controls and boundaries

For f=5, psi quadratic, k=2, l=3, T=2/5, D=24. At F=5*3^m, m>=1, chi induced, b=2, U=-5 and V=-2 both 3-adic units. The ordinary level-raised Bernoulli value is 16/5=(4/5)*(1-psi(3)*3). The finite integer sum S=8 at m=1,2,3,4. Thus v_3(S)=v_3(T)=0, while a=30*(4/5)=24 has valuation 1. For example a0=3^s, choose m=s+2, yielding the strict required bound. These are surrogate finite sums, not a calculation of absolute Galois lifts; the uniform congruence in section 4 covers the latter mathematically.

Negative control: f=1 trivial character, k=2, l=3. All unit b have b^2-1=0 mod 3, so no witness U unit. T=B_2/2=1/12 has v_3(T)=-1, whereas every actual zVal is integral. The equality cannot hold. This shows why the nonexceptional hypothesis cannot be dropped; it is not a counterexample to the source theorem (nor a resolution of exc).

The general argument, not the regression fixtures, supplies the theorem. Classical cyclotomic and coefficient-field facts, Bernoulli denominator and Fourier theory remain imported as specified; exact original Lean replay and foundational correspondence remain outstanding. Next reconstruct the genuine PrimRam and exceptional exc, integrate the primitive and level-change estimates, and verify their source interfaces. No RH/GRH certification.

Boundary: RH-A26-D05_ZEVAL_EXACT_BERNOULLI_VALUATION_RECONSTRUCTED__PRIMRAM_EXC_FOUNDATIONAL_CORRESPONDENCE_ORIGINAL_REPLAY_OPEN.
