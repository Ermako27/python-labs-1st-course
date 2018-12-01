# Ермаков Максим ИУ7-14

s = input('Введите строку: ')
s += ' '
extr = '!'
elem = ''
k = 0
l = s.find(' ')
num = l
n = ''
cur = ''

# выделяем количество числел
# Использовать массивы нельзя, поэтому все числа получается переводом в int
# Границы числа определяются пробелами
for e in range(l): 
    n += s[e]
n = int(n)

# цикл для выделения первого элемента для сравнения чисел в строке
for e in range(l+1, s.find(' ', l+1)): 
    cur += s[e]
cur = int(cur)

l = s.find(' ', l+1)
# В цикле в диапазоне ранее вычисленного n выделяются и сравниваются числа
# cur - первый элемент с ним начинается сравнение последующих
for i in range(num,n+num):
    for j in range(num+1, s.find(' ', num+1)):
        elem += s[j]
    elem = int(elem)
    
    num = s.find(' ', num+1)
    if elem > cur:
        k += 1
    if elem < cur and k != 0:
        extr = cur
        break
    cur = elem
    elem = ''
        
if extr != '!':
    print('Первый экстремум: ', extr)
else: print('В последовательности нет экстремумов')  






































'''
for el in s: # отсекаем первое число т.к. оно не входит
    if el != ' ':
        i += 1
    elif el == ' ':
        s = s[i+1:]
        break
i = 0
for el in s: # запоминаем первый элемент в изменённой строке для сравнения
    if el != ' ':
        i += 1
    elif el == ' ':
        h = int(s[:i+1])
        break
i = 0
while s != '': # пока строка не кончится искать экстремум
    while s[i] != ' ': # цикл для формирования числа любой длины и знака
        elem += s[i]
        i += 1  
    if int(elem) > h:
        k += 1
    if int(elem) < h and k != 0:
        extr = h
        break
        
    h = int(elem)
    s = s[i+1:]
    i = 0
    elem = ''

if extr != '!':
    print('Первый экстремум: ', extr)
else: print('В последовательности нет экстремумов')            
'''

