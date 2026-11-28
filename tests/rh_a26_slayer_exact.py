"""Exact finite controls of SLayer, not original formal replay."""
from itertools import product
from math import gcd

def ceil_power(p,x):
    d=1;m=0
    while d<x:d*=p;m+=1
    return d,m

layers=0
for p,c,E,k in product((2,3,5,7,11,13),range(1,5),range(1,65),range(1,9)):
    if p==2 and c<2:continue
    n=p**(c-1)*(p-1)*k
    d,m=ceil_power(p,4*E+4)
    w=p**(c+m); n1=d*n
    assert 4*E+4<=d<p*(4*E+4)
    assert p<=n+1 and d<=(n+1)*(4*E+4)
    assert w>2*E+1 and n1//2>2*E+1 and n1%2==0
    assert w<=2*n1
    assert pow(1+p**c,d,w)==1
    assert pow(1+p**c,d//p,w)!=1
    layers+=1

# Finite endomorphism models: range inclusion and kernel length.
matrices=0
for q,d in product((2,3,4,5,8,9),(1,2,3,4,5,8,9)):
    # Sample all 2x2 matrices for small rings; subset for larger rings.
    R=range(q) if q<=5 else (0,1,2,q-1)
    V=list(product(range(q),repeat=2))
    for a,b,c,e in product(R,repeat=4):
        if gcd(a*e-b*c,q)!=1:continue
        def T(x):return ((a*x[0]+b*x[1])%q,(c*x[0]+e*x[1])%q)
        def P(x):
            for _ in range(d):x=T(x)
            return x
        def diff(x,y):return tuple((i-j)%q for i,j in zip(x,y))
        I={diff(T(x),x) for x in V}
        J={diff(P(x),x) for x in V}
        K={x for x in V if T(x)==x}
        H={x for x in V if P(x)==x}
        assert J<=I and K<=H
        assert len(K)*len(I)==len(V)==len(H)*len(J)
        assert len(I)%len(J)==0
        matrices+=1

# Relative different norm for explicit prime-power cyclotomic towers.
# Absolute cyclotomic discriminant p^(p^(j-1)*(j*p-j-1)).
def discr_exp(p,j):return p**(j-1)*(j*(p-1)-1)
disc=0
for p,c,m in product((2,3,5,7,11,13),range(1,6),range(1,7)):
    if p==2 and c<2:continue
    d=p**m;n1=p**(c+m-1)*(p-1)
    delta=discr_exp(p,c+m)-d*discr_exp(p,c)
    assert delta==m*n1
    assert 0<=delta<=(c+m)*n1
    disc+=1
print(f"PASS {layers} layer inequalities and exact orders; {matrices} matrix kernel/cokernel controls; {disc} cyclotomic different norm cases")
