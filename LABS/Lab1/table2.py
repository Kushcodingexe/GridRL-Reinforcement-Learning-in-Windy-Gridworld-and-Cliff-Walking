import matplotlib.pyplot as plt

# Data for 10-year costs
columns = ['Location', 'Without Synergy (B INR)', 'With Synergy (B INR)']
data = [
    ['Chennai', '629.47', '587.37'],
    ['Gurugram', '608.34', '564.42'],
    ['Pune', '602.24', '562.24']
]

fig, ax = plt.subplots(figsize=(8, 2.5))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

plt.title('Total 10-Year Cost Comparison by Location', fontsize=14, pad=20)
plt.show()
