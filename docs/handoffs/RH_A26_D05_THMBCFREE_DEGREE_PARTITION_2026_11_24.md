# RH-A26 D05 — composite-field prime restriction and combined minus-length bound

**Disposition:** independent conventional reconstruction of the exact conditional theorem Odd.thmBcFree_of, following #609 (PrimeBound) and #610 (StickBound). Also reconstruct the deterministic arithmetic-to-exponential estimate used by its first downstream consumer, conditional on the source window and height hypotheses. No original Lean replay, foundational certification or conclusion of RH/GRH.

## Source identities

Reopened from the pinned original intake, relative to Development/AutomorphicArithmetic/AutomorphicVarieties:

| Module | SHA-256 |
|---|---|
| OddResidueBounds/DegExistsLift.lean | f595c6c2a1dc4459e3cbd1558fe3421cbcea4770a041c7f87fba3fb4505b772d |
| OddResidueBounds/ThmBcOfPsiBound.lean | 90808ac87265e481e18121781c242726f0a8ae0bfd9832cf3b4d31c079c49d24 |
| OddResidueBounds/ZeroMemUnrHom.lean | c6cac1eefc91d4bf1972ae1b8ccc54ab3ce3238e19e397dafb49bb739bcecf48 |
| StmtFields.lean | 6504b5c58704921aae65b2651c419051c6f0cf3c040bc517dc663cfa19dce50a |
| PrimeSetBoundDataOfPrimitiveChar.lean | 8d78f096654f4cdd977c71b1b163bb0883c53a295d0928816d96b0d6a8362cf1 |
| LengthEqAddEigen.lean | b10fd612b8aec69ff4f2839049eb06613d0078d2aeddac738f0f8461eb3151f2 |
| CMFieldExponentialBounds/ConductorBoundsOfIsChiField.lean | 0aac6a0e5cfa8c19b5f19d15fcad05fac66b882520fdcd7253b2d300e3f47309 |
| CMFieldExponentialBounds/ErrorTermsLeSqrtExpRpow.lean | 1725fcaea1649db68c3876803ae79e3140ac464dbbe9b04be77cf47b51ecdc59 |
| CMFieldExponentialBounds/minusle.lean | cfcfbbd6e38f27efcfa3b0647c824de3470705e17f5d665bb0dd935ff87fdf3b |
| CMFieldExponentialBounds/LogConductorMulHeightLeOfPageN.lean | 2aad58f4fae8542a82dd7d7cd408018bd6124d46d794995638e8b6d6c71dead2 |
| CMFieldExponentialBounds/AdmissibleOfPageN.lean | ded642308ff9cd83eed14643f20899986c271c73f2ee900bccf6f7a32f3b350d |
| HeightAndVanishing/JointWinOfCounts.lean | 3c71cf0dabc617e3d1ab9fc04939c311e4242912407cdfbc71c8e0764563d558 |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/HVCore.lean | 695927bf54a16053ae211e0d1f7ad26217806520d60f884459f9c0d7aac1460d |

## 1. Genuine composite-field restriction

Notation distinguishes the source's prime named d from a field degree: write q,p for the auxiliary primes (source q,d), A=(m,H) for AbF, o=[U(m):H]=A.deg, h for the field parameter (source e in IsCompField), n=[E:Q], F=condF E, and j:E->Q(mu_N) for the embedding in IsCompField. Let U(v)=(Z/v)^*. By PrimePair, q,p are distinct odd primes coprime to m. The actual source IsCompField requires 2^(h+2),m,q,p to divide N and gives the full fixing criterion for every cyclotomic automorphism:
    a = +/-1 mod 2^(h+2),
    [a]_m in H,
    (a/q)=1,
    (a/p)=1.
Here parentheses are Jacobi symbols (Legendre symbols at the prime moduli). This is not merely a statement that E embeds in some cyclotomic field.

The Galois group of Q(mu_N) is U(N), with a acting by raising a primitive N-th root to a. Define the homomorphism
    U(N) -> U(2^(h+2))/{+1,-1} x U(m)/H x {+1,-1} x {+1,-1}
by the four conditions above (reduce, reduce, quadratic character, quadratic character). Both Jacobi symbols are multiplicative and nonzero on these units. Its kernel is exactly the fixing subgroup of j(E), by the source criterion. The fundamental theorem of finite Galois theory and the first isomorphism theorem identify the degree n with the order of the image. The target has order 2^h * o * 4, since U(2^(h+2)) has order 2^(h+1) and the sign subgroup has order two. Hence
    n divides 2^(h+2) o.
In particular every odd prime l dividing n divides o. This proves the exact DegExistsLift.deg statement, including overlap between the two-power modulus and m, and m=1 (unit group trivial). No independence of the four restrictions was assumed. The source proves the same support statement via the exponent 2^(h+1)o and Cauchy's theorem, without asserting that the degree equals that exponent. Our product-image argument also gives the stronger degree divisibility above. In fact the odd prime supports of n and o agree: projection to U(m)/H is onto by surjective unit reduction, whence o divides n. Under the actual coprimality of q,p with m and the two-power modulus, CRT also makes the two quadratic components independent of the first two. Only the inclusion of supports is needed downstream.

A larger cyclotomic ambient field is not a larger composite field. For example h=2, m=7, H={1,-1}, o=3, q=11, p=23, N=16*7*11*23. The four conditions have image order 4*3*2*2=48. Although phi(N)=8*6*10*22=10560 contains the primes 5 and 11, the composite-field degree 48 has odd prime support {3}. Using phi(N) instead of the quotient degree would introduce spurious bad primes. Conversely taking the whole unit group as H would give o=1 and no odd bad prime. These are finite group examples of the exact defining criterion.

## 2. Minimal cyclotomic modulus and all quantifiers

Since IsCompField supplies a positive witness N, the set of positive cyclotomic moduli admitting an embedding of E is nonempty and has a least element F=condF E, which belongs to that set. Thus F>0 and E embeds at F. This only uses well-ordering and the source definition, not equality with a conjectural conductor. Also n<=phi(F)<=F by finite-dimensional injectivity.

The source ThmBcFree is existential in a SINGLE real constant C, uniform in A,h,t,q,p,E; h>=2, t>=2, PrimePair and IsCompField hold, E is CM. Its conclusion VVminusLe is universal in the algebraic closure Omega of E and in a family ld(l) of source LData at every prime l. It asserts first that each minusLen for l odd and 1<=e<t is finite, then a bound on the real sum over ANY finite set S of odd primes, with the exponent range Ico 1 t (t excluded). These are not bounds on the entire Sha group at 2 or on the opposite sign component.

Fix arbitrary Omega, ld and such an exponent e. Write L_l(e)=minusLen(ld(l),e) in extended lengths; by #609 PrimeBound under PsiBound, for l odd not dividing n these lengths are finite. By #610 StickBound with C=40, for odd l dividing n they are also finite (Procyc holds automatically at odd l). Only now pass to their ordinary natural values. For all finite S of odd primes partition exactly into
    S_good={l in S : l does not divide n},
    S_bad={l in S : l divides n}.
The degree restriction gives S_bad subset P_o, the finite set of DISTINCT odd prime factors of o. o is a positive subgroup index, so P_o is well-defined, including empty when o is a power of 2. No multiplicity factors or enumeration of all primes are needed. All estimates below use nonnegative terms.

## 3. Assembly of exact minusBound

Write k=e+1 and bnd(F,k)=16 F^(k+1) k!. Good-prime estimate from #609, weakened to the exact original PrimeBound constant n:
    sum_(l in S_good) log(l)L_l(e) <= n log bnd(F,e+1).
Since 2<=k<=t and tF>=2, 16<=(tF)^4, F^(k+1)<=(tF)^(t+1), k!<=k^k<=t^t<=(tF)^t. Thus log bnd(F,k)<=(2t+5)log(tF). Sum over e=1,...,t-1, interchange finite sums, and use (t-1)(2t+5)<=3t^2 (difference t^2-3t+5=(t-1)(t-2)+3>0). The good part is at most
    3 n t^2 log(tF).
This reproduces log_bnd_le_mul_log and the exact first term of the source, without requiring the optional sharper d/2 parity result.

For each l in S_bad, #610 gives
    log(l)L_l(e) <= 40 l n^2 (e+1) log^2(e l F).
Here e>=1 so the logarithms are nonnegative; e+1<=t and e<=t, hence the right side <=40 l n^2 t log^2(t l F). There are t-1 terms, so the contribution <=40 l n^2 t^2 log^2(t l F). Summing and enlarging S_bad to P_o by nonnegativity gives exactly
    sum_(l in S) log(l) sum_(1<=e<t) L_l(e)
      <= 3 n t^2 log(tF) + 40 sum_(l in P_o) l n^2 t^2 log^2(t l F)
      = minusBound(40,o,n,F,t).
This proves the source VVminusLe including individual finiteness and every finite-set bound, hence Odd.thmBcFree_of : PsiBound -> ThmBcFree under the reconstructed inputs. C=40 is a permissible explicit universal witness from #610, not the source's own chosen witness. In particular no bad primes appear just because q,p vary. The bad-prime bound cannot be applied to l=2 without an additional hypothesis; the theorem does not attempt this. No continuity, count, or dimension property of ld is inferred from its indexing.

An immediate useful consequence of the uniform finite-set bound is that for fixed E,t and ld, only finitely many odd primes have positive minusLen at any exponent below t: a nonzero such term contributes at least log 3, so arbitrarily many distinct ones would contradict the bound. This is not an effective list of which groups are nonzero; at good primes the earlier integer product supplies a more specific support restriction.

## 4. Deterministic downstream bridge, with source hypotheses explicit

The actual first consumer is HV.Core.of_four_alt, calling HV.vwin_of_counts in HeightAndVanishing/JointWinOfCounts.lean, which uses thmBc_iff and vwin_of_joint. It ALSO requires PoitouTateDuality, LocalFinitenessK, LocalTateDualityK, LemmaK, ThmBab, CountI, CountII, CountIII, CountV and CountZ. The minus-length bound does not prove these. We reconstruct the part supplied by ThmBcFree, not the independent window/count statements.

The forward direction ThmBcFree -> ThmBc Ct evaluates admitted e,t at any x>=2 and uses e(x),t(x)>=2. For the converse when Ct>=1, take arbitrary integers h,t>=2, x=max(2^h,t), and functions equal to h,t at x and 2 elsewhere. For y>=2, their pointwise bounds 2^e(y)<=y^2 and t(y)<=y^Ct follow from x's definition or y>=2. No regularity of admitted functions is required by its source definition. This proves thmBc_iff with the same C. It does not establish a window.

The conductor bound needed for the composite field follows directly from the same fixing criterion. Put L=lcm(2^(h+2),m,q,p), dividing N. Every cyclotomic automorphism congruent to 1 modulo L satisfies the four conditions, so j(E) is contained in the fixed field of the reduction kernel U(N)->U(L), namely Q(mu_L) inside Q(mu_N). The latter equality follows from the action on a primitive L-th root and finite Galois theory. Therefore
    1<=F<=L<=2^(h+2)mqp, n<=F.
For the IsChiField specialization A=AbF.ofChar psi, m=psi.N, and H is the character kernel, as proved by StmtFields.isCompField_ofChar. This establishes the conductor bound needed in the actual consumer.

For any W with log(Ft)<=2W, let u=Ft>=1. Since n<=F and t>=1,
    3 n t^2 log(tF)<=3 u^3<=3 u^4,
    l n^2 t^2 log^2(t l F)<=l^3 u^4,
where log v<=v for v>=1 and the logarithms are nonnegative. Thus with C arbitrary real, K=3+|C| sum_(l in P_o) l^3,
    minusBound(C,o,n,F,t) <= K u^4 <= K exp(8W).
This is the precise source minusBound_le_exp_of_log_le. K depends on C,o, not on q,p,x,t. This is why the degree restriction mattered: it keeps the constant independent of the auxiliary primes that vary in the asymptotic argument.

For the actual arithmetic threshold, use the numerical upper bound from PageN as used in LogConductorMulHeightLeOfPageN: 2^h<=2 x^(2+8 eps), 0<eps<1/52, t<=x^Ct, log(qp)<=x^(eps/4). These explicit inequalities are sufficient for the following calculation; we do not here reconstruct existence or the complete PageN contract. Set W=x^(eps/4), x>=1. Then
    log(Ft) <= 3 log 2+log m+(2+8 eps+Ct)log x+W.
As log x=o(x^(eps/4)) and m,Ct,eps fixed, for all sufficiently large x the constant and logarithmic terms together are at most W. The threshold is uniform in q,p,h,t satisfying those bounds. Consequently log(Ft)<=2W, and the minus contribution is at most K exp(8 x^(eps/4)).

The full arithmetic group is reconstructed from the two sign components at odd primes by the actual involution cAct on Sha. Its involutivity and preservation of Sha follow from the cohomology action previously reconstructed in #609. Since 2 is a unit, x maps to ( (x+s cAct x)/2, (x-s cAct x)/2 ) for s=(-1)^e; inverse is addition. Thus shaLen=plusLen+minusLen, even for extended lengths before either is finite. This is the argument of LengthEqAddEigen.shaLen_eq_add. With the given BoundedHeightTwoPlaceCondition at 2 and given VVplusLe at odd primes, all lengths are finite in range; partitioning any finite prime set into {2} and odd primes yields VVle with budget B2 log 2+Bm+Bp, exactly vvle_of_parts. At 2 no splitting is used.

If the other two window estimates actually hold, their budgets in the source are exp(x^(4eps/5)) at 2 and u^C+C exp(x^(4eps/5)) on the opposite sign, with u=Ft. For fixed C,K, define b=x^(4eps/5), a=x^(eps/4), v=x^(eps/5); x>=1 so a<=b, b>=1, and x^eps=bv. Put D=9+2|C|, H=log 2+|K|+|C|+1. Since log u<=2a, the sum of the three budgets is <=H exp(D b). For v>=2(D+log H+1), we have log H+D b<=bv/2, so the sum <= exp(x^eps/2)=sqrt(exp(x^eps)). This is the explicit error-term domination of ErrorTermsLeSqrtExpRpow, with threshold max(1,[2(D+log H+1)]^(5/eps)). It is uniform in u satisfying the actual log bound. No assumption on signs of C,K is needed for this upper estimate because absolute values bound their contributions.

This reconstructs the deterministic arithmetic assembly and the downstream numerical domination **conditional on** the separate window/height statements; it is not a reconstruction of JointWin, CountI/II/III/V/Z, the simultaneous parameter choice of vwinAt_of_joint, or the original Lean declarations. Next inspect the exact window selection and the actual other-sign and prime-2 bounds, not a hypothetical improved minus estimate. The fixed classical inputs of #604--#610 and their foundational correspondence remain outstanding.

Boundary: RH-A26-D05_THMBCFREE_CONDITIONAL_RECONSTRUCTED__WINDOW_SELECTION_OTHER_SIGN_AND_TWO_PLACE_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
