import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp
import math


def f(x):  # фенкция
    return x**3 - 4*x - 1

def f_derivative(x):  # производная
    return 3*(x**2) - 4

def f_second_derivative(x):  # вторая производная
    return 6*x

a, b = [float(x) for x in input('введите границы: ').split()]
h = abs(b-a)/100
min_max = [a, b] # минимум и максимум(концы полинома)
f_min_max = [f(a), f(b)]  # значения минимума и максимума
roots = []  # корни
extremes = []  # экстремумы
f_extremes = []  # значения в экстремумах
bend = []  # точки перегиба
f_bend = []  # значения точек перегиба
rootcount = 0  # количество корней
#excount = 0  # количество экстремумов
#bendcount = 0  # количество точек перегиба

side1 = a
side2 = b
while side1 < side2:  # нахождение корней
    e = side1 + h
    f_side1 = f(side1)
    f_e = f(e)
    if (f_side1 > 0 and f_e < 0) or (f_side1 < 0 and f_e > 0):
        roots.append(sp.brentq(f, side1, e))
        rootcount += 1
    side1 = e

side1 = a
side2 = b
while side1 < side2:  # Экстремумы
    e = side1 + h
    f_side1 = f_derivative(side1)
    f_e = f_derivative(e)
    if (f_side1 > 0 and f_e < 0) or (f_side1 < 0 and f_e > 0):
        ex = sp.brentq(f_derivative, side1, e)
        if f_derivative(ex - h/2) * f_derivative(ex + h/2) < 0:
            extremes.append(ex)
            f_extremes.append(f(ex))
            #excount += 1
    side1 = e

side1 = a
side2 = b
while side1 < side2:  # точки перегиба
    e = side1 + h
    f_side1 = f_second_derivative(side1)
    f_e = f_second_derivative(e)
    if (f_side1 > 0 and f_e < 0) or (f_side1 < 0 and f_e > 0):
        per = sp.brentq(f_second_derivative, side1, e)
        if f_second_derivative(per - h/2) * f_second_derivative(per + h/2) < 0:
            bend.append(per)
            f_bend.append(f(per))
            #bendcount += 1
    side1 = e




plt.title('f(x) = $x^3$ - 4x - 1')
x1 = np.linspace(a, b, 5)
plt.plot(x1, f(x1))
plt.plot(roots, [0]*rootcount, 'bo', label='Корни')
plt.plot(extremes, f_extremes, 'ro', label='Экстремумы')
plt.plot(bend, f_bend, 'go', label='Точки перегиба')
plt.plot(min_max, f_min_max, 'ko', label='Минимум и максимум')
plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0)
plt.grid()
plt.show()
