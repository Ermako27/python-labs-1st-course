import random as r
import time
mass = [2,1,7,3,6,4,9,2,0]
m1 = [r.randint(0,1000) for x in range(5000)]
m2 = [r.randint(0,30000) for x in range(50000)]
m3 = [r.randint(0,1000000) for x in range(200000)]


def qsort(a,l,h): # алгоритм быстрой сортировки
    if h-l > 0:
        p = part(a,l,h)
        qsort(a,l,p-1)
        qsort(a,p+1,h)

def part(a,l,h): # разделение 
    d = l
    pi = h
    for i in range(l, h):
        if a[i] < a[pi]:
            a[i], a[d] = a[d], a[i]
            d += 1
    a[pi], a[d] = a[d], a[pi]

    return d

print('Сортировка методом быстрой сортировки') # Пример работы 
print()
print('Пример работы алгоритма:')
print('Исходный массив: ', mass)
qsort(mass,0,len(mass)-1)
print('Отсортированный массив: ', mass)
print()

start = time.clock() # время работы при 5000
qsort(m1,0,len(m1)-1)
end = time.clock()
dif1 = end - start

start = time.clock() # время работы при 50000
qsort(m2,0,len(m2)-1)
end = time.clock()
dif2 = end - start

 
start = time.clock() # время работы при 200000
qsort(m3,0,len(m3)-1)
end = time.clock()
dif3 = end - start

print('Размер массива      Время сортировки в секундах')
print('-'*47)
print(' '*4,len(m1), '{:23.4f}'.format(dif1))
print('-'*47)
print(' '*4,len(m2), '{:22.4f}'.format(dif2))
print('-'*47)
print(' '*4,len(m3), '{:21.4f}'.format(dif3))






            
