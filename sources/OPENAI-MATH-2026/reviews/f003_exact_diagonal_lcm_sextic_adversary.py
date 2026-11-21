#!/usr/bin/env python3
"""Exact bounded adversary for pinned OAI26 F003 full-diagonal/lcm/sextic audit.

Integer Eisenstein quotient calculations are unit-mask/primitive-pairing examples,
not a construction of the actual Hecke sextic characters. The sextic valuation
identities are checked symbolically against the source's closed local tables.
Does not certify infinite Poisson estimates, new Lean theorems, or MATHCERT.
"""
from fractions import Fraction
from itertools import product
from math import gcd, lcm

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
total=0

def check(x, msg=""):
    global total
    assert x, msg
    total+=1

def enorm(z):
    a,b=z
    return a*a-a*b+b*b

def trcoeff(z):
    a,b=z
    return 2*a-b,-a-b

def vals(m):
    return product(range(m),repeat=2)

def units(m):
    return [z for z in vals(m) if gcd(enorm(z),m)==1]

def pair_zero(x,m,y,n):
    L=lcm(m,n)
    a,b=trcoeff(x)
    c,d=trcoeff(y)
    return ((L//m*a-L//n*c)%L==0 and (L//m*b-L//n*d)%L==0)

def norm_sq(q,c,j):
    # row g_{p^c}, normalized by q^(c/2); j=c means zero mod p^c
    if c%6:
        return q**(c-1) if j==c-1 else 0
    if j==c-1:
        return q**(c-2)
    if j>=c:
        return (q-1)**2*q**(c-2)
    return 0

def cardinal_val(q,d,j):
    return (q-1)*q**(d-j-1) if j<d else 1

def fpow(q,expo):
    if expo>=0: return Fraction(q**expo)
    return Fraction(1,q**(-expo))

def main():
    for a,b in product(range(-40,41),repeat=2):
        check(2*enorm((a,b))==a*a+b*b+(a-b)**2)
    ms=(2,4,5,7,8,10,11,16)
    us={m:units(m) for m in ms}
    for m in ms:
        U=us[m]
        for x in U:
            for y in U:
                check(pair_zero(x,m,y,m)==(x==y),
                      f"diagonal primitive pairing at {m}: {x},{y}")
        check(Fraction(len(U),m*m)<=1)
        print(f"integer ideal ({m}) diagonal: units={len(U)}, mean norm^2={Fraction(len(U),m*m)}")
    ps=((2,4),(2,8),(2,16),(4,8),(4,16),(8,16),
        (2,10),(5,10),(4,10),(5,20),(4,20),(10,20),
        (5,25),(7,14))
    us[20]=units(20)
    us[25]=units(25)
    us[14]=units(14)
    for m,n in ps:
        for x in us[m]:
            for y in us[n]:
                check(not pair_zero(x,m,y,n),
                      f"shared-prime mixed zero-frequency not zero: {m} {n} {x} {y}")
        L=lcm(m,n)
        check(m*n//gcd(m,n)==L)
        check((m*n)**2//(L*L)==gcd(m,n)**2)
        check(L*L<=m*m*n*n)
        print(f"shared-prime ({m}),({n}): zero mode exactly vanishes; pair period norm={L*L}, product norm={(m*n)**2}")
    # The uncorrected trace is degenerate mod 3 (intentional hostile test).
    check((2*2-1)%3==0)
    check((-2-1)%3==0)
    # Do not generalize this raw trace to the pinned primitive quotientTrace.
    for q in (7,13,19,31): # q=1 mod 6; compatible with a genuine order-six character
        for c in range(1,19):
            powersum=sum(cardinal_val(q,c,j)*norm_sq(q,c,j)
                         for j in range(c+1))
            check(Fraction(powersum,q**c)==Fraction(q-1,q),
                  f"diagonal Plancherel q={q},c={c}")
            for d in range(c+1,19):
                intersect=[j for j in range(d+1)
                           if norm_sq(q,c,j)>0 and norm_sq(q,d,j)>0]
                check(bool(intersect)==(c%6==0),
                      f"unequal support q={q},c={c},d={d}")
                if c%6: continue
                if d%6:
                    check(intersect==[d-1])
                    numer=cardinal_val(q,d,d-1)**2 * norm_sq(q,c,d-1)*norm_sq(q,d,d-1)
                    observed=Fraction(numer,q**(2*d))
                    expected=(Fraction(q-1,q)**4)*fpow(q,c-d+1)
                    check(observed==expected,
                          f"mixed L1 square q={q},c={c},d={d}: {observed} != {expected}")
                else:
                    check(intersect==[d-1,d])
                    # Both exponents divisible by six -> exact integer-valued
                    # square roots of local amplitude products.
                    b=q**((c+d-4)//2)
                    val=(cardinal_val(q,d,d-1)*(q-1)*b + 
                         cardinal_val(q,d,d)*(q-1)**2*b)
                    observed=Fraction(val,q**d)
                    expected=2*Fraction((q-1)**2,q**2)*fpow(q,(c-d)//2)
                    check(observed==expected,
                          f"principal/principal mixed L1 q={q},c={c},d={d}")
        # Hostile surviving first case, before sqrt normalizations:
        g6=(q-1)*q**5
        g7_coeff=q**6  # multiplied by nonzero prime Gauss tau(chi), |tau|^2=q
        check(g6!=0 and g7_coeff!=0)
        check(Fraction((q-1)**2,q**2)>0)
        print(f"sextic q={q}: low unequal powers annihilate; p^6/p^7 survives; local means PASS")
    for Z in (2,3,5,7):
        for rho in range(2,16):
            for d in range(0,rho):
                if (rho-d)%2: continue
                for A in (2,4,8,12):
                    k=Z**rho
                    l=Z**d
                    u=Z**((rho-d)//2)
                    check(k==l*u*u)
                    check(Fraction(l,(1+u)**A)<=fpow(Z,d-A*(rho-d)//2),
                          f"conditional period Poisson exponent {Z},{rho},{d},{A}")
    print("EXACT ASSERTIONS",total,"PASS")
    print("BOUNDARY: source's actual character, infinite lattice Poisson, global seeded energies not replayed by finite tests")
    print("BOUNDARY: first nonzero sixth-power shared-prime survivor p^6/p^7 remains")
    print("PIN",PIN)

if __name__=="__main__":
    main()
