import matplotlib.pyplot as plt
import numpy as np

# Data in Billions INR
locations = ['Chennai', 'Gurugram', 'Pune']

# Without Synergy
prod_cost_without = np.array([30.75, 30.10, 29.90])
inv_cost_without  = np.array([0.139, 0.103, 0.184])
log_cost_without  = np.array([6.50, 6.50, 5.50])
sm_cost_without   = np.array([2.50, 2.50, 2.50])
depr_without      = np.array([5.00, 4.00, 5.00])
total_without     = prod_cost_without + inv_cost_without + log_cost_without + sm_cost_without + depr_without

# With Synergy
prod_cost_with = np.array([28.6125, 27.72, 27.705])
inv_cost_with  = np.array([0.129, 0.095, 0.171])
log_cost_with  = np.array([5.85, 5.85, 4.95])
sm_cost_with   = np.array([2.50, 2.50, 2.50])
depr_with      = np.array([5.00, 4.00, 5.00])
total_with     = prod_cost_with + inv_cost_with + log_cost_with + sm_cost_with + depr_with

# Plot settings
bar_width = 0.5
ind = np.arange(len(locations))

# Figure 1: Total Cost Breakdown Without Synergy (Stacked Bar Chart)
fig1, ax1 = plt.subplots(figsize=(8, 6))
p1 = ax1.bar(ind, prod_cost_without, bar_width, label='Production')
p2 = ax1.bar(ind, inv_cost_without, bar_width, bottom=prod_cost_without, label='Inventory')
p3 = ax1.bar(ind, log_cost_without, bar_width, 
             bottom=prod_cost_without+inv_cost_without, label='Logistics')
p4 = ax1.bar(ind, sm_cost_without, bar_width, 
             bottom=prod_cost_without+inv_cost_without+log_cost_without, label='S&M')
p5 = ax1.bar(ind, depr_without, bar_width, 
             bottom=prod_cost_without+inv_cost_without+log_cost_without+sm_cost_without, label='Depreciation')

ax1.set_title('Total Cost Breakdown Without Synergy')
ax1.set_ylabel('Cost (Billion INR)')
ax1.set_xticks(ind)
ax1.set_xticklabels(locations)
ax1.legend()

for i, v in enumerate(total_without):
    ax1.text(i, v + 0.5, f'{v:.2f}B', ha='center', fontweight='bold')

# Figure 2: Total Cost Breakdown With Synergy (Stacked Bar Chart)
fig2, ax2 = plt.subplots(figsize=(8, 6))
p1w = ax2.bar(ind, prod_cost_with, bar_width, label='Production')
p2w = ax2.bar(ind, inv_cost_with, bar_width, bottom=prod_cost_with, label='Inventory')
p3w = ax2.bar(ind, log_cost_with, bar_width, 
              bottom=prod_cost_with+inv_cost_with, label='Logistics')
p4w = ax2.bar(ind, sm_cost_with, bar_width, 
              bottom=prod_cost_with+inv_cost_with+log_cost_with, label='S&M')
p5w = ax2.bar(ind, depr_with, bar_width, 
              bottom=prod_cost_with+inv_cost_with+log_cost_with+sm_cost_with, label='Depreciation')

ax2.set_title('Total Cost Breakdown With Synergy')
ax2.set_ylabel('Cost (Billion INR)')
ax2.set_xticks(ind)
ax2.set_xticklabels(locations)
ax2.legend()

for i, v in enumerate(total_with):
    ax2.text(i, v + 0.5, f'{v:.2f}B', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
