
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from pyqtgraph import PlotWidget

def add_planet():
    form.tableWidget.insertRow(1)

def delete_planet():
    if (form.tableWidget.rowCount()>1):
        form.tableWidget.removeRow(form.tableWidget.rowCount()-1)

def draw():
    print(form.tableWidget.item(2, 2).text())

Form, Window = uic.loadUiType('D:\PythonProjects\\MathModellingLab\interface.ui')
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.pushButton.clicked.connect(add_planet)
form.pushButton_2.clicked.connect(delete_planet)
form.pushButton_3.clicked.connect(draw)
window.show()
app.exec_()
