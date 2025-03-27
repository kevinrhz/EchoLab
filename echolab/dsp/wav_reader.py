import numpy as np
from scipy.io import wavfile

def load_wav(path: str):
    """Load a WAV file and return (time, data, sample_rate)"""
    sample_rate, data = wavfile.read(path)
    