"""Finite exact controls of SSha mechanisms, not original kernel replay."""
from itertools import product
from math import gcd

# Cyclic image order, nontrivial action, finite torsion divisibility lifts.
orders=lifts=signs=0
for p,c in product((2,3,5,7),range(1,4)):
    if p==2 and c<2:continue
    k=1+p**c
    for nu in range(c,c+5):
        q=p**nu;n=p**(nu-c)
        assert pow(k,n,q)==1
        if n>1:assert pow(k,n//p,q)!=1
        orders+=1
        for E in range(1,17):
            a=k**E;v=0;t=a-1
            while t%p==0:t//=p;v+=1
            for r in range(1,5):
                Q=p**r; big=p**(r+v)
                coeff=(pow(k,-E,big)-1)%big
                unit=coeff//p**v
                assert gcd(unit,p)==1
                for x in (0,1,Q//2,Q-1):
                    # x/Q as class at exponent r; lift to exponent r+v
                    y=x*pow(unit,-1,Q)%Q
                    assert coeff*y%big==x*p**v
                    lifts+=1
            for x in (0,1,q//2,q-1):
                y=pow(k,-E,q)*x%q
                assert a*y%q==x%q
                signs+=1
# Finite analogue of compact extension: subgroup H of C_m x C_n,
# open normal N in kernel of restriction, well-defined HN extension.
ext=local=0
for m,n in product(range(1,9),repeat=2):
    G=list(product(range(m),range(n)))
    add=lambda x,y:((x[0]+y[0])%m,(x[1]+y[1])%n)
    for d in range(1,m+1):
        if m%d:continue
        H=[(i,0) for i in range(0,m,d)]
        N=[(0,j) for j in range(n)]
        for q in (2,3,4,5):
            for t in range(q):
                if t*len(H)%q:continue
                phi={h:(h[0]//d*t)%q for h in H}
                psi={}
                for h,z in product(H,N):
                    x=add(h,z)
                    assert x not in psi or psi[x]==phi[h]
                    psi[x]=phi[h]
                assert all(psi[h]==phi[h] for h in H)
                assert all(psi[add(x,y)]==(psi[x]+psi[y])%q for x,y in product(psi,repeat=2))
                ext+=1
                # local group N meets H trivially, extension kills it
                assert all(psi[z]==0 for z in N)
                local+=1
# Character injection via generator values for finite cyclic products,
# and length = log_l(cardinality) for primary modules.
chars=lengths=0
for p,exps in product((2,3,5),product(range(3),repeat=2)):
    m,n=(p**e for e in exps)
    for nu in range(1,4):
        q=p**nu
        vals=[(a,b) for a,b in product(range(q),repeat=2) if m*a%q==0 and n*b%q==0]
        assert len(vals)==gcd(m,q)*gcd(n,q)
        # distinct generator values determine distinct maps.
        maps={tuple((i*a+j*b)%q for i,j in product(range(m),range(n))) for a,b in vals}
        assert len(maps)==len(vals)
        chars+=len(vals)
    assert m*n==p**sum(exps)
    lengths+=1
print(f"PASS {orders} cyclotomic orders; {lifts} scalar coboundary lifts; {signs} twist-sign identities; {ext} character extensions; {local} local-zero controls; {chars} generator character controls; {lengths} length identities")
