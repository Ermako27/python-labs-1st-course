# Ермаков Максим ИУ7-14
# Сумма бесконечного
from math import fabs
n = 0
f = 0
j = 1
t = 1
k = 0
eps = float(input('Введите точность: '))
hn = int(input('Введите номер начального элемента: '))
mx = int(input('Введите максимальное количество элементов суммы: '))
step = int(input('Введите шаг: '))
steptype = input('Введите тип шага (*, +): ')

print(' n \t    текущий  \t         сумма')

while fabs(t) > eps:
    k += 1
    n += 1
    t = ((2*n + 1)/(3*n + 1))**(n/2)
    f += t
    if steptype == '+':
        if n >= hn and n % step == 0:
            print('{:2d}{:^30.7f}{:>10.7f}'.format(n,t,f))
    elif steptype == '*':

        if n >= hn and n == step**j:
            j += 1
            print('{:2d}{:^30.7f}{:>10.7f}'.format(n,t,f))

    if n == mx:
        print('\nРяд не сошелся за ', n,'итераций')
        break

if fabs(t) < eps:
    print('\nс точностью: ',eps,'сумма: %.7f ' % f,'число элементов: ', k)
