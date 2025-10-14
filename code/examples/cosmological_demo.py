"""
宇宙学尺度模拟使用示例

展示不同红移和参数的宇宙学模拟
"""

from src.cosmological_scale_simulation import CosmologicalParameters, CosmologicalSimulator
import matplotlib.pyplot as plt


def redshift_study():
    """
    红移研究：不同宇宙时期的结构形成
    """
    redshifts = [15.0, 10.0, 5.0]  # 不同红移
    results = []
    
    for z in redshifts:
        print(f"\n模拟红移 z = {z}")
        
        # 根据红移调整参数
        params = CosmologicalParameters(
            redshift=z,
            rho_0=1e-20 * (1 + z)**3,  # 随红移变化的密度
            total_time=1e14 / (1 + z)   # 早期演化更快
        )
        
        simulator = CosmologicalSimulator(params)
        simulator.run_simulation()
        
        comparison = simulator.compare_with_observations()
        results.append((z, comparison))
        
        print(f"质量: {comparison['simulated_mass_solar']:.2e} M☉")
        print(f"σ₈: {comparison['simulated_sigma8']:.3f}")
    
    return results


def parameter_sensitivity_study():
    """
    参数敏感性分析
    """
    feedback_coefficients = [1e-4, 1e-3, 1e-2]
    sensitivity_results = []
    
    for k in feedback_coefficients:
        params = CosmologicalParameters(k=k)
        simulator = CosmologicalSimulator(params)
        simulator.run_simulation()
        
        mass = simulator.calculate_total_mass()
        sigma8 = simulator.calculate_sigma8()
        
        sensitivity_results.append({
            'feedback_coefficient': k,
            'final_mass': mass,
            'sigma8': sigma8,
            'structure_count': simulator.history['structures'][-1]['count']
        })
    
    return sensitivity_results


if __name__ == "__main__":
    print("=== EQT 宇宙学尺度模拟示例 ===")
    
    # 红移研究
    print("\n1. 红移演化研究:")
    redshift_results = redshift_study()
    
    # 参数敏感性
    print("\n2. 参数敏感性分析:")
    sensitivity_results = parameter_sensitivity_study()
    
    for result in sensitivity_results:
        print(f"k={result['feedback_coefficient']:.1e}: "
              f"质量={result['final_mass']:.2e} kg, "
              f"σ₈={result['sigma8']:.3f}")
    
    print("\n宇宙学模拟示例完成!")
