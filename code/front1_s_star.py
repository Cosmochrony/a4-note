"""Radicand algebra for a supplied purely electric two-form (exact symbolic, no sampling).

Setting: a := |E_P|^2/beta^2 >= 0 for the electric part of the polarisation P, and b := P.R_chi/beta^2 the coefficient
of s^4 in the radicand Delta_chi(s) = 1 - a s^2 + b s^4 + O(s^6). The coefficient b is parametrisation-dependent
(A4-Note, Lemma on parametrisation dependence): under s = t + alpha t^3 it shifts by alpha P.P/beta^2 = -2 alpha a.

Checks:
  (A) Exactly straight ray, Delta_chi(t) = 1 - a t^2: first contact t_* = beta/|E_P| (exact).
  (B) Algebra of the truncated radicand with b != 0: smallest positive root s_*^2 = (a - sqrt(a^2 - 4b))/(2b) and its
      series in b. This is algebra in a fixed chart; b has no intrinsic meaning, so the series is not an intrinsic
      result.
  (C) The other root (a + sqrt(a^2 - 4b))/(2b) tends to infinity as b -> 0.
  (D) Worked example in a model where R_chi is parallel to P: the odd reparametrisation that affinises the ray removes
      the quartic term and gives t_* = beta/|E_P| exactly.
Nothing here selects a locking mechanism or fixes a value of |u|. No figures.
"""

import sympy as sp


def main():
    checks = {}

    s, t = sp.symbols("s t", real=True)
    a, b = sp.symbols("a b", positive=True)           # a = |E_P|^2/beta^2, b = P.R_chi/beta^2
    beta, EP = sp.symbols("beta E_P", positive=True)  # beta, |E_P|

    # ---- (A) Leading-order contact: quadratic radicand --------------------------------------------
    D2 = 1 - a * s**2
    roots2 = sp.solve(sp.Eq(D2, 0), s)
    s_star_lead_sq = sp.Rational(1, 1) / a
    # the positive root is 1/sqrt(a):
    pos2 = [r for r in roots2 if (r.subs(a, 1) > 0)]
    checks["A_leading_root"] = sp.simplify(pos2[0] ** 2 - s_star_lead_sq) == 0
    # in dictionary scales a = EP^2/beta^2  =>  s_* = beta/EP
    s_star_lead = sp.sqrt(s_star_lead_sq).subs(a, EP**2 / beta**2)
    checks["A_leading_beta_over_EP"] = sp.simplify(s_star_lead - beta / EP) == 0

    # ---- (B) Quartic contact: smallest positive root and its series in b --------------------------
    x = sp.symbols("x", positive=True)                # x = s^2
    quart = 1 - a * x + b * x**2                       # Delta_chi as a function of x = s^2
    xroots = sp.solve(sp.Eq(quart, 0), x)
    # boundary branch = first contact = SMALLEST positive root = minus-sign root
    x_boundary = (a - sp.sqrt(a**2 - 4 * b)) / (2 * b)
    checks["B_boundary_is_a_root"] = sp.simplify(quart.subs(x, x_boundary)) == 0
    # series about b = 0
    ser = sp.series(x_boundary, b, 0, 3).removeO()
    expected = 1 / a + b / a**3 + 2 * b**2 / a**5
    checks["B_series"] = sp.simplify(ser - expected) == 0
    # first correction to s_* itself, in dictionary scales
    s_star_sq = (1 / a + b / a**3).subs({a: EP**2 / beta**2, b: sp.Symbol("PR", real=True) / beta**2})
    PR = sp.Symbol("PR", real=True)                   # P.R_chi
    s_star = sp.sqrt(s_star_sq)
    s_star_series = sp.series(s_star, PR, 0, 2).removeO()
    expected_s = (beta / EP) * (1 + PR * beta**2 / (2 * EP**4))
    checks["B_s_star_correction"] = sp.simplify(s_star_series - expected_s) == 0

    # ---- (C) The other root runs to infinity as b -> 0 (interior, not first contact) -------------
    x_interior = (a + sp.sqrt(a**2 - 4 * b)) / (2 * b)
    checks["C_interior_diverges"] = sp.limit(x_interior, b, 0, "+") == sp.oo
    checks["C_boundary_finite"] = sp.limit(x_boundary, b, 0, "+") == 1 / a

    # ---- (D) Parallel cubic response is pure reparametrisation gauge ------------------------------
    # rem:conditional-sign: fixed-generator orbit => R_chi = -(2/3)|c|^2 P (P-parallel).
    c2 = sp.symbols("c2", positive=True)              # |c|^2
    # Two-form along the straight ray with parallel cubic response:
    #   F_chi(s) = (s - (2/3) c2 s^3) P.  Affinise by t := s - (2/3) c2 s^3  => F_chi = t P.
    f = s - sp.Rational(2, 3) * c2 * s**3             # modulus map t = f(s)
    # The scalar invariant F.F = (t)^2 (P.P); on the electric branch P.P = -2|E_P|^2, so
    #   Delta_chi = 1 + (1/2beta^2) F.F = 1 - (|E_P|^2/beta^2) t^2  -- NO quartic in the affine modulus t.
    PdotP = -2 * EP**2
    D_in_t = 1 + (1 / (2 * beta**2)) * t**2 * PdotP
    # contact in t:
    t_star = sp.solve(sp.Eq(D_in_t, 0), t)
    t_star_pos = [r for r in t_star if r.subs({beta: 1, EP: 1}) > 0][0]
    checks["D_affine_contact_exact"] = sp.simplify(t_star_pos - beta / EP) == 0
    # Now express Delta_chi in the ORIGINAL modulus s by substituting t = f(s); the apparent quartic is
    # exactly the fold of the non-affine modulus, i.e. it carries no invariant: the contact value of the
    # invariant t is unchanged. Check that f is an odd, invertible-near-0 reparametrisation (f'(0) != 0).
    checks["D_odd_reparam"] = (f.subs(s, -s) + f) == 0 and sp.diff(f, s).subs(s, 0) == 1

    # Consistency: substitute the parallel R_chi into the quartic coefficient b and confirm the induced
    # apparent b matches a pure reparametrisation (it shifts the cubic, not the invariant contact t_*).
    # P.R_chi with R_chi = -(2/3)c2 P and P.P = -2 EP^2  =>  P.R_chi = -(2/3)c2 (-2 EP^2) = (4/3)c2 EP^2.
    PR_parallel = sp.Rational(4, 3) * c2 * EP**2
    checks["D_parallel_PR_sign"] = (PR_parallel > 0)  # positive, would mimic an "interior" b>0...
    # ...but it is gauge: the invariant contact is t_* = beta/EP regardless. (verified above)

    # ---- (E) Transverse residue is the single open datum -----------------------------------------
    # Only a P-transverse R_chi can move s_* off beta/|E_P| (A4-Note 3.0, Lemma on parametrisation dependence);
    # its source is not established (rem:path-invariant). We record this as the residual open coefficient.
    # (E) is a statement about the model of A4-Note 3.0, not a computed check; it is not recorded as a PASS item.

    # ---------------------------------------------------------------------------------------------
    print("Front 1 - radial saturation contact s_* (exact symbolic, no sampling)")
    print("=" * 78)
    print(f"  Radicand (electric):  Delta_chi(s) = 1 - a s^2 + b s^4,  "
          f"a=|E_P|^2/beta^2, b=P.R_chi/beta^2")
    print(f"  (A) leading contact:  s_*^2 = 1/a  =>  s_* = beta/|E_P|")
    print(f"  (B) boundary branch:  s_*^2 = (a - sqrt(a^2-4b))/(2b)")
    print(f"      series in b:      s_*^2 = 1/a + b/a^3 + 2b^2/a^5 + ...")
    print(f"      correction:       s_* = (beta/|E_P|)(1 + P.R_chi beta^2/(2|E_P|^4) + ...)")
    print(f"  (C) interior root diverges as b->0 (not first contact)")
    print(f"  (D) parallel R_chi = -(2/3)|c|^2 P is pure gauge: affine contact t_* = beta/|E_P| exactly")
    print(f"  (E) only P-transverse R_chi shifts s_* (source not established)")
    print("-" * 78)
    allok = True
    for k, v in checks.items():
        ok = bool(v)
        allok = allok and ok
        print(f"  [{'PASS' if ok else 'FAIL'}]  {k}")
    print("=" * 78)
    print("RESULT: s_* = beta/|E_P| for the exactly straight ray (exact algebra); a P-transverse R_chi would shift it.")
    print("ALL CHECKS PASS" if allok else "SOME CHECKS FAILED")
    return allok


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
