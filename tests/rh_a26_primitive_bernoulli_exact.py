"""Exact rational regression for RH-A26 primitive Bernoulli denominator transport.
Not a verification of Rec, the Sha bound, or the original Lean kernel.
"""
from fractions import Fraction as Q
from math import comb, gcd, prod

def prime(n):
    return n >= 2 and all(n % p for p in range(2, int(n**0.5)+1))

def bernoulli(k):
    b=[Q(1)]
    for j in range(1,k+1):
        b.append(-sum(comb(j+1,i)*b[i] for i in range(j))/ (j+1))
    return b

B=bernoulli(16)
def P(k): return prod(p for p in range(2,k+2) if prime(p))
def coeff(n,k,a):
    return Q(n)**(k-1)*sum(comb(k,j)*B[j]*Q(a,n)**(k-j) for j in range(k+1))
def gen(n,k,chi): return sum(chi(a)*coeff(n,k,a) for a in range(1,n+1))
def chi4(a): return (1 if a%4==1 else -1) if a%2 else 0
def chi5(a): return 0 if a%5==0 else (1 if a%5 in (1,4) else -1)
def chi8(a): return 0 if a%2==0 else (1 if a%8 in (1,7) else -1)
def chi12(a): return 0 if gcd(a,12)!=1 else (1 if a%12 in (1,11) else -1)
def val(n,p):
    assert n and p>1
    n=abs(n); r=0
    while n%p==0: n//=p; r+=1
    return r

def main():
    nc=nl=nv=0
    for n in range(1,25):
        for k in range(17):
            for a in range(1,n+1):
                c=n*P(k)*coeff(n,k,a)
                assert c.denominator==1
                nc+=1
    for f,chi in [(4,chi4),(5,chi5),(8,chi8),(12,chi12)]:
        for k in range(1,9):
            v=gen(f,k,chi)
            af=f*P(k)*v
            for t in range(1,7):
                an=f*t*P(k)*v
                assert af.denominator==an.denominator==1
                assert an==t*af
                nl+=1
                if af:
                    for p in (2,3,5,7,11,13):
                        assert val(an.numerator,p)==val(af.numerator,p)+val(t,p)
                        nv+=1
    assert gen(5,2,chi5)==Q(4,5)
    assert gen(10,2,lambda a: chi5(a) if gcd(a,10)==1 else 0)==Q(12,5)
    assert 5*P(2)*gen(5,2,chi5)==24
    assert 10*P(2)*gen(5,2,chi5)==48
    assert nc==5100 and nl==192
    print(f"PASS {nc} coefficient checks; {nl} conductor cases; {nv} nonzero valuation checks; imprimitive negative control")
if __name__=="__main__": main()
