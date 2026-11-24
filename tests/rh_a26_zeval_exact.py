"""Exact rational checks for RH-A26 zEval; not original Lean replay.

Tests the actual denominator-cleared identity, level change, unit hypothesis
and valuation stability under congruent scalar representatives. These are
finite controls, not an enumeration of Galois lifts.
"""
from fractions import Fraction as Q
from math import comb, gcd, prod, inf

def prime(n):
    return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def bernoulli(k):
    a=[Q(1)]
    for j in range(1,k+1):
        a.append(-sum(comb(j+1,i)*a[i] for i in range(j))/(j+1))
    return a
B=bernoulli(12)
def P(k): return prod(p for p in range(2,k+2) if prime(p))
def D(k): return 2*k*P(k)
def C(F,k,u):
    return sum(comb(k,j)*B[j]*Q(F)**(j-1)*u**(k-j) for j in range(k+1))/k
def th(F,b,u): return (b*(u%F))//F-(b*((-u)%F))//F
def units(F): return [t for t in range(1,F+1) if gcd(t,F)==1]
def v(x,p):
    x=Q(x)
    if not x: return inf
    def vi(n):
        n=abs(n); i=0
        while n%p==0: n//=p; i+=1
        return i
    return vi(x.numerator)-vi(x.denominator)
def chi1(a): return 1
def chi4(a): return 0 if not a%2 else (1 if a%4==1 else -1)
def chi5(a): return 0 if a%5==0 else (1 if a%5 in (1,4) else -1)
def chi8(a): return 0 if not a%2 else (1 if a%8 in (1,7) else -1)
def chi12(a): return 0 if gcd(a,12)!=1 else (1 if a%12 in (1,11) else -1)
def gen(F,k,chi): return k*sum(C(F,k,u)*chi(u) for u in units(F))
def test_pointwise():
    count=0; denominator_needed=0
    for F in range(2,25):
        U=units(F)
        for k in range(2,11):
            R={u:C(F,k,u) for u in U}
            for b in U:
                for u in U:
                    E=b**(k-1)*th(F,b,u)*u**(k-1)+2*R[b*u%F]-2*b**k*R[u]
                    assert (D(k)*E/F).denominator==1
                    count+=1
                    if (E/F).denominator!=1: denominator_needed+=1
    assert denominator_needed
    return count,denominator_needed
def test_valuation():
    level=weighted=stable=divisibility=positive=exceptional=0
    for f,chi in [(1,chi1),(4,chi4),(5,chi5),(8,chi8),(12,chi12)]:
        for k in range(2,9):
            if chi(-1)!=(-1)**k: continue
            T=gen(f,k,chi)/k
            assert T
            a=f*P(k)*k*T
            assert a.denominator==1
            for l in (3,5,7):
                N0=f//l**v(f,l)
                for m in range(max(1,v(f,l)),4):
                    F=N0*l**m; M=l**m
                    U=units(F)
                    TF=gen(F,k,chi)/k
                    assert TF==T*(1-chi(l)*l**(k-1))
                    assert v(TF,l)==v(T,l)
                    level+=1
                    b=next((b for b in U if (chi(b)*b**k-1)%l),None)
                    if b is None:
                        exceptional+=1; continue
                    S=sum(th(F,b,u)*u**(k-1)*chi(u) for u in U)
                    V=b**(k-1)*chi(b); W=chi(b)*b**k-1
                    err=D(k)*(V*S-2*W*TF)
                    assert v(err,l)>=m
                    assert (err/F).denominator==1
                    weighted+=1
                    if m<=v(D(k),l)+v(T,l): continue
                    assert v(S,l)==v(T,l)
                    # Replace cyclotomic residues by congruent integers, with
                    # three deterministic choices of lift errors. Exact Galois
                    # lift congruence follows from the proof, not this test.
                    for j in (-1,0,2):
                        z=sum(th(F,b,u)*(u+M*j*(u%3+1))**(k-1)*chi(u) for u in U)
                        assert (z-S)%M==0
                        assert v(z,l)==v(T,l)
                        assert v(a,l)-v(z,l)==v(f*P(k)*k,l)
                        stable+=1
                        if v(z,l)>0: positive+=1
                        for s in range(m+1):
                            if m>s+v(D(k),l)+v(T,l):
                                assert v(l**s*z,l)<m
                                assert v(z,l)<=v(a,l)
                                divisibility+=1
    # Target positive valuation: primitive conductor 8, k=4, l=11.
    # D is an 11-adic unit; m=2 supports a0=1, m=3 supports a0=11.
    f,k,l,chi=8,4,11,chi8
    T=gen(f,k,chi)/k
    assert T==-11 and v(D(k),l)==0
    a=f*P(k)*k*T
    for m in (2,3):
        F=f*l**m; M=l**m; U=units(F)
        TF=gen(F,k,chi)/k
        assert TF==T*(1-chi(l)*l**(k-1))
        assert v(TF,l)==1
        level+=1
        b=next(b for b in U if (chi(b)*b**k-1)%l)
        S=sum(th(F,b,u)*u**(k-1)*chi(u) for u in U)
        err=D(k)*(b**(k-1)*chi(b)*S-2*(chi(b)*b**k-1)*TF)
        assert (err/F).denominator==1 and v(err,l)>=m
        weighted+=1
        for j in (-1,0,2):
            z=sum(th(F,b,u)*(u+M*j*(u%3+1))**(k-1)*chi(u) for u in U)
            assert (z-S)%M==0 and v(z,l)==1
            assert v(a,l)-v(z,l)==v(f*P(k)*k,l)
            stable+=1; positive+=1
            for s in range(m-1):
                assert v(l**s*z,l)<m and v(z,l)<=v(a,l)
                divisibility+=1
    assert exceptional and positive and stable and divisibility
    return level,weighted,stable,divisibility,positive,exceptional
def controls():
    for m in range(1,5):
        F=5*3**m
        assert gen(F,2,chi5)==Q(16,5)
        assert sum(th(F,2,u)*u*chi5(u) for u in units(F))==8
    assert gen(5,2,chi5)==Q(4,5)
    assert gen(1,2,chi1)/2==Q(1,12)
    assert v(Q(1,12),3)==-1
    assert all((b*b-1)%3==0 for b in units(9))
    assert v(sum(th(9,2,u)*u for u in units(9)),3)==0
if __name__=="__main__":
    n,d=test_pointwise()
    l,w,s,a,p,e=test_valuation()
    controls()
    print(f"PASS {n} pointwise identities ({d} need denominator); {l} level identities; {w} weighted congruences; {s} stable representative valuations ({p} positive); {a} divisibility comparisons; {e} excluded cases; exact negative control")
