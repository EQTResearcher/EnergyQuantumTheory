#"""
#Stability test: Y-type (star) vs Triangle topology
#"""

import numpy as np
import matplotlib.pyplot as plt
from baryon_model import EnergyQuantumEvent, interaction_weight, compute_orthogonality

def create_y_type_baryon():
    """1 high-freq center + 3 near-freq quarks"""
    center = EnergyQuantumEvent(f=1.0e24, theta=0.0, d=[0, 0, 0.1])
    q1 = EnergyQuantumEvent(f=0.95e24, theta=0.0, d=[1, 0, 0])
    q2 = EnergyQuantumEvent(f=0.95e24, theta=0.0, d=[0, 1, 0])
    q3 = EnergyQuantumEvent(f=0.95e24, theta=np.pi, d=[0, 0, 1])
    return [center, q1, q2, q3]

def create_triangle_baryon():
    """3 near-freq quarks only"""
    q1 = EnergyQuantumEvent(f=0.98e24, theta=0.0, d=[1, 0, 0])
    q2 = EnergyQuantumEvent(f=0.98e24, theta=0.0, d=[0, 1, 0])
    q3 = EnergyQuantumEvent(f=0.98e24, theta=np.pi, d=[0, 0, 1])
    return [q1, q2, q3]

def apply_perturbation(events, delta=0.1):
    """Apply small random perturbation to directions"""
    for e in events:
        noise = np.random.normal(0, delta, 3)
        e.d = e.d + noise
        if np.linalg.norm(e.d) > 0:
            e.d = e.d / np.linalg.norm(e.d)

def simulate_evolution(events, steps=20, perturb_step=0):
    """Simulate evolution and record metrics"""
    total_weights = []
    orthogonality = []
    
    for step in range(steps):
        if step == perturb_step:
            apply_perturbation(events)
        
        # Compute total interaction weight
        total_w = 0.0
        n = len(events)
        for i in range(n):
            for j in range(i+1, n):
                total_w += interaction_weight(events[i], events[j])
        total_weights.append(total_w)
        
        # Compute direction orthogonality
        orthogonality.append(compute_orthogonality(events))
        
        # Simple phase update
        for e in events:
            e.update_phase(2 * np.pi * e.f * 1e-25)
    
    return np.array(total_weights), np.array(orthogonality)

def stability_index(weights, ortho, w0, o0):
    """Compute stability index S = avg(w/w0 + o/o0)"""
    w_norm = weights / (w0 + 1e-12)
    o_norm = ortho / (o0 + 1e-12)
    return np.mean(w_norm + o_norm)

# Run comparison
np.random.seed(42)

# Y-type configuration
y_events = create_y_type_baryon()
w0_y, o0_y = simulate_evolution(y_events.copy(), steps=1, perturb_step=0)
w_y, o_y = simulate_evolution(create_y_type_baryon(), steps=20, perturb_step=1)
S_y = stability_index(w_y, o_y, w0_y[0], o0_y[0])

# Triangle configuration
tri_events = create_triangle_baryon()
w0_tri, o0_tri = simulate_evolution(tri_events.copy(), steps=1, perturb_step=0)
w_tri, o_tri = simulate_evolution(create_triangle_baryon(), steps=20, perturb_step=1)
S_tri = stability_index(w_tri, o_tri, w0_tri[0], o0_tri[0])

print(f"Y-type (Star) stability index: {S_y:.3f}")
print(f"Triangle topology stability index: {S_tri:.3f}")

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(w_y / w0_y[0], label=f'Y-type (S={S_y:.2f})')
plt.plot(w_tri / w0_tri[0], label=f'Triangle (S={S_tri:.2f})')
plt.xlabel('Evolution step')
plt.ylabel('Normalized total weight')
plt.legend()
plt.title('Interaction Weight Stability')

plt.subplot(1, 2, 2)
plt.plot(o_y / o0_y[0], label='Y-type')
plt.plot(o_tri / o0_tri[0], label='Triangle')
plt.xlabel('Evolution step')
plt.ylabel('Normalized orthogonality')
plt.legend()
plt.title('Direction Orthogonality Stability')

plt.tight_layout()
plt.savefig('stability_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nFigure saved as 'stability_comparison.png'")
