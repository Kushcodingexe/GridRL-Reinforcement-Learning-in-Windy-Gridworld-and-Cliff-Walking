import matplotlib.pyplot as plt
import numpy as np

# Data for cost per car (in K INR)
locations = ['Chennai', 'Gurugram', 'Pune']
cost_per_car = [866.78, 839.06, 830.68]  # in K INR

plt.figure(figsize=(8,6))
bars = plt.bar(locations, cost_per_car, color=['salmon', 'gold', 'lightgreen'], edgecolor='black')

plt.xlabel('Location', fontsize=12)
plt.ylabel('Cost per Car (K INR)', fontsize=12)
plt.title('10-Year Cost per Car (Without Synergy)', fontsize=14)

# Adjust y-axis limits based on the data range (min=830.68, max=866.78)
plt.ylim(820, 880)

# Annotate each bar with the cost value
for bar, cost in zip(bars, cost_per_car):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{cost:.1f}K', ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
