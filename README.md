# A4-Note — The Born–Infeld Saturation Margin of the Chiral Modulus

*Antisymmetric Structure, Lorentzian Genus, and Electric Determination of the Generation Split*

J. Beau, Independent Researcher, France

## Status

Working paper, v2.0. DOI: [10.5281/zenodo.20633931](https://doi.org/10.5281/zenodo.20633931)

## Abstract

This note is the companion of the **Projective Residue Schur reduction** (PRS) and takes up its
open deliverable on the Lorentzian saturation functional: the definition of
$\mathcal{B}_{\mathrm{sat}}(s)$ along the $J_\Pi$-odd modulus that controls the three-generation
split coefficient $u$.

Three results are established.

1. **Antisymmetry lemma.** The generation modulus is $J_\Pi$-odd, and the symmetric square
   $M = F_\chi F_\chi$ is $J_\Pi$-even from birth, so it cannot carry the oriented modulus or the
   spontaneous $V-A$ branch choice; the primary modulus variable must be an antisymmetric chiral
   two-form $F_{\chi,\mu\nu}(s)$.

2. **Sign-locked saturation functional.** $\mathcal{B}_{\mathrm{sat}}(s)$ is defined as the
   Born–Infeld determinantal saturation margin of this two-form, with the overall sign fixed by
   the admissibility role of $\mathcal{B}_{\mathrm{sat}}$ (projection locking; axiom A4 selects
   saturated minima), not by matching a Maxwell weak-field expansion. This neutralises the
   convention sign-trap that would otherwise make the split sign a free choice.

3. **Genus reduction.** The second variation reduces to
   $\mu_\chi := \partial_s^2 \mathcal{B}_{\mathrm{sat}}(0) = \tfrac{1}{2}\,P_{\chi,\mu\nu} P_\chi^{\mu\nu}$,
   so the existence and stability of the split are governed entirely by the Lorentzian genus of
   the chiral polarisation $P_\chi$ in the effective metric $g^{\mu\nu} = 2\eta^{\mu\nu}$.

The coincidence lock is discharged to a tangential coincidence; the Schur transversality on which
it rests is closed in PRS in the present Lorentzian spin stratum, selecting the Schur-transverse
branch. Assembling the projector-completion grading, the oriented-cascade lift, and the
symbol-compatible spin frame, the genus is determined: in the Schur-transverse branch the chiral
polarisation is electric, so $\mu_\chi < 0$ and the split opens spontaneously, $u \neq 0$.

The radicand is then extended to quartic order: the Born–Infeld pseudoscalar cancels on the
electric locus, and the amplitude $|u|$ is reduced to the transverse cubic backreaction of the
two-form trajectory, modulo odd reparametrisation, together with the boundary-versus-interior
selection of the saturation problem. On the corpus-derived real symplectic cascade the transverse
(spin-two) channel of the cubic response vanishes at the metaplectic phase $\gamma = 0$ for every
ordering and reference, so the derived amplitude mechanism is Born–Infeld saturation while the
split persists, $u \neq 0$; the sixth-order interior lock is doubly conditional, on a non-derived
complex phase and on a non-prescribed ordering. Using the companion eliminated-block note, the
boundary-versus-interior selection is closed by admissibility: the saturation contact
$\Delta_\chi(s_*) = 0$ is the unique chart-independent A4 lock, with invariant magnitude $u(s_*)$.
The magnitude $|u|$ itself is not predicted: it is fixed through the chiral-frontier normalisation
$\mathcal{N}_A$, a dictionary-bound quantity.

The even sector $\mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$ of $E_\Pi^2$ is the algebraic value of
$(C_2 - J_3^2)/C_2$ at $C_2 = 2$; reading it as the Born–Infeld even sector would require an
identification with the conditional $3 \times 3$ model of O30 on $\mathrm{Sym}^2(V_\rho)$ that is
not available and is not used.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It is the
companion to **PRS** (Schur form of $E_\Pi$, A4 stratification, finite/Lorentzian separation,
Schur transversality) and discharges its open deliverable on the saturated Born–Infeld functional
along the $J_\Pi$-odd modulus, with the sign convention locked by the admissibility role of the
functional. The Lorentzian genus is determined electric in the Schur-transverse branch, so the
split exists; what remains is the magnitude $|u|$, dictionary-bound through $\mathcal{N}_A$, and
the upstream structural fronts (ADE case selection, level-to-generation map, cascade exponent
$\beta$, transfer constant $N_{\mathrm{casc}}$).

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/A4Note.tex` and produces
`out/A4Note.pdf`.
