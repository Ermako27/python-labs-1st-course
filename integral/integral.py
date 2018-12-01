# Ермаков Максим ИУ7-14

from functions import midle_squares, trapeze

print('Используемая функция: 1/ln(x)')
print('а - нижняя граница интегрирования.')
print('Из области определения функции => a > 0 и a неравна 1.')
print('Методы: серединные прямоугольники, трапеции')
print()
n_mass = [int(x) for x in input('Введите количества разбиений n1 и n2: ').split()]
eps = float(input('Введите точность: '))
a, b = [int(x) for x in input('Введите границы интегрирования: ').split()]
method1_n1 = method1_n2 = 0
method2_n1 = method2_n2 = 0
i = 1
integr_n = integr_2n = 0
mistake = eps + 1

# первая часть программы
# каждым методом считаем интеграл при n1 и n2
for n in n_mass:
    method1_n1 = method1_n2
    method1_n2 = midle_squares(n, a, b)
    
    method2_n1 = method2_n2
    method2_n2 = trapeze(n, a, b)

print()
print(' '*30, n_mass[0], ' '*13, n_mass[1])
print('серединные прямоугольники', '{:11.7f}{:17.7f}'.format(method1_n1, method1_n2))
print('трапеции', '{:28.7f}{:17.7f}'.format(method2_n1, method2_n2))
print('\nМетод трапеций менее точный, значит вычисление '
      'с точностью до эпсилон')
print('проводим для этого метода.\n')


# Вторая часть программы
# Пока погрешность не станет меньше точности удаваиваем n

integr_2n = trapeze(i, a, b)
while mistake > eps:
    i *= 2
    integr_n = integr_2n
    integr_2n = trapeze(i, a, b)
    #print(integr_2n, i)
    mistake = abs(integr_2n - integr_n)

print('Значение интеграла с точностью ', eps,
      ', полученное при ', i,' разбиениях,')
print('равно {:1.7f}.'.format(integr_2n))
    


















    
'''
print(method1_n1, method1_n2)
print(method2_n1, method2_n2)    
mistake_1 = abs(method1_n2 - method1_n1)
mistake_2 = abs(method2_n2 - method2_n1)
print(mistake_1, mistake_2)
'''  

