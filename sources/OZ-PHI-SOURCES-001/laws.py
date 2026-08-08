from __future__ import annotations

def divs(n): return [d for d in range(1,n+1) if n%d==0]
def chi3(n): return 0 if n%3==0 else (1 if n%3==1 else -1)
def chi4(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
def chi5(n): return 0 if n%5==0 else (1 if n%5 in (1,4) else -1)
def psi1(n): return [0,1,0,0,-1][n%5]
def psi2(n): return [0,0,1,-1,0][n%5]
def sig(n,p,chi=lambda _:1,mode=1):
    if n<=0:return 0
    if mode==1:return sum(chi(d)*d**p for d in divs(n))
    return sum(chi(n//d)*d**p for d in divs(n))
def dil(n,q,fn): return fn(n//q) if n%q==0 else 0

def c(f,n):
    if f=='A': return sig(n,2,chi3,1)-dil(n,2,lambda m:sig(m,2,chi3,1))
    if f=='B': return sig(n,2,chi3,2)-6*dil(n,2,lambda m:sig(m,2,chi3,2))-8*dil(n,4,lambda m:sig(m,2,chi3,2))
    if f=='C': return sig(n,2,chi3,2)-8*dil(n,2,lambda m:sig(m,2,chi3,2))
    if f=='D': return sum((psi1(d)-2*psi2(d))*d**2 for d in divs(n))
    if f=='E': return sig(n,2,chi4,2)-8*dil(n,2,lambda m:sig(m,2,chi4,2))
    if f=='F': return sig(n,2,chi3,2)-7*dil(n,2,lambda m:sig(m,2,chi3,2))-8*dil(n,4,lambda m:sig(m,2,chi3,2))
    if f=='alpha': return sig(n,3)-17*dil(n,2,lambda m:sig(m,3))-9*dil(n,3,lambda m:sig(m,3))+16*dil(n,4,lambda m:sig(m,3))+153*dil(n,6,lambda m:sig(m,3))-144*dil(n,12,lambda m:sig(m,3))
    if f=='gamma': return sig(n,3)-28*dil(n,2,lambda m:sig(m,3))+63*dil(n,3,lambda m:sig(m,3))-36*dil(n,6,lambda m:sig(m,3))
    if f=='delta': return sig(n,3)-14*dil(n,2,lambda m:sig(m,3))-dil(n,3,lambda m:sig(m,3))+16*dil(n,4,lambda m:sig(m,3))+14*dil(n,6,lambda m:sig(m,3))-16*dil(n,12,lambda m:sig(m,3))
    if f=='epsilon': return sig(n,3)-21*dil(n,2,lambda m:sig(m,3))+84*dil(n,4,lambda m:sig(m,3))-64*dil(n,8,lambda m:sig(m,3))
    if f=='zeta': return sum(chi3(d)*chi3(n//d)*d**3 for d in divs(n))
    if f=='eta': return sig(n,3,chi5,2)-14*dil(n,2,lambda m:sig(m,3,chi5,2))-16*dil(n,4,lambda m:sig(m,3,chi5,2))
    raise KeyError(f)
FAMILIES=['A','B','C','D','E','F','alpha','gamma','delta','epsilon','zeta','eta']
def table(nmax=60): return {f:[c(f,n) for n in range(1,nmax+1)] for f in FAMILIES}
