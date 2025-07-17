import matplotlib.pyplot as plt
import numpy as np

# Locations
locations = ['Chennai', 'Gurugram', 'Pune']

# -- Without Synergy --
# Costs per car (in thousand INR)
# Production, Inventory, Logistics, S&M, Depreciation
prod_cost_no = np.array([615, 602, 598])        # from 30.75B, 30.10B, 29.90B divided by 50,000 cars (in K INR)
inv_cost_no  = np.array([2.78, 2.06, 3.68])       # in K INR
log_cost_no  = np.array([130, 130, 110])          # in K INR
sm_cost_no   = np.array([50, 50, 50])              # in K INR
depr_cost_no = np.array([100, 80, 100])            # in K INR

# Total cost without synergy per car (in K INR)
total_no = prod_cost_no + inv_cost_no + log_cost_no + sm_cost_no + depr_cost_no

# -- With Synergy --
prod_cost_synergy = np.array([572.25, 554.4, 554.1])  # in K INR
inv_cost_synergy  = np.array([2.58, 1.9, 3.42])        # in K INR
log_cost_synergy  = np.array([117, 117, 99])           # in K INR
sm_cost_synergy   = np.array([50, 50, 50])              # in K INR
depr_cost_synergy = np.array([100, 80, 100])            # in K INR

# Total cost with synergy per car (in K INR)
total_synergy = prod_cost_synergy + inv_cost_synergy + log_cost_synergy + sm_cost_synergy + depr_cost_synergy

# Plotting settings
bar_width = 0.5
ind = np.arange(len(locations))

# --- Plot 1: Without Synergy ---
fig, ax = plt.subplots(figsize=(9, 6))
p1 = ax.bar(ind, prod_cost_no, bar_width, label='Production')
p2 = ax.bar(ind, inv_cost_no, bar_width, bottom=prod_cost_no, label='Inventory')
p3 = ax.bar(ind, log_cost_no, bar_width, bottom=prod_cost_no+inv_cost_no, label='Logistics')
p4 = ax.bar(ind, sm_cost_no, bar_width, bottom=prod_cost_no+inv_cost_no+log_cost_no, label='S&M')
p5 = ax.bar(ind, depr_cost_no, bar_width, bottom=prod_cost_no+inv_cost_no+log_cost_no+sm_cost_no, label='Depreciation')

ax.set_title('Total Cost Breakdown per Car (Without Synergy)', fontsize=14)
ax.set_ylabel('Cost per Car (K INR)', fontsize=12)
ax.set_xticks(ind)
ax.set_xticklabels(locations, fontsize=12)
ax.legend(fontsize=10)

# Annotate total cost on top of bars
for i, total in enumerate(total_no):
    ax.text(i, total + 5, f'{total:.1f}K', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# --- Plot 2: With Synergy ---
fig2, ax2 = plt.subplots(figsize=(9, 6))
p1s = ax2.bar(ind, prod_cost_synergy, bar_width, label='Production')
p2s = ax2.bar(ind, inv_cost_synergy, bar_width, bottom=prod_cost_synergy, label='Inventory')
p3s = ax2.bar(ind, log_cost_synergy, bar_width, 
              bottom=prod_cost_synergy+inv_cost_synergy, label='Logistics')
p4s = ax2.bar(ind, sm_cost_synergy, bar_width, 
              bottom=prod_cost_synergy+inv_cost_synergy+log_cost_synergy, label='S&M')
p5s = ax2.bar(ind, depr_cost_synergy, bar_width, 
              bottom=prod_cost_synergy+inv_cost_synergy+log_cost_synergy+sm_cost_synergy, label='Depreciation')

ax2.set_title('Total Cost Breakdown per Car (With Synergy)', fontsize=14)
ax2.set_ylabel('Cost per Car (K INR)', fontsize=12)
ax2.set_xticks(ind)
ax2.set_xticklabels(locations, fontsize=12)
ax2.legend(fontsize=10)

# Annotate total cost on top of bars
for i, total in enumerate(total_synergy):
    ax2.text(i, total + 5, f'{total:.1f}K', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
