"""Finite arithmetic checks of source thresholds and CRT, not homology replay."""
from itertools import product
from math import gcd
from functools import reduce

def primes(n):
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0: n//=p
        p+=1
    if n>1: out.append(n)
    return out

crt=0
for a,b,c in product(range(-16,17),repeat=3):
    if gcd(gcd(a,b),c)!=1: continue
    row=[a,b]
    if not any(row):
        assert abs(c)==1
        row[0]+=c
    else:
        j=0 if a else 1
        k=1-j
        ps=primes(row[j])
        modulus=reduce(lambda x,y:x*y,ps,1)
        t=next(x for x in range(modulus) if all(x%p==(1 if row[k]%p==0 else 0) for p in ps))
        row[k]+=t*c
    assert gcd(*row)==1
    crt+=1
range_checks=0
for i,s in product(range(41),range(1,9)):
    for inj in (False,True):
        n=2*i+s+1+int(inj)
        assert n+1>=2*(i+int(inj))+s+1
        assert n+1>=i+2+int(inj)+s
        for p in range(1+int(inj),i+1+int(inj)):
            q=i+int(inj)-p
            assert 0<=q<i
            if p%2==0:
                assert n-p>=2*q+s+2
            else:
                assert n-(p+1)>=2*q+s+1
            range_checks+=1
        assert n>=2*i+max(1,s-1)
for p in range(101):
    assert sum((-1)**j for j in range(p+1))==int(p%2==0)
for e in range(1001):
    k=2*e+2; E=e+1
    N=2*(k+1)+4
    assert N==4*E+6
    assert k==2*E and k+1==2*E+1
    assert N>=2*k+4
print(f"PASS {crt} CRT row shortenings; {range_checks} diagonal checks; 101 alternating signs; 1001 torsion rank joins")
