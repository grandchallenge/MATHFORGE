"""Exact finite controls for the composite-field prime restriction and minusBound.

These enumerate fixing subgroups of the actual cyclotomic unit groups,
not number-field cohomology. Integer inequalities avoid floating-point
logarithm estimates. The general proofs are in the companion dossier.
"""
from math import gcd, lcm, factorial, prod

def units(m):
    return [a for a in range(m) if gcd(a,m)==1]

def prime_factors(n):
    assert n>0
    ans=set()
    p=2
    while p*p<=n:
        if n%p==0:
            ans.add(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ans.add(n)
    return ans

def subgroup(m,gens):
    H={1%m}
    for a in gens:
        assert gcd(a,m)==1
        powers={1%m}; b=a%m
        while b not in powers:
            powers.add(b);b=b*a%m
        H={a*b%m for a in H for b in powers}
    return H

def check_field(h,m,H,q,p):
    assert q%8==3 and p%16==7 and gcd(q*p,m)==1
    assert prime_factors(q)=={q} and prime_factors(p)=={p}
    A=2**(h+2); N=lcm(A,m,q,p)
    Um=units(m); o=len(Um)//len(H)
    coset={a:min(a*b%m for b in H) for a in Um}
    def leg(a,p):return 1 if pow(a%p,(p-1)//2,p)==1 else -1
    def image(a):
        return (min(a%A,(-a)%A),coset[a%m],leg(a,q),leg(a,p))
    U=units(N); images={image(a) for a in U}
    identity=image(1)
    fixing=[a for a in U if (a%A in (1,A-1) and a%m in H and leg(a,q)==1 and leg(a,p)==1)]
    assert set(fixing)=={a for a in U if image(a)==identity}
    n=len(U)//len(fixing)
    assert len(U)==n*len(fixing) and n==len(images)
    assert (2**(h+2)*o)%n==0 and n%o==0
    assert prime_factors(n)-{2}==prime_factors(o)-{2}
    assert {im[1] for im in images}==set(coset.values())
    fixing_set=set(fixing)
    assert all(pow(a,2**(h+1)*o,N) in fixing_set for a in U)
    # Independent exact count: quadratic factors are independent of first
    # two restrictions, but those first two can overlap at the prime 2.
    assert n==4*len({(im[0],im[1]) for im in images})
    return n,o,len(U)

def degree_tests():
    cases=0; elements=0; overlap=0; no_odd=0
    for m in (1,4,5,8,11,13,16,20,25):
        q,p=(3,7) if gcd(m,21)==1 else (11,23)
        U=units(m)
        for h in (2,3):
            for H in ({1%m},subgroup(m,[-1]),set(U)):
                n,o,count=check_field(h,m,H,q,p)
                cases+=1;elements+=count
                if m%2==0 and n<2**(h+2)*o:overlap+=1
                if not (prime_factors(o)-{2}):no_odd+=1
    n,o,ambient=check_field(2,7,{1,6},11,23)
    assert (n,o,ambient)==(48,3,10560)
    assert prime_factors(ambient)-prime_factors(n)=={5,11}
    assert overlap and no_odd
    return cases+1,elements+ambient,overlap,no_odd

def budget_tests():
    checks=0; sums=0
    for F in (1,2,3,7,16,48,101):
        for t in range(2,41):
            values=[]
            for e in range(1,t):
                k=e+1
                bnd=16*F**(k+1)*factorial(k)
                assert bnd<=(t*F)**(2*t+5)
                values.append(bnd);checks+=1
            assert prod(values)<=(t*F)**(3*t*t)
            assert sum(e+1 for e in range(1,t))<=t*t
            sums+=1
    return checks,sums

def polynomial_bounds():
    checks=0
    for n in (1,2,3,6,12,48):
        for F in (n,n+1,2*n):
            for t in (1,2,5,16,100):
                u=F*t
                assert n*t*t*u<=u**4
                for l in (3,5,7,11):
                    assert l*n*n*t*t*(l*u)**2<=l**3*u**4
                    checks+=1
    return checks

if __name__=="__main__":
    a,b,c,d=degree_tests();e,f=budget_tests()
    print(f"PASS {a} composite fixing-group cases, {b} unit actions, {c} overlapping-modulus strict divisibilities, {d} no-odd-bad-prime cases; {e} integer Bernoulli size bounds, {f} exponent-sum budgets, {polynomial_bounds()} polynomial domination checks; ambient-degree negative control")
