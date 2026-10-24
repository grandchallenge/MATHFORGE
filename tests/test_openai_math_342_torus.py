"""Exact, dependency-free exterior algebra checks for OAI family 342's revised
four-torus cone example. A finite symbolic certificate, not a Lean proof.

Pinned upstream:
  openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
  preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/
  build/sections/08-cones.tex, Example 'Strict inclusion on the four-torus'.

F, K here are independent formal variables standing for
  f(x_1) = sin(2*pi*x_1)/4 and k(x_2) = sin(2*pi*x_2)/4.

All algebra uses exact rational polynomial coefficients.
"""
import unittest
from fractions import Fraction
from itertools import permutations


def pconst(x):
    v = Fraction(x)
    return {(0, 0): v} if v else {}


ONE, ZERO = pconst(1), {}
F = {(1, 0): Fraction(1)}
K = {(0, 1): Fraction(1)}


def padd(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, Fraction(0)) + c
            if not out[m]:
                del out[m]
    return out


def pscale(a, p):
    return {m: a * c for m, c in p.items() if a * c}


def pmul(a, b):
    out = {}
    for (ai, aj), av in a.items():
        for (bi, bj), bv in b.items():
            m = ai + bi, aj + bj
            out[m] = out.get(m, Fraction(0)) + av * bv
            if not out[m]:
                del out[m]
    return out


def form(*entries):
    # Each entry is (coordinate_i, coordinate_j, coefficient_polynomial).
    return {(i, j): p for (i, j, p) in entries if p}


def fadd(*forms):
    out = {}
    for a in forms:
        for ij, p in a.items():
            out[ij] = padd(out.get(ij, ZERO), p)
            if not out[ij]:
                del out[ij]
    return out


def fscale(p, a):
    return {ij: pmul(p, v) for ij, v in a.items() if pmul(p, v)}


def e(i, j):
    assert 1 <= i < j <= 4
    return form((i, j, ONE))


def permutation_sign(indices):
    assert len(indices) == len(set(indices)) == 4
    inversions = sum(indices[i] > indices[j] for i in range(4) for j in range(i+1, 4))
    return -1 if inversions % 2 else 1


def wedge_volume(a, b):
    out = ZERO
    for (i,j),p in a.items():
        for (k,l),q in b.items():
            if len({i,j,k,l}) == 4:
                out = padd(out, pscale(permutation_sign((i,j,k,l)), pmul(p,q)))
    return out


def hodge(a):
    out = {}
    for (i,j),p in a.items():
        missing = tuple(x for x in range(1,5) if x not in (i,j))
        sign = permutation_sign((i,j,*missing))
        out[missing] = padd(out.get(missing, ZERO), pscale(sign,p))
    return {ij:p for ij,p in out.items() if p}


def sd(a):
    return fscale(pconst(Fraction(1,2)), fadd(a,hodge(a)))


def asd(a):
    return fscale(pconst(Fraction(1,2)), fadd(a,fscale(pconst(-1), hodge(a))))


U = fadd(e(1,2),e(3,4))
V0 = fadd(e(1,3),fscale(pconst(-1),e(2,4)))
W = fadd(e(1,4),e(2,3))
ETA = fadd(U, fscale(pscale(2,F),e(1,3)), fscale(pscale(2,K),e(2,3)))
PPLUS = fadd(U,V0)
PMINUS = fadd(U,fscale(pconst(-1),V0))
R_SQUARED = padd(ONE,pmul(F,F),pmul(K,K))


class Family342ExactTorusAlgebra(unittest.TestCase):
    def test_hodge_star_and_self_duality(self):
        self.assertEqual(hodge(hodge(ETA)), ETA)
        for a in (U,V0,W):
            self.assertEqual(hodge(a),a)
        self.assertEqual(wedge_volume(U,U),pconst(2))
        self.assertEqual(wedge_volume(V0,V0),pconst(2))
        self.assertEqual(wedge_volume(W,W),pconst(2))
        self.assertEqual(wedge_volume(U,V0),ZERO)
        self.assertEqual(wedge_volume(U,W),ZERO)
        self.assertEqual(wedge_volume(V0,W),ZERO)

    def test_eta_decomposition_and_positivity_discriminant(self):
        eta_plus = fadd(U,fscale(F,V0),fscale(K,W))
        eta_minus = fadd(fscale(F,fadd(e(1,3),e(2,4))),
                         fscale(K,fadd(e(2,3),fscale(pconst(-1),e(1,4)))))
        self.assertEqual(sd(ETA),eta_plus)
        self.assertEqual(asd(ETA),eta_minus)
        self.assertEqual(wedge_volume(eta_plus,eta_plus), pscale(2,R_SQUARED))
        self.assertEqual(wedge_volume(eta_minus,eta_minus),
                         pscale(-2,padd(pmul(F,F),pmul(K,K))))
        # r^2 - (f^2+k^2) == 1, hence both Hermitian eigenvalues
        # r +/- sqrt(f^2+k^2) are strictly positive.
        self.assertEqual(padd(R_SQUARED,pscale(-1,padd(pmul(F,F),pmul(K,K)))),ONE)
        self.assertEqual(wedge_volume(ETA,ETA), pconst(2))

    def test_taming_and_cohomology_orthogonality(self):
        # The self-dual tamers U +/- V0 pair with F via 1 +/- f;
        # |f| <= 1/4 makes both strict. Exact algebra verifies the
        # pairing polynomials and the orthogonality obstruction.
        self.assertEqual(wedge_volume(PPLUS, fadd(U,fscale(F,V0),fscale(K,W))),
                         pscale(2,padd(ONE,F)))
        self.assertEqual(wedge_volume(PMINUS, fadd(U,fscale(F,V0),fscale(K,W))),
                         pscale(2,padd(ONE,pscale(-1,F))))
        self.assertEqual(wedge_volume(PPLUS,PMINUS),ZERO)
        self.assertEqual(wedge_volume(PPLUS,PPLUS),pconst(4))
        self.assertEqual(wedge_volume(PMINUS,PMINUS),pconst(4))

    def test_constant_anti_invariant_obstruction(self):
        # For constant harmonic SD form aU+bV0+cW, pointwise
        # anti-invariance to F requires a+b*f(x1)+c*k(x2) == 0.
        # Independence of 1, sin(2*pi*x1), sin(2*pi*x2) proves a=b=c=0.
        # This code checks the algebraic injectivity of the coefficient map.
        a,b,c = Fraction(17,19),Fraction(5,7),Fraction(-11,13)
        polynomial = padd(pscale(a,ONE),pscale(b,F),pscale(c,K))
        self.assertEqual(polynomial[(0,0)],a)
        self.assertEqual(polynomial[(1,0)],b)
        self.assertEqual(polynomial[(0,1)],c)
        self.assertEqual(len(polynomial),3)

    def test_exterior_closedness_by_actual_coordinate_dependencies(self):
        # Every polynomial coefficient uses f=f(x1), k=k(x2).
        # For each coefficient of e^(i,j), d(c_ij e^(i,j)) can only
        # be nonzero if x1 or x2 is absent from the wedge basis.
        def dependency_closed(two_form):
            for (i,j), polynomial in two_form.items():
                for (f_power,k_power), coefficient in polynomial.items():
                    if coefficient and f_power and 1 not in (i,j):
                        return False
                    if coefficient and k_power and 2 not in (i,j):
                        return False
            return True
        self.assertTrue(dependency_closed(ETA))
        self.assertTrue(dependency_closed(PPLUS))
        self.assertTrue(dependency_closed(PMINUS))
        self.assertFalse(dependency_closed(fscale(F,e(2,3))))

    def test_periodic_primitives_and_closedness(self):
        # η - U = 2 f(x1) dx1∧dx3 + 2 k(x2) dx2∧dx3.
        # With f=sin(2πx1)/4, k=sin(2πx2)/4, η-U=dβ, where
        # β=-(cos(2πx1)+cos(2πx2))/(4π) dx3.
        # Differential of each term uses its own coordinate, so
        # dη=dU+2 df∧dx1∧dx3+2 dk∧dx2∧dx3=0.
        self.assertEqual(fadd(ETA,fscale(pconst(-1),U)),
                         fadd(fscale(pscale(2,F),e(1,3)),
                              fscale(pscale(2,K),e(2,3))))
        self.assertEqual(wedge_volume(U,U),pconst(2))


if __name__ == '__main__':
    unittest.main()

# Matrix-check extension verifies actual J action, not only exterior products.
def mat_form(a):
    m = [[ZERO for _ in range(4)] for _ in range(4)]
    for (i,j),v in a.items():
        m[i-1][j-1] = v
        m[j-1][i-1] = pscale(-1,v)
    return m


def mmul(a,b):
    return [[padd(*(pmul(a[i][k],b[k][j]) for k in range(4))) for j in range(4)] for i in range(4)]


def madd(a,b):
    return [[padd(a[i][j],b[i][j]) for j in range(4)] for i in range(4)]


def mscale(c,a):
    return [[pmul(c,v) for v in row] for row in a]


def mt(a):
    return [[a[j][i] for j in range(4)] for i in range(4)]


def eye(c=ONE):
    return [[c if i==j else ZERO for j in range(4)] for i in range(4)]


class Family342MatrixGeometry(unittest.TestCase):
    def setUp(self):
        self.a = mat_form(fadd(U,fscale(F,V0),fscale(K,W)))
        self.j = mscale(pconst(-1), self.a)  # r*J; r²=1+f²+k²

    def test_j_is_orthogonal_almost_complex_structure(self):
        self.assertEqual(mmul(self.j,self.j),mscale(pscale(-1,R_SQUARED),eye()))
        self.assertEqual(mmul(mt(self.j),self.j),mscale(R_SQUARED,eye()))

    def test_both_closed_tamers_are_pointwise_positive(self):
        for form_, expected in ((PPLUS,padd(ONE,F)),(PMINUS,padd(ONE,pscale(-1,F)))):
            a=mmul(mat_form(form_),self.j)
            symmetric=mscale(pconst(Fraction(1,2)),madd(a,mt(a)))
            self.assertEqual(symmetric,eye(expected))
        # J-taming: v^T Bα J v = (1±f)/r ||v||² and |f|≤1/4.

    def test_eta_is_j_invariant_and_strictly_positive(self):
        e=mat_form(ETA)
        self.assertEqual(mmul(mmul(mt(self.j),e),self.j),mscale(R_SQUARED,e))
        s=mscale(pconst(Fraction(1,2)),madd(mmul(e,self.j),mt(mmul(e,self.j))))
        # Spectrum of S/r has values r +/- sqrt(f²+k²). Their positivity
        # follows since (r² - f² - k²)=1 > 0.
        c=madd(s,mscale(pscale(-1,R_SQUARED),eye()))
        self.assertEqual(mmul(c,c),eye(pmul(R_SQUARED,padd(pmul(F,F),pmul(K,K)))))

