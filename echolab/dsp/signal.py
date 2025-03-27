import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, data: np.ndarray, sample_rate: int):
        if data.ndim != 1:
            raise ValueError("Signal data must be 1D (mono) for now")

        self.data = data.astype(np.float32)
        self.samples = len(data)
        self.sample_rate = sample_rate
        self.duration = self.samples / sample_rate
        self.time = np.linspace(0, self.duration, self.samples, endpoint=False)

    def plot(self, title="Waveform", start_time=0.0, end_time=None):
        """Plot signal between start and end time in seconds."""
        end_time = end_time or self.duration
        idx_start = int(start_time * self.sample_rate)
        idx_end = int(end_time * self.sample_rate)

        t = self.time[idx_start:idx_end]
        y = self.data[idx_start:idx_end]

        plt.figure(figsize=(10, 4))
        plt.plot(t, y)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def normalize(self, target_peak=1.0):
        """Scale signal so its max absolute amplitude is target_peak."""
        max_val = np.max(np.abs(self.data))
        if max_val > 0:
            self.data *= (target_peak / max_val)
        return self

    def copy(self):
        return Signal(np.copy(self.data), self.sample_rate)