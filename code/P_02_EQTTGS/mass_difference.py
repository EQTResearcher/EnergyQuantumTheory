#"""
#Proton-neutron mass difference from frequency difference in EQT
#"""

import numpy as np

# Fundamental constants
h = 6.62607015e-34    # J·s
c = 299792458         # m/s
eV_to_J = 1.602176634e-19

# Experimental mass difference
delta_m_exp_MeV = 1.293
delta_m_exp_J = delta_m_exp_MeV * 1e6 * eV_to_J

# Calculate required frequency difference
delta_f = delta_m_exp_J / h  # Hz

# Quark frequencies (derived from current quark masses)
m_u_MeV = 2.2
m_d_MeV = 4.7
f_u = (m_u_MeV * 1e6 * eV_to_J) / h
f_d = (m_d_MeV * 1e6 * eV_to_J) / h

# Baryon masses in EQT (Y-type model)
# Proton: center + 2u + 1d
# Neutron: center + 1u + 2d
# Mass difference comes from (2d + u) - (2u + d) = d - u

mass_diff_from_quarks = (f_d - f_u) * h / (1e6 * eV_to_J)  # MeV

# Include small center frequency shift (estimated)
delta_f_center = 0.2 * delta_f  # 20% contribution from center shift
total_delta_f = (f_d - f_u) + delta_f_center
total_mass_diff = total_delta_f * h / (1e6 * eV_to_J)

print("=== Proton-Neutron Mass Difference in EQT ===")
print(f"Experimental value: {delta_m_exp_MeV:.3f} MeV")
print()
print("From quark frequency difference alone:")
print(f"  f_d - f_u = {f_d - f_u:.3e} Hz")
print(f"  Mass difference = {mass_diff_from_quarks:.3f} MeV")
print()
print("Including center frequency shift:")
print(f"  Total Δf = {total_delta_f:.3e} Hz")
print(f"  Total mass difference = {total_mass_diff:.3f} MeV")
print()
print("Relative error:", abs(total_mass_diff - delta_m_exp_MeV) / delta_m_exp_MeV * 100, "%")

# Y-type model total masses
f_center = 930e6 * eV_to_J / h  # 930 MeV center
M_proton = (f_center + 2*f_u + f_d) * h / (1e6 * eV_to_J)
M_neutron = (f_center + f_u + 2*f_d) * h / (1e6 * eV_to_J)

print(f"\nY-type model absolute masses:")
print(f"  Proton mass = {M_proton:.1f} MeV")
print(f"  Neutron mass = {M_neutron:.1f} MeV")
print(f"  Difference = {M_neutron - M_proton:.3f} MeV")
