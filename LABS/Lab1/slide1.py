import matplotlib.pyplot as plt
import numpy as np

# Locations and corresponding cost per car (in thousand INR)
locations = ['Chennai', 'Gurugram', 'Pune']
cost_per_car = [897.8, 864.0, 861.7]  # in K INR as calculated

plt.figure(figsize=(8,6))
bars = plt.bar(locations, cost_per_car, color=['salmon', 'gold', 'lightgreen'], edgecolor='black')

plt.xlabel('Location', fontsize=12)
plt.ylabel('Cost per Car (K INR)', fontsize=12)
plt.title('2027 Total Cost per Car (Without Synergy)', fontsize=14)
plt.ylim(850, 920)

# Annotate each bar with the exact cost per car value
for bar, cost in zip(bars, cost_per_car):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{cost:.1f}K', ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
