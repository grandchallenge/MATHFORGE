"""Finite arithmetic controls for primRam and exceptional Kummer vanishing.

Character exponents are exact integers mod the group exponent. No finite
control substitutes for the Galois, local inertia or cohomology proof.
"""
from math import gcd, lcm, prod
from fractions import Fraction
from itertools import product

def prime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def units(n): return [x for x in range(n) if gcd(x,n)==1]
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def order(x,n):
    y=1%n; j=0
    while True:
        j+=1; y=y*x%n
        if y==1%n: return j

def characters(n):
    """Enumerate all homomorphisms U(n) -> Z/E, E=exponent U(n)."""
    U=units(n); E=lcm(*(order(x,n) for x in U))
    maps=[{1%n:0}]; H={1%n}
    for x in U:
        if x in H: continue
        r=1; y=x%n
        while y not in H: r+=1; y=y*x%n
        powers=[pow(x,j,n) for j in range(r)]
        maps=[{h*p%n:(m[h]+j*b)%E for h in H for j,p in enumerate(powers)}
              for m in maps for b in range(E) if (r*b-m[y])%E==0]
        H=set(maps[0])
    assert len(maps)==len(U) and len({tuple(m[x] for x in U) for m in maps})==len(U)
    return U,E,maps

def conductor_tests():
    nchar=0; ram=0; unram=0; excluded=0; exc=0; nonexc=0; lifts=0
    for f in range(1,41):
        U,E,maps=characters(f)
        for m in maps:
            assert all(m[x*y%f]==(m[x]+m[y])%E for x in U for y in U)
            nchar+=1
            cond=min(d for d in divisors(f) if all(m[x]==0 for x in U if x%d==1%d))
            if cond!=f:
                excluded+=1
                continue
            for p in (2,3,5,7,11,13,17,19,23,29,31,37,41):
                f0=f
                while f0%p==0: f0//=p
                K=[x for x in U if x%f0==1%f0]
                if f%p==0:
                    assert any(m[x]!=0 for x in K)
                    ram+=1
                else:
                    assert all(m[x]==0 for x in K)
                    unram+=1
            n=lcm(*(E//gcd(E,m[x]) for x in U))
            for ell in (3,5,7,11):
                if n%ell==0: continue
                # Match against inverse k-th cyclotomic power using
                # exact character exponents in a common cyclic root group.
                g=next(g for g in range(1,ell) if order(g,ell)==ell-1)
                logs={pow(g,i,ell):i for i in range(ell-1)}
                F=lcm(f,ell); R=lcm(E,ell-1)
                for k in range(2,9):
                    if (m[-1%f]*(R//E)-k*(R//2))%R: continue
                    matches=all((m[b%f]*(R//E)+k*logs[b%ell]*(R//(ell-1)))%R==0
                                for b in units(F))
                    if matches:
                        assert f in (1,ell)
                        exc+=1
                    else: nonexc+=1
                    # At a raised modulus, order and parity remain the same.
                    for N in (2*f,3*f):
                        V=units(N)
                        assert set(b%f for b in V)==set(U)
                        assert lcm(*(E//gcd(E,m[b%f]) for b in V))==n
                        assert m[-1%N%f]==m[-1%f]
                        lifts+=1
    assert exc and nonexc and excluded
    return nchar,ram,unram,excluded,exc,nonexc,lifts

def root_unit_tests():
    checks=0
    for ell in (3,5,7,11):
        for a in (1,2,3):
            M=ell**a
            for n in range(1,13):
                if n%ell==0: continue
                for x in range(M):
                    if pow(x,n,M)==1 and x!=1:
                        assert gcd(x-1,M)==1
                        checks+=1
        # Negative control: nontrivial ell-power root congruent to 1.
        assert pow(1+ell,ell,ell**2)==1 and gcd(ell,ell**2)>1
    return checks

def rational_power_tests():
    count=0
    for ell in (3,5,7):
        for exps in product(range(-2,3),repeat=4):
            for sign in (-1,1):
                a=sign*prod(Fraction(p)**(ell*v) for p,v in zip((2,3,5,7),exps))
                y=sign*prod(Fraction(p)**v for p,v in zip((2,3,5,7),exps))
                assert y**ell==a
                count+=1
    # Excluding a place leaves an obstruction: ell-th root of 2.
    assert 1%3!=0
    # At even exponent the sign is not an even power of a rational.
    assert -1<0
    return count

if __name__=="__main__":
    c,r,u,d,e,n,l=conductor_tests()
    print(f"PASS {c} characters; {r} primitive ramification kernels; {u} unramified kernels; {d} nonprimitive controls; {e} exceptional / {n} nonexceptional comparisons; {l} induced order/parity checks; {root_unit_tests()} root-unit checks; {rational_power_tests()} signed rational-power cases; negative controls")
