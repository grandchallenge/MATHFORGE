#!/usr/bin/env python3
"""Exact finite adversary: mod-36 global-unit six-sector Gaussian selection.

Models a primitive additive trace on each prime residue field, with sextic
character chosen to match the source's *global unit restriction*. It does
NOT claim to reconstruct the pinned trace or character at all finite residues,
and is NOT an infinite radial-sum proof or an independently Lean-checked lemma.
"""
from itertools import product
from math import gcd

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES={7:(3,1),13:(4,1),19:(5,2),31:(6,1),37:(7,3)}
ROOTS6=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
UNITS=ROOTS6
count=0

def check(b,msg=""):
    global count
    assert b,msg
    count+=1

def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c-b*d
def norm(z):
    a,b=z;return a*a-a*b+b*b
def residue(z,q,r):return (z[0]+r*z[1])%q
def primitive_logs(q):
    for g in range(2,q):
        vals=[pow(g,k,q) for k in range(q-1)]
        if len(set(vals))==q-1:return g,{v:i for i,v in enumerate(vals)}
    raise ValueError(q)

def poly_sum(P,Q):return [add(a,b) for a,b in zip(P,Q)]
def poly_times_e6(P,k):return [mul(v,ROOTS6[k%6]) for v in P]
def equal_mod_phi_q(P,Q):
    # q is prime and !=3: Phi_q stays of degree q-1 over Q(omega).
    return len({sub(x,y) for x,y in zip(P,Q)})==1
def gauss_poly(q,r,logs,e,d,z):
    P=[(0,0)]*q
    Z=residue(z,q,r)
    for x in range(1,q):
        P[(Z*x)%q]=add(P[(Z*x)%q],ROOTS6[(e*d*logs[x])%6])
    return P
def check_prime(q,p):
    check(norm(p)==q)
    r=(-p[0]*pow(p[1],-1,q))%q
    check((r*r+r+1)%q==0)
    g,logs=primitive_logs(q)
    m=((q-1)//6)%6
    ures=residue(UNITS[1],q,r)
    e=next((k for k in (1,5) if k*(logs[ures]%6)%6==m),None)
    check(e is not None,f"no unit-calibrated primitive order-six char q={q}")
    for j,u in enumerate(UNITS):
        check(norm(u)==1)
        check((e*logs[residue(u,q,r)])%6==(m*j)%6,
              f"actual unit exponent mismatch q={q},u={u}")
    for d in range(1,6):
        for z in product(range(-2,3),repeat=2):
            P=gauss_poly(q,r,logs,e,d,z)
            for j,u in enumerate(UNITS):
                Q=gauss_poly(q,r,logs,e,d,mul(u,z))
                expect=poly_times_e6(P,(-d*m*j)%6)
                check(equal_mod_phi_q(Q,expect),
                      f"Gauss-row unit covariance q={q},d={d},u={u},z={z}")
    print(f"prime q={q}, p={p}: global unit character gamma={m}, finite Gauss row covariance PASS")

def composite_sectors():
    # Composite supported ideals from independently distributed good primes.
    normset=[]
    gammas=[]
    for c,d,e in product(range(0,7),repeat=3):
        Ni=7**c*13**d*37**e
        gamma=((Ni-1)//6)%6
        expect=(c*1+d*2+e*0)%6
        check(Ni%6==1)
        check(gamma==expect,f"gamma nonadditive {c,d,e}")
        check(Ni%36==(6*gamma+1)%36)
        normset.append(Ni)
        gammas.append(gamma)
    for i in range(len(normset)):
        for j in range(len(normset)):
            gi,gj=gammas[i],gammas[j]
            orbit_sum=(0,0)
            for k in range(6):
                orbit_sum=add(orbit_sum,ROOTS6[(k*(gj-gi))%6])
            check(orbit_sum==((6,0) if gi==gj else (0,0)),
                  f"unit rotation sum {normset[i]},{normset[j]}")
            if normset[i]%36!=normset[j]%36:
                check(orbit_sum==(0,0))
    for q in (7,13,19,31,37):
        check((q**6)%36==1)
        check(((q**6)%36 != (q**7)%36)==(q%36!=1))
    print("composite supported norm labels and exact six-projector orthogonality PASS")

def main():
    for a,b in product(range(-20,21),repeat=2):
        check(2*norm((a,b))==a*a+b*b+(a-b)**2)
    for j,u in enumerate(UNITS):
        check(norm(u)==1)
        check(u==ROOTS6[j])
    for q,p in PRIMES.items():check_prime(q,p)
    composite_sectors()
    print("EXACT ASSERTIONS",count,"PASS")
    print("SCOPE: finite primitive-trace models; analytic source proof in report, new Lean elaboration not claimed")
    print("PIN",PIN)

if __name__=="__main__":main()
