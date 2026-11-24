# RH-A26 D05 — full torsion-layer transfer, conditional counting and reciprocity reconstruction

**Disposition:** independent conventional mathematical proofs of the source's torsion-layer transfer, the counting argument relative to its genuine auxiliary system, and the reciprocity implication from classical global and local duality. The latter inputs and the construction of the auxiliary Euler system remain explicitly imported/open for exact-source foundational audit. Not a Lean replay or RH/GRH certification.

## Exact sources reopened

Relative to original pinned lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties:

| Module | SHA-256 |
|---|---|
| PrimitiveFrobeniusFixed/ShaToShT.lean | 70b3de3374bda1e2cdfd223e5f1d6981f42001ed015ccb557bd4cd5e65e38ef5 |
| GaloisLibrary/KummerTheory/LenDirected.lean | 8cd5d4b8fdb2f55a4b4f218edbb1914520759fc08dc4162b91f5edeca09e2c38 |
| GaloisLibrary/SelmerTransport/ConjStableShaFam.lean | d601228f26cb82f2f228b44b6ab97a6dd8e35ff8ca0b32d3e3ec9b13dae14aad |
| PrimitiveFrobeniusFixed/QocEquiv.lean | c15c50b0938eb0912788f3af40a2176a5ec5fa160cba55965f224dc23d51c323 |
| PrimitiveFrobeniusFixed/IsAdmissiblePrimeListNil.lean | 4a5b83a90871ef58923fddc1c12ae6d3f5ddff7339747c1493a1dd17c758f433 |
| PrimitiveFrobeniusFixed/FrobFix.lean | 6183defac979c455b2bfd61358107bccb9515cb1e973e274691da656fe9247a1 |
| PrimitiveFrobeniusFixed/ShtNu.lean | beffd52a0cf388d3da30267a9c3a7d933206e21f878e994583b158bea18e56be |
| PrimitiveFrobeniusFixed/Imports.lean | 84635651a46afbbd553918517c3aea5f30a1af15797020ec61c9f3391b669ae9 |
| PrimitiveFrobeniusFixed/ImportsAlt.lean | d09e644132b439db7a096d34e4a465724aa30044892758a2f866cf3beb2a288d |
| PrimitiveFrobeniusFixed/ChiDvd.lean | f570d34cb67e0e4778c66aef8d722ea721db7b5ff7e2e2a78dd398d3f8462803 |
| PrimitiveFrobeniusFixed/AddPowNsmul.lean | f7c2eab83b9fadff50f59dcab3ad1437c28149fb8d95b30812275a9b816365ab |
| PrimitiveFrobeniusFixed/RadEqv.lean | 206485612ec5b28c7293344474b82a7fe289963866d9199be416ab8b30d8ca55 |
| PrimitiveFrobeniusFixed/ChebQ.lean | 7f078e823f265111799ec6e78ebe50b79b8e06b7098b6e11b10aec1d8400c675 |
| PrimitiveFrobeniusFixed/PlaceBasic.lean | 55a6f8f20a629ce5bf4ce29232136e36ae859e6250403009fa574e7f48f0984e |
| PrimitiveFrobeniusFixed/OverIff.lean | 189230817c6416180d71e7e0fbc7fba7568ad1f8d46709f06003f5c3fe97df28 |
| PrimitiveFrobeniusFixed/NuSysEx.lean | 07dca756b6ecc3dfe57c1dad484f793ded486c1c57bd3b559007509bc41b26d9 |

Original Formalism/GaloisCohomology/Statement.lean SHA 67dc5835eb4b337dfbbbf7f0accd1198b59793ae70f5af34421a7c35410d632c defines QZ = Q_l/Z_l with discrete topology. ConjStableShaFam defines QO = O tensor_{Z_l} QZ and shaFam (all inertia and decomposition at l). The remaining notation follows the source, not an alternative model.

## 1. Genuine torsion coefficients and normalized representatives

Let O be the source's DVR finite over Z_l, with uniformizer pi and fraction field K. Use the standard faithful embedding of Z_l and the torsion-free finite Z_l-module O. Tensor the exact sequence Z_l -> Q_l -> Q_l/Z_l by O. This gives QO = K/O: O[1/l]=K since l is a unit times pi to a positive power. All elements are pi-power torsion and QO[a] = a^{-1}O/O is cyclic, isomorphic to O/(a) for nonzero a; its length is v_O(a). Thus a primitive element w with annihilator (a) generates QO[a]. These are the mathematical coefficient facts behind qoCyc.

G is the absolute Galois group of Q. For an O-unit character alpha and delta with u=alpha(delta)-1 a unit, any locally constant 1-cocycle c admits the normalized representative
    c0(g) = c(g) - (alpha(g)-1) u^{-1} c(delta).
It is locally constant even if alpha has not separately been asserted continuous into discrete O: the correction uses alpha(g)c(delta)=c(g delta)-c(g). The cocycle law is preserved by subtracting a coboundary. It satisfies c0(delta)=0, and the representative is unique, since a coboundary zero at delta is identically zero by invertibility of u. The local witness m_D is changed by subtracting the same global normalizer; local triviality in H1 is preserved.

The source's ShT(a) consists of normalized locally constant cocycles with values killed by a, zero on inertia outside F, and at every place dividing F a decomposition-group coboundary with a-killed witness. The source ShaU requires inertia-local triviality everywhere and decomposition-local triviality at l, with no common torsion level imposed.

To cover the source ShaU, let c0 be normalized and choose a single decomposition witness m0 at a place above l. Compactness of G and local constancy give finite image of c0. Choose k large enough that pi^k annihilates all those values and m0. At all places above l, Galois transitivity and cocycle conjugation transport m0 to alpha(s)m0-c0(s); this is killed by the same pi^k. At any place outside F, alpha is trivial on inertia by the source first ramification hypothesis, so the local coboundary condition makes c0 zero there. At a place dividing F but not l, the second ramification hypothesis supplies i in inertia with alpha(i)-1 a unit. A witness m on inertia satisfies (alpha(i)-1)m=c0(i), so pi^k m=0. Since inertia is normal in the decomposition group D, the corrected cocycle d=c0-(alpha-1)m vanishes on inertia. For x in D and i in inertia,
    0=d(x i x^{-1})=(1-alpha(i))d(x).
The unit forces d(x)=0. Thus m works on all of D, including its required common torsion bound. This treats the possibly infinite collection of places without trying to take a maximum of infinitely many arbitrary witnesses.

Therefore every source ShaU class is represented by some ShT(pi^k), under the stated unit, place-transitivity and ramification hypotheses. ShT(pi^k) increases with k. Its image P_k in H1 has length at most length ShT(pi^k) (indeed normalization gives injection on the source cocycles), and ShaU is contained in their union. Equality of this union with ShaU is not needed or claimed.

If all length ShT(a)<=B for a nonzero, any finite strict chain in ShaU has finitely many witnesses to its strict inclusions. One P_k contains all witnesses. Intersect each submodule in the chain with P_k: the intersections still strictly increase. Hence the chain's length is at most B. Taking the supremum proves the exact shaToShT conclusion length ShaU<=B, including B=infinity. No finite-generation assumption on ShaU is used. This also proves lenDirected (for cofinally bounded increasing P_k).

## 2. From a global cocycle to a usable local reciprocity step

In the actual count, U=G_{Q(mu_F)}, M=l^m, F=N0 M, alpha is trivial modulo M on U, and beta=chi_l alpha^{-1}. The source Dat includes l odd, oddness at -1 modulo M, and a g with alpha(g)-chi_l(g) a unit. On U, the cyclotomic character is also 1 modulo M. A normalized ShT(a0) cocycle, for a0 dividing M, restricts to an additive homomorphism on U, equivariant by alpha on G-conjugation. It is detected there: if zero on U, it descends to G/U on its value module; this quotient is abelian, so the cocycle identities at g delta and delta g give (alpha(delta)-1)c(g)=0. This forces c=0. This independently proves the restriction/detection part of shtNu. Its Frobenius test follows as well: at q congruent to 1 modulo F, q not dividing F, D_q is contained in U because inertia is trivial on mu_F and a Frobenius lift acts by q on mu_F. The unramified additive map on D_q factors through the procyclic D_q/I_q; if zero on one Frobenius it is zero on D_q and by equivariance on every conjugate. Thus adding q to the local-zero constraints is exactly the kernel of evaluation at that Frobenius.

For nu from IsNu (additive on U, locally constant there, equivariant by beta), choose d with beta(d)-1 a unit; Dat.notCyc supplies d because beta-1=alpha^{-1}(chi_l-alpha). An explicit global extension is
    n(g) = (beta(d)-1)^{-1} nu([d,g]),
where [d,g]=d g d^{-1}g^{-1} lies in U. The commutator identity [d,gh]=[d,g] g[d,h]g^{-1} proves the cocycle rule; equivariance proves n|U=nu. It is locally constant, n(d)=0, and each n-value is a scalar times a nu-value. This reconstructs ImportsAlt.ext without an extension-existence black box.

For ChiDvd.step let a0|a|M and a kill nu(U). The extension n and the original c are killed by a. The character modulo a has open kernel containing U; at primes outside Nq with F|N, inertia lies in U, alpha is 1 modulo a, and both c,n vanish by their stated unramified conditions. At primes over N other than q, the required a-killed local witnesses are the original ShT(a0) witnesses if over F and 0 otherwise (the additional Sn zero conditions). At q, q=1 modulo F makes D_q a subgroup of U, hence alpha and beta trivial modulo a; c kills inertia there. These are precisely Rec's conditions, including l|N, q!=l and a!=0. Thus Rec applied to n gives y c(g)=0 for nu(tau)=y w0 on inertia at q. This reconstructs the actual step, not just a formal length inequality.

## 3. Independently reconstruct Rec from its stated classical duality inputs

Source statement: ML.recip : PoitouTateDuality -> UnramifiedOrthogonality -> Rec. The argument below imports those precise two classical duality properties, rather than assuming Rec. The imported global property is the vanishing of the sum of local invariants of a global degree-two class over a finite ramification set, and local invariant injectivity for cyclotomic coefficients. The imported local property is the annihilator characterization of the unramified H1 groups for Tate-dual coefficients, as in UnramifiedOrthogonalityAt. We do not here reconstruct those foundational theorems or validate their complete Lean statement correspondence.

Set B=O/(a), identify QO[a] with B using 1 -> w0, and denote the transported cocycles by C,N. For a unit a the conclusion is trivial; otherwise choose r>0 with l^r in (a). Put R=Z/l^r, with natural map phi:R->B. Write A(g),D(g) for reduced alpha,beta, so A D = phi(chi_r). The character and cocycles into these discrete finite modules are locally constant. R-linear maps lambda:B->R separate elements: decompose the finite abelian l-group into cyclic summands R/(l^s), and on a component detecting a nonzero value use its injection into R by multiplication by l^(r-s). Thus enough to prove lambda(N(tau) C(g))=0 for every lambda.

Form the continuous R(1)-valued cup cocycle
    W(g,h)=lambda(N(g) A(g) C(h)).
The two crossed-homomorphism laws give dW=0 by expansion: the four terms chi_r(g)W(h,k)-W(gh,k)+W(g,hk)-W(g,h) cancel using A(g)D(g)=phi(chi_r(g)). For every inertia outside primes S dividing N_level*q (N_level denotes Rec's integer N, not the cocycle N), A=1 and C=N=0; chi_r=1 there since l belongs to S, so D=1 too. The common subset defined by those four conditions is a closed normal subgroup: use the cocycle law and conjugation with trivial action. It contains the closed normal inertia-generated kernel of G->G_S, so W descends to G_S, by invariance under multiplication on the right in each argument.

At v in S other than q, C(h)=(A(h)-1)b_v on the chosen D_v. There W=dV where V(g)=-lambda(N(g) A(g) b_v). This is the explicit local coboundary; substitution in dV verifies the sign. All those local degree-two classes vanish. For l odd, real places contribute no positive-degree l-primary obstruction, and the global invariant sum/injectivity property forces W|D_q to be a coboundary. Here use the actual distinguished place over q and the standard place concordance over Q.

On D_q, A=D=1, and C is additive and vanishes on inertia. Choose Frobenius s and the continuous unramified homomorphism x0:D_q->R sending s to 1, obtained by reducing D_q/I_q = profinite Z. Then C(h)=phi(x0(h)) C(s), since both maps factor through that procyclic quotient and agree on its generator. Define f(g)=lambda(N(g) C(s)); it is an R(1)-cocycle because chi_r(g) acts trivially after applying phi on D_q. W(g,h)=f(g)x0(h). Every unramified R-valued homomorphism x is x(s)x0, so the vanishing local cup extends to all such x. Local unramified orthogonality makes f unramified. Since chi_r is trivial on inertia, restriction being a coboundary there means f(tau)=0 literally. Now
    lambda(N(tau) C(g)) = x0(g) f(tau)=0
for every g in D_q. Separation by lambda yields N(tau) C(g)=0 in B, and N(tau)=y mod a yields y c(g)=0 in QO. This proves Rec under the exact classical inputs and standard place and procyclic facts; no Euler-system or Bernoulli hypothesis is used. The source's glob/locq/core argument has thereby been independently reconstructed using an explicit procyclic generator and separating functionals.

## 4. The auxiliary prime selection (conditional on ordinary Chebotarev)

The following is an independent reconstruction of the structural pick proof in AddPowNsmul, under standard cyclotomic Galois surjectivity, Frobenius reduction, and Chebotarev for a nonempty open subset of the absolute Galois group. Chebotarev in this form follows by taking an open normal finite-index subgroup whose coset lies in the open subset, applying finite Chebotarev to its conjugacy class outside any finite set, and choosing a conjugate lift of Frobenius in that coset.

Let r be the source auxiliary prime, rho^M=r, H=U intersect Stab(rho). The Kummer map U->mu_M, u->u(rho)/rho, is a homomorphism with kernel H since U fixes mu_M. Conjugation by g acts on its image by chi_l(g) modulo M (the factors from g(rho)/rho cancel). Hence any M-torsion additive equivariant map f on U vanishing on H factors through a cyclic subgroup of mu_M and satisfies (gamma(g)-chi_l(g)) f=0. This proves the radEqv mechanism. For nonzero c with character alpha, Dat.notCyc implies H is not contained in ker c.

If nu=0, any value generates its zero image. Otherwise nu(U) has finite image generating a single cyclic O-module V: QO torsion layers are nested cyclic modules, so a value with maximal annihilator valuation generates the image module. Put K={u in U: nu(u) in pi V}. The quotient map nu mod pi V is nonzero. If H were contained in K, the Kummer equivariance argument for beta would force this quotient to be killed by beta(g)-chi_l(g). For g acting by -1 on mu_F, alpha(g) is -1 modulo M by Dat.odd, hence 1-alpha(g) is a unit because l is odd. Thus beta(g)-chi_l(g)=beta(g)(1-alpha(g)) is a unit, a contradiction. So H not contained in K. Outside K, nu(u) generates V (unit multiple of a generator).

Also H is not contained in C=G_{Q(mu_{F*l})}. Choose u fixing mu_F and acting by 1+F on mu_{F*l}, and g acting by inversion there; these lifts exist by cyclotomic surjectivity. The ratios u(rho)/rho and g^{-1}(rho)/rho lie in mu_M, which U fixes. The element g u g^{-1} u fixes rho because g inverts that ratio. It fixes mu_F but acts by (1+F)^2 modulo F*l, which is not 1 because l is odd and l|F. Hence it belongs to H but not C.

The three proper exclusions inside H are ker c, K (take K=ker c when nu=0), and C. Put B0=ker c. Every x in H has x^M in B0, with M odd. To prove H is not covered by these three subgroups: a group cannot be the union of two proper subgroups (multiply an element exclusive to each). If a cover by K,B0,C existed, choose x outside B0,C (hence in K), y outside K,C (hence in B0). Then xy must be in C. The element x^2 y is outside K and C; it cannot lie in B0 either, because that implies x^2 in B0 and together with x^M in B0 and odd M forces x in B0. Contradiction. The exclusion set is nonempty open since U,H and all the kernels/preimages are open (locally constant maps on U).

Chebotarev provides q and Frobenius phi in it, avoiding any specified finite primes, including divisors of F*l*r and the existing list product. The element fixes mu_F but not mu_{F*l}, giving q=1 mod F but q!=1 mod F*l. Since it fixes rho, reduction at q gives an M-th root of r in F_q^*: q is prime to r and the root is a unit, and Frobenius acts by q on its reduction. Thus ord_q(r) divides (q-1)/M, an integer prime to l because v_l(F)=m and q!=1 mod F*l. These are AdmP and freshness, while phi outside B0 gives c(phi)!=0 and outside K gives generation of nu(U). This recovers the actual selection conditions of pick; the availability of a genuine NuSys remains a separate input.

## 5. The exact counting budget

Assume the original Dat and source NuSys exists, with its init and step witnesses, for w whose annihilator is (M). Write z=zVal, M=z k, with a0*z|M, so z,k,a0 nonzero and a0|k. For each admissible list L define a_L generator of the ideal annihilating nu_L(U); it divides M since values are M-torsion. Let j(L)=v(a_L) and J=v(M). Write S_L=Sn(a0,r prod L), where Sn imposes zero on all decomposition groups at primes dividing that product. Only lists with a0|a_L are used.

**Key local estimate.** At a selected prime, suppose nu_new(tau) has annihilator (a) and a_new annihilates nu_new(U). Since tau lies in U, a_new=a e. If a0|a, apply the step above with a_new and generator w0 of QO[a_new]. Write nu_new(tau)=y w0. Then y c(phi)=0 for all c in the old Sn. If a is a unit, so is a0, and c=0. Otherwise v(y)<v(a_new) and v(a)=v(a_new)-v(y), hence v(e)=v(y); y and e are associates, so e c(phi)=0. (Zero y belongs to the unit-a case.) Evaluation has image in QO[e], length at most v(e). Its kernel equals the new Sn by the all-place Frobenius test in section 2. Exactness gives
    len(old Sn) <= len(new Sn)+v(e)
in extended lengths; no prior finiteness of old Sn is assumed.

**Initial step.** NuSys.init gives nu_empty(tau_r)=unit*z*w, of annihilator (k). Therefore a_empty=k e0. Applying the local estimate with a=k to Sn(a0,1)=ShT(a0) gives length ShT(a0)<=length S_empty+v(e0).

**Inductive step.** If S_L is nonzero, choose c nonzero in it. It is detected on U. The prime selection in section 4 supplies a fresh admissible q with c(phi)!=0 and nu_L(phi) generating the image module. NuSys.step gives nu_{q::L}(tau)=unit*nu_L(phi), with annihilator (a_L). So a_{q::L}=a_L e, and a0 still divides it. Since e kills the nonzero evaluation, e is not a unit and v(e)>0. Thus j strictly increases, bounded by J. The local estimate gives
    len(S_L)+j(L) <= len(S_{q::L})+j(q::L).
Every nonzero state has such a successor. Descending induction on J-j, or iterating at most J-j times, reaches S=0. This proves length S_L+j(L)<=J for all states, even if lengths were initially allowed infinite. This is the source chain lemma and full count induction, not a heuristic count of examples.

Finally
    len(ShT(a0)) <= len(S_empty)+v(e0)
                  <= J-v(k)
                  = v(z).
The middle inequality uses j(empty)=v(k)+v(e0), with all valuations finite since a_empty|M and M nonzero. This proves the exact count inequality given the genuine NuSys and reciprocity inputs. Combined with section 1 and the source zEval witnesses z|A_f, a0*z|M for every nonzero a0 (not independently reconstructed here), it yields the intended primitive bound in the nonexceptional branch once the genuine ramification/unit conditions from prim_case hold. The exceptional exc branch and zEval remain open.

## 6. Evidence and precise next mathematical target

This is a substantial mathematical reconstruction rather than full original-kernel replay: it treats the actual local witnesses, coefficient ring, reciprocity pairing, prime selection and counting budget. Classical place theory, cyclotomic facts, Chebotarev, Poitou–Tate invariant sum and unramified orthogonality are imported as stated mathematical theorems; semantic/foundational exact-source replay remains open. The genuine construction of NuSys in NuSysEx is not independently established. The source starts with laxEx, obtains a norm/congruence-compatible system via sysOfLax, constructs Kolyvagin-style classes via kolEx and derInv, then verifies NuSys. The next work must reconstruct these witnesses and their local/global identities, not another abstract counting lemma. Independently verify zEval and exceptional exc as well; then integrate with primitive conductor accounting.

Boundary: RH-A26-D05_SHA_TORSION_TRANSFER_PROVED__COUNT_RECIP_PICK_RECONSTRUCTED_WITH_EXPLICIT_CLASSICAL_AND_NUSYS_INPUTS__NUSYS_ZEVAL_EXC_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
