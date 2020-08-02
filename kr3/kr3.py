# вариант 28
import random
import math
import numpy
import matplotlib.pyplot as plt
# Переменные
n = 9
delta_x = 0.12
x = []
y = []
sum_x = 0# сумма x
sum_y = 0# сумма y
sum_2x = 0# сумма x**2
pr_xy = 0# сумма x*y
a_f = 0# для прямой
b_f = 0# для прямой

sum_3x = 0# сумма x**3
sum_4x = 0# сумма x**4
sum_5x = 0
sum_6x = 0
sum_7x = 0
sum_8x = 0
pr_y2x = 0
pr_y3x = 0
pr_y4x = 0
# Логика

# Заполнение списоков
for i in range(9):
    if i == 0:
        x.append(0)
        sum_x = sum_x + x[i]
        sum_2x = sum_2x + x[i]**2
        sum_3x = sum_3x + x[i]**3
        sum_4x = sum_4x + x[i]**4
        sum_5x = sum_5x + x[i]**5
        sum_6x = sum_6x + x[i]**6
        sum_7x = sum_7x + x[i]**7
        sum_8x = sum_8x + x[i]**8
        y.append(3*x[i]*(2+math.cos(x[i]**(2+x[i]))))
        sum_y = sum_y + y[i]
        pr_xy = pr_xy + x[i]*y[i]
        pr_y2x = pr_y2x + x[i]**2*y[i]
        pr_y3x = pr_y3x + x[i]**3*y[i]
        pr_y4x = pr_y4x + x[i]**4*y[i]
    else:
        x.append(x[i-1] + delta_x )
        sum_x = sum_x + x[i]
        sum_2x = sum_2x + x[i]**2
        sum_3x = sum_3x + x[i]**3
        sum_4x = sum_4x + x[i]**4
        sum_5x = sum_5x + x[i]**5
        sum_6x = sum_6x + x[i]**6
        sum_7x = sum_7x + x[i]**7
        sum_8x = sum_8x + x[i]**8
        y.append(3*x[i]*(2+math.cos(x[i]**(2+x[i]))))
        sum_y = sum_y + y[i]
        pr_xy = pr_xy + x[i]*y[i]
        pr_y2x = pr_y2x + x[i]**2*y[i]
        pr_y3x = pr_y3x + x[i]**3*y[i]
        pr_y4x = pr_y4x + x[i]**4*y[i]
# 4 порядок
m1_4 = numpy.array([[n,sum_x,sum_2x,sum_3x,sum_4x],[sum_x,sum_2x,sum_3x,sum_4x,sum_5x],[sum_2x,sum_3x,sum_4x,sum_5x,sum_6x],[sum_3x,sum_4x,sum_5x,sum_6x,sum_7x],[sum_4x,sum_5x,sum_6x,sum_7x,sum_8x]])
v1_4 = numpy.array([sum_y,pr_xy,pr_y2x,pr_y3x,pr_y4x])
otvet_4 = numpy.linalg.solve(m1_4,v1_4)
print(otvet_4)
print(x)
print(y)
polinom = []
for i in range(9):
    polinom.append(otvet_4[0] + otvet_4[1]*x[i] + otvet_4[2]*x[i]**2 + otvet_4[3]*x[i]**3 + otvet_4[4]*x[i]**4)

plt.plot(x,y)# сначала появится этот график, после график полинома(но только при закрытие 1 графика)
plt.show()

plt.plot(x,polinom)
plt.show()
