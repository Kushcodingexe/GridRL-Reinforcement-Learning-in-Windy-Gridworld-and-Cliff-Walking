import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Constants
MAX_DEMAND = 99
INITIAL_INVENTORY = 115
ORDER_DELAY = 3  # Order arrives after 3 days
HOLDING_COST_PER_UNIT = 0.75
LOST_SALE_COST_PER_UNIT = 18
ORDER_COST = 75
ALPHA = 0.1  # Learning rate
GAMMA = 0.99  # Discount factor
EPISODES = 5000
MAX_DAYS = 100  # Maximum days per episode

# Policies to simulate
policies = {
    "Policy I": (125, 150),
    "Policy II": (125, 250),
    "Policy III": (150, 250),
    "Policy IV": (175, 250),
    "Policy V": (175, 300),
}

# Demand distribution: Uniform between 0 and 99
def sample_demand():
    return np.random.randint(0, 100)

# TD(0) simulation
def simulate_td(policy_p, policy_q):
    V = defaultdict(float)
    total_costs = []

    for episode in range(EPISODES):
        inventory = INITIAL_INVENTORY
        days_to_arrival = 0
        outstanding_order = 0
        state = (inventory, days_to_arrival)
        total_cost = 0

        for day in range(MAX_DAYS):
            demand = sample_demand()
            sales = min(inventory, demand)
            lost_sales = max(0, demand - inventory)
            inventory -= sales

            # Receive order if it's the arrival day
            if days_to_arrival == 1:
                inventory += outstanding_order
                outstanding_order = 0
                days_to_arrival = 0
            elif days_to_arrival > 1:
                days_to_arrival -= 1

            # Place new order if below reorder point and no outstanding order
            order_cost = 0
            if inventory <= policy_p and days_to_arrival == 0:
                outstanding_order = policy_q
                days_to_arrival = ORDER_DELAY
                order_cost = ORDER_COST

            # Costs
            holding_cost = HOLDING_COST_PER_UNIT * inventory
            lost_sale_cost = LOST_SALE_COST_PER_UNIT * lost_sales
            step_cost = holding_cost + lost_sale_cost + order_cost
            reward = -step_cost
            total_cost += step_cost

            next_state = (inventory, days_to_arrival)
            V[state] += ALPHA * (reward + GAMMA * V[next_state] - V[state])
            state = next_state

            if inventory == 0:
                break

        total_costs.append(total_cost)

    avg_cost = np.mean(total_costs)
    return V, total_costs, avg_cost

# Run simulations for each policy
results = {}
for name, (p, q) in policies.items():
    V, costs, avg = simulate_td(p, q)
    results[name] = {
        "value_function": V,
        "costs": costs,
        "avg_cost": avg
    }

results_summary = {k: v["avg_cost"] for k, v in results.items()}
results_summary_sorted = dict(sorted(results_summary.items(), key=lambda item: item[1]))
print(results_summary_sorted)
