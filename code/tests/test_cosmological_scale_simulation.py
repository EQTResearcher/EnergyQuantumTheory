"""
宇宙学尺度模拟模块单元测试
"""

import pytest
import numpy as np
from src.cosmological_scale_simulation import CosmologicalParameters, CosmologicalSimulator


class TestCosmologicalParameters:
    """测试宇宙学参数配置"""
    
    def test_default_parameters(self):
        """测试默认参数值"""
        params = CosmologicalParameters()
        assert params.L == 1e6 * 3.086e16  # 1 Mpc
        assert params.rho_0 == 1e-20
        assert params.redshift == 10.0


class TestCosmologicalSimulator:
    """测试宇宙学模拟器"""
    
    @pytest.fixture
    def simulator(self):
        """创建模拟器实例"""
        params = CosmologicalParameters(N=50)  # 较小网格加速测试
        return CosmologicalSimulator(params)
    
    def test_initialization(self, simulator):
        """测试初始化"""
        assert simulator.rho.shape == (50,)
        assert np.all(simulator.rho >= 0)
    
    def test_structure_detection(self, simulator):
        """测试结构检测"""
        test_rho = simulator.params.rho_0 * np.array([1.0, 3.0, 1.0])  # 中间有结构
        structures = simulator.detect_structures(test_rho, threshold=2.0)
        assert structures['count'] == 1
        assert structures['max_overdensity'] == 3.0
    
    def test_mass_calculation(self, simulator):
        """测试质量计算"""
        mass = simulator.calculate_total_mass()
        assert mass > 0
    
    def test_sigma8_calculation(self, simulator):
        """测试σ₈计算"""
        sigma8 = simulator.calculate_sigma8()
        assert 0 <= sigma8 <= 2.0  # 合理范围
