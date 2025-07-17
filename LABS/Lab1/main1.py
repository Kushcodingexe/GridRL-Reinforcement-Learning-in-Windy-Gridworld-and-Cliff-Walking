import numpy as np
import matplotlib.pyplot as plt

# Parameters
d = 100  # Distance to target in meters
v = 20   # Velocity in m/s
num_trials = 10000  # Number of simulations

def simulate_1D():
    """ Simulates the 1D random walk process until the object reaches or exceeds distance d. """
    times = []
    for _ in range(num_trials):
        position = 0
        time = 0
        while position < d:
            forward_step = np.random.uniform(1, 10)  # Move forward
            backward_step = np.random.uniform(1, 5)  # Move backward
            position += forward_step - backward_step  # Net movement
            time += (forward_step + backward_step) / v  # Time taken
        times.append(time)
    return np.array(times)

def simulate_2D():
    """ Simulates the 2D random walk process until the object reaches or exceeds distance d. """
    times = []
    for _ in range(num_trials):
        position = np.array([0.0, 0.0])  # (x, y) coordinates
        time = 0
        while np.linalg.norm(position) < d:
            angle = np.random.uniform(0, np.pi)  # Random angle in radians (0 to 180 degrees)
            forward_step = np.random.uniform(1, 10)  # Move forward
            backward_step = np.random.uniform(1, 5)  # Move backward

            # Compute movement in x and y directions
            dx_f = forward_step * np.cos(angle)
            dy_f = forward_step * np.sin(angle)
            dx_b = backward_step * np.cos(angle)
            dy_b = backward_step * np.sin(angle)

            # Update position
            position += np.array([dx_f, dy_f]) - np.array([dx_b, dy_b])
            time += (forward_step + backward_step) / v  # Time taken

        times.append(time)
    return np.array(times)

# Run simulation for 1D
times_1D = simulate_1D()

# Compute CDF
times_1D_sorted = np.sort(times_1D)
cdf_1D = np.arange(1, len(times_1D_sorted) + 1) / len(times_1D_sorted)

# Print mean time for 1D
print(f"Mean time taken in 1D case: {np.mean(times_1D):.2f} seconds")

# Plot CDF
plt.figure(figsize=(8, 5))
plt.plot(times_1D_sorted, cdf_1D, label="1D Case", lw=2)
plt.xlabel("Time (seconds)")
plt.ylabel("Cumulative Probability")
plt.title("CDF of Time to Reach Distance d in 1D Random Walk")
plt.legend()
plt.grid(True)
plt.show()

# Run simulation for 2D
times_2D = simulate_2D()

# Compute CDF
times_2D_sorted = np.sort(times_2D)
cdf_2D = np.arange(1, len(times_2D_sorted) + 1) / len(times_2D_sorted)

# Print mean time for 2D
print(f"Mean time taken in 2D case: {np.mean(times_2D):.2f} seconds")

# Plot CDF
plt.figure(figsize=(8, 5))
plt.plot(times_2D_sorted, cdf_2D, label="2D Case", lw=2, linestyle="dashed")
plt.xlabel("Time (seconds")
plt.ylabel("Cumulative Probability")
plt.title("CDF of Time to Reach Distance d in 2D Random Walk")
plt.legend()
plt.grid(True)
plt.show()
