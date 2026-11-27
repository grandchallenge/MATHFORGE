# RH-A26 D05 — genuine Hecke spectral gap

Disposition: conventional reconstruction of the active SGap spine: Design, Hilb, Unfold, AEConst, Arith, Dens, GapAbs and sGap_of_parts under standard finite-dimensional field, number-field lattice and Haar-measure facts explicitly identified below. Retain source constants. This establishes the contraction with the actual Lz hypotheses and arithmetic coset operator, not the distinct SHecke detection or SLoc evaluation bound. No original Lean replay or certification.

## Source identity

Original publisher archive restored and independently hash-matched to the prior intake (tracker #577 recovery receipt 3fba3e86a56244c5aae25e82a96e348c; 64/64 earlier mirror blobs matched original bytes). The following SHA-256 hashes are from the restored original source, relative to Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion:
| File | SHA-256 |
|---|---|
| SBridgeAlt.lean | ab24a2e16c750c8bfbb20571b1995a9c91bf08d5e050fbdc3967aecbd7b0c481 |
| ActLPos.lean | 7e4840179da3ad19729771188ef5b90129d4821d36fb0fe637b939228c58f874 |
| ArithmeticGapBounds/AEConst.lean | be567b62cc8a307798e5b737f384a1927e106ebb7d02b6e2f0afd6a75b883abb |
| ArithmeticGapBounds/ClosureBound.lean | 3cfa9e418d286ceda1f6ccdf9d018a88fd7afa36a4b5f540721b0d55aebaac84 |
| ArithmeticGapBounds/PDesign.lean | c0fef0e55fb2693b08e59fcfa68e5c419702e0393505905bbd856d40c62a4246 |
| ArithmeticGapBounds/PGapAng.lean | bbe8968a7a6b2ed2e58756f867d78a0926bbc0536b9be7169657e3443606903f |
| ArithmeticGapBounds/PGapAbs.lean | 9084d0ad95d3ad3d6057213b0fc0e4568d51dcf3b5208bfaf543d3474b50565d |
| ArithmeticGapBounds/SGapOfParts.lean | 7481108591f9b4a5115bb39db992bc0428c80965293d3a20102e782228440b41 |
| ArithmeticGapBounds/SGapOf.lean | 0c42d4a3f8edc3d1e9432026cec1f26fb7ebbc49f2ff758863d443c1bbdd7071 |
| ArithmeticGapBounds/Arith.lean | 9d1947b01217da11e8317e09d9f099b5f9f415927c1dd775f6eb6734c35567a4 |
| ArithmeticGapBounds/PArith.lean | bd48240ad63b896bbcaa03c35e12036bf6d1eb94c7b5b194bd423ab6677fa654 |
| ArithmeticGapBounds/IntegralTransvectionMemSlIntegersConjugateZero.lean | 62a5d0c84291021b0e68471c3e274ea2f00acf8612e2563293a82492d64e97e9 |
| ArithmeticGapBounds/PDensM.lean | 77d3443f612ee1981b3b009bbe057aede11584062dc2e84a4a6e771d2742408a |
| ArithmeticGapBounds/PAEConst.lean | 76d90e55318fb3bc14b7b9f3ba6f53d8d70acb6ba6601f0db14579e71f0990e1 |
| ArithmeticGapBounds/PUnfold.lean | 8eb1b432dc5800a1bf6df410a808f50df1cc9b31987ff11aa3ee76369c55fca1 |
| ArithmeticGapBounds/PUnfoldA.lean | fff1ee69268e1f4699fd3095e0769240a53c2f7483963778eb5a8bfd6c9175ac |
| ArithmeticGapBounds/PUnfoldB.lean | 33e4858d5005223faad5fe4bfe6ab74d33da95ad0051dad5682948c997fd99b5 |
| ArithmeticGapBounds/AeEqCosetAvgOfMemInvariantSubspace.lean | 030a9567435e2bb444ad1d4fdebc306619dce00e5133db52c76cc1a3933eb677 |
| ArithmeticGapBounds/PGlueG.lean | 1bec3d120226e4d6abff7c0f0f63b71e53a5e431217db9a176953f4f359b9979 |
| ArithmeticGapBounds/PGlueM.lean | e7d052be1b5af6a73f5b0f8648474293bb7be0296fd2a064e00b4b8f19a29e0f |
| ArithmeticGapBounds/PGlueK.lean | ee28c77e25b231f6aa7e10743c10d022dd14e67e62356a2c25645afe79222879 |

## 1. The precise finite averaging lemma

Use source notation B=E intersect E' inside K, [K:B] finite, TwoTr(E,K) means all elements outside E constitute one E-double coset, and [E':B]>=25. The source average is over B\K, i.e. representatives with multiplication by B on the left. For fixed x and B-invariant functions on S, restrict to f(g)=a(j(g)x), h(g)=b(j(g)x). Both descend to the finite group K/core_K(B) because the core is a finite-index normal subgroup of K contained in B (kernel of the finite permutation action on cosets). The E and E' images have the same indices and TwoTr holds in the quotient. Thus normalized coset averages equal normalized finite group averages.

On this finite group G, let f be left E-invariant of mean zero, h left E'-invariant. For the unnormalized correlation c(s)=sum_g f(sg)f(g), c is E-biinvariant by change of variable. It is ||f||^2 on E and constant on G\E. Summing c over G gives (sum f)^2=0, hence that constant is nonpositive (if E=G the mean-zero f is zero). Projection P' onto left E'-invariant functions is averaging over E'; consequently
    ||P'f||^2 = <P'f,f> = |E'|^-1 sum_(s in E') c(s) <= [E':B]^-1 ||f||^2.
Since <f,h>=<P'f,h>, Cauchy-Schwarz gives the exact Design squared bound with 1/25. The same inequality holds for normalized averages. This reconstructs PDesign.core and design_holds, including nonnormal B. The finite group need not be simple, and the bound does not rely on independent random cosets.

## 2. Arithmetic geometry supplies Tri

Let O=O_L, pi a prime element, residue field F=O/(pi) of size Q>=25, N>=3. Use exactly K_r=D_r^-1 SL_N(O) D_r where D_r has pi in the first r diagonal entries and 1 elsewhere, r=0,1,2. Set B=K0 intersect K1 intersect K2, E01=K0 intersect K1, E02=K0 intersect K2, E12=K1 intersect K2. In K_r coordinates the conjugated principal congruence subgroup modulo pi^2 is contained in all K_s: each entry of the deviation from identity is multiplied by at worst pi^-2 under D_s D_r^-1 conjugation. Determinant 1 plus integral entries makes the inverse integral by adjugate. O/(pi^2) is finite, so all three indices [K_r:B] are finite.

Compute adjacent intersections directly from entry scaling. In K0 coordinates E01 is the preimage under reduction of the line stabilizer of the first coordinate; entries in column 0 away from row 0 are divisible by pi. In K1 coordinates E12 similarly stabilizes line 1. In K2 coordinates E12 stabilizes the hyperplane with coordinate 1 equal to zero, since row 1 off diagonal must be divisible by pi. Reduction SL_N(O)->SL_N(F) is onto: Gaussian elimination over a field expresses determinant-one matrices as products of elementary transvections (including the determinant-one diagonal and signed swaps), whose coefficients lift. SL_N(F) acts transitively on ordered pairs of distinct lines: choose basis vectors along the lines, extend to a basis, and adjust determinant by rescaling a basis vector without changing either line. The dual action gives the same property for hyperplanes. Thus each required stabilizer has exactly two double cosets, by transitivity of the stabilizer on the complement of its fixed point in the respective projective space. This proves two0,two1,two2 in Tri, with the orientations as in PArith.

For the lower index bounds consider the integral transvections t_10(a)=I+a E_10 in E02. Membership in K1 requires pi|a, so t_10(a)^-1 t_10(b)=t_10(b-a) is in B only if a=b mod pi. Distinct residues give distinct B cosets; hence [E02:B]>=Q. Likewise t_21(a) in E01 belongs to K2 only when pi|a, giving [E01:B]>=Q. This checks all Tri fields with the source's threshold 25. No use of strong approximation or uniform representation-theoretic gap is needed for these finite-index assertions.

## 3. Density of the generated arithmetic subgroups

The join K0 vee K1 contains all integral transvections, and t_0j(1/pi) for j!=0 by the scaled-entry criterion. A determinant-one signed permutation matrix in K0 conjugates these into t_ij(±1/pi) for arbitrary i!=j (the sign can be inverted). The transvection commutator identity [t_ik(a),t_kj(b)]=t_ij(ab) for distinct indices then proves inductively that all t_ij(a/pi^m) with a in O and m>=0 belong to the join. The extra index exists precisely because N>=3. This is a shorter conventional reconstruction of mem_sup with the same group and conclusion.

To prove density at all infinite places simultaneously, use the actual totally complex field hypothesis. The chosen complex embeddings identify O with a full real lattice in C^r2 (standard Minkowski embedding theorem). The lattice has bounded covering radius R. Since the nonunit pi has absolute norm >1, the product of the embedding moduli squared of pi is >1. For any epsilon>0, the centrally symmetric convex product of complex disks of radii epsilon |sigma_w(pi)|^m has volume tending to infinity with m. Minkowski's convex body theorem therefore gives a nonzero a in O such that q=a/pi^m has all complex moduli <epsilon. Approximate the vector of ratios z_w/sigma_w(q) by one integral element b with error <=R in every coordinate, and multiply by q. Then bq lies in O[1/pi] and approximates the arbitrary z to accuracy R epsilon. This verifies PDensM.dense_pow without assuming every embedding of pi has modulus >1. Continuity of each transvection in its coefficient shows that the closure of the actual image of K0 vee K1 under jS contains independently supported transvections at every complex place. Elementary generation of SL_N(C) at each place and the finite product prove Dens. These arguments use Minkowski lattice and convex-body results, not a new proof of those standard inputs.

## 4. The Hilbert inequality with exact source constants

Let W1,W2,W3 and K12,K13,K23 be the closed subspaces in Hilb. For each pair (Wa,Wb) with K contained in both, assume the specified 1/5 correlation when the first vector is orthogonal to K. Let P_i be orthogonal projection to W_i and Q_i=I-P_i. For x perpendicular to K, a=P_a x and b=P_b x, then a is orthogonal to K, so
    ||a+b||^2 <= (6/5)(||a||^2+||b||^2).
Also <x,a+b>=||a||^2+||b||^2. Cauchy-Schwarz and division only when the sum is nonzero give ||a||^2+||b||^2<=(6/5)||x||^2. Hence
    (4/5)||x||^2 <= ||Q_a x||^2+||Q_b x||^2.
For arbitrary x subtract its projection to K, leaving y orthogonal to K and the same Q_a,Q_b values. Let s=||Q_a y||^2+||Q_b y||^2 and T=Q_a+Q_b. Since <Ty,y>=s, nonnegativity of ||Ty-(4/5)y||^2 and the preceding inequality imply
    ||T x||^2 >= (4/5)s.
This is pair_all. Adding over three pairs and using ||u+v+w||^2=sum_pairs||u+v||^2-sum_i||u_i||^2 yields
    ||D x||^2 >= (3/5)<D x,x>,   D=Q1+Q2+Q3.
D is bounded positive self-adjoint, with ker D=W=W1 intersect W2 intersect W3. The Cauchy-Schwarz inequality for the positive semidefinite form <D x,y> follows by considering the discriminant of <D(x+t y),x+t y>. Applied to x,Dx it gives
    ||D x||^4 <= <D x,x><D(D x),D x>,
so the last bound implies <D y,y>>=(3/5)||y||^2 on the range of D (zero y harmless). The closure of the range is W-perp, by self-adjointness; continuity extends this bound there. This proves closure_bound without assuming a closed range or finite-dimensional space.

Now take v in W1 intersect W2, v perpendicular to W, w in W1 intersect W3. Subtract P_W w, retaining inner product and not increasing its norm. For nonzero v,w normalize to unit length, choose the sign of w so t=<v,w>>=0. Then for v+w in W-perp,
    (3/5)(2+2t) <= ||Q2 w||^2+||Q3 v||^2 <= 2(1-t^2).
The second inequality follows by projecting w to W2 and v to W3, since each contains the other unit vector. Divide by 2(1+t)>0 to obtain t<=2/5. Scale back. This proves exactly hilb_holds and its orientations (the opposite sign of a correlation is handled by absolute value). It is not an argument that all pairwise projections have norm <=2/5 including constants.

## 5. Measure and finite-index averaging

Use the exact GapAbs hypotheses: countable Lambda, injective j into a second-countable locally compact Hausdorff group S, left Haar measure, fundamental domains D_i of K_i, finite equal volumes of D0,D1 and finite B indices. We use the standard basic Haar measure facts (left invariance, regularity, local L1 translation continuity for locally integrable bounded functions, sigma-finiteness and nonsingularity of right translations) and the actual almost-everywhere fundamental-domain property. No lattice covolume theorem is required here because the domains are given.

For B<=K finite index, right coset representatives c for B\K give a B fundamental domain as the union of j(c)D_K up to null sets: the K translates of D_K partition S a.e., and the cosets partition K. Countability permits removal of exceptional null sets invariant under the countable subgroup. An invariant function has equal integral over any two fundamental domains of the same subgroup, by partitioning each by its intersections with the translates of the other and using left invariance (first nonnegative functions, then signed integrable functions). Hence measure multiplies by index, and integral over a B domain is index times integral of avg(B,K) over a K domain. Apply to |u| for integrability, u for signed integrals. Average is K-invariant by permutation of cosets under right multiplication, fixes K-invariant functions and is measurable as finite sum. The tower law follows by multiplying representatives for B\E and E\K, which gives representatives for B\K. This verifies Unfold. One can use any common B-domain DB.

Consider the Hilbert space L2(DB,mu) with representatives extended to S as B-invariant measurable functions on the conull B-translate partition, zero on the B-invariant exceptional null set. On this space P_E=avg(B,E) is a well-defined bounded orthogonal projection for B<=E<=K_i: Jensen and unfolding bound its norm by 1, its square equals itself, and for every E-invariant function v, unfolding the product gives <P_E f,v>=<f,v>. Any equality a.e. on DB between B-invariant functions spreads globally by countable translates. Thus W(E)=im P_E is precisely the closed subspace with E-invariant representatives, and its classes are invariant a.e. under E. This establishes the representative/projection content used in PGapAng. For a in W(E) orthogonal to W(K), replace its representative by the E-average minus the K-average; it is the same L2 class and has K-average pointwise zero. For b in W(E') choose an E'-invariant representative. Apply Design at every x, take square roots, integrate over DK using Cauchy-Schwarz, and unfold all three products to DB. The common finite index cancels. This is angle with factor 1/5 and exactly the pairs E01,E02 in K0, E12,E01 in K1, E12,E02 in K2.

For AEConst, a measurable u invariant a.e. under a dense subgroup is constant a.e. To justify extending the invariance to all of S, use bounded injective transform arctan u. On compact sets left translations are continuous in local L1, by approximation by compactly supported continuous functions using Haar regularity (nearby translates of a compact set lie in a fixed compact set). Second countability supplies sequences from the dense subgroup; invariance passes in L1 on every compact, hence a.e. globally by a countable compact exhaustion. Fubini on the sigma-finite product now gives for a.e. x, u(gx)=u(x) for a.e. g. Right translation by fixed x preserves the Haar null class, so choosing one such x proves a.e. constancy. This is a conventional proof of PAEConst's conclusion, not an assumption that a.e. invariance is pointwise or that the dense subgroup acts transitively.

## 6. GapAbs on the actual intersection spaces

Set W1=W(E01), W2=W(E02), W3=W(E12), K12=W(K0), K13=W(K1), K23=W(K2). The pairwise inclusions and angles are precisely those of section 5. The triple intersection consists only of constants: a representative is invariant a.e. under all Eij, and the group of translations under which it is invariant a.e. is a subgroup (Haar null sets are translation-invariant). By TwoTr and E02 not contained in B, E01 and E02 generate K0: take an element of E02 outside E01, and the single nontrivial E01-double coset covers every other element of K0. Likewise E12 and E01 generate K1 because [E01:B]>=25. Thus invariance extends to K0 vee K1, dense by hypothesis, and AEConst applies. Conversely constants are in each space since DB has finite volume. This explains why density is needed, not just the finite-group correlation.

For actual K1-invariant w of mean zero and finite squared integral on D1, let v=avg(E01,K0)w=P_K0 w (tower law). The unfolding identities show finite square integral and mean zero on D0. The DB volume computed via K0 and K1 gives equal indices [K0:B]=[K1:B]=n, since the given equal finite covolumes are positive (a countable union of null fundamental-domain translates cannot cover a nonzero Haar measure). Then on DB, v lies in W1 intersect W2 and is perpendicular to constants, w lies in W1 intersect W3, and
    <v,w>=||v||^2=n integral_D0 v^2,
    ||w||^2=n integral_D1 w^2.
Hilb yields ||v||^2<=(2/5)||v||||w||, so ||v||<=(2/5)||w|| (including zero v). Cancel n to get GapAbs exactly. This is not the weaker general Jensen bound of 1.

## 7. Glue to SGap: GL cosets, SL and scalar invariance

The source Lz(d,f) requires f continuous on Gp=product_w GL_N(C), invariant under GL_N(O) embedded diagonally through the complex places, invariant under all tuples of nonzero scalar matrices, square-integrable and mean zero on the supplied SL fundamental domain D0. It is not a statement for arbitrary L2 functions on all GL quotients. Let S=Sp=product_w SL_N(C), j=jS, qel=diag(pi,1,...,1). The actual Hecke subgroup Hq is {h in GL_N(O): qel h qel^-1 in GL_N(O)}, and Hecke average is over Hq\GL_N(O) of f(qel h x) with complex embeddings understood. For SL_N(O), intersection Hq equals E01 in K0 coordinates: conjugation preserves determinant 1. Every GL coset has an SL representative: given g, multiply on the left by diag(det g,1,...,1)^-1, whose inverse is a commuting integral unit diagonal in Hq. Two SL representatives have equal GL coset iff their quotient lies in the intersection. Thus exact coset bijection, preserving index and summands; finiteness already follows from Tri. No tacit replacement of GL by SL of equal cardinal.

For each D_r choose a complex scalar at every place whose Nth power is the inverse determinant of that embedded D_r. This makes q_r in S, with conjugation by q_r identical to conjugation by D_r. The image of K_r under j is exactly q_r^-1 latS q_r by the defining equation (converse follows by conjugating a diagonal embedded integral determinant-one matrix back using D_r over L; scalar cancels). Translate the given D0 by q_r^-1 on the left to get domains D_r' of equal volume, including r=2. Left Haar invariance gives exact integrals. Put w(x)=f(ofS(q_1 x)). It is K1-invariant, continuous, square-integrable and mean zero on D1', with the original norm. By scalar invariance, for x in S the actual Hecke average restricted to ofS(x) equals avg(E01,K0)w(x); the scalar determinant normalization is harmless only because Lz explicitly includes it. GapAbs applies. The finite Hecke sum is continuous and GL_N(O)-invariant by coset permutation; scalar invariance follows by centrality. It has finite square integral and mean zero by the equality just proved. Therefore SGap holds with squared contraction (2/5)^2, which implies the required (3/5)^2 bound exactly as in SGapOfParts. Iteration preserves Lz and gives (3/5)^r in the norm, or (3/5)^(2r) for squared integral. Source constants are retained, not optimized.

## 8. Remaining frontier and evidence qualification

The reconstructed SGap is the actual arithmetic contraction, not an appeal to general property T or a spectral gap for a different space. Classical field elementary generation, Minkowski and Haar/functional analysis facts above are explicit; formal correspondence and original Lean replay remain separate. SHecke is logically distinct: exponential decay of Hecke-transformed cycle evaluations does not by itself imply that the original evaluation is zero. The source invokes actual affine-stabilizer vanishing, transfer, finite-dimensional cycle representatives and a module-ideal argument in HeckeDoubleCosets/Assemble.lean; these must be independently checked. SLoc must then prove a cycle evaluation bound from a bulk L2 norm, with genuine compact-local averaging, not a pointwise estimate inferred from L2. Height moments, Whitney form construction, scalar averaging, invariant extension and stability remain as in #622.

Boundary: RH-A26-D05_SGAP_ARITHMETIC_CONTRACTION_RECONSTRUCTED__SHECKE_DETECTION_SLOC_HEIGHT_FORM_STABILITY_COUNTING_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
