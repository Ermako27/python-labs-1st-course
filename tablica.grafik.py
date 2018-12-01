# Ермаков Максим ИУ7-14
# Таблица значений, график

# 1) Вывод таблицы значений
from math import sin
xmin = float(input('Введите минимальное значение аргумента: '))
xmax = float(input('Введите максимальное значение аргумента: '))
step = float(input('Введите щаг: '))
xm = xmin 
xx = xmax
s1 = 0
s2 = 0
sc = 0 # значение функции в каждой точке
smin = 1.021*xmin**3 - 3.995*xmin**2 + 2.5 # s(xmin)
smax = smin # s(xmax)
count = 0
ocount = 0

N = int(abs(xmax - xmin)/step)# кол-во итераций в цикле for
print(" x \t           s1 \t          s2")
for i in range(N+1):
    s1 = 1.021*xm**3 - 3.995*xm**2 + 2.5 
    s2 = 3.04*xm**3 - 2.89*sin(5*xm) - 1.72
    if s1 < 0:
        ocount += 1
    elif s1 > 0:
        count +=1
    if 0.001< abs(s1) < 1000 and 0.001< abs(s2) < 1000:
        print('{:9.3f}{:15.3f}{:15.3f}'.format(xm,s1,s2))
    else:
        print('{:9.3f}{:15.2e}{:15.2e}'.format(xm,s1,s2))
    if s1 > smax: # Наибольшее значение s1
        smax = s1
    if s1 < smin: # Наименьшее значение s1
        smin = s1
    xm += step



# 2) График s1

mz = round(((0 - smin)/(smax - smin))*59 + 1)# кол-во знаков перед нулем

if abs(smin) <= 0.001 or abs(smin) >= 1000:
    esmin = '{:15.2e}'.format(smin)
else: esmin = '{:15.3f}'.format(smin)

if abs(smax) <= 0.001 or abs(smax) >= 1000:
    esmax = '{:57.2e}'.format(smax)
else: esmax = '{:57.3f}'.format(smax)

print('\nГрафик функции S1')

if smin > 0 and smax > 0:
    print('\n',esmin,esmax)
    print(' '*9 + '+' + '-'*60 + '+')
    for i in range(N+1):
        sc = 1.021*xmin**3 - 3.995*xmin**2 + 2.5 # значение в текущей точке
        m = round(((sc - smin)/(smax - smin))*59 + 1)
        print('{:9.3f}'.format(xmin), ' '*(m-1) + '*')
        xmin += step
        
elif smin < 0 and smax < 0:
    print('\n',esmin,esmax)
    print(' '*9 + '+' + '-'*60 + '+')
    for i in range(N+1):
        sc = 1.021*xmin**3 - 3.995*xmin**2 + 2.5 
        m = round(((sc - smin)/(smax - smin))*59 + 1)
        print('{:9.3f}'.format(xmin), ' '*(m-1) + '*')
        xmin += step

elif smin <= 0 and smax >= 0:
    print('\n',esmin,esmax)
    
    print(' '*9 + '+'+ '-'*(mz-1)+'0'+'-'*(60-mz) + '+')
    for i in range(N+1):
        sc = 1.021*xmin**3 - 3.995*xmin**2 + 2.5 
        m = round(((sc - smin)/(smax - smin))*59 + 1)
        if mz > m:
            print('{:9.3f}'.format(xmin), ' '*(m-1) + '*' + ' '*(mz-m-1) + '|')
        elif mz == m:
            print('{:9.3f}'.format(xmin), ' '*(m-1) + '*')
        elif mz < m:
            print('{:9.3f}'.format(xmin), ' '*(mz-1) + '|' + ' '*(m-1-mz) + '*')
        xmin += step

print('\nКоличество положительных значений: ',count, 'количество отрицательных значений: ', ocount)
