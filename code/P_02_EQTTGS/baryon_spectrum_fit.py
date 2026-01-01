#"""
#Fit baryon octet masses with Y-type model
#"""

import numpy as np
from scipy.optimize import least_squares

# Experimental baryon masses (MeV/c^2)
baryons = [
    ("p",    [2, 1, 0], 938.272),   # uud
    ("n",    [1, 2, 0], 939.565),   # udd  
    ("Lambda",[1, 1, 1], 1115.683), # uds
    ("Sigma+",[2, 0, 1], 1189.37),  # uus
    ("Sigma0",[1, 1, 1], 1192.642), # uds (different state)
    ("Sigma-",[0, 2, 1], 1197.449), # dds
    ("Xi0",  [1, 0, 2], 1314.86),   # uss
    ("Xi-",  [0, 1, 2], 1321.71)    # dss
]

# Extract data
counts = np.array([b[1] for b in baryons])  # (u, d, s) counts
masses_exp = np.array([b[2] for b in baryons])

def mass_model(params):
    """Y-type model: M = M_g + n_u*M_u + n_d*M_d + n_s*M_s"""
    M_g, M_u, M_d, M_s = params
    quark_masses = np.array([M_u, M_d, M_s])
    return M_g + counts @ quark_masses

def residuals(params):
    return mass_model(params) - masses_exp

# Initial guess (MeV)
x0 = [900, 2, 5, 100]

# Fit with bounds
bounds = ([800, 0, 0, 50], [1000, 10, 10, 200])
result = least_squares(residuals, x0, bounds=bounds)

M_g_fit, M_u_fit, M_d_fit, M_s_fit = result.x

print("=== Baryon Octet Mass Fit (Y-type Model) ===")
print(f"Fitted parameters:")
print(f"  Gluon event mass M_g = {M_g_fit:.1f} MeV/c²")
print(f"  Up quark mass M_u = {M_u_fit:.1f} MeV/c²")  
print(f"  Down quark mass M_d = {M_d_fit:.1f} MeV/c²")
print(f"  Strange quark mass M_s = {M_s_fit:.1f} MeV/c²")
print()

# Compare predictions
masses_pred = mass_model([M_g_fit, M_u_fit, M_d_fit, M_s_fit])
print("Baryon    Exp(MeV)  Pred(MeV)  Residual(MeV)")
print("-" * 50)
for i, b in enumerate(baryons):
    residual = masses_pred[i] - b[2]
    print(f"{b[0]:<8}  {b[2]:>8.3f}  {masses_pred[i]:>9.3f}  {residual:>11.3f}")

# Calculate RMS error
rms_error = np.sqrt(np.mean((masses_pred - masses_exp)**2))
print(f"\nRMS error: {rms_error:.1f} MeV")
