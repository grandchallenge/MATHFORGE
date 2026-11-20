#!/usr/bin/env python3
"""GCL F003 pinned-source independent exact checks; stdlib, no upstream import.

Only finite algebraic/accounting identities and exact lattice fixtures are executed.
The universal Schwartz/Euler and Gaussian-energy statements require the mathematical
proof in WP03_F003_NATURAL_GAUSSIAN_ENERGY_RADIAL_EULER_AUDIT.md.
"""
from fractions import Fraction as F
from itertools import product

PIN = '1581d4cbdd69a0faf34b2089614fe2a814316a6a'

def norm_eis(a,b):
    return a*a - a*b + b*b

def lattice_count(bound):
    """#(a,b) with N(a+b*omega) < bound; bound is positive rational."""
    assert bound > 0
    t = 0
    while F(t*t) < 2*bound:
        t += 1
    return sum(norm_eis(a,b) < bound for a,b in product(range(-t,t+1), repeat=2))

def rad_exponents(x,k0,sigma,delta,reserve,q,k):
    assert k in (1,6,7) and q>=0 and sigma>=0
    moving = F(0) if k==6 else q
    removal = k*q
    main = k0 + max(x,F(0)) + 2*sigma + delta + reserve
    err = k0 + max(x-2*removal+moving,F(0)) + sigma + delta + reserve
    return main,err,moving,removal

def loss_exponents(bcap,epsmask,epschild,epsremove,d,delta,reserve,theta,clip,kappa,mesh,sigma,q,k):
    common = (2*bcap*epsmask + epschild + epsremove +
              (d+delta+reserve+theta)/6 + clip/3 + kappa*mesh)
    return common+sigma/3, common+k*q

def poly_diff(p):
    return [F(i)*p[i] for i in range(1,len(p))]

def next_euler_poly(p):
    # If D^j e^-x = e^-x P_j(x), D=x*d/dx.
    d=poly_diff(p)
    q=[F(0)]*(max(len(p),len(d))+1)
    for i,c in enumerate(p):q[i+1]-=c
    for i,c in enumerate(d):q[i+1]+=c
    while len(q)>1 and not q[-1]:q.pop()
    return q

def stirling(n):
    s=[[0]*(n+1) for _ in range(n+1)]
    s[0][0]=1
    for j in range(1,n+1):
        for k in range(1,j+1):
            s[j][k]=s[j-1][k-1]+k*s[j-1][k]
    return s

def run():
    assertions=0
    for a,b in product(range(-17,18),repeat=2):
        assert 2*norm_eis(a,b)==a*a+b*b+(a-b)**2
        assertions+=1
    for root in [F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(7)]:
        K=root*root
        count=lattice_count(2*K)
        bound=(1+4*root)**2
        assert count <= bound, (K,count,bound)
        if K>=1: assert count>1
        assertions+=2
    radii=0
    counterexample=None
    for k,x,k0,sigma,q,delta,reserve in product(
        (1,6,7),
        [F(-3),F(-1,2),F(0),F(1,3),F(5)],
        [F(0),F(3,7)],
        [F(0),F(1,2),F(2)],
        [F(0),F(1,12),F(1,3),F(3,2)],
        [F(0),F(1,9)],
        [F(0),F(2,5)],
    ):
        if q<sigma/6:continue
        rm,re,moving,removal=rad_exponents(x,k0,sigma,delta,reserve,q,k)
        assert re <= rm-sigma
        assert removal==k*q
        assert moving==(F(0) if k==6 else q)
        assert -2*removal+moving == {1:-q,6:-12*q,7:-13*q}[k]
        lm,le=loss_exponents(F(1),F(1,100),F(1,7),F(1,11),
             F(3,5),delta,reserve,F(1,13),F(1,17),F(3,4),F(1,5),sigma,q,k)
        assert le-lm==k*q-sigma/3
        if k==1 and le<lm: counterexample=(sigma,q,le-lm)
        radii+=1
        assertions+=5
    assert counterexample is not None
    q=F(1,3)
    assert rad_exponents(F(0),F(0),F(1),F(0),F(0),q,6)[2] != q
    assertions+=1
    table=stirling(11)
    p=[F(1)]
    for j in range(12):
        expected=[F(0)]*(j+1)
        for k in range(j+1):expected[k]=F((-1)**k*table[j][k])
        assert p==expected,(j,p,expected)
        for x in [F(0),F(1,2),F(1),F(3,2),F(7)]:
            val=sum(c*x**i for i,c in enumerate(p))
            independent=sum(F((-1)**k*table[j][k])*x**k for k in range(j+1))
            assert val==independent
            assertions+=1
        p=next_euler_poly(p)
        assertions+=1
    print('PIN',PIN)
    print('PASS exact Eisenstein norm and positive-cutoff lattice fixtures')
    print('PASS main/error conductor, radius and loss equalities:',radii,'cases')
    print('PASS hostile k=1 loss-monotonicity counterexample:',counterexample)
    print('PASS k=6 conductor moving-charge mutation rejected')
    print('PASS Gaussian Euler polynomial recurrences j=0..11')
    print('ASSERTIONS',assertions)
    print('BOUNDARY sharp source-family main/error Gaussian powers NOT reconstructed')

if __name__=='__main__':run()
