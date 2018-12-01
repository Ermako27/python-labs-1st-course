# Ермаков Максим ИУ7-14

from math import fabs, factorial

eps = float(input('Введите точность: '))
a = float(input('Введите параметр а: '))
t = 0
n = 0
c = 1
while fabs(c) > eps:
    n += 1
    c = ((a**((2*n)+1))/(factorial(2*n+1)))# текущий член
    t += c # Сумма ряда
m = int(input('Введите количество строк: '))
p = int(input('Введите количество столбцов: '))
a = [[int(input('Введите элемент: ')) for j in range(p)] for i in range(m)]
x = []

for i in range(m):          # заполнение массива Х числами > t
    for j in range(p):
        if a[i][j] > t:
            x.append(a[i][j])

mx = x[0]
for i in range(len(x)): # Нахождение в массиве X макс элемента
    if x[i] > mx:
        mx = x[i]
        k = i
print('\nВектор Х до изменения: ')
print(x)
print('\nПервый элемент: ', x[0])
print('Максиммальный элемент: ', x[k], 'c индексом: ', k)
y = x[0]    # меняем местами максимальный и минимальный элементы
x[0] = x[k]
x[k] = y



print('\nСумма ряда: ', t)
print('\nМатрица:')
for i in range(m):
    for j in range(p):
        print('{:4d}'.format(a[i][j]), end = '')
    print('\n')

print('Вектор X.')
print(x)



    


        



