"""Remark 'Weights and the cascade generator' (A4-Note 3.0): exact computation behind it.

X = log g with g = exp(E) exp(2F) in SL_2, lifted to Sym^2 in the basis (e_0, e_+, e_-); P_0 = diag(0.3, 1, 0.7).
The script computes ad_X^3 P_0 exactly, extracts its outer block on (e_+, e_-), splits it into J_Pi-even and J_Pi-odd
parts under J_Pi^(2) (J e_0 = -e_0, J e_+ = e_-), and checks that the J_Pi-odd outer part has a non-zero
off-diagonal entry (anti-Hermitian type, not seen by a J_3 carrier).
This is a computation on matrices: P_0 is not J_Pi-invariant, so no premise of the chiral two-form hypothesis holds.
Exact symbolic, no sampling. English.
"""

import sympy as sp


def sym2_lift(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    s2 = sp.sqrt(2)
    return sp.Matrix([[a + d, s2 * c, s2 * b], [s2 * b, 2 * a, 0], [s2 * c, 0, 2 * d]])


def main():
    E = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    g = (sp.eye(2) + E) * (sp.eye(2) + 2 * F)                      # exp(E) exp(2F), E^2 = F^2 = 0
    assert g == sp.Matrix([[3, 1], [2, 1]]) and g.det() == 1
    r = sp.acosh(sp.Rational(1, 2) * g.trace())                     # cosh r = 2
    X2 = (r / sp.sinh(r)) * (g - sp.Rational(1, 2) * g.trace() * sp.eye(2))
    X = sym2_lift(X2)
    P0 = sp.diag(sp.Rational(3, 10), 1, sp.Rational(7, 10))
    ad = lambda A, B: A * B - B * A
    Y = ad(X, ad(X, ad(X, P0)))
    J = sp.Matrix([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
    Yodd = (Y - J * Y * J.inv()) / 2
    outer = Yodd[1:, 1:]
    entry = sp.simplify(outer[0, 1])
    checks = {
        "outer_odd_offdiag_nonzero": entry != 0,
        "outer_odd_is_antisymmetric_not_J3": sp.simplify(outer[0, 1] + outer[1, 0]) == 0 and sp.simplify(outer[0, 0]) == 0,
        "P0_not_J_invariant": sp.simplify(P0 - J * P0 * J.inv()) != sp.zeros(3, 3),
    }
    for k, v in checks.items():
        print(f"  [{'OK ' if v else 'FAIL'}] {k}")
        assert v, k
    print("J_Pi-odd outer off-diagonal entry =", sp.nsimplify(entry), "=", sp.N(entry, 8))
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
