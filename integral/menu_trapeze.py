from functions import trapeze
i = 1

while True:
    print('Введите, что вы хотите посчитать.')
    n = input('1 - c заданным количесвтом разбиений.\n'
                  '2 - с заданной точностью.\n'
                  '0 - выход.\n')
    if n == '1':
        print('Вы выбрали количество разбиений.')
        a,b = [int(x) for x in input('Введите границы интегрирования: ').split()]
        n = int(input('Введите количество разбиений: '))
        res = trapeze(n, a, b)
        print('Интеграл при', n,'разбиениях равен: {:1.7f}.'.format(res))
        k = input('Если хотите выйти нажмите 0.')
        if k == '0':
            break
        else: continue
    if n == '2':
        print('Вы выбрали точность.')
        eps = float(input('Введите точность: '))
        a,b = [int(x) for x in input('Введите границы интегрирования: ').split()]
        mis = eps + 1
        integr_n = integr_2n = 0

        integr_2n = trapeze(i, a, b)
        while mis > eps:
            i *= 2
            integr_n = integr_2n
            integr_2n = trapeze(i, a, b)
            mis = abs(integr_2n - integr_n)
        print('Значение интеграла с точностью ', eps,
              ', полученное при ', i,' разбиениях,')
        print('равно {:1.7f}.'.format(integr_2n))
        k = input('Если хотите выйти нажмите 0.')
        if k == '0':
            break
        else: continue
    if n == '0':
        break
    
        
        
        
        
        

        
        
    

