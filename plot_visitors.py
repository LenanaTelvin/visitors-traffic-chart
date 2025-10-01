# plot_visitors.py
# Recreates the Visitors by web traffic sources bar chart.
import matplotlib.pyplot as plt
import numpy as np

months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
desktop = [50, 53, 59, 56, 62]
mobile = [39, 47, 42, 51, 51]
referral = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.22

c_blue = '#2f83d6'
c_pink = '#e06b9a'
c_yellow = '#f2b400'

fig, ax = plt.subplots(figsize=(10,5.5))
b1 = ax.bar(x - width, desktop, width, color=c_blue)
b2 = ax.bar(x, mobile, width, color=c_pink)
b3 = ax.bar(x + width, referral, width, color=c_yellow)

for bars in (b1, b2, b3):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f"{int(bar.get_height())}", ha='center', va='bottom', fontsize=9)

ax.set_title('Visitors by web traffic sources', fontsize=16, pad=14)
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylabel('visitors\\nin thousands', fontsize=11, labelpad=10)
ax.set_ylim(0,110)
ax.set_yticks([0,20,40,60,80,100])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(['Direct', 'Referral', 'Social'], loc='upper left', frameon=False, fontsize=9)
plt.tight_layout()
plt.savefig('visitors_by_web_traffic.png', dpi=150)
plt.show()
