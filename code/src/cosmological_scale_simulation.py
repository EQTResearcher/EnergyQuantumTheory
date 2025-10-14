"""
EQT Cosmological Scale Simulation Module

模拟宇宙学尺度的星系形成过程，验证质量积累和结构形成。
基于能量子理论（EQT）的多尺度统一框架。

Author: EQT Research Team  
Created: 2025
License: MIT
Reference: JWST (2023) 高红移星系观测, DESI (2025) 结构形成
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from dataclasses import dataclass
from typing import Tuple, Optional, Dict
import astropy.units as u
from astropy.constants import M_sun, pc


@dataclass
class CosmologicalParameters:
    """
    宇宙学尺度模拟参数配置类
    
    Attributes:
        L (float): 模拟区域尺寸 (m)
        N (int): 网格点数
        dt (float): 时间步长 (s)
        total_time (float): 总模拟时间 (s)  
        rho_0 (float): 初始宇宙物质密度 (kg/m³)
        k (float): 结构形成反馈系数 (s⁻¹)
        D (float): 宇宙学扩散系数 (m²/s)
        S_cosmic (float): 宇宙学涨落强度 (kg/m³ s)
        m (int): 非线性反馈幂次
        redshift (float): 模拟对应的红移
    """
    L: float = 1e6 * 3.086e16  # 1 Mpc in meters
    N: int = 100
    dt: float = 1e12           # 时间步长 ~ 3万年
    total_time: float = 1e14   # 总时间 ~ 3百万年
    rho_0: float = 1e-20       # 初始宇宙密度
    k: float = 1e-3            # 结构形成系数
    D: float = 1e-10           # 宇宙学扩散系数
    S_cosmic: float = 1e-10    # 宇宙学涨落
    m: int = 2                 # 非线性反馈
    redshift: float = 10.0     # 对应JWST高红移观测


class CosmologicalSimulator:
    """
    宇宙学尺度模拟器类
    
    实现宇宙学尺度下物质密度场的演化模拟，验证：
    1. 星系质量函数和分布
    2. 结构形成时间尺度  
    3. 与JWST、DESI观测数据对比
    """
    
    def __init__(self, params: CosmologicalParameters):
        """
        初始化宇宙学模拟器
        
        Args:
            params: 宇宙学模拟参数配置对象
        """
        self.params = params
        self.x = np.linspace(-params.L/2, params.L/2, params.N)
        self.rho = self._initialize_cosmic_density()
        self.laplacian = self._build_laplacian()
        self.history = {
            'time': [],
            'density': [],
            'mass': [],
            'structures': []
        }
        
    def _initialize_cosmic_density(self) -> np.ndarray:
        """
        初始化宇宙物质密度场
        
        Returns:
            np.ndarray: 包含宇宙学扰动的初始密度分布
        """
        # 宇宙微波背景级别的初始扰动 ~ 10^-5
        cosmic_perturbation = 1e-5 * np.random.randn(self.params.N)
        return self.params.rho_0 * (1 + cosmic_perturbation)
    
    def _build_laplacian(self):
        """
        构建宇宙学尺度的拉普拉斯算子
        
        Returns:
            scipy.sparse matrix: 拉普拉斯算子矩阵
        """
        dx = self.params.L / self.params.N
        diagonals = [1, -2, 1]
        offsets = [-1, 0, 1]
        return diags(diagonals, offsets, shape=(self.params.N, self.params.N)) / dx**2
    
    def calculate_structure_feedback(self, rho: np.ndarray) -> np.ndarray:
        """
        计算结构形成正反馈项
        
        Args:
            rho: 当前物质密度场
            
        Returns:
            np.ndarray: 结构形成反馈项
        """
        return self.params.k * rho**self.params.m
    
    def calculate_cosmic_diffusion(self, rho: np.ndarray) -> np.ndarray:
        """
        计算宇宙学扩散项
        
        Args:
            rho: 当前物质密度场
            
        Returns:
            np.ndarray: 宇宙学扩散项
        """
        return self.params.D * (self.laplacian @ rho)
    
    def calculate_gravitational_convection(self, rho: np.ndarray) -> np.ndarray:
        """
        计算引力对流项 (v ~ -∇ρ/ρ₀)
        
        Args:
            rho: 当前物质密度场
            
        Returns:
            np.ndarray: 引力对流项
        """
        dx = self.params.L / self.params.N
        grad_rho = np.gradient(rho, dx)
        v = -grad_rho / self.params.rho_0  # 引力驱动的速度场
        return -np.gradient(rho * v, dx)
    
    def calculate_cosmic_fluctuation(self) -> np.ndarray:
        """
        计算宇宙学原初涨落
        
        Returns:
            np.ndarray: 宇宙学涨落项
        """
        return self.params.S_cosmic * np.random.randn(self.params.N)
    
    def detect_structures(self, rho: np.ndarray, threshold: float = 2.0) -> Dict:
        """
        检测形成的宇宙学结构
        
        Args:
            rho: 当前密度场
            threshold: 结构检测阈值
            
        Returns:
            Dict: 结构检测结果
        """
        overdensity = rho / self.params.rho_0
        structures = overdensity > threshold
        
        structure_properties = {
            'count': np.sum(structures),
            'mass_fraction': np.sum(rho[structures]) / np.sum(rho),
            'max_overdensity': np.max(overdensity),
            'positions': self.x[structures]
        }
        
        return structure_properties
    
    def run_simulation(self) -> None:
        """
        执行完整的宇宙学模拟过程
        """
        steps = int(self.params.total_time / self.params.dt)
        
        print(f"开始宇宙学模拟: {steps} 步, 红移 z={self.params.redshift}")
        
        for step in range(steps):
            current_time = step * self.params.dt
            
            # 计算各项物理过程
            feedback = self.calculate_structure_feedback(self.rho)
            diffusion = self.calculate_cosmic_diffusion(self.rho)
            convection = self.calculate_gravitational_convection(self.rho)
            fluctuation = self.calculate_cosmic_fluctuation()
            
            # 更新密度场
            delta_rho = self.params.dt * (feedback - diffusion - convection + fluctuation)
            self.rho += delta_rho
            self.rho = np.maximum(self.rho, 0)  # 确保密度非负
            
            # 记录历史数据和检测结构
            if step % 100 == 0:
                structures = self.detect_structures(self.rho)
                self.history['time'].append(current_time)
                self.history['density'].append(self.rho.copy())
                self.history['mass'].append(self.calculate_total_mass())
                self.history['structures'].append(structures)
                
                if step % 1000 == 0:
                    print(f"步数: {step}, 结构数量: {structures['count']}, "
                          f"最大过密度: {structures['max_overdensity']:.2f}")
    
    def calculate_total_mass(self) -> float:
        """
        计算总质量
        
        Returns:
            float: 总质量 (kg)
        """
        dx = self.params.L / self.params.N
        return np.sum(self.rho * dx**3)
    
    def calculate_sigma8(self) -> float:
        """
        计算结构形成幅度 σ₈
        
        Returns:
            float: σ₈ 值
        """
        from scipy.ndimage import uniform_filter
        
        # 在8 Mpc/h尺度上计算密度涨落
        window_size = max(1, int(8 * 3.086e16 / (self.params.L / self.params.N)))
        smoothed_rho = uniform_filter(self.rho, size=window_size)
        delta_rho = (self.rho - smoothed_rho) / smoothed_rho
        
        # 计算均方根涨落
        sigma8 = np.sqrt(np.mean(delta_rho**2))
        return sigma8
    
    def compare_with_observations(self) -> Dict[str, float]:
        """
        与观测数据对比
        
        Returns:
            Dict: 与观测数据的对比结果
        """
        total_mass_kg = self.calculate_total_mass()
        total_mass_solar = total_mass_kg / M_sun.value
        
        sigma8 = self.calculate_sigma8()
        
        comparison = {
            'simulated_mass_solar': total_mass_solar,
            'jwst_expected_mass': 1e9,  # JWST观测的典型星系质量 M☉
            'simulated_sigma8': sigma8,
            'desi_measured_sigma8': 0.78,  # DESI 2025测量值
            'mass_consistency': total_mass_solar / 1e9,
            'sigma8_consistency': sigma8 / 0.78
        }
        
        return comparison
    
    def visualize_cosmic_evolution(self, save_path: Optional[str] = None) -> None:
        """
        可视化宇宙学演化结果
        
        Args:
            save_path: 图片保存路径
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 最终密度分布
        axes[0, 0].plot(self.x / 3.086e16, self.rho, 'b-', linewidth=2, label="ρ(r)")
        axes[0, 0].set_xlabel("Position (Mpc)")
        axes[0, 0].set_ylabel("Density (kg/m³)")
        axes[0, 0].set_title("Final Matter Density Distribution")
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # 过密度演化
        overdensity = self.rho / self.params.rho_0
        axes[0, 1].plot(self.x / 3.086e16, overdensity, 'r-', linewidth=2)
        axes[0, 1].axhline(y=2.0, color='gray', linestyle='--', label='Structure Threshold')
        axes[0, 1].set_xlabel("Position (Mpc)")
        axes[0, 1].set_ylabel("Overdensity ρ/ρ₀")
        axes[0, 1].set_title("Matter Overdensity")
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # 质量演化历史
        times_Myr = np.array(self.history['time']) / (1e6 * 365.25 * 24 * 3600)
        masses_solar = np.array(self.history['mass']) / M_sun.value
        axes[1, 0].plot(times_Myr, masses_solar, 'g-', linewidth=2)
        axes[1, 0].set_xlabel("Time (Myr)")
        axes[1, 0].set_ylabel("Total Mass (M☉)")
        axes[1, 0].set_title("Mass Accumulation History")
        axes[1, 0].grid(True, alpha=0.3)
        
        # 结构数量演化
        structure_counts = [s['count'] for s in self.history['structures']]
        axes[1, 1].plot(times_Myr, structure_counts, 'purple', linewidth=2)
        axes[1, 1].set_xlabel("Time (Myr)")
        axes[1, 1].set_ylabel("Number of Structures")
        axes[1, 1].set_title("Structure Formation History")
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()


def main():
    """
    主函数：运行宇宙学尺度模拟示例
    """
    # 初始化宇宙学参数
    params = CosmologicalParameters()
    simulator = CosmologicalSimulator(params)
    
    print("=== EQT 宇宙学尺度模拟 ===")
    print(f"模拟尺度: {params.L / 3.086e16:.1f} Mpc")
    print(f"红移: z = {params.redshift}")
    print(f"初始密度: {params.rho_0:.1e} kg/m³")
    
    # 运行模拟
    simulator.run_simulation()
    
    # 计算和对比结果
    total_mass = simulator.calculate_total_mass()
    sigma8 = simulator.calculate_sigma8()
    comparison = simulator.compare_with_observations()
    
    print(f"\n=== 模拟结果 ===")
    print(f"总质量: {total_mass:.2e} kg")
    print(f"太阳质量: {comparison['simulated_mass_solar']:.2e} M☉")
    print(f"JWST预期质量: ~1e9 M☉")
    print(f"质量一致性: {comparison['mass_consistency']:.2f}")
    
    print(f"\n结构形成幅度:")
    print(f"模拟 σ₈: {sigma8:.3f}")
    print(f"DESI测量 σ₈: 0.78")
    print(f"σ₈一致性: {comparison['sigma8_consistency']:.3f}")
    
    # 可视化
    simulator.visualize_cosmic_evolution("cosmological_simulation.png")


if __name__ == "__main__":
    main()
