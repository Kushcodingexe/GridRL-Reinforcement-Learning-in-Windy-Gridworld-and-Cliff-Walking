import matplotlib.pyplot as plt
import numpy as np

# Data for cost per car (post-synergy, in K INR)
locations = ['Chennai', 'Gurugram', 'Pune']
cost_per_car_post = [841.8, 803.0, 807.0]  # in K INR

plt.figure(figsize=(8,6))
bars = plt.bar(locations, cost_per_car_post, color=['salmon', 'gold', 'lightgreen'], edgecolor='black')

plt.xlabel('Location', fontsize=12)
plt.ylabel('Cost per Car (K INR)', fontsize=12)
plt.title('10-Year Cost per Car (Post-Synergy)', fontsize=14)
plt.ylim(790, 860)

# Annotate each bar with the cost value
for bar, cost in zip(bars, cost_per_car_post):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{cost:.1f}K', ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
