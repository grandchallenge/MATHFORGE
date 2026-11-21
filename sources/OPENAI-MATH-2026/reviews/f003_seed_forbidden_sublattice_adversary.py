#!/usr/bin/env python3
"""Exact finite adversary: F003 genuine sextic local support + squarefree seed radius gates.

Tests algebraic finite products/valuations and source-necessary coefficient
conditions only. Does not instantiate full upstream Input, certify Poisson,
or Lean-elaborate the new generic theorem.
"""
from itertools import product, combinations
from fractions import Fraction

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES=((7,(3,1)),(13,(4,1)),(37,(7,3)))
assertions=0

def require(ok,msg=""):
    global assertions
    assert ok,msg
    assertions+=1

def add(x,y):
    return x[0]+y[0],x[1]+y[1]

def mul(x,y):
    a,b=x;c,d=y
    return a*c-b*d,a*d+b*c-b*d

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def pow_eis(z,n):
    out=(1,0)
    for _ in range(n):
        out=mul(out,z)
    return out

def conjugate(z):
    a,b=z
    return a-b,-b

def divide_if_possible(z,p,q):
    t=mul(z,conjugate(p))
    if t[0]%q or t[1]%q:
        return None
    out=(t[0]//q,t[1]//q)
    require(mul(p,out)==z,"Eisenstein exact quotient")
    return out

def valuation(z,p,q,cap=20):
    if z==(0,0):
        return cap
    e=0
    while e<cap:
        quotient=divide_if_possible(z,p,q)
        if quotient is None:break
        e+=1
        z=quotient
    return e

def local_row_nonzero(exponent,v):
    """Matches pinned sextic prime-power support, 0-exponent means identity."""
    if exponent==0:return True
    return v==exponent-1 or (exponent%6==0 and v>=exponent)

def active_support_restriction(exps,seed_indices,j):
    seednorm=1
    nI=1
    for idx, (q,_) in enumerate(PRIMES):
        nI*=q**exps[idx]
        if idx in seed_indices:
            seednorm*=q
    if nI >= seednorm**(j+1):
        return None
    require(all(exps[i]>=1 for i in seed_indices))
    witness=[i for i in seed_indices if 1<=exps[i]<=j]
    require(bool(witness),f"no prime with exponent ≤j: seed={seed_indices},e={exps},j={j}")
    for deltas in ((0,)*len(seed_indices),(1,)*len(seed_indices),(3,)*len(seed_indices)):
        valuations=[0,0,0]
        for i,delta in zip(seed_indices,deltas):
            valuations[i]=j+delta
        require(any(not local_row_nonzero(exps[i],valuations[i]) for i in seed_indices),
                f"nonzero physical row on seed^{j}: seed={seed_indices},e={exps},j={j}")
    # Origin has infinite valuation at all primes. A source row cannot
    # have all exponents divisible by six under H < N(seed)^6.
    if j==5:
        require(not all(e%6==0 for e in exps),"nonzero principal-origin row below seed^6")
    return True

def main():
    for q,p in PRIMES:
        require(norm(p)==q)
        for e in range(1,9):
            for v in range(0,10):
                expected=(v==e-1 or (e%6==0 and v>=e))
                require(local_row_nonzero(e,v)==expected)
        for a,b in product(range(-16,17),repeat=2):
            require(2*norm((a,b))==a*a+b*b+(a-b)**2)
    for size in (1,2,3):
        for seed_indices in combinations(range(3),size):
            seed=(1,0);n=1
            for idx in seed_indices:
                seed=mul(seed,PRIMES[idx][1])
                n*=PRIMES[idx][0]
            require(norm(seed)==n)
            for j in range(1,6):
                I=pow_eis(seed,j+1)
                z=pow_eis(seed,j)
                require(norm(I)==n**(j+1))
                require(norm(z)==n**j)
                for idx in seed_indices:
                    q,p=PRIMES[idx]
                    require(valuation(z,p,q)==j,"valuation of sharp boundary shell")
                    require(local_row_nonzero(j+1,j),"row nonzero at exact threshold")
                # Actual source at H<n^(j+1) cannot have this column;
                # at equality threshold, local Gaussian support is nonzero.
                require(not (norm(I)<n**(j+1)))
            for exps in product(range(0,9),repeat=3):
                if not all(exps[i]>=1 for i in seed_indices):
                    continue
                for j in range(1,6):
                    active_support_restriction(exps,seed_indices,j)
            # A truly nonzero source requires seed norm≤H. When seed norm>H,
            # the sum is empty independently of the physical Gaussian radius.
            for H in (Fraction(0),Fraction(n,3),Fraction(n-1),Fraction(n)):
                if H<n:
                    for exps in product(range(0,7),repeat=3):
                        if all(exps[i]>=1 for i in seed_indices):
                            NI=1
                            for idx in range(3):
                                NI*=PRIMES[idx][0]**exps[idx]
                            require(NI>H,"seed-empty gate violated")
            print(f"seed prime indices={seed_indices}; N(seed)={n}, five forbidden sublattices and sharpness PASS")
    # Direct physical origin (0,0) is divisible by every ideal; it is not a
    # hidden exception to the nonprincipal Gauss zero for exponents 1..5.
    for q,p in PRIMES:
        require(valuation((0,0),p,q,20)==20)
        for e in range(1,6):
            require(not local_row_nonzero(e,20))
        require(local_row_nonzero(6,20))
    print("EXACT ASSERTIONS",assertions,"PASS")
    print("NOT CLAIMED: full Input instantiation; new Lean theorem elaboration; four seeded powers; MATHCERT")
    print("PIN",PIN)

if __name__=="__main__":main()
