import matplotlib.pyplot as plt

# Data for the corrected third slide table (Post-Synergy Cost Breakdown)
columns = ['Cost Component', 'Chennai', 'Gurugram', 'Pune']
data = [
    ['Production Cost (Post-Synergy)', '572.25K', '554.4K', '554.1K'],
    ['Inventory Carrying Cost (Post-Synergy)', '0.129B', '0.095B', '0.171B'],
    ['Logistics Cost (Post-Synergy)', '5.85B', '5.85B', '4.95B'],
    ['Selling & Marketing (S&M)', '2.50B', '2.50B', '2.50B'],
    ['Depreciation', '5.00B', '4.00B', '5.00B'],
    ['Total Cost (With Synergy)', '42.09B', '40.17B', '40.33B'],
    ['Cost per Car (With Synergy)', '842K', '803K', '807K']
]

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.5)

plt.title('Revised Cost Breakdown (With Synergy) – Per Car and Total', fontsize=14, pad=20)
plt.show()
