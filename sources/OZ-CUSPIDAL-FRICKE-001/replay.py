from __future__ import annotations
from fractions import Fraction as Q
from math import comb,lcm
import hashlib,json

def level6(nmax=40):
    w=[Q(1),Q(17)]
    for n in range(1,nmax): w.append(Q(17*(2*n+1)*w[n]-n*w[n-1],n+1))
    b=[Q(0),Q(1)]
    for m in range(2,nmax+1):
        c1=(2*m-1)*(17*(m-1)**2+17*(m-1)+5);c2=(m-1)**3
        b.append(Q(c1*b[m-1]-c2*b[m-2]+w[m-1],m**3))
    return w,b

def d1(nmax=40):
    b=[Q(0),Q(1)]
    for m in range(2,nmax+1):
        c1=(2*m-1)*(10*(m-1)**2+10*(m-1)+4);c2=64*(m-1)**3
        b.append(Q(c1*b[m-1]-c2*b[m-2]+comb(2*m-2,m-1),m**3))
    return b

def denominator_witness(seq,nmax=40):
    d=1;out=[]
    for n in range(1,nmax+1):
        d=lcm(d,n);x=seq[n]*d**3
        out.append({'n':n,'d_n':d,'scaled_integer':x.denominator==1,'scaled_value':str(x.numerator) if x.denominator==1 else str(x)})
    return out

def eta_product_prefix(nmax=12):
    a=[1]+[0]*nmax
    for r in (1,2,3,6):
        k=1
        while r*k<=nmax:
            step=r*k
            for _ in range(2):
                b=a[:]
                for i in range(nmax+1-step): b[i+step]-=a[i]
                a=b
            k+=1
    f=[0]*(nmax+1)
    for i in range(nmax): f[i+1]=a[i]
    return f

def witness_digest(seq,nmax=40):
    w=denominator_witness(seq,nmax)
    raw=json.dumps(w,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest(), all(x['scaled_integer'] for x in w)

def evidence():
    w,b=level6(40);bs=d1(40);f=eta_product_prefix(12)
    fstar=f[:]
    for n in range(2,len(fstar),2): fstar[n]-=4*f[n//2]
    d6,ok6=witness_digest(b);d1d,ok1=witness_digest(bs)
    return {
      'level6':{'w_prefix':[str(x) for x in w[:5]],'B_prefix':[str(x) for x in b[:5]],'denominator_range':[1,40],'all_scaled_integer':ok6,'witness_sha256':d6},
      'd1':{'B_prefix':[str(x) for x in bs[:5]],'denominator_range':[1,40],'all_scaled_integer':ok1,'witness_sha256':d1d},
      'newform':{'f6_q1_q8':f[1:9],'fstar_q1_q8':fstar[1:9]}
    }
