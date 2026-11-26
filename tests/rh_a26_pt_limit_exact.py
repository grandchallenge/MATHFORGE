"""Exact finite controls for the limiting PT length proof.
Finite module identities, not Galois cohomology or original Lean replay.
"""
from itertools import product
from math import prod

def val(n,p):
    assert n>0
    v=0
    while n%p==0:n//=p;v+=1
    assert n==1
    return v

def finite_kernel(p,a,b,t):
    # X=Z/p^a, P=Z/p^b, f multiplication by p^t
    A=p**a;B=p**b
    assert p**t*A%B==0
    K={x for x in range(A) if p**t*x%B==0}
    I={p**t*x%B for x in range(A)}
    count=stable=bad=0
    for r in range(1,7):
        QX=p**min(a,r);QP=p**min(b,r)
        kr={x for x in range(QX) if p**t*x%QP==0}
        redK={x%QX for x in K}
        Ir={p**r*x%B for x in I}
        pP={p**r*x%B for x in range(B)}
        assert (redK==kr)==(I & pP==Ir)
        assert QP//len({p**t*x%QP for x in range(QX)})==p**min(r,val(B//len(I),p))
        if r>=b:
            assert redK==kr;stable+=1
        if redK!=kr:bad+=1
        count+=1
    return count,stable,bad

def module_controls():
    n=s=b=0
    for p in (2,3,5):
        for a,d in product(range(1,5),repeat=2):
            for t in range(max(0,d-a),d+1):
                x,y,z=finite_kernel(p,a,d,t);n+=x;s+=y;b+=z
    assert b>0
    # free lattice f=p: integral kernel zero, mod p^r kernel p elements.
    for p,r in product((2,3,5,7),range(1,6)):
        assert sum(p*x%p**r==0 for x in range(p**r))==p
    return n,s,b

def coefficient_controls():
    count=0
    for p in (2,3,5):
        for r in range(1,4):
            for s in range(r,5):
                A=p**r;B=p**s
                for u in (1,1+p,1+p**2):
                    for e in (-2,-1,0,1,2):
                        t=pow(u,e+1,B);dual=u*pow(t,-1,B)%B
                        assert dual==pow(u,-e,B)
                        for a in range(A):
                            assert (dual*(p**(s-r)*a))%B==p**(s-r)*(pow(u,-e,A)*a%A)
                            count+=1
    return count

def cokernel_controls():
    count=0
    for p,rank,a,b in product((2,3,5),range(3),range(4),range(4)):
        sizes=[rank*r+min(r,a)+min(r,b) for r in range(1,9)]
        assert (sizes==list(range(1,9)))==(rank==1 and a==b==0)
        count+=1
    return count

if __name__=="__main__":
    n,s,b=module_controls()
    print(f"PASS {n} finite kernel/cokernel comparisons; {s} stabilized cases; {b} spurious-kernel negative cases; {coefficient_controls()} twist/inclusion checks; {cokernel_controls()} zero-twist cardinal growth comparisons")
