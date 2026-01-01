#"""
#Demonstration of narrowband quark model
#"""

import numpy as np
import matplotlib.pyplot as plt
from baryon_model import random_unit_vector

def create_quark_band(f_center, sigma_f, theta_center, n_events=20):
    """Create a narrowband of quark events"""
    events = []
    for _ in range(n_events):
        f = np.random.normal(f_center, sigma_f)
        theta = np.random.normal(theta_center, 0.1)
        d = random_unit_vector()
        events.append(type('Event', (), {'f': f, 'theta': theta, 'd': d})())
    return events

# Parameters
f_u_center = 5.3e20  # Hz (corresponding to ~2.2 MeV)
f_d_center = 11.3e20 # Hz (corresponding to ~4.7 MeV)  
sigma_f = 0.5e20     # 10% bandwidth

# Create bands
u_band = create_quark_band(f_u_center, sigma_f, 0.0)
d_band = create_quark_band(f_d_center, sigma_f, np.pi)

# Plot frequency distributions
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist([e.f for e in u_band], bins=15, alpha=0.7, label='Up quark band')
plt.hist([e.f for e in d_band], bins=15, alpha=0.7, label='Down quark band')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count')
plt.title('Narrowband Quark Frequency Distributions')
plt.legend()

plt.subplot(1, 2, 2)
# Simulate proton vs neutron total frequency
proton_freqs = [e.f for e in u_band[:2]] + [e.f for e in d_band[:1]]
neutron_freqs = [e.f for e in u_band[:1]] + [e.f for e in d_band[:2]]
plt.hist(proton_freqs, bins=10, alpha=0.7, label='Proton (uud)')
plt.hist(neutron_freqs, bins=10, alpha=0.7, label='Neutron (udd)')
plt.xlabel('Total Frequency (Hz)')
plt.ylabel('Count')
plt.title('Proton vs Neutron Total Frequency')
plt.legend()

plt.tight_layout()
plt.savefig('narrowband_demo.png', dpi=150, bbox_inches='tight')
plt.show()

print("Narrowband demonstration saved as 'narrowband_demo.png'")
