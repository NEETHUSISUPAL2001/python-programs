import numpy as np
import matplotlib.pyplot as plt

# Define a 2x2 matrix dataset
data = np.array([[1, 2],
                 [3, 4]])

# Split the dataset into x and y components
x = data[0, :]  # Take the first row as x
y = data[1, :]  # Take the second row as y

# Create a scatter plot
plt.scatter(x, y, label='Data Points', color='b', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of 2x2 Matrix Dataset')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
