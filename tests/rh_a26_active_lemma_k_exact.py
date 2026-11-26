"""Exact controls for active Lemma K numerical inequalities, not field homology."""
from itertools import product
from fractions import Fraction as Q


def valuation(a,p):
    assert a
    v=0
    while a%p==0:
        a//=p;v+=1
    return v


def run():
    lte=0
    for p,d,e in product((2,3,5,7),range(1,21),range(1,21)):
        v=2+valuation(d,p)+valuation(e,p)
        modulus=p**(v+1)
        assert valuation((pow(1+p*p,d*e,modulus)-1)%modulus,p)==v
        lte+=1
    local=0
    for e,n in product(range(1,51),repeat=2):
        assert 3+e<=2*(2*e)*(2*e+3)
        x=2*e*n
        d=(n+1)*(4*e+4);nn=d*n
        assert d<=8*x and nn<=4*x*x and 2*e*nn<=x**5
        assert 73*x**4<=x**11
        v=e*n
        assert 7681212*v**6<=(2*v)**24
        local+=1
    poly=0
    for u,Y in product(range(2,101),(Q(1,2),Q(2,3),Q(1),Q(2),Q(10))):
        b=u+2*u*u;g=u+2*u*Y+2;c=f=u
        assert ((b+f)*g+c+f)*u<=u**9*Y
        poly+=1
    assert 5*(max(24,9)+2)+11==141
    assert max(141,0)+9==150
    print(f'PASS {lte} local valuation identities; {local} descent/local/exponent cases; {poly} polynomial bounds')


if __name__=='__main__':
    run()
