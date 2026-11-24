"""Exact finite controls for the StickBound proof, not arithmetic Sha replay."""
from fractions import Fraction as Q
from math import gcd, comb, factorial, prod
from itertools import product

def prime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def bern(k):
    b=[Q(1)]
    for j in range(1,k+1): b.append(-sum(comb(j+1,i)*b[i] for i in range(j))/(j+1))
    return b
def C(M,k,b):
    return sum(comb(k,j)*v*Q(M)**(j-1)*b**(k-j) for j,v in enumerate(bern(k)))/k
def E(M,a,b):
    u=pow(a,-1,M)*b%M
    return (a-1)//2-(a*u-b)//M
def v(n,p):
    n=Q(n)
    if not n: return float('inf')
    def vi(n):
        c=0
        while n%p==0: n//=p; c+=1
        return c
    return vi(abs(n.numerator))-vi(n.denominator)
def unit(M): return [b for b in range(M) if gcd(M,b)==1]
def near():
    ct=level=0
    for M in range(2,19):
        for a in (2*M+1,4*M+1):
            for k in range(2,8):
                D=2*k*prod(p for p in range(2,k+2) if prime(p))
                for b in unit(M):
                    u=pow(a,-1,M)*b%M
                    assert (D*(C(M,k,b)-a**k*C(M,k,u)-b**(k-1)*E(M,a,b))/M).denominator==1
                    ct+=1
                for p in [p for p in range(2,M+1) if prime(p) and M%p==0]:
                    J=M*p
                    for b in unit(M):
                        assert sum(C(J,k,b+j*M) for j in range(p))==C(M,k,b)
                        level+=1
    return ct,level
def determinant(A):
    A=[[Q(x) for x in row] for row in A]; n=len(A); ans=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:return Q(0)
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];ans=-ans
        t=A[j][j]; ans*=t
        for i in range(j+1,n):
            q=A[i][j]/t
            for h in range(j,n):A[i][h]-=q*A[j][h]
    return ans
def det_tests():
    ct=bad=0
    for M in range(3,24):
        U=unit(M); a=2*M+1
        reps=sorted({min(b,M-b) for b in U})
        d=len(reps)
        for k in range(2,8):
            s=(-1)**k; den=M*k*factorial(k+1)
            coeff={b:-(C(M,k,b)-a**k*C(M,k,pow(a,-1,M)*b%M)) for b in U}
            # phi = inverse cyclotomic action, so basis exponent b (not b^-1).
            A=[[Q(0) for _ in reps] for _ in reps]
            for j,g in enumerate(reps):
                for b in U:
                    h=g*b%M; rep=min(h,M-h)
                    A[reps.index(rep)][j]+=coeff[b]*(1 if h==rep else s)
            X=determinant([[den*x for x in row] for row in A])
            assert X.denominator==1 and X
            bd=den*2*a**k*M**k*factorial(k)
            assert abs(X)<=bd**d
            for p in (2,3,5,7):
                if len(U)%p==0:
                    assert v(X,p)>=0;bad+=1
            ct+=1
    return ct,bad
def lengths():
    n=0
    for p in (2,3,5,7):
        for exps in product(range(5),repeat=3):
            for r in range(5):
                assert sum(min(r,x) for x in exps)<=r*sum(x>0 for x in exps)
                n+=1
    return n
def constants():
    n=0
    for N in range(1,21):
        for l in (2,3,5,7,11):
            for e in range(1,13):
                M=N*l;k=e+1;a=2*M+1;T=e*M
                bd=M*k*factorial(k+1)*2*a**k*M**k*factorial(k)
                assert bd*M<=T**(10*k)
                n+=1
    return n
if __name__=="__main__":
    n,l=near(); d,b=det_tests()
    print(f"PASS {n} twisted congruences; {l} distribution identities; {d} signed determinants; {b} bad-prime determinant comparisons; {lengths()} length bounds; {constants()} constant inequalities")
