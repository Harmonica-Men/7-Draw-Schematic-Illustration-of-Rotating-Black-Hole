import math
import matplotlib.pyplot as plt

theta = 0.0
x_vals = []
y_vals = []

# Compute ellipsoidal static limit shell
while theta < 6.28:
    x = math.cos(theta)
    y = 0.7 * math.sin(theta)
    x_vals.append(x)
    y_vals.append(y)
    theta += 0.05

plt.plot(x_vals, y_vals, label='Ellipsoidal Static Limit Shell')

# Compute outer event horizon
x_vals.clear()
y_vals.clear()
theta = 0.0
while theta < 6.28:
    x = 0.7 * math.cos(theta)
    y = 0.7 * math.sin(theta)
    x_vals.append(x)
    y_vals.append(y)
    theta += 0.05

plt.plot(x_vals, y_vals, label='Outer Event Horizon')

# Compute inner event horizon
x_vals.clear()
y_vals.clear()
theta = 0.0
while theta < 6.28:
    x = 0.3 * math.cos(theta)
    y = 0.3 * math.sin(theta)
    x_vals.append(x)
    y_vals.append(y)
    theta += 0.05

plt.plot(x_vals, y_vals, label='Inner Event Horizon')

# Compute ring singularity
x_vals.clear()
y_vals.clear()
theta = 0.0
while theta < 6.28:
    x = 0.1 * math.cos(theta)
    y = 0.05 * math.sin(theta)
    x_vals.append(x)
    y_vals.append(y)
    theta += 0.05

plt.plot(x_vals, y_vals, label='Ring Singularity')

# Draw axis of rotation
plt.axhline(y=1, color='black', linestyle='--', label='Axis of Rotation')
plt.axhline(y=-1, color='black', linestyle='--')

plt.title('Schematic Illustration of Rotating Black Hole (Cross-Section)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
