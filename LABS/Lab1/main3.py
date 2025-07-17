import numpy as np

# Define constants
CARRYING_COST = 75  # USD per unit per day
LOSS_PER_UNIT = 18  # USD (goodwill + lost income)
ORDER_COST = 75     # USD per order
INITIAL_INVENTORY = 115
DAYS_TO_SIMULATE = 365  # Simulate for 1 year
LEAD_TIME = 3  # Days between order placement and arrival
DAILY_DEMAND_RANGE = (0, 99)  # Daily demand (inclusive)

# Define policies (P: reorder point, Q: reorder quantity)
POLICIES = {
    "Policy I": (125, 150),
    "Policy II": (125, 250),
    "Policy III": (150, 250),
    "Policy IV": (175, 250),
    "Policy V": (175, 300)
}

# Function to simulate one policy
def simulate_policy(P, Q):
    inventory = INITIAL_INVENTORY
    order_arrival = None
    total_carrying_cost = 0
    total_loss_cost = 0
    total_order_cost = 0

    for day in range(1, DAYS_TO_SIMULATE + 1):
        # Daily demand
        demand = np.random.randint(DAILY_DEMAND_RANGE[0], DAILY_DEMAND_RANGE[1] + 1)

        # Check if an order arrives
        if order_arrival == day:
            inventory += Q
            order_arrival = None

        # Calculate lost sales
        if demand > inventory:
            lost_sales = demand - inventory
            total_loss_cost += lost_sales * LOSS_PER_UNIT
            inventory = 0
        else:
            inventory -= demand

        # Carrying cost
        total_carrying_cost += inventory * CARRYING_COST

        # Place an order if inventory is at or below the reorder point
        if inventory <= P and order_arrival is None:
            total_order_cost += ORDER_COST
            order_arrival = day + LEAD_TIME

    # Total cost
    total_cost = total_carrying_cost + total_loss_cost + total_order_cost
    return total_cost

# Simulate all policies and compare
results = {}
for policy, (P, Q) in POLICIES.items():
    total_cost = simulate_policy(P, Q)
    results[policy] = total_cost

# Print results
for policy, cost in results.items():
    print(f"{policy}: Total Cost = ${cost:,.2f}")
