"""Exact controls: source affine conjugation, coset classification, detection recurrence."""
from fractions import Fraction as F
from itertools import product, permutations
from math import prod

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def inv(A):
    n=len(A); B=[list(map(F,row))+e for row,e in zip(A,eye(n))]
    for j in range(n):
        i=next(i for i in range(j,n) if B[i][j])
        B[j],B[i]=B[i],B[j]
        v=B[j][j]; B[j]=[x/v for x in B[j]]
        for i in range(n):
            if i!=j:
                v=B[i][j]; B[i]=[a-v*b for a,b in zip(B[i],B[j])]
    return [row[n:] for row in B]
def trans(n,i,j,a):
    A=eye(n); A[i][j]=F(a);return A
def affine():
    count=excluded=integral=0
    for p,n,b,seed in product((2,3,5,7),(1,2,3),(1,2),range(12)):
        N=n+b;c=eye(N)
        for i in range(N):
            c=mul(c,trans(N,i,(i+1)%N,seed+i+1))
        # invertible permutations diversify first column.
        if seed%2:c[0],c[-1]=c[-1],c[0]
        ci=inv(c);v=[row[0] for row in ci]
        for j in range(n,N):
            if int(v[j])%p==0:excluded+=1;continue
            u=pow(int(v[j])%p,-1,p);t=(1-u*v[j])/p
            y=[F(u,p)*a+(t if i==j else 0) for i,a in enumerate(v)]
            assert y[j]==F(1,p)
            G=eye(N)
            for i in range(N):G[i][j]=y[i]
            q=eye(N);q[0][0]=p
            qc=mul(q,c);gamma=mul(qc,G)
            assert all(x.denominator==1 for row in gamma+inv(gamma) for x in row)
            S=eye(N)
            # use h=I+pE, stabilizes every residue line
            if n>1:S[0][1]=p*(seed+1)
            A=mul(mul(inv(G),S),G)
            expected=[row[:] for row in S]
            for i in range(N):expected[i][j]+=sum(S[i][k]*y[k] for k in range(N))-y[i]
            assert A==expected
            assert all(A[i]==eye(N)[i] for i in range(n,N))
            assert [row[:n] for row in A[:n]]==[row[:n] for row in S[:n]]
            delta=mul(mul(qc,S),inv(qc))
            assert all(x.denominator==1 for row in delta+inv(delta) for x in row)
            assert A==mul(mul(inv(gamma),delta),gamma)
            assert all(x.denominator==1 for row in A+inv(A) for x in row)
            count+=1;integral+=1
    assert count and excluded
    return count,excluded,integral
def lines(p,n):
    return [((0,)*i+(1,)+tail) for i in range(n) for tail in product(range(p),repeat=n-i-1)]
def geometry():
    count=0
    for p,n,b in product((2,3,5),(1,2,3),(1,2)):
        A=lines(p,n);B=lines(p,n+b)
        assert len(B)==(p**(n+b)-1)//(p-1)
        assert {v+(0,)*b for v in A}=={v for v in B if not any(v[n:])}
        assert len(B)>=n+b
        count+=1
    return count
def recurrence():
    accepted=rejected=0
    for a,M,x,y in product((F(1,100),F(1,20),F(1,5),F(1,2)),range(6),range(-5,6),range(-25,26)):
        if abs(y)>M*abs(x) or a*(1+M)>F(1,5):
            rejected+=1;continue
        assert abs((1-a)*x+a*y)>=F(4,5)*abs(x)
        accepted+=1
    # If the small-correction hypothesis is removed, an actual fast-decay example exists.
    assert (1-F(1,2))+F(1,2)*F(1,5)==F(3,5)
    return accepted,rejected
if __name__=="__main__":
    print("PASS affine cases, excluded pivots, integral stabilizers:",affine())
    print("PASS projective coset partitions:",geometry())
    print("PASS recurrence admitted/rejected:",recurrence())
