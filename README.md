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

Results, each for a supplied two-form and under the hypotheses named in the paper:

1. **Symmetric square.** The generation modulus is $J_\Pi$-odd under a $J_\Pi$-covariant family, and the symmetric
   square $M = F_\chi F_\chi$ of an odd two-form is $J_\Pi$-even, so it cannot carry the branch sign; the carrier is
   taken, by hypothesis, to be an odd antisymmetric chiral two-form $F_{\chi,\mu\nu}(s)$.

2. **Saturation functional.** $\mathcal{B}_{\mathrm{sat}}(s)$ is defined as the Born–Infeld determinantal saturation
   margin of such a supplied two-form, with the sign fixed by the admissibility role of axiom A4, not by a Maxwell
   weak-field expansion.

3. **Genus reduction.** The second variation is
   $\mu_\chi := \partial_s^2 \mathcal{B}_{\mathrm{sat}}(0) = \tfrac{1}{2}\,P_{\chi,\mu\nu} P_\chi^{\mu\nu}$, the
   Lorentzian genus of the chiral polarisation $P_\chi$: $\mu_\chi > 0$ makes the symmetric point a strict local
   minimum of $\mathcal{B}_{\mathrm{sat}}$ and $\mu_\chi < 0$ a strict local maximum. Under a local-minimum reading of
   axiom A4, a negative genus means the symmetric point is not locked; the existence of a locked pair and the
   non-vanishing of $u$ there are hypotheses.

Hypotheses that no source supplies are stated where used: a full-rank Lorentzian co-metric, the construction of the
two-form from the locking data, the local-minimum reading of A4, the existence and non-degeneracy of the locked pair,
the covariance of the locking family under $J_\Pi$, and from PRS the generation-reading hypothesis and the first-order
transport hypothesis; the coincidence with the Born–Infeld modulus is used only to read the lock along that modulus.
The scope is that of PRS: for the reference operator the split vanishes, for a general locking operator the consequences
are conditional, and no mechanism for a non-zero split is derived. The genus is not
determined: the central commutator does not supply an electric assignment, because the central direction is not
temporal in the co-metrics of the corpus (rank-three co-metric of Q5b with a zero central entry, conditional completion
of Q8, free temporal coefficient in Q11) and because no map from the generation operator to a two-form is available.

The radicand is extended to quartic order. Its quartic coefficient depends on the parametrisation of the modulus
(it shifts by $\alpha\,P\cdot P$ under $s \to s + \alpha s^3$), so it selects neither a boundary contact nor an
interior stationary point. Under the construction hypothesis the carrier is one-dimensional, so the two-form trajectory
is collinear and the cubic response is parallel to $P$. For a purely electric two-form the radicand is then exactly
$1 - |E|^2 \varphi(s)^2/\beta^2$, a contact exists if and only if $|\varphi|$ reaches $\beta/|E|$, and in the chart
$t = \varphi(s)$ the first contact is $t_* = \beta/|E|$. The defect rate is covariant under reparametrisation, and the
first contact and $|u(s_*)|$ are chart-independent when the contact exists. No selection of the A4 lock between a
boundary contact and an interior stationary point is established. The magnitude $|u|$ is not predicted: it is fixed
through the chiral-frontier normalisation
$\mathcal{N}_A$, a dictionary-bound quantity.

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
