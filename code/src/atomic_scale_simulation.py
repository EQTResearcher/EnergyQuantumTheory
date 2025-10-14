"""
EQT Atomic Scale Simulation Module

模拟氢原子尺度的能量子密度场演化，验证电荷生成和精细结构常数。
基于能量子理论（EQT）的核心原理：力 F ∝ -∇ρ

Author: EQT Research Team
Created: 2025
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass
class SimulationParameters:
    """
    原子尺度模拟参数配置类
    
    Attributes:
        L (float): 模拟区域尺寸 (m)
        N (int): 网格点数
        dt (float): 时间步长 (s)
        total_time (float): 总模拟时间 (s)
        rho_0 (float): 均衡能量子密度 (m^-3)
        k (float): 正反馈系数 (s^-1)
        D (float): 扩散系数 (m^2/s)
        S_quantum (float): 量子涨落强度 (m^-3 s^-1)
        m (int): 正反馈幂次
    """
    L: float = 1e-9      # 1 nm 模拟区域
    N: int = 100         # 网格点数
    dt: float = 1e-12    # 1 ps 时间步长
    total_time: float = 1e-8  # 10 ns 总时间
    rho_0: float = 1e10  # 均衡密度
    k: float = 1e-3      # 正反馈系数
    D: float = 1e-19     # 扩散系数
    S_quantum: float = 1e20  # 量子涨落
    m: int = 2           # 正反馈幂次


class AtomicScaleSimulator:
    """
    原子尺度模拟器类
    
    实现氢原子尺度下能量子密度场的演化模拟，验证：
    1. 正负电荷分离现象
    2. 精细结构常数计算
    3. 电荷量匹配验证
    """
    
    def __init__(self, params: SimulationParameters):
        """
        初始化模拟器
        
        Args:
            params: 模拟参数配置对象
        """
        self.params = params
        self.x = np.linspace(-params.L/2, params.L/2, params.N)
        self.rho = self._initialize_density()
        self.laplacian = self._build_laplacian()
        self.history = []
        
    def _initialize_density(self) -> np.ndarray:
        """
        初始化能量子密度场
        
        Returns:
            np.ndarray: 初始密度分布，包含随机扰动
        """
        # CMB级别初始扰动 ~ 10^-5
        perturbation = 1e-5 * np.random.randn(self.params.N)
        return self.params.rho_0 * (1 + perturbation)
    
    def _build_laplacian(self):
        """
        构建拉普拉斯算子矩阵（二阶中心差分）
        
        Returns:
            scipy.sparse matrix: 拉普拉斯算子矩阵
        """
        dx = self.params.L / self.params.N
        diagonals = [1, -2, 1]
        offsets = [-1, 0, 1]
        return diags(diagonals, offsets, shape=(self.params.N, self.params.N)) / dx**2
    
    def calculate_feedback(self, rho: np.ndarray) -> np.ndarray:
        """
        计算正反馈项
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 正反馈项
        """
        return self.params.k * rho**self.params.m
    
    def calculate_diffusion(self, rho: np.ndarray) -> np.ndarray:
        """
        计算扩散项
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 扩散项
        """
        return self.params.D * (self.laplacian @ rho)
    
    def calculate_convection(self, rho: np.ndarray) -> np.ndarray:
        """
        计算对流项 (v ~ -∇ρ)
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 对流项
        """
        dx = self.params.L / self.params.N
        grad_rho = np.gradient(rho, dx)
        v = -grad_rho / self.params.rho_0  # 速度场
        return -np.gradient(rho * v, dx)
    
    def calculate_quantum_fluctuation(self) -> np.ndarray:
        """
        计算量子涨落项
        
        Returns:
            np.ndarray: 量子涨落项
        """
        return self.params.S_quantum * np.random.randn(self.params.N)
    
    def run_simulation(self) -> None:
        """
        执行完整的模拟过程
        """
        steps = int(self.params.total_time / self.params.dt)
        
        for step in range(steps):
            # 计算各项物理过程
            feedback = self.calculate_feedback(self.rho)
            diffusion = self.calculate_diffusion(self.rho)
            convection = self.calculate_convection(self.rho)
            noise = self.calculate_quantum_fluctuation()
            
            # 更新密度场
            delta_rho = self.params.dt * (feedback - diffusion - convection + noise)
            self.rho += delta_rho
            self.rho = np.maximum(self.rho, 0)  # 确保密度非负
            
            # 记录历史数据
            if step % 100 == 0:
                self.history.append(self.rho.copy())
    
    def calculate_charge(self) -> float:
        """
        计算净电荷量
        
        Returns:
            float: 电荷量 (C)
        """
        dx = self.params.L / self.params.N
        charge_density = self.rho - self.params.rho_0
        return np.sum(charge_density * dx**3)
    
    def calculate_fine_structure_constant(self, frequency: float = 1e15) -> float:
        """
        计算精细结构常数
        
        Args:
            frequency: 特征频率 (Hz)
            
        Returns:
            float: 计算的精细结构常数
        """
        # Γ ~ ρc³/f³
        gamma = (self.params.rho_0 * (3e8)**3) / (frequency**3)
        # E = hf
        energy = 6.626e-34 * frequency
        # α ~ Γħc/E
        alpha = (gamma * 1.054e-34 * 3e8) / energy
        
        return alpha
    
    def visualize_results(self, save_path: Optional[str] = None) -> None:
        """
        可视化模拟结果
        
        Args:
            save_path: 图片保存路径
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # 密度分布图
        ax1.plot(self.x, self.rho, 'b-', linewidth=2, label="ρ(r)")
        ax1.set_xlabel("Position (m)")
        ax1.set_ylabel("Density (m^-3)")
        ax1.set_title("Energy Quanta Density Distribution")
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 电荷密度图
        charge_density = self.rho - self.params.rho_0
        ax2.plot(self.x, charge_density, 'r-', linewidth=2, label="Charge Density")
        ax2.set_xlabel("Position (m)")
        ax2.set_ylabel("Charge Density (m^-3)")
        ax2.set_title("Charge Distribution")
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()


def main():
    """
    主函数：运行原子尺度模拟示例
    """
    # 初始化参数
    params = SimulationParameters()
    simulator = AtomicScaleSimulator(params)
    
    print("开始原子尺度模拟...")
    print(f"模拟参数: L={params.L:.1e} m, N={params.N}, dt={params.dt:.1e} s")
    
    # 运行模拟
    simulator.run_simulation()
    
    # 计算结果
    charge = simulator.calculate_charge()
    alpha = simulator.calculate_fine_structure_constant()
    
    print(f"\n模拟结果:")
    print(f"净电荷: {charge:.2e} C")
    print(f"预期电荷: ±1.60e-19 C (氢原子电荷)")
    print(f"计算精细结构常数: {alpha:.5f}")
    print(f"标准精细结构常数: 0.007297 (1/137)")
    
    # 可视化
    simulator.visualize_results("atomic_scale_simulation.png")


if __name__ == "__main__":
    main()
