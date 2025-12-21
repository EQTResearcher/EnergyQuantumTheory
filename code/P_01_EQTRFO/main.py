# main.py
import numpy as np
from events import EventManager
from dynamics import PhaseUpdater, WeightUpdater, CascadeTrigger
from analysis import StructureAnalyzer
from utils import set_seed

# 参数配置（正文基准）
params = {
    'N_initial': 10000,
    'steps': 150,
    'alpha': 0.5,
    'beta': 0.3,
    'lambda_d': 0.8,
    'w_trigger': 0.8,
    'rho_crit_factor': 2.5,
    'eta_d': 0.15,
    'seed': 42
}

set_seed(params['seed'])

# 初始化
manager = EventManager(params['N_initial'])
phase_updater = PhaseUpdater(params['alpha'])
weight_updater = WeightUpdater(params['beta'], params['lambda_d'])
cascade = CascadeTrigger(params['w_trigger'], params['rho_crit_factor'], params['eta_d'])
analyzer = StructureAnalyzer()

print(f"初始事件数: {len(manager.events)}, 初始总能量: {manager.total_energy():.4f}")

# 主循环
for step in range(params['steps']):
    phase_updater.update(manager)
    weight_updater.update(manager)
    cascade.trigger(manager)
    
    if step % 20 == 0:
        analyzer.analyze(manager, step)
        print(f"步 {step}: 事件数 {len(manager.events)}, 平均频率 {manager.avg_frequency():.4f}, "
              f"总能量 {manager.total_energy():.4f}")

print("模拟完成！复现正文图4–5结果。")
