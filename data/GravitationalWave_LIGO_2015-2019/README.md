# Dataset Name: GravitationalWave_LIGO_2015-2019

## 1. Dataset Overview

- **Description**: LIGO gravitational wave detection data containing time series of binary black hole mergers and neutron star mergers from 2015-2019, used to study frequency characteristics of gravitational wave signals.
- **Data Type**: Observational Data
- **Research Relevance**: Validate EQT theory's frequency sequencing ($35-250 \, \text{Hz}$) and graviton behavior in the dynamic equation $\frac{\partial \rho}{\partial t} = k \rho^2 - D \nabla^2 \rho - \nabla \cdot (\rho \mathbf{v}) + S$.
- **Time Range**: 2015-09-01 to 2019-12-31
- **Data Volume**: 2 `.h5` files, approximately 500 MB total

## 2. Data Source

- **Institution/Project**: LIGO Scientific Collaboration
- **Public Link**: [https://www.gw-openscience.org/GWTC-1/](https://www.gw-openscience.org/GWTC-1/)
- **License**: CC0 1.0 Universal
- **Citation Requirement**:
  ```bibtex
  @article{LIGO_GWTC1,
    title = {GWTC-1: A Gravitational-Wave Transient Catalog of Compact Binary Mergers Observed by LIGO and Virgo during the First and Second Observing Runs},
    author = {LIGO Scientific Collaboration and Virgo Collaboration},
    journal = {Physical Review X},
    volume = {9},
    number = {3},
    pages = {031040},
    year = {2019},
    doi = {10.1103/PhysRevX.9.031040}
  }
  ```

## 3. Data Format & Content

- **File List**:
  - `GW150914_strain.h5`: Time series of the first detected binary black hole merger (GW150914) in 2015.
  - `GW170817_strain.h5`: Time series of the binary neutron star merger (GW170817) in 2017.
- **Format**: HDF5
- **Field Description**:
  - `time`: Timestamp (seconds)
  - `strain`: Gravitational wave strain (dimensionless)
  - `frequency`: Signal frequency (Hz)
- **Data Structure**: 1D time series, sampling rate 4096 Hz
- **Units**: Time (s), Strain (dimensionless), Frequency (Hz)
- **Preprocessing Notes**: Noise below 20 Hz and above 1000 Hz has been removed, preserving valid signals in the 35-250 Hz range.

## 4. Usage Instructions

- **Recommended Tools**: Python (`h5py`, `pandas`), GWpy
- **Example Code**:
  ```python
  import h5py
  import matplotlib.pyplot as plt
  
  with h5py.File("data/GravitationalWave_LIGO_2015-2019/GW150914_strain.h5", "r") as f:
      time = f["time"][:]
      strain = f["strain"][:]
      freq = f["frequency"][:]
  
  plt.plot(time, strain, color="#2196F3")
  plt.xlabel("Time (s)")
  plt.ylabel("Strain")
  plt.title("GW150914 Gravitational Wave Signal")
  plt.show()
  
  # Frequency distribution analysis
  plt.hist(freq, bins=50, color="#2196F3")
  plt.xlabel("Frequency (Hz)")
  plt.ylabel("Count")
  plt.title("GW150914 Frequency Distribution")
  plt.show()
  ```
- **EQT Analysis Suggestions**:
  - Extract 35-250 Hz frequency distribution to validate EQT's predicted graviton frequency range ($\nu \sim 10^2 \, \text{Hz}$).
  - Simulate gravitational wave signals using dynamic equations, comparing contributions from the positive feedback term ($k \rho^2$).

## 5. Contribution & Updates

- **Contributor**: [@EQTResearcher](https://github.com/EQTResearcher)
- **Update Log**:
  - 2025-10-12: Initial upload of GW150914 and GW170817 data.
- **How to Contribute**: Fork repository, add new data or improve documentation, submit Pull Request.
- **Contact**: Discord channel `#EQT-data`

## 6. Related Resources

- **References**: EQT monograph "The Nature of Gravity", Chapter 3 "Frequency Field and Gravitational Waves".
- **External Links**: [https://gwosc.org](https://gwosc.org)
- **Community Discussion**: [https://x.com/EQTResearch/status/123456789](https://x.com/EQTResearch/status/123456789)

## 7. Notes & Cautions

- Data is for academic research purposes only.
- High-frequency noise (> 1000 Hz) may affect analysis; additional filtering is recommended.
- GW170817 data contains multiple detector signals; LIGO-Hanford and LIGO-Livingston data should be processed separately.
