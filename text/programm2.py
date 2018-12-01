# Ермаков Максим ИУ7-14
# Вариант задачи без функций Python


from functions2 import word_len2, word_count2, oft2, rplc
from functions import exp

lines = ['Смешанные, все увеличивающиеся? Толпы',
         'бежали, назад к тому месту. Где пять минут',
         'тому назад войска! Войска! Проходили мимо императоров:', 
         'нет. Только; трудно 10+4-5. Было, остановить эту',
         'толпу. Но невозможно было? Самим податься',
         'назад вместе с: толпой. Болконский только',
         'старался 5+5 не отставать от Кутузова и',
         'оглядывался, недоумевая и 1-1 нет. в силах понять того,',
         'что делалось перед ним.'
         ]
lines_2 = ['']*len(lines)


# Количество слов во всем тексте
count = 0
max_len = 0  # макс. длина строки в тексте для форматирования по-правому краю
for line in lines:
    count += word_count2(line)
    if len(line) > max_len:
        max_len = len(line)
'''
вывод неизмененного текста проиходит после поиска
количества слов в строке т.к. в этом цикле находится
переменная max_len, необходимая для форматирования 
правому краю, если выводить текст раньше этого цикла,
то не будет известна максимальная длина строки и
форматирование будет невозможно.
'''
# вывод текста
print('Текст до изменения: ')
print()
for line in lines:
   print(line)
print()

# вывод самых длинных слов в каждой строке
i = 1
current_word = 0
for line in lines:
    current_word = word_len2(line)
    print('Самое длинное слово в %d строке: %s' % (i, current_word))
    i += 1
print()
print('Количество слов во всем тексте: %d' % count)

# Самое частое слово
print('Самое частое слово в тексте: %s' % oft2(lines))
print()



# Форматирование текста
fw = input('Выберете слово которое вы хотите заменить: ')
sw = input('Введите слово на которое выхотите заменить: ')
dw = input('Введите слово которое вы хотите удалить: ')
print()
print('Форматирование по правому краю: ')
print()
st = ''
tab = 0
ml = 0
m = 0

for line in lines:
    st = rplc(line, fw, sw)
    st = rplc(st, dw, '')
    if '+' in st or '-' in st:
        st = exp(st)
    if len(st) > ml: # находит самую длинную измененную строку
        ml = len(st)
    lines_2[m] = st[:-2]
    m += 1
    tab = max_len + 2 - len(st)
    print(' '*tab + st)


print()
print('Форматирование по центру: \n')
difference = 0
spaces = []
space_count = 0
new_string = ''
k = 0
j = 0
for line in lines_2:
    space_count = word_count2(line) - 1
    spaces = [' ']*space_count
    difference = ml - len(line)

    # последовательно добавляем к каждому разделению по пробелу
    # пока не будет достигнута необходимая длина строки
    while j <= difference:
        spaces[j % space_count] += ' '
        j += 1
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
    st = ''
    j = 0









