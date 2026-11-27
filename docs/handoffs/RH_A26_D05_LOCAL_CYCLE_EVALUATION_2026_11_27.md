# RH-A26 D05 — compact-local cycle evaluation (SLoc)

Disposition: independent conventional reconstruction of actual AvgS, SimpBd, Unfold, Discr, OverlapG and sLoc_of_parts. All use the exact source cone, inverse congruence action, affine simplex integration, probability averaging and moving frame. Standard finite-dimensional integration, positive definite spectral theorem, Haar measure, Minkowski lattice and previously reconstructed SEv bar-prism facts explicit. No original Lean replay, full SSurj, BOdd or RH/GRH certification.

## Source lock

Restored publisher archive SHA256 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc. Paths relative to Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion. SHA256 from original restored bytes:
| File | SHA256 |
|---|---|
| ActLPos.lean | 7e4840179da3ad19729771188ef5b90129d4821d36fb0fe637b939228c58f874 |
| SBridgeAlt.lean | ab24a2e16c750c8bfbb20571b1995a9c91bf08d5e050fbdc3967aecbd7b0c481 |
| CompactLocalSets/Assemble.lean | e02c282e5b475403f3433d8a9ba1278d03d5641a69700ba5eaa368a88734af62 |
| CompactLocalSets/DiscrHolds.lean | 41cd271e16356308b35d75976f8f190087853292e0e1efcb3b553d1fbdc719c0 |
| CompactLocalSets/MargInt.lean | 43e2c1a593cac0e471f60fd80de479a65602db4fb3ac51e97701afee063b4e1b |
| CompactLocalSets/MeasurableSetSimplex.lean | 05f285ab5af1be313d293c6b6a02c252b66e9b7a29a28a6748b3abe00cc4ff61 |
| CompactLocalSets/Overlap.lean | 7d82e0a6821e571530ca8bfc185be5660dfd750176b2fa06ac3c451b24bd8b32 |
| CompactLocalSets/OverlapG.lean | 54f7e64892a406511ae55494df549c84b60c9bbfcd832f2248a1ddbfbf84ea16 |
| CompactLocalSets/SLocOf.lean | d1155c06b156c41d83f53edcd6d652e211a3917dcf544fd3ca6eb652daf0107b |
| CompactLocalSets/SimpBd.lean | d736fa8a5cdfd91385753da5733568be8cd1182533c6a205b3d4cd15035e8d98 |
| CompactLocalSets/SimpBdM.lean | 0df9844157b07e4481b241f981b27530aad9cf914d384ea64b51ac3c49d34ca2 |
| CompactLocalSets/Unfold.lean | f75679c25fdad55b4ec327977d11686826e82f9ae68e9ab4fa5b5265ca24db43 |
| CompactLocalSets/UnfoldM.lean | e0bf9e8eeb3cbf5b66d8566df7078777456637ca51ac8ef4cf9dc1e5eeb6b24e |

## 1. Exact contract, not a trace inequality for arbitrary forms

Let L be a number field (not required totally complex for SLoc), N>=1, q=k+1, V=HS(L,N) the real vector space of tuples of Hermitian complex matrices indexed by infinite places, P=Pos the positive definite cone, o=tuple of identity matrices. Gp=product of GL_N(C), Sp=product of SL_N(C). Write A_g p=(g^-1)^* p g^-1 componentwise. This is a left action by real linear isomorphisms: A_g A_h=A_(gh). The moving frame fr(omega,g)=omega(A_g o) composed on each argument with A_g. FInv(omega,g) means omega(A_g p) composed with A_g on every argument equals omega(p) on P. Good means continuous on P and dC(intP omega)=0, where intP is the actual integral over the affine standard simplex, not an a priori de Rham cohomology class. Smoothness and exterior closedness are not extra hypotheses. Dom supplies a finite-volume fundamental domain D for latS=embedded SL_N(O_L) in Sp, a Haar measure nu also right invariant. SLoc assumes Good, FInv under embedded GL_N(O_L) and all tuples of nonzero complex scalars, and integrability of squared moving-frame norm on D. For each real bar q-cycle z there must be one real constant C, chosen before omega, with
    |ev(emb,intP omega,o,z)| <= C sqrt(integral_D ||fr(omega,x)||^2 dnu).
No claim for arbitrary L2 forms or evaluation on arbitrary noncycles. Existence of Dom is an input here, not a result of SLoc.

## 2. Probability averaging preserves the evaluation (AvgS)

Use the precise abstract contract in OverlapG and MargInt: a group G acts through rho:G->H on Y, an invariant homogeneous q-cocycle F on Y, probability law P0 on X, map e:X->Y, and basepoint y0. The hypotheses guarantee integrability of every mixed tuple using either e(x_j) or y0 after independent prescribed H translations. Set Y'=H x {0,1} with H acting by left multiplication on the first coordinate. Define
    F'((h_j,b_j)_{j=0}^q)=E F((h_j . y_j)_{j=0}^q),
where y_j=e(X_j) if b_j=1 and y0 otherwise, with independent X_j~P0. The expectation is finite by the mixed-integrability premise. Invariance of F gives invariance of F'. To check dC F'=0 at any (q+2)-tuple, take independent variables at ALL q+2 slots. Each deleted-face marginal is exactly the required product law on q+1 slots; the deleted coordinate integrates to 1 because P0 is probability. Every face integrable, so sum and integral commute and the resulting alternating sum is E(dC F)=0. This is precisely marg/marg_int and avgS_of, with mixed flags, not just a common random translation of all vertices.

The SEv prism identity already reconstructed in #622/#624 states that evaluations of any invariant closed homogeneous cocycle on a cycle are independent of basepoint. For completeness, equivariant maps from the homogeneous bar vertex set G to Y' defined by g->rho(g).(1,0) and g->rho(g).(1,1) induce chain maps on ordered tuples. The signed prism sum inserting the switch from the first to second list has boundary equal to their difference minus the prism on the boundary (the interior terms cancel). Thus on cycles a closed cochain has equal evaluations. Apply to F', identifying the all-zero flags with the original evaluation and all-one flags with the product average. This proves the exact source identity. It does NOT assert invariance under arbitrary independent perturbations of one simplex; cancellation occurs on the full cycle.

## 3. Simplex integration acquires an ambient density (SimpBd)

In the actual general finite-dimensional real normed V of dimension d, let A_j (j=0..q) be invertible real linear maps, B compact, mu additive Haar. If mu(B)=0 the normalized measure nm=(mu(B))^-1 mu|B is zero (extended nonnegative convention 0*infinity=0), and its q+1-fold product is zero; q+1>=1, so all integrals with this measure are zero, and C=0 works, including mixed tuples. Otherwise 0<mu(B)<infinity, nm is probability. All tuples in B^(q+1) are supported a.e. there. Let Delta={t_i>=0,sum t_i<=1}, tau_0=1-sum t_i, tau_j=t_j for j>=1. Set K=Kset(A,B), the compact image of Delta x B^(q+1) under p=sum tau_j A_j y_j. This is the same KS/Kset in source, not necessarily the entire convex hull of union A_j B (only one point from each indexed set). On the cone case K lies in P by positive definite convexity and action preservation.

Given continuous omega on K, its evaluated simplex integrand at (t,y) is continuous on the compact product, with directions d_j=A_j y_j-A_0 y_0. It is bounded and measurable there; by dominated convergence the integral is continuous in y on B^(q+1). Replacing any of its variables by a fixed y0 in B preserves this fact, proving all mixed-integrability claims. Measurability off the compact sets is not needed: extend the restricted functions by zero for integrals on the supports. Define G(p)=1_K(p)||omega(p)|| (measurable). Choose r>=0 bounding ||y|| on B, a=sum_j ||A_j||, E=(2 a r)^q. By alternating operator norm bound, absolute integrand <=E G(p). q=0 uses the empty product. This E depends on geometry only, not omega.

For fixed t, at least one tau_i>=1/(q+1). Holding other vertices fixed, p=T y_i+b with T=tau_i A_i invertible and
    |det T|^-1=tau_i^-d |det A_i|^-1 <=(q+1)^d |det A_i|^-1.
By additive Haar change of variables, integration in y_i with nm is at most mu(B)^-1 |det T|^-1 integral_V G dmu. Integrating the other independent variables contributes no factor because their laws have mass 1. Thus the full expectation of G(p) is bounded by mu(B)^-1 S integral_K ||omega||, with S=sum_i (q+1)^d |det A_i|^-1 (source uses the sum rather than a max). This uniform bound at every t, including boundary, does not require all tau_i positive or an integrable inverse of the smallest tau. Tonelli on nonnegative functions followed by integration over Delta proves exactly SimpBd with
    C1=E * mu(B)^-1 * S * volume(Delta).
This is the source coord_step/exists_big/main. No dimension-dependent trace theorem or unverified regularity of omega. All constants finite. Illustrative q=1,V=R, A0=A1=id,B=[0,1]: at midpoint the density of the mean of two uniform points is triangular of height 2, not a point mass. Fixed endpoints alone would not give an ambient density. Finite tests below check this example and the general determinant and weight mechanism, not the analytic result itself.

## 4. Compact unfolding from cone to group (Unfold)

Need bound integral_K ||omega|| by C2 integral_K' ||fr omega|| for compact K subset P, using actual scalar invariance. Cannot identify the cone with Sp (determinant directions and unitary stabilizers); source instead thickens by a compact identity neighborhood W in Sp, defined by all entry distances to identity <=1/2. It is compact since closed and bounded in the finite-dimensional matrix space with det=1 closed; contains open identity neighborhood, hence 0<nu(W)<infinity. Put K1={A_(s^-1)p:s in W,p in K}. Continuous image of W x K, compact in P. For every s in W, K subset A_s K1. Choose D0=max(1,sup_W |det_R A_s|), m0=1/D0>0. Change of variables yields
    m0 integral_K ||omega(p)|| dmu <= integral_K1 ||omega(A_s p)|| dmu(p).
Integrate over W, interchange via Tonelli (continuity on W x K1 gives measurability there).

For any p in K1 choose g=c t with c tuple of scalar matrices and t in Sp such that A_g o=p. At each place take g=p^-1/2 from positive definite spectral theorem, then normalize determinant by c=(det g)^(1/N)>0. The source dec_K/dec_bdd gives uniform entry bounds R for g and t on K1. To verify existence directly, on compact K1 positive definite eigenvalues have common positive lower bound and finite upper bound (min/max Rayleigh quotient on product with unit sphere, finite places). Hence g, c and c^-1, t=c^-1 g have bounded entries. This continuous positive square root construction is a conventional proof of the same dec_K contract using the spectral theorem, without claiming equality with the source's choice of roots or optimizing its constants. Alternatively its exact g g*=p^-1 bounds g entries and determinant p bounds c^-1 as in UnfoldM. No choice needs to be measurable in p: inner estimate below is pointwise for each p, while the original double-integrand is jointly measurable.

For s in W the entries of s g and s t are <=R'=N*(3/2)*R by matrix multiplication. Put K'={x in Sp: all entries <=R'}, compact. Then W t subset K'. The actual frame formula gives omega(A_X o)=fr(omega,X) composed with A_(X^-1) on each argument. Since scalar matrices commute and FInv for scalars implies fr(omega,c x)=fr(omega,x), for X=s g=c s t the frame is exactly fr(omega,s t). The operator norm on V with the source entrywise sup norm satisfies ||A_(X^-1)||<=N^2 (R')^2 by summing entries of X* h X twice. Hence
    ||omega(A_s p)|| <= B0 ||fr(omega,s t)||, B0=(N^2 (R')^2)^q.
Right Haar invariance, explicitly part of Dom, implies integral_W ||fr(omega,s t)|| dnu(s)=integral_Wt ||fr(omega,x)|| dnu(x)<=integral_K' ||fr omega||. Left invariance alone would not justify this particular equality. Combine the double integral estimates:
    integral_K ||omega|| dmu <= C2 integral_K' ||fr omega|| dnu,
    C2=B0 mu(K1)/(m0 nu(W)).
All factors finite, denominator strictly positive. This is the source Unfold constant construction, including its Jacobian direction and dependence on geometry. Empty K causes no problem (integrals zero). We retain source norm bound and do not attempt a quantitative optimization of existential R.

## 5. Discrete lattice overlap (Discr, OverlapG)

An element of latS in a fixed compact set has all matrix entries bounded at the chosen embeddings. For real places the one embedding is real; for complex pairs the other embedding has the same modulus. The Minkowski embedding of O_L as a lattice (with real slots and complex pairs) has only finitely many points in a bounded set. Thus finitely many integral matrices satisfy the bound, and hence finitely many embedded determinant-one matrices. This establishes Discr also for fields with real places. Countability follows from O_L finite free Z-module; image subgroup countable. The compact overlap count does not assume a compact fundamental domain.

Let K' compact, Gamma=latS, D the given fundamental domain. Set M=|Gamma intersect (K' (K')^-1)| finite by compactness of the product and Discr. For fixed x, if some gamma0 x belongs to K', every gamma with gamma x in K' satisfies gamma gamma0^-1 in that finite set, and the map gamma->gamma gamma0^-1 is injective. If no such gamma, count zero. Thus multiplicity <=M uniformly in x. For nonnegative measurable Gamma-invariant f, use the a.e. partition by left translates of D and left invariance of nu:
    integral_K' f = integral_D f(x) sum_gamma 1_K'(gamma x) dnu(x) <= M integral_D f.
Tonelli is legitimate for nonnegative terms. This proves OverlapG, including nonnormal lattices and arbitrary measurable fundamental domains with the stated property. For the frame norm f(x)=||fr(omega,x)||, continuity follows from continuity of omega on P and group action; arithmetic FInv and A_(gamma x)=A_gamma A_x imply left Gamma-invariance exactly. No inference of invariance from norm alone.

## 6. Assemble the actual SLoc

Take B a small positive-radius closed ball about o contained in P (P open by positive-definite eigenvalue criterion). Finite-dimensional Haar measure gives 0<mu(B)<infinity. Use e(y)=y as point of P on B and o elsewhere; outside B is a null set. For fixed bar generator g=(g1,...,gq), let h_j=emb(g1...gj) with h_0=1. Then A_j=A_(h_j). Its Kset lies in P, so section 3 gives the mixed-integrability hypotheses of AvgS for F=intP omega, including arbitrary H tuple translations. F invariant by change of affine coordinates: A_h is linear and form pullback equality yields equality of simplex integrands. F closed by exact Good premise. For this fixed g, sections 3-5 plus Holder with exponent 2 on D give
    E |intP omega((h_j.e(Y_j))_j)| <= C1 C2 M sqrt(nu(D)) sqrt(integral_D ||fr omega||^2).
The actual hypothesis makes the last integral finite; all intermediate nonnegative integrals bounded by it are finite, permitting their real conversion. Constants depend on L,N,q,D,B and g, chosen before omega. The common frame is precisely the source frame, not a different Riemannian norm. The average identity of section 2 for the actual cycle z now gives its evaluation as a finite sum of signed coefficients z_g times these simplex averages. Triangle inequality yields SLoc with C_z=sum_(g in supp z) |z_g| C1_g C2_g M_g sqrt(nu(D)), exactly the structure of sLoc_of_parts. Zero cycle has zero constant. This proof uses no bound uniform in z, and no positivity of a signed cycle. There is no pointwise norm estimate from L2.

## 7. Consequence and boundary

Together with #623, each iterate satisfying Lz and the required Good/arithmetic/scalar conditions has an upper bound on its cycle evaluations by C_z times its moving-frame norm; to use the coordinatewise SGap on forms, a fixed finite frame basis and norm equivalence give the form-norm bound as in LemBound (no changing norm each iteration). With #624, the finite evaluation vector must vanish if the hypotheses of the actual SHecke (finite generation, stability, degree and dimension threshold) hold. This closes the direct compact-local analytic bridge, not the existence of the smooth representing form or invariant mean. SSurj still requires SPrime, SHt, SPU, SMom, SWhit, SCen, SMean, SInv and their precise assembly, plus finite-generation geometry/stability, invariant-form source correspondence and later counting/torsion. No original Lean replay or RH/GRH certification. Classical integration, positive definite spectral theorem and Minkowski embedding inputs explicit, exact source contracts retained.

Boundary: RH-A26-D05_SLOC_COMPACT_LOCAL_EVALUATION_RECONSTRUCTED__HEIGHT_MOMENTS_WHITNEY_SCALAR_MEAN_FORM_STABILITY_GEOMETRY_COUNTING_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
