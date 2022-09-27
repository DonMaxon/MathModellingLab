
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from pyqtgraph import PlotWidget
import plotting as pl
import numpy as np
from threading import Thread


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
    th = Thread(target=pl.start_plotting, args=(m, x, y, v_x, v_y, total_time, step, schema_type))
    th.start()
    #pl.start_plotting(m, x, y, v_x, v_y, total_time, step, schema_type)


Form, Window = uic.loadUiType('interface.ui')
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.pushButton.clicked.connect(add_planet)
form.pushButton_2.clicked.connect(delete_planet)
form.pushButton_3.clicked.connect(draw)
window.show()
app.exec_()
