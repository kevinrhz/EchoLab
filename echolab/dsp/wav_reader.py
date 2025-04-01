import numpy as np
from pathlib import Path
from scipy.io import wavfile
from echolab.dsp.signal import Signal

def load_wav(path: str | Path) -> Signal:
    """Load a WAV file and return a Signal object"""
    path = Path(path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"WAV file not found: {path}")

    sample_rate, data = wavfile.read(path)

    if data.ndim > 1:
        data = data[:, 0]
        print("Stereo detected - using only channel 0")

    return Signal(data, sample_rate)