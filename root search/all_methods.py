# ввод значений и поиск орезка с корнем
import math
a, b = [float(x) for x in input('Введите границы интервала: ').split()]
eps = float(input('Введите точность: '))

def f(x):
    return x**3 - 4*x + 1

def f1(x):
    return 3*x**2 - 4

def f2(x):
    return 6*x

# метод половинного
def half_del(a,b,eps):
    while abs(b-a) > eps:
        root = (a+b)/2
        if f(a)*f(b) < 0:
            a = root
        else:
            b = root
    print((a+b)/2)

# метод хорд
def horda(a,b,eps):
    while(abs(b-a) > eps):
        a = b - (b-a)*f(b)/(f(b)-f(a))
        b = a + (a-b)*f(a)/(f(a)-f(b))
    print(b)


# метод касательной
def new(a,b,x0, eps):
    flag = 0
    x1 = x0 - (f(x0) / f1(x0))
    while abs(x1-x0) < eps:
        x1 = x0 - (f(x0)/f1(x0))
        if x1 < a or x1 > b:
            flag = 1
        x0 = x1
    if flag:
        print('касательная выходит за пределы отрезка')
    else:
        print(x1)
def kasat(a, b, eps):
    if f(a)*f2(a) > 0:
        x0 = a
        new(a,b,x0, eps)
    elif f(b)*f2(b) > 0:
        x0 = b
        new(a, b, x0, eps)
    else:
        print('не удается найти первое приближение корня')

# упрощенный метод ньютона
def simple_new(a,b,x0, eps):
    const_root = f1(x0)
    x1 = x0 - (f(x0) / const_root)
    while abs(x1-x0) < eps:
        x1 = x0 - (f(x0)/const_root)
        if x1 < a or x1 > b:
            print('корень выходит за пределы отрезка')
        x0 = x1
    print(x1)
def closer(a, b, eps):
    if f(a)*f2(a) > 0:
        x0 = a
        simple_new(a, b, x0, eps)
    elif f(b)*f2(b) > 0:
        x0 = b
        simple_new(a, b, x0, eps)
    else:
        print('не удается найти первое приближение корня')

# комбинированный метод
def combination(a, b, eps):
    while abs(a-b) > 2*eps:
        if f(a)*f2(a) < 0:
            a = a - ((f(a)*(a-b))/(f(a)-f(b)))
        elif f(a)*f2(a) > 0:
            a = a - (f(a)/f1(a))
        if f(b)*f2(b) < 0:
            b = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        elif f(b)*f2(b) > 0:
            b = b - (f(b)/f1(b))
    root = (a+b)/2
    print(root)

# метод секущих
def sek(a,b,eps):
    x1 = a
    x2 = b
    flag = 0
    while abs(b-a) > eps:
        t = b
        b = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        a = t
        if b < x1 or b > x2:
            flag = 1
    if flag:
        print('секущая выходит за границы отрезка')
    else:
        print(b)

# метод стеффенсона
def steff(a, b, x0, eps):
    flag = 0
    x1 = x0 - ((f(x0)) ** 2 / (f(x0 + f(x0)) - f(x0)))
    while abs(x1 - x0) < eps:
        x1 = x0 - ((f(x0))**2 /(f(x0 + f(x0)) - f(x0)))
        if x1 < a or x1 > b:
            flag = 1
        x0 = x1
    if flag:
        print('касательная выходит за пределы отрезка')
    else:
        print(x1)


def priblijenie(a, b, eps):
    if f(a) * f2(a) > 0:
        x0 = a
        steff(a, b, x0, eps)
    elif f(b) * f2(b) > 0:
        x0 = b
        steff(a, b, x0, eps)
    else:
        print('не удается найти первое приближение корня')


half_del(a,b,eps)
