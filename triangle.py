
# Ермаков Максим ИУ7-14

# длины сторон
# определить является ли реугольник равносторонним
# биссектрису из наименьшего угла
# принадлежность треугольнику, если да, то найти расстояние до ближайшей стороны



from math import sqrt, acos, cos

while True:
    try:
        
        Ax, Ay = map(int,input('\nВведите координаты 1-ой точки треугольника. ').split())
        Bx, By = map(int,input('Введите координаты 2-ой точки треугольника. ').split())
        Cx, Cy = map(int,input('Введите координаты 3-ой точки треугольника. ').split())
        Ox, Oy = map(int,input('Введит координаты точки О. ').split())
    except ValueError:
        print('Введены неверные данные.\n')
    else: 
        lng_AB = sqrt((Bx - Ax)**2 + (By - Ay)**2) # Длины сторон
        lng_BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
        lng_AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)
        
        if (lng_AB < lng_AC + lng_BC) and (lng_AC < lng_AB + lng_BC) and (lng_BC < lng_AB + lng_AC):
            print('\nДлины сторон треугольника: %.3f, %.3f, %.3f' % (lng_AB, lng_BC, lng_AC))
        
            if lng_AB == lng_BC == lng_AC:
                print('\nТреугольник, построенный по заданным точкам равносторонний. ')
            else:
                print('\nТреугольник не равносторонний.')

            ugl_A = acos(((Bx - Ax)*(Cx - Ax) + (By - Ay)*(Cy - Ay))/(lng_AB * lng_AC)) # Углы
            ugl_B = acos(((Ax - Bx)*(Cx - Bx) + (Ay - By)*(Cy - By))/(lng_AB * lng_BC))
            ugl_C = acos(((Bx - Cx)*(Ax - Cx) + (By - Cy)*(Ay - Cy))/(lng_BC * lng_AC))
    
            if min(ugl_A, ugl_B, ugl_C) == ugl_A:
                biss = (2*lng_AB*lng_AC*cos(ugl_A/2))/(lng_AB + lng_AC)
 
            elif min(ugl_A, ugl_B, ugl_C) == ugl_B:
                biss = (2*lng_AB*lng_BC*cos(ugl_B/2))/(lng_AB + lng_BC)
   
                
            elif min(ugl_A, ugl_B, ugl_C) == ugl_C:
                biss = (2*lng_AC*lng_BC*cos(ugl_C/2))/(lng_AC + lng_BC)

            print('Биссектриса L меньшего угла: %.3f ' % (biss))
    
            a = (Ax - Ox)*(By - Ay) - (Bx - Ax)*(Ay - Oy) # Псевдоскалярное произведение
            b = (Bx - Ox)*(Cy - By) - (Cx - Bx)*(By - Oy) # [a,b] = x1*y2 - x2*y1
            c = (Cx - Ox)*(Ax - Cy) - (Ax - Cx)*(Cy - Oy)

            if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
                print('Точка принадлежит площади треугольника.')

                h_AB = (abs((Bx - Ax)*(Oy - Ay) - (Ox - Ax)*(By - Ay)))/lng_AB # Расстояние от точки до ближайшей прямой
                h_AC = (abs((Cx - Ax)*(Oy - Ay) - (Ox - Ax)*(Cy - Ay)))/lng_AC
                h_BC = (abs((Cx - Bx)*(Oy - By) - (Ox - Bx)*(Cy - By)))/lng_BC
                h_min = min(h_AB, h_AC, h_BC)
                print('Расстояние до ближайшей стороны треугольника: %.3f\n' % (h_min))
            else:
                print('Точка не принадлежит треугольнику.\n')

        else:
            print('\nПо данным точкам невозможно построить треугольник.\n')


        
    inp = input('\nЕсли Вы хотите завершить программу нажмите Enter.\n'
                'Если Вы хотите продолжить нажмите любую клавишу.')

    if inp == '': # Завершение цикла
         break
        
    
        
