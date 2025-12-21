# dynamics.py
import numpy as np

class PhaseUpdater:
    def __init__(self, alpha):
        self.alpha = alpha
    
    def update(self, manager):
        n = len(manager.events)
        for i in range(n):
            pull = 0.0
            for j in range(n):
                if i != j and manager.weights[i,j] > 0.1:
                    delta = manager.events[j].theta - manager.events[i].theta
                    pull += manager.weights[i,j] * np.sin(delta)
            manager.events[i].theta += 2 * np.pi * manager.events[i].f + self.alpha * pull
            manager.events[i].theta %= 2 * np.pi

class WeightUpdater:
    def __init__(self, beta, lambda_d):
        self.beta = beta
        self.lambda_d = lambda_d
    
    def update(self, manager):
        n = len(manager.events)
        for i in range(n):
            for j in range(i+1, n):
                fi, fj = manager.events[i].f, manager.events[j].f
                k = (fi * fj / (fi + fj + 1e-8))**2
                delta_theta = manager.events[j].theta - manager.events[i].theta
                cos_term = np.cos(delta_theta)
                dot_d = np.dot(manager.events[i].d, manager.events[j].d)
                delta_w = self.beta * k * cos_term * (1 + self.lambda_d * dot_d) * (1 - manager.weights[i,j])
                manager.weights[i,j] += delta_w
                manager.weights[j,i] = manager.weights[i,j]
                manager.weights[i,j] = np.clip(manager.weights[i,j], 0, 1)

class CascadeTrigger:
    def __init__(self, w_trigger, rho_crit_factor, eta_d):
        self.w_trigger = w_trigger
        self.rho_crit_factor = rho_crit_factor
        self.eta_d = eta_d
    
    def trigger(self, manager):
        n = len(manager.events)
        rho = np.sum(manager.weights, axis=1)
        avg_rho = np.mean(rho)
        rho_crit = self.rho_crit_factor * avg_rho
        
        new_events = []
        for i in range(n):
            for j in range(i+1, n):
                if manager.weights[i,j] > self.w_trigger and rho[i] + rho[j] > rho_crit:
                    fi, fj = manager.events[i].f, manager.events[j].f
                    if fi < fj:
                        fi, fj, i, j = fj, fi, j, i
                    f_new = fi - fj
                    if f_new > 0.01:
                        manager.events[i].f = fj  # 红移
                        theta_new = (manager.events[i].theta + manager.events[j].theta) / 2
                        d_avg = manager.events[i].d + manager.events[j].d
                        d_new = d_avg + self.eta_d * np.random.normal(0, 1, 3)
                        d_new /= np.linalg.norm(d_new) + 1e-8
                        new_events.append((f_new, theta_new, d_new))
        
        for f_new, theta_new, d_new in new_events:
            manager.add_event(f_new, theta_new, d_new)
