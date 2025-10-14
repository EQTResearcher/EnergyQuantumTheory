"""
动态方程模块单元测试
"""

import pytest
import numpy as np
from src.dynamic_equations.core import (
    EQT DynamicsSolver, DynamicsParameters, BoundaryCondition,
    NumericalScheme, create_gaussian_initial_condition
)


class TestDynamicsSolver:
    """测试动态方程求解器"""
    
    @pytest.fixture
    def solver(self):
        """创建求解器实例"""
        params = DynamicsParameters(dt=0.01, dx=0.1, total_time=0.1)
        return EQT DynamicsSolver(params)
    
    @pytest.fixture
    def test_field(self):
        """创建测试场"""
        return create_gaussian_initial_condition((10, 10), sigma=0.2)
    
    def test_reaction_term(self, solver, test_field):
        """测试反应项计算"""
        reaction = solver.reaction_term(test_field)
        assert reaction.shape == test_field.shape
        assert np.all(reaction >= 0)
    
    def test_diffusion_term(self, solver, test_field):
        """测试扩散项计算"""
        diffusion = solver.diffusion_term(test_field)
        assert diffusion.shape == test_field.shape
    
    def test_boundary_conditions(self, solver, test_field):
        """测试边界条件应用"""
        for bc_type in BoundaryCondition:
            solver.params.bc_type = bc_type
            result = solver.apply_boundary_conditions(test_field.copy())
            assert result.shape == test_field.shape
    
    def test_time_step(self, solver, test_field):
        """测试时间步进"""
        new_field = solver.time_step(test_field)
        assert new_field.shape == test_field.shape
        assert np.all(new_field >= 0)
    
    def test_gaussian_initialization(self):
        """测试高斯初始条件"""
        field = create_gaussian_initial_condition((20, 20))
        assert field.shape == (20, 20)
        assert np.max(field) > 0
        assert np.all(field >= 0)


def test_parameter_validation():
    """测试参数验证"""
    with pytest.raises(ValueError):
        DynamicsParameters(dt=0)  # 无效时间步长
