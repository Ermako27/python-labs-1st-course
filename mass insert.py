# Ермаков Максим Сергеевич ИУ7-14


a = ['']*25
b = ['']*15
f = 0 # счетчик элементов в массиве A  
g = 0 # счетчик элементов в массиве B

elema = input('Введите элемент массива A: ')
while True: # заполняем массив A
    if elema != '':
        a[f] = int(elema)
        elema = input('Введите элемент массива A: ')
        f += 1
    else: break

print('\nМассив A до изменения: ', a[:f], '\n' )
  
elemb = input('Введите элемент массива B: ')
while True: # заполняем массив B
    if elemb != '':
        b[g] = int(elemb)
        elemb = input('Введите элемент массива B: ')
        g += 1
    else: break
    
print('\nМассив B: ', b[:g])
sr = f + g
k = int(input('\nВведите K: '))
n = f - k + 1 # сколько элементов необходимо передвинуть

for i in range(n+1): # сдвигаем элементы в массиве A
    a[f+g] = a[f]
    f -= 1

for i in range(g): # вставляем элементы из B
    a[k] = b[i]
    k += 1
    
print('\nОбъединенные массивы: ', a[:sr])

