# RH-A26 D05 — finite Galois character transport and aggregate prime budget

**Disposition:** independent conventional reconstruction of ML.psiOf (Rec -> PsiBound) and the good-prime aggregation PrimeBound, using the prior conditional character inequality and stated classical foundations. The arithmetic Sha model and sign action are identified through their actual inflation construction. No original Lean replay, certification, or claim of the remaining bad-prime estimates.

## Source lock

Relative to original pinned lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties, reopened on CHAD:

| Module | SHA-256 |
|---|---|
| PrimitiveFrobeniusFixed/PsiOf.lean | be81f7279d28d67f9be81ade8a028375c11be57c11a5559f82240c14009ebd63 |
| PrimitiveFrobeniusFixed/Iv.lean | 5f08d36359f3812eb54ad017057aaf484eaf0073462746a27746861c19e6bdcc |
| OddResidueBounds/ZeroMemUnrHom.lean | c6cac1eefc91d4bf1972ae1b8ccc54ab3ce3238e19e397dafb49bb739bcecf48 |
| OddResidueBounds/AtPrime.lean | b7dbeb409c0fa08ac71c0380c8b39a2b0a716c9c328dfcacec3071e80c7458d2 |
| OddResidueBounds/PsiReal.lean | 16c55e01c50db93ff5152d11734df1f2d8d61a179e729bf77cbaefaaa6fe6a97 |
| OddResidueBounds/ProdVal.lean | 60726d2c52718b2d783b243709f656aefb6be581d335bac86720847877b4bf8b |
| OddResidueBounds/ThmBcOfPsiBound.lean | 90808ac87265e481e18121781c242726f0a8ae0bfd9832cf3b4d31c079c49d24 |
| OddResidueBounds/ChiFacts.lean | 25bf3da99a4e1476b9d27675ecb1eefd638c9048862d3f2e6c373727103bdb78 |
| OddResidueBounds/ActFacts.lean | 41aea4b8d6555218b46bde6d855b8dbc9cb76a0ba5e05d0f7d96ec7c405aa96b |
| OddResidueBounds/ActEx.lean | 71ac9ef1a779f4a2db19e35f9378e4003ff36ede20de337fe3960f64045e9339 |
| OddResidueBounds/ActConj.lean | 7c4ac179c945d0e4ed47adf4a387f8cbc3eb99fa5e4b1c741df81aa99bebde68 |
| CharacterLevelBounds/EigV.lean | 4d076154ed063735fd06a0aa883bfb28c0815ca5773458976d19ed5f12217763 |
| GaloisLibrary/SelmerTransport/ShaDecompSign.lean | 9150ecd352a3f7269bd121f43e12b2ebf879a839d24aa4db5bf5403015808f2f |
| GaloisLibrary/SelmerTransport/ExistsO.lean | ddee4514bddb2fc5de526ee8e9d561ca731f88bee75be6deabed3369889c8b9c |
| GaloisLibrary/SelmerTransport/NormO.lean | 36faf0c9c525924fff7507dd76d04e15f74a6c8504a7ae12d4f0aec6f890573f |
| GaloisLibrary/SelmerTransport/QoBase.lean | 96f207837fa516329761bdf7c707e7ff3d45fe5598ce11ac93b8b6fe435f571d |
| GaloisLibrary/SelmerTransport/ShaLenEq.lean | 77cc17f54620c295c60629531a6144c04796bdd4ae250841ca0078fb07a81e1e |
| GaloisLibrary/SelmerTransport/ShaModel.lean | 2c74ff73930693c0476dce67072d98f6389bacb7358a3dae47589f977550a415 |
| GaloisLibrary/SelmerTransport/InflAct.lean | 2664b30f5f2a85d0c08113b4a62149d5a6af32af9136c6b434f1a1379f9cf1f5 |
| GaloisLibrary/SelmerTransport/GalEmbFam.lean | 094f7f6ff784faecefcb02a102bb4776f2238446713e23eb440805ef6108a21a |
| GaloisLibrary/SelmerTransport/SelEigBase.lean | da8c33be3bde62eec61ade2414f1cd4dfc3152a7bcdc344cd99484d847f1ddf4 |
| GaloisLibrary/BernoulliNumbers/Prodint.lean | d82d20b5a36498bc9231c8e2fcb59b98fe75beea5b6f4dfdf2f060045ef41fdb |
| GaloisLibrary/BernoulliNumbers/Denupper.lean | 7f52c467183143e17739040b361c026c259fca85246e9bc99f7ca656b34e04d7 |
| GaloisLibrary/BernoulliNumbers/MapGenBChar.lean | 7a84fd98752f7b2a310001da8a8f3dcb7447f967173d5bbdf28f3025d6a51129 |
| PartsConj.lean | 5af29a66a26b7fd9711bc55bc7306832de08ca164fd3f4305f2a793981f615c0 |
| LengthEqAddEigen.lean | b10fd612b8aec69ff4f2839049eb06613d0078d2aeddac738f0f8461eb3151f2 |

## 1. Actual field action and PsiBound

Let E/Q be a finite CM abelian Galois field, d=[E:Q], G=Gal(Omega/Q), U=Gal(Omega/E), H=Gal(E/Q). Write R=Z_l, O a finite DVR over R, QO=O tensor_R Q_l/R. Let l be odd and l not divide d. Put e>=1, k=e+1. The source IsCycAct means that rho:(Z/N)^* -> H describes the restriction of ANY automorphism of Omega acting on mu_N by the specified exponent. In particular if cls_N:G->(Z/N)^* is the usual cyclotomic action and p:G->H restriction, then rho cls_N=p pointwise. Standard Galois extension of embeddings gives surjectivity of p and of cls_N; thus rho is onto, U=ker p is normal open with index d. These establish actFacts in this setting. If E is initially only embedded in a cyclotomic field, extend that embedding to Omega over E; restriction of cyclotomic automorphisms defines rho. Since a subgroup of an abelian group is normal, E/Q is abelian Galois. This gives actEx. Complex conjugation acts on roots by inversion and restricts to the CM involution c_E, so rho(-1)=c_E!=1 (actConj).

For any psi:H->O^*, form the actual Dirichlet character psi' by psi rho on units, zero on nonunits. Its order divides |H|=d (every H element is killed by d), so its order is prime to l. Its coefficient embedding is exactly chiOf rho psi. The assumed parity chiOf(-1)=(-1)^k transfers by injectivity. The Galois character dirG(psi')=psi rho cls_N=psi p=theta, including on all of G, not only Frobenius elements. Hence the reconstructed #608 vChar gives
    length_O ShaU(twist2(chi_l^(-e) theta^(-1)),l,G) <= v_O(a)
where a=alN(k,chiOf rho psi) in O.

The exact eigenspace transport works as follows. On QO write r0(g)=chi_l(g)^(-e) and r1(g)=r0(g)/theta(g). They restrict to the same action on U. On H1(U,QO), the G-conjugation action is [z(u)] -> [ri(g) z(g^-1 u g)], for i=0 or 1. Consequently the theta-eigenspace for r0 equals the invariant space for r1, including inside the local kernels. Inner conjugation by u in U acts trivially on H1: the cocycle law gives r_i(u) z(u^-1 h u)=z(h)+(r_i(h)-1)z(u). The local family shaFam consists of ALL inertia groups and decomposition groups above l, and is conjugation-stable. Restriction from G to U induces the isomorphism from the global local kernel for r1 to the U-local kernel invariants, by the prime-to-index transfer reconstructed in #591/#592: finite quotient H has order d invertible in O, so averaging kills positive-degree cohomology of H, giving global restriction isomorphism onto invariants by inflation-restriction; for each local D the index [D:D intersect U] divides d, hence local restriction is injective by the same argument. Thus local vanishing descends and ascends, not just global H1. This proves the exact eigV equality for this application. The discrete actions are continuous because theta factors through H and chi_l modulo any torsion annihilator is continuous.

By definition of psiLen (ZeroMemUnrHom), its module is precisely that theta eigenspace for r0 on U. Thus psiLen=V(l,e,dirG(psi')) and psiLen<=v_O(a). This proves ML.psiOf: Rec -> PsiBound. Together with #605's implication from the stated PoitouTateDuality and UnramifiedOrthogonality properties to Rec it gives ML.iv, with both properties retained. No foundational correspondence is assumed established by composition.

## 2. Original arithmetic module and sign

The source ShaMinus D e is Sha D e intersect the eigenspace of cAct with eigenvalue s=(-1)^(e+1), not the unconditional -1 eigenspace. Its length over R is minusLen D e. The model maps Sha D e by inflation along G_E -> GS(E,S) with S the primes over l (D.hS), to the same absolute local kernel used above. The original action on coefficients is the twist by the negative e power of the cyclotomic character (qzTw_apply, PartsConj), pulled back along that quotient. Inertia outside S is in the kernel and the quotient action descends; the inflation argument of #594 gives injectivity and identifies the image as precisely those classes trivial on all inertia outside S and decomposition groups above S. Triviality on inertia within S follows from the decomposition condition. The choice of one place above each prime of E is immaterial by G_E conjugacy and explicit coboundary transport. Under G_E=U, decomposition and inertia are intersections with U (GalEmbFam: both conditions on the action on the valuation ring/residue field are identical); l-adic twist restriction is the same action. This gives the conventional ShaModel identification via actual inflation, using standard place theory and the source LData compatibility that D.chi pulls back to the cyclotomic action. That exact compatibility and all formal interfaces remain to be replayed.

For the sign action, PartsConj defines the original automorphism action using a lift sigma in G by the cocycle formula chi_l(sigma)^(-e) z(conjGS_sigma h), with conjGal_sigma(g)=sigma^-1 g sigma. Since inflation commutes with this conjugation, this is exactly the conjugation action on the absolute cohomology module. Independence of lift follows from the inner-coboundary formula of section 1. Consequently the inflated isomorphism is equivariant and restricts to exact sign eigenspaces, giving the length equality of ShaLenEq. No identification of just dimensions or arbitrary choice of sign is used.

Choose O to contain all roots of unity of order exponent(H), for example the integer ring of Q_l adjoined a primitive such root. This is a finite DVR, embedded in the algebraic closure of Q_l. We import the standard finite local-field integral-closure theorem. Put r=v_O(l)=length_O O/lO>0, finite, the source eO. O is finite free over R (torsion-free finite module over a PID). Tensoring continuous cocycles, coboundaries and H1 with O commutes with their construction: choose a finite R-basis of O; cochains with discrete coefficients O tensor M identify as a finite direct sum of copies of the original cochains and differentials are coordinatewise. Arbitrarily many local restriction kernels commute with this finite direct sum, because a tuple belongs to their intersection exactly when each coordinate does. The same holds for the sign kernel of cAct-s. This proves the needed QoBase compatibility, including the O-linear tensor identification. For a finite length R-module A each simple R factor is F_l, and tensoring a composition series by the flat O yields O/lO factors of length r. If A has infinite length, arbitrarily long finite strict chains survive by faithful flatness and the extended equality holds (each nonzero quotient remains nonzero; r finite positive). This removes any assumption of finiteness before the bound.

## 3. Exact good-prime character decomposition and real inequality

The source ShaDecompSign gives an inequality. At the good primes in PrimeBound we can use an exact decomposition, without any modular semisimplicity claim at bad primes. As d is a unit in O, define
    E_psi=(1/d) sum_(h in H) psi(h)^(-1) action(h)
for all O-valued characters of H. H is finite abelian and O contains the required roots, so there are d distinct characters (decompose H into cyclic factors). Orthogonality holds over O: sum of a nontrivial character over H is zero by multiplying by a nonidentity character value, using the domain property; the same identity in the character variable holds because characters separate H. These identities in the group algebra imply the E_psi are pairwise orthogonal idempotents summing to identity, with image the psi-eigenspace on ANY O-module, including a torsion module. The CM involution c_E has order two, and 2 is a unit. In the sign-s module only psi(c_E)=s contributes, since opposite signs differ by a unit. Therefore, by section 2,
    r * minusLen(D,e) = sum_(psi(c_E)=s) psiLen(psi)
in extended lengths, under the source model compatibility. This is stronger than the inequality required by atPrime.

The pullback psi -> chiOf rho psi is injective by surjectivity of rho and the injective coefficient embedding; its image is exactly the characters with ker containing ker rho and parity s in the splitting coefficient field. All such characters occur because their values have order dividing exponent(H), and these roots already lie in O. This is the source set charSet(PadicAlgCl_l,parE rho k): parE is the intersection of containing ker rho and parKer, the latter means -1 belongs to the character kernel iff k is even. Since psi(c_E) is ±1, this is exactly the required parity. No character can be counted twice, and there are exactly d/2 of the matching parity: evaluation at c_E is onto {±1} since characters separate c_E, and its fibers have equal size. This sharper count holds for CM fields, not an arbitrary cyclotomic quotient with trivial conjugation.

For any such character chi, write A_chi=den(N,k) Bprim(k,chi)=N P_k B_(k,chi_prim), P_k=product of primes <=k+1. By #604 it belongs to O, and by #607's nonvanishing at k>=2 and matching parity it is nonzero. Thus v_O(A_chi) is finite. The l-adic absolute value obeys -log|A_chi|_l=v_O(A_chi)*log(l)/r, since v_O(l)=r and units have norm 1. Applying PsiBound to each eigenspace, the decomposition implies finiteness of minusLen and
    minusLen(D,e)*log(l) <= sum_(chi in charSet(PadicAlgCl_l,parE rho k)) -log|A_chi|_l.
We divided only by positive finite r. This proves psiReal and atPrime at exactly the good primes of the source. The source's existential subset T can be the full parity set; we do not need to choose it independently for every prime. Even if using the weaker ShaDecompSign inequality, the same conclusion holds.

## 4. One rational integer controls every prime simultaneously

Fix the character set C in C defined by parE rho k, or more generally any set of characters selected by their kernels in P subset parKer N k. All character values are in the cyclotomic field K=Q(mu_m), m=exponent((Z/N)^*). Every automorphism of K acts on characters by raising their values to a power coprime to m, preserving their kernels and parity. Since Bprim is computed at the minimal conductor, unchanged by injective coefficient maps, A_{sigma chi}=sigma A_chi. Thus the product M=prod_(chi in C) A_chi is fixed by Gal(K/Q), so rational. It is integral by the denominator argument in #604 and closure of algebraic integers under products, hence an ordinary integer. Every factor is nonzero by #607, including the trivial primitive character when parity is even, so M!=0 (empty product 1). Any embedding K->algebraic closure of Q_l maps the full root group bijectively to the corresponding root group and hence bijects the character sets with the same kernels. The same integer M therefore equals the product over the full l-adic set, not a product over an arbitrarily chosen embedding or a single conjugate. Each factor is integral, so all -log norms are nonnegative. Consequently
    sum_(chi in any subset T) -log|A_chi|_l <= v_l(M) log(l).
This reconstructs the required k>=2 part of b_prodint and prodVal with w(l)=v_l(M) for primes l. No k=1 extension of b_prodint is claimed here; downstream PrimeBound uses e>=1 so k>=2.

For the ordinary absolute bound, the absolutely convergent Fourier series for B_k on [0,1] gives |B_k(x)| <= 2 k! zeta(k)/(2pi)^k <= 4 k!/(2pi)^k for k>=2, since sum_(n>=1)n^-k <= 1+integral_1^infty x^-2 dx=2. If f is the primitive conductor, |B_(k,chi_prim)| <= f^k *4 k!/(2pi)^k (each of f values has modulus <=1); f<=N. The elementary primorial estimate P_k<=4^(k+1) follows by induction: for odd n=2a+1>=3 the product of primes a+1<p<=2a+1 divides binomial(2a+1,a), at most 2^(2a) by the two equal central coefficients; apply induction to a+1. For even n>=4 there is no new prime; n=1,2 are immediate. Hence
    |A_chi| <= N*4^(k+1)*4 N^k k!/(2pi)^k
            <= 16 N^(k+1) k! = bnd(N,k),
using 4<2pi. This proves the exact source constant (for k>=2). Thus log|M|<=|C| log bnd(N,k). The usual prime factorization of the nonzero integer M gives, for ANY finite set of primes S,
    sum_(l in S) v_l(M) log(l) <= log|M|.
Combine with section 3 to obtain the genuine PrimeBound statement:
    sum_(l in S) log(l) * minusLen(D_l,e)
       <= d log(bnd(N,e+1))
for all finite S of odd primes not dividing d, and all such minusLen finite. In fact the argument gives the stronger coefficient d/2 rather than d in CM fields, from the precise parity count. This is a uniform finite-set budget, independent of how many good primes are considered. In particular only primes dividing the single nonzero M can have positive minusLen among good primes. No bad prime estimate follows.

For an exact nonreal-character example take E=Q(mu_5), d=4, k=3, N=5. The two parity-matching characters send 2 to i and -i. Their primitive Bernoulli values are (12±6i)/5, so A=72±36i and M=6480=2^4*3^4*5. At good prime 5 the two factors have total valuation 1, so minusLen at 5 is at most 1. This is a bound, not a computed value of that cohomology group. It demonstrates why all conjugates, rather than a single algebraic number in an arbitrary embedding, must enter the common budget.

## 5. Boundary

The reconstruction establishes ML.psiOf, ML.iv conditional on its exact duality inputs, and PrimeBound conditional on PsiBound and the conventional model/local-field inputs specified above. It uses the genuine sign and coefficient normalization, exact character set, integer product and stated bnd constant. The source stickBound is a DIFFERENT statement, for all primes under Procyc, involving an exponent bound killPow, a torsion length estimate lenPow and generator estimate gen. ThmBcFree_of combines those with PrimeBound and a degree condition. Those bad-prime estimates and their uniformity have not been proved here. Nor is this independent Lean replay or certification. Next inspect actual killPow, gen, lenPow and degree route in ThmBcOfPsiBound, followed by the downstream threshold argument, while retaining foundational exact correspondence and original replay obligations.

Boundary: RH-A26-D05_PSIBOUND_GOOD_PRIME_AGGREGATE_RECONSTRUCTED__STICKBOUND_BAD_PRIMES_THRESHOLD_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
