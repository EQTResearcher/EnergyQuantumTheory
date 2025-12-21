# Energy Quantum Theory (EQT) - Early Galaxy Formation Simulation

This repository contains the complete code for the numerical simulations presented in the paper:

**"Rapid Formation of Mature Galaxies at z > 13: A High-Frequency Cascade Model from Planck-Scale Origins"**

The code implements a novel cosmological model based on high-frequency energy quanta events evolving via energy-conserving difference-frequency cascades. It reproduces the rapid formation of massive, ordered disk galaxies in <300 Myr, consistent with JWST 2025 observations.

## Requirements

Python 3.10+  
numpy, scipy, networkx, matplotlib, numba

Install via:
```bash
pip install numpy scipy networkx matplotlib numba
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/EQTResearcher/EnergyQuantumTheory.git
cd EnergyQuantumTheory
```

2. Run the benchmark simulation:
```bash
python main.py
```

This will reproduce:
- Initial 10,000 high-frequency events
- Evolution to ~16,000 events in 150 steps
- Early galaxy formation diagnostics (high-density cores, disk-like structures)
- Energy conservation validation

Expected runtime: 4–6 hours on a standard workstation (64-core CPU).

## Output

Console output includes:
- Event count and average frequency per 20 steps
- High-density core count
- Final energy conservation check

Visualization and detailed analysis can be enabled by extending `analysis.py`.

## Citation

If you use this code, please cite our paper (in press).

## License

MIT License - free to use, modify, and distribute.

Contact: lkshbj@sina.com

Last updated: December 2025
```
