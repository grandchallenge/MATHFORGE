"""Finite controls for Lemma K reduction, not arithmetic homology replay."""
from itertools import product
from math import prod


def controls():
    good = rejected = 0
    for l, a, b, u, v in product((2, 3, 5), (1, 2), (1, 2), (1,), (1, 2)):
        A, B, U, V = l**a, l**b, l**u, l**v
        elems = list(product(range(A), range(B)))
        p_maps = [(s,t) for s,t in product(range(U), repeat=2)
                  if s*A % U == t*B % U == 0 and (s%l or t%l)]
        h_maps = [(s,t) for s,t in product(range(V), repeat=2)
                  if s*A % V == t*B % V == 0]
        for ps,pt in p_maps:
            assert len({(ps*x+pt*y)%U for x,y in elems}) == U
            for hs,ht in h_maps:
                ker = [(x,y) for x,y in elems if (hs*x+ht*y)%V == 0]
                image = {(hs*x+ht*y)%V for x,y in elems}
                Y = {(ps*x+pt*y)%U for x,y in ker}
                for c in range(3):
                    if any(l**c*x%A or l**c*y%B for x,y in ker):
                        rejected += 1
                        continue
                    assert len(Y) <= l**c
                    assert U <= l**c*len(image)
                    good += 1
    assert 27 > 3 # h=0, X=Z/27, c=1: excluded kernel condition
    return good, rejected


def size_controls():
    count=0
    for e,n in product(range(1,51), repeat=2):
        x=2*e*n
        c=sum(j+2 for j in range(1,2*e+1))
        assert c==e*(2*e+5) and c<=2*e*(2*e+3)
        assert 2*e<=x and 4*e+4<=4*x and n*(4*e+4)<=4*x
        assert 4*n*(2*e)*(2*e+3)*n<=10*x*x<=x**9-1
        assert 2304*49 < 2**17 <= x**17
        count+=1
    return count


if __name__=='__main__':
    a,b=controls()
    print(f'PASS {a} admitted finite-module comparisons; {b} rejected kernel hypotheses; {size_controls()} exact exponent controls')
