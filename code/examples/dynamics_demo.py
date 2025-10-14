"""
动态方程使用示例

展示EQT动态方程的不同应用场景和参数研究
"""

import numpy as np
import matplotlib.pyplot as plt
from src.dynamic_equations.core import (
    EQT DynamicsSolver, DynamicsParameters, BoundaryCondition, 
    NumericalScheme, create_gaussian_initial_condition
)
from src.dynamic_equations.visualization import DynamicsVisualizer


def basic_simulation_demo():
    """基础模拟演示"""
    print("=== EQT 动态方程基础演示 ===\n")
    
    # 设置参数
    params = DynamicsParameters(
        k=1e-4, D=0.1, v=0.05, S=0.0,
        dt=0.01, dx=0.1, total_time=5.0,
        bc_type=BoundaryCondition.ZERO_FLUX,
        scheme=NumericalScheme.UPWIND
    )
    
    # 创建初始条件
    initial_rho = create_gaussian_initial_condition(
        shape=(100, 100), center=(0.5, 0.5), 
        sigma=0.1, amplitude=1.0
    )
    
    # 创建求解器并求解
    solver = EQT DynamicsSolver(params)
    
    def progress_callback(step, total_steps, time):
        print(f"进度: {step}/{total_steps} (时间: {time:.2f})")
    
    results = solver.solve(initial_rho, progress_callback)
    
    print(f"\n模拟完成! 总步数: {results['total_steps']}")
    print(f"最终总质量: {np.sum(results['final_density']):.4f}")
    
    # 可视化
    visualizer = DynamicsVisualizer(solver)
    visualizer.plot_final_state(results, 'final_state.png')
    visualizer.plot_time_evolution(results, 'time_evolution.png')
    
    return results


def boundary_condition_study():
    """边界条件研究"""
    print("\n=== 边界条件对比研究 ===\n")
    
    bc_types = [BoundaryCondition.ZERO_FLUX, BoundaryCondition.PERIODIC]
    results = {}
    
    for bc_type in bc_types:
        print(f"测试边界条件: {bc_type.value}")
        
        params = DynamicsParameters(
            bc_type=bc_type, total_time=2.0
        )
        
        initial_rho = create_gaussian_initial_condition(
            shape=(50, 50), center=(0.3, 0.3)
        )
        
        solver = EQT DynamicsSolver(params)
        results[bc_type.value] = solver.solve(initial_rho)
    
    return results


def parameter_sensitivity_analysis():
    """参数敏感性分析"""
    print("\n=== 参数敏感性分析 ===\n")
    
    # 测试不同的反应系数
    k_values = [1e-5, 1e-4, 1e-3]
    sensitivity_results = []
    
    for k in k_values:
        params = DynamicsParameters(k=k, total_time=3.0)
        initial_rho = create_gaussian_initial_condition((80, 80))
        
        solver = EQT DynamicsSolver(params)
        results = solver.solve(initial_rho)
        
        final_stats = {
            'k': k,
            'final_mass': np.sum(results['final_density']),
            'max_density': np.max(results['final_density']),
            'mass_change': (np.sum(results['final_density']) - 
                          np.sum(initial_rho)) / np.sum(initial_rho)
        }
        sensitivity_results.append(final_stats)
        
        print(f"k={k:.1e}: 质量变化 = {final_stats['mass_change']:.2%}")
    
    return sensitivity_results


if __name__ == "__main__":
    # 运行基础演示
    basic_results = basic_simulation_demo()
    
    # 边界条件研究
    bc_results = boundary_condition_study()
    
    # 参数敏感性分析
    sensitivity_results = parameter_sensitivity_analysis()
    
    print("\n=== 所有演示完成! ===")
