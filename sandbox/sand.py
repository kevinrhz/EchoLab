import numpy as np
import matplotlib.pyplot as plt

N = 10
x = np.linspace(0, 1, N)

plt.stem(x, np.ones_like(x))
plt.title("10 Points from 0 to 1 using linspace")
plt.xlabel("Time (s)")
plt.ylabel("Sample Value")
plt.grid(True)
plt.show()
