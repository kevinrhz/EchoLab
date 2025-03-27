import numpy as np
import matplotlib.pyplot as plt

rate = 44100
duration = 0.01  # seconds
freq = 440

t = np.linspace(0, duration, int(rate * duration), endpoint=False)
y = 0.5 * np.sin(2 * np.pi * freq * t)

plt.plot(t, y)
plt.title("440 Hz Sine Wave (10 ms)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
