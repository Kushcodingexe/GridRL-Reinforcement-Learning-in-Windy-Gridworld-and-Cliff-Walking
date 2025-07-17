import numpy as np
import matplotlib.pyplot as plt

# Grid configuration
ROWS, COLS = 7, 10
START = (3, 0)
GOAL = (3, 7)
WIND = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def transition(state, move_index):
    r, c = state
    dr, dc = MOVES[move_index]
    wind_push = WIND[c]
    new_r = max(0, min(ROWS - 1, r + dr - wind_push))
    new_c = max(0, min(COLS - 1, c + dc))
    return (new_r, new_c), -1, (new_r, new_c) == GOAL

def choose_action(Q, state, eps):
    if np.random.rand() < eps:
        return np.random.randint(len(MOVES))
    values = [Q.get((state, a), 0) for a in range(len(MOVES))]
    max_val = max(values)
    best = [a for a, v in enumerate(values) if v == max_val]
    return np.random.choice(best)

def sarsa_learn(episodes, lr, discount, eps):
    Q = {}
    total_steps = 0
    for ep in range(episodes):
        s = START
        a = choose_action(Q, s, eps)
        done = False
        while not done:
            next_s, reward, done = transition(s, a)
            next_a = choose_action(Q, next_s, eps)
            current = Q.get((s, a), 0)
            future = Q.get((next_s, next_a), 0)
            Q[(s, a)] = current + lr * (reward + discount * future - current)
            s, a = next_s, next_a
            total_steps += 1
    return Q, total_steps

def trace_optimal_route(Q):
    route = [START]
    s = START
    visited = set()
    while s != GOAL and len(route) < 100:
        visited.add(s)
        q_vals = [Q.get((s, a), float('-inf')) for a in range(len(MOVES))]
        best_a = [a for a, val in enumerate(q_vals) if val == max(q_vals)]
        if not best_a:
            break
        a = np.random.choice(best_a)
        next_s, _, _ = transition(s, a)
        if next_s in visited:
            break
        route.append(next_s)
        s = next_s
    return route

def display_route(route):
    plt.figure(figsize=(12, 8))
    for r in range(ROWS + 1):
        plt.axhline(r - 0.5, color='orange', linewidth=0.5)
    for c in range(COLS + 1):
        plt.axvline(c - 0.5, color='orange', linewidth=0.5)

    plt.plot(START[1], START[0], 'go', markersize=12, label='Start')
    plt.plot(GOAL[1], GOAL[0], 'ro', markersize=12, label='Goal')

    r_coords = [s[0] for s in route]
    c_coords = [s[1] for s in route]
    plt.plot(c_coords, r_coords, 'b-', linewidth=2, label=f'Path ({len(route) - 1} steps)')
    plt.scatter(c_coords, r_coords, c='blue', s=10)

    plt.title("Windy Grid World - SARSA Path")
    plt.legend(loc='upper right')
    plt.xlim(-0.5, COLS - 0.5)
    plt.ylim(ROWS - 0.5, -0.5)
    plt.xticks(range(COLS))
    plt.yticks(range(ROWS))
    plt.gca().set_aspect('equal')
    plt.grid(False)
    plt.show()

def run():
    ep_count = 500
    alpha = 0.4
    gamma = 1.0

    q_eps_01, steps_01 = sarsa_learn(ep_count, alpha, gamma, eps=0.1)
    q_eps_001, steps_001 = sarsa_learn(ep_count, alpha, gamma, eps=0.01)

    print(f"Total steps (ε=0.1): {steps_01 / 1000:.2f}k")
    print(f"Total steps (ε=0.01): {steps_001 / 1000:.2f}k")

    best_q = q_eps_01 if steps_01 < steps_001 else q_eps_001
    path = trace_optimal_route(best_q)

    print(f"Path length: {len(path) - 1}")
    print("Path taken:", path)
    display_route(path)

if __name__ == "__main__":
    run()
