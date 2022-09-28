
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from pyqtgraph import PlotWidget
import plotting as pl
import numpy as np
import os
from threading import Thread
import subprocess
import schemas as sch


def add_planet():
    form.tableWidget.insertRow(1)


def delete_planet():
    if form.tableWidget.rowCount()>1:
        form.tableWidget.removeRow(form.tableWidget.rowCount()-1)


def get_column(n, s):
    global form
    res = np.zeros(s)
    for i in range(s):
        res[i] = float(form.tableWidget.item(i, n).text())
    return res


def draw():
    global form
    global window
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
    #args = str(m) + ' ' + str(x) + ' ' + str(y) + ' ' + str(v_x) + ' ' + str(v_y) + ' ' + str(total_time) + ' ' + str(step) + ' ' + str(schema_type)
    #print(args)
    #os.system("plotting.py " + args)



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(Ui_MainWindow)
        self.canvas = pl.MplCanvas(self, width=50, height=40, dpi=100)
        self.mass = 0
        self.x = 0
        self.y = 0
        self.v_x = 0
        self.v_y = 0
        self.total_time = 0
        self.time_step = 0
        self.schema_type = 0
        self.schema = None
        self.count = 0
        self.x_lim = 0
        self.y_lim = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.update_plot)
        self.setCentralWidget(self.canvas)

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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 480, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 20, 661, 261))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 480, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 480, 191, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 330, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 360, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(140, 390, 151, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 420, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 300, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 300, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 300, 141, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 330, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(750, 330, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 70, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 140, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 210, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 101, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 280, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить планету"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vx"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Vy"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Масса"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "1.2166E30"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "149500000000"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "23297.8704870374"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "6.083E24"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "299000000000"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "16474.0822085901"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", "1.2166E25"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "448500000000"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "13451.0317972361"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("MainWindow", "1.8249E25"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "598000000000"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "11648.9352435187"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("MainWindow", "2.4332E25"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "747500000000"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("MainWindow", "10419.1244280004"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("MainWindow", "3.0415E25"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Удалить планету"))
        self.pushButton_3.setText(_translate("MainWindow", "Нарисовать"))
        self.radioButton.setText(_translate("MainWindow", "Эйлера"))
        self.radioButton_2.setText(_translate("MainWindow", "Верле"))
        self.radioButton_3.setText(_translate("MainWindow", "Эйлера-Крамера"))
        self.radioButton_4.setText(_translate("MainWindow", "Бимана"))
        self.label.setText(_translate("MainWindow", "Схема:"))
        self.label_2.setText(_translate("MainWindow", "Шаг по времени"))
        self.label_3.setText(_translate("MainWindow", "Время моделирования"))
        self.lineEdit.setText(_translate("MainWindow", "3600"))
        self.lineEdit_2.setText(_translate("MainWindow", "31536000"))
        self.label_4.setText(_translate("MainWindow", "Общая энергия"))
        self.label_5.setText(_translate("MainWindow", "Текущее время"))
        self.label_6.setText(_translate("MainWindow", "Центр масс Vx"))
        self.label_7.setText(_translate("MainWindow", "Центр масс Vy"))


#Form, Window = uic.loadUiType('interface.ui')
app = QApplication([])
window = Ui_MainWindow()
#form = Form()
#form.setupUi(window)
#form.pushButton.clicked.connect(add_planet)
#form.pushButton_2.clicked.connect(delete_planet)
#form.pushButton_3.clicked.connect(draw)
window.show()
app.exec_()
