import sys

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
import ast
from schemas import PlanetSystem
from threading import Thread
from multiprocessing import Queue, Process

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=50, height=60, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(121)
        self.ax_3d = fig.add_subplot(122, projection='3d')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, m, x, y, v_x, v_y, total_time: int, step: int, schema_type: int, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setFixedWidth(QApplication.desktop().availableGeometry().width())
        self.setFixedHeight(QApplication.desktop().availableGeometry().height())

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.canvas = MplCanvas(self, width=50, height=40, dpi=100)
        self.mass = np.copy(m)
        self.x = np.copy(x)
        self.y = np.copy(y)
        self.v_x = np.copy(v_x)
        self.v_y = np.copy(v_y)
        self.total_time = total_time
        self.time_step = step
        self.schema_type = schema_type
        self.schema = PlanetSystem(self.mass, self.x, self.y, self.v_x, self.v_y,
                                   self.total_time, self.time_step)
        try:
            if self.schema_type == 1:
                self.xx, self.yy, self.vx, self.vy = self.schema.euler_scheme()
            if self.schema_type == 2:
                self.xx, self.yy, self.vx, self.vy = self.schema.euler_kramer_scheme()
            if self.schema_type == 3:
                self.xx, self.yy, self.vx, self.vy = self.schema.verlet_scheme()
            if self.schema_type == 4:
                self.xx, self.yy, self.vx, self.vy = self.schema.beeman_scheme()
        except Exception as e:
            sys.stdout = open('error.txt', 'w')
            print(e)
            sys.stdout.close()

        sys.stdout = open('output.txt', 'w')
        print([self.vx[-1], self.vy[-1]])
        sys.stdout.close()
        sys.stdout = open('rx.txt', 'w')
        print(self.xx[:, -1].tolist())
        sys.stdout.close()
        sys.stdout = open('ry.txt', 'w')
        print(self.yy[:, -1].tolist())
        sys.stdout.close()

        self.count = 0
        self.x_lim = np.max(np.abs(self.xx))*1.1
        self.y_lim = np.max(np.abs(self.yy))*1.1
        self.x_lim = np.max(np.array([self.x_lim, self.y_lim]))
        self.y_lim = self.x_lim
        self.update_plot(self.xx, self.yy)

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(50)
        #self.timer.timeout.connect(self.update_plot)
        #self.timer.start()

        self.setCentralWidget(self.canvas)

        self.show()

    def update_plot(self, x, y):
        self.canvas.ax.cla()  # Clear the canvas.
        for i in range(len(self.schema.mass)):
            self.canvas.ax.scatter(x[i, :], y[i, :])
        self.canvas.ax.scatter(x[:, -1], y[:, -1], c='black')
        self.canvas.ax.set_xlim([-self.x_lim, self.x_lim])
        self.canvas.ax.set_ylim([-self.y_lim, self.y_lim])
        self.canvas.ax_3d.cla()  # Clear the canvas.
        for i in range(len(self.schema.mass)):
            self.canvas.ax_3d.scatter(x[i, :], y[i, :], 0)
        self.canvas.ax_3d.scatter(x[:, -1], y[:, -1], 0, c='black')
        self.canvas.ax_3d.set_xlim([-self.x_lim, self.x_lim])
        self.canvas.ax_3d.set_ylim([-self.y_lim, self.y_lim])
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mass = np.array(ast.literal_eval(sys.argv[1]), dtype=float)
    x_coord = np.array(ast.literal_eval(sys.argv[2]), dtype=float)
    y_coord = np.array(ast.literal_eval(sys.argv[3]), dtype=float)
    v_x_coord = np.array(ast.literal_eval(sys.argv[4]), dtype=float)
    v_y_coord = np.array(ast.literal_eval(sys.argv[5]), dtype=float)
    time = int(sys.argv[6])
    time_step = int(sys.argv[7])
    scheme_type = int(sys.argv[8])
    w = MainWindow(mass, x_coord, y_coord, v_x_coord, v_y_coord, time, time_step, scheme_type)
    app.exec_()
