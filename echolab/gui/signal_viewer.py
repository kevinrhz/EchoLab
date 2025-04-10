from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg


class SignalViewer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.plot_widget = pg.PlotWidget(title="Waveform")
        self.plot_widget.setLabel("bottom", "Time", "s")
        self.plot_widget.setLabel("left", "Amplitude")
        self.plot_widget.setMouseEnabled(x=False, y=False)
        self.plot = self.plot_widget.plot()

        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def update_signal(self, signal, start_time=0.0, end_time=None):
        end_time = end_time or signal.duration
        sample_rate = signal.sample_rate

        start_idx = int(start_time * sample_rate)
        end_idx = int(end_time * sample_rate)

        t = signal.time[start_idx:end_idx]
        y = signal.data[start_idx:end_idx]

        decimation = max(1, len(signal.data) // 2000)
        self.plot.setData(t[::decimation], y[::decimation])