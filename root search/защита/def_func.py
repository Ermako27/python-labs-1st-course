import math as m

def func(x):
    return m.sin(x)


def sek(x1, x2, eps):
    a = x1
    b = x2
    #print(a,b)
    while abs(x2 - x1) > eps:
        tmp = x2
        x2 = x2 - (func(x2) * (x2 - x1)) / (func(x2) - func(x1))
        x1 = tmp
    if b-a > 0.01:
        print('секущая выходит за границы отрезка')
    else:
        print(x2)
