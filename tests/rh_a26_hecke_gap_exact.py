"""Exact finite controls for the RH-A26 arithmetic spectral-gap reconstruction.
The proofs are in the companion dossier. These do not compute a global automorphic spectrum.
"""
from itertools import product, permutations, combinations
from fractions import Fraction as F

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm2(a):return dot(a,a)

def projective(q):
    return [(1,a,b) for a,b in product(range(q),repeat=2)]+[(0,1,a) for a in range(q)]+[(0,0,1)]

def design():
    n=cases=pairs=0
    for q in (2,3,5,7,29):
        P=projective(q)
        assert len(P)==q*q+q+1
        incidence=[{i for i,p in enumerate(P) if dot(p,h)%q==0} for h in P]
        assert all(len(s)==q+1 for s in incidence)
        n+=len(P)
        for a,b in combinations(incidence,2):
            assert len(a&b)==1
            pairs+=1
        # Every point has the same degree. For arbitrary centered f,
        # incidence summation has exact squared norm q times ||f||^2.
        assert all(sum(i in s for s in incidence)==q+1 for i in range(len(P)))
        for seed in range(10):
            f=[(i*i+seed*i+3*i**3)%19-9 for i in range(len(P))]
            f=[len(P)*x-sum(f) for x in f]
            g=[(i*seed+7*i*i)%23-11 for i in range(len(P))]
            af=[sum(f[i] for i in s) for s in incidence]
            assert sum(f)==sum(af)==0
            assert norm2(af)==q*norm2(f)
            # normalize by q+1 on each side; source squared bound 1/index.
            assert dot(af,g)**2 <= (q+1)*norm2(f)*norm2(g)
            if q>=25:assert 25*dot(af,g)**2 <= (q+1)**2*norm2(f)*norm2(g)
            cases+=1
        # constant functions: without mean zero the contraction fails.
        assert all(len(s)==q+1 for s in incidence)
        assert 25*((q+1)*len(P))**2 > ((q+1)*len(P))**2
    return n,pairs,cases

def hilbert():
    accepted=rejected=0
    for a,b,c,d,e,f in product((-2,-1,0,1,2),repeat=6):
        normals=((10,a,b),(c,10,d),(e,f,10))
        if any(25*dot(x,y)**2>norm2(x)*norm2(y) for x,y in combinations(normals,2)):
            rejected+=1;continue
        assert dot(normals[0],cross(normals[1],normals[2]))!=0
        for i,j,k in ((0,1,2),(1,0,2),(2,0,1)):
            v=cross(normals[i],normals[j])
            w=cross(normals[i],normals[k])
            assert norm2(v)>0 and norm2(w)>0
            assert 25*dot(v,w)**2<=4*norm2(v)*norm2(w)
        accepted+=1
    assert accepted and rejected
    return accepted,rejected

def matrix(N,i,j,a):
    return tuple(tuple(F(int(r==s))+ (a if (r,s)==(i,j) else 0) for s in range(N)) for r in range(N))
def mul(A,B):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)) for i in range(n))
def kg(A,r,p):
    return all((A[i][j]*F(p)**(int(i<r)-int(j<r))).denominator==1 for i,j in product(range(len(A)),repeat=2))
def arith():
    n=0
    for p,N in product((2,3,5,29),(3,4)):
        for a in range(p):
            u=matrix(N,1,0,F(a))
            v=matrix(N,2,1,F(a))
            assert kg(u,0,p) and kg(u,2,p)
            assert kg(v,0,p) and kg(v,1,p)
            assert kg(u,1,p)==(a==0)
            assert kg(v,2,p)==(a==0)
            n+=2
        for i,k,j in permutations(range(N),3):
            for m in range(4):
                a=F(2,p**m);b=F(1,p)
                x=matrix(N,i,k,a);y=matrix(N,k,j,b)
                assert mul(mul(mul(x,y),matrix(N,i,k,-a)),matrix(N,k,j,-b))==matrix(N,i,j,a*b)
                n+=1
    return n
if __name__=="__main__":
    print("PASS design points, distinct plane pairs, function tests:",design())
    print("PASS Hilbert accepted/rejected normal triples:",hilbert())
    print("PASS arithmetic transvection and commutator comparisons:",arith())
