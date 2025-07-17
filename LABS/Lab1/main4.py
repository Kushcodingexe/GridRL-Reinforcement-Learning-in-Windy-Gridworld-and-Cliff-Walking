import numpy as np
import matplotlib.pyplot as plt

# Given parameters
mu = 1  # Service rate (μ)
lambdas = np.array([0.5, 0.6, 0.7, 0.8, 0.9])  # Arrival rates (λ)

# Compute E[T] and E[N] for each λ
E_T = 1 / (mu - lambdas)  # Expected response time
E_N = lambdas / (mu - lambdas)  # Expected number of jobs in the system

# Check Little's Law
little_law_values = lambdas * E_T

# Print values for verification
print("λ\tE[T]\tE[N]\tλ * E[T] (Little's Law)")
for i in range(len(lambdas)):
    print(f"{lambdas[i]:.1f}\t{E_T[i]:.2f}\t{E_N[i]:.2f}\t{little_law_values[i]:.2f}")

# Plot E[T] and E[N]
plt.figure(figsize=(10, 5))

# Plot E[T]
plt.subplot(1, 2, 1)
plt.plot(lambdas, E_T, marker='o', linestyle='-', color='b', label="E[T]")
plt.xlabel("λ (Arrival Rate)")
plt.ylabel("E[T] (Response Time)")
plt.title("Expected Response Time vs. λ")
plt.grid()
plt.legend()

# Plot E[N]
plt.subplot(1, 2, 2)
plt.plot(lambdas, E_N, marker='s', linestyle='-', color='r', label="E[N]")
plt.xlabel("λ (Arrival Rate)")
plt.ylabel("E[N] (Number of Jobs)")
plt.title("Expected Number of Jobs vs. λ")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
