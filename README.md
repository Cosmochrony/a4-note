# A4-Note — The Born–Infeld Saturation Margin of the Chiral Modulus

*Antisymmetric Structure and Lorentzian Genus of the Generation Split*

J. Beau, Independent Researcher, France

## Status

Working paper, v3.0 (candidate, not deposited). DOI: [10.5281/zenodo.20633931](https://doi.org/10.5281/zenodo.20633931)

## Abstract

This note is the companion of the **Projective Residue Schur reduction** (PRS) and takes up its
open deliverable on the Lorentzian saturation functional: the definition of
$\mathcal{B}_{\mathrm{sat}}(s)$ along the $J_\Pi$-odd modulus that controls the three-generation
split coefficient $u$.

Three results are established.

1. **Antisymmetry lemma.** The generation modulus is $J_\Pi$-odd, and the symmetric square
   $M = F_\chi F_\chi$ is $J_\Pi$-even from birth, so it cannot carry the oriented modulus; the primary
   modulus variable must be an antisymmetric chiral two-form $F_{\chi,\mu\nu}(s)$.

2. **Sign-locked saturation functional.** $\mathcal{B}_{\mathrm{sat}}(s)$ is defined as the
   Born–Infeld determinantal saturation margin of a supplied such two-form, with the overall sign fixed by
   the admissibility role of $\mathcal{B}_{\mathrm{sat}}$ (projection locking; axiom A4 selects
   saturated minima), not by matching a Maxwell weak-field expansion.

3. **Genus reduction.** The second variation reduces to
   $\mu_\chi := \partial_s^2 \mathcal{B}_{\mathrm{sat}}(0) = \tfrac{1}{2}\,P_{\chi,\mu\nu} P_\chi^{\mu\nu}$,
   so the existence and stability of the split are governed by the Lorentzian genus of
   the chiral polarisation $P_\chi$ in an effective co-metric of Lorentzian signature.

Premises that no source supplies are stated as hypotheses wherever a result uses them: a full-rank Lorentzian
co-metric, the construction of the two-form from the locking data, the coincidence of the Born–Infeld
modulus with the Schur tilt, the non-degeneracy of the split at the locked pair, and, for the
Schur-transverse branch, the hypotheses of PRS (chiral splitting, contraction, Lichnerowicz compression,
symbol condition, transport of the metaplectic opening to the locking operator, non-annihilation). The genus is not determined: the
central commutator does not supply an electric assignment, because the central direction is not
temporal in the co-metrics of the corpus (rank-three co-metric of Q5b with a zero central entry,
conditional completion of Q8, free temporal coefficient in Q11) and because no map from the
generation operator to a two-form is available.

For a supplied purely electric two-form the radicand is extended to quartic order: the
Born–Infeld pseudoscalar cancels, and the amplitude $|u|$ is reduced to the transverse cubic
backreaction of the two-form trajectory, modulo odd reparametrisation, together with the
boundary-versus-interior selection of the saturation problem. On the real symplectic cascade of
the model the transverse (spin-two) channel of the cubic response vanishes at the metaplectic phase
$\gamma = 0$ for every ordering and reference, so the amplitude mechanism is Born–Infeld
saturation; the sixth-order interior lock is doubly conditional, on a non-derived complex phase and
on a non-prescribed ordering. With the companion eliminated-block note, which fixes one block of
the $J_\Pi$-odd tangent as half the defect rate $\partial_s \Delta_\chi(P)|_0$ rather than a unique
carrier, the saturation contact $\Delta_\chi(s_*) = 0$ is the unique chart-independent A4 lock under
the stated premises. The magnitude $|u|$ itself is not predicted: it is fixed through the
chiral-frontier normalisation $\mathcal{N}_A$, a dictionary-bound quantity.

The even sector $\mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$ of $E_\Pi^2$ is the algebraic value of
$(C_2 - J_3^2)/C_2$ at $C_2 = 2$; reading it as the Born–Infeld even sector would require an
identification with the conditional $3 \times 3$ model of O30 on $\mathrm{Sym}^2(V_\rho)$ that is
not available and is not used.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It is the
companion to **PRS** (Schur form of $E_\Pi$, A4 stratification, finite/Lorentzian separation,
Schur-null / Schur-transverse dichotomy) and takes up its open deliverable on the saturated
Born–Infeld functional along the $J_\Pi$-odd modulus, with the sign convention locked by the
admissibility role of the functional. The Lorentzian genus is the sign of $P_{\mu\nu}P^{\mu\nu}$ of a
supplied two-form and is not determined here; what remains is the construction of that two-form, the
magnitude $|u|$, dictionary-bound through $\mathcal{N}_A$, and the upstream structural fronts (ADE
case selection, level-to-generation map, cascade exponent $\beta$, transfer constant
$N_{\mathrm{casc}}$).

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/A4Note.tex` and produces
`out/A4Note.pdf`.
