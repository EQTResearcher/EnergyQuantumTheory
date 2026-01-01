
#"""
#Core event model for baryon structure in EQT.
#"""

import numpy as np

def random_unit_vector():
    """Generate random 3D unit vector"""
    vec = np.random.normal(0, 1, 3)
    return vec / np.linalg.norm(vec)

class EnergyQuantumEvent:
    def __init__(self, f, theta, d=None):
        """
        f: frequency (Hz)
        theta: phase [0, 2π)
        d: direction vector (3D unit vector)
        """
        self.f = f
        self.theta = theta % (2 * np.pi)
        if d is None:
            d = random_unit_vector()
        self.d = np.array(d) / np.linalg.norm(d)
        self.frozen = False

    def update_phase(self, delta_theta):
        if not self.frozen:
            self.theta = (self.theta + delta_theta) % (2 * np.pi)

def interaction_weight(e1, e2, lambda_d=0.8):
    """EQT interaction weight between two events"""
    if e1.frozen or e2.frozen:
        return 0.0
    
    freq_term = (e1.f * e2.f) / (e1.f + e2.f + 1e-12)
    phase_term = np.cos(0.5 * (e1.theta - e2.theta)) ** 2
    dir_term = 1.0 + lambda_d * np.dot(e1.d, e2.d)
    
    return freq_term * phase_term * dir_term

def compute_orthogonality(events):
    """Volume spanned by first 3 direction vectors"""
    if len(events) < 3:
        return 0.0
    mat = np.stack([e.d for e in events[:3]], axis=1)
    return abs(np.linalg.det(mat))

def total_mass_from_frequency(events, h=6.62607015e-34, c=299792458):
    """Compute total mass from sum of h*f/c^2"""
    total_f = sum(e.f for e in events)
    return (h * total_f) / (c * c)  # kg

def mass_MeV_from_frequency(events):
    """Convert total frequency to mass in MeV/c^2"""
    h = 6.62607015e-34  # J·s
    c = 299792458       # m/s
    eV_to_J = 1.602176634e-19
    
    total_f = sum(e.f for e in events)
    mass_J = h * total_f
    mass_MeV = mass_J / (1e6 * eV_to_J)
    return mass_MeV
