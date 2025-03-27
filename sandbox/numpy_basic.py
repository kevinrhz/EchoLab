import numpy as np

# 🎧 1D signal: mono audio (1 channel)
signal = np.array([0.0, 0.5, -0.75, 1.0, 0.75])
print("Signal:", signal)
print("Shape:", signal.shape)
print("Dimensions (ndim):", signal.ndim)

# 🎛 2D signal: stereo audio (2 channels)
stereo = np.array([
    [0.0,  0.0],   # left, right
    [0.5,  0.2],
    [-0.7, -0.3],
    [1.0,  0.4],
])
print("\nStereo:", stereo)
print("Shape:", stereo.shape)  # 4 samples x 2 channels
print("Access left channel:", stereo[:, 0])
print("Access right channel:", stereo[:, 1])
print("Access sample 2, right channel:", stereo[2, 1])
