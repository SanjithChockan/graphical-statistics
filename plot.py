import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of angles from 0 to 360 inclusive, with an 18-degree interval
angles_deg = np.arange(0, 361, 18)

# Convert angles to radians
angles_rad = np.radians(angles_deg)

# Calculate x and y positions
x_pos = 5 * np.cos(angles_rad)
y_pos = 5 * np.sin(angles_rad)

# Create a table with the data
print("Angle (degrees) | x-position | y-position")
print("-" * 40)
for angle, x, y in zip(angles_deg, x_pos, y_pos):
    print(f"{angle:14.1f} | {x:10.4f} | {y:10.4f}")

# Plot 1: Angle vs x-position
plt.figure(figsize=(10, 6))
plt.scatter(angles_deg, x_pos, color='blue')
plt.plot(angles_deg, x_pos, color='red', linestyle='-')
plt.xlabel('Angle (degrees)')
plt.ylabel('x-position')
plt.title('Angle vs x-position')
plt.grid(True)
plt.savefig('angle_vs_x_position.png')
plt.close()

# Plot 2: Angle vs y-position
plt.figure(figsize=(10, 6))
plt.scatter(angles_deg, y_pos, color='green')
plt.plot(angles_deg, y_pos, color='red', linestyle='-')
plt.xlabel('Angle (degrees)')
plt.ylabel('y-position')
plt.title('Angle vs y-position')
plt.grid(True)
plt.savefig('angle_vs_y_position.png')
plt.close()

# Plot 3: x-position vs y-position
plt.figure(figsize=(10, 6))
plt.scatter(x_pos, y_pos, color='purple')
plt.plot(x_pos, y_pos, color='red', linestyle='-')
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.title('x-position vs y-position')
plt.grid(True)
plt.savefig('x_position_vs_y_position.png')
plt.close()