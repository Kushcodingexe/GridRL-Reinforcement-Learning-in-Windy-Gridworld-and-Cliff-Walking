import numpy as np
import matplotlib.pyplot as plt

def simulate_pursuit(trials=10000):
    capture_times = []
    
    for _ in range(trials):
        fighter_pos = np.array([0, 50], dtype=float)  # Convert to float
        bomber_pos = np.array([70, 0], dtype=float)  # Convert to float

        time = 0
        
        while np.linalg.norm(fighter_pos - bomber_pos) >= 20:
            fighter_speed = np.random.uniform(10, 100)
            bomber_speed = np.random.uniform(10, 50)
            
            # Compute unit direction vector from fighter to bomber
            direction = (bomber_pos - fighter_pos).astype(float)  # Convert to float
            direction /= np.linalg.norm(direction)  
  
            

            # Update positions
            fighter_pos += direction * fighter_speed
            bomber_pos += np.random.uniform(-1, 1, 2) * bomber_speed  # Random movement
            
            time += 1  # Assume time step of 1 second
        
        capture_times.append(time)
    
    return capture_times

# Run simulation
trials = 10000
capture_times = simulate_pursuit(trials)

# Compute and print average time to capture
average_time = np.mean(capture_times)
print(f"Average time to capture: {average_time:.2f} seconds")

# Plot histogram
plt.hist(capture_times, bins=50, density=True, alpha=0.6, color='b')
plt.xlabel('Time to Capture (s)')
plt.ylabel('Probability Density')
plt.title('Distribution of Time to Capture')
plt.show()
