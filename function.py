from math import log
b1, a2 = map(float,input('Введите два аргумента b1 и a2 соответственно: ').split())
if b1 > 0: 
    z = 10 * log(b1)
    print('z(b1) = %.3f' % z)
elif b1 <= 0:
    z = 10 * b1
    print('z(b1) = %.3f' % z)
if a2 > 0:
    z = 10 * log(a2)
    print('z(a2) = %.3f' % z)
elif a2 <= 0:
    z = 10 * a2
    print('z(a2) = %.3f' % z)
