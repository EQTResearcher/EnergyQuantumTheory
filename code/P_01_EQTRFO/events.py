# events.py
import numpy as np

class EnergyEvent:
    def __init__(self, f, theta, d):
        self.f = f
        self.theta = theta % (2 * np.pi)
        self.d = d / np.linalg.norm(d)

class EventManager:
    def __init__(self, N_initial):
        np.random.seed(42)
        self.events = []
        fs = np.random.normal(1.0, 0.05, N_initial)
        fs = np.clip(fs, 0.1, 2.0)
        thetas = np.random.uniform(0, 2*np.pi, N_initial)
        ds = np.random.normal(0, 1, (N_initial, 3))
        norms = np.linalg.norm(ds, axis=1)
        ds[norms > 0] /= norms[norms > 0][:, np.newaxis]
        
        for i in range(N_initial):
            self.events.append(EnergyEvent(fs[i], thetas[i], ds[i]))
        
        self.weights = np.zeros((N_initial, N_initial))
        self.initial_energy = np.sum(fs)
    
    def total_energy(self):
        return sum(e.f for e in self.events)
    
    def avg_frequency(self):
        return np.mean([e.f for e in self.events])
    
    def add_event(self, f_new, theta_new, d_new):
        self.events.append(EnergyEvent(f_new, theta_new, d_new))
        # 权重矩阵扩展（实际稀疏实现）
