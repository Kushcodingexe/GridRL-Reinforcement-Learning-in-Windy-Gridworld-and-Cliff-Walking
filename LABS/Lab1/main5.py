import numpy as np
import matplotlib.pyplot as plt

# Rewards for each state
R = np.array([4, 7, 1], dtype=float)

# Transition probabilities under the given policy π:
# π(S0) = a2, π(S1) = a1, π(S2) = a3
P_pi = np.array([
    [0.5, 0.4, 0.1],  # from S0 using a2
    [0.2, 0.4, 0.4],  # from S1 using a1
    [0.3, 0.2, 0.5]   # from S2 using a3
], dtype=float)

def compute_value_function(gamma):
    """
    Solve (I - gamma * P_pi) * V = R for V = [V0, V1, V2].
    """
    I = np.eye(3)
    A = I - gamma * P_pi  # Left-hand side
    b = R                 # Right-hand side
    V = np.linalg.solve(A, b)
    return V

# List of discount factors to evaluate
gammas = [0.001, 0.01, 0.1, 0.3, 0.9]

# Arrays to store the computed values
v0_list, v1_list, v2_list = [], [], []

# Compute V(S0), V(S1), V(S2) for each gamma
for g in gammas:
    Vg = compute_value_function(g)
    v0_list.append(Vg[0])
    v1_list.append(Vg[1])
    v2_list.append(Vg[2])
    print(f"gamma = {g}")
    print(f"  V(S0) = {Vg[0]:.6f}, V(S1) = {Vg[1]:.6f}, V(S2) = {Vg[2]:.6f}\n")

# Plot the results
plt.figure(figsize=(8, 5))

# Plot V(S0), V(S1), V(S2) vs gamma
plt.plot(gammas, v0_list, marker='o', label='V(S0)')
plt.plot(gammas, v1_list, marker='s', label='V(S1)')
plt.plot(gammas, v2_list, marker='^', label='V(S2)')

plt.xlabel('Discount Factor (gamma)')
plt.ylabel('Value Function Vπ(S)')
plt.title('Long-Term Discounted Reward for Different Discount Factors')
plt.grid(True)
plt.legend()
plt.show()
