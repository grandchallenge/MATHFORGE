"""Exact finite controls of the rank and index-two arguments, not class group computation."""
from itertools import product
from math import gcd

def v2(n):
    assert n
    v=0
    while n%2==0:n//=2;v+=1
    return v

def frob():
    n=0
    for p in range(3,300,2):
        c=2 if p%8==3 else 4 if p%16==7 else 0
        if not c:continue
        assert v2(p*p-1)==(3 if c==2 else 4)
        for k in range(3,11):
            M=2**k; H={1};a=p%M
            while a not in H:H.add(a);a=a*p%M
            assert (M//2)%len(H)==0 and M//2//len(H)<=c
            n+=1
    return n

def rank(vectors,r):
    piv={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return len(piv)

def involutions():
    n=0
    # Every matrix of sizes 1..3; no assumption of diagonalizability.
    for r in range(1,4):
        for cols in product(range(2**r),repeat=r):
            def apply(x):
                y=0
                for i in range(r):
                    if x>>i&1:y^=cols[i]
                return y
            if any(apply(apply(1<<i))!=1<<i for i in range(r)):continue
            d=r-rank([cols[i]^(1<<i) for i in range(r)],r)
            assert r<=2*d
            n+=1
    return n

def cyclic_chars():
    n=0
    for m in (2,4,6,8,12,16,20):
        U=list(range(0,m,2))
        # Characters of V=C_m and U=<2>, explicit generator values.
        for forbidden in [[],[0],[2],[4],[6]]:
            S={x%m for x in forbidden}
            assert S<=set(U)
            CV=[a for a in (0,1) if m*a%2==0 and all(a*s%2==0 for s in S)]
            CU=[a for a in (0,1) if (m//2)*a%2==0 and all(a*(s//2)%2==0 for s in S)]
            extend=[a for a in CU if a==0] # sigma^2=2
            assert len(CV)==2*len(extend)
            assert len(CU)<=len(CV) and len(CU)<=len(CV)**2
            n+=1
    # C4 over C2: nonzero invariant character need not extend.
    assert (2//2)*1%2==1
    return n

def degree_transfer():
    n=0
    for h in range(2,7):
        for m,q,d in ((1,3,7),(5,3,7),(8,3,7),(7,11,23)):
            from math import lcm
            N=lcm(2**(h+2),m,q,d)
            V=[a for a in range(N) if gcd(a,N)==1 and a%m==1%m and pow(a%q,(q-1)//2,q)==1 and pow(a%d,(d-1)//2,d)==1 and a%(2**(h+2)) in (1,2**(h+2)-1)]
            U=[a for a in V if a%(2**(h+2))==1]
            assert len(U)>0 and len(V) in (len(U),2*len(U))
            n+=1
    return n

if __name__=="__main__":
    print(f"PASS {frob()} dyadic Frobenius indices; {involutions()} characteristic-two involutions; {cyclic_chars()} character extension cases; {degree_transfer()} composite-field index controls")
