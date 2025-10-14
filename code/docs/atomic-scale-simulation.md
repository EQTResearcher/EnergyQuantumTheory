# 原子尺度模拟文档

## 物理背景
基于能量子理论（EQT）模拟氢原子尺度的电荷生成过程，验证：
- 能量子密度场分化为正负电荷区
- 计算净电荷量匹配基本电荷
- 推导精细结构常数

## 核心方程
```
∂ρ/∂t = kρ^m + D∇²ρ - ∇·(ρv) + S_quantum
v = -∇ρ/ρ₀
F ∝ -∇ρ
```

## 使用方法
```python
from src.atomic_scale_simulation import SimulationParameters, AtomicScaleSimulator

# 基本使用
params = SimulationParameters()
simulator = AtomicScaleSimulator(params)
simulator.run_simulation()

# 获取结果
charge = simulator.calculate_charge()
alpha = simulator.calculate_fine_structure_constant()
```

## 预期结果
- 电荷量：~1.6×10⁻¹⁹ C
- 精细结构常数：~0.0073
- 计算时间：~10⁻⁸ s
