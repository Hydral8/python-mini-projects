import matplotlib.pyplot as plt
import numpy as np

PI = np.pi

x = np.arange(0, 2 * PI, 0.1)
sin = np.sin(x)
cos = np.cos(x)

plt.plot(x, sin, 'r', x, cos, 'b')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
