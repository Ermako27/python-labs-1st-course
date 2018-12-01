#Ермаков Максим
while True:
    try:
        a, b, c = [float(x) for x in input('Введите коэффиценты'
                                           'a,b,c соответственно: ').split()]
    except ValueError:
        print('Введены неверные данные')
    else:
        discr = b**2 - 4 * a * c
        import math
        if a != 0:
            if discr > 0:
                import math
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
            elif discr == 0:
                x = -b / (2 * a)
                print('x = %.2f' % x)
            else:
                print('Корней нет')

        elif b != 0:
            x = -c/b
            print("не квадратное \nx = %.3f" % (x))
        elif a == 0 and b == 0 and c != 0:
            print("нет таких x")
        else:
            print("x любое")
    inp = input('Если Вы хотите завершить программу нажмите Enter.\n'
                'Если Вы хотите продолжить нажмите любую клавишу.')
    if inp == '': # Завершение цикла
         break
