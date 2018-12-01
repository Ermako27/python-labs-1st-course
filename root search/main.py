from functions import func, brentq_method


a, b = [int(x) for x in input('Введите границы интервала: ').split()]
h = float(input('Введите шаг: '))
eps = float(input('Введите точность: '))
max_iter = int(input('Введите максимальное количество итераций: '))
print()
new_a = a
new_b = b
root_num = 1
#prev_root = 0 # хранит предыдущий корень
print('0 - Ошибки отсутствуют\n' \
      '1 - Превышено допустимое количество итераций\n' \
      '2 - Деление на ноль\n')
print()
print('| Номер корня |    Xn    |    Xn+1    |   Корень   | Значение f(x) | Число итераций | Код ошибки |')
print('-'*98)

while new_a < new_b:
    e = new_a + h  # верхняя граница интервала с корнем
    f_new_a = func(new_a)
    f_e = func(e)
    if (f_new_a >= 0 and f_e <= 0) or (f_new_a <= 0 and f_e >= 0):
        brentq_method(root_num, new_a, e, eps, max_iter)
        print('-'*98)
        root_num += 1
    new_a = e  # нижняя граница интервала с корнем



