# RH-A26 D05: invariant mean and invariant-form completeness

Conventional reconstruction, not certification or original Lean replay. Original publisher archive SHA256 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc. Paths relative to ReductionBoundsTorsion.

* MeanLatticeCounts/CountableLatS.lean: 19e9310d5a4d337914d96d02a2446b5b163ec803409911f9f66f8da1a4ab1cac
* PermutationSigns/FFTAsm.lean: 0dd80fa8167a387f3ff24bf963444246a9bb84b54687d8aaef98053ee8f57111
* PermutationSigns/PlacePermOperatorBicommutantSpan.lean: 837474b52b1a19cb24b92030c8df1ba824170a9088c4532f3a33bf6ba256f72f
* PermutationSigns/PlacePermOperatorCommutantSpan.lean: ddc759740298a622e02c6f8381110dea9e5f1f37f1a069b45a17a403e441c3f1
* PermutationSigns/BlkConjTranspose.lean: 61f4c39fce0818fa0009ec8d7e5be80a6223123a9c80b7e860d4257e25703195
* SmoothCompositionIdentity/MatOne.lean: a955a1d7ce302b67c9faa35171d784f379212d6b0f62cd42cb99b495d7b9cc5c
* PermutationSigns/SinvOfSwt.lean: 98b32abdfc3c5b7b47e14e451ac659b364f7efdcfc223449ab676bb39557c6e4

## SMean
Write A_g(H)=(g^-1)* H g^-1, so A_g A_h=A_gh. The frame is omega(A_g I) composed in every slot with A_g. On the product special linear group it is left invariant under latS by arithmetic invariance. Right multiplication by k commutes with left lattice action and preserves the two-sided Haar measure of Dom. Its preimage of the fundamental domain is another fundamental domain; integrate the invariant translated frame on either domain and change variables. Countability follows from finite rank of O_L. Integrability is a premise.

For a stabilizer u choose c_w^N=det u_w (N>=1); |c_w|=1. Then k_w=c_w^-1 u_w has determinant one and identical congruence action. Frame(gk)=frame(g) composed with A_u. Continuous linear slot composition commutes with Bochner integration, so normalized mean M is fixed. Every positive H=A_g I by square root factorization. Define bar omega(H)=M composed with A_(g^-1), zero outside the cone. If A_g I=A_h I, h^-1 g fixes I; thus choice independence, FInv and constant frame follow. No period preservation asserted by SMean.

## FFT
Let V be the direct sum over places of C^N, H=V^tensor q. Operators P_(sigma,w) have entry 1 when I has labels w and J=I composed with sigma. Their span A is unital, closed under multiplication and adjoint. Let B span the tensor powers of block unitary matrices; B commutes with A.

sw1: Hilbert-Schmidt projection P onto A commutes with left multiplication L_a because A and its orthogonal complement are left invariant (adjoint closure). Represent a linear map on matrices by blocks between column spaces. If it commutes with all L_a, each block commutes with A and hence with T in A''. Therefore P commutes with L_T. Evaluate at identity: P(T)=T, giving A''=A.

sw2: Z in A' has support only on I,J with equal place labels at every slot (commutation with label projections). Summing label-restricted permutations gives ordinary permutations, so coefficients are invariant under simultaneous slot permutation. Thus q! Z is the sum over I,J of Z_IJ times symmetrized tensors of matrix units E_(I_i,J_i), all nonzero terms block-compatible.

Let complex linear phi vanish on B. Diagonalize each Hermitian block by a unitary and vary the eigenvalues independently. The polynomial phi(D(z)^tensor q) has individual degrees at most q and vanishes on the product grid of (q+1)-st roots of unity; successive univariate root counting makes it identically zero. Evaluate at real eigenvalues. For arbitrary D=H+iK with H,K Hermitian, use the same argument on {0,...,q}^2 then evaluate at (1,i). Extract coefficient t_1...t_q of phi((sum t_i E_i)^tensor q): every symmetrized compatible tensor is annihilated. Repeated units retain factorial multiplicities. Hence phi(Z)=0, and finite-dimensional separation gives Z in B. Thus A'=B and B'=A; no stable range N>=q needed.

cplx: complexify the real Hermitian space via D=H+iK and extend real multilinear form complex multilinearly. Encode coefficients T_IJ on compatible matrix-unit tuples and zero elsewhere. Evaluation is sum T_IJ product of input entries I_i,J_i. Invariance extends by complex multilinearity. With this pairing the conjugated coefficient is D^transpose T conjugate(D); transpose permutes the unitary blocks bijectively. Uniqueness on compatible units implies T commutes with the block-unitary tensor powers, thus T in A.

fft_of: insert the permutation expansion of T into evaluation. Each permutation gives zero unless labels constant along cycles, else gives one trace of an ordered product per cycle. Take real part Re(c t)=Re(c)Re(t)-Im(c)Im(t); alternatize and divide by q! since beta is already alternating. This gives exactly AT spanning, not independence.

## AGood and SInv
At I use local positive Hermitian x and Q_x(Y)=xYx. Invariance gives omega(x^2) composed with Q_x in each slot = beta. Derivative of x->x^2 at I is twice identity; local inverse function theorem and smooth inversion of Q_x yield smoothness. Differentiating gives D omega_I[X](Y_1,...,Y_q)=-1/2 sum_i beta(...,XY_i+Y_iX,...). Exterior alternation kills each term because XY_i+Y_iX is symmetric in that pair. Transitivity and linear pullback transport closedness and smoothness to the cone; Stokes gives Good.

Padding inserts zero tangent blocks and identity metric complement, preserving trace factors. Replication by d multiplies every trace by d, hence weight d^j for j permutation cycles. Pullbacks along padding and replication are invariant by block congruence; identity values determine forms, so weights extend throughout the cone and to simplex integrals. One-cycle terms vanish in even degree q=k+1 by cyclic trace and odd sign of q-cycle. Group terms by j=2,...,q using same coefficients in every rank. Evaluations annihilate boundaries by Good, respect stabilization and scale by d^j under replication. For primitive z, SPsi gives two-block replicated cycle homologous to twice stabilized cycle. Thus (2^j-2)a_j(z)=0 and all evaluations vanish. Uses previously reconstructed SChain, SEv, SPsi, SStokes, classical calculus and finite-dimensional algebra; original formal replay open.

Next actual SPrime and final analytical join; averaging alone does not preserve periods. Geometry, stability, counting, torsion, foundational correspondence and original replay remain open.
