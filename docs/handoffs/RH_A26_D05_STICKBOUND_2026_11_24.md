# RH-A26 D05 — independent conventional StickBound reconstruction

Disposition: reconstruct killPow, lenPow, gen and stickBound for the actual source modules under explicit classical number-theoretic foundations. In particular the classical integral Stickelberger annihilation theorem, Hilbert class field reciprocity, conductor-discriminant formula, Minkowski theorem and Dirichlet S-unit theorem are imported, not silently asserted kernel-verified. The source's Procyc hypothesis remains. No original Lean replay or certification.

## Source lock

Pinned original intake, paths relative to Development/AutomorphicArithmetic/AutomorphicVarieties:
- OddResidueBounds/KillPow.lean 95f8dc382b4fa6fc184d09af764e1779aac60b1f0f2ca6ad3d9c54d2c5db3d2b
- OddResidueBounds/LenPow.lean f7b67ba5ed1217bb095966082e22818c972b8b578d014f1d55fd22b31e634972
- OddResidueBounds/Imports.lean 355f227b82d8ac114f0bb67950900d31709c2b2908ca14f243ee70b420a23427
- OddResidueBounds/ThmBcOfPsiBound.lean 90808ac87265e481e18121781c242726f0a8ae0bfd9832cf3b4d31c079c49d24
- OddResidueBounds/ZKill.lean d5495503aac3d7c3e2c60281aca410d8d12af9b63699a2000727476cde8d5eaf
- OddResidueBounds/ResKill.lean 55fc9c4d319c3ec98d218df151bb871f3605f30cb09e1fa41f9a3bc0a9fd422e
- OddResidueBounds/TotKill.lean 569f670bad147dab530bb8418957cd40ff250934398a4574ae8fcc1cf74ff464
- OddResidueBounds/HomKill.lean ee984209e6870579c3d34a87989e616aa6ec435318ea71b132ce8fcdcdbf4b9f
- OddResidueBounds/ClKill.lean 5c4397bfd3f24e98988cff03cc82e11c87a67e5b4d1235a613c44a7f5c9aaca8
- OddResidueBounds/NearLevel.lean bad0b2884bd5235d76fef77c0cd27d62c142b9ef1964de445e8bcc56a15b9f07
- OddResidueBounds/YLevel.lean 3f9276b2c0d0a89e2b3b371772f9cbc3f5f8e02dd5fead8c1a3b6dce41e379
- OddResidueBounds/YNear.lean 39e14bcfab195ae32be9215c149930da22b006090182d4c5c61505055112fdab
- OddResidueBounds/AdjKill.lean 807fbb8a7eebb823d0a15e87acb3edcef3a3c0cd5ba9204a0501635ce2a4968d
- OddResidueBounds/DetVal.lean 28d3c83a351865b4a0926df739ac735594fdf506680333678c610e9924f32c3c
- OddResidueBounds/BdxLog.lean 1fce923f902dffe8d815b9b9011eee14685f0910780b246fdb37cd9d37109f10
- OddResidueBounds/UnrInj.lean 2ed357118ae8211a5167723b0c3341ca7fd8311e95de28ba6ff3fd53830ee55a
- OddResidueBounds/UnrSel.lean 1d5ae2924a797b140654231927d0882332733de5fdc57841e22a38665e047fcb
- OddResidueBounds/SelCard.lean 046055bc7b1550fba42ff1c5bea013c55f2561ad8c650967a55e245bfdb5005c
- OddResidueBounds/FnOne.lean 414cf16647b991be50743acd47a0eedac25889fdbb4ce52cafebbf4444ef577e
- OddResidueBounds/LogH.lean ed772a79b8c1dd1b792b6232c44b350bac34bbdc1b2736dda2acb88e680bd6cc
- OddResidueBounds/LogDisc.lean 616fb5faac39b0e4af4df027af5546ed8826fab13f0b80d89ae26813673ad683
- OddResidueBounds/TorsRep.lean e3242263cfd32adc72e15ecb04a6b18f08cab00648a0dd553076d2af5657ffe8
- OddResidueBounds/CobOne.lean b93fbbe7f0668c04f2b8d3eb863d8d15472d757ce4f10fa88c010a3852b1c4c1
- StickelbergerCharacterEval/Detint.lean 4d473de1cb0c6eb0e28ae5076fab49ddc2dc1a1f0e6db39dc37bcb766c1ef3fe
- StickelbergerElements/CoefMapSingle.lean 6a6f5ee77987cdce70b9d4deb748966b70bab63f0c03cfe304e5af011d271ac6
- StickelbergerElements/TwistedBernoulliValueCongrPowMulFirst.lean 9e221c1c4b555e5aeb72c9a1616421aed64f57d5cffc57f362b1e74c221f3e4e
- GaloisLibrary/KummerTheory/XdualExt.lean 8384572e4b4c2919e9c83c5c07d343803becbfe5a3eadf3de9b89428f1555aff
- GaloisLibrary/KummerTheory/ResInfInj.lean e9244a8c28ffdc87256df5e200125a57a08519eb62a6cba8d0f6d8ad7b37ef72
- GaloisLibrary/KummerTheory/ResInfMem.lean a075dd12de307ff8fd2c022c85f6271260d05772a932e0506a0c506b89124249

## 1. Statement and module-length lemma

Let E be a CM subfield of Q(mu_N), d=[E:Q], l prime, R=Z_l, QZ=Q_l/Z_l, e>=1, k=e+1. On the Galois quotient G_S(E) unramified outside the primes over l the source qzTw acts on QZ by the inverse e-th cyclotomic power. D.hchi identifies the pullback with this action. Sha consists of classes locally trivial at the decomposition groups over l. The sign submodule ShaMinus is the (-1)^k eigenspace under the actual complex conjugation action (as in #609). Procyc means l odd or the cyclotomic image is trivial modulo 4. No assumption l does not divide d.

For any R-module X and scalar a, K_j=ker(a^j:X->X), K_0=0. The map a^(j-1):K_j->K_1 has kernel K_(j-1), so K_j/K_(j-1) injects into K_1. Additivity of extended length (or finite chains) yields length K_r <= r length K_1. If r=0, K_0=0 even when K_1 has infinite length. For P killed by a^r, P is a submodule of K_r. This proves the exact lenPow for arbitrary commutative R, no finite generation or DVR needed.

## 2. Genuine generator estimate

Let F=E(mu_l), m=[F:Q]<= (l-1)d <= ld. Its relative degree divides l-1; F embeds in Q(mu_(lN)). Let x in H1(qzTw)[l]. Choose continuous cocycle z representing x; lz=dm for some m in QZ. Multiplication by l is onto QZ, choose m' with lm'=m. Replace z by z-dm', whose values are all killed by l. This is torsRep. Restrict its inflation to G_F. Cyclotomic action mod l is trivial there, so it is a continuous homomorphism to F_l, zero on inertia away from l because it came from G_S(E). The restriction is injective as a function of the chosen representatives: if two such homomorphisms agree, their difference vanishes on G_F; the inflated cocycle factors through Gal(F/E), a group of order prime to l, and is a coboundary by averaging, hence so is the original by inflation injectivity. This proves unrInj (no assertion that arbitrary representative choice is a linear map).

Since F contains mu_l, finite Hilbert 90/Kummer as reconstructed in #608 identifies each such homomorphism with a unique class in F^*/F^{*l}. For each prime v outside l, inertia fixes the radical, so its normalized local valuation is integral; hence the exponent of the radicand at v is divisible by l. This gives unrSel into the actual SelK(S,l)/powK, S the primes over l. There is an exact sequence from S-units modulo l-th powers to that group and onto the l-torsion of the S-class group: send a radicand to the class of the fractional S-ideal with exponents v(a)/l; its l-th power is principal, and every l-torsion S-ideal class admits such a generator. The kernel consists precisely of S-units after multiplication by an l-th power. Dirichlet's S-unit theorem gives free rank r1+r2-1+|S| and a cyclic finite root group; its quotient by l-th powers has size at most l. Since |S|<=m and r1+r2<=m, size <= l^(2m). The S-class group is a quotient of the ordinary class group, so the Selmer quotient has size <= l^(2m) h_F, with h_F the class number. This proves selCard. The source F_l-module H1[l] is therefore finite with cardinal l^g and length g; no finiteness assumed before injection.

For the class number estimate set L=lN>=2. The classical conductor-discriminant formula for abelian F/Q gives |disc F|<=L^m since each of the m character conductors divides L. Also m<=phi(L)<=L. We can derive a slightly stronger logH than required without importing the source's ideal-counting bound: Minkowski gives an integral ideal representative of norm <= sqrt(|disc F|) in every class. The usual Minkowski prefactor (4/pi)^r2 m!/m^m <=1: for m>=2 use AM-GM m!/m^m <= ((m+1)/(2m))^m <=(3/4)^m, r2<=m/2, and (3/4)*sqrt(4/pi)<1; m=1 is immediate. For X>=1 the number of ideals of norm <=X is <=X^2 zeta_F(2)<=X^2 zeta(2)^m<=X^2 2^m. The Euler product inequality follows prime by prime from at most m local factors and each residue degree >=1; zeta(2)<=2 by the integral bound. Hence log h_F<=log|disc F|+m log 2<=2m log L<=3m log L. This gives the actual needed LogH conclusion with the classical Minkowski and conductor-discriminant inputs explicit.

Taking logarithms of l^g<=l^(2m) h_F gives g log l<=2m log l+3m log L<=5m log L. Since log l>=log 2>5/8, g<=8m log L<=8 l d log(lN). For the elementary log lower bound, integrate 1/x over [1,2] or use log 2=2*(1/3+1/(3^3*3)+...)>2/3. This proves the exact gen constant for every prime and every integer e; no Procyc needed.

## 3. Stickelberger restriction at finite cyclotomic levels

Set M=N*l and a=2M+1, odd, coprime M. For a multiple J=M*l^n define b a unit residue, u=[a^-1 b]_J, j=(a*u-b)/J, E1=(a-1)/2-j. The classical Stickelberger theorem for K=Q(mu_J) states the integral element the integral multiple of the classical theta specified below annihilates its ideal class group: with theta=sum_b (b/J)[sigma_b^-1], the element (a[sigma_a^-1]-1) theta has coefficient (a*[a^-1 b]-b)/J=j at [sigma_b^-1] (indeed multiply by [sigma_a^-1], reindex a*t=b). This is the exact integral Stickelberger annihilation, since a coprime J. The full group norm also annihilates class group: norm an ideal to Q and extend it, giving the product of all conjugates, principal. Thus sum_b E1(b)[sigma_b^-1] annihilates the class group, precisely clKill. The displayed convention, not a choice of Frobenius inverse, determines the exponents. We import the classical Stickelberger theorem (not the higher-twist annihilator) explicitly.

Write G_E=Gal(Omega/E), H=ker chi_l. A class x in Sha inflates to a cocycle f; on H it is a homomorphism h independent of representative because H acts trivially. By local conditions and inertia outside l killed in G_S, h vanishes on all inertia intersect H and on decomposition over l intersect H. It has finite image by compactness and discrete torsion coefficients. We need a finite-level unramified extension of this homomorphism, not an assumption that it is already a finite-level class.

Choose open normal V in G_E with V intersect H contained in ker h; possible since ker h relatively open. Extend h to HV by factoring through HV/V=H/(H intersect V); this is a well-defined continuous homomorphism. The descending open subgroups H_n=ker(chi_l mod l^n) eventually lie in HV by compactness. On inertia outside l, H_n already lies in H on those inertia elements since prime-to-l inertia acts trivially on l-power roots. Thus extension still vanishes there. For places over l, the union C of their decomposition groups in G_E is compact: finitely many primes of E over l, each union is conjugates of one closed subgroup, compact image of G_E times that subgroup. On H intersect C the homomorphism is zero. The compact set in HV intersect C where the extended homomorphism is nonzero is disjoint from H, hence disjoint from sufficiently deep H_n by nested compactness. Restrict to such an H_n, obtaining a homomorphism h_n vanishing on all inertia, even on all decomposition above l. This supplies the needed xdualExt, using actual all-place conditions rather than arbitrary extension of a class.

For all sufficiently large J=M*l^n the fixed field of G_E intersect ker(cls_J) is Q(mu_J), since E is embedded in Q(mu_N) inside Omega. The group G_K lies in H_n and restriction of h_n is unramified at every finite place. K is totally imaginary (J>2), so Hilbert class field reciprocity factors the homomorphism through Cl(K), compatibly with conjugation by lifts of cyclotomic automorphisms. This is the precise ordinary-class-group case of pullOnto/HomKill, with no archimedean obstruction at l=2. Apply clKill to the Artin image of an element u in H intersect ker(cls_M). Such u fixes mu_J because it fixes both mu_M and every l-power root. Its conjugates w_b=sigma_b^-1 u sigma_b also fix mu_J and belong to H. The restriction of h_n on w_b is the original h. Therefore sum_b E1(b) h(w_b)=0.

Let Gamma=Gal(E/Q), rho_J the cyclotomic restriction. The source uses phi=rho_J^-1 after identifying Gq with Gamma. Its integer twisted element ytEl(e,a,phi)=-sum_b b^e E1(b)[phi(b)^-1]=-sum_b b^e E1(b)[rho_J(b)]. Under the actual cohomology action its restriction to H at u is -sum_b b^e E1(b) chi_l(sigma_b)^(-e) h(w_b). Choose n also above the l-power annihilator of the finite image h, so b^e chi_l(sigma_b)^(-e) acts as 1 on that image, since chi_l(sigma_b)=b mod l^n. Thus the restriction vanishes. This proves resKill at every sufficiently high level, simultaneously for all such u for the given x. The level can depend on x; the ultimate annihilator cannot.

## 4. A single integral l-adic annihilator, independent of the level

Let C_J(b)=J^(k-1) B_k(b/J)/k. The actual rational yEl at level J is -sum_b (C_J(b)-a^k C_J([a^-1 b]))[phi(b)^-1]. Use the expansion from #607:
    C_J(b)=b^k/(kJ)-b^(k-1)/2+J/(k P_k)*R(b), R(b) integral.
Since a*u=b+J*j, binomial expansion gives
    a^k u^k=b^k+k b^(k-1) J*j+J^2 A,
    a^(k-1)u^(k-1)=b^(k-1)+J B,
with A,B integers. Subtracting C_J(b)-a^k C_J(u) yields
    b^(k-1)*((a-1)/2-j) + J/(2k P_k)*integer.
This is the actual YNear congruence including its denominator D=2k P_k. The integer assertion uses a odd. All lifts of unit residues from M to J are units since the prime supports agree; Bernoulli distribution gives sum of C_J along each fiber equal to C_M. Therefore the rational yEl after pushforward to Gamma is independent of n (YLevel). Its coefficients differ from the corresponding integer ytEl by elements of l-adic valuation >=v_l(J)-v_l(D), tending to infinity. This proves the actual NearLevel integral lift z in R[Gamma], with coefficientwise convergence to the same fixed rational yEl. It is an element of the finite group algebra, not merely an infinite-level family.

Every class x in H1 has l-power annihilator, since its continuous cocycle has finite image in QZ. Thus for each x sufficiently high integer approximants act exactly as z. Section 3 now gives that the restriction h_{z x} to H vanishes on H intersect ker(cls_M). For any u in H, u^phi(M) lies there (Euler's theorem); hence phi(M) times the restriction is zero on all H.

To descend this to the actual cohomology group, Procyc ensures the closed cyclotomic image is procyclic: for odd l, Z_l^* is finite cyclic of order l-1 times Z_l, procyclic, and for l=2 the image lies in 1+4Z_2. This image is infinite since E has finite degree and cyclotomic degrees grow without bound. A topological generator gamma therefore has gamma^(-e)!=1 for e>=1. A continuous cocycle whose restriction to H is zero factors through that image. Multiplication by gamma^(-e)-1 is onto QZ; choose a coboundary agreeing at gamma. Their difference vanishes on the dense cyclic subgroup, and by continuity everywhere. Consequently restriction to H is injective on H1(G_S,qzTw), since the cyclotomic kernel in G_S is the image of H. This proves resInfInj in the needed case, and the totKill implication. Thus z kills phi(M)x for all x in Sha. This is the genuine ZKill conclusion, including the finite-index factor phi(M). There is no division by phi(M) or by d.

## 5. Signed integral determinant and uniform annihilator

Let c in Gamma be complex conjugation, nonidentity of order two, s=(-1)^k. For any commutative ring A, the quotient A[Gamma]/(c-s) is free of rank d/2: choose one representative of each pair g,cg; relation cg=s*g, with s^2=1. This works at 2 as well. Multiplication by z has matrix in A; Cayley-Hamilton (or adjugate applied to the identity basis vector) gives det(z) in the ideal generated by z in this quotient. Thus in A[Gamma], det(z)=u*z+v*(c-s), no inversion of d or 2. On an s-eigenvector killed by z, the scalar det(z) kills it. Apply to phi(M)x in ShaMinus. This gives exactly adjKill.

Over C the determinant is the product of eigenvalues of multiplication by yEl indexed by characters psi of Gamma with psi(c)=s. There are d/2 (ordinary characteristic-zero character orthogonality). With chi(b)=psi(phi(b))^-1, eigenvalue is
    (1-a^k chi(a))*(-B_{k,chi}/k)
where B is the ordinary, possibly imprimitive generalized Bernoulli value at M, NOT Bprim. By the #607 nonvanishing and level change, it is nonzero: primitive parity agrees, k>=2, and every extra Euler factor 1-chi_prim(p)*p^(k-1) is nonzero in C since magnitude of the second term exceeds 1. Also 1-a^k chi(a)!=0 since a>1. This establishes nonzero determinant without requiring nonzero modulo l.

The source denY=M*k*(k+1)! clears all coefficients of C_M, hence of yEl, by the Bernoulli denominator result of #604. Therefore X=denY^(d/2)*det(yEl) is a nonzero rational integer, the determinant of the integer matrix of multiplication by denY*yEl. Fourier bound as in #609 gives |B_{k,chi}|<=4 M^k k!/(2pi)^k<=M^k k!. Since |1-a^k chi(a)|<=2 a^k, each eigenvalue has absolute value <=sizeY=2 a^k M^k k!. Hence |X|<=bdX^(d/2), bdX=denY*sizeY, exactly the Detint contract. The determinant over R of z is the same rational determinant embedded in Q_l, since the matrix construction commutes with base change. In particular det(z) divides X in R. Write r0=v_l(X), r1=v_l(phi(M)), both finite nonnegative. The units in R can be canceled, giving l^(r0+r1) kills ShaMinus and
    (r0+r1) log l <= (d/2) log bdX + log M.
This is the source killPow, with explicit constants below.

Set T=e*l*N>=2. M<=T, k=e+1<=T, a=2M+1<=T^3, k+1<=T^2. Then
    bdX*M=M*k*(k+1)!*(2*a^k*M^k*k!)*M
      <= T^(7k+6) <= T^(10k)
using factorial <= n^n and k>=2. This is the source BdxLog argument without its extra factor 3 in T. Since d>=2, log M<= (d/2)log M, so
    (r0+r1)log l <= 5 d k log T.
This proves killPow with C=5 (the source proof gives C=30). We have retained the half-rank determinant and used T rather than 3T; both inequalities are explicit. No claim that these constants are optimal.

## 6. Assemble stickBound

Combining lenPow, gen and killPow yields finite minusLen<=r*g, and
    minusLen(D,e)*log l <= 40*l*d^2*(e+1)*(log(e*l*N))^2.
Indeed r log l<=5 d(e+1)log(e*l*N), and g<=8 l d log(lN)<=8 l d log(e*l*N). This proves the actual existential StickBound with explicit C=40, versus 240 obtainable from source C=30 and factor 8. No semisimplicity, no division by the field degree, and no assumption of finiteness before proving it. It also covers l=2 when Procyc holds; without Procyc the injectivity argument was not established. The actual source ThmBcFree only needs odd primes.

## Boundary

Conventional reconstruction with explicit classical integral Stickelberger annihilation, Artin reciprocity for the Hilbert class field (including conjugation naturality), Dirichlet S-unit theorem, conductor-discriminant and Minkowski estimates, cyclotomic/local Galois facts and the source LData compatibility. Those foundational formal correspondences and original Lean kernel replay remain open. The present proof does not prove those foundational theorems from first principles. The next actual target is DegExistsLift.deg and ThmBcOfPsiBound.thmBcFree_of, including the exact prime partition and subsequent thresholds. The good-prime result #609 is separate; no conclusion about RH or GRH follows from either bound alone.

Boundary: RH-A26-D05_STICKBOUND_CONVENTIONALLY_RECONSTRUCTED__DEGREE_PARTITION_THRESHOLD_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
