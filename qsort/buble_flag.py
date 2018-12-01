import random as r
#m = [r.randint(0,20) for i in range(10)]
t = int(input('Сколько чисел вы хотите ввести: '))
st = str(t)
m = [int(x) for x in input('Введите ' + st + ' чисел в одной строке: ').split()]

print('Неотсортированный массив: ', m)

def buble_flag(mass):
    flag = True
    while flag:
        flag = False
        for i in range(len(mass)-1):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
                flag = True
    return mass

print('Отсотированный массив: ', buble_flag(m))

'''
n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
'''

