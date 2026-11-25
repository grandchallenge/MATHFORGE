# RH-A26 D05 — actual tower descent and the arithmetic-center estimates

Disposition: independent conventional reconstruction of genLevel, descends/step0, xUnip, growth, detBound, exists_centres_norm and the two ABound estimates conditional on IsTower and the source limiting Poitou–Tate length identity PTShaAt. The source obtains that last identity from finite-level Poitou–Tate and local finiteness/duality; the exact limiting bridge is still to be audited. No assertion of uniform IsTower for varying base fields, LemmaK, original Lean replay or certification. Source constants retained.

## Source lock

Relative to Development/AutomorphicArithmetic/AutomorphicVarieties in the pinned intake:
- AdditiveValuationNorms/GenLevel.lean cad2e80c77f57eec4b3827aca1b3a534e8e91ef4a8403c944be27404d6f01606
- AdditiveValuationNorms/Descends.lean 10eeba6946e97802ec1aad528ca089a4ba962c988acedf3cb1fed27d9b15f037
- AdditiveValuationNorms/ABoundOfDescends.lean 30d198e1610fb4ce9152eec6d4baa3c1bfd5ac30c3e9fdc7fa33a4d4445b09e6
- AdditiveValuationNorms/ABoundOfIsTower.lean 4249346d3d787ad97c32ccbc0e95b11d72ec30923358bf98246f95f71dbc465d
- AdditiveValuationNorms/DetBound.lean 5926650338f221b316f4a0322467df20ac1a5f2bb822f49e28a4ebdf3dd242db
- AdditiveValuationNorms/Helly.lean 442f188f136ff8668c3b0b111e200f5056caea45e13a526de755a2f272048cf8
- AdditiveValuationNorms/PadicUnitsDistanceLeMax.lean a66c415852356c2527d1e604f42c28c996f15d768ed5f7f204096f80daf7f4bd
- AdditiveValuationNorms/LteNorm.lean e24722105b4c2121c0f3c5b902994973e1c4ebd98e8bdbdb2623511625b2cf1e
- AdditiveValuationNorms/Growth.lean f48f9a66ef01757fe817311237d4a0c1f14b20aff238e946715200004c02cf20
- AdditiveValuationNorms/ImportsTer.lean 70868d537a331002b29216bde7b388efa9e3910f0edab21d55b326572d6bc74c
- AdditiveValuationNorms/ImportsAlt.lean 8b29aed2a5c7e3fbc65df2e3131490d96e9a1255b90df7ea04d43a15bd1ad29b
- AdditiveValuationNorms/ExistsCentresLevel.lean 529e8eb85c14a999966f3d8f4d7e415a87b4f33484c4d7db2f117678c507fd94
- AdditiveValuationNorms/XUnip.lean 5ae4c3f56a05c681cea47f9b2c6df9fcca869a059d75fcf751ce3d339a8b3f31
- AdditiveValuationNorms/DualUnip.lean 57ae575a6998791bb7a9edad6e71af47cf10121e5c8cbe9ac98089197173faf1
- AdditiveValuationNorms/ShaLeV.lean bf65172b1182f9d50858d61ad23b75e9c2755963a01b90cd9aff14aa3f8f575b
- NumberFieldTowers/ExistsDescends.lean ad5198ddc985ff0ef9c7f4f15962c2a9584836b35f8c923027e9ea3bdd8c411d
- NumberFieldTowers/Imports.lean 4ce26c6acf620009cc862839ad9fbfcb478889979b89f8587c108bf96b241e20
- NumberFieldTowers/ShaDGen.lean a4070db25e51fe1f80e161e14a106eccf616a0ff1884ddb4991cf338d9eefa47
- NumberFieldTowers/CokerDual.lean 3aab5f9d6b12973fca8c9879da600f4317fd306405b74b5f1ea38f08ae8de1c8
- NumberFieldTowers/XTwApplyApply.lean c2e7a92efa7592787e53fe71e7c0de2c233bcd442adb1e05ad12f86383714056
- NumberFieldTowers/LenDual.lean b8d7cd4f494ae99b46bb3fccf55ea8ad1fb32843f5fdaafa3fd7fd55ad0fa12b
- GaloisLibrary/KummerTheory/ResInfOnto.lean d4be022e36c4a4679ed28ae07b1bc0a406228aa6d2c47ce0550c00bde306beb9
- GaloisLibrary/KummerTheory/DinfNil.lean d589ae989125c5652b51765825b355bb5112782f22a1371b0e4c8365ee263086
- GaloisLibrary/KummerTheory/Mk0IdMapCongr.lean 087733e315e76bbc37332cf27e466ba636d35940a911bc601abb931efbcec4e4

## 1. Genuine tower and descent (not an abstract replacement)

Write p=l, R0=Z_p, Q=Q_p/Z_p with discrete topology. Let L0 be a number field with HasMuQ (mu_p for odd p, mu_4 for p=2), G its absolute Galois group, chi its p-adic cyclotomic character, H=ker chi. Let c be the maximal exponent for which L0 contains mu_(p^c). It exists by cyclotomic degree growth, with c>=1, c>=2 at 2. The image of chi is a closed infinite subgroup of principal units, hence 1+p^c Z_p: the logarithm identifies the relevant principal units with Z_p additively, and its closed subgroups are p^a Z_p. Choose gamma lifting a generator u, with v_p(u-1)=c. This is genLevel. The unique degree p^m cyclotomic layer has absolute group G_m=chi^-1(closure <u^(p^m)>), by the same nested-field argument as #613.

The source XDual(p,H) consists of locally constant additive homomorphisms f:H->Q vanishing on H intersect inertia at every valuation ring and on H intersect decomposition at every valuation ring over p. Denote it D=Dinf p p top. This is not the unrestricted character module. For the source valuation-ring indexing, nontrivial restrictions to a number field correspond to finite primes, and the trivial valuation has trivial inertia and full decomposition but valuation(p)=1, so it adds no constraint. Under field embedding, inertia/decomposition are intersections with the embedded absolute group; the absolute kernel H is the same for every layer. Thus the source DinfTransport identifies the actual D of every layer with the same D, including all local conditions. The source X=XP is Hom_R0(D,Q) (all linear homomorphisms, not an arbitrarily chosen lattice).

For e nonzero, restriction of the actual Sha class to H is independent of coboundary representative (H acts trivially). Its image satisfies f(g h g^-1)=chi(g)^(-e) f(h) for g in G_m. The local kernels give exactly the defining vanishings of D. Conversely any f satisfying those conditions extends to a continuous cocycle on G_m. Here is a direct conventional proof in this principal-unit setting: the surjection G_m->Z_p splits continuously. Choose a lift of a topological generator, take its procyclic closed subgroup, and take its pro-p component (inverse limit of the p-primary cyclic factors of finite cyclic quotients). That component maps onto Z_p, and an infinite procyclic pro-p group is Z_p, so restriction is an isomorphism. Write G_m=H semidirect Z_p; the cocycle z(h s)=f(h) with z(s)=0 obeys the cocycle law by the stated equivariance and is continuous. Thus no assertion of splitting the full absolute group over an arbitrary quotient is needed. A cocycle restricting to zero on H factors through Z_p; multiplication by u^(-e p^m)-1 on Q is surjective (nonzero scalar), so subtract a coboundary matching its value at a generator; density and continuity give zero. This proves restriction injectivity.

At a finite prime away from p, inertia acts trivially on p-power roots and restriction z vanishes by D. At a prime over p, the local decomposition group's cyclotomic image is infinite, because a finite extension of Q_p cannot contain roots of unity of unbounded p-power order (their degrees grow). It is closed procyclic within the principal units. On its kernel z=f=0, so its descended cocycle is a coboundary by the same generator argument. This is decCob in the actual setting. Thus the class belongs to ShaAbs; #594's inflation identification gives precisely Sha D_source e on the quotient unramified outside p, using the source LData compatibility. This reconstructs resInfOnto/resInfInj in the case used by desc, not their most general odd-prime hypothesis without HasMuQ.

The untwisted action dRep(g)f(h)=f(g^-1 h g) factors through G/H since inner conjugation by H does not affect an additive homomorphism. Its continuity on each f with discrete target follows as follows: choose an open normal W in G such that f vanishes on W intersect H; commutators with W lie there, so W fixes f. H fixes it too. The image of WH is open in the cyclotomic image (quotient topology). Also f has finite image by compactness, hence is killed by a power of p. Twisting dRep by chi^(-e) retains an open stabilizer. Invariants under G_m thus equal the kernel of dTw(gamma^(p^m))-1, equivalently the inverse-generator kernel. This is shaDGen in this application.

Duality: Q is divisible and injective over the PID R0 (Baer's criterion), and a cogenerator: any nonzero cyclic submodule has a map to Q nonzero on its generator, which extends to the ambient module. Hence for an endomorphism g of D, the cokernel of precomposition by g on X is Hom(ker g,Q), by restriction surjectivity and exactness. Dualization preserves extended length: for finite length use the dual composition series, with simple factor F_p self-dual; if length is infinite, annihilators of arbitrarily long strict submodule chains form strict reverse chains by the cogenerator property. This proves cokerDual/lenDual without finiteness assumption on D. The actual xRep(g) is precomposition by dRep(g^-1); xTw(g)=chi(g)^e xRep(g). In particular the positive twist on X is the dual of the inverse generator with negative twist on D. Write A=xRep(gamma). We obtain the exact source step0/Descends equality
    shaInv(L_m,p,e) = length_R0 X / (((u^e A)^(p^m)-I)X).
Field transport and LData independence are as in #594/#609/#613. This is an equality for the actual local kernel, not only a comparison of dimensions. The source IsTower hypothesis supplies total complexity, HasMuQ, R>=1 and a surjection R0^R -> X; we do not yet prove the latter exists uniformly for varying L0.

## 2. Why the operator is unipotent modulo p

On any f in D the conjugation action of gamma factors through a finite cyclic p-group on its orbit, by the open stabilizer just proved and the principal-unit image. D is p-primary torsion. In particular D[p] is a vector space over F_p. The surjection R0^R -> X implies dim D[p]<=R: by injectivity of Q, restriction X->Hom(D[p],Q) is onto and kills pX, and a vector space with more than R independent elements would have dual dimension >R. On this finite-dimensional space a common power gamma^(p^a) fixes all elements. In characteristic p, (dRep(gamma^-1)-1)^(p^a)=dRep(gamma^(-p^a))-1, hence acts by zero. By duality X/pX is Hom(D[p],Q): a map on D vanishing on D[p] factors through pD and extends from pD, so is p times a map on D. Thus A mod p is unipotent, meaning A-I is nilpotent. Its nilpotence exponent is <=R because dim X/pX<=R. This proves the required xUnip. Scalar u^e=1 mod p makes g=u^e A unipotent modulo p for every e, with the same bound.

## 3. Exact linear growth bound, including nonfree modules

Let X be any R0-module generated by R elements, g unipotent modulo p. Set j0=floor(log_p R)+3 as in the source. For R=0 X=0 and all bounds trivial (Nat.log convention). For R>=1, take k=floor(log_p R)+1. In characteristic p, g^(p^k)-1=(g-1)^(p^k) modulo p and p^k>R, so its image lies in pX. Binomial expansion shows g^(p^(k+1))-1 maps into p^2 X: each term of (I+B)^p-I has that image when B maps into pX (including p=2). Further p-powers preserve this property. For w=g^(p^n), n>=j0, write S=I+w+...+w^(p-1). Since w=I modulo p^2 X, Sx=p x+p^2 y for some y. Thus pX subset SX+p(pX); pass to the finitely generated module (pX+SX)/SX and apply Nakayama, which gives pX subset SX. Consequently length coker S<=length X/pX<=R. For endomorphisms a,b the exact sequence coker b -> coker(ab) -> coker a ->0 (first map induced by a) gives length coker(ab)<=length coker a+length coker b, even infinite lengths. With w^p-I=S(w-I), one level increases length by at most R. For m<=j0, factor g^(p^j0)-I by g^(p^m)-I to see cokernel length is nondecreasing. Iterating proves the exact growth and twLen_le_growth:
    twLen(A,u,e,m)<=twLen(A,u,e,j0)+R*max(m-j0,0).
No cancellation of p on a torsion module, no free-module assumption, and no subtraction of infinite lengths.

## 4. Determinant and centers

Take any presentation pi:R0^R -> X. Lift images of the R basis vectors under A^(p^j0) to R0^R to obtain a matrix S with pi S=A^(p^j0) pi. For every scalar a, the induced map coker(aS-I)->coker(a A^(p^j0)-I) is surjective. By Smith normal form over the DVR, length of the former is v_p(det(aS-I)), interpreted as infinity if determinant zero. This is lift. Factor the characteristic polynomial over an algebraic closure of Q_p; for eigenvalues z_i with multiplicity, det(aS-I)=prod_i(a z_i-1), even for a singular or nondiagonalizable S.

The source IsLevel condition gives the exact elementary valuation identity
    |(u^(p^j))^a-(u^(p^j))^b|_p=p^(-j-c)|a-b|_p
for nonnegative integers a,b (zero difference included). Proof: for a unit 1+t with v_p(t)=c, expansion to the p-th power increases valuation by exactly one if p odd and c>=1, or p=2,c>=2; the leading p*t term has strictly smaller valuation than all remaining terms. Raising to a positive integer prime to p preserves valuation by the same binomial argument. Factor out the smaller power, and decompose |a-b| into its p-power and prime-to-p parts. This proves lteNorm and explains the stricter hypothesis at 2.

For any eigenvalue z, let a_e=(u^(p^j))^e and r_e=p^(j+c)|a_e z-1|_p. For units a,b, |a-b|_p<=max(|az-1|_p,|bz-1|_p): if |z|>=1 take the difference; if |z|<1 both right-hand norms equal 1. By lteNorm, |e-e'|_p<=max(r_e,r_e'). Thus the closed balls in Z_p centered at e of radius r_e have the finite intersection property: in any finite collection the center of the smallest radius lies in every ball. Z_p is compact, so choose a point s in ALL the balls. This is helly/ball, and yields
    p^(-j-c)|s-e|_p <= |a_e z-1|_p
for every integer e>=0. Crucially s is in Z_p even if z is in a nontrivial algebraic extension, or there is no exact root; it is not necessarily an exact logarithm or eigenvalue. One center per eigenvalue, multiplicity retained. Multiply norm inequalities at fixed j=j0 and reverse to valuations, including infinity (if a factor on right vanishes its left vanishes, so the corresponding center equals e):
    twLen(A,u,e,j0)<=sum_i (j0+c+v_p(s_i-e)).
Combine with growth:
    twLen(A,u,e,m)<=sum_i(max(m,j0)+c+v_p(s_i-e)).
If each |s_i-e|_p>=p^(-B), all valuations <=B and the source first ABound follows exactly, with R'=R and centers in Q_p:
    shaInv(L_m,p,e)<=R*(max(m,j0)+c+B).
No new assumption of eigenvector decomposition on X. The lift need not be unique; existence of a single fixed lift is sufficient.

Concrete illustration (not an arithmetic tower computation): p=3, u=4, X=Z_3, A=4^-2 (a p-adic unit), R=1, c=1, j0=3. Then g=4^(e-2); for e!=2 the quotient length is m+1+v_3(e-2), by the valuation formula, and at e=2 it is infinite. The center s=2 is exact in this scalar illustration. A general lifted matrix needs the compact-ball argument above rather than the assumption every center is an exact zero.

## 5. SecondBound and remaining dependencies

Apply the exact growth inequality to actual descent and choose a layer L2 of relative degree p^j0, which exists by section 1. It gives
    shaInv(L_m,p,e)<=shaInv(L2,p,e)+R*max(m-j0,0).
In the source Formalism/GaloisCohomology/Statement.lean, Sha2Zl is the locally trivial submodule of H2(zlTw D_source (e+1)), VLen is length of that entire H2, and PTShaAt states (under PTCase) length Sha2Zl=shaLen. L2 is totally complex because HasMuQ, so PTCase holds even at 2. With that EXACT limiting length identity, submodule inclusion gives shaInv(L2,p,e)<=VLen(D_source,e), proving SecondBound and hence ABound under IsTower and PTShaAt. No finiteness is needed to obtain this inequality. The original shaLeV invokes GlobalTheory.TateLimit.finite_level and ptShaAt from PoitouTateDuality, LocalFinitenessK and LocalTateDualityK. This reconstruction has NOT independently verified that finite-to-limit passage; the limiting PTShaAt identity remains an explicit dependency. Nor have we yet verified that the rank R of the actual arithmetic X exists uniformly for the varying two-prime base; the source's towerFixed, towerTwo, baseRk and twoBase are the next required arithmetic arguments. LemmaK and other-sign estimates remain separate. This is a conditional reconstruction of the genuine aBound_of_isTower spine, not complete independent discharge of all its source inputs. Original formal correspondence and Lean replay remain open.

Boundary: RH-A26-D05_TOWER_DESCENT_CENTRES_GROWTH_RECONSTRUCTED__LIMITING_PT_UNIFORM_TOWER_RANK_TWOBASE_LEMMAK_OTHER_SIGN_ORIGINAL_REPLAY_OPEN.
