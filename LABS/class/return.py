import numpy as np
import matplotlib.pyplot as plt

def compute_discounted_rewards(reward_vector, transition_matrices, policy, discount_factors):
    states = len(reward_vector)
    discounted_rewards = {}
    iterations = {}

    for gamma in discount_factors:
        # Compute the transition matrix under the given policy
        policy_transition_matrix = np.zeros((states, states))
        for s in range(states):
            action = policy[s]
            policy_transition_matrix[s] = transition_matrices[action][s]

        # Solve (I - gamma * P) * V = R iteratively
        I = np.eye(states)
        P = policy_transition_matrix
        R = reward_vector
        V = np.zeros(states)
        
        max_iterations = 20000
        epsilon = 1e-6
        num_iterations = 0

        for _ in range(max_iterations):
            num_iterations += 1
            V_new = R + gamma * np.dot(P, V)
            if np.max(np.abs(V_new - V)) < epsilon:
                break
            V = V_new

        discounted_rewards[gamma] = V
        iterations[gamma] = num_iterations

    return discounted_rewards, iterations

# Inputs
reward_vector = np.array([4, 7, 1])  # R(S0) = 4, R(S1) = 7, R(S2) = 1

transition_matrices = {
    0: np.array([
        [0.3, 0.4, 0.3],
        [0.6, 0.2, 0.2],
        [0.2, 0.2, 0.6]
    ]),
    1: np.array([
        [0.5, 0.4, 0.1],
        [0.3, 0.2, 0.5],
        [0.4, 0.2, 0.4]
    ]),
    2: np.array([
        [0.25, 0.25, 0.5],
        [0.4, 0.3, 0.3],
        [0.2, 0.3, 0.5]
    ])
}

policy = [0, 1, 2]  # pi(S0) = a0, pi(S1) = a1, pi(S2) = a2
discount_factors = [0.1, 0.01, 0.001, 0.3]

# Compute discounted rewards and iterations
discounted_rewards, iterations = compute_discounted_rewards(reward_vector, transition_matrices, policy, discount_factors)

# Print discounted rewards
print("Long-term Discounted Rewards:")
for gamma in discount_factors:
    print(f"Gamma = {gamma}:")
    for state, reward in enumerate(discounted_rewards[gamma]):
        print(f"  State S{state}: {reward:.4f}")

# Plot results
fig, ax1 = plt.subplots()

# Plot iterations
ax1.set_ylabel('Discount Factor (gamma)')
ax1.set_xlabel('Number of Iterations')
ax1.plot([iterations[gamma] for gamma in discount_factors], discount_factors, marker='o', color='tab:blue', label='Iterations')
ax1.tick_params(axis='x', labelcolor='tab:blue')
ax1.legend(loc='upper left')

# Plot discounted rewards
ax2 = ax1.twiny()
ax2.set_xlabel('Discounted Reward')
for state in range(len(reward_vector)):
    ax2.plot([discounted_rewards[gamma][state] for gamma in discount_factors], discount_factors, marker='x', label=f'Reward S{state}')
ax2.legend(loc='upper right')

plt.title('Discount Factor vs Iterations and Discounted Rewards')
plt.show()
