# RH-A26 D05 — Whitney representing form

Scope: actual SWhit contract in SBridgeAlt and sWhit_of in ActHomApply, using the source's eta recursion, signed telescoping comparison, and finite-overlap growth. Conventional reconstruction, not original kernel replay. Standard smooth calculus (product and chain rules, d²=0, pullback naturality), finite-dimensional simplex integration/Fubini/FTC are explicit inputs. No arbitrary alternating-cocycle hypothesis. Prior SPU and SMom are used only for the later specialization; the theorem itself holds for its stated PU and nonnegative invariant Ht.

## Source identity

Restored original source paths relative to LiteratureResults/KTheoryStability/ReductionBoundsTorsion under Development/AutomorphicArithmetic/AutomorphicVarieties.
| Source | SHA256 |
|---|---|
| ActLPos.lean | 7e4840179da3ad19729771188ef5b90129d4821d36fb0fe637b939228c58f874 |
| SBridge.lean | b894ee21eaf1fa4fa41d4dd615fa8058a16720b659321eac46b3d4b069f50dbf |
| SBridgeAlt.lean | ab24a2e16c750c8bfbb20571b1995a9c91bf08d5e050fbdc3967aecbd7b0c481 |
| WhittakerSmoothForms/ActHomApply.lean | b723eae14c1ad488671828df0a0b26a518a11290179ecf7382c8c742367e7882 |
| WhittakerSmoothForms/AltSmulRightComp.lean | 0221a6740a8d9e1419d0970e24a7c272ab7be0c482d701b8275190213a6d3a6e |
| WhittakerSmoothForms/BfDep.lean | 32dac7ad59eb878a152a24d0242454c8edbc58d77833d33ccf1a94bf31219afb |
| WhittakerSmoothForms/EtaTop.lean | bf811add3d17fda67811a51b185c117aa5fc71af11cf435f31f88dde0a0d92db |
| WhittakerSmoothForms/EvEqLc.lean | 304b6be40edabb17b04a10182e3e70e7b8333fad9c8d1e8fc610003466ae26d6 |
| WhittakerSmoothForms/ExtDerivCongrNhds.lean | f8bc77945f6f3a0768fa8b4e38ba19dcf36bda30a2ca3bff5353622140f77986 |
| WhittakerSmoothForms/ExtDerivDelG.lean | db0bf32125a169121681783f2cbc672f7554e0f4e9063f5c70f0d58f1c04a995 |
| WhittakerSmoothForms/IntegrableOnSimp.lean | 868513c55cdabd7d836f9b93dd619918d3b327e2c217648633c06f1beccd3cfb |
| WhittakerSmoothForms/PSmooth.lean | c73ec29cdbeabc94f661046dd8fab50ac372a46a974814c0c2c071c408c12cb9 |
| WhittakerSmoothForms/PosDefOfSphere.lean | cce9528da5846fe02a75a1859e9258c9f2aaabe884e79110f82ea1bbbca7f112 |
| WhittakerSmoothForms/SimplexMem.lean | fe936afb61322c4d2c7c66b8c97c39de1fc0fd3a46b1d64c5d5dde587de51338 |
| WhittakerSmoothForms/SkipSuccAbove.lean | 6f4562639338dd28f484a91d8611bb6ca3653e5a6d6610247136d43da349604c |
| WhittakerSmoothForms/Smooth.lean | e3fa4b4b2aea4d0c2ffce101d6167aac11966c64c60de8f752fc5d3278999 |
| StokesSimplices/SStokesOf.lean | 2559f4bf528fc20c1d5c14da17f1ee615c7bce11f015f681e1139d6fa8665d05 |
| StokesSimplices/PInsertNth.lean | 8dc35b1b0ed5ce5f43cd721d4c05f86795f348180730ffd9eede91b3afb85acb |
| StokesSimplices/AlternatingMapSubBaseEqAlternatingSumRemoveNth.lean | 1f4de7ac0b23bf4b2bdf90dfe54b61d7cd06b9a9238206f3b114fdff15612183 |
| StokesSimplices/InsertNthSuccEq.lean | ca89c292a6e5df6074a7f7c773a11b47d56361be2794fcaac20b07bc3559a477 |
| StokesSimplices/SubSlice.lean | 45a288554e7f562b5d93f0345a204405195d7fdc7aabb1d083178ef17fd6a2b6 |
| StokesSimplices/SumInsertNth.lean | 31ede6c2c43ffaa849ba7343b72311a19055eb4ad4e69cd57f1d79b67e6f09ca |

## 1. Exact objects

Put p=k+1>=1, Gamma=GL_N(O_L), V=product Hermitian matrices, U=positive definite cone, A(gamma)=actL(emb gamma). More generally use the source Hyp: U open convex in a real normed space, A linear group action preserving U, phi smooth on U, psi_gamma(h)=phi(A(gamma^-1)h), locally finite nonzero sets and sum_gamma psi_gamma=1. U is open by uniform positive lower eigenvalue at a point and convex by positivity of quadratic forms (N=0 harmless). For actual arithmetic action A(x)h=(x^-1)*h x^-1, A(xy)=A(x)A(y). Base point o=identity. Source c is invariant homogeneous group p-cocycle on p+1 arguments, deletion coboundary delta c=0; c is not assumed alternating.

Finite-arity notation for source eta (the infinite tuple notation simply pads unused entries): eta_j has form degree j and p-j+1 group arguments for 0<=j<=p; K eta_j has p-j group arguments for j<p. eta_0(g)=constant 0-form c(g). Define
    (K beta)(g_0,...,g_(r-1))(h)=sum_gamma psi_gamma(h) beta(gamma,g_0,...,g_(r-1))(h),
    eta_(j+1)=d K eta_j.
These are precisely SimplexMem.Kf and eta. Source PDep: eta_j depends on first p-j+1 arguments, follows by induction because K prepends one argument. Only values on U matter for derivatives; local finiteness means a neighborhood in U has a single finite set of indices supporting all psi, not merely pointwise finite sums. Smoothness inductively from product, finite sum and exterior derivative. eta_j closed: constant for j=0, d²=0 for j>0.

## 2. Group contraction, top-form independence and equivariance

For any group cochain beta of degree r>=1 (possibly form-valued), delta K beta+K delta beta=beta, because the first face of (gamma,g_0,...,g_r) gives beta(g) with coefficient sum psi=1 and all other faces give negative delta K beta. This is the exact source PHom. Exterior derivative commutes with delta (finite alternating sum), and delta eta_0=0. By induction delta eta_(j+1)=d delta K eta_j=d eta_j=0. At j=p, eta_p has one group argument; delta eta_p(g0,g1)=eta_p(g1)-eta_p(g0)=0, hence is independent of the remaining group argument on U. This is EtaTop, not an assumption that averaging over the whole group is meaningful.

For a linear map B preserving U with psi_gamma(Bh)=psi_(a gamma)(h), and invariant c, induction gives B^*eta_j(g)=eta_j(a g) and B^*K eta_j(g)=K eta_j(a g): at j=0 use invariance of c; for K use reindexing gamma->a gamma of the locally finite sum, for d use naturality of pullback. This is source PEquiv, including the inverse a when B=A(x): psi_gamma(A(x)h)=psi_(x^-1 gamma)(h). Consequently eta_p invariant under arithmetic group, by independence of final argument. For actual scalar tuple s with common modulus, actL(s) is common multiplication by positive r=|s_w|^-2, so homogeneity of phi and commutation with A(gamma) give psi_gamma(rh)=psi_gamma(h). Apply with a=1 to get full pullback invariance under common modulus (not invariance under independent scalar moduli; SCen must do that). This reasoning includes the derivative action on all arguments, not just invariance of form coefficients.

## 3. Stokes for the exact source parameter simplex

For q-form alpha, I(alpha;y0,...,yq) integrates alpha at y0+sum t_i(y_i-y0), evaluated on edge vectors y_i-y0 for i=1,...,q, over t_i>=0,sum t_i<=1, ordinary coordinate Lebesgue measure (volume 1/q!, zero-dimensional integral evaluation). Convex U ensures simplex lies in U, compactness and continuity ensure integrability even if ambient V infinite-dimensional. No nondegeneracy required. Source SStokes claims delta I(alpha)=I(d alpha) for C¹ on open U. Reconstruct source slice mechanism: pull back along affine map P to coordinate simplex; differential alternation is sum_i (-1)^(i-1) partial_i of alpha evaluated on edge list omitting i. Integrate each by Fubini and FTC in t_i between 0 and 1-sum other t_j. Lower face gives I(alpha;delete y_i) with sign (-1)^i. Upper faces all parameterize face opposite y0. Changing between omitted barycentric coordinates is affine with absolute Jacobian 1 (one coordinate replaced by 1-minus-sum, others permuted); therefore integrate all upper terms in coordinates based at y1. Alternating multilinearity gives
    alpha(v2-v1,...,v_(q+1)-v1)
      =sum_(i=1..q+1) (-1)^(i-1) alpha(v1,...,omit v_i,...,v_(q+1))
where v_i=y_i-y0; any terms with repeated v1 vanish. Thus upper terms combine to I(alpha;delete y0) with sign +. This reproduces PInsertNth.asm's subAlt, subHyp, subSlice mechanism conventionally with elementary change of variables, FTC and Fubini as inputs. Works q=0, degenerate simplices and affine ambient spaces. No claim of line-by-line formal replay of slice lemmas.

## 4. Signed comparison of integrated form with original cocycle

Source Wf and Bf have different group arities and simplex vertex windows. For g=(g0,...,gp), write y_i=A(g_i)o. For 0<=j<=p define
    W_j(g)=I(eta_j(g0,...,g_(p-j)); y_(p-j),...,y_p).
For 0<=j<p and tuple g=(g0,...,g_(p-1)) define
    B_j(g)=I(K eta_j(g0,...,g_(p-j-1)); y_(p-j-1),...,y_(p-1)).
Then W_0=c, using zero-simplex integration, and W_p=I(eta_p; y0,...,yp), independent of final group argument of eta_p.

Verify exact EtaTop.chain. Set a=p-j-1>=0, beta=K eta_j of group degree a, Y=(y_a,...,y_p), Z=Y with first vertex deleted. In delta B_j(g), faces i=0,...,a delete from group prefix, so integrals all use Z; faces i=a+1,...,p leave beta on prefix unchanged and delete corresponding vertex from Y. Since delta beta=eta_j, the first block plus the missing i=a+1 group-face term equals W_j:
    sum_(i=0..a+1) (-1)^i I(beta(delete_i(g0,...,g_(a+1)));Z)=W_j.
The i=a+1 term here is (-1)^(a+1) I(beta(g0,...,g_a); Z). Subtract it to obtain first block; add the remaining faces with their actual signs (-1)^(a+l), l=1,...,j+1. The total is
    delta B_j = W_j + (-1)^a sum_(l=0..j+1)(-1)^l I(beta;delete_l Y)
              = W_j + (-1)^a W_(j+1).
This is source chain with a=k-j. All face identities use ordered tuples; no antisymmetrization of c.

Telescoping starts W0=delta 0+1 W0. If W0=delta b+s W_j, substitute W_j=delta B_j-(-1)^a W_(j+1), update b<-b+s B_j and s<- -s (-1)^a. After p steps s=(-1)^(p(p+1)/2), obtained by summing a from p-1 down to 0 plus p minus signs. Source tele only needs s=±1; this explicit value is a derived check, not a change to its construction. B_j invariant under simultaneous left multiplication by pullback equivariance plus affine transport of simplex. Thus b invariant. We obtain c=delta b+s I(eta_p; orbit simplex). Set actual omega=s eta_p(1). Smooth closed and invariant as above. Source Good requires continuous on U and delta intP omega=0, follows by Stokes from d omega=0. This equality is stronger than merely equality of some chosen periods, but weaker than equality on every individual simplex: delta b need not vanish there.

## 5. Exact cycle evaluation

Source chains are real finitely supported combinations of inhomogeneous tuples (g1,...,gp). Partial products P_i=g1...g_i, P_0=1 convert to ordered homogeneous vertices. The deletion face i=0 translates the suffix partial products by g1; invariance of b removes it. Internal face i=1,...,p-1 multiplies adjacent g_i g_(i+1); last face drops final g_p. These are precisely ActLPos.bd terms with signs (-1)^i, using associativity even in noncommutative groups. Consequently evaluation of delta b equals evaluation of b on bd z by linearity, zero for IsCyc. This reconstructs EvEqLc.pEv (sWhit_of has unused _hEv argument; direct pEv supplies equality). Thus ev(emb,intP omega,o,z)=ev(id,c,1,z) for every source cycle. No rationality, alternation, primitive or finite-generation assumptions added to SWhit.

## 6. Growth via uniform overlap, not uniform bound on all c

Let S=closure of {phi!=0} relative to U and source O={gamma: some h in S and A(gamma^-1)h in S}, finite. At fixed h, active closure labels R_h={gamma:A(gamma^-1)h in S} nonempty from sum psi=1. For gamma0 in R_h, gamma0^-1 gamma in O for all gamma in R_h (apply definition at A(gamma0^-1)h), injection gives #R_h<=#O. If gamma not in R_h, psi_gamma vanishes on neighborhood of h, so d psi_gamma=0 there. Important: using pointwise nonzero set alone is insufficient for derivatives in general. For tuple entirely in R_h, invariance of c under left gamma0^-1 bounds |c| by C0=max_{O^(p+1)} |c|; no global boundedness of c assumed. This is exactly source Nr, nr_mul, c_bdd.

Fix a continuous linear map T:V->V with all ||d psi_gamma(h) T||<=M, M>=0. Since eta_j closed, product rule gives eta_(j+1)=sum_gamma d psi_gamma wedge eta_j(prepend gamma), with usual unnormalized exterior product of 1-form and j-form. Each term on T has norm <=(j+1) M ||eta_j(prepend gamma) composed on all slots with T|| (alternating sum of j+1 terms). For active remaining arguments, induction from C0 yields C_(j+1)=#O (j+1) C_j and bound C_j M^j. Inactive labels contribute zero. Thus C_p=C0 (#O)^p p!, with sign unit modulus. Top independence lets choose remaining argument gamma0 active; no requirement that identity label be active. This is source pBound. Explicit wedge expression is a consequence of its recursion, not substitution of a different Whitney formula.

Take h=A(x)o, T=A(x). Chain rule d psi_gamma(h) T = d phi(A(emb gamma^-1 x)o) A(emb gamma^-1 x). Source PU.deriv gives <=C_phi Ht(emb gamma^-1 x)=C_phi Ht(x), using invariant nonnegative Ht, replace C_phi by max(C_phi,0). Therefore
    ||fr omega(x)|| <= C_p max(C_phi,0)^p Ht(x)^p.
Matches SWhit exponent p=k+1 and quantifiers, even Ht=0 and degree p>=1. PU.bdd not needed for this direct estimate, but source hypothesis retained. Actual SPU witness a=1 gives Ht=ht. Squaring requires moment A=2p, and SMom #627 supplies finite integral when N>=2p+2=2k+4, over special-linear domain; this is a specialization of bound and moment, not yet SCen/SMean/SInv or proof of their preservation. SWhit only claims common-modulus invariance; independent scalar moduli remain.

## 7. Boundary

Actual SWhit conventionally reconstructed with source eta/K, signed chain comparison and closure-overlap derivative estimate. Stokes source slicing reconstructed using standard elementary calculus; original Lean dependencies, correspondence and replay still open. Next SCen: genuine scalar averaging over unit-logarithm lattice, preserving exact cycles and growth; then SMean, SInv, SPrime, geometry/stability/counting/torsion. No RH/GRH certification.

Boundary RH-A26-D05_WHITNEY_FORM_CONVENTIONALLY_RECONSTRUCTED__SCALAR_AVERAGING_MEAN_INVARIANT_FORM_STABILITY_GEOMETRY_COUNTING_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
