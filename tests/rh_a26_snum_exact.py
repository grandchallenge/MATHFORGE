"""Exact rational/integer controls of numerical absorption; not Lean replay."""
from fractions import Fraction as F
from itertools import product
from math import factorial

facts=0
for n in range(1,101):
    assert 2**(n-1)*factorial(n)<=n**n
    facts+=1
# Tuple count by recursion and rational harmonic majorant.
from functools import lru_cache
@lru_cache(None)
def tuples(n,x):
    if n==1:return x
    return sum(tuples(n-1,x//j) for j in range(1,x+1))
tc=0
for n,x in product(range(1,9),range(1,101)):
    H=sum((F(1,j) for j in range(1,x+1)),F(0))
    assert tuples(n,x)<=x*H**(n-1)
    tc+=1
poly=0
for u,Y in product(range(2,65),(F(1,2),F(2,3),F(1),F(3,2),F(10),F(100))):
    b=u+2*u*u; g=u+2*u*Y+2; c=v=t=u
    assert b+v<=3*u*u and g<=6*u*Y
    assert ((b+v)*g+c+v)*t<=19*u**4*Y<=u**9*Y
    for C in (-3,0,9,24,40):
        A=F(u)**max(C,9)*Y
        assert A>=1 and 4*A<=u**(max(C,9)+2)*Y
        poly+=1
down=0
for E,n in product(range(1,41),range(1,41)):
    x=2*E*n; d=(n+1)*(4*E+4); n1=d*n; w=2*n1
    assert d<=8*x and n1<=4*x*x and 2*E*n1<=x**5
    # Rational majorant for log(2D'), using log(w)<=w and Z>=1/2.
    for Z in (F(1,2),F(1),F(10)):
        Y=Z+d*Z+n1*w
        assert Y<=73*x**4*Z<=x**11*Z
        for C in (0,1,9,26):
            assert (2*E*n1)**C*Y<=x**(5*C+11)*Z
            down+=1
assert 5*(max(24,9)+2)+11==141
print(f"PASS {facts} Minkowski factorial bounds; {tc} ideal tuple majorants; {poly} arithmetic and exponential absorption controls; {down} layer descent controls")
