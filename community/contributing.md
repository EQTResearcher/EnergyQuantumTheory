# EQT-Research Contribution Guide

## Welcome!

Welcome to the Energy Quantum Theory community! This is an openly collaborative physics research project driven by global volunteers. Whether you are an experienced physicist, a programmer, or a curious student, there are ways for you to participate. This guide will help you get started and become a member of our community.

## Our Collaboration Philosophy

- **Open**: All research processes, code, data, and discussions are open to community members.
- **Collaborative**: We integrate global intelligence by decomposing tasks and working asynchronously.
- **AI-Augmented**: We actively use AI tools to enhance efficiency but maintain critical thinking; all outputs require human review.
- **Modular Innovation**: We encourage building upon the work of others and hope your work will become a foundation for future contributions.

## Step 1: Integrate into the Community

1. **Explore & Understand**
   - **First Steps**: Please read the project `README.md` and `docs/theory/fundamentals.md` to understand EQT's basic framework and this project's goals.
   - **Learn by Observation**: Browse existing Issues and Pull Requests to get a feel for the community's collaboration style.
2. **Join the Conversation**
   - **Core Discussion Hub**: Join our Discord server and introduce yourself in the `#introduce-yourself` channel.
   - **Asynchronous Collaboration Center**: Raise questions or suggestions in GitHub Issues.

## Step 2: Choose Your Contribution Path

We have designed diverse tasks for members with different backgrounds. Please choose your entry point:

### Path 1: Theoretical Exploration

- **Beginner**: Proofread formulas in theoretical documents, translate documentation, add intuitive explanations for complex concepts.
- **Intermediate**: Derive solutions for equations in specific scenarios (e.g., density distribution under a spherical symmetric potential) under guidance.
- **Expert**: Develop new theoretical modules, or deeply connect EQT with specific physical phenomena (e.g., dark matter halos, CMB fluctuations).

### Path 2: Code & Simulation

- **Beginner**: Fix code warnings, write unit tests, improve docstrings.
- **Intermediate**: Implement numerical solutions for theoretical formulas, or optimize the computational performance of existing simulations.
- **Expert**: Build new numerical simulators (e.g., for galaxy formation, particle interactions), or develop specialized EQT computation libraries.

### Path 3: Data & Experiment

- **Beginner**: Organize, clean, and label public scientific datasets.
- **Intermediate**: Perform reproducible analysis of public data (e.g., from LIGO, Planck) using the EQT framework.
- **Expert**: Design tabletop-level verification experiment protocols, or propose new ideas for analyzing data from large-scale experiments (e.g., LHC).

### Path 4: Community & Outreach

- **Beginner**: Assist in managing community channels, organize meeting notes.
- **Intermediate**: Create popular science content, design visualizations, manage social media accounts.
- **Expert**: Organize online/offline seminars, coordinate cross-team projects.

**Unsure where to start?**  
Check the `community/good-first-issues.md` file, which lists tasks specifically curated for newcomers with clear steps.

## Step 3: Start Contributing

Once you've chosen a task, please follow this workflow:

1. **Claim a Task**
   - Comment on the relevant GitHub Issue to state that you are starting work on it, preventing duplicate efforts.
2. **Set Up Your Development Environment**
   ```bash
   # Fork and clone the repository
   git clone https://github.com/YOUR-USERNAME/EnergyQuantumTheory.git
   cd EnergyQuantumTheory
   # Create your feature branch from main
   git checkout -b feature/your-descriptive-branch-name
   ```
3. **Do Your Work**
   - **Theoretical Documents**: Work in the `docs/` directory. We recommend using KaTeX for rendering mathematical formulas. For complex formulas, you can use AI tools to generate drafts, but manual verification for correctness is mandatory. Example:
     ```markdown
     The energy quanta density field is defined as:
     $$
     \rho(\mathbf{r}, t) = \sum_f \rho_f(\mathbf{r}, t)
     $$
     ```
   - **Code**: Work in the `code/` directory. Please write clear docstrings and simple usage examples for your code.
   - **Data**: Work in the `data/` directory. Ensure data sources are clear and provide a descriptive `README.md`.
4. **AI-Assistance Best Practices**
   - **Use Cases**: Generating code skeletons, debugging errors, translating documentation, visualization inspiration, literature summarization.
   - **Principles**:
     - **Prompts Must Be Precise**: Provide the AI with clear context and requirements.
     - **Output Must Be Reviewed**: AI can generate plausible but incorrect content. You are the first line of responsibility for its output.
     - **Acknowledge AI Assistance**: In your commit messages or PR description, acknowledge significant AI assistance as a matter of scientific rigor.
5. **Submit Your Contribution**
   - Ensure your code or documentation includes the correct license header.
   - Commit your changes:
     ```bash
     git add .
     git commit -m "Descriptive Message: Clearly state what this commit does"
     git push origin feature/your-descriptive-branch-name
     ```
   - Open a Pull Request: On GitHub, open a Pull Request from your branch to the main repository's `main` branch. Please use our PR template to clearly describe your changes, motivation, and any points requiring reviewer attention.

## Step 4: Review & Merge

- **Review Process**: Maintainers and other community members will review your PR and suggest improvements. This is a process for mutual learning and enhancing quality—please maintain an open mind.
- **Interaction & Revisions**: Please respond to review comments promptly. The discussion and revision process is a valuable contribution in itself.
- **Merge**: Once your PR is approved, a maintainer will merge it into the main branch. Congratulations! Your contribution is now part of the project.

## Intellectual Property & Licensing

- **Code**: Licensed under the MIT License. Please add the following header to code files:
  ```python
  # Copyright (c) 2025 Kaisheng Li & Longji Li. Licensed under the MIT License.
  ```
- **Documentation & Theory**: Licensed under the CC BY-SA 4.0 license. Please add the following to the end or beginning of documents:
  ```
  Copyright (c) 2025 Kaisheng Li & Longji Li. Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
  ```
- Submitting a PR constitutes your agreement to license your contribution under these terms.

## Getting Help

- 💬 **Technical Discussions**: Use the relevant GitHub Issue.
- 🗣️ **Instant Communication**: Use the appropriate channels on Discord.
- 📚 **Consult Documentation**: The project documentation is your best first resource.

---

We look forward to your contributions!

Every Pull Request, every in-depth discussion in an Issue, helps collectively advance humanity's understanding of the physical world. Thank you for joining us on this exciting journey!
