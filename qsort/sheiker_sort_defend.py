import random as r

M = int(input('Введите размер массива: '))
print()
mass = [r.randint(0,20) for x in range(M)]
print('Неотсортированный массив: ', mass)


start = 0
end = len(mass) - 1
 
while start <= end:
    #print(left,right)
    for i in range(start, end):
        if mass[i] > mass[i + 1]:
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
    end -= 1
    for i in range(end, start, -1):
        if mass[i - 1] > mass[i]:
            mass[i], mass[i - 1] = mass[i - 1], mass[i]
    start += 1

print('Отсортированный массив: ', mass)
