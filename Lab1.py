import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from pyqtgraph import PlotWidget
#import plotting as pl
#import main as mn
import numpy as np
import ast
from threading import Thread
from threading import Event
import time

close = False
p = QtCore.QProcess()

def add_planet():
    form.tableWidget.insertRow(1)


def delete_planet():
    if (form.tableWidget.rowCount()>1):
        form.tableWidget.removeRow(form.tableWidget.rowCount()-1)


def get_column(n, s):
    global form
    res = np.zeros(s)
    for i in range(s):
        res[i] = float(form.tableWidget.item(i, n).text())
    return res


def draw():
    global form
    close = False
    s = form.tableWidget.rowCount()
    m = get_column(4, s)
    x = get_column(0, s)
    y = get_column(1, s)
    v_x = get_column(2, s)
    v_y = get_column(3, s)
    total_time = int(form.lineEdit_2.text())
    step = int(form.lineEdit.text())
    schema_type = 1
    if form.radioButton_2.isChecked():
        schema_type = 3
    if form.radioButton_3.isChecked():
        schema_type = 2
    if form.radioButton_4.isChecked():
        schema_type = 4
    #th = Thread(target=pl.start_plotting, args=(m, x, y, v_x, v_y, total_time, step, schema_type))
    #th.start()
    th = Thread(target=run, args=(m, x, y, v_x, v_y, total_time, step, schema_type))
    th.start()
    th.join()


    #pl.start_plotting(m, x, y, v_x, v_y, total_time, step, schema_type)


def run(m, x, y, v_x, v_y, total_time, step, schema_type):
    global p
    global form
    script_file = QtCore.QCoreApplication.applicationDirPath() + r'/main.py'
    p.start('python',
            [r'C:/Users/79372/PycharmProjects/MathModellingLab/main.py', str(m.tolist()), str(x.tolist()),
             str(y.tolist()), str(v_x.tolist()), str(v_y.tolist()),
             str(total_time), str(step), str(schema_type)])
    print(p.pid())
    p.waitForFinished(30000)
    print(p.pid())
    with open('output.txt', 'r') as outfile, open('rx.txt', 'r') as rxout, open('ry.txt', 'r') as ryout:
        res = np.array(ast.literal_eval(outfile.read()), dtype=float)
        vx = res[0]
        vy = res[1]
        xx = np.array(ast.literal_eval(rxout.read()), dtype=float)
        yy = np.array(ast.literal_eval(ryout.read()), dtype=float)
        form.lineEdit_4.setText(str(total_time))
        form.lineEdit_5.setText(str(vx))
        form.lineEdit_6.setText(str(vy))
        kinetic = np.sum(m[1:])*(vx**2+vy**2)/2
        rx = xx[1:]-xx[0]
        ry = yy[1:]-yy[0]
        potential = 6.67e-11*(np.sum(m[1:]/(rx**2+ry**2)**0.5))*m[0]
        energy = kinetic - potential
        form.lineEdit_3.setText(str(energy))


Form, Window = uic.loadUiType('interface.ui')
app = QApplication(sys.argv)
window = Window()
form = Form()
form.setupUi(window)
form.pushButton.clicked.connect(add_planet)
form.pushButton_2.clicked.connect(delete_planet)
form.pushButton_3.clicked.connect(draw)
window.show()
app.exec_()
