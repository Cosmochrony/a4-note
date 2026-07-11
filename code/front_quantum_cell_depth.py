#!/usr/bin/env python3
"""Front "Generation stabilisation depths" -- the quantum (UV-catastrophe) third way.

Reconnaissance, exact, NO fit, NO mass input.

Jerome's analogy: the linear count N(lambda;n)~F_KM n is the Rayleigh-Jeans equipartition
(too small / divergent), the exponential A(n)=exp(beta* n) is the brutal regime; the Planck
cure is a DISCRETE occupation -- quantise the projective capacity entry. Stabilisation = the
first quantum of resolved projected capacity:
    n_g^qcell = inf{ n : I_{lambda_g}(n) >= DeltaI_g^cell },
with DeltaI_g^cell a capacity quantum fixed by the REPRESENTATION (dim rho_g, leading irrep
dimension, irrep count, or a single cell), NOT a fitted parameter.

This script tests whether quantising the CUMULATIVE COUNT escapes the structural lock just
deposited (PYO 1.8): every depth that is a function of c_g(p)=F_KM(lambda_g) inherits the
band-edge divergence c_1->0 and the symmetry pin c_2=1/2.

Key identity (proved here numerically + analytically): with the corpus cumulative projected
capacity at level g equal to the linear count, I_{lambda_g}(n) = N(lambda_g;n) = c_g(p) n,
    n_g^qcell = DeltaI_g^cell / c_g(p),
so the quantum sits in the NUMERATOR and c_g stays in the DENOMINATOR. Quantisation cures the
functional FORM but not the resolution DENSITY c_g where the obstruction lives.
A Bose/Planck occupation Phi_g(n) = 1/(exp(Delta_g/I_g(n)) - 1) gives, at its first quantum,
the SAME c_g-routed depth. Demonstrated below.

Brutal pass/fail (Jerome): PASS Dn in [50,80], q-stable, correctly ordered. FAIL otherwise.
Reuses spectral/relaxation/spectral_relaxation_lib.py (km_cdf, ADE_CASES).
"""

import math
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "spectral/relaxation"
sys.path.insert(0, str(LIB))
import spectral_relaxation_lib as R   # noqa: E402

CASE = "2I_ord5"
LEVELS = R.normalised_levels(CASE)                  # [20/24, 1, 30/24]
BLOCK_DIM = R.ADE_CASES[CASE]["dims"]               # [54, 25, 40] = sum of squares of irrep dims
LEAD_IRREP = [6, 5, 4]                              # leading irrep dim per block (6D+3D+3D / 5D / 4D+4D+2D+2D)
N_IRREPS = [3, 1, 4]                                # number of irreps per block
SUM_IRREP = [12, 5, 12]                             # sum of irrep dims per block
PRIMES = [5, 13, 29, 53]
BETA_STAR = 0.127
DN_REQ = math.log(3477.0) / BETA_STAR

QUANTA = {
    "block dim rho_g (=sat)": BLOCK_DIM,
    "leading irrep dim":      LEAD_IRREP,
    "sum of irrep dims":      SUM_IRREP,
    "irrep count":            N_IRREPS,
    "single cell (1,1,1)":    [1, 1, 1],
}

checks = []
def record(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def first_quantum_depth(dI, c):
    """n = inf{ n in N : c*n >= dI } = ceil(dI / c) (linear count I=c*n)."""
    return math.ceil(dI / c)


print("=== Quantum-cell depth on the cumulative count  I_{lambda_g}(n) = c_g(p) n ===")
print("    n_g^qcell = inf{ n : c_g n >= DeltaI_g } = ceil(DeltaI_g / c_g)\n")

c_by_p = {p: [float(R.km_cdf(l, p)) for l in LEVELS] for p in PRIMES}

worst_band_in_range = False
for qname, dI in QUANTA.items():
    print(f"  quantum = {qname:24s}  DeltaI_g = {dI}")
    gaps = []
    orders = []
    for p in PRIMES:
        c = c_by_p[p]
        n = [first_quantum_depth(d, ci) for d, ci in zip(dI, c)]
        gap = max(n) - min(n)
        gaps.append(gap)
        orders.append(tuple(int(x) for x in (n[0] > n[1], n[1] > n[2])))  # (n1>n2, n2>n3)
        print(f"      p={p:2d}: n=({n[0]:4d},{n[1]:4d},{n[2]:4d})  Dn={gap:4d}  "
              f"order(n1>n2,n2>n3)={orders[-1]}")
    in_band_all = all(50 <= g <= 80 for g in gaps)
    order_stable = len(set(orders)) == 1
    if in_band_all and order_stable:
        worst_band_in_range = True
    print(f"      -> Dn in [50,80] for all p? {in_band_all}   order q-stable? {order_stable}\n")

record("NO representation quantum gives Dn in [50,80] q-stably with a stable order",
       not worst_band_in_range,
       "every quantum reduces to n_g = DeltaI_g / c_g, c_g-locked")

# --------------------------------------------------------------------------
# The c_g lock, made explicit: n_g^qcell * c_g = DeltaI_g (a representation integer),
# so the depth is c_g-routed for EVERY quantum.
# --------------------------------------------------------------------------
print("=== The lock: n_g^qcell is c_g-routed (numerator = quantum, denominator = c_g) ===")
dI = LEAD_IRREP
p = 53
c = c_by_p[p]
prod = [first_quantum_depth(d, ci) * ci for d, ci in zip(dI, c)]
print(f"    leading-irrep quantum {dI}, p=53:  n_g * c_g = {[round(x,2) for x in prod]} ~ DeltaI_g {dI}")
record("n_g^qcell * c_g recovers the representation quantum (denominator is c_g, untouched)",
       all(abs(prc - d) <= 1.0 for prc, d in zip(prod, dI)),
       "quantisation acts on the numerator only")

# --------------------------------------------------------------------------
# A genuine Bose/Planck occupation on the linear count gives the SAME c_g-routed depth.
#   Phi_g(n) = 1/(exp(Delta_g / (c_g n)) - 1);  first quantum Phi=1 at exp(.)=2 ->
#   c_g n = Delta_g / ln 2  ->  n = Delta_g / (c_g ln 2).   Still ~ 1/c_g.
# --------------------------------------------------------------------------
print("\n=== Bose/Planck occupation on the count: still c_g-routed ===")
Delta = LEAD_IRREP
for p in PRIMES:
    c = c_by_p[p]
    n_bose = [Dg / (ci * math.log(2)) for Dg, ci in zip(Delta, c)]
    gap = max(n_bose) - min(n_bose)
    print(f"    p={p:2d}: n_Bose=({n_bose[0]:.1f},{n_bose[1]:.1f},{n_bose[2]:.1f})  Dn={gap:.1f}")
# divergence with p (band edge) persists
c5, c53 = c_by_p[5], c_by_p[53]
g5 = Delta[0]/(c5[0]*math.log(2)) - Delta[2]/(c5[2]*math.log(2))
g53 = Delta[0]/(c53[0]*math.log(2)) - Delta[2]/(c53[2]*math.log(2))
record("Bose-occupation first-quantum depth still diverges with p (band edge), not q-stable",
       g53 > 2 * g5, f"Dn {g5:.1f} (p=5) -> {g53:.1f} (p=53)")

print("\n=== VERDICT (quantum third way) ===")
print("Quantising the projective-capacity ENTRY does NOT escape the structural lock when the")
print("quantised object is the linear cumulative count I_{lambda_g}(n)=c_g(p) n: the first-")
print("quantum depth is n_g^qcell = DeltaI_g^cell / c_g(p) for EVERY representation quantum, and")
print("a Bose/Planck occupation gives the same c_g-routed depth. The quantum (the 'hbar of")
print("capacity') sits in the NUMERATOR = the representation datum DeltaI_g; the obstruction")
print("sits in the DENOMINATOR = the Kesten-McKay resolution density c_g(p), which quantisation")
print("does not touch. So the band-edge divergence (c_1->0) and the symmetry pin (c_2=1/2)")
print("survive, exactly as in PYO 1.8.")
print()
print("CONCEPTUAL PAYOFF (the analogy, correctly placed): the UV cure quantises the OCCUPATION")
print("DENSITY, not the mode count. The faithful third way is therefore to quantise the")
print("RESOLUTION DENSITY itself -- replace the continuous F_KM(lambda) by a discrete per-level")
print("occupation -- which is precisely a decaying capacity-controlled per-level profile")
print("sigma_{lambda_g}(n). The quantum analogy IDENTIFIES the deferred Weil/Schur object as the")
print("right one and tells us HOW to build it (as a Planck/Bose/Fermi occupation of the level")
print("resolution), rather than as an ad hoc decaying profile. Same future front, now principled.")

n_pass = sum(1 for _, ok, _ in checks if ok)
print(f"\n{n_pass}/{len(checks)} checks pass.")
assert n_pass == len(checks)
