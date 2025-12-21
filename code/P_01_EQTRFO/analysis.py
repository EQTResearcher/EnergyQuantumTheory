# analysis.py
import numpy as np
import matplotlib.pyplot as plt

class StructureAnalyzer:
    def analyze(self, manager, step):
        # 简单诊断：高密度核识别与盘状统计
        rho = np.sum(manager.weights, axis=1)
        high_density = np.where(rho > np.mean(rho) * 5)[0]
        print(f"步 {step}: 高密度核数 {len(high_density)}")
        # 可扩展保存图4–5
