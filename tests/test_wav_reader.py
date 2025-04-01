import unittest
from pathlib import Path
from echolab.dsp.wav_reader import load_wav

class TestWavReader(unittest.TestCase):
    def setUp(self):
        base_dir = Path(__file__).resolve().parents[1]
        self.test_wav_path = base_dir / 'data' / 'sine440hz.wav'

    def test_wav_load(self):
        signal = load_wav(self.test_wav_path)

        self.assertEqual(signal.sample_rate, 44100)
        self.assertGreater(signal.duration, 0.01)
        self.assertEqual(signal.data.ndim, 1)
        self.assertEqual(len(signal.time), len(signal.data))

if __name__ == '__main__':
    unittest.main()