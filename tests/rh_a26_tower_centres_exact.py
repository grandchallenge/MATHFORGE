"""Exact controls for tower descent's algebraic estimates.
No computation of actual number-field Sha, no original Lean replay.
"""
from itertools import product
from math import prod

def val(n,p):
    if not n:return float('inf')
    n=abs(n);r=0
    while n%p==0:n//=p;r+=1
    return r

def logp(n,p):
    k=0
    while p**(k+1)<=n:k+=1
    return k

def lte():
    count=0
    for p in (2,3,5,7):
        for c in range(2 if p==2 else 1,4):
            for j in range(3):
                for a,b in product(range(10),repeat=2):
                    K=j+c+6;M=p**K;u=1+p**c
                    d=(pow(u,p**j*a,M)-pow(u,p**j*b,M))%M
                    assert min(val(d,p),K)==min(j+c+val(a-b,p),K)
                    count+=1
    # Excluded case at 2: u=3, c=1, v2(u^2-1)=3 not 2.
    assert val(3**2-1,2)==3
    return count

def balls():
    count=0
    for p in (2,3,5):
        for c in (2,3):
            for j in (0,1):
                K=3;P=p**K;M=p**(K+j+c);u=1+p**c
                for z in range(0,M,max(1,M//31)):
                    # Truncated required residue precision for each ball.
                    req=[max(0,min(K,val((pow(u,p**j*e,M)*z-1)%M,p)-j-c)) for e in range(2*P)]
                    s=next(s for s in range(P) if all((s-e)%p**k==0 for e,k in enumerate(req)))
                    assert all(min(val(s-e,p),K)>=k for e,k in enumerate(req))
                    count+=1
    return count

def mul(A,B,M):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%M for j in range(2)) for i in range(2))
I=((1,0),(0,1))
def power(A,n,M):
    B=I
    while n:
        if n%2:B=mul(B,A,M)
        A=mul(A,A,M);n//=2
    return B
def subI(A):return tuple(tuple(A[i][j]-I[i][j] for j in range(2)) for i in range(2))
def coker(A,mods,p):
    # Enumerate images in genuine mixed finite modules.
    im={tuple(sum(A[i][j]*x[j] for j in range(2))%mods[i] for i in range(2)) for x in product(*(range(m) for m in mods))}
    q=prod(mods)//len(im)
    assert q*len(im)==prod(mods)
    return val(q,p)
def growth():
    count=0
    for p in (2,3,5):
        j0=logp(2,p)+3
        for a,b in product((1,2,3),repeat=2):
            mods=(p**a,p**b);M=max(mods)
            for r,s in product((0,1,2),repeat=2):
                # Matrix respects the two different annihilator ideals.
                A=((1+p*r,p**max(a-b,0)),(p**(1+max(b-a,0))*s,1+p*s))
                assert all(A[i][j]*mods[j]%mods[i]==0 for i in range(2) for j in range(2))
                for e in (0,1,2):
                    u=1+p**(2 if p==2 else 1)
                    g=tuple(tuple(pow(u,e,M)*v%M for v in row) for row in A)
                    lens=[]
                    for m in range(j0+3):
                        T=subI(power(g,p**m,M))
                        L=coker(T,mods,p);lens.append(L)
                        det=T[0][0]*T[1][1]-T[0][1]*T[1][0]
                        assert L<=val(det,p)
                        count+=1
                    assert all(L<=lens[j0]+2*max(m-j0,0) for m,L in enumerate(lens))
                    assert all(x<=y for x,y in zip(lens,lens[1:]))
    # Singular lift does not imply the quotient of a torsion module is infinite.
    assert coker(((0,0),(0,0)),(4,8),2)==5
    return count
if __name__=="__main__":
    print(f"PASS {lte()} valuation identities; {balls()} finite ball-intersection controls; {growth()} mixed-module cokernel/determinant comparisons; 2-adic and singular-lift negative controls")
