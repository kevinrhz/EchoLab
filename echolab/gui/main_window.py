from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
)
import sys
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EchoLab - Waveform Viewer")

        self.label = Qlabel("Load a .wav file to begin")
        self.button = QPushButton("Open WAV File")
        self.button.clicked.connect(self.open_wav)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)