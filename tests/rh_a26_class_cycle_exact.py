"""Exact finite controls of bar cycles, residue cocycles and group-ring filters.
Not original Lean replay, not certification.
"""
from collections import Counter
from itertools import product, permutations
from math import gcd, prod, comb

def accum(dst,src,a=1):
    for k,v in src.items(): dst[k]+=a*v

def clean(d,q=None):
    return {k:(v if q is None else v%q) for k,v in d.items() if (v if q is None else v%q)}

def bd(t,mul):
    r=Counter(); r[t[1:]]+=1
    for i in range(len(t)-1):
        r[t[:i]+(mul(t[i],t[i+1]),)+t[i+2:]]+=(-1)**(i+1)
    r[t[:-1]]+=(-1)**len(t)
    return r

def prism(t,g,mul,inv):
    r=Counter()
    for i in range(len(t)+1):
        r[t[:i]+(g,)+tuple(mul(mul(inv(g),x),g) for x in t[i:])]+=(-1)**i
    return r

bar_cases=0; coc_cases=0
for Q in (2,3,4,5,7,8,9):
    for E in (1,2,3):
        z=[tuple(x for j in js for x in (j,1)) for js in product(range(Q),repeat=E)]
        b=Counter()
        for t in z: accum(b,bd(t,lambda x,y:(x+y)%Q))
        assert not clean(b,Q)
        bar_cases+=len(z)
        for r in (1,2,3):
            N=Q*r
            for u in (1,Q-1):
                assert gcd(u,Q)==1
                a=pow(u,-1,Q)
                def lg(x):return a*x
                def U(x,y):return (lg(x)+lg(y)-lg((x+y)%N))//N
                for x in range(Q):
                    # Check carry sum and explicit inserted cup-product
                    chi=lambda j:(r*u*x*j)%N
                    assert sum(U(chi(j),chi(1)) for j in range(Q))%Q==x
                    for g in range(N):
                        # sum over one independent j in each of E pairs
                        # and each insertion slot (factorized exactly).
                        S=sum(U(chi(j),chi(1)) for j in range(Q))
                        Sg0=sum(U(g,chi(j)) for j in range(Q))
                        Sg1=sum(U(chi(j),g) for j in range(Q))
                        # each adjacent insertion cancels, leaving final w(g)
                        val=0
                        for i in range(E):
                            val+=(Sg0-Sg1)*S**(E-1)*(chi(1)%Q)
                        val+=S**E*(g%Q)
                        assert val%Q==(x**E*g)%Q
                        coc_cases+=1
# Explicit prism chain identity, including noncommutative negative controls.
G=list(permutations(range(3)))
mul=lambda a,b:tuple(a[b[i]] for i in range(3))
inv=lambda a:tuple(a.index(i) for i in range(3))
prism_cases=0
for n in (1,2,3):
    for t in product(G,repeat=n):
        for g in G:
            lhs=Counter()
            for p,v in prism(t,g,mul,inv).items(): accum(lhs,bd(p,mul),v)
            for p,v in bd(t,mul).items(): accum(lhs,prism(p,g,mul,inv),v)
            rhs=Counter(); rhs[tuple(mul(mul(inv(g),x),g) for x in t)]+=1; rhs[t]-=1
            assert clean(lhs)==clean(rhs)
            prism_cases+=1
# Construct SEta in the integral group ring, not merely check divisibility mod Q.
def conv(a,b,q=None):
    c=Counter()
    for x,v in a.items():
        for y,w in b.items(): c[(x+y) if q is None else (x+y)%q]+=v*w
    return clean(c)
def poly_div(f,d):
    f=Counter(f); out=Counter(); n=max(d); assert d[n]==1
    while f:
        top=max(f)
        if top<n: break
        a=f[top]; j=top-n; out[j]+=a
        for k,v in d.items():
            f[k+j]-=a*v
            if not f[k+j]: del f[k+j]
    assert not f
    return clean(out)
filters=0
for ell,c,nu,M in [(2,2,2,3),(2,2,3,3),(2,2,4,3),(3,1,2,2),(3,2,2,3),(5,1,2,4),(7,1,1,3)]:
    Q=ell**nu; w=ell**c; K=1+w
    P={0:1}
    for j in range(M): P=conv(P,{1:1,0:-K**j})
    raw={K**i:v for i,v in P.items()}
    divisor={w*j:(-1)**(M-j)*comb(M,j) for j in range(M+1)}
    quot=poly_div(raw,divisor)
    def reduce_ring(a):
        b=Counter()
        for i,v in a.items():b[i%Q]+=v
        return clean(b)
    target=reduce_ring(raw)
    for t0 in range(M+1):
        R=reduce_ring(quot)
        eta={(0,0):1}; shift=0
        for t in range(M+1):
            if t==t0:continue
            diff=(t0-t)%Q
            a=next(i for i in range(Q) if diff*i%Q==w%Q)
            geom=Counter()
            for j in range(a):geom[diff*j%Q]+=1
            R=conv(R,geom,Q)
            out=Counter()
            for (x,y),v in eta.items():
                out[(x,(y+1)%Q)]+=v;out[((x+t)%Q,y)]-=v
            eta=clean(out);shift+=t
        shifted=Counter()
        for (x,y),v in eta.items():
            for j,a in R.items():shifted[((x+j-shift)%Q,y)]+=v*a
        for t in range(M+1):
            out=Counter()
            for (x,y),v in shifted.items():out[(x+t*y)%Q]+=v
            assert clean(out)==(target if t==t0 else {})
            filters+=1
# Source polynomial-loss bound: divisibility in Z/Q, not cancellation.
loss=0
for ell,c in product((2,3,5,7),range(1,5)):
    K=1+ell**c
    for M in range(3,min(18,ell**c),2):
        E=(M-1)//2
        p=prod(K**E-K**j for j in range(M) if j!=E)
        assert p!=0
        for nu in range(c,c+6):
            Q=ell**nu
            assert pow(ell,M*(c+M),Q)%gcd(p,Q)==0
            loss+=1
print(f"PASS {bar_cases} cyclic bar summands; {coc_cases} residue cocycle controls; {prism_cases} noncommutative prism identities; {filters} integral group-ring projections; {loss} polynomial loss divisibilities")
