import os

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QLabel
)
from PyQt6.QtGui import QAction
import sys
from echolab.dsp.wav_reader import load_wav
from echolab.dsp.signal import Signal


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EchoLab")
        self.setMinimumSize(800, 600)

        # Main widget + layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_action = QAction("Open WAV", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        self.signal = None

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open WAV file", "", "WAV files (*.wav)")
        if not path:
            return

        try:
            self.signal = load_wav(path)
            QMessageBox.information(self, "Success", f"Loaded: {path}\nSample rate: {self.signal.sample_rate} Hz")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())