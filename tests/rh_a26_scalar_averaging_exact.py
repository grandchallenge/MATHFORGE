"""Exact finite controls of SCen; no numerical claim about arithmetic units."""
from fractions import Fraction as Q
from itertools import product

def antiderivative(t):
    # periodic continuous tent f(t)=min(frac(t),1-frac(t)), mean 1/4
    t=Q(t);n=t//1;u=t-n
    return Q(n,4)+(u*u/2 if u<=Q(1,2) else u-u*u/2-Q(1,4))

def intervals():
    n=0
    for b in range(1,25):
        for a in range(-2*b,2*b+1):
            t=Q(a,b)
            assert antiderivative(t+1)-antiderivative(t)==Q(1,4)
            for l in (Q(1,3),Q(1),Q(2),Q(-1),Q(-3)):
                # integral of f along a translated integer loop in log coords.
                if l.denominator==1:
                    assert antiderivative(t+l)-antiderivative(t)==l/4
                assert (antiderivative(t+l)-antiderivative(t))+(antiderivative(t)-antiderivative(0))==antiderivative(t+l)
            n+=1
    return n

def weighted():
    n=0
    for r in range(1,5):
        for m in product((1,2),repeat=r):
            for t in product((-2,0,3),repeat=r):
                c=Q(sum(a*b for a,b in zip(m,t)),sum(m))
                p=[m[i]*(t[i]-c) for i in range(1,r)]
                z=[-sum(p,Q(0))/m[0]]+[p[i-1]/m[i] for i in range(1,r)]
                assert sum(a*b for a,b in zip(m,z))==0
                assert [x+c for x in z]==list(t)
                n+=1
    return n

def phases():
    n=0
    for a,b in product(range(-5,6),repeat=2):
        if a==b==0:continue
        d=a*a+b*b
        inv=(Q(a,d),Q(-b,d))
        # multiplication of conjugate inverse, entry, inverse
        for x,y in product(range(-2,3),repeat=2):
            u,v=inv
            l=(u*x+v*y,u*y-v*x)
            out=(l[0]*u-l[1]*v,l[0]*v+l[1]*u)
            assert out==(Q(x,d),Q(y,d))
            n+=1
    return n

if __name__=="__main__":
    for label,f in (("period shifts and exact cycle periods",intervals),("weighted logarithm decomposition",weighted),("scalar phase cancellation",phases)):
        print("PASS",label,f())
