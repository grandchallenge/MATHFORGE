"""Exact finite controls for height and source partition arithmetic.
Rational test metrics on Z[i]^2. Cutoff controls use only source plateau
constraints, not numerical evaluation of its smoothTransition.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt

def tr(A):return tuple(zip(*A))
def mm(A,B):return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in zip(*B)) for row in A)
def inv(A):
    (a,b),(c,d)=A;t=a*d-b*c
    return ((d/t,-b/t),(-c/t,a/t))
def Q(A,v):return sum(v[i]*A[i][j]*v[j] for i,j in product(range(2),repeat=2))
def dist(A):return (1+sum(abs(A[i][j]-int(i==j)) for i,j in product(range(2),repeat=2)))**2
def shortest(A):
    # det/trace <= smallest eigenvalue for positive symmetric 2x2.
    (a,b),(c,d)=A
    lower=(a*d-b*c)/(a+d)
    assert lower>0
    B=min(a,d)
    n=isqrt(int(B/lower))+1
    return min(Q(A,v) for v in product(range(-n,n+1),repeat=2) if any(v))
def height(x):
    a=inv(x)
    return 1/(shortest(mm(tr(a),a))*shortest(mm(x,tr(x))))
def heights():
    n=0
    for a,b,c in product((F(1,2),F(1),F(2)),(-1,0,1),(F(1,2),F(1),F(2))):
        x=((a,F(b)),(F(0),c));h=height(x)
        for k in (-2,-1,0,1,2):
            g=((F(1),F(k)),(F(0),F(1)))
            assert height(mm(g,x))==h
            for r in (F(1,2),F(2)):
                y=((r,F(k)),(F(0),1/r))
                assert height(mm(x,y))<=dist(y)*dist(tr(inv(y)))*h
                assert height(tuple(tuple(r*z for z in row) for row in x))==h
                n+=1
    return n
def scale():
    n=0
    for m in range(-8,9):
        a=F(4)**m
        for i,j in product(range(16,64),range(17)):
            l=a*i/16
            assert a<=l<4*a
            X=F(j,16);v=a*X+4*a*(1-X)
            assert l/4<=v<=4*l
            n+=1
    return n
def relative():
    n=0
    for delta in (F(0),F(1,16),F(1,8),F(1,4)):
        for i,j in product(range(9),repeat=2):
            a=1-delta+2*delta*F(i,8)
            b=1-delta+2*delta*F(j,8)
            assert abs(1/a-1)<=2*delta
            assert abs(a/b-1)<=3*delta
            n+=1
    return n
def primal():
    # The translate v+u lands in the plateau, pairing difference is Q(u).
    n=0
    for a,b in product((F(1,4),F(1),F(4)),repeat=2):
        H=((a,F(0)),(F(0),b))
        for u in product(range(-2,3),repeat=2):
            if not any(u):continue
            A=Q(H,u);s=F(1)
            while s<4*A:s*=4
            while s>=16*A:s/=4
            assert 4*A<=s<=16*A
            B=isqrt(int(s/(4*min(a,b))))+1
            S=[v for v in product(range(-B,B+1),repeat=2) if Q(H,v)<=s/4]
            for v in S:
                w=tuple(v[i]+u[i] for i in range(2))
                assert Q(H,w)<=s
                P=sum(u[i]*H[i][i]*v[i] for i in range(2))
                P1=sum(u[i]*H[i][i]*w[i] for i in range(2))
                assert P1-P==A and P*P+P1*P1>=A*A/2
                n+=1
    return n
def dual():
    n=0
    for s,m,A in product((F(1,4),F(1),F(4)),repeat=3):
        if 4*s*m<1:continue
        Q0=s*m/(4*A);X=A*s/m
        assert s*s==4*Q0*X
        assert Q0>=1/(16*A)
        n+=1
    return n
if __name__=="__main__":
    for name,f in (("height invariance/distortion",heights),("scale interpolation",scale),("relative normalization",relative),("primal pairing",primal),("dual bound",dual)):
        print("PASS",name,f())
