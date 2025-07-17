import matplotlib.pyplot as plt

# Data (all values in thousand INR per car)
columns = ['Cost Component', 'Chennai', 'Gurugram', 'Pune']
data = [
    ['Production Cost', '615', '602', '598'],
    ['Inventory Carrying Cost', '2.78', '2.06', '3.68'],
    ['Logistics Cost', '130', '130', '110'],
    ['S&M Cost', '50', '50', '50'],
    ['Depreciation', '69', '55', '69'],
    ['Total Cost per Car', '897.8', '864.0', '861.7']
]

# Create a figure
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis('tight')
ax.axis('off')

# Create table
table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

plt.title('2027 Per-Car Cost Breakdown (Without Synergy)', fontsize=14, pad=20)
plt.show()
