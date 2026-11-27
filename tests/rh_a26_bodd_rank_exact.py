"""Finite exact controls for BOdd weight arithmetic and Hermitian trace parity.
Gaussian integer pairs, no floating-point arithmetic or arithmetic homology replay.
"""
from itertools import permutations, product
from math import prod

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def sc(c,a):return (c*a[0],c*a[1])
def summ(xs):
    r=(0,0)
    for x in xs:r=add(r,x)
    return r
def mm(A,B):
    return tuple(tuple(summ(mul(A[i][k],B[k][j]) for k in range(len(A))) for j in range(len(A))) for i in range(len(A)))
def trace(xs):
    A=xs[0]
    for B in xs[1:]:A=mm(A,B)
    return summ(A[i][i] for i in range(len(A)))
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def herm(a,b,c,d):return (((a,0),(c,d)),((c,-d),(b,0)))
def blk(A,d):
    n=len(A)
    return tuple(tuple(A[i%n][j%n] if i//n==j//n else (0,0) for j in range(d*n)) for i in range(d*n))
def contraction(ys,p):
    n=len(ys[0]);q=len(p)
    def term(a):
        r=(1,0)
        for i in range(q):r=mul(r,ys[i][a[i]][a[p[i]]])
        return r
    return summ(term(a) for a in product(range(n),repeat=q))
def cycles(p):
    seen=set();c=0
    for i in range(len(p)):
        if i in seen:continue
        c+=1
        while i not in seen:seen.add(i);i=p[i]
    return c
def main():
    w=0
    for l,k in product(range(1,9),range(0,18,2)):
        for j in range(1,k+2):
            v=prod(l**j-l**(i+2) for i in range(k))
            assert (v==0)==(j>=2 or l==1 and k>0)
            w+=1
    b=0
    for q in (1,2,3,4):
        ys=[herm(i+1,2-i,i%3-1,2*i-1) for i in range(q)]
        for p in permutations(range(q)):
            assert contraction([blk(A,2) for A in ys],p)==sc(2**cycles(p),contraction(ys,p))
            b+=1
    a=0
    for q in (1,3,5):
        for s in range(8):
            ys=[herm(i+s+1,2*i-s,(i+s)%3-1,(2*i+s)%5-2) for i in range(q)]
            assert trace(ys[::-1])==conj(trace(ys))
            v=summ(sc(sign(p),trace([ys[i] for i in p])) for p in permutations(range(q)))
            assert v[1 if q%4==1 else 0]==0
            a+=1
    # Weight-one zero does not by itself detect homology; kernel inclusion needed.
    assert (0,1)[0]==0 and (0,1)!=(0,0)
    print(f"PASS {w} exact weight factors; {b} block contraction identities; {a} trace parity controls; detection negative control")
if __name__=="__main__":main()
