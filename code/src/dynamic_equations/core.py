"""
EQT Dynamic Equations Core Module

实现能量子理论（EQT）的核心动态方程：
∂ρ/∂t = kρ² + D∇²ρ - ∇·(vρ) + S

包含反应-扩散-平流方程的数值求解器，支持多种边界条件和数值格式。

Author: EQT Research Team
Created: 2025
License: MIT
"""

import numpy as np
from typing import Tuple, Optional, Dict, Callable
from dataclasses import dataclass
from enum import Enum


class BoundaryCondition(Enum):
    """边界条件类型枚举"""
    ZERO_FLUX = "zero_flux"      # 零通量边界
    PERIODIC = "periodic"        # 周期性边界  
    DIRICHLET = "dirichlet"      # 固定值边界
    NEUMANN = "neumann"          # 诺伊曼边界


class NumericalScheme(Enum):
    """数值格式枚举"""
    CENTRAL_DIFFERENCE = "central"     # 中心差分
    UPWIND = "upwind"                  # 迎风差分
    LAX_WENDROFF = "lax_wendroff"      # Lax-Wendroff格式


@dataclass
class DynamicsParameters:
    """
    动态方程模拟参数配置类
    
    Attributes:
        k (float): 反应项系数
        D (float): 扩散系数
        v (float): 平流速度
        S (float): 源项强度
        dt (float): 时间步长
        dx (float): 空间步长
        total_time (float): 总模拟时间
        bc_type (BoundaryCondition): 边界条件类型
        scheme (NumericalScheme): 数值格式
    """
    k: float = 1e-4
    D: float = 0.1
    v: float = 0.05
    S: float = 0.0
    dt: float = 0.1
    dx: float = 1.0
    total_time: float = 50.0
    bc_type: BoundaryCondition = BoundaryCondition.ZERO_FLUX
    scheme: NumericalScheme = NumericalScheme.CENTRAL_DIFFERENCE


class EQT DynamicsSolver:
    """
    EQT动态方程求解器类
    
    实现反应-扩散-平流方程的数值求解：
    ∂ρ/∂t = kρ² + D∇²ρ - ∇·(vρ) + S
    """
    
    def __init__(self, params: DynamicsParameters):
        """
        初始化求解器
        
        Args:
            params: 动态方程参数配置
        """
        self.params = params
        self.boundary_handlers = {
            BoundaryCondition.ZERO_FLUX: self._apply_zero_flux_bc,
            BoundaryCondition.PERIODIC: self._apply_periodic_bc,
            BoundaryCondition.DIRICHLET: self._apply_dirichlet_bc
        }
        
    def reaction_term(self, rho: np.ndarray) -> np.ndarray:
        """
        计算反应项: kρ²
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 反应项
        """
        return self.params.k * rho**2
    
    def diffusion_term(self, rho: np.ndarray) -> np.ndarray:
        """
        计算扩散项: D∇²ρ (中心差分)
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 扩散项
        """
        laplacian = np.zeros_like(rho)
        
        # 内部点使用中心差分
        laplacian[1:-1, 1:-1] = (
            rho[2:, 1:-1] + rho[:-2, 1:-1] + 
            rho[1:-1, 2:] + rho[1:-1, :-2] - 
            4 * rho[1:-1, 1:-1]
        ) / (self.params.dx ** 2)
        
        return self.params.D * laplacian
    
    def advection_term(self, rho: np.ndarray) -> np.ndarray:
        """
        计算平流项: -∇·(vρ)
        
        Args:
            rho: 当前密度场
            
        Returns:
            np.ndarray: 平流项
        """
        advection = np.zeros_like(rho)
        
        if self.params.scheme == NumericalScheme.UPWIND:
            # 迎风差分格式
            for i in range(1, rho.shape[0]-1):
                for j in range(1, rho.shape[1]-1):
                    if self.params.v >= 0:
                        advection_x = -self.params.v * (rho[i, j] - rho[i, j-1]) / self.params.dx
                    else:
                        advection_x = -self.params.v * (rho[i, j+1] - rho[i, j]) / self.params.dx
                    advection[i, j] = advection_x
                    
        elif self.params.scheme == NumericalScheme.CENTRAL_DIFFERENCE:
            # 中心差分格式
            advection[1:-1, 1:-1] = -self.params.v * (
                rho[1:-1, 2:] - rho[1:-1, :-2]
            ) / (2 * self.params.dx)
        
        return advection
    
    def source_term(self, shape: Tuple[int, int]) -> np.ndarray:
        """
        计算源项: S
        
        Args:
            shape: 场形状
            
        Returns:
            np.ndarray: 源项
        """
        return np.full(shape, self.params.S)
    
    def _apply_zero_flux_bc(self, rho: np.ndarray) -> np.ndarray:
        """应用零通量边界条件"""
        rho[0, :] = rho[1, :]    # 上边界
        rho[-1, :] = rho[-2, :]  # 下边界
        rho[:, 0] = rho[:, 1]    # 左边界
        rho[:, -1] = rho[:, -2]  # 右边界
        return rho
    
    def _apply_periodic_bc(self, rho: np.ndarray) -> np.ndarray:
        """应用周期性边界条件"""
        rho[0, :] = rho[-2, :]   # 上边界
        rho[-1, :] = rho[1, :]   # 下边界
        rho[:, 0] = rho[:, -2]   # 左边界
        rho[:, -1] = rho[:, 1]   # 右边界
        return rho
    
    def _apply_dirichlet_bc(self, rho: np.ndarray, value: float = 0.0) -> np.ndarray:
        """应用狄利克雷边界条件"""
        rho[0, :] = value    # 上边界
        rho[-1, :] = value   # 下边界
        rho[:, 0] = value    # 左边界
        rho[:, -1] = value   # 右边界
        return rho
    
    def apply_boundary_conditions(self, rho: np.ndarray) -> np.ndarray:
        """
        应用边界条件
        
        Args:
            rho: 需要应用边界条件的场
            
        Returns:
            np.ndarray: 应用边界条件后的场
        """
        handler = self.boundary_handlers.get(self.params.bc_type)
        if handler:
            return handler(rho)
        return rho
    
    def time_step(self, rho: np.ndarray) -> np.ndarray:
        """
        执行一个时间步的演化
        
        Args:
            rho: 当前时间步的密度场
            
        Returns:
            np.ndarray: 下一时间步的密度场
        """
        # 计算各项
        reaction = self.reaction_term(rho)
        diffusion = self.diffusion_term(rho)
        advection = self.advection_term(rho)
        source = self.source_term(rho.shape)
        
        # 组合各项并更新
        drho_dt = reaction + diffusion + advection + source
        new_rho = rho + drho_dt * self.params.dt
        
        # 应用边界条件
        new_rho = self.apply_boundary_conditions(new_rho)
        
        # 确保密度非负
        new_rho = np.maximum(new_rho, 0.0)
        
        return new_rho
    
    def solve(self, initial_rho: np.ndarray, 
              progress_callback: Optional[Callable] = None) -> Dict:
        """
        求解动态方程
        
        Args:
            initial_rho: 初始密度场
            progress_callback: 进度回调函数
            
        Returns:
            Dict: 模拟结果和历史数据
        """
        rho = initial_rho.copy()
        steps = int(self.params.total_time / self.params.dt)
        
        history = {
            'time': [],
            'density': [],
            'total_mass': [],
            'max_density': []
        }
        
        for step in range(steps):
            current_time = step * self.params.dt
            
            # 执行时间步
            rho = self.time_step(rho)
            
            # 记录历史数据
            if step % 10 == 0:  # 每10步记录一次
                history['time'].append(current_time)
                history['density'].append(rho.copy())
                history['total_mass'].append(np.sum(rho))
                history['max_density'].append(np.max(rho))
            
            # 进度回调
            if progress_callback and step % 100 == 0:
                progress_callback(step, steps, current_time)
        
        results = {
            'final_density': rho,
            'history': history,
            'parameters': self.params,
            'total_steps': steps
        }
        
        return results


def create_gaussian_initial_condition(shape: Tuple[int, int], 
                                    center: Tuple[float, float] = (0.5, 0.5),
                                    sigma: float = 0.1,
                                    amplitude: float = 1.0) -> np.ndarray:
    """
    创建高斯初始条件
    
    Args:
        shape: 场形状 (ny, nx)
        center: 高斯中心位置 (x, y)，范围 [0, 1]
        sigma: 高斯标准差
        amplitude: 峰值幅度
        
    Returns:
        np.ndarray: 高斯初始条件
    """
    ny, nx = shape
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    X, Y = np.meshgrid(x, y)
    
    # 计算到中心的距离
    r2 = (X - center[0])**2 + (Y - center[1])**2
    
    return amplitude * np.exp(-r2 / (2 * sigma**2))
