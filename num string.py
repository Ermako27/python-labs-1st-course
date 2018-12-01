# Ермаков Максим ИУ7-14
s = input('Введите строку: ')
s += ' '
extr = '!'
elem = ''
i = 0
k = 0


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
s = input('Введите строку: ')
s = s[1:]
wsp = ''
extr = '!'

for i in range(len(s)):
    if s[i] != ' ':
        wsp += s[i]

num = int(wsp)

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num  % 10
num = num // 10
if b > a and b > c:
    extr = b

while num != 0:
    a = b
    b = c
    c = num % 10
    num = num // 10
    if b > a and b > c:
        extr = b
        
if  extr != '!':
    print('Первый экстремум последовательности: ', extr)
else:
    print('В данной последовательности нет экстремумов!')

for i in range(2,len(wsp)-1):
    if int(wsp[i-1]) < int(wsp[i]) and int(wsp[i]) > int(wsp[i+1]):
        extr = int(wsp[i])
        break
'''
