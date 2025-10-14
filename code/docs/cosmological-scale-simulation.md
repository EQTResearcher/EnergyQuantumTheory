# 宇宙学尺度模拟文档

## 物理背景
基于能量子理论（EQT）模拟宇宙学尺度的结构形成过程，验证：
- 星系质量积累和分布
- 结构形成时间尺度
- 与JWST高红移星系和DESI大尺度结构的观测对比

## 核心方程
```
∂ρ/∂t = kρᵐ + D∇²ρ - ∇·(ρv) + S_cosmic
v = -∇ρ/ρ₀  (引力驱动)
F ∝ -∇ρ     (EQT统一框架)
```

## 关键参数
- **尺度**: 1 Mpc (百万秒差距)
- **时间**: ~3百万年
- **红移**: z ~ 10 (JWST观测范围)
- **初始密度**: 10⁻²⁰ kg/m³ (宇宙平均密度)

## 预期结果
- 星系质量: ~10⁹ M☉ (匹配JWST观测)
- 结构幅度: σ₈ ~ 0.78 (匹配DESI测量)
- 形成时间: ~10⁶ 年

## 使用方法
```python
from src.cosmological_scale_simulation import CosmologicalParameters, CosmologicalSimulator

# 基本模拟
params = CosmologicalParameters(redshift=10.0)
simulator = CosmologicalSimulator(params)
simulator.run_simulation()

# 结果分析
mass = simulator.calculate_total_mass()
sigma8 = simulator.calculate_sigma8()
comparison = simulator.compare_with_observations()
```

## 验证指标
1. **质量一致性**: 模拟质量 vs JWST观测
2. **结构一致性**: σ₈ vs DESI测量  
3. **时间尺度**: 结构形成速率
4. **空间分布**: 星系成团性
