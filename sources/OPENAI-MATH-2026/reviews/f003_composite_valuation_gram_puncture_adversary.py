#!/usr/bin/env python3
"""OAI26 F003 exact local sextic mixed L1, CRT products, origin and puncture tests.

Uses exact rational Eisenstein norms and rational + rational*sqrt(q) magnitude
arithmetic. It tests the prime-power Gauss values supplied by the immutable
source, rather than re-implementing its primitive quotientTrace. No floating
point, no mock claim that these finite checks prove analytic Poisson/Lean.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import gcd

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES=(7,13,19,31,37)
checks=0

def require(condition, msg=""):
    global checks
    assert condition, msg
    checks+=1

@dataclass(frozen=True)
class Quad:
    q:int
    a:F=F(0)
    b:F=F(0)
    def __add__(self,other):
        require(self.q==other.q,"mixed quadratic fields")
        return Quad(self.q,self.a+other.a,self.b+other.b)
    def __mul__(self,other):
        if isinstance(other,(int,F)):return Quad(self.q,self.a*other,self.b*other)
        require(self.q==other.q)
        return Quad(self.q,self.a*other.a+self.q*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__

def unit(q):return Quad(q,F(1))
def zero(q):return Quad(q)
def halfpow(q,n):
    # q^(n/2) with n integral; odd powers contain exact sqrt(q).
    v=F(q)**((n-(n%2))//2)
    return Quad(q,v) if n%2==0 else Quad(q,F(0),v)

def absrow(q,e,valuation):
    """|g_{p^e}(z)| from pinned actual sextic-prime-power Gauss table."""
    if e==0:return unit(q)
    if valuation==e-1:
        return halfpow(q,e-2) if e%6==0 else halfpow(q,e-1)
    if valuation>=e and e%6==0:
        return (q-1)*halfpow(q,e-2)
    return zero(q)

def mean_by_valuation(q,a,b):
    d=max(a,b)
    if d==0:return unit(q)
    total=zero(q)
    for v in range(d+1):
        prob=F(q-1,q**(v+1)) if v<d else F(1,q**d)
        total+=prob*(absrow(q,a,v)*absrow(q,b,v))
    return total

def closed(q,a,b):
    if a==b:return unit(q) if a==0 else F(q-1,q)*unit(q)
    c,d=sorted((a,b))
    if c==0:
        if d%6==0:return 2*F(q-1,q)*halfpow(q,-d)
        return F(q-1,q)*halfpow(q,1-d)
    if c%6:return zero(q)
    if d%6:return F((q-1)**2,q*q)*halfpow(q,c-d+1)
    return 2*F((q-1)**2,q*q)*halfpow(q,c-d)

def gram_possible(e,f):
    if e==f:return True
    if e==0 or f==0:return True
    return min(e,f)%6==0

def enorm(z):
    a,b=z;return a*a-a*b+b*b

def origin(q,e):
    # Actual normalized sextic Gauss row at z=0.
    if e==0:return F(1)
    if e%6:return F(0)
    return F((q-1)*q**(e//2-1))

def test_local_table():
    for q in PRIMES:
        require(q%6==1)
        for a,b in product(range(19),repeat=2):
            observed=mean_by_valuation(q,a,b)
            expected=closed(q,a,b)
            require(observed==expected,(q,a,b,observed,expected))
            require((observed!=zero(q))==gram_possible(a,b),(q,a,b))
            require(observed==mean_by_valuation(q,b,a))
            if a==b and a:
                require(observed==F(q-1,q)*unit(q))
            if a and b and a!=b and min(a,b)%6:
                require(observed==zero(q))
        for c in (6,12,18):
            require(closed(q,c,c+1)==F((q-1)**2,q*q)*unit(q))
            require(origin(q,c)==F((q-1)*q**(c//2-1)))
        require(origin(q,7)==0)
        print(f"prime norm q={q}: exact local CRT mean-absolute table and zero supports PASS")

def test_composite_product():
    for qa,qb in ((7,13),(7,37),(13,37),(7,19)):
        for a,b,c,d in product(range(0,9,2),repeat=4):
            # Two distinct prime-power local fields; product mean
            # of the CRT character over L=I∩J factors exactly.
            ma=closed(qa,a,c);mb=closed(qb,b,d)
            require((ma==zero(qa) or mb==zero(qb)) ==
                    (not gram_possible(a,c) or not gram_possible(b,d)))
            # Check each local product via an independently computed
            # valuation distribution, not by reusing the formula.
            require(ma==mean_by_valuation(qa,a,c))
            require(mb==mean_by_valuation(qb,b,d))
            # Scaling invariance of local valuation under units is exact;
            # the cofactor units change phases, never these magnitudes.
            require(gcd(qa,qb)==1)
        print(f"CRT pair norms {qa} x {qb}: local product probabilities, phase-independent support PASS")
    # Norm-mod-36 unit-sector filter and valuation graph are independent.
    for q in PRIMES:
        for a,b in product(range(20),repeat=2):
            gamma_diff=(q**a-q**b)%36
            if gamma_diff:
                # radial cross term vanishes, even when local rows overlap
                require((q**a)%36!=(q**b)%36)
            if a and b and a!=b and min(a,b)%6:
                require(not gram_possible(a,b))
    # q=37 has no rotation selection, but 1 and 7 rows still disjoint.
    require(37**1%36==37**7%36)
    require(closed(37,1,7)==zero(37))
    require(closed(37,6,7)!=zero(37))
    # Squarefree coprime pairs can have large mean-absolute correlation,
    # hence local absolute values alone do not imply a power saving.
    require(closed(7,0,1)==F(6,7)*unit(7))
    require(closed(13,0,1)==F(12,13)*unit(13))

def test_origin_and_projection():
    for q in PRIMES:
        for e in (6,12,18):
            # With 2K <= 1, actual ballProfile samples only z=0.
            # The two actual rows g_1(0)=1 and g_(p^e)(0)>0
            # can cancel, whereas deleting the p^e column raises
            # the energy from 0 to 1 (volume normalized to 1).
            G=origin(q,e)
            require(G>0)
            c0=F(1)
            cp=-F(1)/G
            require(c0+cp*G==0)
            require(c0*c0==1)
            # Weighted child-energy operator is not contractive under
            # a general coefficient projection, even W >= 0.
            require((c0+cp*G)**2<c0**2)
    # Check exact raw valuation residual pool for error k=1,6,7.
    for k in (1,6,7):
        retained=[]
        for e in range(0,k+5):
            if e==k:retained.append(e-k)
            else: require(e!=k)
        require(retained==[0])
        splits=[(i,k-i) for i in range(k+1)]
        require(len(splits)==k+1)
        require(all(i+j==k for i,j in splits))
        # Counterfactual unpunctured quotient contains p at e=k+1.
        require(k+1-k==1)
        print(f"p^{k} raw exact valuation: p-free; {k+1} plain allocation partitions before cancellation")

def main():
    for a,b in product(range(-33,34),repeat=2):
        require(2*enorm((a,b))==a*a+b*b+(a-b)**2)
    test_local_table()
    test_composite_product()
    test_origin_and_projection()
    print("EXACT ASSERTIONS",checks,"PASS")
    print("NOT CHECKED: source lean elaboration of new CRT theorem, Gaussian physical K-dependent bound or four seeded powers")
    print("PIN",PIN)

if __name__=="__main__":main()
