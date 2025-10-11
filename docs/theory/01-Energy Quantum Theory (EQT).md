# Energy Quantum Theory (EQT)

Copyright (c) 2025 Kaisheng Li & Longji Li. Licensed under CC BY-SA 4.0.

The theoretical framework of EQT centers on the energy quantum number density ($\rho(\mathbf{r}, t) = \sum_f \rho_f$) and frequency ($f$), unifying the four fundamental interactions (electromagnetic, weak, strong, gravitational) via Planck's formula ($E = hf$), same-frequency resonance, energy minimization, and density gradients, while remaining compatible with Big Bang cosmology. The force definition $\mathbf{F} = -\kappa m \nabla \rho$ links force to the gradient of the density field, with frequency $f$ determining spin $s$ and operator form. The density field $\rho(\mathbf{r}, t)$, as a sum of multi-frequency subfields (unit: J/m³), is described by dynamic equations governing its evolution. Below, I reorganize the dynamic equations, field variables, Lagrangian, and field equations to clarify their relationships, ensuring consistency in spin, frequency, force, and spacetime definitions (time: $\frac{\partial \rho}{\partial t}$, space: $\rho(\mathbf{r})$ ), providing a clear and unified theoretical framework.

---

## 1. Field Variables

Field variables form the core of the theory, describing the physical behavior of energy quanta and mass quanta, characterized by frequency $f$ and spin $s$:

- **Energy Quantum Number Density** ( $\rho_f(\mathbf{r}, t)$ ):
  - Represents the energy density of energy quanta (e.g., photons, gluons, gravitons) at frequency $f$, unit J/m³, expressed as $\rho_f = \langle \phi_f^\dagger \phi_f \rangle$ (quantum field expectation value).
  - Total density field: $\rho(\mathbf{r}, t) = \sum_f \rho_f$, total energy density: $\epsilon = \sum_f \rho_f \cdot hf$.
  - Frequency ranges:
    - Low frequency ($f \approx 10 - 10^3 \, \text{Hz}$): Gravitons (spin 2).
    - Medium frequency ($f \approx 10^6 - 10^{20} \, \text{Hz}$): Photons, gluons (spin 1).
    - High frequency ($f \approx 10^{23} - 10^{25} \, \text{Hz}$): W/Z bosons (spin 1), mass quanta (spin 1/2).
- **Mass Quantum Field** ( $\psi_m(f, s, \mathbf{r}, t)$ ):
  - Describes particles with rest mass (e.g., electrons, quarks, $f = mc^2/h$, spin $s = 1/2$; W/Z bosons, $s = 1$).
  - Frequency $f > 10^{24} \, \text{Hz}$, spinor field (spin 1/2) or vector field (spin 1).
- **Vector Field** ( $A^\mu(f, \mathbf{r}, t)$ ):
  - Describes spin-1 energy quanta (e.g., photons, gluons, $f \approx 10^6 - 10^{24} \, \text{Hz}$).
  - Field strength tensor: $F^{\mu\nu}(f) = \partial^\mu A^\nu(f) - \partial^\nu A^\mu(f)$.
- **Tensor Field** ( $h^{\mu\nu}(f, \mathbf{r}, t)$ ):
  - Describes spin-2 gravitons ($f \approx 10 - 10^3 \, \text{Hz}$), related to spacetime curvature.
- **Higgs Field** ( $\phi_H(f, \mathbf{r}, t)$ ):
  - Spin 0, scalar field, frequency $f \approx 3.02 \times 10^{25} \, \text{Hz}$, confers rest mass to mass quanta: $m(f) = g_H \phi_H(f)$.
- **Dark Energy Field** ( $\rho_\phi(\mathbf{r}, t)$ ):
  - Approximately uniform, $\rho_\phi \approx 10^{-120} \, \text{J/m}^3 \approx 10^{-47} \, \text{GeV}^4$, $\nabla \rho_\phi \approx 0$, drives cosmic expansion.

**Spacetime Definition**:

- Time: $\frac{\partial \rho}{\partial t} = \sum_f \frac{\partial \rho_f}{\partial t}$, rate of density change, reflecting cosmic evolution (high freq. $\sim 10^{-25} \, \text{s}$: QGP; low freq. $\sim 10^{18} \, \text{s}$: modern universe).
- Space: $\rho(\mathbf{r}) = \sum_f \rho_f(\mathbf{r})$, density distribution, gradient $\nabla \rho = \sum_f \nabla \rho_f$ drives forces (microscopic $\sim 10^{-18} \, \text{m}$: strong/weak forces; macroscopic $\sim 10^{22} \, \text{m}$: gravity; cosmic scale $\sim 10^{26} \, \text{m}$: dark energy).

---

## 2. Force Definition

Force is driven by the density field gradient:

$$
\mathbf{F} = -\kappa m \nabla \rho = -\kappa m \sum_f \nabla \rho_f
$$

- $\rho(\mathbf{r}, t) = \sum_f \rho_f$: Total energy density, unit J/m³.
- $\nabla \rho$: Gradient, unit J/m⁴ = kg/s²·m³.
- $m$: Mass of affected particle, unit kg.
- $\kappa(f, s)$: Frequency- and spin-dependent coupling coefficient, unit m³/s², matching force units:

$$
\mathbf{F} \, (\text{kg·m/s}^2) = \kappa \, (\text{m}^3/\text{s}^2) \cdot m \, (\text{kg}) \cdot \nabla \rho \, (\text{kg/s}^2 \cdot \text{m}^3)
$$
  
- Specific forms:
  - **Strong force** (gluons, $f \approx 10^{23} - 10^{24} \, \text{Hz}$, $s = 1$):

$$
\rho_g = \frac{g_s^2 M}{4\pi r^2} e^{-m_g r}, \quad \mathbf{F} \propto -\frac{g_s^2 M m}{r^3} e^{-m_g r}, \quad g_s^2 \approx 1, \quad m_g \approx 100 \, \text{MeV}/c^2, \quad \kappa \propto g_s^2
$$

  - **Weak force** (W/Z, $f \approx 10^{25} \, \text{Hz}$, $s = 1$):

$$
\rho_W = \frac{g_W^2 M}{4\pi r^2} e^{-M_W r}, \quad \mathbf{F} \propto -\left( \frac{g_W^2 M m}{r^3} + \frac{g_W^2 M m M_W}{r^2} \right) e^{-M_W r}, \quad g_W^2 \approx 0.033, \quad M_W \approx 80 \, \text{GeV}/c^2, \quad \kappa \propto g_W^2
$$

  - **Gravity/Dark matter** (gravitons, $f \approx 10 - 10^3 \, \text{Hz}$, $s = 2$):

$$
\rho = \frac{\sqrt{2\pi G_{\text{eff}}} M}{4\pi r^2}, \quad \mathbf{F} = -\frac{G_{\text{eff}} M m}{r^2}, \quad G_{\text{eff}} \approx 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}, \quad \kappa \propto G_{\text{eff}}
$$

    Dark matter: $G_{\text{eff}} \propto \varepsilon \approx 10^{-15}$ or $g_a \gamma \approx 10^{-12} \, \text{GeV}^{-1}$.
  - **Dark energy** (very low frequency, $\nabla \rho_\phi \approx 0$):
    
$$
\rho_\phi \approx 10^{-120} \, \text{J/m}^3, \quad \mathbf{F} \approx 0, \quad p_\phi \approx -\rho_\phi, \quad \kappa \approx 0
$$

**Physical Meaning**:

- Force $\mathbf{F} = -\kappa m \nabla \rho$ reflects homogenization driven by density gradients, unifying the four interactions.
- Frequency $f$ determines spin $s$ and $\kappa(f, s)$, with high frequencies corresponding to short-range forces (strong/weak) and low frequencies to long-range forces (gravity).

---

## 3. Dynamic Equations

The dynamic equations are extended to multi-frequency form, describing the evolution of each frequency component $\rho_f$:

$$
\frac{\partial \rho_f}{\partial t} = k_f \rho_f^m - D_f \nabla^2 \rho_f - \nabla \cdot (\rho_f \mathbf{v}_f) + S_f
$$

- Total density evolution:

$$
\rho = \sum_f \rho_f, \quad \frac{\partial \rho}{\partial t} = \sum_f \frac{\partial \rho_f}{\partial t}
$$
  
- Parameters:
  - $k_f$: Positive feedback coefficient, frequency-dependent, e.g.:
    - Strong force: $k_f \propto g_s^2 \approx 1$ ($f \approx 10^{23} - 10^{24} \, \text{Hz}$).
    - Weak force: $k_f \propto g_W^2 \approx 0.033$ ($f \approx 10^{25} \, \text{Hz}$).
    - Gravity: $k_f \propto G_{\text{eff}}$ ($f \approx 10 - 10^3 \, \text{Hz}$).
    - Dark energy: $k_f \approx 0$.
  - $D_f$: Diffusion coefficient, high $D_f$ for high frequencies (electromagnetic/strong forces, fast diffusion), low $D_f$ for low frequencies (gravity, persistent).
  - $\mathbf{v}_f \propto -\nabla \rho_f$: Flow velocity, consistent with force $\mathbf{F} = -\kappa m \nabla \rho_f$, driving matter toward high-density regions.
  - $S_f \propto \hbar \nabla^4 \rho_f$: Quantum fluctuations, significant at high frequencies (e.g., QGP), weak at low frequencies.
  - $m$: Nonlinear exponent, typically $m = 2$ (similar to Jeans instability).
- Inter-frequency interactions:
  - Cross terms $k_{f1,f2} \rho_{f1} \rho_{f2}$ represent coupling between different frequency $\rho_f$, e.g., interaction between high-frequency photons and low-frequency gravitons.
- Physical meaning:
  - Positive feedback $k_f \rho_f^m$: Drives density clustering (e.g., quark confinement, galaxy formation).
  - Diffusion $-D_f \nabla^2 \rho_f$: Drives energy minimization (e.g., cosmic expansion).
  - Fluid term $-\nabla \cdot (\rho_f \mathbf{v}_f)$: Drives matter flow, consistent with $\mathbf{F} = -\kappa m \nabla \rho_f$.
  - Quantum fluctuations $S_f$: Trigger density perturbations (e.g., seeds during inflation).

**Connection to Force**:

- The fluid term $-\nabla \cdot (\rho_f \mathbf{v}_f)$ (with $\mathbf{v}_f \propto -\nabla \rho_f$) corresponds to the force $\mathbf{F} = -\kappa m \nabla \rho_f$, reflecting matter motion driven by density gradients.

---

## 4. Lagrangian

The Lagrangian integrates all field variables, including free field and interaction terms, considering frequency $f$ and spin $s$:

$$
\begin{aligned}
L = & \sum_f \left[ \frac{1}{2} (\partial_\mu \rho_f) (\partial^\mu \rho_f) - \frac{1}{2} m^2(f) \rho_f^2 \right] + \sum_{f,s} \overline{\psi}_m(f, s) (i \gamma^\mu \partial_\mu - m(f)) \psi_m(f, s) \\
& + \sum_f \frac{1}{4} F_{\mu\nu}(f) F^{\mu\nu}(f) + \sum_f \frac{1}{2} (\partial_\mu h^{\mu\nu}(f)) (\partial^\rho h_{\mu\nu}(f)) + (\partial_\mu \phi_H(f)) (\partial^\mu \phi_H(f)) - V(\phi_H(f)) + L_{\text{int}}
\end{aligned}
$$

- **Free field terms**:
  - $\rho_f$ (scalar field, spin 0): Describes energy quantum number density.
  - $\psi_m(f, s)$ (spinor field, spin 1/2): Describes fermions (e.g., electrons, quarks).
  - $A^\mu(f)$ (vector field, spin 1): Describes photons, gluons, W/Z bosons.
  - $h^{\mu\nu}(f)$ (tensor field, spin 2): Describes gravitons.
  - $\phi_H(f)$ (scalar field, spin 0): Higgs field, confers mass.
- **Interaction term**:

$$
L_{\text{int}} = \sum_{f,s} g(f, s) \cdot \rho_f \cdot \left[ \overline{\psi}_m(f, s) \psi_m(f, s) + A_\mu(f) A^\mu(f) + h_{\mu\nu}(f) h^{\mu\nu}(f) \right] \cdot \phi_H(f)
$$

  - $g(f, s) = \frac{A(s)}{(f - f_0)^2 + \gamma(s)^2}$: Lorentzian form, frequency matching drives same-frequency resonance.
  - $A(s)$: Spin-dependent coupling strength (electromagnetic: $\alpha \approx 1/137$, strong: $\alpha_s \approx 1$, weak: $\alpha_W \approx 0.033$, gravity: $G_{\text{eff}}$).
  - $\gamma(s)$: Resonance width, depends on spin and particle lifetime.
- **Dark energy**:
  - As a uniform background field, $\rho_\phi \approx 10^{-120} \, \text{J/m}^3$, can be included via potential $V(\rho_\phi) \approx -\rho_\phi$.

---

## 5. Field Equations

Derived via variational principle ($\delta S = \delta \int L \, d^4x = 0$):

- **Energy quantum number density**:

$$
\Box \rho_f + m^2(f) \rho_f = g(f, s) \cdot \left[ \overline{\psi}_m(f, s) \psi_m(f, s) + A_\mu(f) A^\mu(f) + h_{\mu\nu}(f) h^{\mu\nu}(f) \right] \cdot \phi_H(f)
$$

- **Mass quantum field** (spin 1/2):

$$
(i \gamma^\mu \partial_\mu - m(f)) \psi_m(f, s) = g(f, s) \cdot \sum_f \rho_f \cdot \phi_H(f) \cdot \psi_m(f, s)
$$

- **Vector field** (spin 1):

$$
\partial_\mu F^{\mu\nu}(f) = g(f, s) \cdot \sum_f \rho_f \cdot \phi_H(f) \cdot A^\nu(f)
$$

- **Tensor field** (spin 2):

$$
\Box h^{\mu\nu}(f) = g(f, s) \cdot \sum_f \rho_f \cdot \phi_H(f) \cdot h^{\mu\nu}(f)
$$
  
- **Higgs field** (spin 0):

$$
\Box \phi_H(f) + \frac{\partial V(\phi_H(f))}{\partial \phi_H(f)} = \sum_{f,s} g(f, s) \cdot \rho_f \cdot \left[ \overline{\psi}_m(f, s) \psi_m(f, s) + A_\mu(f) A^\mu(f) + h_{\mu\nu}(f) h^{\mu\nu}(f) \right]
$$

**Correspondence with Dynamic Equations**:

- The dynamic equation $\frac{\partial \rho_f}{\partial t} = k_f \rho_f^m - D_f \nabla^2 \rho_f - \nabla \cdot (\rho_f \mathbf{v}_f) + S_f$ is the non-relativistic form of the field equation $\Box \rho_f + m^2(f) \rho_f = \text{source term}$:
  - Positive feedback $k_f \rho_f^m \sim g(f, s) \cdot \text{source term}$.
  - Diffusion $-D_f \nabla^2 \rho_f \sim \Box \rho_f$.
  - Fluid term $-\nabla \cdot (\rho_f \mathbf{v}_f) \sim \mathbf{F} = -\kappa m \nabla \rho_f$.
  - Quantum fluctuations $S_f \sim \hbar \nabla^4 \rho_f$.

---

## 6. Unification of the Four Fundamental Forces

- **Electromagnetic force** (photons, $f \approx 10^6 - 10^{20} \, \text{Hz}$, $s = 1$):
  - $\rho_f \propto \frac{\alpha M}{4\pi r^2}$, $\mathbf{F} \propto -\frac{\alpha M m}{r^3}$, $\kappa \propto \alpha \approx 1/137$.
  - Vector field $A^\mu(f)$, operator $\partial_\mu F^{\mu\nu}$.
- **Weak force** (W/Z, $f \approx 10^{25} \, \text{Hz}$, $s = 1$):
  - $\rho_W = \frac{g_W^2 M}{4\pi r^2} e^{-M_W r}$, $\mathbf{F} \propto -\left( \frac{g_W^2 M m}{r^3} + \frac{g_W^2 M m M_W}{r^2} \right) e^{-M_W r}$, $\kappa \propto g_W^2 \approx 0.033$.
  - Vector field $A^\mu(f)$, operator $\partial_\mu F^{\mu\nu}$.
- **Strong force** (gluons, $f \approx 10^{23} - 10^{24} \, \text{Hz}$, $s = 1$):
  - $\rho_g = \frac{g_s^2 M}{4\pi r^2} e^{-m_g r}$, $\mathbf{F} \propto -\frac{g_s^2 M m}{r^3} e^{-m_g r}$, $\kappa \propto g_s^2 \approx 1$.
  - Vector field $A^\mu(f)$, operator $\partial_\mu F^{\mu\nu}$.
- **Gravity/Dark matter** (gravitons, $f \approx 10 - 10^3 \, \text{Hz}$, $s = 2$):
  - $\rho = \frac{\sqrt{2\pi G_{\text{eff}}} M}{4\pi r^2}$, $\mathbf{F} = -\frac{G_{\text{eff}} M m}{r^2}$, $\kappa \propto G_{\text{eff}}$.
  - Tensor field $h^{\mu\nu}(f)$, operator $\Box h^{\mu\nu}$.
- **Dark energy** (very low frequency, $\nabla \rho_\phi \approx 0$):
  - $\rho_\phi \approx 10^{-120} \, \text{J/m}^3$, $\mathbf{F} \approx 0$, diffusion term $D_f \nabla^2 \rho_f$ drives expansion.

---

## 7. Bridging Micro and Macro Scales

- **Microscopic** (quantum mechanics):
  - High-frequency $\rho_f$ ($f \approx 10^{23} - 10^{25} \, \text{Hz}$, $s = 1, 1/2$) drives short-range forces (strong, weak), e.g., quark confinement, β-decay.
  - Same-frequency resonance via $g(f, s)$ enables energy transfer.
- **Macroscopic** (general relativity):
  - Low-frequency $\rho_f$ ($f \approx 10 - 10^3 \, \text{Hz}$, $s = 2$) drives long-range forces (gravity), e.g., galaxy formation.
  - Dark energy ($\nabla \rho_\phi \approx 0$) dominates expansion via large $D_f$.
- **Higgs field** ($f \approx 3.02 \times 10^{25} \, \text{Hz}$, $s = 0$):
  - Connects energy quanta and mass quanta via $m(f) = g_H \phi_H(f)$, operator $\Box \phi_H(f)$.

---

## 8. Philosophical and Scientific Insights

- **Planck's formula**: $E = hf$ unifies energy quanta and mass quanta, $\rho_f \cdot hf$ reflects energy density.
- **Force and density field**: $\mathbf{F} = -\kappa m \nabla \rho$ unifies the four forces, frequency $f$ determines spin and operators.
- **Spacetime definition**: Time ($\frac{\partial \rho}{\partial t}$) and space ($\rho(\mathbf{r})$) are based on the density field, compatible with Big Bang theory.
- **Same-frequency resonance**: $g(f, s)$ drives interactions, frequency matching determines efficiency.
