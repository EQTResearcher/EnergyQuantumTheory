import numpy as np
from scipy.sparse import lil_matrix

class EventManager:
    def __init__(self, N_initial):
        self.n = N_initial
        
        self.fs = np.random.normal(1.0, 0.05, N_initial)
        self.fs = np.clip(self.fs, 0.1, 2.0)
        self.thetas = np.random.uniform(0, 2*np.pi, N_initial)
        self.ds = np.random.normal(0, 1, (N_initial, 3))
        norms = np.linalg.norm(self.ds, axis=1)
        norms[norms == 0] = 1.0
        self.ds /= norms[:, np.newaxis]
        
        self.initial_energy = np.sum(self.fs)
        self.weights = lil_matrix((N_initial, N_initial))
    
    def total_energy(self):
        return np.sum(self.fs)
    
    def add_event(self, f_new, theta_new, d_new):
        self.n += 1
        self.fs = np.append(self.fs, f_new)
        self.thetas = np.append(self.thetas, theta_new)
        self.ds = np.vstack((self.ds, d_new))
        
        old_n = self.weights.shape[0]
        new_weights = lil_matrix((self.n, self.n))
        new_weights[:old_n, :old_n] = self.weights
        self.weights = new_weights
