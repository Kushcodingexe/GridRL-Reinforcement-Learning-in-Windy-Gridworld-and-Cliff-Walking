import matplotlib.pyplot as plt
import numpy as np

# Define conversion factor: multiply per-car value in K INR by 0.725 to get 10-year total in B INR
factor = 0.725

# Pre-Synergy per-car values (in K INR)
pre_ch = [615, 2.78, 130, 50, 69]
pre_gu = [602, 2.06, 130, 50, 55]
pre_pu = [598, 3.68, 110, 50, 69]

# Post-Synergy per-car values (in K INR)
post_ch = [572.25, 2.58, 117, 50, 69]
post_gu = [554.4, 1.90, 117, 50, 55]
post_pu = [554.1, 3.42, 99, 50, 69]

# Convert to 10-year totals in B INR
def convert(values):
    return [v * factor for v in values]

pre_ch_b = convert(pre_ch)
pre_gu_b = convert(pre_gu)
pre_pu_b = convert(pre_pu)

post_ch_b = convert(post_ch)
post_gu_b = convert(post_gu)
post_pu_b = convert(post_pu)

# Create arrays: rows = locations, columns = cost components [Production, Inventory, Logistics, S&M, Depreciation]
pre_data = np.array([pre_ch_b, pre_gu_b, pre_pu_b])
post_data = np.array([post_ch_b, post_gu_b, post_pu_b])

locations = ['Chennai', 'Gurugram', 'Pune']
x = np.arange(len(locations))
bar_width = 0.6

# Define component labels and colors
components = ['Production', 'Inventory', 'Logistics', 'S&M', 'Depreciation']
colors = ['skyblue', 'lightgreen', 'tomato', 'violet', 'gray']

def plot_stacked(ax, data_array, title):
    bottom_vals = np.zeros(len(locations))
    for i in range(data_array.shape[1]):
        ax.bar(x, data_array[:, i], bar_width, bottom=bottom_vals,
               color=colors[i], edgecolor='black', label=components[i] if x[0]==0 and i==0 else "")
        bottom_vals += data_array[:, i]
    # Annotate totals
    for i, total in enumerate(bottom_vals):
        ax.text(i, total + 1, f'{total:.1f}B', ha='center', fontsize=10, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(locations, fontsize=12)
    ax.set_ylabel('Cost (B INR)', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.set_ylim(0, bottom_vals.max()*1.15)

# Create subplots for Pre- and Post-Synergy
fig, (ax_pre, ax_post) = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('10-Year Total Cost Breakdown by Location\nPre-Synergy vs. Post-Synergy', fontsize=16)

plot_stacked(ax_pre, pre_data, 'Pre-Synergy Breakdown')
plot_stacked(ax_post, post_data, 'Post-Synergy Breakdown')

# Create a unified legend at the top
patches = [plt.matplotlib.patches.Patch(color=colors[i], label=components[i]) for i in range(len(components))]
fig.legend(handles=patches, loc='upper center', ncol=5, fontsize=10, bbox_to_anchor=(0.5, 0.98))

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
