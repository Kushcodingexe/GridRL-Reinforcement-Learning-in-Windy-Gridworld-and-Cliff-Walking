import matplotlib.pyplot as plt
import numpy as np

# Define locations and x-axis positions
locations = ['Chennai', 'Gurugram', 'Pune']
x = np.arange(len(locations))
bar_width = 0.6

# --- Pre-Synergy Data (2027, in K INR per car) ---
production_pre = np.array([615, 602, 598])
inventory_pre  = np.array([2.78, 2.06, 3.68])
logistics_pre  = np.array([130, 130, 110])
sm_pre         = np.array([50, 50, 50])
depreciation_pre = np.array([100, 80, 100])
total_pre = production_pre + inventory_pre + logistics_pre + sm_pre + depreciation_pre

# --- Post-Synergy Data (2027, in K INR per car) ---
production_post = np.array([572.25, 554.4, 554.1])
inventory_post  = np.array([2.58, 1.90, 3.42])
logistics_post  = np.array([117, 117, 99])
sm_post         = np.array([50, 50, 50])
depreciation_post = np.array([100, 80, 100])
total_post = production_post + inventory_post + logistics_post + sm_post + depreciation_post

# Create subplots for side-by-side comparison
fig, (ax_pre, ax_post) = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('Cost Breakdown per Car: Pre-Synergy vs. Post-Synergy (2027)', fontsize=16)

def plot_stacked_bar(ax, production, inventory, logistics, sm, depreciation, title):
    # Plot each component as a stacked bar
    p1 = ax.bar(x, production, bar_width, label='Production')
    p2 = ax.bar(x, inventory, bar_width, bottom=production, label='Inventory')
    p3 = ax.bar(x, logistics, bar_width, bottom=production+inventory, label='Logistics')
    p4 = ax.bar(x, sm, bar_width, bottom=production+inventory+logistics, label='S&M')
    p5 = ax.bar(x, depreciation, bar_width, bottom=production+inventory+logistics+sm, label='Depreciation')
    
    # Annotate total cost above each bar
    totals = production + inventory + logistics + sm + depreciation
    for i, total in enumerate(totals):
        ax.text(i, total + 5, f'{total:.1f}K', ha='center', fontsize=10, fontweight='bold')
    
    ax.set_title(title, fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, fontsize=12)
    ax.set_ylabel('Cost per Car (K INR)', fontsize=12)
    ax.legend(fontsize=10)
    
# Plot Pre-Synergy Breakdown
plot_stacked_bar(ax_pre, production_pre, inventory_pre, logistics_pre, sm_pre, depreciation_pre,
                 'Pre-Synergy Breakdown')

# Plot Post-Synergy Breakdown
plot_stacked_bar(ax_post, production_post, inventory_post, logistics_post, sm_post, depreciation_post,
                 'Post-Synergy Breakdown')

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()
