# RH-A26 D05 — active headline Lemma K route and conditional final estimates

## Correction to dependency prioritization

PR #620 reconstructed the genuine parallel GeneratorCountTuples.LemmaKOfPublished route, conditional on KBridge and TorsBoundPow. That argument is valid as a conditional source theorem, but is NOT the actual supplier of LemmaK along the headline path. Earlier statements naming KBridge as the next load-bearing headline obligation were premature. This addendum corrects the priority without deleting the admitted parallel theorem. Do not infer a missing hypothesis in the headline from the parallel wrapper.

Source recovery: same pinned public mirror tamnd/riemann-lean@54f24d40f22dda515b978dfacfb3164991d30317; its declared archive SHA matches original intake as recorded in #620. CHAD remains disconnected; no fresh independent archive rehash. Exact source blobs below.

## 1. Active dependency chain

All paths relative to lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties:
| File | Git blob | Relevant declaration |
| --- | --- | --- |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean | 01c499108485b16d33791a9e46fbb1e2af865522 | vwin_of_hypotheses_H_E_alt calls ZK.lemmaK_litN_alt hH.litN |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/KFinal.lean | 9b26f8a76facea83b64788eaabdf30c492023644 | lemmaK_litN_alt invokes lemmaK_of_litN_alt hN bOdd |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/LemmaKOfLitN.lean | d9b4b0270de55f739f2d097ffba669478feffcb9 | lemmaK_of_litN_alt invokes ZK.lemmaK hB pt_s hN.coh.lfK hN.coh.ltK |
| ModularityArgument/ClassCounting/LemmaKOfLitN.lean | 2b1e21f70e69ace53b5219e9e0807b6de0d1920e | ZK.lemmaK supplies all 21 steps to lemmaK_of_steps |
| ModularityArgument/ClassCounting/LemmaKOfSteps.lean | 6202fdeed68f7ca2c64e2f14ddfd416331bf1c10 | Exact BOdd, SFew, SCount, SSha, SLayer, STors, ShaK, SNum, SFinal contracts |
| ModularityArgument/ClassCounting/BOdd.lean | 4a683e6c236327e51ab03bc84da83f6f1f0602cc | bOdd := PositivityTheory.KB.bOdd_zk |
| LiteratureResults/KTheoryStability/ReductionBoundsTorsion/TorsionIntegers/Bridge.lean | 7ff84d3d02c1f4cfb386505d590e2eb4e0c96f8c | bOdd_zk transports lev and zSeq, then uses bStarOdd |
| LiteratureResults/KTheoryStability/ReductionBoundsTorsion/FinalOdd.lean | a2c342444c2bf90d11b59deb8f2d3d98aa47e6fa | bStarOdd from sBStarOdd_of with sChain, sSep', sBridge, sStab, surjectivity and weight-cycle constructions |
| ModularityArgument/ClassCounting/SFinal.lean | a960a48653fa69c34f72f5f8ed434135ff1163a6 | sFinal |
| ModularityArgument/ClassCounting/NumThree.lean | 900c8e3fca10cdf9256061213dcc9453bf98f3d2 | sNum |
| ModularityArgument/ClassCounting/ExponentLe.lean | 2b3e4233ad68b7007573c70feaf4703d85452b47 | torsAll, sTors |

The actual chain does not use the KBridge hypothesis in this invocation. It constructs a uniform finite Sha bound by counting finite cyclotomic-layer equivariant Kummer classes using homology evaluations, then applies the already reconstructed limiting Poitou–Tate identities. The arithmetic homology torsion estimate remains shared, through KT.tors_le and orbnum (not simply the parallel torsMain wrapper). BOdd concerns rank of the image of a particular iterated difference operator on ODD homology, not the entire homology rank. For L totally complex, k even, k+1<r2(L), n>=2(k+1)+4, l positive, its contract is rank_Z span{zSeq(O_L,l,x,k): x in H_{k+1}(GL_n(O_L),Z)}<=r2(L). No arbitrary K-theory finiteness theorem substitutes for this.

## 2. Independent reconstruction of the actual final step SFinal

Put n=[L:Q], D=|disc L|, e>=1, l prime, X=H2(Z_l(e+1)) for the actual source G_S, and A=Q_l/Z_l(-e). Assume ShaK(C): shaInv=s finite and s log l<=kBound(C,e,n,D). This is the exact premise of SFinal in the actual source, NOT KBridge. From #615 and the original finite-level duality hypotheses, the global length formula says length X+length coker loc2=length Sha^1(A)+sum_v length H0(G_v,A). In particular, by nonnegativity, length X<=s+sum_v length H0(G_v,A), without subtraction of infinite lengths.

Let U_v be the image of the local cyclotomic character. In the usual absolute-local correspondence for the actual LData, the cyclotomic character on G_Q_l is onto Z_l^* (the local l-power cyclotomic degrees are phi(l^j)); the subgroup G_{L_v} has index [L_v:Q_l]<=n. Hence [Z_l^*:U_v]=d_v<=n, finite. Equivalently one may use the source's ineOpen and inertia image inclusion. This explicitly uses classical local cyclotomic/absolute Galois correspondence. In the abelian unit group, (1+l^2)^d_v lies in U_v. On invariants in A it follows that ((1+l^2)^(d_v e)-1) annihilates them (the inverse twist is multiplication by a unit times the same difference). The valuation identity proved in #614 gives exactly 2+v_l(d_v)+v_l(e), valid also at 2. Thus H0(G_v,A) has length at most this value, bounded by 2+floor(log_l n)+e. There are at most n places v. This proves sf_nu/sf_loc with the exact source constants.

Consequently length X <= s+n(2+floor(log_l n)+e), a finite integer. Any finite-length Z_l-module has cardinal l^length by the composition series, all simple modules F_l; no need to assume finite cardinal before proving finite length. Therefore
    log|X| <= kBound(C,e,n,D)+n(2+floor(log_l n)+e) log l.
HasMuQ gives l<=n+1. Since floor(log_l n) log l<=log n, the second term is <=n(3+e)log(n+1). For e>=1 and Y=log(2D)>1/2,
    3+e <= 4(2e)(2e+3)Y.
This bounds the local correction by the exact polynomial term in GeneratorCountTuples.NumFin. The already reconstructed NumFin of #620 gives kBound(max(C,0)+9,e,n,D), establishing SFinal with original exponent. This is an actual downstream use of #615, not merely the parallel KBridge estimate.

## 3. Conditional actual counting assembly SNum

Write E>=1, k=E-1, and suppose the exact SFew, SCount, SSha, SLayer and STors hold. SLayer supplies L', c,d with n'=d n, d<=(n+1)(4E+4), w=l^c<=2n', D'<=D^d w^n', plus restriction length comparison shaInv(L,l,E)<=shaInv(L',l,E), and 2E+1<w and 2E+1<r2(L'). These are not proved by the numerical argument. On any actual Lay(l,c,nu,zeta,gamma) over L', SFew supplies Few with exponent b=2E+(2E+1)(c+2E+1) and bound B=(l^nu)^r2(L') T1 T2, where T1=tc(L',4E+6,2E+1), T2=tc(L',4E+6,2E). Apply SCount (order E), divide by the positive integer (l^nu)^r2(L'), not by a vanishing cardinal. It gives finite EqHom of cardinal <=T1 T2 l^J uniformly in every actual layer, with J=(b+v_l(E))*gens(L')+c+v_l(E). Apply SSha and restriction to get length s of the original field finite and
    s log l <= log T1+log T2+J log l.
Here positivity of l^s<=T1 T2 l^J ensures both T_i are positive; the source uses Nat.card, so one cannot simply log potentially zero values. This is the precise cancellation of the growing layer factor; it is why the counting route gives a uniform bound. The arithmetic Few/Count/Sha/Layer premises are still open, not replaced by this cancellation.

The numerical estimates in NumThree can be reconstructed with the exact constants. Set u=2E n'>=2, Y=log(2D')>1/2, f=v_l(E). We have c,l<=w<=2n'<=u, f<=E<=u, log l<=u. Since 2E+1<r2(L')<=n', b<=u+3n'^2<=u+2u^2. The gens estimate follows from numGens at l=2 as in #620: floor(log_2 classNumber L')<=4n'Y; hence g=gens<=u+2uY+2<=6uY (uY>=1 and Y>=1/2). b+f<=3u^2, c+f<=4uY. Then J<=19u^3Y (u^2>=4), J log l<=19u^4Y<=u^9Y (u^5>=32). This is num_poly with its source constants. STors(C0) yields
    s log l<=2 exp(u^C0 Y)+u^9 Y.
Set a=u^max(C0,9)Y>=1. Then 2 exp(a)+a<=exp(4a) since exp(3a)>=1+3a and (3a-1) exp(a)>=a for a>=1. As u^2>=4, this proves num_three with exponent max(C0,9)+2.

To descend the estimate use x=2E n>=2 and Y0=log(2D)>1/2. The degree inequality gives d<=8x, n'<=4x^2 and 2E n'<=8x^2<=x^5. Also w<=8x^2, so
    log(2D')<=log 2+d log D+n' log w
              <=Y0+8x Y0+32x^4<=73x^4Y0<=x^11Y0.
Thus kBound(C,E,n',D')<=kBound(5C+11,E,n,D) for C>=0. Combining proves conditional SNum with exactly C=5(max(C0,9)+2)+11, as in source.

## 4. Actual torsion exponent conversion (conditional on geometric torsion theorem)

Source ExponentLe proves torsAll with C0=24 via KT.tors_le and orbnum. The geometric premises must be audited. For e,n,D>=1, 1<=N<=4e+6, 0<=m<=2e+1, let v=en>=1, Y=log(2D)>0.69. We have nN,N<=10v, m+1<=4v, log(2DnN)<=Y+10v-1<=16vY. Hence
    12(nN)^3 N log(2DnN) + 2 nN^2 <=1920300 v^5Y
(the second term is <=200v^2<=300v^5Y). Multiplying by m+1 and adding 2m<=12v^6Y yields <=7681212 v^6Y <=(2en)^24Y. This is exponent_le (in its needed natural parameter case) with source constant. When KT.tors_le and orbnum are established, their source log_le_exp inequality gives actual STors with C0=24. Conditional SNum gives C=141, SFinal gives CK=150. This is the source's witness recipe, not an optimization and not a claim that the geometric premises are established.

## 5. Open frontier

Active proof supplies 21 steps: SChain, SPrism, SPrismMul, SZc, SRel, STrans, SCoc, SThetaOf, SPhi, SEta, SStein, SClassOf, SUpperOf, SDetect, SCount, SFewOf, SSha, SLayer, STors, SNum, SFinal. We reconstructed conditional SNum/SFinal and numerical exponent_le, not the other steps' actual mathematical contracts. BOdd and the cyclotomic counting and detection constructions are substantive, and the shared geometric arithmetic homology bound still needs verification. The headline path has no unresolved KBridge obligation identified at this juncture. The prior parallel reconstruction is retained as such; no claim of an actual failure in the submitted proof. No original Lean replay, formal correspondence or certification. Next trace sChain through the actual finite evaluation construction and independently reconstruct the BOdd spine and shared torsion theorem. The prior publication infrastructure remains disconnected.

Boundary: RH-A26-D05_ACTIVE_LEMMAK_ROUTE_CORRECTED__CONDITIONAL_SNUM_SFINAL_RECONSTRUCTED__BODD_CYCLOTOMIC_COUNTING_GEOMETRIC_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
