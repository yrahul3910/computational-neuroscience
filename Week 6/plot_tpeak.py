import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(1, 21)) / 2
y = [0, 5, 13, 15, 15, 18, 21, 24, 25, 27, 29, 30, 31, 31, 33, 33, 34, 34, 35, 36]

plt.plot(x, y)
plt.show()
