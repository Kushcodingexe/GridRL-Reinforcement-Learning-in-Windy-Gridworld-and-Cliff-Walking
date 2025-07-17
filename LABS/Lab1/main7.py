import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_bandits = 2000  # Number of bandit tasks+


n_arms = 10       # Number of arms per bandit
n_steps = 1000    # Number of time steps
epsilon = 0.1     # Epsilon for epsilon-greedy

# Function to run the 10-armed testbed experiment
def run_bandit_experiment(initial_Q=0, epsilon=0):
    np.random.seed(42)  # For reproducibility
    
    # True action values (q) for each bandit
    true_q = np.random.randn(n_bandits, n_arms)

    # Estimated values and action counts
    Q = np.full((n_bandits, n_arms), initial_Q, dtype=np.float64)
    action_counts = np.zeros((n_bandits, n_arms), dtype=np.int32)

    rewards = np.zeros(n_steps)

    for t in range(n_steps):
        # Action selection (epsilon-greedy)
        greedy_action = np.argmax(Q, axis=1)  # Greedy choice
        random_action = np.random.randint(0, n_arms, size=n_bandits)  # Random choice

        choose_random = np.random.rand(n_bandits) < epsilon
        actions = np.where(choose_random, random_action, greedy_action)

        # Rewards
        noise = np.random.randn(n_bandits)  # Gaussian noise (0,1)
        rewards_t = true_q[np.arange(n_bandits), actions] + noise

        # Update action-value estimates using sample-average method
        action_counts[np.arange(n_bandits), actions] += 1
        Q[np.arange(n_bandits), actions] += (rewards_t - Q[np.arange(n_bandits), actions]) / action_counts[np.arange(n_bandits), actions]

        # Store average reward at this time step
        rewards[t] = np.mean(rewards_t)

    return rewards

# Run experiments
greedy_zero = run_bandit_experiment(initial_Q=0, epsilon=0)
eps_greedy_zero = run_bandit_experiment(initial_Q=0, epsilon=0.1)
greedy_high = run_bandit_experiment(initial_Q=5, epsilon=0)
eps_greedy_high = run_bandit_experiment(initial_Q=5, epsilon=0.1)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(greedy_zero, label="Greedy (Q=0)", linestyle='--', color='b')
plt.plot(eps_greedy_zero, label="ε-Greedy (Q=0, ε=0.1)", linestyle='-', color='r')
plt.plot(greedy_high, label="Greedy (Q=5)", linestyle='--', color='g')
plt.plot(eps_greedy_high, label="ε-Greedy (Q=5, ε=0.1)", linestyle='-', color='m')

plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.title("10-Armed Bandit: Greedy vs. ε-Greedy with Different Initializations")
plt.legend()
plt.grid(True)
plt.show()
