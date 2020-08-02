import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.pyplot as plt
# Create app
app = QtWidgets.QApplication(sys.argv)

#init
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#hook logic
def dihtomia():
    l_wall = int(ui.lineEdit_4.text())
    r_wall = int(ui.lineEdit.text())
    a = float(ui.lineEdit_3.text())
    exp = float(ui.lineEdit_2.text())
    iter=0
    e=math.exp(1)
    while abs(l_wall-r_wall)>exp:
        deli = (l_wall+r_wall)/2
        if (3*deli-a*e**deli>0 and 3*l_wall-a*e**l_wall>0) or (3*deli-a*e**deli<0 and 3*l_wall-a*e**l_wall<0):
            iter+=1
            l_wall=deli
            x = l_wall
            print(x)
            ui.label_6.setText(f'Иксы:{x}')
        else:
            iter+=1
            r_wall=deli
            x = r_wall
            print(x)
            ui.label_6.setText(f'Икс для дихтомии:{x}')
    ui.label_5.setText(f'Итерации: {iter}')
ui.pushButton.clicked.connect(dihtomia)

#          3*x-a*e**x=0
def horda():
    e = math.exp(1)
    A=float(ui.lineEdit_3.text())
    a=int(ui.lineEdit_4.text())
    b=int(ui.lineEdit.text())
    exp=float(ui.lineEdit_2.text())
    fa= 3*a-A*e**a
    fb=3*b-A*e**b
    xo=float(ui.lineEdit_5.text())
    iter=0
    x = 0
    while abs(x-xo)>exp:
        if fb*(-1*a*e**x)>0:
            x = xo - ((b-xo)*(3*xo-A*e**xo))/(fb-(3*xo-a*e**xo))
            if (3*x-A*e**x>0 and 3*a-A*a**x<0) or (3*x-A*e**x<0 and 3*a-A*a**x>0):
                iter+=1
                a = x
                xo = a
                print(xo)
                ui.label_7.setText(f'Икс для хорд: {xo}')
            else:
                iter+=1
                b = x
                xo = b
                print(xo)
                ui.label_7.setText(f'Икс для хорд: {xo}')
        else:
            x = xo - ((xo-a)*(3*xo-A*e**xo))/((3*xo-A*e**xo)-fa)
            if (3*x-A*e**x>0 and 3*a-A*a**x<0) or (3*x-A*e**x<0 and 3*a-A*a**x>0):
                iter+=1
                a = x
                xo = a
                print(xo)
                ui.label_7.setText(f'Икс для хорд: {xo}')
            else:
                iter+=1
                b = x
                xo = b
                print(xo)
                ui.label_7.setText(f'Икс для хорд: {xo}')

ui.pushButton_2.clicked.connect(horda)


def kasatel():
    e=math.exp(1)
    A=float(ui.lineEdit_3.text())
    x0=float(ui.lineEdit_5.text())
    exp=float(ui.lineEdit_2.text())
    fx0= 3*x0-A*e**x0
    xp=3 - A*e**x0# производная
    iter=0
    x1 = x0 - fx0/xp
    while abs(x1 - x0)<exp:
        fx0 = 3*x0-A*e**x0
        xp =3 - A*e**x0
        x1 = x0 - fx0/xp
        x0 = x1
        print(x1)
    ui.label_8.setText(f'икс для ньютона: {x1}')

ui.pushButton_3.clicked.connect(kasatel)

#0 = 3*x - A*exp**x
#x = A*exp**x/3

def iteracia():
    e=math.exp(1)
    A=float(ui.lineEdit_3.text())
    x0 = float(ui.lineEdit_6.text())
    exp = float(ui.lineEdit_2.text())
    a = int(ui.lineEdit_4.text())
    b = int(ui.lineEdit.text())
    y = (A*e**x0)/3
    fpy = (A*e**x0)/3
    while abs(y-x0)>e:
        y = (A*e**x0)/3
        x0 = y
    else:
        print('не работает')
    ui.label_9.setText(f'икс для итераций: {x0}')

ui.pushButton_4.clicked.connect(iteracia)

#Main Loop
sys.exit(app.exec_())
