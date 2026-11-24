# RH-A26 D05 — primitive ramification, exceptional vanishing, and assembly of ML.vChar

**Disposition:** independent conventional reconstruction of the complete conditional statement ML.vChar (including the primitive and induced cases), under the source Rec and the classical arithmetic foundations identified in this and earlier dossiers. No original Lean kernel replay, proof of all foundational hypotheses of the submitted RH/GRH chain, exact downstream semantic correspondence, or MATHCERT certification.

## Source identities

Reopened directly from the pinned original intake. Relative to lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties:

| Module | SHA-256 |
|---|---|
| PrimitiveFrobeniusFixed/PrimRam.lean | 4be7bfc7e61bdb16913af56f9729f68bb5c42f4ff040ca96bc41ecff2d8153ff |
| PrimitiveFrobeniusFixed/RatPlace.lean | e2dc01eeee8390f9c86df508689b13331c321f165a59ed02ea8fae0124b30039 |
| PrimitiveFrobeniusFixed/PrimCase.lean | 7a267aaec723dbe9b97c01e9d92e35756f1d63e02fef2b8a5ead2ce9983b0ab3 |
| PrimitiveFrobeniusFixed/ShaToShT.lean | 70b3de3374bda1e2cdfd223e5f1d6981f42001ed015ccb557bd4cd5e65e38ef5 |
| PrimitiveFrobeniusFixed/IneTau.lean | 25a386d960bca196db6ee3b2a0456cf8132a3357362c0ba66125c3370c733c74 |
| PrimitiveFrobeniusFixed/PlaceBasic.lean | 55a6f8f20a629ce5bf4ce29232136e36ae859e6250403009fa574e7f48f0984e |
| GaloisLibrary/KummerTheory/RadExists.lean | f4ac97ceace8ad6d7455ebf69f705017bd6b6bf069ee6f08055d09727bb41762 |
| GaloisLibrary/KummerTheory/DvdOfIne.lean | 0a363fd9c2f04757d08a0f5df45893b9de10da24aee5e8fa47780ac53e7f7bea |
| GaloisLibrary/KummerTheory/RadClKer.lean | 6028e18122352d960244598d9c96a995758c06d5e8027ba1bf9413ca3de0a51f |
| CharacterLevelBounds/ShaFamMono.lean | 088b497cf3b210287fe2c8ec1dd991ad5d12f80b38bd2584d332336f112a0566 |

Use the actual definitions: G=Gal(Qbar/Q), chi=chi_l, dirG(psi)=psi composed with cyclotomic action modulo the character's level, alpha=(chi^e dirG(psi))^(-1), QO=O tensor_Zl (Q_l/Z_l), rho=twist2(alpha). The source V(l,e,dirG(psi)) is length_O ShaU(twist2(alpha),l,G), not a different Selmer module. ShaU uses all inertia conditions and decomposition conditions above l.

Imports for this dossier: standard finite/infinite Galois restriction and local place theory (inertia images and fixed fields), cyclotomic Galois surjectivity, total ramification of Q_p(mu_{p^s}) and unramifiedness of prime-to-p roots of unity, finite DVR facts, and independence of distinct field automorphisms. The finite-root Kummer argument is given explicitly below. These classical inputs are not claims of independent replay of their exact formal implementations. Earlier mathematical dossiers #604--#607 supply the denominator, torsion transfer, count/Rec, NuSys and zEval arguments, respectively, with their own stated foundations. The present assembly is conditional on those arguments and inputs; no conclusion about the entire submitted proof follows merely from the assembly.

## 1. The three conclusions of primRam

Let psi be primitive at f, with character order n prime to l, O the coefficient DVR, maximal ideal (pi) and residue field of characteristic l. The finite image values satisfy x^n=1. If x!=1 but x-1 is a nonunit, reduction gives x=1 modulo pi, so the geometric sum 1+x+...+x^(n-1), which is zero in the domain since x^n=1, reduces to n!=0. Contradiction. Thus every nonidentity character value differs from 1 by a unit. This proves the source's third statement, including the n=1 vacuous case. It does not assert that a general l-power root has this property.

Fix an arbitrary place above a rational prime p. Write f=p^s f0, p not dividing f0. The image of its inertia under cyclotomic action modulo f is exactly
    ker((Z/f)^* -> (Z/f0)^*) = (Z/p^s)^* x {1}
in the Chinese remainder description. Indeed prime-to-p roots are unramified and p-power roots generate a totally ramified local extension. The latter assertion follows from the Eisenstein polynomial Phi_(p^s)(1+X) for s>=1; base change to the unramified prime-to-p cyclotomic extension preserves Eisenstein and hence total ramification. Thus all p-power unit actions lift to inertia at that place; at s=0 the image is trivial. This also treats p=2 and f0=1, with the trivial factor convention. For example a nominal conductor with p=2,s=1 has trivial 2-part and cannot support a primitive character at that level.

If p divides f, the character is nontrivial on that kernel. Otherwise, by surjective reduction, it factors through f0<f, contradicting minimal conductor f. Choose a kernel element with psi(u)!=1 and lift it to inertia. The preceding unit lemma proves that dirG(psi)(g)-1 is a unit, at every place above p. For a place not above f, its inertia acts trivially on mu_f, hence dirG(psi)=1 there. In the source Over A f means f is in the valuation maximal ideal: for a nontrivial finite place over p this is p|f. For valuations with no rational prime below them all integers are units; inertia is trivial (residue map is injective on the algebraic extension of Q with trivial valuation). This proves all three source statements of primRam with the actual conductor and all-place quantifiers.

## 2. A residual Kummer vanishing lemma over Q

Let l be odd and eta:G->F_l^* the action on mu_l. Let z:G->F_l be a locally constant cocycle
    z(gh)=z(g)+eta(g) z(h).
Assume z vanishes on inertia at at least one place over every rational prime p. We prove z is a coboundary.

Choose a primitive l-th root zeta. Then h(g)=zeta^z(g) is a continuous multiplicative cocycle into mu_l, since g(zeta)=zeta^eta(g). Its kernel together with the cyclotomic kernel contains an open normal subgroup: h is locally constant on compact G and is 1 near identity; the kernel is a subgroup by the cocycle identity, and its finite-index core is open normal. Intersect with the kernel of the action. Thus the cocycle descends to a finite Galois extension L/Q containing mu_l.

For completeness, finite Hilbert 90 in the needed convention: choose x in L with beta=sum_(s in Gal(L/Q)) h(s)^(-1) s(x) !=0; such x exists by independence of distinct field automorphisms. Then g(beta)=h(g) beta by the cocycle identity and reindexing. It follows beta^l=a in Q^*, since all h(g)^l=1. This proves the needed radical representation directly.

At a chosen place over p, vanishing on absolute inertia implies beta fixed by it. In the finite Galois extension containing beta, the image of absolute inertia is the local inertia group I of L_w/Q_p. Therefore beta belongs to the fixed field L_w^I, an unramified extension of Q_p. In the valuation normalized by v_p(p)=1, its valuation is an integer. As beta^l=a, we obtain l|v_p(a) for every p. This reasoning also applies at p=l and to negative valuations; it uses unramified fixed fields, not tame Kummer assumptions at l.

Every nonzero rational a is a sign times the finite product of rational primes raised to its integer valuations. Since all these exponents are multiples of l and l is odd, a=y^l for a nonzero rational y (including negative a). Thus beta=y*zeta^j for some j mod l, and the equation g(beta)=zeta^z(g) beta now reads
    z(g)=(eta(g)-1)j.
This is the asserted coboundary. In particular if some t satisfies eta(t)!=1 and z(t)=0, then j=0 and z=0. This reconstructs RatPlace.kum, radExists, the needed rational case of dvdOfIne, and rat_pow. It relies on the actual inertia condition at ALL rational primes. No class-number bound for a general number field is asserted. At l=2 a=-1 is an obstruction to the elementary rational-power step (and the chosen normalizing action -1 is trivial modulo 2); the source excludes 2.

## 3. Exceptional branch exc for the genuine coefficient module

Assume alpha(g)-chi(g) is a nonunit for every g and alpha kills inertia away from l. Then modulo pi, alpha equals the mod-l cyclotomic character eta, embedded in the residue field of O. Choose a place A0 over l and t in its inertia acting on mu_l by inversion, by total ramification of Q_l(mu_l). Since l odd, eta(t)=-1!=1 and alpha(t)-1 is a unit. This is the required source normalizer.

Take arbitrary a0!=0 and c in ShT(QO,alpha,t,l,a0). By definition c is locally constant, a crossed homomorphism, c(t)=0, a0 kills every value, it vanishes on inertia outside l, and at each place over l it is a local coboundary. At A0 that local coboundary has form c(g)=(alpha(g)-1)m on the decomposition group. The normalization at t gives m=0 by the unit property, hence c vanishes on the entire decomposition group at A0. In particular it vanishes on inertia there.

First suppose pi*c=0. All values then lie in W=QO[pi], an F_l-vector space because pi divides l. The scalar alpha acts on W as the ordinary F_l scalar eta(g), by the congruence modulo pi. For every F_l-linear functional lambda:W->F_l, lambda composed with c is a locally constant residual cocycle satisfying the exact hypotheses of section 2 and normalized at t. Thus lambda(c(g))=0 for all g. Linear functionals separate points (extend any nonzero vector to a basis), so c=0. This proves the actual sht_pi for the source module; the same proof works for any O-module and pi-killed values.

For general c, write a0=unit*pi^j. Then pi^j*c=0. Induction on j proves c=0: if pi^(j+1)*c=0, d=pi^j*c is in the same ShT submodule and pi*d=0, so d=0; apply the induction hypothesis. The zero exponent case is immediate. Thus ShT(QO,alpha,t,l,a0)=0 for every nonzero a0. Apply the previously reconstructed shaToShT with F=l and B=0: the first ramification condition is the assumed unramifiedness outside l; the second is vacuous; the normalizer is t. Hence length ShaU(twist2(alpha),l,G)=0, so ShaU=0. This proves the full statement exc, not just vanishing of a residual approximation or a finite layer.

## 4. Assemble the primitive estimate and the sharper branchwise statement

Let psi be primitive at f, l odd, e>=1, k=e+1, l not dividing orderOf psi, and psi(-1)=(-1)^k. Set T=B_(k,psi)/k, P_k=product of primes <=k+1 and a_f=f P_k B_(k,psi) in O (integrality proved in #604). Assume the source Rec. Split on the exact dichotomy in PrimCase.

**Nonexceptional:** there exists g with alpha(g)-chi(g) a unit. Choose once a lift delta of -1, e.g. complex conjugation in an embedding into C. Then chi(delta)=-1, dirG(psi)(delta)=psi(-1)=(-1)^k, and alpha(delta)=-1, so alpha(delta)-1=-2 is a unit. This avoids choosing a new normalizer at each precision. Away from l the cyclotomic action on l-power roots is trivial; consequently alpha=dirG(psi)^(-1) on those inertia groups. By section 1, alpha is trivial outside f*l, and at any place above f but not l some inertia g has alpha(g)-1 a unit (inversion preserves the unit-difference property). These are precisely the two ramification hypotheses of shaToShT at F0=f*l.

For every nonzero a0, use #607 to choose m>=max(1,v_l(f)), F=N0*l^m and b,sigma, satisfying Dat and a0*z|l^m, z|a_f, v_O(z)=v_O(T). The genuine NuSys (#606) supplies the system required by count (#605); count under Rec gives
    length_O ShT(QO,alpha,delta,F,a0) <= v_O(z).
The source ShT depends on F only through the sets of places over F and not over F. Since F=N0*l^m and f*l have identical sets of rational prime divisors, these sets are identical, also for trivial valuations. Therefore the two ShT submodules coincide literally (source shT_congr/over_lev), with the SAME delta and a0. We obtain the uniform bound length ShT(F0,a0)<=v_O(T) for every a0. This bound is finite and nonnegative by #607; it does not depend on the auxiliary level. ShaToShT now yields
    V(l,e,dirG(psi)) <= v_O(T) <= v_O(a_f).
The final inequality is exactly the multiplier comparison v_O(a_f)=v_O(T)+v_O(f P_k k). This is the sharper nonexceptional estimate as a complete conditional theorem, not a claim that v_O(T) is always nonnegative on the exceptional branch.

**Exceptional:** alpha(g)-chi(g) is a nonunit for all g. For inertia at any place outside l, chi(g)=1 and alpha(g)=dirG(psi)(g)^(-1). If dirG(psi)(g)!=1, the unit property from section 1 implies alpha(g)-1 is a unit, contradiction. Hence alpha is trivial on all such inertia. Section 3 applies, proving V=0, unconditionally in Rec on this branch. Since a_f is in O, v_O(a_f)>=0. This proves the other half of prim_case. One must not apply the sharper v_O(T) bound here: for psi trivial, k=2,l=3, v_3(B_2/2)=-1 and V=0, so that purported bound would be false.

As an additional consequence, in the exceptional primitive case f has no prime divisor other than l: otherwise primRam would force nontrivial inertia outside l. If f=l^s and s>=2, the kernel of reduction modulo l is an l-group; the prime-to-l character is trivial on it and factors through l, contradicting primitivity. Thus f=1 or f=l. This is a diagnostic consequence, not an assumption used in exc.

## 5. Induction of characters and the exact ML.vChar conclusion

For an arbitrary character psi of level N in the source statement, let phi be its primitive character of conductor f|N. Reduction on units is onto (CRT), so pullback preserves character order and parity. Cyclotomic actions at N and f commute with reduction, hence dirG(psi)=dirG(phi), including the entire twisted representation, local conditions and V. Under the injective coefficient-field embedding the primitive character and its conductor are unchanged. The source uses Bprim, so a_N=N P_k B_(k,phi)=(N/f) a_f, not the imprimitive ordinary sum at N. Thus a_f|a_N. Apply section 4 to phi:
    V(l,e,dirG(psi)) <= v_O(a_f) <= v_O(a_N).
This is the precise conclusion of ML.vChar with all original hypotheses: Rec, l odd, e>=1, character order prime to l, parity and identification of a_N with alN. The proof does not assume a primitive ambient character. On the nonexceptional branch the stronger bound by v_O(B_(k,phi)/k) is independent of N; on the exceptional branch V=0.

## 6. Evidence boundary and continuation

This closes the conventional mathematical reconstruction of the stated conditional character inequality, not its exact original Lean replay. The classical foundations imported across the dossiers (in particular the source PoitouTateDuality and UnramifiedOrthogonality properties implying Rec) and their formal statement correspondence remain explicit. The result is not a proof of Dirichlet GRH or RH, and does not assert that the entire original proof chain is valid. The next substantive task is to inspect the genuine consumers of ML.vChar and independently reconstruct their character-length aggregation and analytic estimate; retain the exact source-to-target bridges and avoid inferring a global theorem from a local cohomological inequality. Independently replay the original declarations and audit their actual dependency/foundational profile under the existing RH-A26 obligations.

Boundary: RH-A26-D05_ML_VCHAR_CONDITIONAL_CHARACTER_INEQUALITY_RECONSTRUCTED__DOWNSTREAM_AGGREGATION_FOUNDATIONAL_CORRESPONDENCE_ORIGINAL_REPLAY_OPEN.
