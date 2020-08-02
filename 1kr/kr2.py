import math

#Вариант 28
#Каменьщиков Семён Валерьевич
#АА-19-05

def simpson(n):
    y = []
    x = []
    sum = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    h = 1/n
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(n):
        y.append(math.log(x[i] + (x[i]*x[i] + 4)**(1/2)))
    for i in range(len(y)):
        if i == 0:
            sum1 = y[0] + y[len(y)-1]
        else:
            if i%2 ==0:
                sum2 = sum2 +y[i]
            else:
                sum3 = sum3 + y[i]
    sum = sum1 +2*sum2 + 4*sum3
    sum = sum * h/3
    return sum


def left():
    y = [0, 0.51, 0.91, 1.28, 1.65, 2.04, 2.47, 2.96, 3.52, 4.17, 4.93]
    x = []
    h = 0.1
    sum = 0
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(len(y)-1):
        if i==len(y)-1:
            break
        sum = sum +y[i]
    sum = h * sum
    return sum

n = int(input('Введите число отрезков: '))
a_simson = simpson(n)
a_left = left()
print('Симпсон ', a_simson)
print('Левые прямоугольники ', a_left)


pog_abs_left =  abs(a_left-((1/2)*(-3+math.exp(2))))
pog_ot_left = (pog_abs_left/a_left)*100

pog_abs_simson = abs(a_simson - (2 - 5**(1/2) + math.log(1+5**(1/2))))
pog_ot_simson = (pog_abs_simson/a_simson)*100


print('Абсолютная погрешность симсон = ', pog_abs_simson)
print('Относительная погрешность симсон = ', pog_ot_simson)
print('Абсолютная погрешность левые прямоугольник = ', pog_abs_left)
print('Относительная погрешность левые прямоугольник = ', pog_ot_left)
