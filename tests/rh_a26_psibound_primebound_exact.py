"""Exact finite controls for RH-A26 PsiBound -> PrimeBound.
Not a computation of arithmetic Sha or an original Lean replay.
"""
from fractions import Fraction as Q
from math import gcd, lcm, prod, comb, factorial

def prime(n): return n>1 and all(n%d for d in range(2,int(n**0.5)+1))
def v(n,p):
    assert n
    n=abs(n); k=0
    while n%p==0: n//=p; k+=1
    return k

def cyclic_projectors():
    checks=signs=0
    for p in (3,5,7,13,17,19,31):
        for a in (1,2):
            M=p**a
            for d in range(2,min(16,p)):
                if d%2 or (p-1)%d: continue
                w=next(x for x in range(1,M) if pow(x,d,M)==1 and all(pow(x,d//q,M)!=1 for q in range(2,d+1) if prime(q) and d%q==0))
                E=[[pow(d,-1,M)*pow(w,(-j*h)%d,M)%M for h in range(d)] for j in range(d)]
                def conv(x,y):
                    return [sum(x[i]*y[(h-i)%d] for i in range(d))%M for h in range(d)]
                assert [sum(e[h] for e in E)%M for h in range(d)]==[1]+[0]*(d-1)
                for j,x in enumerate(E):
                    for k,y in enumerate(E):
                        assert conv(x,y)==(x if j==k else [0]*d)
                        checks+=1
                for s in (1,-1):
                    chosen=[j for j in range(d) if pow(w,j*(d//2),M)==s%M]
                    assert len(chosen)==d//2
                    expected=[0]*d
                    expected[0]=pow(2,-1,M)
                    expected[d//2]=s*pow(2,-1,M)%M
                    assert [sum(E[j][h] for j in chosen)%M for h in range(d)]==expected
                    signs+=1
    # modular failure: C3 regular representation over F3, only one
    # character and its eigenspace dimension 1, not the full dimension 3.
    assert len([x for x in range(1,3) if pow(x,3,3)==1])==1
    assert gcd(3,3)!=1
    return checks,signs

def B(k):
    b=[Q(1)]
    for j in range(1,k+1):
        b.append(-sum(comb(j+1,i)*b[i] for i in range(j))/(j+1))
    return b
def coeff(f,k,a):
    return Q(f)**(k-1)*sum(comb(k,j)*b*Q(a,f)**(k-j) for j,b in enumerate(B(k)))
def mul(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scaled_char(f,k,N,j):
    # f=5, generator 2, characters j=1,2,3, or trivial primitive f=1.
    if j==0:
        raw=(coeff(1,k,1),Q(0))
    else:
        roots=[(1,0),(0,1),(-1,0),(0,-1)]
        raw=[Q(0),Q(0)]
        for i in range(4):
            t=pow(2,i,5); r=roots[(i*j)%4]; c=coeff(f,k,t)
            for h in range(2): raw[h]+=r[h]*c
    den=N*prod(p for p in range(2,k+2) if prime(p))
    result=tuple(den*x for x in raw)
    assert all(x.denominator==1 for x in result)
    return tuple(int(x) for x in result)

def budget():
    products=valuations=0
    for N in (5,10,15,20):
        for k in range(2,11):
            chars=[j for j in range(4) if j%2==k%2]
            A=[scaled_char(1 if j==0 else 5,k,N,j) for j in chars]
            if (N,k)==(5,3): assert A==[(72,36),(72,-36)]
            M=mul(*A)
            assert M[1]==0 and M[0]!=0
            if (N,k)==(5,3): assert M[0]==6480
            bound=16*N**(k+1)*factorial(k)
            assert all(x*x+y*y<=bound*bound for x,y in A)
            assert abs(M[0])<=bound**2
            products+=1
            # Check all prime factors in a finite set, and exact local norm
            # additivity for split Gaussian roots modulo a sufficiently
            # high prime power. Hensel lifting computes the actual roots.
            for p in (5,13,17,29,41):
                L=v(M[0],p)+1
                mod=p**L
                root=next(x for x in range(p) if (x*x+1)%p==0)
                base=p
                for _ in range(1,L):
                    root=next(root+t*base for t in range(p) if ((root+t*base)**2+1)%(base*p)==0)
                    base*=p
                assert (root*root+1)%mod==0
                for i in (root,-root):
                    vals=[(x+y*i)%mod for x,y in A]
                    assert all(vals)
                    assert sum(v(t,p) for t in vals)==v(M[0],p)
                    valuations+=1
    return products,valuations

if __name__=="__main__":
    c,s=cyclic_projectors(); b,vv=budget()
    print(f"PASS {c} Fourier projector products; {s} sign decompositions; {b} parity-selected integer products; {vv} split-prime valuation sums; modular negative control")
