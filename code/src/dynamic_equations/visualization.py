"""
动态方程可视化模块

提供模拟结果的可视化和分析工具
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Optional
from .core import EQT DynamicsSolver, DynamicsParameters


class DynamicsVisualizer:
    """动态方程可视化类"""
    
    def __init__(self, solver: EQT DynamicsSolver):
        self.solver = solver
    
    def plot_final_state(self, results: Dict, 
                        save_path: Optional[str] = None) -> None:
        """
        绘制最终状态
        
        Args:
            results: 模拟结果
            save_path: 保存路径
        """
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # 最终密度分布
        im1 = axes[0].imshow(results['final_density'], cmap='viridis', 
                           origin='lower', aspect='auto')
        axes[0].set_title('Final Density Distribution')
        axes[0].set_xlabel('X Position')
        axes[0].set_ylabel('Y Position')
        plt.colorbar(im1, ax=axes[0], label='Density ρ')
        
        # 初始与最终对比
        initial = results['history']['density'][0]
        final = results['final_density']
        
        im2 = axes[1].imshow(final - initial, cmap='RdBu_r', 
                           origin='lower', aspect='auto')
        axes[1].set_title('Density Change (Final - Initial)')
        axes[1].set_xlabel('X Position')
        axes[1].set_ylabel('Y Position')
        plt.colorbar(im2, ax=axes[1], label='Δρ')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_time_evolution(self, results: Dict,
                          save_path: Optional[str] = None) -> None:
        """
        绘制时间演化
        
        Args:
            results: 模拟结果
            save_path: 保存路径
        """
        history = results['history']
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # 总质量演化
        axes[0, 0].plot(history['time'], history['total_mass'])
        axes[0, 0].set_xlabel('Time')
        axes[0, 0].set_ylabel('Total Mass')
        axes[0, 0].set_title('Total Mass Evolution')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 最大密度演化
        axes[0, 1].plot(history['time'], history['max_density'])
        axes[0, 1].set_xlabel('Time')
        axes[0, 1].set_ylabel('Maximum Density')
        axes[0, 1].set_title('Maximum Density Evolution')
        axes[0, 1].grid(True, alpha=0.3)
        
        # 选择几个时间点展示密度分布
        time_indices = [0, len(history['time'])//3, 2*len(history['time'])//3, -1]
        for idx, time_idx in enumerate(time_indices):
            ax = axes[1, idx]
            density = history['density'][time_idx]
            im = ax.imshow(density, cmap='viridis', origin='lower', aspect='auto')
            ax.set_title(f'Time = {history["time"][time_idx]:.2f}')
            if idx == 0:
                ax.set_ylabel('Y Position')
            ax.set_xlabel('X Position')
            plt.colorbar(im, ax=ax)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_animation(self, results: Dict, 
                        filename: str = 'dynamics_evolution.gif') -> None:
        """
        创建演化动画（需要安装imageio）
        
        Args:
            results: 模拟结果
            filename: 动画文件名
        """
        try:
            import imageio
        except ImportError:
            print("请安装 imageio: pip install imageio")
            return
        
        history = results['history']
        frames = []
        
        for i, density in enumerate(history['density']):
            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(density, cmap='viridis', origin='lower', aspect='auto')
            ax.set_title(f'Time = {history["time"][i]:.2f}')
            ax.set_xlabel('X Position')
            ax.set_ylabel('Y Position')
            plt.colorbar(im, ax=ax, label='Density ρ')
            plt.tight_layout()
            
            # 转换为图像
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            frames.append(image)
            
            plt.close(fig)
        
        # 保存为GIF
        imageio.mimsave(filename, frames, fps=10)
        print(f"动画已保存为: {filename}")
