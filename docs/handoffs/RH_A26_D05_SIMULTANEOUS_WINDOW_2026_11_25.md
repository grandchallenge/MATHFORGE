# RH-A26 D05 — simultaneous-window selection and its arithmetic interface

**Disposition:** independent conventional reconstruction of the genuine window1, window, exc, point, point2, partA, partB and thmBab_of arguments conditional on the exact ABound, FixedIn, TwoIn and LemmaK inputs. The final wrapper thmBab_of_lemmaK is traced to its actual outstanding arithmetic bridges; it is not claimed independently proved from FerreroWashington and duality by this dossier. Retain original constants, not optimize. No original Lean replay or certification.

## Source lock

Pinned original intake, paths relative to Development/AutomorphicArithmetic/AutomorphicVarieties:

| Module | SHA-256 |
|---|---|
| LayeredIsomorphisms/ThmBabOfLemmaK.lean | 8c18862cdb0e969e14e8e7bb0b429a60f3be96587f907194d6604276d692a3ca |
| LayeredIsomorphisms/ThmBabOf.lean | c263c5de2b26c9ade93525ea218afa71304f44a9916bc97b7e2573f5fd61e33b |
| LayeredIsomorphisms/Window1.lean | 9b80fe0dd466a58b0fae61b8d875bce2c40be17d56341c072a95462c41778d88 |
| LayeredIsomorphisms/Window.lean | 354e0ad1b87c54c46a40486a037d0a10b598ffc1b1d8e840e4f80560090a50be |
| LayeredIsomorphisms/SecondBound.lean | d0e3d59ca3196bc37ccf563afbe6829d6497e607c533b7984f27d5b8c91a29d6 |
| LayeredIsomorphisms/Exc.lean | 7bb13ceb4141dea9a35e93dbba8b71b06e44b172584e06c886b0c5a518146cfe |
| LayeredIsomorphisms/Near1.lean | ce808763ab7c876f1450be042cd5e57cb68961d7f7b12678c945eed5e2b52853 |
| LayeredIsomorphisms/ImportsAlt.lean | 64dfdb3fb277bfa34743573339b931a9e3696ff189570dfa2a940e095517cf47 |
| LayeredIsomorphisms/Point2.lean | 2e4ab589f6336247b0f18f3d0b1fcefac944ff582487421ab6608fbbbc5cf322 |
| LayeredIsomorphisms/PartA.lean | 73c1660109e43f18debb3b2fd6ccdd4f7022c79c7c8eb7467ca7385cb5e72eb1 |
| LayeredIsomorphisms/PartB.lean | 4b6133d7cc4a262e1a96e0b0e4bf48f7ce9fdc6d4e8dc4102d3ce039be4055ab |
| LayeredIsomorphisms/Final.lean | def019c1ab61e3f781ea87e3f7b6b2adaafeed0cfceb23eca48b8ccf5b6f3c8e |
| LayeredIsomorphisms/Klen.lean | a4a479699418e10e610e89596fd95af23f5f0bd17fcfb22ee29078240db918c1 |
| LayeredIsomorphisms/Kexp.lean | 9b5ee8c9c9b2fed70a419758cc416e75cc5ddd261481c718ae850226d72981ec |
| LayeredIsomorphisms/Layeremb.lean | ae52006a0bf5603dad099e010134fc9842a5aa8edf504f076579eef4d5d8a6c1 |
| LayeredIsomorphisms/Layerdisc.lean | 0f3c529f7cb9fd7115b668f9a15c493fbd192ccd8f19500c64f90cb89edfb797 |
| LayeredIsomorphisms/Layerex.lean | b679097141506f11ec43905c9a2bbade0429f93b237e3a96dec3289decabb9cb |
| LayeredIsomorphisms/Layeriso.lean | 3d3d880a0a4b8a2b00e9f4fc324a719da66d4b410242d1213e77ae87ebbb6b2a |
| LayeredIsomorphisms/Vvat.lean | 4707f2abfa05547502a807c190a25ae33857adf1d39cfb14d6bc699086b6e949 |
| LayeredIsomorphisms/Logs.lean | 3c9f09399c37e4fe416429a69cc586a0b51db7476fdf60a178b39627239b35b5 |
| LayeredIsomorphisms/Kmono.lean | c8014bf9ddbf29d96b451dc80106df51a4b03e0672793f1c39477eec3471267a |
| AdditiveValuationNorms/ABoundOfIsTower.lean | 4249346d3d787ad97c32ccbc0e95b11d72ec30923358bf98246f95f71dbc465d |
| AdditiveValuationNorms/ABoundOfDescends.lean | 30d198e1610fb4ce9152eec6d4baa3c1bfd5ac30c3e9fdc7fa33a4d4445b09e6 |
| QuadraticExtensions/IsAlgClosureRat.lean | eb9dcd0239166240b7856794bdd79c67ebda19d18f83f76dd93728725fa31420 |
| GeneratorCountTuples/LemmaK.lean | 65f1f885b171ff2aaf4478e96a1099e6d8adb3e863f7b35cfa8641028d4ad4be |
| PublishedTheorems/FerreroWashington.lean | 1f56d2c4c78367fc7165908ba2a5ae342a24a47e527bae0bc5609ad8e5a9f8c8 |

## 1. The exact arithmetic assumptions, not generic exceptional sets

Use the source conventions. Write l for a prime, R for a nonnegative integer, j0=Nat.log l R+3, and S(L,e)=shaInv L l e, an extended natural length. HasMuQ requires a primitive l-th root for odd l and a primitive fourth root for l=2. IsLayer l m L0 L1 means adjoining l-power roots of unity and relative degree l^m.

ABound(l,R,L0) is a conjunction:
(A) there exist an ultrametric normed extension of Q_l, at most R centers s_i, and c with a primitive l^c-th root in L0, such that if every norm |s_i-e|_l >= l^(-B), then S(L1,e)<=R'*(max(m,j0)+c+B), where R' is the number of centers, for all e>=1 and every layer of degree l^m;
(B) SecondBound: for every such layer and every layer L2 of degree l^j0 and actual data D on L2, S(L1,e)<=VLen(D,e)+R*max(m-j0,0).
Both are essential. The first handles nonexceptional orders, the second bounds exceptional orders by a fixed-degree layer. They are NOT implied by the window lemma.

LemmaK(CK) says, for totally complex L with HasMuQ and e>=1, the source H2(zlTw D (e+1)) is finite and log its cardinal <= kBound(CK,e,n,D0)=exp((2 e n)^CK log(2 D0)), where n is the absolute degree and D0 the absolute discriminant. The source VLen is the module length of this H2. We use this exact conditional input, not an asserted known bound for arbitrary cohomology. A finite Z_l-module of length v has cardinal l^v by a composition series (every simple factor F_l). Thus VLen is finite and <=2 kBound since log l>=log 2>1/2. This is klen; increasing CK preserves LemmaK since 2 e n>=2 and log(2D0)>=0. Set CK=max(CK_original,1) as in the source.

## 2. At most one exceptional integer per center (near1 and exc)

Fix Z>=1 and b=floor(log_l Z), so l^b<=Z<l^(b+1). If integers a,d in [1,Z] have |s-a| and |s-d| strictly less than l^(-b), the ultrametric inequality implies |a-d|_l<l^(-b), using the isometric scalar embedding of Q_l. If a!=d, its integral valuation is >=b+1, so l^(b+1) divides a-d. But 0<|a-d|<Z<l^(b+1), contradiction. Strict inequality is required: at Z=4,l=3,b=1, center 1, integers 1 and 4 have distance at most 1/3; both qualify under a non-strict threshold. For Z=0 the interval is empty and no logarithm argument is needed.

For each actual ABound center take its set of qualifying integers in [1,Z]. Their union Exc has cardinal <=R'<=R. Every e in [1,Z] outside Exc satisfies all the lower distance bounds with B=b. ABound(A) gives FirstBound with R in place of R'. The same c works for every Z; Exc may depend on Z and the base field. This is the exact exc statement. No enumeration of algebraic centers is necessary. The arithmetic existence and uniform number of those centers are still inputs.

## 3. The actual interval construction (window1, window)

Given U>0, B>=1 and a finite set T of at most R real numbers, find y such that
    U/(2^(R+2) B^R) <= y, 2y<=U,
    for all a in T and u in [y,2y], a<=u implies B*a<=u.
Proof by induction on R. For R=0 choose y=U/2. For R>0, if there exists a0 in T with U/(2B)<a0<=U, replace U by U/(2B) and remove a0. Apply induction with R-1. The discarded a0 is above every new u, so its implication is vacuous; all other implications come from induction. Multiplying denominators gives precisely the source lower bound. If no such a0 exists, take y=U/2. An a<=u<=U must then satisfy a<=U/(2B), hence B*a<=U/2<=u. This completes the proof even for B=1, nonpositive thresholds and repeated threshold images. The lower bound is exactly the source's, not an optimized variant.

For X>1, 0<eta<=Ct, set U=log X, B=Ct/eta, T={log(k)/Ct : k in Exc}, using the real logarithm for positive k. Omit k=0 from the set (its Good implication is automatically true). The cardinal remains <=R. Set Y=exp(y). Then X^(1/J)<=Y and Y^2<=X, with J=2^(R+2)*(Ct/eta)^R. For every x in [Y,Y^2], an exceptional positive integer k<=x^Ct implies log(k)/Ct<=log x. By the proved implication, log(k)/eta<=log x, i.e. k<=x^eta. This proves the actual Good(eta,Ct,Exc,x) for the WHOLE closed interval, not just integer x or sampled endpoints.

Example in base-2 logarithmic coordinates: U=128, B=2, Ct=2, eta=1, exceptional integers {2^80,2^20,4} give thresholds {40,10,1}. With a0=40 the upper bound becomes 32; with a0=10 it becomes 8; then choose y=4. The window is [2^4,2^8] in x, inside [X^(1/J),X] for R=3 and J=256. Throughout, 2^80 and 2^20 exceed x^2, and 4<=x. This is illustrative arithmetic, not a calculated exceptional set of a number field.

## 4. Pointwise estimates on the selected window

Fix eta=eps/(2 CK), eps>0, CK>0. Suppose n(L2)<=n0, log(2|disc L2|)<=c0*x^(eps/4), x>=1, c0>=0. For e in [1,Z] with e<=x^Ct, split on Exc. Outside Exc FirstBound gives finite length <=R*(max(m,j0)+c+Nat.log l Z). Inside Exc, Good gives e<=x^eta. L2 contains the required roots via L0, and is totally complex since those roots have order >2. LemmaK and klen give finite VLen <=2 exp((2 e n)^CK log(2|disc L2|)). Since (2 e n)^CK <=(2 n0)^CK x^(eps/2), this is at most 2 exp((2 n0)^CK c0 x^(3eps/4)). Apply SecondBound to the actual L1,L2,D. In both cases we have finite S(L1,e) and
    S(L1,e)<= R*(m+j0+c+Nat.log l Z) + 2 exp((2 n0)^CK c0 x^(3eps/4)).
The positivity and extended-length finiteness justify conversion to real lengths. This is point, retaining the exact exponents.

Take Z=floor(X^Ct), 1<=x<=X and X^(1/J)<=x, Ct>=0, J>0. Then Nat.log l Z <= Ct log X/log l <=2 Ct J log x (if Z=0 the natural log is zero). If m<=a*(1+log x), a>=0, and c<=c1, define
    C=R*(a+j0+c1+2 Ct J)+1+(2 n0)^CK c0.
All its summands are nonnegative. The last display implies S+1<=ptBound(C,eps,x)=C*(1+log x)+2 exp(C*x^(3eps/4)), exactly point2. All constants are independent of x, e, X and the varying L1 when the indicated input bounds are uniform. Also if 2^h<=x^A1, x>=1, then h+2<=(2|A1|+2)*(1+log x), by log 2>1/2, which is the other log estimate used by partA.

For any fixed real C,Ct and eps>0, x^Ct ptBound(C,eps,x)<=exp(x^(4eps/5)) eventually: for x>=1 the left side is bounded above by 3 exp((|Ct|+|C|)log x+|C|+|C|x^(3eps/4)). Its logarithmic upper exponent including log 3 is o(x^(4eps/5)), since 4/5>3/4 and eps>0. This proves final without changing the source target. With t<=x^Ct, at most t-1 nonnegative terms bounded by ptBound, and all finite, their sum is <=exp(x^(4eps/5)). The source vvat uses shaLen_eq_shaInv; its conventional justification is the equivariant inflation and local-place transport already reconstructed in #594/#609: extending a field isomorphism to algebraic closures identifies Galois groups, cyclotomic actions and inertia/decomposition subgroups, hence the actual kernels. No original Lean implementation replay.

## 5. Fixed-degree reference layers, discriminant and transport

Classical finite/infinite Galois theory is used explicitly. Over a number field with HasMuQ the image on l-power roots is a closed infinite subgroup of 1+l Z_l for l odd or 1+4 Z_2 at 2. Those groups are isomorphic to Z_l by the l-adic logarithm. The image is infinite since cyclotomic degrees over Q are unbounded while the base degree is finite. A closed infinite subgroup of Z_l is l^s Z_l: choose a nonzero element of minimal valuation, its integer multiples are dense in that subgroup. It has unique subgroups of each index l^j; the nested cyclotomic finite stages exhaust the tower and realize every such subgroup (eventually reductions of 1+l^s Z_l give each index). This gives layerex under HasMuQ. More generally the source layeriso for any two isomorphic bases follows by identifying the bases in a common algebraic closure, where adjoining primitive l^k roots gives nested fields; equal finite relative degrees force equality. IsAbField A identifies a unique fixed subfield in Q(mu_m) after embedding into a common algebraic closure, by its actual fixing criterion depending only on cyclotomic action mod m. This proves the abiso needed in partB; HasMu follows because its fixing group acts trivially on mu_l.

If L1=L0(mu_(l^k)) and L0 embeds in Q(mu_N), then L1 embeds in Q(mu_(N*l^k)). Since L1 contains the indicated primitive root, phi(l^k)<=degree(L1), hence l^k<=2 degree(L1), including k=0. This proves layeremb. The discriminant estimate log|disc L|<=degree(L) log N follows either from the cyclotomic discriminant formula and the discriminant tower formula or conductor-discriminant (classical inputs as in #610); all degrees positive and |disc|>=1. If degree(L0)<=n1, L0 embeds at N0 P, and L2 has degree l^j0 relative to L0, choose n0=(n1+1) l^j0 and c0=log 2+n0 log(2 n0 N0)+n0. For w>=1 and log P<=w, the preceding bounds give log(2|disc L2|)<=log 2+n0(log(2 n0 N0)+log P)<=c0 w. This is exactly layerdisc.

PartA uses the actual TwoBase hypothesis: HasMuQ(2,L0), degree <=8 M.deg, embedding at 4 M.m q d, and for every composite field E at h>=2 a layer L1 of relative degree 2^m with m<=h+2 and S(E,k)<=1+S(L1,k) for every k>=1. It also assumes ABound(2,R,L0). The root c is bounded by 16 M.deg since 2^c<=2 degree(L0) and c<2^c. Apply layerdisc with n1=8 M.deg, N0=4 M.m, j=j0, P=q d, w=x^(eps/4). Its log P assumption follows from log(qd)<=X^(eps/(4J)) and x>=X^(1/J). Take a=2|A1|+2 for m. Sections 2–4 now give the source ptBound on S(E,k), including the extra +1 from TwoBase, uniformly in q,d and E. Summing yields BaAt on every Good point of the prescribed range. The uniform threshold depends on the fixed parameters, not on q,d,X, e(.), t(.) or E. This proves partA conditional on TwoBase and ABound; their construction is not assumed proved.

PartB fixes l odd, A, a representative L0 with IsAbField A and ABound. HasMu A gives HasMuQ. Fix the degree-l^j0 reference layer L2; its degree and discriminant supply n0 and c0=log(2|disc|). Choose c1=c and a=j0, since the desired L1 has relative degree l^j0. For any other base representative L0' and its layer of this degree, abiso and layeriso give an isomorphic reference field; shaInv transport gives identical length. Thus the chosen c, n0, c0 and the exceptional set from L0 suffice for ALL representatives. Sections 2–4 give VVat at every Good point, with uniform threshold, and prove partB conditional on ABound.

## 6. Simultaneity and quantifiers: exact thmBab_of

Assume exists CK LemmaK CK, FixedIn, TwoIn, with the exact definitions in SecondBound. Choose CK>=1 as above. For each M choose R0(M) from TwoIn, BEFORE q,d vary. For l,A choose Rl(l,A) from an existing ABound representative of IsAbField A (take 0 if no such witness). FixedIn supplies that witness whenever l,A have the required hypotheses and a representative exists. If there is no representative the corresponding universal BbAt statement is vacuous. These choices depend only on M or (l,A), not on Ct, eps, A1, X,q,d, e(.),t(.). This constructs the actual BConst K.

For fixed Ct>=1, eps in (0,1/52), A1, M, finite auxiliary set B' with OddPrimesWithRootsOfUnity and field data L(l), put R=R0(M)+sum_(l in B') Rl(l,L(l)), eta=eps/(2 CK), J=2^(R+2)*(2 CK Ct/eps)^R. We have 0<eta<=Ct. PartA supplies a threshold x0A, and each partB a threshold x0(l). Choose x1>=1 and above all these finitely many thresholds, then X0=max(2,x1^J). This choice is before admitted functions e,t and before X,q,d. For X>=X0, every x>=X^(1/J) is above every threshold.

Given admitted functions, X and a PrimePair with log(qd)<=X^(eps/(4J)), choose the actual TwoBase/ABound representative from TwoIn and its ExcA of size <=R0. Each partB supplies Exc_l of size <=Rl, independent of x and of the other field representatives. Take their union with ExcA, of size <=R. Section 3 produces the same Y for the entire union, X^(1/J)<=Y, Y^2<=X. Good for the union implies Good for each subset (not the reverse). Every x in [Y,Y^2] therefore satisfies ALL BaAt and BbAt estimates simultaneously. This proves ThmBab K Ct, uniformly for all Ct>=1, with the exact source J and threshold ordering. This is the substantive selection argument in thmBab_of, not an existence claim based on independently chosen intervals.

## 7. What the original wrapper still requires

Actual ThmBabOfLemmaK.lean has the following dependency chain:
- aBound_of_isTower(PoitouTateDuality, LocalFinitenessK, LocalTateDualityK) gives TowerBound. It calls genLevel, descends, aBound_of_descends. The last uses actual twisted cokernel length, xUnip, exists_centres_norm, twLen_le_growth and shaLeV. These are the mathematical sources of ABound(A) and (B). Their independent reconstruction for the genuine arithmetic tower has NOT been supplied here.
- fixedIn(FerreroWashington,TowerBound) uses towerFixed and a uniform class group mod-l rank bound for a fixed abelian base; the source Published.FerreroWashington states that exact finite-layer rank bound. The correspondence with the classical theorem and the passage to the source infinite module require audit.
- twoIn(FerreroWashington,TowerBound) uses towerTwo and twoBase. In towerTwo the uniform R=4*(g+6*M.deg) comes from baseRk, involving charStep, orbTwo, ineTwo and quadStep for the two varying auxiliary primes. This uniformity is NOT a direct consequence of applying FerreroWashington separately to each varying base. twoBase also uses compIndex and shaTwo to obtain the +1 transfer. Those exact arithmetic steps require independent reconstruction.
- LemmaK is the genuine quantified H2 cardinal bound in GeneratorCountTuples/LemmaK.lean, not established by this selection argument.

Hence thmBab_of_lemmaK follows from these exact source dependencies if established; no claim of independent verification of all of them or of the full VWin theorem. Even after ThmBab, the other-sign height/count argument is separate. Next independently reconstruct ABound from actual tower descends and twisted cokernel estimates, then verify fixed/two-base uniform rank and +1 transfer, and LemmaK. Exact foundational correspondence and original Lean replay remain open. The proof's mission is verification and explanation, not constant optimization.

Boundary: RH-A26-D05_CONDITIONAL_THMBAB_WINDOW_SELECTION_RECONSTRUCTED__ABOUND_TOWER_DESCENT_UNIFORM_TWOBASE_RANK_LEMMAK_OTHER_SIGN_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
