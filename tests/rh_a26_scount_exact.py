"""Exact finite controls of SCount mechanisms; not a Lean replay."""
from itertools import product
from math import gcd, prod

def val(n,p):
    assert n>0
    v=0
    while n%p==0:n//=p;v+=1
    return v

def det(M):
    # Fraction-free elimination, exact pivoting.
    M=[row[:] for row in M]; n=len(M); sign=1; old=1
    for k in range(n-1):
        i=next((i for i in range(k,n) if M[i][k]),None)
        if i is None:return 0
        if i!=k:M[k],M[i]=M[i],M[k];sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=M[i][j]*pivot-M[i][k]*M[k][j]
                assert x%old==0
                M[i][j]=x//old
            M[i][k]=0
        old=pivot
    return sign*M[-1][-1]

dc=0
for n,r,a in product(range(1,8),range(1,5),range(2,8)):
    N=n*r
    G=[[int(i//n==j//n and i%n==(j+1)%n) for j in range(N)] for i in range(N)]
    assert abs(det([[G[i][j]-a*(i==j) for j in range(N)] for i in range(N)]))==(a**n-1)**r
    # basis e_i-e_last of augmentation hyperplane
    if N>1:
        H=[[G[i][j]-G[i][-1]-a*(i==j) for j in range(N-1)] for i in range(N-1)]
        assert abs(det(H))*(a-1)==(a**n-1)**r
    else:assert a-1==a**n-1
    dc+=1
lc=0
for p,c,E,depth,r in product((2,3,5,7),range(1,5),range(1,26),range(4),range(1,5)):
    if p==2 and c==1:continue
    a=(1+p**c)**E; n=p**depth; nu=c+depth; v=val(E,p)
    assert val(a-1,p)==c+v
    # exact modular valuation, avoiding huge a**n
    k=nu+v
    assert pow(a,n,p**k)==1%p**k
    assert pow(a,n,p**(k+1))!=1
    eq=r*k-c-v
    assert eq>=0 and r*nu<=eq+c+v
    lc+=1
# Two-coordinate free lattice, g swaps, d=m id. Coker(delta) cyclic
# order a^2-1 via (x,y)->x+a*y. U/deltaY is kernel of m on it.
wc=kc=ic=0
for a,m in product(range(2,13),range(1,25)):
    D=a*a-1
    W=[j for j in range(D) if m*j%D==0]
    C=[(x,y) for x,y in product(range(m),repeat=2) if (y-a*x)%m==0 and (x-a*y)%m==0]
    assert len(W)==len(C)==gcd(m,D)
    wc+=1
    for p in (2,3,5,7,11):
        if (a-1)%p:continue
        seen=set()
        for j in W:
            if p*j%D:continue
            z=(-a*p*j//D,-p*j//D)
            assert (-a*z[0]+z[1],z[0]-a*z[1])==(p*j,0)
            assert all(m*x%p==0 for x in z)
            key=tuple(x%p for x in z)
            assert key not in seen
            seen.add(key);ic+=1
        for nu in range(1,val(D,p)+1):
            q=p**nu; u=D//q
            for b in range(4):
                s=p**b
                images={((s*j)%q,(s*a*j)%q) for j in W}
                K=[j for j in W if s*j%q==0 and s*a*j%q==0]
                assert all(u*s*j%D==0 for j in K)
                assert len(images)*len(K)==len(W)
                assert p**val(len(W),p)<=len(images)*p**((b+val(u,p))*int(len(seen)>1))
                kc+=1
# Finite primary groups: exact kernel count with diagonal multiplication.
pc=0
for p,exps,s in product((2,3,5),product(range(4),repeat=3),range(5)):
    h=sum(e>0 for e in exps)
    size=p**sum(exps); ker=p**sum(min(e,s) for e in exps)
    image=size//ker
    assert ker<=p**(s*h) and size<=image*p**(s*h)
    pc+=1
print(f"PASS {dc} lattice determinants; {lc} valuation/cancellation cases; {wc} exact quotient counts; {ic} SelInv injections; {kc} weighted-norm kernels; {pc} primary kernel counts")
