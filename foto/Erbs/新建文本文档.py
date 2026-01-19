import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置数据范围 (晴天指数 CI 从 0 到 1.0)
ci = np.linspace(0, 1.0, 500)
dg = []

# Erbs 模型公式计算
for k_t in ci:
    if k_t <= 0.22:
        val = 1.0 - 0.09 * k_t
    elif 0.22 < k_t <= 0.80:
        val = 0.9511 - 0.1604 * k_t + 4.388 * (k_t**2) - 16.638 * (k_t**3) + 12.336 * (k_t**4)
    else:
        val = 0.165
    dg.append(val)

# 绘图
plt.figure(figsize=(8, 6), dpi=150) # 高清分辨率
plt.plot(ci, dg, 'k-', linewidth=2, label='Erbs Model')

# 添加装饰以模仿原图风格
plt.xlabel('Clearness Index  ($CI$)', fontsize=20, fontname='Arial')
plt.ylabel('Diffuse Fraction  ($D_g$)', fontsize=20, fontname='Arial')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 1.0)
plt.ylim(0, 1.1)
plt.legend()

# 标注关键区间
plt.axvline(x=0.22, color='gray', linestyle=':', alpha=0.5)
plt.axvline(x=0.80, color='gray', linestyle=':', alpha=0.5)
plt.text(0.1, 0.2, 'Linear\nRegion', fontsize=15, color='gray')
plt.text(0.5, 0.8, 'Polynomial\nRegion', fontsize=15, color='gray')
plt.text(0.85, 0.3, 'Const\nRegion', fontsize=15, color='gray')

plt.tight_layout()

# 保存或显示
plt.show()
