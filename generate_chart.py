import matplotlib.pyplot as plt
import numpy as np

# Set font for CJK characters
plt.rcParams['font.family'] = 'Noto Sans CJK SC'
plt.rcParams['axes.unicode_minus'] = False

# Data for comparison
labels = ['本系统 (v8.1)', 'GMRC 指南', 'GE 标准', 'Siemens 标准', 'ISO 21789']
min_values = [110, 100, 125, 130, 120]
max_values = [150, 150, 175, 180, 160]
typical_values = [125, 125, 150, 155, 140]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# Create error bars to represent the range
ax.bar(x, typical_values, width, label='典型/基准设定值', color='#3498db', alpha=0.7)
ax.errorbar(x, typical_values, yerr=[np.array(typical_values)-np.array(min_values), np.array(max_values)-np.array(typical_values)], 
            fmt='none', ecolor='#e74c3c', capsize=5, label='标准推荐区间')

# Add labels and title
ax.set_ylabel('开启压力 (mmH2O)')
ax.set_title('防爆门开启压力设定值：本系统与行业标准对比', fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for i, v in enumerate(typical_values):
    ax.text(i, v + 5, f'{v}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/ge-filter-selector/compliance_chart.png', dpi=300)
print("Chart generated successfully at /home/ubuntu/ge-filter-selector/compliance_chart.png")
