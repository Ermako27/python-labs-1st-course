# Ермаков Максим ИУ7-14
# Вариант задачи с функциями Python

# Функции длина слова, количество слов, наиболее частое слово
from functions import word_len, oft, exp, word_count
i = 1
lines = ['Смешанные, все увеличивающиеся? Толпы',
         'бежали, назад к тому месту. Где пять минут',
         'тому назад w войска! Проходили мимо императоров:', 
         'нет. Только; трудно 10+4-5 w. Было, остановить эту',
         'толпу. Но невозможно было? Самим податься',
         'назад вместе с: толпой w. Болконский только',
         'старался 5+5 не отставать от Кутузова и w',
         'оглядывался, недоумевая и 1-1 не. В силах понять того,',
         'что делалось перед ним.'
         ]

lines_2 = []
max_len = 0
count = 0
for line in lines:
   count += word_count(line)

   if len(line) > max_len:
       max_len = len(line)

print()

# вывод текста
print('Текст до изменения: ')
print()
for line in lines:
   print(line)

print()
# самое длинное слово в  каждой строке
for state in lines:
    print('Самое длинное слово в %d строке: %s' % (i, word_len(state)))
    i += 1
print('\nКоличество слов во всем тексте: ', count)
print('Самое частое слово в тексте: ', oft(lines))

print()
fw = input('Выберете слово которое вы хотите заменить: ')
sw = input('Введите слово на которое выхотите заменить: ')
dw = input('Введите слово которое вы хотите удалить: ')
for line in lines:
    if '+' in line or '-' in line:
        lines_2.append(exp(line))
    else:
        lines_2.append(line)

print()
print('Форматирование по правому краю: \n')
for line in lines_2:
    print(line.replace(fw, sw).replace(dw, '').rjust(max_len, ' '))
print()
print('Форматирование по центру: \n')
difference = 0
spaces = []
space_count = 0
new_string = ''
ml = len(sorted(lines_2, key=lambda x: len(x))[-1])
k = 0
for line in lines_2:
    line = line.replace(fw, sw).replace(dw, '') # замена и удаление слов
    space_count = word_count(line) - 1  # количество пробелов в строке
    spaces = [' ']*space_count
    difference = ml - len(line)  # недостающее количество знаков

    # последовательно добавляем к каждому разделению по пробелу
    # пока не будет достигнута необходимая длина строки
    for i in range(difference):
        spaces[i % space_count] += ' '
    # поэлементно создаем новую строку из старой
    # добавлением слов, если в сторой строке встречается
    # пробел, то заменяем его элементом из spaces -
    # увеличенным пробелом
    for elem in line:
        if elem != ' ':
            new_string += elem
        elif elem == ' ' and k != len(spaces):
            new_string += spaces[k]
            k += 1
    print(new_string)
    difference = 0
    spaces = []
    space_count = 0
    new_string = ''
    k = 0














