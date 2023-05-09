import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10, 300)
y = np.random.randn(10, 300)

plt.scatter(x, y, label = 'stars', color = 'green')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Graph')

plt.show()
