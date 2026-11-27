"""Exact finite controls for the SMom source mechanisms.
Log coordinates use rational values; exponential packing counts are tested
with base 2 rather than numerical exp. No number-field or Haar proof by test.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, prod

def gaps():
    count=0
    for N in range(2,7):
        n=N-1
        for d in product(range(-2,4),repeat=n):
            raw=[0]
            for t in d:raw.append(raw[-1]-t)
            mean=F(sum(raw),N);s=[t-mean for t in raw]
            W=sum(abs(t) for t in d);Phi=sum(s[i]-s[j] for i in range(N) for j in range(i+1,N))
            assert Phi==sum((i+1)*(n-i)*d[i] for i in range(n))
            T=2;delta=s[0]-s[-1]
            assert W<=delta+2*n*T and Phi>=n*delta-n**3*T
            for B in (-2,0,2*n-1,F(4*n-1,2)):
                Bp=max(B,0);eps=F(2*n-Bp,N)
                C=2*n*Bp*T+2*n**3*T+(2*n-Bp)*2*n*T
                assert eps>0 and B*W-2*Phi<=C-eps*sum(map(abs,s))
                count+=1
    return count

def packing():
    count=0
    for N in range(2,6):
        for s in product(range(-2,3),repeat=N):
            if sum(s)!=0:continue
            factors=[F(2)**(s[i]-s[j]) for i in range(N) for j in range(i+1,N)]
            cards=[ceil(x)**2 for x in factors]
            assert prod(cards)>=prod(x*x for x in factors)
            for x in factors:
                m=ceil(x)-1
                assert 0<=m<x and 2*m*m<=4*x*x
            count+=1
    return count

def normalization():
    # logarithmic model of determinant normalization: exact sums.
    count=0
    for N in range(2,5):
        for l in product((-1,0,1),repeat=2*N):
            b=[l[:N],l[N:]]
            r=list(range(N))
            a=[-F(sum(bw)+sum(r),N) for bw in b]
            s=[r[i]+sum(a[w]+b[w][i] for w in range(2))/2 for i in range(N)]
            assert sum(s)==0 and abs(a[0]-a[1])<=2
            for i in range(N):
                v=[a[w]+b[w][i]+r[i]-s[i] for w in range(2)]
                assert sum(v)==0 and all(-4<=x<=4 for x in v)
                assert all(a[w]+r[i]-s[i]<=3 for w in range(2))
            assert all(s[i+1]-s[i]<=5 for i in range(N-1))
            count+=1
    return count

def height():
    # rational triangular matrices and denominator-cleared coordinates.
    count=0
    for a,b,t in product((F(1,2),F(1),F(2)),(-2,0,2),(F(1,2),F(1),F(2))):
        p=((a,F(b)),(F(0),1/a));pi=((1/a,-F(b)),(F(0),a))
        for u,v in product(range(-3,4),repeat=2):
            if u==v==0:continue
            primal=(pi[0][0]*u+pi[0][1]*v,pi[1][1]*v)
            dual=(a*u,F(b)*u+v/a)
            k=1 if v else 0;j=0 if u else 1
            assert primal[k]==(u,v)[k]/p[k][k]
            assert dual[j]==p[j][j]*(u,v)[j]
            L=primal[0]/t;R=primal[1]*t
            Ld=dual[0]*t;Rd=dual[1]/t
            M=max(a,1/a,abs(b),1)
            assert L*L+R*R>=1/(M*M*max(t,1/t)**2)
            assert Ld*Ld+Rd*Rd>=min(t,1/t)**2/(M*M)
            count+=1
    return count

def threshold():
    count=0
    for N in range(2,15):
        for A in range(N-1):
            assert 2*A<2*(N-1)
            # Endpoint ray: all gap concentrated at first cut.
            for u in range(1,9):
                s=[F((N-1)*u,N)]+[F(-u,N)]*(N-1)
                W=sum(abs(s[i]-s[i+1]) for i in range(N-1))
                Phi=sum(s[i]-s[j] for i in range(N) for j in range(i+1,N))
                assert W==u and Phi==(N-1)*u
                assert 2*A*W-2*Phi<0
                assert 2*(N-1)*W-2*Phi==0 # no strict margin at equality
                count+=1
    return count

if __name__=="__main__":
    for name,f in (("cone and root-weight comparisons",gaps),("Gaussian entry counts",packing),("determinant log normalization",normalization),("primal/dual triangular coordinate",height),("strict threshold and endpoint",threshold)):
        print("PASS",name,f())
