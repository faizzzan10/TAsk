import matplotlib.pyplot as plt

# Sample data
x = range(10)
y1 = [i**2 for i in x]
y2 = [i*3 for i in x]

# Create figure and primary y-axis
fig, ax1 = plt.subplots()

# Plot first data set on primary y-axis
ax1.plot(x, y1, color='b', label='Data 1')
ax1.set_ylabel('Y-axis 1 (squared)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create secondary y-axis
ax2 = ax1.twinx()

# Plot second data set on secondary y-axis
ax2.plot(x, y2, color='r', label='Data 2')
ax2.set_ylabel('Y-axis 2 (tripled)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set x-axis label
plt.xlabel('X-axis')

# Adjust layout and display legend
plt.tight_layout()
plt.legend()
plt.show()
