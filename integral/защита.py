from functions import three_eight
integral = 0
print('Функция х*х.')
n = int(input('Введите количество разбиений n: '))
a, b = [int(x) for x in input('Введите границы интегрирования: ').split()]
h = (b-a)/n
print()
if n % 3 != 0:
    print('n должен быть кратным 3.')
else:
    integral = three_eight(n, a, b)
    print('значение интеграла: {:0.7f} при '.format(integral), n,'разбиениях')
    print('шаг: {:0.7f} '.format(h))
    
            
        
