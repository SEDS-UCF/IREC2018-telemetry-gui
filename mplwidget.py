# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.pyplot as plt
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')
plt.style.use('dark_background')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.altitude_graph = self.fig.add_subplot(211)

        self.altitude_graph.spines['right'].set_visible(False)
        self.altitude_graph.spines['top'].set_visible(False)

        self.altitude_graph.set_title('Altitude')
        self.altitude_graph.set_xlabel('Time (s)')
        self.altitude_graph.set_ylabel('Altitude (ft)')
        
        self.acceleration_graph = self.fig.add_subplot(212)

        self.acceleration_graph.spines['left'].set_position(('outward', 0))
        self.acceleration_graph.spines['right'].set_visible(False)
        self.acceleration_graph.spines['bottom'].set_position('center')
        self.acceleration_graph.spines['top'].set_visible(False)
        self.acceleration_graph.spines['left'].set_smart_bounds(True)
        self.acceleration_graph.spines['bottom'].set_smart_bounds(True)

        self.acceleration_graph.xaxis.set_ticks_position('bottom')
        self.acceleration_graph.yaxis.set_ticks_position('left')

        self.acceleration_graph.set_xlabel('Time (s)')
        self.acceleration_graph.set_ylabel('Acceleration (m/s^2)')
        self.acceleration_graph.set_title('Acceleration')

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
