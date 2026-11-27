"""Exact finite controls of source eta/K and simplex comparison.
Affine barycentric partition on a finite simplex, not the arithmetic PU.
Cyclic group invariant coboundaries need not be alternating. Tests do not
establish existence of the arithmetic partition or original formal replay.
"""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial

def delete(g,i):return g[:i]+g[i+1:]
def delta(f,g):return sum((-1)**i*f(delete(g,i)) for i in range(len(g)))

def check(n,p):
    G=tuple(range(n))
    def b(g):
        d=tuple((x-g[0])%n for x in g)
        return sum((i+1)*(x+1)**2 for i,x in enumerate(d))+prodcode(d)
    def c(g):return delta(b,g)
    @lru_cache(None)
    def eta(j,prefix,edges):
        if j==0:return c(prefix)
        # d psi_gamma(e) is difference of vertex coordinate indicators.
        return sum((-1)**i*((v==a)-(u==a))*eta(j-1,(a,)+prefix,delete(edges,i))
                   for i,(u,v) in enumerate(edges) for a in G if (v==a)!=(u==a))
    def edges(y):return tuple((y[0],v) for v in y[1:])
    def W(j,g):
        return F(eta(j,g[:p-j+1],edges(g[p-j:])),factorial(j))
    def B(j,g):
        y=g[p-j-1:];prefix=g[:p-j]
        return F(sum(eta(j,(a,)+prefix,edges(y)) for a in y),factorial(j)*(j+1))
    count=0;ntop=0;nonalt=0
    for g in product(G,repeat=p+1):
        assert W(0,g)==c(g)
        for j in range(p):
            assert delta(lambda h:B(j,h),g)==W(j,g)+(-1)**(p-j-1)*W(j+1,g)
            count+=1
        s=1;bs=[]
        for j in range(p):
            bs.append(s);s*= -(-1)**(p-j-1)
        assert s==(-1)**(p*(p+1)//2)
        assert c(g)==delta(lambda h:sum(bs[j]*B(j,h) for j in range(p)),g)+s*W(p,g)
        E=edges(g)
        assert all(eta(p,(a,),E)==eta(p,(0,),E) for a in G)
        assert all(W(p,tuple((v+a)%n for v in g))==W(p,g) for a in G)
        ntop+=1
        if len(set(g))<len(g) and c(g):nonalt+=1
    # The contraction identity on arbitrary (not necessarily cocycle) cochains.
    contractions=0
    for g in product(G,repeat=p+1):
        def raw(t):return prodcode(t)
        for a in G:
            def K(f,t):return f((a,)+t)
            assert delta(lambda t:K(raw,t),g)+K(lambda t:delta(raw,t),g)==raw(g)
            contractions+=1
    return count,ntop,nonalt,contractions

def prodcode(g):
    r=1
    for x in g:r=r*(x+2)+3
    return r

def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def partial(g):
    out=[(0,1,2)]
    for h in g:out.append(mul(out[-1],h))
    return tuple(out)
def bar_controls():
    G=tuple(permutations(range(3)));count=0
    for p in range(1,5):
        for g in product(G,repeat=p):
            y=partial(g)
            for i in range(p+1):
                if i==0:
                    assert delete(y,0)==tuple(mul(g[0],h) for h in partial(g[1:]))
                elif i==p:assert delete(y,i)==partial(g[:-1])
                else:assert delete(y,i)==partial(g[:i-1]+(mul(g[i-1],g[i]),)+g[i+1:])
                count+=1
    return count

if __name__=="__main__":
    total=[0]*4
    for n,p in ((3,1),(3,2),(3,3),(3,4),(4,2),(4,3)):
        total=[a+b for a,b in zip(total,check(n,p))]
    assert total[2]>0
    for label,v in zip(("signed descent faces","top independence/equivariance","nonalternating cocycle controls","contraction identities"),total):
        print("PASS",label,v)
    print("PASS noncommutative bar faces",bar_controls())
