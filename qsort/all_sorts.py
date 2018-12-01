import random as r
import matplotlib.pyplot as plt
import numpy as np
import time


# Быстрая сортировка
def qsort(a, l, h):
    if h-l > 0:
        p = part(a, l, h)
        qsort(a, l, p-1)
        qsort(a, p+1, h)

def part(a, l, h):
    d = l
    pi = h
    for i in range(l, h):
        if a[i] < a[pi]:
            a[i], a[d] = a[d], a[i]
            d += 1
    a[pi], a[d] = a[d], a[pi]
    return d

# Сортировка пузырьком
def bubble(li):
    n = 1
    while n < len(li):
        for i in range(len(li)-n):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
        n += 1
    return li


# Сортировка пузырьком с флагом
def buble_flag(mass):
    flag = True
    while flag:
        flag = False
        for i in range(len(mass)-1):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
                flag = True
    return mass

# Сортировка шейкера
def sheiker(mass,start,end):
    while start <= end:
        for i in range(start, end):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
        end -= 1
        for i in range(end, start, -1):
            if mass[i - 1] > mass[i]:
                mass[i], mass[i - 1] = mass[i - 1], mass[i]
        start += 1
    return mass

# Сортировка простым выбором
def just_select(MAS):
    for i in range(len(MAS) - 1):
        min_i = i
        j = i + 1
        while j < len(MAS):
            if (MAS[j] < MAS[min_i]):
                min_i = j
            j += 1
        if (min_i != i):
            MAS[i],MAS[min_i] = MAS[min_i],MAS[i]
    return MAS

# Соритровка бинарными вставками
def binar_insert(MAS):
    for i in range(1,len(MAS)):
        if (MAS[i-1] > MAS[i]):
            x = MAS[i]
            left = 0
            right = i - 1
            while (left <= right):
                sred = (left + right) // 2
                if (MAS[sred] < x):
                    left = sred + 1
                else:
                    right = sred - 1
            j = i - 1
            while j >= left:
                MAS[j+1] = MAS[j]
                j-=1
            MAS[left] = x

    return MAS

# Сортировка простыми вставками
def just_insert(MAS):
    for i in range(1,len(MAS)):
        x = MAS[i]
        j = i - 1
        while j >= 0:
            if(MAS[j] < x):
                break
            MAS[j+1] = MAS[j]
            MAS[j] = x
            j = j - 1
    return MAS

# Вставка с барьером
def VsSBar(array):
    back = array[0]

    for i in range(2, len(array)):
        if array[i - 1] > array[i]:
            array[0] = array[i]
            j = i - 1

            while array[j] > array[0]:
                array[j + 1] = array[j]
                j = j - 1

            array[j + 1] = array[0]

    array[0] = back

    i = 1
    while array[i] < back:
        array[i - 1] = array[i]
        i += 1

    array[i - 1] = back

    return array

# Сортировка Шеллом
def Shell(MAS):
    n = len(MAS)
    i = 0
    while ((2**i-1) <= n):
        i += 1
    i = i - 1
    k = n // (2**i - 1)
    while k > 0:
        for i in range(len(MAS) - k):
            j = i
            while (j >= 0) and MAS[j] > MAS[j+k]:
                x = MAS[j]
                MAS[j] = MAS[j + k]
                MAS[j + k] = x
                j -= 1
        i -= 1
        k = n // (2**i - 1)
    return MAS

# Пирамидальная сортировка
def piramid(li):
    def downHeap(li, k, n):
        new_elem = li[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and li[child] < li[child + 1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(size // 2 - 1, -1, -1):
        downHeap(li, i, size)
    for i in range(size - 1, 0, -1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i)
    return li

# Улучшенный пузырек
def better_bubble(A):
    for i in range(len(A)):
        f = 0
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                f = 1
        if f == 0:
            break
    return A

N = [1000, 3000, 5000, 7000, 9000, 11000]
times = []
for i in N:
    m = [r.randint(0,100) for j in range(i)]
    start = time.clock()
    qsort(m, 0, len(m)-1)
    end = time.clock()
    dif = end - start
    times.append(dif)

plt.title('Метод quick sort')
plt.grid(True)
plt.xlabel('количество элементов')
plt.ylabel('Время в секундах')
plt.plot(N, times)
plt.xticks(N,N)
plt.show()






