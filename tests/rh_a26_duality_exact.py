"""Finite algebraic controls of the duality bridge; not a Lean replay."""
from itertools import product
from math import gcd

def run():
    counts = dict(cup_sign=0, dual=0, coefficient=0, kernel=0, primitive=0)
    for p, r, d in product((2, 3, 5), range(1, 4), range(1, 9)):
        N = p**r
        for u in range(N):
            if gcd(u, N) != 1 or pow(u, d, N) != 1:
                continue
            geo = [sum(pow(u,j,N) for j in range(i)) % N for i in range(d+1)]
            # Sample all character generators, with bounded Kummer values.
            for k in range(0,N,max(1,N//12)):
                if k*geo[d] % N:
                    continue
                for c in range(N):
                    if d*c % N:
                        continue
                    for g,h in product(range(d), repeat=2):
                        kg,kh,kgh = k*geo[g],k*geo[h],k*geo[(g+h)%d]
                        cg,ch,cgh = c*g,c*h,c*((g+h)%d)
                        db = pow(u,g,N)*kh*ch-kgh*cgh+kg*cg
                        assert (db+kg*ch+cg*pow(u,g,N)*kh)%N == 0
                        counts['cup_sign'] += 1
    for p,r,a in product((2,3,5,7),range(1,5),range(0,5)):
        if a>r: continue
        N, n=p**r,p**a
        duals=[t for t in range(N) if n*t%N==0]
        assert len(duals)==n
        for u in range(1,N,p):
            if gcd(u,N)!=1: continue
            for e in (1,2,3,7):
                v=pow(u,e+1,N)
                for t in duals:
                    twisted=u*pow(v,-1,N)*t%N
                    assert twisted==pow(u,-e,N)*t%N
                    assert (twisted*v-u*t)%N==0
                    counts['dual']+=1
        for t in duals:
            assert (p*t)% (p*N) == p*t
            assert (p*t)*n%(p*N)==0
            counts['coefficient']+=1
    # f: Z/p^a -> Z/p^b, f(x)=q*x.  Exact induced kernel filtration.
    for p,a,b,k in product((2,3,5),range(5),range(5),range(5)):
        n,m=p**a,p**b
        q=p**(max(0,b-a)+k)
        K={x for x in range(n) if q*x%m==0}
        C=m//len({q*x%m for x in range(n)})
        for r in range(1,7):
            nr,mr=gcd(n,p**r),gcd(m,p**r)
            kr=sum(q*x%mr==0 for x in range(nr))
            cr=mr//len({q*x%mr for x in range(nr)})
            assert cr==gcd(C,p**r)
            if r>=b:
                intersection=sum(x%nr==0 for x in K)
                assert kr==len(K)//intersection
            counts['kernel']+=1
    # finite analogue of the locally invariant correction to a primitive
    for p,R,c,r in product((2,3,5),range(1,5),range(5),range(1,5)):
        if not c<=r<=R: continue
        N=p**R
        step=p**(R-r)
        # action by 1+p^c, with c=0 only when this is a unit
        u=(1+p**c)%N
        if gcd(u,N)!=1: continue
        for b in range(0,N,step):
            for inv in range(0,N,p**(R-min(R,c))):
                a=(b+inv)%N
                assert (u-1)*(a-b)%N==0
                assert p**r*a%N==0
                counts['primitive']+=1
    print(counts, 'total', sum(counts.values()))

if __name__=='__main__':
    run()
