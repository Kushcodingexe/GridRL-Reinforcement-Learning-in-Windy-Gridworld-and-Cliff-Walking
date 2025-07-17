import numpy as np
import random
import json
from collections import defaultdict

# Define states and actions
states = ["S1", "S2", "S3", "S4", "S5"]
actions = ["a1", "a2", "a3", "a4", "a5", "a6"]

# Function to generate dataset
def generate_samples(num_samples):
    dataset = []
    for _ in range(num_samples):
        state = random.choice(states)
        action = random.choice(actions)
        next_state = random.choice(states)  # Random transition
        dataset.append((state, action, next_state))
    return dataset

# Function to compute transition probability matrix
def compute_transition_matrix(dataset):
    transition_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    
    for state, action, next_state in dataset:
        transition_counts[state][action][next_state] += 1
    
    transition_matrix = {}
    for state in transition_counts:
        transition_matrix[state] = {}
        for action in transition_counts[state]:
            total = sum(transition_counts[state][action].values())
            transition_matrix[state][action] = {
                next_state: round(count / total, 3)  # Round for better readability
                for next_state, count in transition_counts[state][action].items()
            }
    
    return transition_matrix

# Function to compute value function V(S1)
def compute_value_function(transition_matrix, gamma=0.9, iterations=100):
    V = {state: 0 for state in states}  # Initialize value function
    for _ in range(iterations):
        new_V = V.copy()
        for state in states:
            max_value = 0
            for action in transition_matrix.get(state, {}):
                expected_value = sum(
                    prob * (1 + gamma * V[next_state])
                    for next_state, prob in transition_matrix[state][action].items()
                )
                max_value = max(max_value, expected_value)
            new_V[state] = round(max_value, 2)  # Round for readability
        V = new_V
    return V["S1"]

# Generate datasets
samples_1000 = generate_samples(1000)
samples_100000 = generate_samples(100000)

# Compute transition probability matrices
trans_matrix_1000 = compute_transition_matrix(samples_1000)
trans_matrix_100000 = compute_transition_matrix(samples_100000)

# Compute value function V(S1) for both sample sizes
V_S1_1000 = compute_value_function(trans_matrix_1000)
V_S1_100000 = compute_value_function(trans_matrix_100000)

# Print results in a formatted way
def print_formatted_output():
    print("Transition Matrix for 1000 samples:")
    print(json.dumps(trans_matrix_1000, indent=4))
    print("\nTransition Matrix for 100000 samples:")
    print(json.dumps(trans_matrix_100000, indent=4))
    print(f"\nValue Function V(S1) for 1000 samples: {V_S1_1000}")
    print(f"Value Function V(S1) for 100000 samples: {V_S1_100000}")

# Execute the print function
print_formatted_output()
