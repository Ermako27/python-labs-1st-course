#Ермаков Максим ИУ7-14
#Найти объем площадь боковой и полной поверхности шарового слоя

import math
try:
    h, r1, r2, R = map(float, input('Введите высоту, радиусы оснований шарового\
слоя и радус полного шара соответственно: ').split())
    V = (math.pi*h**3)/6 + (math.pi*h*(r1**2 + r2**2))/2
    Sbok = 2*math.pi*R*h
    Spoln = Sbok + math.pi*r1**2 + math.pi*r2**2
    print('Объем = %.3f \nПлощадь боковой поверхности = %.3f\
\nПлощадь полной поверхности = %.3f' % (V, Sbok, Spoln ))
except ValueError:
    print('Введены либо неверные либо неплоные данные')
