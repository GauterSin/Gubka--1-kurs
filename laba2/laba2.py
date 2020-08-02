import math
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_MainWindow
import sys


# create app
app = QtWidgets.QApplication(sys.argv)

#init
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#hook logic
def yakobi():
    x = float(ui.lineEdit_3.text())
    y = float(ui.lineEdit_2.text())
    e = float(ui.lineEdit.text())
    a = float(ui.lineEdit_4.text())
    b = float(ui.lineEdit_5.text())
    x1=0
    y1=0
    e = math.exp(1)
    f1 = math.atan(-1*a*x)/x
    f2 = 1/(e**(y**2-b)**2)
    x1 = 1/(e**(f1**2-b)**2)
    y1 = math.atan(-1*a*f2)/f2
    while abs(y1-f1)>e and abs(x1-f2)>e:
        f1 = y1
        f2 = x1
        y1 = math.atan(-1*a*f2)/f2
        x1 = 1/(e**(f1**2-b)**2)
    ui.label_6.setText(f'Итерации: {x1}')
    ui.label_7.setText(f'Итерации: {y1}')
ui.pushButton.clicked.connect(yakobi)

def gauss():
    x = float(ui.lineEdit_3.text())
    y = float(ui.lineEdit_2.text())
    e = float(ui.lineEdit.text())
    a = float(ui.lineEdit_4.text())
    b = float(ui.lineEdit_5.text())
    x1=0
    y1=0
    e = math.exp(1)
    f1 = math.atan(-1*a*x)/x
    f2 = 1/(e**(y**2-b)**2)
    x1 = 1/(e**(f1**2-b)**2)
    y1 = math.atan(-1*a*f2)/f2
    while abs(f1-y)>e and abs(f2-x)>e:
        f1 = y1
        y1 = math.atan(-1*a*f2)/f2
        f2 = x1
        x1 = 1/(e**(f1**2-b)**2)
    ui.label_8.setText(f'Итерации: {x1}')
    ui.label_9.setText(f'Итерации: {y1}')
ui.pushButton_3.clicked.connect(gauss)




#Main Loop
sys.exit(app.exec_())
