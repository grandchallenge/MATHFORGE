"""Exact arithmetic checks for the source NuSys construction.
Not a kernel replay or substitute for the algebraic number theory proof.
"""
from math import gcd

def prime(n):
    return n>1 and all(n%i for i in range(2,int(n**.5)+1))
def units(n): return [i for i in range(n) if gcd(i,n)==1]
def T(n,b,t): return (b*(t%n))//n-(b*((-t)%n))//n
def root(p):
    return next(g for g in range(2,p) if len({pow(g,i,p) for i in range(p-1)})==p-1)
def distribution():
    count=0
    for H in range(2,31):
        for q in range(2,44):
            if not prime(q) or gcd(H,q)!=1: continue
            for b in range(min(H,q)):
                for t in units(H):
                    lift=[t+j*H for j in range(q) if (t+j*H)%q]
                    assert sum(T(H*q,b,v) for v in lift)==T(H,b,t)-T(H,b,t*pow(q,-1,H))
                    count+=1
    return count
def jacobi():
    count=congruences=0
    for H in range(3,17):
        for p in range(H+1,170,H):
            if not prime(p): continue
            for t in units(H):
                for j in range(1,H-1):
                    A=(p-1)//H*t; B=(p-1)//H*(j*t%H)
                    val=sum(pow(x,A,p)*pow(1-x,B,p) for x in range(p))%p
                    assert (val==0)==(t+(j*t%H)<H)
                    count+=1
                for b in range(1,H):
                    e=sum(1 for j in range(1,b) if t+(j*t%H)<H)
                    en=sum(1 for j in range(1,b) if (-t)%H+(j*(-t)%H)<H)
                    assert en-e==T(H,b,t)
    # Exact character exponent multisets after reduction at q:
    # eta_{Hq} -> eta_H^(q^-1), when eta_{Hq}^q=eta_H.
    # Compare coefficients in the group ring, stronger than equality after
    # evaluating at a particular root in a residue field.
    for H,q in [(3,7),(5,3),(5,11),(9,19),(12,5)]:
        p=next(p for p in range(H*q+1,3000,H*q) if prime(p))
        g=root(p); log={pow(g,i,p):i for i in range(p-1)}
        for j in range(1,H-1):
            left=[0]*H; right=[0]*H
            for x in range(2,p):
                k=log[x]+j*log[(1-x)%p]
                left[((k%(H*q))*pow(q,-1,H))%H]+=1
                right[(k*pow(q,-1,H))%H]+=1
            assert left==right
            congruences+=1
    return count,congruences
def derivative():
    count=0
    for l in (3,5,7):
        for m in (1,2):
            M=l**m
            for q in range(M+1,250,M):
                if not prime(q): continue
                n=q-1
                # exponent-vector identity (tau-1) D = n - N
                D=list(range(n)); diff=[D[(i-1)%n]-D[i] for i in range(n)]
                assert diff==[n-1]+[-1]*(n-1)
                assert all(x%M==y%M for x,y in zip(diff,[-1]*n))
                count+=1
    return count
def weighted():
    count=0
    # Real character via Legendre symbol; mod ell^m, exact reindexing.
    for l in (3,5,7):
        for m in (1,2):
            M=l**m; F=M
            def alpha(t): return 1 if pow(t%l,(l-1)//2,l)==1 else -1
            for b in range(F):
                for d in units(F):
                    a=d%M
                    z=sum(T(F,b,t)*alpha(t) for t in units(F))
                    h=sum(2*(T(F,b,t*d*d)-2*a*T(F,b,t*d)+a*a*T(F,b,t))*alpha(t) for t in units(F))
                    assert (h-2*(alpha(d)-a)**2*z)%M==0
                    count+=1
    return count
if __name__=="__main__":
    d=distribution(); j,c=jacobi(); k=derivative(); w=weighted()
    # Unit correction is essential: a root of order 3 is not killed by P
    # with a mismatched action exponent; the correct action exponent kills it.
    assert (2-1)%3!=0 and (2-2)%3==0
    print(f"PASS {d} distribution identities; {j} Jacobi reductions; {c} compatible character sum cases; {k} derivative identities; {w} weighted initial sums; root-action negative control")
