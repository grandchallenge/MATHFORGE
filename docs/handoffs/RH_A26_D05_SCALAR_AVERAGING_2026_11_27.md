# RH-A26 D05 — central scalar averaging (SCen)

Disposition: conventional reconstruction of actual SCen, TSpan, TScal, TSimp, TAv and AvCongr.join. Source works for arbitrary number fields and continuous forms with closed simplex-integral cochains, not only smooth exterior-closed forms. Classical Dirichlet unit theorem, product formula, finite-dimensional Bochner integration and Fubini explicit; prior SEv (invariant closed cochain basepoint independence on cycles) retained. Original formal correspondence and kernel replay open. No claim of RH/GRH certification.

## Source identity

Paths relative to Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion in restored original publisher archive SHA256 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc.
| File | SHA256 |
|---|---|
| ActLPos.lean | 7e4840179da3ad19729771188ef5b90129d4821d36fb0fe637b939228c58f874 |
| SBridgeAlt.lean | ab24a2e16c750c8bfbb20571b1995a9c91bf08d5e050fbdc3967aecbd7b0c481 |
| CentralPositiveSemidefinite/ActLEqOfScalar.lean | 2b5823ae4d141f5035b22e322c73a56c429f0701fd080a1c8245d9849eaad9ce |
| CentralPositiveSemidefinite/AvCongr.lean | 7f0003d883a8dc830f0dca5aea31aba1bd553c7199a07aba461f93f94d39fe7c |
| CentralPositiveSemidefinite/ContinuousOnPullbackCentralScalingSimplexParam.lean | b5a32b857916f4bcd7655e23cdc3e8de04b819c5e05cce08ded5e1f654d244bd |
| CentralPositiveSemidefinite/FInvIff.lean | 8940bb9b601ff44a79fcf3981803b316401e559f9a2c9e3c0cf8c9a02c46b870 |
| CentralPositiveSemidefinite/LamSApply.lean | 5badc353ea87881697ca2387e71ad614cdd6aad52e7f521575b071bf830318cd |
| CentralPositiveSemidefinite/RealSmulPosSemidef.lean | 75d2421ac3762ff06902aeb3593d0369745756b5d53c3e7fb64706f3ac32519c |
| CentralPositiveSemidefinite/SCenOf.lean | a8484424d2b91c66db857af353fb6aafa285ded42eef81f2114dbaa8b535b016 |
| CentralPositiveSemidefinite/TSpan.lean | f37cdfca8431ab0aeae4c4b1d9ad1577a609088568708a01eab7329e5fca118a |

## 1. Exact contract and scalar action

Let L be any number field, W its nonempty finite set of infinite places, N any natural, V=HS(L,N) (real tuples of Hermitian matrices), P=Pos (positive cone), G=Gp product GL_N(C), Gamma=Gm=GL_N(O_L). Form degree q=k+1. A_g h=(g^-1)*h g^-1. A_g A_h=A_(gh); o=identity. For a form omega define pb(g)omega(h)=omega(A_g h) composed with A_g in each of its q slots. Hence pb(g)pb(k)=pb(kg), the reverse order of group multiplication. The source Good means continuous on P and delta(intP omega)=0; no differentiability hypothesis. FInv(g) means pb(g)omega=omega on P. SCen assumes Good, FInv under embedded Gamma, and FInv under scalar tuples with common modulus. Also B:G->R with norm(fr omega(x))<=B(x), and for every compact K subset G a C_K with B(xg)<=C_K B(x) for g in K, all x. No continuity or measurability of B required. Output omega' Good, arithmetic invariant, FInv for every scalar tuple, exact equal evaluations on every real bar cycle, norm(fr omega'(x))<=C B(x).

For t in R^W define source sc(t)=tuple exp(t_w) I. It is a continuous group homomorphism from addition into center of G (entries and inverse entries continuous), with A_sc(t) on w-block equal exp(-2t_w) h_w. For general nonzero complex scalar s_w, inverse congruence yields |s_w|^-2 h_w, since conjugate inverse times inverse equals squared inverse modulus. Thus actL(scal s)=actL(sc(log|s|)), not necessarily equality of group elements. For integral unit u, lg(u)_w=log|w(u)| (source infinite-place norm unweighted; embedding norm equals it). The scalar matrix uI lies in Gamma with integral inverse, so actL(emb(uI))=actL(sc(lg u)). These are all TScal facts, including operator continuity by finite dimensionality. If N=0 matrices have no entries and q>=1 forms vanish, same formulas remain valid; no N>=1 needed. Fix(omega) is set of t for which pb(sc t)omega equals omega on P. It contains zero and is closed under addition, but not necessarily real scaling. Common-modulus premise gives the entire diagonal line R*1 in Fix, and arithmetic invariance gives lg(u) in Fix for every integral unit.

## 2. TSpan: actual weighted logarithms

Write m_w=1 for real, 2 for complex place; M=sum m_w=[L:Q]>0. Product formula for units gives sum m_w lg(u)_w=0. Dirichlet unit theorem supplies a fundamental system of units (finite list) whose weighted logarithms, with one place removed, span R^(|W|-1); this is the exact classical input span_fund in LamSApply. The reconstruction does not prove Dirichlet's theorem itself. The source lamS is inverse of weighted coordinate deletion on H0={z:sum m_w z_w=0}: for w!=w0 set z_w=t'_w/m_w; at omitted w0 set z_w0=-sum t'_w/m_w0. It maps weighted fundamental-unit log vectors to actual lg vectors by product formula, hence their span is H0. For arbitrary t, c=(sum m_w t_w)/M and t-c*1 in H0, so
    R^W = R*1 + span_R{lg(u): u in finite list}.
This is exact TSpan, including mixed real/complex places. When |W|=1 the unit list is empty and the common line already exhausts all logarithms. Do not replace weighted mean by unweighted mean for mixed signature. Example for real quadratic L=Q(sqrt 2), u=1+sqrt 2 has conjugate 1-sqrt 2, inverse absolute values, log vector (a,-a) with a=log(1+sqrt 2)>0. Common scale supplies (1,1), so all directions spanned. Example is illustrative, not a substitute for TSpan.

## 3. Actual interval average and compact regularity

For v in Fix(omega), source av(v,omega)(h)=integral_0^1 pb(sc(tau v))omega(h) d tau (Bochner integral of alternating form values), defined on V; only behavior on P is required. A_sc preserves P. Map (tau,h)->pb(sc(tau v))omega(h) continuous on R x P by finite-dimensional continuity of A, evaluation and composition with linear maps. For each h in P interval integrand continuous and integrable; local compact neighborhood of h inside open P gives a uniform bound on [0,1] times that neighborhood, and dominated convergence gives continuity on P. This is source av_cont. No assumptions outside P are used; totalized integrals there have no role.

For any g commuting with sc(t) (here every g), use pb(g)pb(k)=pb(kg), interchange continuous linear slot composition with Bochner integral, to obtain pb(g)av(v,omega)=av(v,pb(g)omega) on P. Thus any existing invariance is preserved, including embedded Gamma, common-modulus scalars, previously acquired log directions. Pullback order matters even though central elements commute. If v in Fix, for fixed h the function f(tau)=pb(sc(tau v))omega(h) is 1-periodic, by applying pb(sc v)omega=omega at A_sc(tau v)h and composing slots. For sigma real,
    pb(sc(sigma v))av(v,omega)(h)=integral_0^1 f(tau+sigma)d tau
       =integral_sigma^(sigma+1) f(t)dt=integral_0^1 f(t)dt.
Proof of last equality: remove integer part of sigma by periodicity and split interval at next integer, translating second piece by -1. This holds for all real sigma, including negative and irrational. Consequently R v subset Fix(av), not merely integer multiples. This establishes TAv periodicity part without a limit, unbounded average or ergodic theorem.

## 4. Exact simplex and cycle comparison with only Good

For y=(y0,...,yq) in P, I(omega;y)=integral over standard q-simplex of omega(y0+sum t_i(y_i-y0)) on the ordered edge list. Convexity ensures points in P, even with degenerate vertices. For linear A_g, affine parameterization and edge lists transform exactly, hence I(pb(g)omega;y)=I(omega;A_g y). This proves TSimp and arithmetic invariance of I(omega) from FInv. The joint integrand on [0,1] x simplex for the averaging path is continuous, on compact product, thus integrable; evaluating the form on fixed edges commutes with Bochner integral. Fubini gives
    I(av(v,omega);y)=integral_0^1 I(omega;A_sc(tau v)y)d tau.
The same joint continuity on bounded tau intervals gives continuity in tau of I(omega;A_sc(tau v)y). These are source av_int and cont_param. Since the coboundary is a finite alternating sum, delta I(av)=integral delta I(omega) at transformed tuples=0, and Good preserved. Do NOT assume d omega exists, or use differentiability of the original form to prove SCen.

For each real finitely supported bar cycle z and fixed tau, let o_tau=A_sc(tau v)o. The commuting central action gives A_sc(tau v) A_emb(partialProd g_j)o=A_emb(partialProd g_j)o_tau. Since F=I(omega) is an invariant closed homogeneous cochain on P, source SEv gives ev(emb,F,o_tau,z)=ev(emb,F,o,z). This is the basepoint prism: the two equivariant maps on homogeneous group vertices g->A_emb(g)o and g->A_emb(g)o_tau are chain-homotopic by alternating mixed-vertex prism; boundary terms cancel on a cycle and delta F=0 kills the homotopy term. Thus every integrand cycle evaluation is the same original evaluation. Commute finite chain sum through interval integral (each simplex integrand continuous) and integrate constant over interval of length one. Exact period identity follows. It need not hold on an individual simplex or noncycle; no assumption of invariance of I under arbitrary scalar action before averaging is used. This is source step_ev; no appeal to differentiable de Rham homotopy.

## 5. Frame growth and finite iteration

Actual fr omega(x)=pb(x)omega(o). By linearity of slot composition under integral and reverse pullback composition,
    fr av(v,omega)(x)=integral_0^1 fr omega(sc(tau v)x)d tau.
Since scalar center commutes, equal x sc(tau v); this orientation is needed for the right-compact-distortion premise on B. If norm(fr omega)<=C B(x) with C>=0, then with K=image([0,1],tau->sc(tau v)) compact,
    norm(fr av(v,omega)(x))<=integral C B(x sc(tau v)) <= C max(C_K,0) B(x).
Interpret first inequality via the pointwise bound on the continuous frame integrand, not by integrating a potentially nonmeasurable B. Nonnegativity of B from initial norm bound; new constant independent of x and degree exponent unchanged. In particular B=C0 ht^p from prior SWhit meets the compact-distortion premise via SHt: ht(xg)<=D_K ht(x), so B(xg)<=max(D_K,0)^p B(x), with C0>=0. Hence the original square-integrability threshold N>=2p+2 is preserved by the finite sequence. No uniform constant across N is required.

Run the source's iter on the finite fundamental-unit list (its recursive order processes the tail first). Each step applies above since arithmetic invariance preserved, so lg(u) is still fixed before averaging. Carry Good, Gamma invariance, diagonal line, original cycle evaluation and growth with new nonnegative C. Also all previously obtained directions remain fixed because the central pullbacks commute. After the list, Fix contains R*1 and every R lg(u). Additivity and TSpan imply Fix=R^W (do not assume Fix was initially a vector space). Every scalar s acts as sc(log|s|) on V, thus full FInv for arbitrary complex nonzero scalar tuples. This completes actual SCen using original interval averages, finite iteration and source quantifiers, not a different averaging on a noncompact group.

## 6. Exact finite controls and limitations

The accompanying fixture uses rational-periodic triangular functions to check continuous nonconstant period averages and translation invariance, exact integration of a nonzero degree-one period on a log-coordinate translation cycle, weighted real/complex logarithm reconstruction (synthetic vectors, not numerical unit theorem), and rational Gaussian scalar inverse-congruence phase independence. These are exact finite controls of mechanisms; they do not prove the actual number-field unit theorem, original analytic integrability or formal replay.

## Boundary

SCen conventionally reconstructed. It consumes Dirichlet's theorem and prior SEv; actual source needs only Good, and no smoothness added. Next SMean: prove the integral moving-frame value is invariant under compact unitary stabilizer, allowing it to extend to a genuinely G-invariant differential form, with exact normalized mean and actual Dom. Then SInv, SPrime and final analytic join; geometry/stability/counting/torsion and original replay remain. No certification.

Boundary RH-A26-D05_SCALAR_AVERAGING_CONVENTIONALLY_RECONSTRUCTED__INVARIANT_MEAN_FORM_PRIME_STABILITY_GEOMETRY_COUNTING_TORSION_FOUNDATIONS_ORIGINAL_REPLAY_OPEN.
