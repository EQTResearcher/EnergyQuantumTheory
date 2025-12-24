import numpy as np
from events import EventManager
from dynamics import PhaseUpdater, WeightUpdater, CascadeTrigger
from analysis import StructureAnalyzer
from utils import set_seed

params = {
    'N_initial': 1000,      # 测试用1000，工作站可改10000
    'steps': 30,            # 测试用30步，工作站可改150
    'alpha': 0.8,
    'beta': 0.5,
    'lambda_d': 0.8,
    'w_trigger': 0.7,
    'rho_crit_factor': 1.8,
    'eta_d': 0.15,
    'seed': 42
}

set_seed(params['seed'])
manager = EventManager(params['N_initial'])

# 初始化种子连接
n = manager.n
num_seeds = 15 * n
rows = np.random.randint(0, n, size=num_seeds)
cols = np.random.randint(0, n, size=num_seeds)
mask = rows != cols
rows, cols = rows[mask], cols[mask]
rows = np.concatenate([rows, cols])
cols = np.concatenate([cols, rows])
data = 0.03 * np.random.rand(len(rows))
data = np.clip(data, 0.01, 0.05)

manager.weights = manager.weights.tolil()
for r, c, d in zip(rows, cols, data):
    manager.weights[r, c] = max(manager.weights[r, c], d)
for i in range(n):
    row_data = manager.weights.data[i]
    if len(row_data) > 0:
        row_data[:] = np.clip(row_data, 0, 0.05)
manager.weights = manager.weights.tocsr()

phase_updater = PhaseUpdater(params['alpha'])
weight_updater = WeightUpdater(params['beta'], params['lambda_d'])
cascade = CascadeTrigger(params['w_trigger'], params['rho_crit_factor'], params['eta_d'])
analyzer = StructureAnalyzer()

print(f"初始: 事件 {manager.n}, 总能量 {manager.total_energy():.3f}")

for step in range(params['steps']):
    phase_updater.update(manager)
    weight_updater.update(manager)
    cascade.trigger(manager)
    
    if step % 10 == 0:
        analyzer.analyze(manager, step)

print("\n✅ 能量守恒验证：")
print(f"初始能量: {manager.initial_energy:.3f}")
print(f"最终能量: {manager.total_energy():.3f}")
print(f"相对变化: {100*(manager.total_energy() - manager.initial_energy)/manager.initial_energy:.3f}%")
