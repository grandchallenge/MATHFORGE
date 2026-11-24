"""Finite exact controls for RH-A26 torsion/count/reciprocity mechanisms.

No finite group fixture proves a Galois reciprocity theorem or an Euler system.
"""
from itertools import product
from math import gcd

def v(n,p):
    assert n != 0
    k=0
    while n%p==0:
        n//=p
        k+=1
    return k

def test_cocycles(p,m):
    # Dihedral group C_m ⋊ C2, coefficients Z/m with reflection acting by -1.
    # Add a central C_m for a genuinely distinct inertia/decomposition group.
    G=list(product(range(m),range(2),range(m)))
    def mul(g,h):
        i,s,j=g; x,t,y=h
        return ((i+(-1)**s*x)%m,(s+t)%2,(j+y)%m)
    def inv(g):
        i,s,j=g
        return ((-(-1)**s*i)%m,s,-j%m)
    def alpha(g): return (-1)**g[1]
    def nu(g): return g[0]
    delta=(0,1,0)
    U=[g for g in G if g[1]==0]
    invu=pow(-2,-1,m)
    def comm(g,h): return mul(mul(mul(g,h),inv(g)),inv(h))
    def ext(g): return invu*nu(comm(delta,g))%m
    assert all(ext(g)==nu(g) for g in U)
    assert ext(delta)==0
    checks=0
    for a in (1,p,m-1):
        for b in (0,1,p):
            def c(g): return (a*ext(g)+(alpha(g)-1)*b)%m
            normalizer=invu*c(delta)%m
            def c0(g): return (c(g)-(alpha(g)-1)*normalizer)%m
            assert normalizer==b%m
            assert all(c0(g)==a*g[0]%m for g in G)
            # D=<reflection> × central C_m; I=<reflection>, normal in D.
            # Common inertia witness extends to D and is killed when c is.
            for g in G:
                if g[0]==0:
                    assert c(g)==(alpha(g)-1)*b%m
            for g,h in product(G,repeat=2):
                assert ext(mul(g,h))==(ext(g)+alpha(g)*ext(h))%m
                assert c0(mul(g,h))==(c0(g)+alpha(g)*c0(h))%m
                checks+=1
    return checks

def test_cups(p):
    # G = C_p × C_p × C2; alpha trivial, beta=chi=sign is
    # not used here since conjugation forces any sign homomorphism on C_p zero.
    # Use D_{2p} × C_p, beta=sign, alpha=1, chi=sign.
    G=list(product(range(p),range(2),range(p)))
    def mul(g,h):
        i,s,j=g; x,t,y=h
        return ((i+(-1)**s*x)%p,(s+t)%2,(j+y)%p)
    def beta(g): return (-1)**g[1]
    def n(g): return g[0]
    def c(g): return g[2]
    def W(g,h): return n(g)*c(h)%p
    checks=0
    for g,h,k in product(G,repeat=3):
        assert (beta(g)*W(h,k)-W(mul(g,h),k)+W(g,mul(h,k))-W(g,h))%p==0
        checks+=1
    # Nonzero product for commuting elements of the two C_p factors:
    # W(g,h)-W(h,g)=1. With trivial action on those factors, this is
    # impossible for a 2-coboundary there. Arbitrary groups do not satisfy Rec.
    g,h=(1,0,0),(0,0,1)
    assert W(g,h)-W(h,g)==1
    return checks

def test_local_coboundary(p):
    # alpha=beta=sign, chi=1; n(g)=first coordinate of D_{2p}.
    G=list(product(range(p),range(2)))
    def mul(g,h): return ((g[0]+(-1)**g[1]*h[0])%p,(g[1]+h[1])%2)
    def alpha(g): return (-1)**g[1]
    checks=0
    for b in range(p):
        def C(g): return (alpha(g)-1)*b%p
        def W(g,h): return g[0]*alpha(g)*C(h)%p
        def V(g): return -g[0]*alpha(g)*b%p
        for g,h in product(G,repeat=2):
            assert W(g,h)==(V(h)-V(mul(g,h))+V(g))%p
            checks+=1
    return checks

def test_budget():
    # Exact torsion layers over Z/p^J. Evaluation maps with image killed
    # by p^e have image cardinality <= p^e and length drop <= e.
    checks=0
    for p in (2,3,5):
        for J in range(1,5):
            M=p**J
            for e in range(J+1):
                for x in range(M):
                    if x*p**e%M: continue
                    image_size=M//gcd(M,x)
                    # f: Z/M -> Z/M by multiplication x.
                    ker_size=gcd(M,x)
                    assert image_size*ker_size==M
                    assert v(image_size,p)<=e
                    assert J<=v(ker_size,p)+e
                    checks+=1
    # Nonuniform bounds fail: layer of order p^k has length k.
    assert [v(3**k,3) for k in range(1,9)]==list(range(1,9))
    return checks

if __name__=="__main__":
    n=sum(test_cocycles(p,m) for p,m in ((3,3),(3,9),(5,5)))
    c=test_cups(3)
    l=sum(test_local_coboundary(p) for p in (3,5,7))
    b=test_budget()
    print(f"PASS {n} cocycle checks; {c} cup identities; {l} local coboundary checks; {b} budget cases; two negative controls")
