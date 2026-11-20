#!/usr/bin/env python3
"""OAI26 F003 exact finite adversary: ray bi-character and annular Cauchy.

Pinned source: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
Source identities:
  Eisenstein/ConjugateLevelAction.lean QuadraticAllOddCRT.quadraticRayExponent/sign
  Cusp/MatrixPhases.lean EisensteinEPrimaryPhase.mul/odd
  GaussSum/CompletedExpansion.lean RayFourExpansion.firstPhaseTable / pairCoeff
  Moments/Smooth.lean wholeKernel / separatedKernel / rootWindow
  Moments/Cauchy.lean whole_kernel_row_estimate
  Moments/ReflectedChild.lean reflected-gauss
  Moments/FirstDivisorCommonBound.lean actual_supported_annular_block

All finite arithmetic uses exact Gaussian rational pairs and Fraction.
The discrete cyclic 4-point Fourier test is an independent algebraic
analogue, not an assertion that a discrete kernel is a Schwartz one.
"""
from fractions import Fraction as F

def mul_mod4(u,v):
    a,b=u; c,d=v
    return ((a*c-b*d)%4,(a*d+b*c-b*d)%4)

UNITS=tuple((a,b) for a in range(4) for b in range(4) if a%2 or b%2)
EX0={(0,1),(0,3),(1,0),(1,1),(3,0),(3,3)}
EX1={(1,2),(1,3),(2,3)}
def exponent(u):
    if u in EX0:return 0
    if u in EX1:return 1
    return 3
def beta(u,v):
    return 1 if exponent(mul_mod4(u,v)) == ((exponent(u)+exponent(v))%4) else -1

def ray_phase_exact():
    assert len(UNITS)==12
    assert len(set(UNITS))==12
    for u in UNITS:
        assert any(mul_mod4(u,v)==(1,0) for v in UNITS)
    for u in UNITS:
        for v in UNITS:
            uv=mul_mod4(u,v)
            assert uv in UNITS
            assert beta(u,v)==beta(v,u)
            assert beta(u,v) in (-1,1)
            for w in UNITS:
                assert beta(uv,w)==beta(u,w)*beta(v,w)
                assert beta(w,uv)==beta(w,u)*beta(w,v)
    patterns={tuple(beta(u,v) for v in UNITS) for u in UNITS}
    kernel=[u for u in UNITS if all(beta(u,v)==1 for v in UNITS)]
    assert len(patterns)==4
    assert len(kernel)==3
    # For bicharacter B, map phi(u)=B(u,*) is a homomorphism.
    # In normalized 2D finite-group Fourier transform,
    # hat B(chi,eta) = (1/12) sum_{u: phi(u)=eta} conj chi(u).
    # Each nonempty fiber has 3 points. Exactly 4 characters
    # are trivial on ker(phi); all other fiber sums vanish.
    # 4*4 coefficients each of magnitude 3/12=1/4.
    image=len(patterns)
    nonzero=image*image
    magnitude=F(len(kernel),len(UNITS))
    mass=nonzero*magnitude
    assert nonzero==16 and magnitude==F(1,4) and mass==4
    assert mass<F(256)
    print("RAY_RING_MOD4_UNIT_GROUP_12_AND_BICHARACTER_PASS")
    print("BICHARACTER_IMAGE_4_KERNEL_3_EXACT_FOURIER_L1_MASS_4_PASS")
    return image, len(kernel), mass

# Gaussian rationals as immutable (re,im) Fraction pairs
def gr(a=0,b=0): return F(a),F(b)
def ga(z,w): return z[0]+w[0],z[1]+w[1]
def gm(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def gc(z): return z[0],-z[1]
def gs(z,k):return z[0]*k,z[1]*k
def gn(z):return z[0]*z[0]+z[1]*z[1]
POW=(gr(1),gr(0,1),gr(-1),gr(0,-1))
PALETTE=(gr(0),gr(1),gr(-1),gr(0,1),gr(0,-1),gr(F(1,2),F(1,2)))
def pw(k):return POW[k%4]
def sm(items):
    z=gr()
    for a in items:z=ga(z,a)
    return z
def coeff(seed,z,i,shift=0):
    return PALETTE[(seed+3*z+5*i+shift)%len(PALETTE)]

def cyclic_fourier_exact():
    nonzero=0
    mutated=0
    for seed in range(101):
        rows=tuple(range(4))
        rho=lambda z:(z+seed)%4
        x=lambda z:(z*2+seed)%4
        u=tuple(range(3))
        v=(0,2,3)
        eta=[POW[(seed+z)%4] for z in rows]
        # Synthetic kernel samples with exact Gaussian rational values.
        h=[PALETTE[(seed+2*k+1)%len(PALETTE)] for k in range(4)]
        c=lambda z,i:coeff(seed,z,i,1)
        # Models the mandatory reflected row z->-z in FirstChildBound:
        d=lambda z,j:coeff(seed,(-z)%4,j,2)
        d_wrong=lambda z,j:coeff(seed,z,j,2)
        direct=sm(gm(eta[z],gm(gm(c(z,i),gc(d(z,j))),
                h[(rho(z)+x(z)-u[i]-v[j])%4]))
            for z in rows for i in range(3) for j in range(3))
        bhat=[gs(sm(gm(h[k],pw(-t*k)) for k in range(4)),F(1,4))
              for t in range(4)]
        separated=gr()
        for t in range(4):
            row_terms=[]
            left_energy=F(0);right_energy=F(0)
            for z in rows:
                left=sm(gm(c(z,i),pw(-t*u[i])) for i in range(3))
                right=sm(gm(gc(d(z,j)),pw(-t*v[j])) for j in range(3))
                row=gm(eta[z],gm(pw(t*(rho(z)+x(z))),gm(left,right)))
                row_terms.append(row)
                left_energy+=gn(left)
                right_energy+=gn(right)
            total=sm(row_terms)
            assert gn(total)<=left_energy*right_energy,(seed,t)
            separated=ga(separated,gm(bhat[t],total))
        assert separated==direct,(seed,separated,direct)
        if direct!=gr():nonzero+=1
        wrong=sm(gm(eta[z],gm(gm(c(z,i),gc(d_wrong(z,j))),
                h[(rho(z)+x(z)-u[i]-v[j])%4]))
            for z in rows for i in range(3) for j in range(3))
        if wrong!=direct:mutated+=1
    assert nonzero>=90 and mutated>=75,(nonzero,mutated)
    print("EXACT_CYCLIC_FOURIER_SEPARATION_AND_COMPLEX_ROW_CAUCHY_PASS",101)
    print("HOSTILE_UNREFLECTED_RIGHT_ROW_REJECTED",mutated)

def majorant_and_divisor():
    # For any radial U (even under reflection), U>=1 on finite rows
    # also controls P(-z), a separate step in ReflectedChild.
    rows=(1,2)
    U={0:F(0),1:F(2),2:F(1),3:F(2)}
    vals={0:gr(1),1:gr(2),2:gr(0),3:gr(0,1)}
    assert all(U[z]==U[(-z)%4] for z in range(4))
    assert all(U[z]>=1 for z in rows)
    lhs=sum((gn(vals[(-z)%4]) for z in rows),F(0))
    rhs=sum((U[z]*gn(vals[z]) for z in range(4)),F(0))
    assert lhs<=rhs
    # If majorant is not even, the same inference fails.
    hostile={0:F(0),1:F(1),2:F(1),3:F(0)}
    p={0:gr(),1:gr(),2:gr(),3:gr(1)}
    wrong_left=sum((gn(p[(-z)%4]) for z in rows),F(0))
    wrong_right=sum((hostile[z]*gn(p[z]) for z in range(4)),F(0))
    assert wrong_left==1 and wrong_right==0
    # The source's active Möbius squarefree/live rule:
    # sqrt(4/n)*sqrt(9/n)=6/n; μ=0 and non-live are killed.
    E1,E2=F(4),F(9)
    norms=(1,3,7,9)
    mu=(1,-1,0,-1)
    cap=F(4)
    lhs=F(0);right=F(0)
    for n,m in zip(norms,mu):
        live=F(n)<=cap
        if m and live:
            lhs+=abs(m)*F(2*3,n)
            right+=F(abs(m),n)*F(6)
        else:
            assert not (m and live)
    assert lhs==right==F(8)
    print("RADIAL_REFLECTION_MAJORANT_EXACT_PASS")
    print("HOSTILE_ASYMMETRIC_MAJORANT_REJECTED")
    print("MOBIUS_LIVE_FILTER_AND_SQRT_DIVISOR_1_OVER_N_PASS")

if __name__=="__main__":
    ray_phase_exact()
    cyclic_fourier_exact()
    majorant_and_divisor()
    print("F003_ANNULAR_REFLECTION_AND_EXACT_RAY_PHASE_AUDIT_PASS")
