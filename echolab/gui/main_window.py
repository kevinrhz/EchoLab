from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QLabel, QDoubleSpinBox, QHBoxLayout
)
from PyQt6.QtGui import QAction
import pyqtgraph as pg
import os
import sys
from echolab.dsp.wav_reader import load_wav
from echolab.dsp.signal import Signal
from echolab.gui.signal_viewer import SignalViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EchoLab")
        self.setMinimumSize(800, 600)

        # Main widget + layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Plot widget
        self.viewer = SignalViewer()
        self.layout.addWidget(self.viewer)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_action = QAction("Open WAV", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # SIDEBAR
        self.sidebar = QVBoxLayout()
        self.sidebar.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Time Range Controls
        self.start_spin = QDoubleSpinBox()
        self.start_spin.setPrefix("Start: ")
        self.start_spin.setSuffix(" s")
        self.start_spin.setSingleStep(0.1)
        self.start_spin.setDecimals(3)

        self.end_spin = QDoubleSpinBox()
        self.end_spin.setPrefix("End: ")
        self.end_spin.setSuffix(" s")
        self.end_spin.setSingleStep(0.1)
        self.end_spin.setDecimals(3)

        self.sidebar.addWidget(self.start_spin)
        self.sidebar.addWidget(self.end_spin)
        self.start_spin.setEnabled(False)
        self.end_spin.setEnabled(False)

        # auto update plot when stat/end times change
        self.start_spin.valueChanged.connect(self.plot_range)
        self.end_spin.valueChanged.connect(self.plot_range)

        # Reset view button
        self.reset_button = QPushButton("Reset View")
        self.reset_button.clicked.connect(self.reset_view)
        self.sidebar.addWidget(self.reset_button)
        self.reset_button.setEnabled(False)

        # Main viewer stays the same
        self.layout.addLayout(self.sidebar, 1)
        self.layout.addWidget(self.viewer, 4)


        self.signal = None


    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open WAV file", "", "WAV files (*.wav)")
        if not path:
            return

        try:
            self.signal = load_wav(path)
            self.viewer.update_signal(self.signal)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        self.start_spin.setEnabled(True)
        self.end_spin.setEnabled(True)
        self.end_spin.setMaximum(self.signal.duration)
        self.start_spin.setMaximum(self.signal.duration)

        self.reset_button.setEnabled(True)



    def plot_range(self):
        if not self.signal:
            return

        start = self.start_spin.value()
        end = self.end_spin.value()

        if start >= end or end > self.signal.duration:
            QMessageBox.critical(self, "Invalid Range", "Start must be less than end time AND within signal duration.")
            return

        self.viewer.update_signal(self.signal, start_time=start, end_time=end)


    def reset_view(self):
        if self.signal:
            self.start_spin.blockSignals(True)
            self.end_spin.blockSignals(True)

            self.start_spin.setValue(0.0)
            self.end_spin.setValue(self.signal.duration)
            self.viewer.update_signal(self.signal)

            self.start_spin.blockSignals(False)
            self.end_spin.blockSignals(False)