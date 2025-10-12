# EQT Data Warehouse Usage and Management Guide

## 1. Overview

This guide explains the structure of the EQT project data warehouse, the data upload process, and collaborative management rules. It ensures dataset uniformity, traceability, and community collaboration efficiency. The data directory stores public experimental or observational data (e.g., LIGO gravitational waves, LHC particle data, CMB power spectra) to support EQT's frequency field theory research.

## 2. Data Upload Process

1. **Create a Subdirectory**: Create a subdirectory following the naming convention `[Data_Type]_[Experiment/Project]_[Brief_Description]` (e.g., `GravitationalWave_LIGO_2015-2019`).
2. **Upload Data Files**: Place files (e.g., `.csv`, `.h5`, `.fits`) into the subdirectory, ensuring standard formats.
3. **Write README.md**: Refer to `template.md` and fill in dataset information (overview, source, format, etc.).
4. **Generate metadata.json**: Refer to `template.json` and complete the metadata, ensuring all fields are filled.
5. **Submit a Pull Request**: Submit the dataset and documentation via GitHub for community review before merging.

## 3. Community Collaboration

- **Review Mechanism**: A core team of 5–10 members reviews data integrity, source legitimacy, and relevance to EQT.
- **Version Control**: Use Git to track data and documentation updates, recording contributor information.
- **Discussion Channel**: Discuss data-related issues in the `#data` channel on Discord.

## 4. AI Tool Support

- **Grok Integration**: Grok can parse `metadata.json` to automatically extract fields (e.g., frequency, time) and generate analysis code or visualizations. For example:
  ```python
  import h5py
  import matplotlib.pyplot as plt
  with h5py.File("data/GravitationalWave_LIGO_2015-2019/GW150914_strain.h5", "r") as f:
      freq = f["frequency"][:]
      plt.hist(freq, bins=50, color="#2196F3")
      plt.xlabel("Frequency (Hz)")
      plt.ylabel("Count")
      plt.title("LIGO GW150914 Frequency Distribution")
      plt.show()
  ```
- **Automated Checks**: AI tools (like Grok) can validate the completeness of fields in `metadata.json` and alert about missing information.

## 5. Maintenance & Updates

- **Regular Checks**: Check data link validity quarterly and update broken URLs.
- **Contribution Incentives**: Recognize outstanding data contributors on platforms like X to enhance community engagement.
- **Backups**: Back up data to cloud storage (e.g., Google Drive, Zenodo) to mitigate GitHub storage limitations.

## 6. Contact

- **Community Discussion**: Discord channel `#EQT-data`.
