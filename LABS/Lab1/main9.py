import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_bandits = 500        # Number of bandits
n_arms = 10            # Number of arms (10-armed bandit)
n_steps = 1000         # Time steps per bandit
c_values = [1, 2, 3, 4]  # Confidence levels
init_val = 0.0         # Initial Q-values

def run_ucb_bandit(c, init_val):
    rewards = np.zeros((n_bandits, n_steps))

    for b in range(n_bandits):
        q_true = np.random.normal(0, 1, n_arms)          # True action values
        q_est = np.full(n_arms, init_val, dtype=float)   # Estimated values
        action_counts = np.zeros(n_arms)                 # Count of actions

        for t in range(1, n_steps + 1):
            # Compute UCB values
            ucb_values = q_est + c * np.sqrt(np.log(t + 1) / (action_counts + 1e-5))
            action = np.argmax(ucb_values)

            # Sample reward with noise
            reward = np.random.normal(q_true[action], 1)

            # Update counts and Q-values
            action_counts[action] += 1
            q_est[action] += (reward - q_est[action]) / action_counts[action]

            rewards[b, t - 1] = reward

    return rewards.mean(axis=0)

# Run simulation for different c values
ucb_results = {}
for c in c_values:
    ucb_results[c] = run_ucb_bandit(c, init_val)

# Plotting results
plt.figure(figsize=(10, 6))
for c, avg_rewards in ucb_results.items():
    plt.plot(avg_rewards, label=f'UCB c={c}')

plt.title("UCB on 10-Armed Bandit (Initial Q=0, 500 Bandits)")
plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
