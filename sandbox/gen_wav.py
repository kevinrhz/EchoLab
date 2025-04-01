import numpy as np
import matplotlib.pyplot as plt

rate = 40
duration = 1  # seconds
freq = 20

t = np.linspace(0, duration, int(rate * duration), endpoint=False)
y = 0.5 * np.sin(2 * np.pi * freq * t)

plt.plot(t, y)
plt.title("Custom Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
