"""Chart covariance of the defect rate and of the first contact (exact symbolic, no sampling).

Setting: the Schur modulus s_proj and a Born-Infeld modulus s_BI = psi(s_proj), psi(0) = 0, psi'(0) != 0 (the
coincidence hypothesis of A4-Note, used only to read the lock along s_BI). Facts checked:
  (a) the first-order defect rate is covariant: d/ds_proj = psi'(0) d/ds_BI, so the rate alone is not a physical
      magnitude;
  (b) when s_* is the first contact of the radicand, the value u(s_*) computed in either chart is the same point of the
      trajectory;
  (c) the genus sign mu_chi^2 = B''(0) is invariant under the reparametrisation (the corollary of A4-Note);
  (d) by contrast, the extremum of a finite polynomial truncation of B is chart-dependent: its location differs
      between the two charts.
No selection of the A4 lock between a boundary contact and an interior stationary point is established. No figures.
"""

import sympy as sp


def main():
    s, sigma = sp.symbols("s sigma", real=True)
    checks = {}

    # Non-degenerate ODD reparametrisation s_BI = psi(s_proj), psi(0)=0, psi'(0)=a1!=0 (odd preserves
    # the J_Pi-odd parity of the modulus). Use sigma = s_proj, s = s_BI.
    a1, a3, a5 = sp.Rational(3, 2), sp.Rational(1, 5), sp.Rational(-1, 40)
    psi = a1 * sigma + a3 * sigma**3 + a5 * sigma**5     # s_BI = psi(s_proj)

    # Odd split function u(s_BI) with u(0)=0 (Lemma u-odd: u(-s) = -u(s)); generic odd cubic jet.
    b1, b3 = sp.Rational(7, 4), sp.Rational(-2, 3)
    u = lambda x: b1 * x + b3 * x**3

    # Even saturation functional B(s_BI) = B0 + (mu2/2) s^2 + g4 s^4 + g6 s^6, supplied electric two-form, mu2 < 0
    # (hypothesis).
    B0, mu2, g4, g6 = sp.Integer(5), sp.Rational(-1, 1), sp.Rational(1, 8), sp.Rational(-1, 200)
    B = lambda x: B0 + (mu2 / 2) * x**2 + g4 * x**4 + g6 * x**6

    # Radicand D_chi(s_BI): electric -> decreasing, hits the bound D=0 at finite |s|. Pick a rational root.
    # D(x) = D0 - c x^2, D0=c*4 -> contact at x_* = 2 (the BI saturation contact, a geometric condition).
    c = sp.Integer(3)
    D0 = c * 4
    D = lambda x: D0 - c * x**2
    x_star_BI = sp.sqrt(D0 / c)                          # = 2, contact in the s_BI chart
    assert sp.simplify(x_star_BI - 2) == 0

    # (a) Rate covariance: d/ds_proj (u o psi)|_0 = u'(0) * psi'(0); ratio to the s_BI rate is psi'(0).
    rate_BI = sp.diff(u(s), s).subs(s, 0)
    rate_proj = sp.diff(u(psi), sigma).subs(sigma, 0)
    checks["a_rate_covariant_phiprime"] = sp.simplify(rate_proj - sp.diff(psi, sigma).subs(sigma, 0) * rate_BI) == 0
    checks["a_rate_not_invariant"] = sp.simplify(rate_proj - rate_BI) != 0   # covariant, not invariant

    # (b) u at the radicand contact is coordinate-independent.
    # s_BI chart: contact x_* from D(x)=0; physical value u(x_*).
    u_phys_BI = sp.nsimplify(u(x_star_BI))
    # s_proj chart: the SAME geometric condition is D(psi(sigma))=0; its positive root sigma_* gives the
    # physical point psi(sigma_*); evaluate u there and compare.
    roots = sp.solve(sp.Eq(D(psi), 0), sigma)
    sigma_star = [r for r in roots if r.is_real and r > 0]
    sigma_star = min(sigma_star, key=lambda r: sp.Abs(r))   # first positive contact
    u_phys_proj = sp.nsimplify(u(psi.subs(sigma, sigma_star)))
    checks["b_u_at_contact_invariant"] = sp.simplify(u_phys_proj - u_phys_BI) == 0

    # (c) Genus sign reparametrisation-invariance: d^2/dsigma^2 (B o psi)|_0 = psi'(0)^2 * B''(0).
    B_proj_2nd = sp.diff(B(psi), sigma, 2).subs(sigma, 0)
    B_BI_2nd = sp.diff(B(s), s, 2).subs(s, 0)
    phip0 = sp.diff(psi, sigma).subs(sigma, 0)
    checks["c_genus_chainrule"] = sp.simplify(B_proj_2nd - phip0**2 * B_BI_2nd) == 0
    checks["c_genus_sign_preserved"] = sp.sign(B_proj_2nd) == sp.sign(B_BI_2nd)

    # (d) Truncated interior extremum is chart-dependent (chart-dependent extremum).
    # s_BI chart: extremum of B truncated at quartic order, B4(x) = B0 + (mu2/2)x^2 + g4 x^4.
    B4_BI = B0 + (mu2 / 2) * s**2 + g4 * s**4
    ext_BI = [r for r in sp.solve(sp.diff(B4_BI, s), s) if r.is_real and r > 0]
    ext_BI = min(ext_BI, key=lambda r: sp.Abs(r))
    # s_proj chart: compose then truncate to quartic in sigma, extremise, map back through psi.
    B_comp = sp.expand(B(psi))
    B4_proj = sum(t for t in B_comp.as_ordered_terms() if sp.degree(t, sigma) <= 4)
    ext_proj_sigma = [r for r in sp.solve(sp.diff(B4_proj, sigma), sigma) if r.is_real and r > 0]
    ext_proj_sigma = min(ext_proj_sigma, key=lambda r: sp.Abs(r))
    ext_proj_mapped = psi.subs(sigma, ext_proj_sigma)       # same physical chart (s_BI) for comparison
    checks["d_truncated_extremum_chart_dependent"] = sp.simplify(ext_proj_mapped - ext_BI) != 0

    for name, ok in checks.items():
        print(f"  [{'OK ' if ok else 'FAIL'}] {name}")
        assert ok, name

    print()
    print("rate (s_BI)   =", rate_BI, "   rate (s_proj) =", sp.nsimplify(rate_proj),
          "  -> covariant by psi'(0) =", phip0, "(rate alone NOT physical)")
    print("contact s_* (geometric, D_chi=0): u(s_*) =", u_phys_BI,
          "= same in both charts: the contact POINT is chart-independent; the parameter value s_* transforms")
    print("truncated interior extremum: s_BI-chart =", sp.nsimplify(ext_BI),
          ", s_proj-chart mapped back =", sp.nsimplify(ext_proj_mapped),
          "-> DIFFERENT physical points -> chart-dependent")
    print()
    print("RESULT: the first-contact POINT of the trajectory is chart-independent (its parameter value transforms);")
    print("the extremum of a truncated polynomial is chart-dependent. No selection of the lock is established.")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
