"""Exact finite controls of SLoc mechanisms, not a numerical proof of SLoc."""
from fractions import Fraction as Q
from itertools import product
from math import prod, comb

def compositions(n,k):
    if k==1:
        yield (n,);return
    for i in range(n+1):
        for rest in compositions(n-i,k-1):yield (i,)+rest

def jacobian():
    count=0
    for q,d in product(range(5),range(1,5)):
        for a in compositions(8,q+1):
            tau=[Q(x,8) for x in a]
            i=max(range(q+1),key=tau.__getitem__)
            assert tau[i]>=Q(1,q+1)
            for det in (Q(1,3),Q(1),Q(5,2)):
                assert 1/(tau[i]**d*det)<=Q((q+1)**d)/det
                count+=1
    return count

def avg():
    # F(a,b,c)=dE(a,b,c), with E translation invariant. Verify the
    # actual product-marginal/cycle mechanism for every mixed flag.
    n=5; samples=(0,1,3)
    def E(a,b):return ((b-a)%n)**2
    def F(a,b,c):return E(b,c)-E(a,c)+E(a,b)
    def Fp(p):
        return sum(F(*[((h+x)%n if b else h) for (h,b),x in zip(p,xs)])
                   for xs in product(samples,repeat=3))/Q(27)
    count=0
    for hs in product(range(n),repeat=4):
        for bs in product((0,1),repeat=4):
            p=list(zip(hs,bs))
            assert sum((-1)**i*Fp(p[:i]+p[i+1:]) for i in range(4))==0
            count+=1
    # Cycle in bar complex: [a|b]-[b|a] for commuting group.
    for a,b in product(range(n),repeat=2):
        for flag in (0,1):
            assert Fp([(0,flag),(a,flag),((a+b)%n,flag)])-Fp([(0,flag),(b,flag),((a+b)%n,flag)])==0
    return count

def overlap():
    count=0
    for a,b in product(range(-7,8),repeat=2):
        if b<a:continue
        lo,hi=Q(a,3),Q(b,3)
        M=2*int(hi-lo)+1
        for j in range(24):
            x=Q(j,24)
            hits=[g for g in range(-10,11) if lo<=g+x<=hi]
            assert len(hits)<=M
            if hits:assert all(abs(g-hits[0])<=hi-lo for g in hits)
            count+=1
    return count

def triangle_density():
    # Exact integration of density for (U+V)/2, U,V uniform [0,1].
    # f(s)=4s (0<=s<=1/2), 4(1-s) (1/2<=s<=1).
    def cdf(x):
        return 2*x*x if x<=Q(1,2) else 1-2*(1-x)**2
    count=0
    for i in range(65):
        for j in range(i,65):
            a,b=Q(i,64),Q(j,64)
            assert 0<=cdf(b)-cdf(a)<=2*(b-a)
            count+=1
    assert cdf(Q(1,1))==1
    return count

def scalar_frame():
    # In dimension one, omega_p(v)=v/p is scalar invariant and fr=1.
    count=0
    for p,s,v in product(range(1,11),range(1,8),range(-5,6)):
        a=Q(1,s*s)
        assert Q(a*v,a*p)==Q(v,p)
        assert Q(a,a)==1
        count+=1
    return count

if __name__=="__main__":
    print("PASS barycentric determinant controls:",jacobian())
    print("PASS mixed-flag averaged cocycle identities:",avg())
    print("PASS compact overlap controls:",overlap())
    print("PASS interval density bounds:",triangle_density())
    print("PASS scalar frame identities:",scalar_frame())
