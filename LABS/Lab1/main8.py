import numpy as np
import matplotlib.pyplot as plt

# Experiment settings
n_bandits = 2000    # Number of independent bandit tasks
n_actions = 20      # 20-armed bandit
n_steps = 1000      # Number of time steps per bandit

# Parameters for methods
epsilon_high = 0.1  # epsilon for epsilon-greedy (0.1)
epsilon_low = 0.01  # epsilon for epsilon-greedy (0.01)
init_zero = 0.0     # initial Q-value = 0
init_optimistic = 40.0  # optimistic initial value

def run_bandit(method, init_value, epsilon=0.0):
    """
    Run one bandit task.
    method: 'epsilon-greedy' or 'greedy'
    init_value: initial estimate for each arm
    epsilon: exploration probability (ignored for greedy method)
    Returns an array of rewards for each time step.
    """
    # Generate deterministic true rewards for each of the 20 arms from Uniform(0,20)
    true_rewards = np.random.uniform(0, 20, n_actions)
    
    # Initialize estimated values and counts
    Q_estimates = np.full(n_actions, init_value)
    action_counts = np.zeros(n_actions)
    
    rewards = np.zeros(n_steps)
    
    for t in range(n_steps):
        if method == "epsilon-greedy":
            if np.random.rand() < epsilon:
                # Explore: choose a random arm
                action = np.random.randint(n_actions)
            else:
                # Exploit: choose the arm with the highest estimated value
                max_est = np.max(Q_estimates)
                # In case of ties, choose randomly among them
                candidates = np.where(Q_estimates == max_est)[0]
                action = np.random.choice(candidates)
        elif method == "greedy":
            # Always choose the best estimated action (no exploration)
            max_est = np.max(Q_estimates)
            candidates = np.where(Q_estimates == max_est)[0]
            action = np.random.choice(candidates)
        else:
            raise ValueError("Method must be either 'epsilon-greedy' or 'greedy'.")
        
        # Since rewards are deterministic, the observed reward is the true reward of the chosen arm.
        reward = true_rewards[action]
        rewards[t] = reward
        
        # Incremental update of Q_estimates (sample-average update)
        action_counts[action] += 1
        Q_estimates[action] += (reward - Q_estimates[action]) / action_counts[action]
    
    return rewards

# Containers for average rewards (over all bandit tasks) for each method
avg_rewards = {
    "eps_0.1": np.zeros(n_steps),
    "eps_0.01": np.zeros(n_steps),
    "greedy_zero": np.zeros(n_steps),
    "greedy_optimistic": np.zeros(n_steps)
}

# Run simulation for each bandit task and accumulate rewards for each method
for _ in range(n_bandits):
    avg_rewards["eps_0.1"] += run_bandit("epsilon-greedy", init_zero, epsilon=epsilon_high)
    avg_rewards["eps_0.01"] += run_bandit("epsilon-greedy", init_zero, epsilon=epsilon_low)
    avg_rewards["greedy_zero"] += run_bandit("greedy", init_zero)
    avg_rewards["greedy_optimistic"] += run_bandit("greedy", init_optimistic)

# Average over the number of bandit tasks
for key in avg_rewards:
    avg_rewards[key] /= n_bandits

# Plot the average rewards over time
plt.figure(figsize=(12, 8))
plt.plot(avg_rewards["eps_0.1"], label="ε-greedy (ε=0.1, init=0)")
plt.plot(avg_rewards["eps_0.01"], label="ε-greedy (ε=0.01, init=0)")
plt.plot(avg_rewards["greedy_zero"], label="Greedy (init=0)")
plt.plot(avg_rewards["greedy_optimistic"], label="Greedy (optimistic init=40)")
plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.title("20-Armed Bandit: Average Reward over Time")
plt.legend()
plt.grid(True)
plt.show()
