# Сортировка массива режимом вставки
# Сортировка массива режимом вставки с барьером
# Пирамидальная
# Шейкер
# Бинарные вставки
# Пузырек
# Улучшенный пузырек
# Пузырек с флагом
# Шелла
# Быстрая
# Выбором
#


N = [100, 1000, 10000, 50000]

from random import *
from time import *


def Xrandom(n):
    X = []
    i = 0
    while i < n - 1:
        k = randrange(0, n)
        X.append(k)
        i += 1
    X.append(0)
    return X


# Режим вставки

def insert(X):
    start = time()
    print(X)
    lenn = len(X)
    # print(lenn)
    for i in range(2, lenn):
        k = X[i]
        j = i - 1
        X[0] = k
        while k < X[j]:
            X[j + 1] = X[j]
            j -= 1
            X[j + 1] = k

    end = time()
    print(X)
    print(len(X))
    # print(end - start)
    return X


# Режим вставки с барьером

def wall_insert(X):
    start = time()
    back = X[0]
    # print(X)
    lenn = len(X)
    for i in range(2, lenn):
        if X[i - 1] > X[i]:
            X[0] = X[i]
            j = i - 1
            while X[j] > X[0]:
                X[j + 1] = X[j]
                j -= 1
            X[j + 1] = X[0]
    array[0] = back

    i = 1
    while array[i] < back:
        array[i - 1] = array[i]
        i += 1

    array[i - 1] = back
    end = time()
    # print(X)
    return X


# Пирамидальная
def piramid(li):
    """Сортирует список в возрастающем порядке с помощью алгоритма пирамидальной сортировки"""
    start = time()

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
    end = time()
    return li


# Шейкер
def sheiker(a):
    start = time()
    # left, right - borders of not sorted part


k = right = len(a) - 1
left = 1
while (left < right):
    # right to left
    for j in range(right, left - 1, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            k = j
        left = k
    # left to right
    for j in range(left, right + 1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            k = j
        right = k
end = time()
return a


# Бинарные вставки
def binary(x):
    for i in range(1, len(x)):
        key = x[i]
        left = 0
        right = i
        while right > left:
            mid = int(left + right) // 2
            if x[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        for j in range(i - 1, left - 1, -1):
            x[j + 1] = x[j]
        x[left] = key
    return x


# Пузырек
def bubble(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[j], x[i] = x[i], x[j]
    return x


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
    return (A)


# Пузырек с флагом
def flag_bubble(a):
    f = True
    while f:
        f = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            f = True
    return a


# Шелла
def shell(A):
    """Сортировка списка"""
    start = time()
    ##    print(A)
    sarr = [1200, 700, 400, 200, 100, 50, 25, 12, 8, 4, 2, 1]
    for i in range(len(A)):
        flag = 0
        for j in range(len(A) - 1):
            # Замена элементов в списке
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = 1
        # Проверка для выхода
        if flag == 0:
            break
    end = time()
    return A


# Быстрая
def qsort(x):
    if len(x) <= 1:
        return (x)
    else:
        q = x[len(x) // 2]
        l = []
        m = []
        r = []
        for i in range(len(x)):
            if x[i] < q:
                l.append(x[i])
            elif x[i] == q:
                m.append(x[i])
            else:
                r.append(x[i])

        return (sort(l) + m + sort(r))


# Выбором
def select(x):
    for i in range(len(x)):
        min_ind = i
        for j in range(i, len(x)):
            if x[min_ind] > x[j]:
                min_ind = j
        x[i], x[min_ind] = x[min_ind], x[i]

    return (x)


print('Сортировка массивов методом .\n')
print('Количество элементов\t\t\tВремя выполнения')
for i in N:
    x1 = Xrandom(i)
    x2 = qsort(x1)
    print(x2)

plt.plot(N, Period)
plt.grid(True)
plt.xlabel('Count of elements')
plt.ylabel('Time')
plt.title('Зависимость времени сортировки от размера массива')
plt.show()