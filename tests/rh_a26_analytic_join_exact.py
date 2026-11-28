"""Finite rational controls of analytic assembly, not source replay."""
from fractions import Fraction as F
from itertools import product
from math import isqrt

# Rank selection and moment exponent, independent of cocycle.
ranks=0
for n0,n1,n2,a,q in product(range(6),range(6),range(6),range(4),range(1,5)):
    n=max(n0,n1,n2,3)
    assert n>=n0 and n>=n1 and n>=n2 and n>=3
    assert 2*(a*q)==a*(2*q)
    ranks+=1
# Weighted means, including zero measure under source inverse convention.
means=0
for weights in product(range(3),repeat=3):
    for vals in product(range(-2,3),repeat=3):
        mass=sum(weights)
        m=F(sum(w*v for w,v in zip(weights,vals)),mass) if mass else F(0)
        assert sum(w*(v-m) for w,v in zip(weights,vals))==0
        assert all((v-m)**2<=2*v*v+2*m*m for v in vals)
        means+=1
# Exact normalized two-state Hecke analogue with eigenvalues 1 and 3/5.
# This tests finite linear transport only, not actual arithmetic gap.
def T(v):
    a,b=v
    return (F(4,5)*a+F(1,5)*b,F(1,5)*a+F(4,5)*b)
iterations=0
for a,b in product(range(-5,6),repeat=2):
    m=F(a+b,2)
    v=(a-m,b-m)
    initial=sum(x*x for x in v)
    for r in range(12):
        assert sum(v)==0
        assert sum(x*x for x in v)==F(9,25)**r*initial
        v=T(v)
        iterations+=1
# Two distinct warnings: decay alone does not imply original value zero;
# a nonzero mean is not contracted.
assert T((F(1),F(-1)))==(F(3,5),F(-3,5))
assert T((F(1),F(1)))==(F(1),F(1))
# Rational-prime special case only (not general principal prime theorem).
primes=[n for n in range(26,100) if all(n%d for d in range(2,isqrt(n)+1))]
assert primes[0]==29
print("PASS",ranks,"rank/exponent cases;",means,"weighted mean cases;",iterations,"exact contraction steps; 2 negative controls; Q prime witness",primes[0])
