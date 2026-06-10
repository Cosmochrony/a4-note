# A4-Note — The Born–Infeld Saturation Margin of the Chiral Modulus

*Antisymmetric Structure and the Reduction of the Generation Split to a Lorentzian Genus*

J. Beau, Independent Researcher, France

## Status

Preprint, v1.0.

## Abstract

This note is the companion of the **Projective Residue Schur reduction** (PRS) and takes up the
first of its open deliverables: the definition of the Lorentzian saturation functional
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

The identification of the Schur projector tilt with the Born–Infeld saturation modulus on the A4
locus is discharged to a tangential coincidence, conditional only on Schur transversality; the
Lorentzian genus computation is deliberately deferred.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It is the
companion to **PRS** (Schur form of $E_\Pi$, A4 stratification, finite/Lorentzian separation)
and discharges its first open deliverable: the definition of the saturated Born–Infeld
functional along the $J_\Pi$-odd modulus, with the sign convention locked by the admissibility
role of the functional. The remaining open deliverable — the computation of the chiral curvature
$\mu_\chi^2$ — is thereby reduced to a single Lorentzian genus question on the chiral
polarisation two-form.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/A4Note.tex` and produces
`out/A4Note.pdf`.
