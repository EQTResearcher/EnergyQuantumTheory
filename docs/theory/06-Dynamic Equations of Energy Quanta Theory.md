# Dynamic Equations of Energy Quanta Theory: Framework, Mechanism, and Unifying Significance

## Abstract

The core of Energy Quanta Theory (EQT) lies in the dynamic equations describing the evolution of the energy quanta density field. Through a set of competing terms, these equations uniformly characterize the physical essence of phenomena ranging from microscopic particle aggregation to macroscopic cosmic structure formation. This paper aims to clarify the concepts, mathematical forms, physical dimensions, and profound physical significance of these dynamic equations, and to demonstrate their potential as a framework for unifying interactions and the origin of complexity.

## 1. General Form and Concepts of the Dynamic Equations

The evolution of the energy quanta density field, $ρ(\mathbf{r}, t)$, is governed by the following nonlinear partial differential equation:

$$
\frac{\partial \rho}{\partial t} = k \rho^m - D \nabla^2 \rho - \nabla \cdot (\rho \mathbf{v}) + S
$$


**Conceptual Overview**:
This equation describes an open, far-from-equilibrium dissipative system. Within it:

- $ρ(\mathbf{r}, t)$ is the energy quanta density field, with dimensions of `[Energy]/[Volume]` (recommended unit: `J/m³`). It is inherently multi-frequency, i.e., $ρ = \sum_f \rho_f$ , representing the superposition of sub-density fields for energy quanta of different frequencies `f` (e.g., photons, gluons, gravitons).
- The four terms on the right-hand side represent the fundamental physical processes of positive feedback, diffusion, advection/flow, and perturbation/source, respectively.

## 2. Detailed Physical Interpretation and Dimensional Analysis of the Terms

### 2.1 Positive Feedback Term: $k \rho^m$

- **Physical Concept**: This term represents the non-linear autocatalytic mechanism of energy quanta interactions. High-density regions further attract more energy quanta or mass quanta through energy quanta exchange, forming a "rich-get-richer" aggregation positive feedback. It is the core engine of structure formation.
- **Mathematics and Dimensions**:
  - Typically, `m = 2` is chosen to reflect two-particle interaction rates.
  - Dimensions: $[k \rho^m] = [k] [\rho]^2$ . Since $[\partial \rho / \partial t] = [\text{Energy}]/([\text{Time}][\text{Volume}])$ and $[\rho] = [\text{Energy}]/[\text{Volume}]$ , it follows that $[k] = [\text{Volume}]/([\text{Time}][\text{Energy}])$ or equivalently $[\text{Time}]^{-1} [\text{Density}]^{-1}$ .
- **Frequency Dependence and Resonance Mechanism**:
  The positive feedback strength is a function of frequency matching: $k(\Delta f) = k_0 \cdot g(\Delta f)$ , where $g(\Delta f)$ is the coupling function, often expressed in Lorentzian form:

$$
g(f, f_0) = \frac{A}{(f - f_0)^2 + \gamma^2}
$$

Here, `f_0` is the characteristic frequency of the particle, and $\gamma$ is the resonance width. During co-frequency resonance ( $f \approx f_0$ ), the feedback efficiency is highest, explaining the selectivity and strength differences between different interactions (electromagnetic, strong, weak).

### 2.2 Diffusion Term: $- D \nabla^2 \rho$

- **Physical Concept**: This term represents the homogenizing tendency due to the random motion of energy quanta (e.g., propagation at light speed). It counteracts infinite clustering caused by positive feedback, representing the system's tendency towards higher entropy and uniformity, playing a stabilizing and smoothing role.
- **Mathematics and Dimensions**:
- The Laplace operator $\nabla^2$ measures the "curvature" of the density field; it is negative at peaks, promoting density decrease.
- Dimensions: $[D \nabla^2 \rho] = [D] [\rho]/[\text{Length}]^2$ . Therefore, $[D] = [\text{Length}]^2/[\text{Time}]$ (e.g., $m²/s$ ).
- **Significance**: The competition with the positive feedback term determines the characteristic scale of the formed structures. A large `D` value suppresses the formation of small-scale structures.

### 2.3 Advection/Flow Term: $- \nabla \cdot (\rho \mathbf{v})$

- **Physical Concept**: This term describes the bulk transport of the energy quanta density field with the velocity field $\mathbf{v}$ . In EQT, the velocity field is driven by the density gradient: $\mathbf{v} \propto -\nabla \rho$ , i.e., flow towards higher density regions. This is the macroscopic manifestation of the force $\mathbf{F} \propto -\nabla \rho$ in a continuous medium.
- **Mathematics and Dimensions**:
- Expanded, it becomes $-\mathbf{v} \cdot \nabla \rho - \rho \nabla \cdot \mathbf{v}$ .
- Substituting $\mathbf{v} = -\alpha \nabla \rho$ , this term becomes $\alpha (\nabla \rho)^2 + \alpha \rho \nabla^2 \rho$ . The $(\nabla \rho)^2$ term provides additional positive feedback, further amplifying the gradient.
- Dimensions: All components are consistent with $[\partial \rho / \partial t]$ .
- **Significance**: This term links the density gradient to the physical force, driving the motion of mass quanta.

### 2.4 Perturbation/Source Term: `+ S`

- **Physical Concept**: This term is the origin of all complexity. It represents intrinsic or extrinsic fluctuations and perturbations that break the system's homogeneity. Without `S`, the system might remain uniform; a tiny `S` acts as a "seed" that can be exponentially amplified by the positive feedback term, eventually forming macroscopic structures.
- **Mathematics and Dimensions**:
- `S` can be a constant, random noise $\eta(\mathbf{r}, t)$ , or a space-time dependent function.
- Dimensions: $[S] = [\text{Energy}]/([\text{Time}][\text{Volume}])$ .
- **Sources and Significance**:
- **Natural Sources**: Quantum fluctuations in the early universe are the primary source of primordial perturbations, with an amplitude of approximately $10^{-5}$ amplified by inflation, becoming the seeds for today's galaxy cluster structures. Temperature fluctuations are also common forms of `S`.
- **Anthropogenic Sources**: All scientific experiments, from particle colliders to laser excitations, essentially involve introducing a specific `S` under controlled conditions to trigger and observe the system's dynamic response, thereby simulating natural processes.

## 3. Unified Picture and Significance under the Multi-Frequency Framework

Extending the dynamic equation to a multi-frequency form is key to EQT's unification of the four fundamental interactions:

$$
\frac{\partial \rho_f}{\partial t} = k_f \rho_f^m - D_f \nabla^2 \rho_f - \nabla \cdot (\rho_f \mathbf{v}_f) + S_f
$$



- **Unification of Interactions**:
  - **Electromagnetic Force**: Dominated by high-frequency photon fields $ρ_f$ ( $f \sim 10^{14} - 10^{25} Hz$ ), where $k_f$ resonates most strongly in the visible light frequency band.
  - **Strong Force**: Dominated by very high-frequency gluon fields $ρ_f$ , its short-range nature described by Yukawa attenuation (implicit in $k_f$ or $D_f$ ).
  - **Weak Force**: Dominated by W/Z boson fields $ρ_f$ , its extremely short range arising from the sharp attenuation of $k_f$ outside the resonance band due to the large $M_W$ .
  - **Gravitational Force**: Dominated by very low-frequency graviton fields $ρ_f$ ( $f < 10^3 Hz$ ), where its small $D_f$ allows perturbations to persist and aggregate on large scales.
- **Explaining Dark Matter and Dark Energy**:
  - **Dark Matter**: Can be interpreted as an energy quanta field existing in the mid-frequency band (e.g., $10^3 - 10^{10} Hz$ ). Its resonance with both ordinary matter (high-frequency electromagnetic coupling) and gravity (low-frequency coupling) is weak (i.e., $g(\Delta f)$ is very small), thus appearing "invisible" yet perceptible through gravitational effects (advection term).
  - **Dark Energy**: Corresponds to a nearly uniform, zero-gradient, very low-frequency background field $ρ_\phi$ . Since its $\nabla \rho \approx 0$ , it does not produce a directional force, but its enormous energy density drives the accelerated expansion of the universe through terms like the diffusion term in the equation.

## Summary and Outlook

The dynamic equations of Energy Quanta Theory provide an exceptionally powerful and unifying framework. They tightly couple the mechanism of force ( $\mathbf{F} = -\kappa m \nabla \rho$ ) with field evolution (dynamic equations), revealing the common physical essence from quantum fluctuations to galaxy formation: namely, the emergence of complexity across different scales, driven by the energy minimization principle, through positive feedback, diffusion, advection, and perturbation of multi-frequency energy quanta fields. This framework not only deepens our understanding of fundamental interactions but also opens up a new and promising path for exploring frontier issues such as quantum gravity and the nature of dark matter.

## Frequency Data Table

For consistency with prior submissions, the following table summarizes the frequency characteristics of key particles across the spectrum, as referenced in the context of EQT:

| Particle        | Frequency (Hz)          | Region               |
|-----------------|-------------------------|----------------------|
| Graviton (hypoth.) | `10` to `10³`         | Low-Frequency        |
| Visible Light Photon | `10¹⁴` to `10¹⁵`    | Low-Frequency        |
| Neutrino        | `~10¹⁵` to `10¹⁶`      | Low-Frequency        |
| Electron        | `~1.24 × 10²⁰`         | Transition           |
| Up Quark        | `~5.32 × 10²⁰`         | Transition           |
| Down Quark      | `~1.14 × 10²¹`         | Transition           |
| Muon            | `~2.55 × 10²²`         | Transition           |
| Strange Quark   | `~2.25 × 10²²`         | Transition           |
| Charm Quark     | `~3.08 × 10²³`         | Transition           |
| Tau Lepton      | `~4.30 × 10²³`         | Transition           |
| Bottom Quark    | `~1.01 × 10²⁴`         | Transition           |
| Gluon           | `~10²³` to `10²⁴`      | Transition           |
| High-Energy Photon | `~10²²` to `10²⁵`   | Transition           |
| W Boson         | `~1.94 × 10²⁵`         | Mass Quanta          |
| Z Boson         | `~2.20 × 10²⁵`         | Mass Quanta          |
| Higgs Boson     | `~3.02 × 10²⁵`         | Mass Quanta          |
| Top Quark       | `~4.18 × 10²⁵`         | Mass Quanta          |

