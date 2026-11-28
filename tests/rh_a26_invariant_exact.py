"""Finite exact controls; not original Lean replay."""
from itertools import product, permutations
from fractions import Fraction as F
from math import factorial

def rank(rows):
    piv = {}
    for row in rows:
        v = {i:F(x) for i,x in enumerate(row) if x}
        while v:
            i=min(v)
            if i not in piv:
                c=v[i]; piv[i]={j:x/c for j,x in v.items()}; break
            c=v[i]
            for j,x in piv[i].items():
                v[j]=v.get(j,F(0))-c*x
                if not v[j]: del v[j]
    return len(piv)

cases=0
for w,n,q in [(1,1,3),(1,2,2),(1,2,3),(2,1,2),(2,2,2),(2,1,3)]:
    basis=list(product(range(w*n),repeat=q))
    pairs=list(product(basis,repeat=2))
    ps=list(permutations(range(q)))
    rows=[]
    for p in ps:
        for labels in product(range(w),repeat=q):
            rows.append([int(tuple(i[k]//n for k in range(q))==labels and tuple(i[k] for k in p)==j) for i,j in pairs])
    # A' coefficients are constant on simultaneous-permutation orbits of compatible pairs.
    orbits={min((tuple(i[k] for k in p),tuple(j[k] for k in p)) for p in ps)
            for i,j in pairs if all(a//n==b//n for a,b in zip(i,j))}
    # Span of symmetrized compatible matrix units (polarization of powers).
    sym=[]
    for i,j in orbits:
        support={(tuple(i[k] for k in p),tuple(j[k] for k in p)) for p in ps}
        sym.append([int(x in support) for x in pairs])
    assert rank(sym)==len(orbits)
    assert rank(rows)>0
    # Every permutation generator commutes with each orbit generator.
    import collections
    def sparse(row):
        return {ij:v for ij,v in zip(pairs,row) if v}
    def mul(a,b):
        out=collections.defaultdict(int)
        for (i,j),x in a.items():
            for (k,l),y in b.items():
                if j==k: out[i,l]+=x*y
        return dict(out)
    for a in map(sparse,rows):
        for b in map(sparse,sym):
            assert mul(a,b)==mul(b,a)
            cases+=1
    print(w,n,q,"dim A",rank(rows),"dim A prime",len(orbits))
# Vandermonde invertibility on exact grid, and repeated-unit coefficient multiplicity.
for q in range(1,8):
    assert rank([[i**j for j in range(q+1)] for i in range(q+1)])==q+1
    assert len(list(permutations(range(q))))==factorial(q)
print("PASS",cases,"commuting generator pairs; 7 interpolation grids")
