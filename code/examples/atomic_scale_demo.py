"""
原子尺度模拟使用示例

展示如何调整参数研究不同物理现象
"""

from src.atomic_scale_simulation import SimulationParameters, AtomicScaleSimulator
import matplotlib.pyplot as plt


def parameter_study():
    """
    参数研究：不同反馈系数的影响
    """
    k_values = [1e-4, 1e-3, 1e-2]  # 不同反馈系数
    results = []
    
    for k in k_values:
        params = SimulationParameters(k=k)
        simulator = AtomicScaleSimulator(params)
        simulator.run_simulation()
        
        charge = simulator.calculate_charge()
        results.append((k, charge, simulator.rho))
        
        print(f"k={k:.1e}, 电荷={charge:.2e} C")
    
    return results


def convergence_test():
    """
    收敛性测试：不同网格分辨率
    """
    N_values = [50, 100, 200]
    convergence_data = []
    
    for N in N_values:
        params = SimulationParameters(N=N, dt=1e-13)
        simulator = AtomicScaleSimulator(params)
        simulator.run_simulation()
        
        final_rho = simulator.rho
        convergence_data.append((N, final_rho))
    
    return convergence_data


if __name__ == "__main__":
    print("=== EQT 原子尺度模拟示例 ===")
    
    # 参数研究
    print("\n1. 参数研究:")
    results = parameter_study()
    
    # 收敛性测试
    print("\n2. 收敛性测试:")
    convergence_data = convergence_test()
    
    print("\n示例运行完成！")
