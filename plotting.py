import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication

import schemas as s
from threading import Thread
from multiprocessing import Queue, Process

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(121)
        self.ax_3d = fig.add_subplot(122, projection='3d')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, m, x, y, v_x, v_y, total_time: int, step: int, schema_type: int, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        #self.queue = Queue(1)
        self.canvas = MplCanvas(self, width=50, height=40, dpi=100)
        self.mass = np.copy(m)
        self.x = np.copy(x)
        self.y = np.copy(y)
        self.v_x = np.copy(v_x)
        self.v_y = np.copy(v_y)
        self.total_time = total_time
        self.time_step = step
        self.schema_type = schema_type
        self.schema = s.PlanetSystem(self.mass, self.x, self.y, self.v_x, self.v_y,
                                     self.total_time, self.time_step)
        if self.schema_type == 1:
            xx, yy, vx, vy = self.schema.euler_scheme()
        if self.schema_type == 2:
            xx, yy, vx, vy = self.schema.euler_kramer_scheme()
        if self.schema_type == 3:
            xx, yy, vx, vy = self.schema.verlet_scheme()
        if self.schema_type == 4:
            xx, yy, vx, vy = self.schema.beeman_scheme()

        self.count = 0
        self.x_lim = np.max(np.abs(xx))*1.1
        self.y_lim = np.max(np.abs(yy))*1.1
        self.update_plot(xx, yy, vx, vy)

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.setCentralWidget(self.canvas)

        self.show()

    def update_plot(self, x, y, v_x, v_y):
        self.canvas.ax.cla()  # Clear the canvas.
        for i in range(len(self.schema.mass)):
            self.canvas.ax.scatter(x[i, self.count], y[i, self.count])
        self.canvas.ax.set_xlim([-self.x_lim, self.x_lim])
        self.canvas.ax.set_ylim([-self.y_lim, self.y_lim])
        self.canvas.ax_3d.cla()  # Clear the canvas.
        for i in range(len(self.schema.mass)):
            self.canvas.ax_3d.scatter(x[i, self.count], y[i, self.count], 0)
        self.canvas.ax_3d.set_xlim([-self.x_lim, self.x_lim])
        self.canvas.ax_3d.set_ylim([-self.y_lim, self.y_lim])
        if self.count == self.schema.n:
            self.timer.stop()
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


if __name__ == '__plotting__':
    app = QtWidgets.QApplication(sys.argv)
    sys.stdout = open('file.txt', 'w')
    print(sys.argv)
    sys.stdout.close()
    #w = MainWindow(sys.)
    app.exec_()
