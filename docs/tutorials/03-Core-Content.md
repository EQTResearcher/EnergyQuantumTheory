# Key Concepts and Equations of the Energy Quantum Theory

Copyright (c) 2025 Kaisheng Li & Longji Li. Licensed under CC BY-SA 4.0.

## Unified Classification of Energy Quanta and Mass Quanta

The **Energy Quantum Theory (EQT)** proposes a **frequency-based classification framework** for all interactions and particles, unifying the fundamental forces and particle behaviors through their frequency characteristics:

- **Ultra-High Frequency (>>10²⁶ Hz, speculative)**: New mass quanta with rest mass (e.g., TeV-scale particles), potentially revealing new physics.
- **Extremely High Frequency (>10²⁰ Hz)**:
  - **Strong Force**: Mediated by gluons (~10²⁰ Hz).
  - **Weak Force**: Mediated by W⁺/W⁻/Z bosons (~10²⁵–10²⁶ Hz).
  - **Higgs Boson**: (~10²⁵ Hz), driving short-range microscopic interactions.
- **High Frequency (>10¹⁰ Hz)**: **Electromagnetic Force** (photons), driving atomic and molecular bonding.
- **Medium Frequency (10³–10¹⁰ Hz)**: Hypothetical dark matter-related forces (e.g., dark photons).
- **Low Frequency (<10³ Hz)**: **Gravity** (possible gravitons), driving macroscopic aggregation.
- **Extremely Low Frequency (10⁻⁴–10⁻³³ Hz)**: Dark energy-related forces (scalar fields), driving cosmic accelerated expansion.

The **strong force**, **electromagnetic force**, and **gravity** are mediated by bosons without rest mass. However, the **weak force** (W/Z bosons) and the **Higgs boson** have rest mass but are included in the frequency table. The rationale for their classification is as follows:

### Weak Force (W/Z Bosons)
- **Frequency Positioning**: The weak force is mediated by W⁺/W⁻/Z bosons, with mass (~80–90 GeV/c²) and a short propagation range (~10⁻¹⁸ m). Using $E = h f$, their energy (~10⁻⁸ J) corresponds to a frequency of ~10²⁶ Hz, far higher than gluons (~10²⁰ Hz).
- **Classification**: The weak force belongs to the **Extremely High Frequency** energy quantum range, associated with high-energy, short-range interactions, similar to the strong nuclear force.
- **Characteristics**: Weak force interactions (e.g., beta decay) involve flavor change and are high-energy but extremely short-range, consistent with extremely high frequencies.

### Higgs Boson
- **Frequency Positioning**: The Higgs boson (~125 GeV/c²) is a massive scalar boson with energy ~10⁻⁸ J, corresponding to a frequency of ~10²⁶ Hz, also in the **Extremely High Frequency** range.
- **Classification**: While the Higgs boson does not directly mediate a force, it gives mass to particles via the Higgs field. Its decay (e.g., producing photons or W/Z bosons) releases high-energy quanta, fitting the extremely high-frequency range.
- **Characteristics**: The Higgs boson influences particle motion and aggregation indirectly through field coupling with mass quanta, potentially playing a key role in the early universe (e.g., electroweak symmetry breaking).

**Speculation**: The frequency bands of W/Z bosons and the Higgs boson lie at the transition region between **energy quanta** and **mass quanta**, suggesting that the **Ultra-High Frequency** (>>10²⁶ Hz) range might correspond to particles with rest mass, representing a state of **frequency condensation**.

## Density Gradient and Force Derivation

The **energy quantum density field** $\rho(\mathbf{r}, t) = \hat{\phi}^\dagger \hat{\phi}$ represents the number density of energy quanta per unit volume, with dimensions J/m³. Its expectation value $\langle \rho \rangle \propto M/r^2$ describes the density distribution around a celestial body with mass $M$. The gravitational effect is hypothesized to originate from the **density gradient** $\nabla \rho$, generating an attractive force through graviton exchange.

Consider two celestial bodies with masses $M_1$ and $M_2$, separated by distance $r$. Their density fields are:

$$
\rho_1(\mathbf{r}) \propto \frac{M_1}{|\mathbf{r} - \mathbf{r}_1|^2}, \quad \rho_2(\mathbf{r}) \propto \frac{M_2}{|\mathbf{r} - \mathbf{r}_2|^2}
$$

The total density field superposition is $\rho_{\text{total}} \approx \rho_1 + \rho_2$, forming a high-density region in the intermediate area. Assuming the graviton exchange rate is proportional to the density gradient, the force is defined as:

$$
\mathbf{F} \propto -\nabla \langle \rho_{\text{total}} \rangle
$$

Calculating the gradient:

$$
\nabla \rho_1 \propto -\frac{M_1 (\mathbf{r} - \mathbf{r}_1)}{|\mathbf{r} - \mathbf{r}_1|^4}, \quad \nabla \rho_2 \propto -\frac{M_2 (\mathbf{r} - \mathbf{r}_2)}{|\mathbf{r} - \mathbf{r}_2|^4}
$$

Near the midpoint of the line connecting the two objects, $\nabla \rho_{\text{total}} \approx \nabla \rho_1 + \nabla \rho_2$, with direction pointing towards the other object and magnitude approximately:

$$
|\nabla \rho_{\text{total}}| \propto \frac{M_1 M_2}{r^3}
$$

Assuming a coupling constant $\kappa \approx \sqrt{8\pi G}$, the force is:

$$
\mathbf{F} \propto -\kappa^2 \nabla \rho_{\text{total}} \propto -\frac{G M_1 M_2}{r^2} \hat{r}
$$

This form is consistent with **Newton’s law of gravitation** $F = G M_1 M_2 / r^2$, indicating that the density gradient, through graviton exchange, reproduces classical gravity.

## Dynamic Equation and Positive Feedback

The dynamic equation describes the evolution of the density field:

$$
\frac{\partial \rho}{\partial t} = k \rho^m - D \nabla^2 \rho - \nabla \cdot (\rho \mathbf{v}) + S
$$

- The **positive feedback term** $k \rho^m$ (typically $m=2$) drives the growth of high-density regions, consistent with the attractive force from graviton exchange.
- Assuming material velocity $\mathbf{v} \propto -\nabla \langle \rho \rangle$, the fluid term $-\nabla \cdot (\rho \mathbf{v})$ reflects the flow of matter towards high-density regions:

$$
-\nabla \cdot (\rho \mathbf{v}) \propto \nabla \cdot (\rho \nabla \rho) \approx \rho \nabla^2 \rho + (\nabla \rho)^2
$$

The positive feedback term $k \rho^2$ amplifies density perturbations and, synergistically with the $(\nabla \rho)^2$ term, drives matter aggregation, similar to **Jeans instability** in galaxy formation. Numerical simulations (e.g., IllustrisTNG) show that initial density perturbations (amplitude $\delta \rho / \rho \approx 10^{-5}$) are amplified by positive feedback, forming galaxy clusters and filamentary structures, consistent with the gravitational effect of $\mathbf{F} \propto -\nabla \rho$.

## Contribution of Quantum Corrections

The **quantum correction term** $S_{\text{quantum}} \propto \hbar \nabla^2 \phi$ introduces fluctuations and tunneling effects, influencing the density gradient:

- **Microscopic Scales**: Quantum fluctuations provide initial perturbations for positive feedback, driving density growth. For example, quantum fluctuations in the early universe (observed in the CMB, Planck 2018) are amplified by positive feedback and graviton exchange, forming large-scale structures.
- **Macroscopic Scales**: Quantum corrections are averaged out by statistical effects, manifesting as classical gravity. Tunneling effects might alter graviton exchange probabilities in high-density regions (e.g., near black holes), but their contribution is negligible in the weak-field limit, where the dynamic equation remains dominated by $\nabla \rho$.
