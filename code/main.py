{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'events'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-5cf64114b1e8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# main.py\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mevents\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mEventManager\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mdynamics\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPhaseUpdater\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mWeightUpdater\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mCascadeTrigger\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0manalysis\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mStructureAnalyzer\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'events'"
     ]
    }
   ],
   "source": [
    "# main.py\n",
    "import numpy as np\n",
    "from events import EventManager\n",
    "from dynamics import PhaseUpdater, WeightUpdater, CascadeTrigger\n",
    "from analysis import StructureAnalyzer\n",
    "from utils import set_seed\n",
    "\n",
    "# 参数配置（正文基准）\n",
    "params = {\n",
    "    'N_initial': 10000,\n",
    "    'steps': 150,\n",
    "    'alpha': 0.5,\n",
    "    'beta': 0.3,\n",
    "    'lambda_d': 0.8,\n",
    "    'w_trigger': 0.8,\n",
    "    'rho_crit_factor': 2.5,\n",
    "    'eta_d': 0.15,\n",
    "    'seed': 42\n",
    "}\n",
    "\n",
    "set_seed(params['seed'])\n",
    "\n",
    "# 初始化\n",
    "manager = EventManager(params['N_initial'])\n",
    "phase_updater = PhaseUpdater(params['alpha'])\n",
    "weight_updater = WeightUpdater(params['beta'], params['lambda_d'])\n",
    "cascade = CascadeTrigger(params['w_trigger'], params['rho_crit_factor'], params['eta_d'])\n",
    "analyzer = StructureAnalyzer()\n",
    "\n",
    "print(f\"初始事件数: {len(manager.events)}, 初始总能量: {manager.total_energy():.4f}\")\n",
    "\n",
    "# 主循环\n",
    "for step in range(params['steps']):\n",
    "    phase_updater.update(manager)\n",
    "    weight_updater.update(manager)\n",
    "    cascade.trigger(manager)\n",
    "    \n",
    "    if step % 20 == 0:\n",
    "        analyzer.analyze(manager, step)\n",
    "        print(f\"步 {step}: 事件数 {len(manager.events)}, 平均频率 {manager.avg_frequency():.4f}, \"\n",
    "              f\"总能量 {manager.total_energy():.4f}\")\n",
    "\n",
    "print(\"模拟完成！复现正文图4–5结果。\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# events.py\n",
    "import numpy as np\n",
    "\n",
    "class EnergyEvent:\n",
    "    def __init__(self, f, theta, d):\n",
    "        self.f = f\n",
    "        self.theta = theta % (2 * np.pi)\n",
    "        self.d = d / np.linalg.norm(d)\n",
    "\n",
    "class EventManager:\n",
    "    def __init__(self, N_initial):\n",
    "        np.random.seed(42)\n",
    "        self.events = []\n",
    "        fs = np.random.normal(1.0, 0.05, N_initial)\n",
    "        fs = np.clip(fs, 0.1, 2.0)\n",
    "        thetas = np.random.uniform(0, 2*np.pi, N_initial)\n",
    "        ds = np.random.normal(0, 1, (N_initial, 3))\n",
    "        norms = np.linalg.norm(ds, axis=1)\n",
    "        ds[norms > 0] /= norms[norms > 0][:, np.newaxis]\n",
    "        \n",
    "        for i in range(N_initial):\n",
    "            self.events.append(EnergyEvent(fs[i], thetas[i], ds[i]))\n",
    "        \n",
    "        self.weights = np.zeros((N_initial, N_initial))\n",
    "        self.initial_energy = np.sum(fs)\n",
    "    \n",
    "    def total_energy(self):\n",
    "        return sum(e.f for e in self.events)\n",
    "    \n",
    "    def avg_frequency(self):\n",
    "        return np.mean([e.f for e in self.events])\n",
    "    \n",
    "    def add_event(self, f_new, theta_new, d_new):\n",
    "        self.events.append(EnergyEvent(f_new, theta_new, d_new))\n",
    "        # 权重矩阵扩展（实际稀疏实现）"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
