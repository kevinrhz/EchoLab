import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pathlib import Path


# Load a local .wav file
file = Path(__file__).resolve().parents[1] / 'data' / 'sine440hz.wav'
rate, data = wavfile.read(file)

# Print metadata
print(f"Sample rate: {rate}")
print(f"Data Type: {data.dtype}")
print(f"Shape: {data.shape}")

duration = data.shape[0] / rate
print(f"Duration: {duration:.2f} seconds")

# If stereo, use one channel for now
if data.ndim > 1:
    data = data[:, 0]
    print("Stereo detected - using only channel 0")

# Build time axis for first 10 milliseconds
ms10 = int(rate * 0.01)
time = np.linspace(0, 0.01, ms10, endpoint=False)

# Plot first 10ms of audio
plt.plot(time, data[:ms10])
plt.title("Waveform (First 10 ms)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()