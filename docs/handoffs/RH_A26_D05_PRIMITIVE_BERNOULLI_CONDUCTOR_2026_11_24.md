# RH-A26 D05: denominator integrality and exact conductor cost

**Status:** independent conventional reconstruction of a bounded arithmetic bridge, conditional on classical von Staudt–Clausen and standard finite character facts. The primitive cohomological estimate, reciprocity/counting argument, original Lean replay and RH/GRH certification are not established here.

## Source lock and precise object

Original archive source paths relative to Development/AutomorphicArithmetic/AutomorphicVarieties (read directly from the pinned intake):

| Module | SHA-256 |
|---|---|
| GaloisLibrary/BernoulliNumbers/MapGenBChar.lean | 7a84fd98752f7b2a310001da8a8f3dcb7447f967173d5bbdf28f3025d6a51129 |
| GaloisLibrary/BernoulliNumbers/Primden.lean | 908554912d2c6e16f0df3604f421e8d4dcf5ff033b7faf5875dfd430f1eeeec0 |
| GaloisLibrary/BernoulliNumbers/Expand.lean | 0bbcc6cbd49d7958fd443912d61bbcc660c81d58b8eab388092bb2f917d775cd |
| GaloisLibrary/BernoulliNumbers/Denint.lean | 9854cb7efb2841b72c28904265312ecfffbef5918bb1de018be4f40f64578481 |
| GaloisLibrary/BernoulliNumbers/Denchar.lean | 34953f42fd63bdf843c2f330c712130bb4121cb899693963388f0793f79f3a8f |
| GaloisLibrary/BernoulliNumbers/Primval.lean | a333dee424f27644559f91cf719885b99523a3fee2c906e5b3cd80bc1e75ab0a |
| GaloisLibrary/BernoulliNumbers/Primmem.lean | f206e63e6cfeae49b78199277978f4d4de8784b59913bbcb0ada4a70fc5188d4 |
| GaloisLibrary/BernoulliNumbers/Primeq.lean | ffc1b77e9b05e45e10ea1b8e55306e2fde9c5749a0bc9b7f06bbee96ed24bbc1 |
| OddResidueBounds/ZeroMemUnrHom.lean | c6cac1eefc91d4bf1972ae1b8ccc54ab3ce3238e19e397dafb49bb739bcecf48 |
| PrimitiveFrobeniusFixed/PrimCase.lean | 7a267aaec723dbe9b97c01e9d92e35756f1d63e02fef2b8a5ead2ce9983b0ab3 |

The exact source quantity alN(k,chi) is den(N,k) times Bprim(k,chi), **not** the generalized Bernoulli sum at the ambient modulus N. Here Bprim is computed at the conductor of chi.

## Independent arithmetic argument

Write P_k for the product of primes at most k+1, d(N,k)=N P_k, and use the convention B_1=-1/2. For 0<=j<=k, P_k B_j is an integer: B_0=1, the B_1 denominator is 2, odd indices j>1 vanish, and for positive even j the von Staudt–Clausen theorem gives squarefree denominator consisting precisely of primes p with p-1 dividing j. Each such p is at most j+1. The j=0 case is dealt with separately.

The polynomial identity B_k(x)=sum_{j=0}^k binom(k,j) B_j x^(k-j) therefore gives, for N>0 and any integer a,

    d(N,k) N^(k-1) B_k(a/N)
      = sum_{j=0}^k binom(k,j) (P_k B_j) N^j a^(k-j) in Z.

This proves coefficient integrality independently, including k=0. Consequently, for any Q-algebra R and subring A containing the values of a function Phi on Z/NZ, the scaled sum d(N,k) genB(k,Phi) lies in A. This uses integer coefficients, not an assumption that A contains all rationals.

For a Dirichlet character, each unit value is a root of unity by the finite order of the input, and nonunit values are zero. Hence character values are integral over Z; the scaled sum is integral over Z. If f is the conductor and phi its primitive character, reduction (Z/NZ)^* -> (Z/fZ)^* is surjective: lift each unit residue at f and impose residue 1 at prime powers in N supported outside f, using CRT. On the remaining prime powers any lift is already a unit. Thus every primitive-character value is zero or an ambient unit-character value. Applying the coefficient lemma at f proves membership of the primitive scaled sum in any such subring A; membership in a Q-subalgebra before scaling is immediate from rational coefficients. This reconstructs the mathematical content of b_primval, b_denchar, b_primmem and b_denint, with standard primitive-character uniqueness imported.

For N a multiple of f, induction from phi to level N preserves the primitive character (by uniqueness of the minimal conductor and injectivity of unit-character pullback). Consequently

    A_f = d(f,k) B_{k,phi},
    A_N = d(N,k) B_{k,phi} = (N/f) A_f.

This reconstructs b_primeq and den_dvd and the arithmetic part of lev_case. In a DVR O finite over Z_l, containing these scaled quantities, normalize v_O by a uniformizer, and let r=v_O(l)>0. For A_f nonzero, exactly

    v_O(A_N) = v_O(A_f) + r v_l(N/f).

For A_f=0 both sides have infinite valuation in the extended convention. The equality follows from the valuation product law and the fact that integers prime to l are units. In particular there is **no additional valuation cost** at l for a prime-to-l change of modulus; otherwise the added cost is explicit and nonnegative. This is sharper bookkeeping than the divisibility inequality alone. The equality does not identify the two ordinary imprimitive sums.

The cohomological side of lev_case is unchanged by the level change if the standard cyclotomic action compatibility and exact character pullback are in force: reduction of cyclotomic actions makes dirG of the induced character equal dirG of phi. Order and parity are preserved by surjective pullback. Therefore, under the original primitive estimate and source coefficient/Galois hypotheses, L <= v_O(A_f) implies L <= v_O(A_N). No assumption about the primitive estimate's truth is smuggled into this implication.

## Exact example and regression

The quadratic character modulo 5 gives B_(2,phi)=4/5. Inducing it to modulus 10 retains that primitive value, but its ordinary level-10 generalized sum is 12/5. With P_2=6, A_5=24 and A_10=48. At l=3 the valuations are both 1; at l=2 they differ by 1 (this is a denominator example, not an application of vChar, which excludes 2). Confusing genB at level 10 with Bprim would give 144 instead of 48.

The GitHub-fetched independent rational Python fixture tests/rh_a26_primitive_bernoulli_exact.py (SHA-256 9e60c8ccf3cc33cc91f2310a8dd0391ac11eb5a549de585b00968f7308fcc145) passed 5,100 coefficients for N=1..24,k=0..16,a=1..N; 192 scaling cases for four real primitive characters (conductors 4,5,8,12), k=1..8 and six level multiples; 576 nonzero valuation checks over six primes; plus the imprimitive negative control. CHAD local receipt 11d0b7836c7c4510a6f64a2e29511ba1. Separate symbolic-engine checks passed the 5,100 coefficients and 192 scaling cases. These are exact bounded regressions; the general proof is the preceding argument.

## Remaining primitive estimate

The actual source theorem ML.vChar assumes Rec, and prim_case splits into a noncyclotomic unit-difference branch and an exceptional branch. In the first branch it uses zEval (ZeNorm.lean, SHA f6bb5faff7c24c765cefd6d64f469ebdef9f7107cd1638043ed79ed55a01b658): for each nonzero a0 obtain z=zVal satisfying a0*z | l^m and z | A_f. Then count (FrobFix.lean, SHA 6183defac979c455b2bfd61358107bccb9515cb1e973e274691da656fe9247a1) under Rec bounds length ShT(a0) by v(z). The transfer shaToShT (SHA 70b3de3374bda1e2cdfd223e5f1d6981f42001ed015ccb557bd4cd5e65e38ef5) passes uniform bounds on torsion layers to full ShaU. The argument requires actual zEval and count, not just divisibility or conductor scaling. Rec is defined in IsAdmissiblePrimeListNil.lean (SHA 4a5b83a90871ef58923fddc1c12ae6d3f5ddff7339747c1493a1dd17c758f433): the local product y*c(g)=0 for paired cocycles under the stated torsion, local, and trivial-action hypotheses; ML.recip in OverIff.lean (SHA 189230817c6416180d71e7e0fbc7fba7568ad1f8d46709f06003f5c3fe97df28) derives it from PoitouTateDuality and UnramifiedOrthogonality. None of those genuine arithmetic inputs has been independently established here.

Next: reconstruct the uniform torsion-layer transfer including normalized local coboundary witnesses in shaToShT, then the counting induction and actual zEval divisibility witnesses, and audit the reciprocity input. No certification or protected RH status change.

Boundary: RH-A26-D05_PRIMITIVE_BERNOULLI_DENOMINATOR_AND_CONDUCTOR_COST_RECONSTRUCTED__PRIMITIVE_SHA_COUNT_ZEVAL_REC_AND_ORIGINAL_LEAN_REPLAY_OPEN.
