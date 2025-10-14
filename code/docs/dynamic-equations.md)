# EQT 动态方程文档

## 核心方程
```
∂ρ/∂t = kρ² + D∇²ρ - ∇·(vρ) + S
```

### 各项物理意义
- **反应项 (kρ²)**: 能量子非线性自相互作用
- **扩散项 (D∇²ρ)**: 能量子随机运动
- **平流项 (-∇·(vρ))**: 在有势场中的定向运动  
- **源项 (S)**: 外部能量输入

## 数值方法

### 空间离散
- **扩散项**: 中心差分格式
- **平流项**: 迎风差分或中心差分
- **反应项**: 显式处理

### 时间推进
- **方法**: 前向欧拉法
- **稳定性**: 需要满足CFL条件

### 边界条件
- **零通量**: ∂ρ/∂n = 0
- **周期性**: ρ(x+L) = ρ(x)
- **狄利克雷**: ρ = 固定值

## 使用方法

```python
from src.dynamic_equations.core import EQT DynamicsSolver, DynamicsParameters

# 设置参数
params = DynamicsParameters(k=1e-4, D=0.1, v=0.05)

# 创建求解器
solver = EQT DynamicsSolver(params)

# 设置初始条件
initial_rho = create_gaussian_initial_condition((100, 100))

# 求解方程
results = solver.solve(initial_rho)
```

## 应用场景

1. **原子尺度**: 电荷分离和粒子形成
2. **宇宙尺度**: 结构形成和星系演化  
3. **一般应用**: 模式形成和自组织现象

## 验证指标

- **质量守恒** (零通量边界)
- **数值稳定性**
- **物理合理性** (密度非负)
