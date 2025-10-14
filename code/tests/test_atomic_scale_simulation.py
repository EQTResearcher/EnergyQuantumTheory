"""
原子尺度模拟模块单元测试
"""

import pytest
import numpy as np
from src.atomic_scale_simulation import SimulationParameters, AtomicScaleSimulator


class TestSimulationParameters:
    """测试参数配置类"""
    
    def test_default_parameters(self):
        """测试默认参数值"""
        params = SimulationParameters()
        assert params.L == 1e-9
        assert params.N == 100
        assert params.dt == 1e-12


class TestAtomicScaleSimulator:
    """测试原子尺度模拟器"""
    
    @pytest.fixture
    def simulator(self):
        """创建模拟器实例"""
        params = SimulationParameters(N=50)  # 使用较小网格加速测试
        return AtomicScaleSimulator(params)
    
    def test_initialization(self, simulator):
        """测试初始化"""
        assert simulator.rho.shape == (50,)
        assert np.all(simulator.rho >= 0)
    
    def test_feedback_calculation(self, simulator):
        """测试正反馈计算"""
        test_rho = np.array([1e10, 2e10])
        feedback = simulator.calculate_feedback(test_rho)
        assert feedback.shape == test_rho.shape
    
    def test_charge_calculation(self, simulator):
        """测试电荷计算"""
        charge = simulator.calculate_charge()
        assert isinstance(charge, float)
    
    def test_fine_structure_constant(self, simulator):
        """测试精细结构常数计算"""
        alpha = simulator.calculate_fine_structure_constant()
        assert 0 < alpha < 0.1  # 合理范围检查
