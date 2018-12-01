import math as m

def func(x):
    return m.sin(x)
    #return x**3 - 4*x - 1

def brentq_method(root_num, x1, x2, eps, max_iter):  # уточнение методом brentq
    root = 0  # уточняемый корень
    error = 0  # номер ошибки
    i = 0  # счетчик итераций

    a = x1
    b = x2
    if abs(func(x1)) > abs(func(x2)):
        t = x1
        x1 = x2
        x2 = t

    x3 = x1
    x4 = x1
    flag = True

    while abs(x1 - x2) > eps:
        if i >= max_iter:
            error = 1
            break
        i += 1

        if func(x1) != func(x3) and func(x2) != func(x3):  # квадратичная экстрополяция
            root = (x1*func(x2)*func(x3))/((func(x1)-func(x2))*(func(x1)-func(x3))) + \
                   (x2*func(x1)*func(x3))/((func(x2)-func(x1))*(func(x2)-func(x3))) + \
                   (x3*func(x1)*func(x2))/((func(x3)-func(x1))*(func(x3)-func(x2)))
        else:
            if func(x2) == func(x1):  # метод секущих
                error = 2
                break
            root = x2 - (func(x2)*(x2-x1))/(func(x2)-func(x1))
            if (((3*x1+x2)/4<root) and (root>x2)) or \
               ((not flag) and (abs(root-x2)>=abs(x2-x3)/2)) or \
               (flag and (abs(root-x2)>=abs(x3-x4)/2)) or \
               ((not flag) and (abs(x2-x3)<eps)) or \
               (flag and (abs(x3-x4)<eps)):  # метод половинного деления

                root = (x1+x2)/2
                flag = True
            else:
                flag = False

        x4 = x3
        x3 = x2

        if func(x1)*func(root) < 0:
            x2 = root
        else:
            x1 = root
        if abs(func(x1)) < abs(func(x2)):
            t = x1
            x1 = x2
            x2 = t
    #new_root = round(root, 4)
    print('{:8d}'.format(root_num), '{:13.3f}'.format(a), '{:12.3f}'.format(b), \
          '{:14.6f}'.format(root), '{:12.6f}'.format(func(root)), \
          '{:13d}'.format(i), '{:14d}'.format(error))
    return root








