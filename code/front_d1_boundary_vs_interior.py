"""Algebra of a radicand contact versus an interior extremum of a truncated saturation functional (exact symbolic).

The script checks three algebraic facts and selects no locking mechanism:
  (1) the root s_c of the radicand Delta_chi(s) = 0 depends only on the radicand, not on the coefficients of the
      saturation functional B(s) or on a sextic parameter gamma;
  (2) a non-zero interior extremum s_int of a truncated B (B'(s) = 0) depends on the sextic coefficient and on gamma;
  (3) varying gamma moves s_int and leaves s_c untouched.
Which of the two configurations, if either, is the A4 lock is not established (A4-Note, remark on the absence of a
selection of the lock). No figures. Code and comments in English.
"""

import sympy as sp


def main():
    s = sp.symbols("s", real=True)
    # Radicand: electric/timelike, decreasing, reaches the BI bound D_chi=0 at finite |s|.
    D0, c = sp.symbols("D0 c", positive=True)
    D_chi = D0 - c * s**2
    s_contact = sp.sqrt(D0 / c)                       # boundary: geometric contact D_chi(s_c)=0
    assert sp.simplify(D_chi.subs(s, s_contact)) == 0

    # Saturation functional. Quartic data (mu2<0, supplied electric two-form, g4) are available; the sextic
    # coefficient is
    # g6 + gamma, where gamma is an assumed parameter of the sextic coefficient (no source fixes it).
    mu2, g4, g6, gamma, B0 = sp.symbols("mu2 g4 g6 gamma B0", real=True)
    B = B0 + (mu2 / 2) * s**2 + g4 * s**4 + (g6 + gamma) * s**6

    checks = {}

    # (1) Contact is fixed by the radicand alone: independent of all B-data and of the sextic parameter gamma.
    checks["contact_indep_g4"] = sp.diff(s_contact, g4) == 0
    checks["contact_indep_g6"] = sp.diff(s_contact, g6) == 0
    checks["contact_indep_gamma"] = sp.diff(s_contact, gamma) == 0
    checks["contact_indep_mu2"] = sp.diff(s_contact, mu2) == 0

    # (2) Non-trivial interior extremum: nonzero root of B'(s)=0, i.e. of
    #     f(s) = mu2 + 4 g4 s^2 + 6(g6+gamma) s^4 = 0.
    # The extremum condition itself depends on the sextic datum and on the phase gamma (df/d* != 0), so by
    # the implicit function theorem the root location moves with them.
    f = mu2 + 4 * g4 * s**2 + 6 * (g6 + gamma) * s**4
    checks["interior_cond_depends_on_g6"] = sp.simplify(sp.diff(f, g6)) != 0
    checks["interior_cond_depends_on_phase_gamma"] = sp.simplify(sp.diff(f, gamma)) != 0
    # Implicit ds/dgamma = -(df/dgamma)/(df/ds): generically non-zero at an interior root.
    ds_dgamma = -sp.diff(f, gamma) / sp.diff(f, s)
    checks["interior_root_moves_with_phase"] = sp.simplify(ds_dgamma) != 0

    # (3) Concrete exact instance: turning on the assumed sextic parameter gamma moves the interior root in
    # w = s^2, while the radicand contact s_c is untouched. Use a genuine sextic (g6 != 0).
    w = sp.symbols("w", positive=True)
    subs0 = {D0: 4, c: 1, mu2: sp.Rational(-1, 1), g4: sp.Rational(1, 8), g6: sp.Rational(1, 100), B0: 5}

    def interior_w(gval):
        quad = (mu2 + 4 * g4 * w + 6 * (g6 + gamma) * w**2).subs({**subs0, gamma: gval})
        return [r for r in sp.solve(quad, w) if r.is_real and r > 0]

    w_g0 = interior_w(0)[0]
    w_gp = interior_w(sp.Rational(1, 100))[0]
    s_c_val = sp.nsimplify(s_contact.subs(subs0))
    checks["phase_moves_interior"] = sp.simplify(w_gp - w_g0) != 0
    checks["phase_leaves_contact"] = sp.simplify(
        s_contact.subs({**subs0, gamma: sp.Rational(1, 100)}) - s_contact.subs({**subs0, gamma: 0})
    ) == 0
    dwint_dg6 = sp.simplify(sp.diff(f, g6))
    dwint_dgamma = sp.simplify(sp.diff(f, gamma))
    w_int_g0, w_int_gp = w_g0, w_gp

    for name, ok in checks.items():
        print(f"  [{'OK ' if ok else 'FAIL'}] {name}")
        assert ok, name

    print()
    print("radicand contact  s_c = sqrt(D0/c)  -> independent of B-coefficients and of the phase gamma")
    print("                       (fixed by the radicand alone: AVAILABLE, chart-independent)")
    print("interior extremum condition f(s) = mu2 + 4 g4 s^2 + 6(g6+gamma) s^4 = 0")
    print("   df/d(g6)    =", dwint_dg6, "   (extremum condition depends on the non-derived sextic datum)")
    print("   df/d(gamma) =", dwint_dgamma, "   (extremum condition depends on the assumed sextic parameter gamma)")
    print(f"   exact instance: s_c = {s_c_val} (gamma-invariant); "
          f"interior s_int^2: gamma=0 -> {w_int_g0}, gamma=1/100 -> {w_int_gp} (gamma-dependent)")
    print()
    print("RESULT: the radicand contact D_chi(s_*)=0 depends on the radicand alone; the interior extremum of a")
    print("truncated B depends on the sextic coefficient and gamma. No selection of the lock is established.")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
