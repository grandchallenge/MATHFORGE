#!/usr/bin/env python3
"""Independent exact-Q checks, weights 1–3, for F008 equations (1.2)–(1.4).

Uses the associative enveloping presentation of t4. The two-sided ideal in
weight 3 is spanned by multiplication of quadratic braid relators by one
generator on either side. No Lean imports, floating-point or random choices.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from sympy import Matrix

def add(*xs):
    out = defaultdict(Fraction)
    for x in xs:
        for word, coeff in x.items():
            out[word] += coeff
    return {k: v for k, v in out.items() if v}

def scale(x, c):
    return {k: c*v for k, v in x.items() if c*v}

def mul(a, b):
    out = defaultdict(Fraction)
    for x, cx in a.items():
        for y, cy in b.items():
            out[x+y] += cx*cy
    return {k: v for k, v in out.items() if v}

def atom(i):
    return {(i,): Fraction(1)}

def bracket(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))

def words(w, a, b):
    v = {(): Fraction(1)}
    for i in w:
        v = mul(v, a if i == 0 else b)
    return v

def subst(p, a, b):
    return add(*(scale(words(w, a, b), c) for w, c in p.items()))

def insert_row(row, pivots):
    row = dict(row)
    while row:
        p = min(row)
        if p not in pivots:
            c = row[p]
            pivots[p] = {k: v/c for k, v in row.items()}
            return
        c = row[p]
        for k, v in pivots[p].items():
            row[k] = row.get(k, Fraction(0)) - c*v
            if not row[k]:
                del row[k]

def canonical_remainder(row, pivots):
    row = dict(row)
    for p in sorted(pivots):
        if p not in row:
            continue
        c = row[p]
        for k, v in pivots[p].items():
            row[k] = row.get(k, Fraction(0)) - c*v
            if not row[k]:
                del row[k]
    return row

edges = [(i,j) for i in range(4) for j in range(i+1,4)]
lookup = {e:i for i,e in enumerate(edges)}
def t(i, j):
    return atom(lookup[tuple(sorted((i,j)))])

disjoint = [bracket(t(i,j),t(k,l)) for i,j,k,l in permutations(range(4),4)]
triples = [bracket(t(i,j),add(t(i,k),t(j,k)))
           for i,j,k in permutations(range(4),3)]
def ideal(n, relators):
    pivots = {}
    for r in relators:
        if n == 2:
            insert_row(r, pivots)
        elif n == 3:
            for j in range(6):
                insert_row(mul(atom(j), r), pivots)
                insert_row(mul(r, atom(j)), pivots)
    return pivots

x, y = atom(0), atom(1)
free = {
    1: [x, y],
    2: [bracket(x,y)],
    3: [bracket(x,bracket(x,y)), bracket(y,bracket(x,y))]
}
def conditions(p, quotient):
    a = add(p,subst(p,y,x))
    b = add(p,subst(p,y,scale(add(x,y),-1)),
            subst(p,scale(add(x,y),-1),x))
    c = add(
        subst(p,t(0,1),add(t(1,2),t(1,3))),
        subst(p,add(t(0,2),t(1,2)),t(2,3)),
        scale(subst(p,t(1,2),t(2,3)),-1),
        scale(subst(p,add(t(0,1),t(0,2)),add(t(1,3),t(2,3))),-1),
        scale(subst(p,t(0,1),t(1,2)),-1))
    return {"anti":a, "three":b, "pent":canonical_remainder(c, quotient)}

for n, basis in free.items():
    q = ideal(n, disjoint+triples)
    columns = [{(tag,w):c for tag, v in conditions(p,q).items()
                for w,c in v.items()} for p in basis]
    coordinates = sorted(set().union(*(set(col) for col in columns)))
    matrix = Matrix([[col.get(k,0) for col in columns]
                     for k in coordinates])
    kernel = matrix.nullspace()
    print(f"degree={n} free_dim={len(basis)} braid_ideal_dim={len(q)} "
          f"rank={matrix.rank()} solution_dim={len(kernel)}")
    assert len(kernel) == (1 if n == 3 else 0)
    if n == 3:
        assert list(kernel[0]) == [1,1]
print("INDEPENDENT_LOW_WEIGHT_CONCORDANCE_PASS")

sigma3 = add(*free[3])
assert not conditions(sigma3, ideal(3,disjoint+triples))["pent"]
bad_ideal = ideal(3,disjoint)
remainder = conditions(sigma3,bad_ideal)["pent"]
assert remainder
print("HOSTILE_MISSING_THREE_STRAND_RELATIONS_DETECTED",
      len(remainder))

flipped_term = scale(subst(sigma3,t(0,1),t(1,2)),2)
wrong_pentagon = canonical_remainder(flipped_term,ideal(3,disjoint+triples))
assert wrong_pentagon
print("HOSTILE_PENTAGON_SIGN_FLIP_DETECTED",len(wrong_pentagon))
