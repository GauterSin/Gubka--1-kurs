import math
import numpy

# Задание 1 интегралл(0, pi/2)( e**(2x)*cos(x)dx )

def left(n):# Все кроме последнего
    y = []
    x = []
    sum = 0
    h = math.pi/(n*2)
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(n):
        y.append(math.exp(2*x[i])*math.cos(x[i]))
    for i in range(len(y)-1):
        if i==len(y)-1:
            break
        sum = sum +y[i]
    sum = h * sum
    return sum
def right(n):# Все кроме первого
    y = []
    x = []
    sum = 0
    h = math.pi/(n*2)
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(n):
        y.append(math.exp(2*x[i])*math.cos(x[i]))
    for i in range(len(y)-1):
        if i==0:
            continue
        sum = sum +y[i]
    sum = h * sum
    return sum
def sred(n):# Все кроме последнего
    y = []
    x = []
    sum = 0
    h = math.pi/(n*2)
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            if i == n-1:
                break
            x.append(x[i-1]+h/2)
    for i in range(len(x)-1):
        y.append(math.exp(2*x[i])*math.cos(x[i]))
    for i in range(len(y)):
        sum = sum +y[i]
    sum = h*sum
    return sum

def trapeciya(n):
    y = []
    x = []
    sum = 0
    h = math.pi/(n*2)
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(len(x)-1):
        if i==0:
            y.append(math.exp((2*x[i])*math.cos(x[i])+math.exp(2*x[len(x)-1])*math.cos(x[len(x)-1])/2))
        else:
            y.append(math.exp(2*x[i])*math.cos(x[i]))
    for i in range(len(y)):
        sum = sum +y[i]
    sum = sum*h
    return sum

def simpson(n):
    y = []
    x = []
    sum = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    h = math.pi/(n*2)
    for i in range(n):
        if i == 0:
            x.append(0)
        else:
            x.append(x[i-1]+h)
    for i in range(n):
        y.append(math.exp(2*x[i])*math.cos(x[i]))
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

n = int(input('Введите n: '))
a_left = left(n)
a_right = right(n)
a_sred = sred(n)
a_trap = trapeciya(n)
a_simpson = simpson(n)
print('Левые прямоугольники ', a_left)
print('Правые прямоугольники ', a_right)
print('Средние прямоугольники ', a_sred)
print('Трапеции ', a_trap)
print('Симпсон ', a_simpson)
