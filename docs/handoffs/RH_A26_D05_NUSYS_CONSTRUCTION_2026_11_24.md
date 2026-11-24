# RH-A26 D05 — independent construction of the NuSys auxiliary system

**Disposition:** conventional independent reconstruction of the actual NuSysEx theorem using explicitly imported classical cyclotomic number-field, class-field and local-field facts. No assumed Lax, Sys, IsKol, NuSys, Stickelberger ideal formula or Jacobi-sum congruence. Original Lean replay, exact correspondence of the classical imported facts, zEval and exc remain open. This is not RH/GRH certification.

## Source lock

Original pinned lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed:

| File | SHA-256 |
|---|---|
| NuSysEx.lean | 07dca756b6ecc3dfe57c1dad484f793ded486c1c57bd3b559007509bc41b26d9 |
| IsAdmissiblePrimeListNil.lean | 4a5b83a90871ef58923fddc1c12ae6d3f5ddff7339747c1493a1dd17c758f433 |
| PlaceEmb.lean | 109fbbd41beaa8d376b4259288cddda1af3d161c636af9f31b6230f9e4d23f27 |
| SysOfLax.lean | 37ebc14eb6194a8f722f2f5988cd0ed5e9029d2c63a80518c81390c3ed15e706 |
| DerInv.lean | dda5d346871faedfc321f3fcfbc032afd5c2bc8a6e76784bfd0503dbfe236029 |
| DerBasic.lean | 305ac0c88a20cb35cf72ee8088659c9671246edebed4664bc1f30afbc01544ca |
| KolEx.lean | 329f31dd00cc1136883c33f94bcc52fc7262203f08b9d10384553c3a1ddae9ff |
| KolHom.lean | c590117c05f769e1a0cbbd64a7fd0f7cd7177724d7e7719df427a749b2efd960 |
| KolUnr.lean | 3c9abd228f5339d61a0e27db0a75365b715608800b5a195d08c36a2da7f89ca4 |
| KolStep.lean | a98bff8d384d7d8aa9525e8c9883e49ef21c9a2b0f838c2a12c562900689795c |
| KolInit.lean | 1c747661b41a2ee66223e17aadeccf8ceb624969d33bb5549de4d590be47a414 |
| ValAddSmul.lean | de8fedae9ecd5719ecf1474f97420c91e0ba0017fb07714e5073de9ef8fdf915 |
| XEx.lean | e1eb33d466a49338f56581ae7675b181b356714ed5a742163a78b4dba6b664b0 |
| XJacPowNe.lean | 3c5a12192b5ce7cf55710cb0aef8ea161461807d6836e95dbded58b8b978b340 |
| XNormDiv.lean | 90ae52d2215b9998c27f01612034fcae133222ee631d6b463e90c1fb2cae11cc |
| AlgStep.lean | ab586357c47d24f6ec007cfdedc4ce3154e448937e0af2f40bf7678a6c71936f |
| ThDist.lean | ab995b9f9f0dff2511f4169fdbf5711545d13127229a4abdbee923a692836058 |
| XCongJac.lean | 5dd01f2b1c786fc6e545be343113d216d656db973ef6e346989ad5bdb7360199 |
| XCongPrin.lean | f1343a22f211a1cda899875991fc6f5fb40e54b1cc05004dd723282e40f951c8 |
| XUniqConj.lean | 68ed01a1174ee1062dd998f3b6fc6547f5a3b9dd15356954784c70c35936c65e |
| IneTau.lean | 25a386d960bca196db6ee3b2a0456cf8132a3357362c0ba66125c3370c733c74 |
| IneRad.lean | 4689706ad55c54dcc30efdfe1b5c2c48ac04805aa5352a6785aaf9bc34c12b08 |
| HasOrdP.lean | c356bf5e9b71feca85c282b8a9b0768aecff3a38d7dd5cc9675704afafb3859a |
| ZSumPKey.lean | a7f3d4d6510effd8e668ce7e277de7196eb663e6ae6a4192de4baeba80fe1fec |

## 1. Exact theorem and imported foundations

Put M=l^m, F=N0 M with l odd, m>=1 and gcd(N0,l)=1. Work in the same algebraic closure Omega of Q. K_H=Q(mu_H), G=Gal(Omega/Q), U=Gal(Omega/K_F). The given Dat character alpha is trivial modulo M on U, odd modulo M, and differs by a unit from the cyclotomic character chi_l at some delta. Let beta=chi_l/alpha. Given r prime, r=1 mod F, b<F, a place A0 above r, lifts sigma_t of t in (Z/F)^*, and w in QO[M], the target is a family nu_L for every distinct-prime admissible list L with:
- additive, locally constant restriction to U, beta-equivariant for G conjugation, M-torsion, inertia-zero outside F*r*prod L;
- at each admissible q::L, any place over q and Frobenius phi, some inertia t and unit u satisfy nu_(q::L)(t)=u nu_L(phi);
- at A0, some inertia t and unit u satisfy nu_empty(t)=u zVal(alpha,sigma,b) w.

We import: cyclotomic Galois group and roots-of-unity structure (roots of unity in K_H have order dividing 2H); Dedekind ideal theory, ideal norm and decomposition/residue-degree laws; existence of degree-one primes in every ideal class outside finite sets (Hilbert class field and Chebotarev); finite-field multiplicative cyclicity; place restriction/conjugacy, inertia surjectivity to finite local extensions, Frobenius on residue fields, cyclotomic unramifiedness away from level, total ramification of Q_q(mu_q), and Hensel/Eisenstein over finite unramified extensions. We use Kronecker's algebraic-integer unit-circle theorem, which follows by bounded conjugate coefficients of all powers. These are conventional theorems, not asserted independently Lean-checked here. The following actual construction does not import the target auxiliary system or its key intermediate contracts.

## 2. Jacobi sums give the precise fractional ideals

For a level H write T_H(t)=floor(b*[t]/H)-floor(b*[-t]/H) on units, with [ ] least residues. Put theta_H=sum T_H(t) sigma_t^{-1} acting multiplicatively on ideals/elements. Thus the source conjI is the inverse conjugate prime. IsX(H,I,X) is (X)=I^theta_H and X bar(X)=1.

First choose a degree-one prime P outside H in K_H; its rational prime p is split completely, p=1 mod H, and reduction at P identifies mu_H with the subgroup of order H in F_p^*. Let eta on F_p^* be the lift of x^((p-1)/H) to mu_H, and set it to zero at 0. For 1<=j<b<H put J_j=sum_x eta(x) eta(1-x)^j, with the power character extended by zero. All three characters eta, eta^j, eta^(j+1) are nontrivial. Standard Gauss-sum computation, briefly: |G(psi)|^2=p by summing over the ratio of two nonzero variables; the sum over x+y=s for s!=0 gives G(eta)G(eta^j)=J_j G(eta^(j+1)), with the s=0 contribution zero by nontriviality. Hence J_j bar(J_j)=p. In particular J_j is nonzero integral and its ideal divides (p).

At sigma_t^{-1} P reduce sigma_t J_j modulo P. The sum becomes sum_x x^A(1-x)^B with A=((p-1)/H)[t], B=((p-1)/H)[jt], both strictly between 0 and p-1. Expanding by the binomial theorem, the only possible nonzero power sum is exponent p-1, since A+B<2(p-1). Its coefficient, if A+B>=p-1, is a nonzero binomial coefficient modulo p (0<=p-1-A<=B<p). Therefore J_j has exponent 1 at this prime precisely when [t]+[jt]<H, and exponent 0 otherwise, because p splits with exponent one. The carry is floor((j+1)[t]/H)-floor(j[t]/H). Summing over j=1..b-1, the exponent of J=prod J_j is b-1-floor(b[t]/H) for b>=1. Thus X=bar(J)/J has precisely T_H(t) as exponent and X bar(X)=1. For b=0 the empty product gives X=1, and for b=1 T_H=0. This reconstructs xJac by finite-field sums and not by assuming an ideal factorization theorem for the Jacobi ratios.

For an arbitrary nonzero integral ideal I, choose degree-one P of class [I]^{-1} outside H and any specified finite primes; let IP=(y). Define X_I=y^theta_H/X_P. Since T_H(-t)=-T_H(t), y^theta_H has complex-conjugate product 1; its ideal is (IP)^theta_H, so X_I satisfies both IsX identities. This is xEx.

If X,X' both satisfy IsX for the same I, X'/X is an algebraic unit with conjugate product 1; every complex embedding commutes with conjugation, so all its complex absolute values are 1. Kronecker and the cyclotomic root-of-unity theorem give (X'/X)^(2H)=1. This ambiguity is the only one. Multiplication/division and raising to powers transfer IsX as dictated by ideal multiplication.

## 3. Norm and congruence across a new prime

Let q prime coprime H, 0<=b<min(H,q), L=K_(Hq), K=K_H. Define f_H(t)=floor(b[t]/H). For unit t mod H, its q lifts are [t]+jH, 0<=j<q. If b>0, multiplying j by b permutes residues modulo q, so summing floors gives
    sum_j floor(b([t]+jH)/(Hq)) = (b-1)(q-1)/2 + f_H(t).
Exactly one lift is divisible by q; it is q*[q^{-1}t]_H, contributing f_H(q^{-1}t). Subtract the analogous formula for -t; the constant cancels, giving the exact distribution of T:
    sum_{t' unit, t'->t} T_(Hq)(t') = T_H(t)-T_H(q^{-1}t).
For b=0 both sides vanish. This proves thDist directly.

Let I' be an ideal of L, I=Norm(I'), and X',X their respective IsX elements. Ideal norm commutes with Galois restriction; the distribution formula identifies the ideal of Norm(X') with that of X/sigma_q^{-1}X. Both are norm-one under complex conjugation. By uniqueness,
    Norm(X') = epsilon * X/sigma_q^{-1}X, epsilon^(2H)=1.
This is xNormDiv, including the direction of the inverse automorphism.

Assume I' prime to q. We show X' congruent to a single root-of-unity multiple of sigma_q^{-1}X at EVERY prime above q, not a separately chosen root at each place.

First take P' degree one above rational p outside Hq. Its lower prime P has residue degree one, so Norm(P')=P. For compatible Teichmueller characters eta' at Hq and eta at H, eta'^q=eta by reduction at P' and injectivity on roots of unity prime to p. At any place over q, reduction of eta' equals reduction of sigma_q^{-1}eta: raising to q agrees, and Frobenius is injective in the residue field. This holds pointwise on F_p including zero. It follows for each Jacobi sum, then the products and conjugates (conjugation of characters is inversion, respecting this same congruence). Their quotients are defined modulo q since their Jacobi sum norms divide powers of p, not q. Canonical Jacobi ratios at the two levels therefore satisfy X' congruent sigma_q^{-1} X at every place over q. Arbitrary choices differ by globally defined roots of unity at their levels. Thus xCongJac holds with one global epsilon in mu_(2Hq).

Next take a principal ideal (y) prime to q in L. At a place above q, the automorphisms above a fixed t mod H induce the same reduction on y because Gal(L/K) is inertia there. Write v_t for that reduction of sigma_t^{-1}y, which is nonzero. The principal theta product in L reduces to prod v_t^(T_H(t)-T_H(q^{-1}t)). The principal theta product of Norm(y), after sigma_q^{-1}, reduces to prod v_(qt)^((q-1)T_H(t)), since the relative norm is the product of q-1 inertia conjugates. Frobenius gives v_(qt)^q=v_t: a lift of sigma_q in the decomposition group acts by q-power on the residue field (its relative inertia factor does not matter). Consequently the latter product is prod (v_t/v_(qt))^T_H(t), the same product by reindexing. This proves xCongPrin at all q places with no root ambiguity.

For general I', choose degree-one P' in inverse class avoiding Hq and let I'P'=(y). Both I' and P' are prime to q, hence y and all theta factors are q-units. Apply the principal relation to (y) and the degree-one relation to P'; divide. Choices differ only by a single global root of unity, so X' congruent epsilon sigma_q^{-1}X at every q place, epsilon^(2Hq)=1. This reconstructs xCong, not just its norm implication.

## 4. Genuine Lax and exact Sys

For every nonzero squarefree admissible d choose the prime P_d of K_(Fd) given by restriction of the SAME A0 over r, and choose X_d satisfying IsX(Fd,P_d,X_d). This requires no consistency assumption on the chosen generators. The support is entirely over r, X_d!=0 and it is a unit at all places not over r. At d=1, r splits completely, so normalized additive valuation of sigma_t X_1 at A0 divided by that of r equals T_F(t). This is precisely HasOrd.

For an admissible extension q*d, relative norm P_(qd) is P_d^s with s the residue degree, which divides ord_(Fqd)(r). This order is l-prime: r=1 mod F, all primes dividing d*q have l-prime orders of r, and CRT gives the least common multiple. Also q prime to F*d and r, q>F>b. The preceding norm/congruence applied with X_d^s gives
    N_q X_(qd) = epsilon (X_d/phi^{-1}X_d)^s,
    X_(qd) congruent epsilon' (phi^{-1}X_d)^s at every q place.
Here N_q is over the q-1 conjugates generated by tau_q, phi acts by q on mu_(Fd), and the two roots may differ but have orders dividing 2Fqd. This constructs actual Lax and HasOrd simultaneously for ALL admissible indices; choose any values on irrelevant indices.

Let delta be the Dat.notCyc witness and a the integer residue of chi_l(delta) mod M. Define P(x)=delta(x)/x^a, x_d=P(X_d)^(2N0 d), and c(d,q)=q*s(d,q). P is multiplicative and kills mu_M, and raising an element of mu_(2Fqd) to 2N0 qd puts it in mu_M. On the cyclotomic fields G acts abelianly, so P commutes with Galois actions there. Applying P and raising the lax norm identity to 2N0 qd removes epsilon exactly. Applying P to the lax congruence is legitimate at every q-place because the congruence holds at every conjugate place and all terms are units; products, inverses and powers preserve equality in the residue field. The root epsilon' also disappears. Hence
    N_q x_(qd) = (x_d/phi^{-1}x_d)^c(d,q),
    x_(qd) congruent (phi^{-1}x_d)^c(d,q) at all q places.
The exponent c(d,q) is l-prime (q=1 mod F, s l-prime). All nonzero/fixed/unit properties survive. This proves the actual Sys contract of sysOfLax, including the changed exponent q*s. No root choice across levels is needed.

## 5. Derivatives and existence of Kolyvagin classes

For every q choose tau_q acting by a generator on mu_q and trivially on all roots of unity of orders coprime to q. In fact any lift from absolute inertia at a q-place of a generator of Gal(Q_q(mu_q)/Q_q) works, by cyclotomic unramifiedness of all other roots. At every q-place one can choose t in inertia inducing this same generator on mu_q. These facts follow from the stated local total ramification and inertia surjectivity.

In multiplicative group-ring notation D_q=prod_{i=0}^{q-2} tau_q^i(.)^i and N_q=prod_{i=0}^{q-2} tau_q^i(.). On K_(Fdq), tau_q^(q-1)=1. Hence by shifting the index,
    tau_q D_q(v)/D_q(v) = v^(q-1)/N_q(v).
The D operators commute, are multiplicative, preserve nonzero elements and units away from r, and commute with G on each cyclotomic field. For L with d=prod L let Y_L=D_L(x_d), D_L the product/composition. We prove its class mod M-th powers is U-invariant IN K_(Fd), not merely in Omega.

Base L empty: Y=x_1 belongs to K_F, fixed by U. For q added to L, put W=D_L(x_(qd)), Y=Y_L, c=c(d,q). Then N_q W=(Y/phi^{-1}Y)^c. Because q=1 mod F, phi^{-1} lies in U. By induction choose Z in K_(Fd) with Z^M=phi^{-1}Y/Y. Put k=(q-1)/M. Then
    tau_q Y_(q::L)/Y_(q::L) = (W^k Z^c)^M.
For every q in a list we can reorder its commuting D factors and use the induction on the shortened list. The quotient U/G_{K_(Fd)} is prod_{q|d}(Z/q)^*, generated by the tau_q. The property gY_L/Y_L in K_(Fd)^{*M} is closed under multiplication, since (ghY/Y)=(g(hY/Y))(gY/Y), and holds trivially for the kernel. Thus it holds for ALL g in U, proving derInv. This is the crucial descent into the SAME finite field.

Fix a primitive M-th root zeta. Choose B_L in Omega with B_L^M=Y_L. For g in U choose Z_g in K_(Fd) with Z_g^M=gY_L/Y_L. Define kappa_L by
    zeta^kappa_L(g) = g P(B_L)/(P(B_L) P(Z_g)).
Raising the right side to M gives 1 since P commutes with g on K_(Fd). P kills mu_M, so the definition is independent of the choices of B_L and Z_g, even of arbitrary roots for the latter. For u,v in U, use Z_(uv)=u Z_v Z_u and P(u Z_v)=u P(Z_v); since U fixes mu_M, this yields kappa_L(uv)=kappa_L(u)+kappa_L(v). Its kernel contains the open subgroup fixing K_(Fd) and P(B_L), so it is locally constant. Extend arbitrarily outside U; only specified arguments will be used. This reconstructs kolEx and kolHom.

At a place outside F*r*d, inertia fixes K_(Fd) and mu_M. The element P(B_L) is a unit there, since Y_L and all its conjugates are units. For inertia g choose Z_g=1; the ratio gP(B_L)/P(B_L) is an M-th root reducing to 1. Reduction on mu_M is injective in residue characteristic prime to M, hence kappa_L(g)=0. This is kolUnr.

## 6. Local step: the genuine relation, including sign

For admissible q::L, fix an arbitrary q-place A and Frobenius phi. Use t in inertia inducing tau_q on mu_q, so t agrees with tau_q on K_(Fdq) (both fix K_(Fd)). Let Y=Y_L, W=D_L(x_(qd)), c=c(d,q), k=(q-1)/M, B^M=D_q W, C^M=Y. The exact Sys and derivative identities give N_q W=(Y/phi^{-1}Y)^c and W congruent (phi^{-1}Y)^c at all q places: applying D_L to the congruence is valid at each conjugate place. Choose Z^M=phi^{-1}Y/Y in K_(Fd); then (W^k Z^c)^M=t(D_q W)/(D_q W).

Write A1=P(B), C1=P(C), V=phi^{-1}C1, R=W/(phi^{-1}Y)^c. They are units at the chosen q-place, and R reduces to 1 at all q places. Then P(R) also reduces to 1. The defining identities are
    zeta^kappa_new(t) = (t A1/A1)/(P(W)^k P(Z)^c),
    zeta^kappa_old(phi^{-1}) = V/(C1 P(Z)).
Using V^M=P(phi^{-1}Y) (commutation on K_(Fd)) and q=1+Mk, divide the first by the c-th power of the second:
    zeta^(kappa_new(t)-c kappa_old(phi^{-1}))
       = (t A1/A1) * (C1/V^q)^c / P(R)^k.
Every factor on the right reduces to 1: inertia for the first, Frobenius applied to V for the second, and Sys congruence at conjugate places for the third. The left is in mu_M and reduction injective. Therefore kappa_new(t)=c kappa_old(phi^{-1})=-c kappa_old(phi) mod M. This gives the actual kolStep equation for every q-place and every Frobenius, with the same c independent of the place. No need to invoke the source kolStep as a premise.

## 7. Initial valuation and the weighted character sum

At r, r prime to F and M; inertia in the local extension adjoining an M-th root rho of r realizes rho->zeta rho. Indeed over the finite unramified local extension containing mu_M, the polynomial X^M-r is Eisenstein and the resulting cyclic extension of degree M is totally ramified. Extend its automorphism to absolute inertia. This establishes the needed ineRad case; no incompatible simultaneous inertia choices.

At the empty list, Y=x_1 and P(Y) has normalized valuations
    h(t)=2N0 (T_F(t d0^2)-2a T_F(t d0)+a^2 T_F(t)),
where d0 is the cyclotomic action of delta on mu_F. This follows by applying P twice to the known valuations of X_1 and using commutation, exactly as in HasOrdP. For B^M=Y, put E=sigma_t P(B). Its M-th power is sigma_t P(Y). Thus E/rho^h(t) is a unit at A0, with M-th power fixed by inertia. The ratio of its inertia conjugate to itself is in mu_M, reduces to 1 and is therefore 1. Hence
    t0 E/E=zeta^h(t).
Conjugating the defining kappa identity (sigma_t^{-1} t0 sigma_t fixes K_F, so choose Z=1) yields
    t * kappa_empty(sigma_t^{-1} t0 sigma_t)=h(t) mod M.
This holds even for negative h(t).

Finally define the actual family
    nu_L(g)=sum_t kappa_L(sigma_t^{-1} g sigma_t) beta(sigma_t) w.
All scalars from Z/M act on the M-killed element w. Beta is 1 modulo M on U since both chi_l and alpha are. Reindexing under G/U proves beta-equivariance: the difference between lifts sigma_(bt) and g sigma_t is in U, which acts trivially on w and by inner conjugation on the additive homomorphism kappa. Finite sums preserve additivity/local constancy and M-torsion; conjugate inertia retains the underlying rational place, so every summand vanishes outside F*r*d. These are all five IsNu fields.

For step at q, conjugate chosen inertia t and phi by sigma_t indices. Cyclotomic actions commute, hence each conjugated inertia element still agrees with tau_q on mu_q, and it belongs to inertia of the corresponding conjugate place; the conjugated Frobenius is Frobenius there. The local step in section 6 holds for every summand with the same coefficient -c. Thus nu_new(t)=-c nu_old(phi), with -c a unit of O. This proves the full NuSys.step condition.

For the initial value use beta(sigma_t)=chi_l(sigma_t)/alpha(sigma_t) and chi_l(sigma_t)=t mod M. Therefore the previous initial congruence gives
    nu_empty(t0)=sum_t h(t) alpha(sigma_t)^(-1) w.
Define Z(f)=sum_t f(t) alpha(sigma_t)^(-1). Modulo M, alpha factors through the finite unit group, so reindexing t->td0 gives Z(f(.d0))=alpha(delta) Z(f) mod M. Applying the operator twice,
    Z(h)=2N0 (alpha(delta)-a)^2 Z(T_F) mod M.
The first factor is a unit because l odd and N0 prime to l. The second is a unit because alpha(delta)-chi_l(delta) is a unit and chi_l(delta)-a is divisible by M in the maximal ideal. Since Mw=0, this proves
    nu_empty(t0)=u0 zVal(alpha,sigma,b) w,
    u0=2N0 (alpha(delta)-a)^2 in O^*.
This proves NuSys.init. It also explains why the *second* application of P is present: the first makes the norm-compatible system, and the second occurs in extracting the Kolyvagin class. Omitting it would change the initial scalar.

Together sections 2–7 give the actual source theorem NuSysEx under the stated imported classical number-theoretic foundations. No bound on Sha, existence of NuSys, or the Bernoulli zEval result was assumed. The target is not a finite list of examples; the arbitrary admissible squarefree indices and all new-place compatibility conditions are handled uniformly.

## 8. Remaining obligations

This independent conventional reconstruction imports classical class field/Chebotarev, cyclotomic and local-field facts explicitly. It is not a verification of their exact original Lean implementations, nor independent replay of the submitted theorem. The full ML.vChar remains dependent on the actual zEval witnesses (including uniformity for each nonzero a0) and exceptional exc branch. The exact duality foundations and source-to-RH semantic correspondence still need audit. Retain the separation from formal or external certification.

Boundary: RH-A26-D05_NUSYS_CONSTRUCTION_RECONSTRUCTED_WITH_EXPLICIT_CLASSICAL_FOUNDATIONS__ZEVAL_EXC_FOUNDATIONAL_CORRESPONDENCE_ORIGINAL_REPLAY_OPEN.
