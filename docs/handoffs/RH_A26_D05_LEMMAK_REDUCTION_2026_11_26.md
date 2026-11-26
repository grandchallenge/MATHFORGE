# RH-A26 D05 — Lemma K finite-module reduction

Disposition: independent conventional reconstruction of the actual cardKill/cardRed/tensCard, residual generator estimate, reduction, numT, numFin, and lemmaK_of. This establishes the reduction conditional on the genuine KBridge and TorsBoundPow, not the construction of KBridge or the arithmetic homology torsion theorem. Retain source constants.

## Source recovery and identity

CHAD authenticated tunnel returned NOT_FOUND (client unseen for 300 seconds). Recovered source access via public mirror tamnd/riemann-lean, pinned commit 54f24d40f22dda515b978dfacfb3164991d30317. Its SOURCE.md declares archive SHA-256 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc, matching the protected original intake. The mirror reports byte-for-byte equality; this turn did not independently download and rehash the full original archive. The recovered files are identified by their returned Git blob IDs below. This is a source-reading recovery, not original Lean replay.

Paths relative to lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties:
| Module | Git blob |
| --- | --- |
| GeneratorCountTuples/LemmaK.lean | 8726ea4259cd1f0fcb350eca97a3be2478261c87 |
| GeneratorCountTuples/LemmaKOfPublished.lean | 82044f2422c5b48970bd94223e33087a7896fc40 |
| GeneratorCountTuples/Bridge.lean | c995485ab93aa56e1eabbdd1900429075fb4c65b |
| GeneratorCountTuples/Reduction.lean | 1cfb92c81ec5c4ed77aac5a7cce457add1e55721 |
| GeneratorCountTuples/CardRed.lean | 687dc64db008616c2c378cf471f7d233db5ff9ec |
| GeneratorCountTuples/CardKill.lean | b4e8ea238f7c5872e9ecf2d7a2fd34becbbc6631 |
| GeneratorCountTuples/TensCard.lean | 674a872e24da91062c9d648b683a7a7502d37367 |
| GeneratorCountTuples/TensTors.lean | 2525b87fbde4cb0941f8802a140bfe8c21b8fa12 |
| GeneratorCountTuples/TensSurj.lean | 1807e6cc0f599678f91374fdf2a931229e47ce5b |
| GeneratorCountTuples/CardH2QuotientLeSha.lean | d0fb6c38a5b1c692fc1152ae78c479e9ba38345e |
| GeneratorCountTuples/ShaDualCard.lean | dc8de27f233ffc28f79470a7f8ba5d3f5b625b8d |
| GeneratorCountTuples/ShaZmCard.lean | 382a94416d7d9562531942d10b29f8058d807abe |
| GeneratorCountTuples/ChiTriv.lean | 6aa3b87fd39127a7a5bf2162dff1fa6a43ff2444 |
| GeneratorCountTuples/PrimeLe.lean | 96d3449535b80f2228cd18425386d8ef5a6bfb67 |
| GeneratorCountTuples/NumGens.lean | 4589c64172fee203f70d695109ed823dc7e1df0a |
| GeneratorCountTuples/NumT.lean | 8cfa46dc1a1ffacbc5653d85c9bcbd4825d85b49 |
| GeneratorCountTuples/NumFin.lean | cdea1fa3945aef9d27013aa240a06c273901a28c |
| GeneratorCountTuples/TorsBoundPow.lean | 3552e823716da4241d053c2cdfe0a116039e7886 |
| HermiteNormalForms/TorsMain.lean | b1f243a54bfcf9e7c9f01a6cb6afb726c961a92c |
| HermiteNormalForms/Assembly.lean | 2170a3e28188b4e75f62aade0ae9e7890155076c |
| HermiteNormalForms/Orbnum.lean | 91b6071b9a06356e587ccafae21fd8354f52cb76 |
| TensorHomCubes/KBridgeOfKPublished.lean | c5623929c5dd753b74fa685ac3c60da8186132d3 |
| TensorHomCubes/KBridgeOfKPublishedW.lean | a71500761dfdf61de0402ff0f457959cfbd0c852 |
| HeightAndVanishing/PublishedTheorems.lean | d9ad2a0b465114d690813335c42c6c21bc7fd8f2 |

## 1. Exact comparison contract and finite-module estimate

Fix the actual totally complex number field L, degree n, absolute discriminant D>=1, prime l, HasMuQ, actual LData, and e>=1. Put R=Z_l, X=H2(zlTw D_source(e+1)), and H=H_{2e}(GL_{4e+4}(O_L),Z) with the actual trivial integral coefficient representation. Write T=torsion(H). The genuine KBridge supplies a FINITE R-module K, a surjection p:K->X, and R-linear h:K->R tensor_Z H such that l^c ker h=0, with c=cOne(2e)=sum_{j=1}^{2e}(j+2)=e(2e+5). The finiteness of X already follows from the surjection; the remaining problem is quantitative. In particular, the bridge is stronger than an abstract comparison of rational vector spaces or a map from an unspecified potentially infinite K. Do not presume this existence.

Let Y=p(ker h), an actual submodule of X killed by l^c. By structure theorem for the finite R-module X, X is a sum of cyclic l-power modules of exponents a_i>=1. Then |X/lX|=l^r, with r the number of summands, and |X[l^c]|=l^(sum_i min(a_i,c))<=l^(rc). So |Y|<=|X/lX|^c, including c=0. This proves cardQuotPow/cardKill in the needed instance. The composite K->X/Y kills ker h and is onto, so K/ker h=im h surjects onto X/Y. The exact identity |X|=|Y||X/Y| proves
    |X| <= |X/lX|^c |im h|.
This is the source cardRed. No injectivity of h or p is assumed. No bound on |K| is needed.

For any abelian H with finite torsion subgroup T (H itself need not be finite-generated), tensor the exact sequence T->H->H/T with R over Z. R is torsion-free and hence flat over the PID Z. Moreover H/T is torsion-free, so R tensor (H/T) is torsion-free: tensor the injection multiplication by a nonzero integer on R with the flat module H/T. Thus any finite-order element of R tensor H belongs to the image of R tensor T. For each t of finite order N and any a in R, write a=k+Nb with k integral, using R/NR=Z/l^{v_l(N)}. Then a tensor t=1 tensor (kt); sums of pure tensors give the source tensSurj. The map T->R tensor T is onto, so every finite submodule of R tensor H has cardinal <=|T|. Apply to im h, finite since K finite, to get
    |X| <= |X/lX|^c |T|.
This is exactly the source reduction's algebraic core, not a claim that H itself is torsion or finite. A large free part of H is irrelevant to the finite image. Example: X=(Z/9)^2, c=1, p=identity, h the map to X/3X. Then |X|=81, |X/3X|=9, |im h|=9, and the bound is equality. Without the kernel-annihilation hypothesis take h=0 and X=Z/27; c=1 would incorrectly bound 27 by 3.

## 2. Residual generator budget

From #615's actual finite-to-limit reduction (H3 residual vanishing, H1 finite and continuous cocycle lifting), X/lX identifies with H2(G_S,T_1), T_1 the residual cyclotomic twist of order e+1. This fact does not require X finite length. Source HasMuQ gives a primitive l-th root in L (square the primitive fourth root if l=2). Thus chi mod l is trivial on G_L and on G_S by the source compatibility, so the residual dual twist 1-(e+1) is the trivial F_l representation, including negative powers. Evaluation at 1 identifies the linear dual with F_l equivariantly and commutes with all restrictions. This proves chiTriv and shaDualCard.

Finite PoitouTate ShaDual gives |ker loc2|=|Sha1(F_l)|. The latter is a group of continuous homomorphisms G_S->F_l trivial on each decomposition group over l; inflating to G_L produces everywhere-unramified characters, even split at l. Ordinary Hilbert class field reciprocity for totally complex L puts this space inside Hom(Cl(O_L),F_l), whose size <=classNumber L by the finite abelian group decomposition. This uses the actual local kernel and no assertion that all unramified characters split at l. By finite local Tate duality each local H2(T_1) has cardinal at most l (its dual is an invariant subspace of F_l); number of primes over l <=n. Counting kernel and image of loc2 gives
    a:=|X/lX|<=classNumber L * l^n.
This reconstructs shaZmCard, card_H2_quotient_le_sha, card_mod_le under exactly the previous finite-level and ordinary class-field inputs.

The same source generator estimate follows from a conventional Minkowski bound, as already used in #610: each class has an integral representative of norm <=sqrt(D), since the usual Minkowski prefactor <=1. For n>=2, AM-GM gives n!/n^n<=(3/4)^n and r2<=n/2, hence prefactor <=((3/4)sqrt(4/pi))^n<1; n=1 immediate. For X0>=1, number of ideals of norm <=X0 <=X0^2 zeta_L(2)<=X0^2 2^n (Euler factors dominated by those of zeta(2)^n, zeta(2)<=2). Thus log classNumber <=log D+n log 2. Consequently
    log a<=log D+n log 2+n log l
          <=4 n log(2D) log l.
Indeed log l>=log 2>1/2, n>=1, so log D<=4n log l log D, and n log 2+n log l<=2n log l<=4n log 2 log l. This retains precisely the source numGens coefficient 4; different classical proof of its class-number input, not a changed bound. Since L contains mu_l, cyclotomic degree l-1<=n (l=2 trivially), so log l<=log(n+1). All logarithms are nonnegative.

Combining with cOne(2e)<=2e(2e+3), from 2 cOne(m)=m(m+5), yields the exact source reduction:
    log |X| <= 4 n log(2D) (2e)(2e+3) log(n+1) + log |T|.
This is valid for every actual LData and e>=1 satisfying the bridge and finite T, under the stated finite-level inputs. It is not a proof of the bridge.

## 3. Numerical conversion with source constants

The source TorsBound(C) asks for finite T and log |T| <= tBound(C,m,N,n,D), with m=2e, N=4e+4 and
    tBound=exp(C*m*(n*N)^3*N*log(2D*n*N)).
Put x=2en>=2, L0=log(2D)>=log2>1/2. Then m<=x, N<=4x, nN<=4x, and log(nN)<=nN<=4x. Thus log(2D*nN)<=L0+4x<=9xL0. Multiplying nonnegative factors gives
    C*m*(nN)^3*N*log(2D*nN)<=2304 |C| x^6 L0.
Choose natural k with 2^k>2304|C|, hence x^k>=2^k. Then tBound<=exp(x^(k+6)L0)=kBound(k+6,e,n,D), exactly numT and TorsBound.pow. If the source geometric torsBound constant 49 is established, k=17 is an admissible witness because 2304*49=112896<131072. This merely instantiates the source witness, not an optimized constant.

For TorsBoundPow(C) take C_K=max(C,0)+9, x as above, b=x^max(C,0)>=1. The residual coefficient satisfies
    4n(2e)(2e+3)log(n+1)<=40 n^2 e^2=10x^2<=x^9-1,
using e>=1, log(n+1)<=n, x>=2. Hence the complete right-hand side of reduction is at most
    exp(bL0)+(x^9-1)bL0 <= exp(b x^9 L0).
The last inequality follows from exp(s+t)=exp(s)exp(t)>=exp(s)(1+t)>=exp(s)+t for s,t>=0. This is the exact source numFin, and proves conditional lemmaK_of. With the previous admissible k=17 and C=23, source recipe would allow C_K=32, conditional on actual torsBound(49) AND KBridge. No assertion that 32 is optimal or that either input has been discharged.

## 4. Actual next obligations, not a generic K-theory citation

KBridgeOfKPublished.lean and KBridgeOfKPublishedW.lean in the mirror define Published.KPublished and KPublishedW structures. Their fields are plus construction, acyclic homology, Milnor, Hurewicz, homological stability, finite generation, Borel rank and Dwyer-Friedlander. The W variant Hurewicz hypothesis permits an extra prime-to-l integer factor in its kernel annihilator. The files themselves do not prove the conversion to KBridge (their K namespace is empty). The exact supplying theorem needs to be located and audited, including the finite comparison module and the l-adic exponent loss. In particular a proof of finiteness of X cannot be replaced by a rational K-theory comparison. No claim of an unproved assumption in the headline follows merely from the local wrapper; the import closure and actual supplying proof must be inspected.

The separate torsMain is not just an appeal to a known bound: it invokes HermiteNormalForms.Assembly.torsBoundPow. That uses sx_exact from ConvexNerveComplexes.AcycSimp and TorsionBoundsChains.TupExact, actual Sx tuple complex, finite orbit estimate orb, stabilizer bound stab, TorsionBoundsChains.mainFace and torsBound_of. Orbnum bounds the orbit-count expression by (2 D nN)^(12(p+1)(nN)^3 N) where p is a tuple degree, not the measuring prime. Assembly uses 12(p+1)<=24p for p=2e>=2 and source stabilizer size <=3^((nN)N), then obtains constant 49. The geometric construction, exactness, orbit and stabilizer claims, and homology torsion estimate are NOT verified by this numerical comparison. They are the next independent reconstruction target.

No original-source Lean replay, unconditional Lemma K, VWin, RH/GRH certification, or independent external review. The finite-level classical inputs, exact source correspondence and remaining other-sign/window/count hypotheses remain explicit. Source-search fallback retained the prior lock by declared archive match, with full independent byte rehash pending when CHAD returns.

Boundary: RH-A26-D05_LEMMAK_REDUCTION_RECONSTRUCTED__KBRIDGE_CONSTRUCTION_ARITHMETIC_HOMOLOGY_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
