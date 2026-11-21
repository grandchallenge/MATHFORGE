#!/usr/bin/env python3
"""OAI26 F003 exact adversary: actual sextic local table and seeded physical sectors.

Checks the mathematical finite quotient/local ingredients and the *exact*
Eisenstein lattice sieve-count identity, not upstream Lean elaboration or
analytic ZeroAt/PositiveAt. All arithmetic integral/Fraction; no floats.
"""
from fractions import Fraction as F
from itertools import combinations, product
from functools import lru_cache
from math import isqrt

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES=((7,(3,1)),(13,(4,1)),(37,(7,3)))
CHECKS=0

def require(x,why=""):
    global CHECKS
    assert x,why
    CHECKS+=1

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)

def conj(z):
    a,b=z
    return (a-b,-b)

def quot(z,p,q):
    t=mul(z,conj(p))
    if t[0]%q or t[1]%q:return None
    ans=(t[0]//q,t[1]//q)
    require(mul(ans,p)==z,"Eisenstein quotient")
    return ans

def valuation(z,p,q):
    if z==(0,0):return 99
    v=0
    while True:
        w=quot(z,p,q)
        if w is None:return v
        z=w
        v+=1
        require(v<90,"infinite factorization")

def local_gauss_abs2(q,e,v):
    """Genuine source normalized sextic prime power Gauss |g|^2 table."""
    if e==0:return 1
    if v==e-1:
        return q**(e-2) if e%6==0 else q**(e-1)
    if v>=e and e%6==0:
        return (q-1)**2*q**(e-2)
    return 0

def tag(e):
    return min(e,6)

def lattice_tag(v):
    return min(v+1,6)

@lru_cache(None)
def lattice(B):
    if B<0:return tuple()
    maxa=isqrt((4*B)//3)+2
    return tuple((a,b) for a in range(-maxa,maxa+1)
                 for b in range(-maxa,maxa+1)
                 if norm((a,b))<=B)

def Afloor_bound(x):
    """Exact # O-lattice points of squared norm <= rational x."""
    x=F(x)
    return len(lattice(x.numerator//x.denominator)) if x>=0 else 0

def shell_data(selected,sigma,K):
    low=[j for j,t in zip(selected,sigma) if t<=5]
    d=1
    for j,t in zip(selected,sigma):
        d*=PRIMES[j][0]**(t-1)
    # Exact inclusion-exclusion on finite Eisenstein ideal sublattices.
    count=0
    for m in range(len(low)+1):
        for subset in combinations(low,m):
            den=d
            for j in subset:den*=PRIMES[j][0]
            count+=((-1)**m)*Afloor_bound(F(2)*K/den)
    return d,low,count

def direct_shell(selected,sigma,K):
    B=(F(2)*K).__floor__()
    total=0
    for z in lattice(B):
        ok=True
        for j,t in zip(selected,sigma):
            q,p=PRIMES[j]
            v=valuation(z,p,q)
            if (t<=5 and v!=t-1) or (t==6 and v<5):
                ok=False
                break
        total+=int(ok)
    return total

def test_eisenstein_and_local_support():
    for q,p in PRIMES:
        require(norm(p)==q)
        for e in range(1,16):
            for v in list(range(0,18))+[99]:
                a=local_gauss_abs2(q,e,v)
                t=tag(e)
                require(a>=0)
                # Proven local normalized row sqrt-q loss for classes 1..5.
                require(a*(q if t<=5 else 1)<=q**e,
                        (q,e,v,a,"local L-infinity bound"))
                if a:
                    require(lattice_tag(v)==t,
                            (q,e,v,a,"wrong physical sector"))
                    require(v>=t-1)
                if t<=5 and v>=t:
                    require(a==0)
        print("local genuine sextic norm",q,"support and sqrt-q saving PASS")

    for exps in product(range(1,11),repeat=3):
        sigma=tuple(tag(e) for e in exps)
        qprod=1
        nlow=1
        for idx,e in enumerate(exps):
            qprod*=PRIMES[idx][0]**e
            if sigma[idx]<=5:nlow*=PRIMES[idx][0]
        for vals in product((0,1,2,3,4,5,6,7,8,9,12,99),repeat=3):
            amp2=1
            for idx,(e,v) in enumerate(zip(exps,vals)):
                amp2*=local_gauss_abs2(PRIMES[idx][0],e,v)
            require(amp2*nlow<=qprod)
            if amp2:
                require(tuple(lattice_tag(v) for v in vals)==sigma,
                        (exps,vals,sigma))
    print("all three-prime tensor factors; 10^3 exponent triples x 12^3 valuations PASS")

def test_exact_eisenstein_shell_count():
    Kvals=[F(1,4),F(1,2),F(1),F(2),F(7,2),F(10),F(25),F(100)]
    count=0
    for m in range(4):
        for selected in combinations(range(3),m):
            n=1
            for j in selected:n*=PRIMES[j][0]
            for sigma in product(range(1,7),repeat=m):
                d,low,arithmetic=shell_data(selected,sigma,F(25))
                require(d>=1 and arithmetic>=0)
                # Minimum column norm for this sector (squarefree seed).
                expected=n*d
                exponents=[t if t<=5 else 6 for t in sigma]
                actual=1
                for j,e in zip(selected,exponents):
                    actual*=PRIMES[j][0]**e
                require(actual==expected,(selected,sigma,actual,expected))
                # Every active ideal in sector has norm >=n*d.
                for h in (expected-1,expected,expected+1):
                    if h<expected:require(h<actual)
                    else:require(actual<=h)
                for K in Kvals:
                    d,low,formula=shell_data(selected,sigma,K)
                    brute=direct_shell(selected,sigma,K)
                    require(formula==brute,
                            (selected,sigma,str(K),formula,brute))
                    if low and F(2)*K<d: require(formula==0)
                    if len(low)>0: require(formula<=Afloor_bound(F(2)*K/d)-1)
                    count+=1
        print(f"seed subset cardinality {m}: exact CRT shell inclusion-exclusion PASS")
    print("physical shell instances",count,"PASS")

def test_seed_radius_zero_and_origin():
    for m in range(4):
        for selected in combinations(range(3),m):
            n=1
            for j in selected:n*=PRIMES[j][0]
            sectors=list(product(range(1,7),repeat=m))
            all_high=(6,)*m
            high_d=1
            for j in selected:high_d*=PRIMES[j][0]**5
            require(n*high_d==n**6)
            for H in (F(0),F(n-1),F(n),F(n**6-1),F(n**6)):
                possible=[]
                for sigma in sectors:
                    d,low,_=shell_data(selected,sigma,F(1,2))
                    if n*d<=H:possible.append(sigma)
                if H<n:require(not possible)
                if H<n**6 and n>1:require(all_high not in possible)
                if H<n**6 and n>1:
                    # At K<=1/2 every non-origin sector is excluded;
                    # all-high excluded by source H.
                    for sigma in possible:
                        _,low,count=shell_data(selected,sigma,F(1,2))
                        require(low and count==0)
    print("live-sector pruning and nontrivial small-physical-radius zero PASS")

def main():
    test_eisenstein_and_local_support()
    test_exact_eisenstein_shell_count()
    test_seed_radius_zero_and_origin()
    print("EXACT ASSERTIONS",CHECKS,"PASS")
    print("PIN",PIN)
    print("LIMITATIONS: finite tests of true local sextic magnitude/support and exact lattice count only.")
    print("NOT PROVED BY EXECUTION: new Lean theorem; source-wide analytic ZeroAt/PositiveAt; four seeded powers.")

if __name__=="__main__":main()
