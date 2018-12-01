from functions import word_count, exp
lines = ['Смешанные, все увеличивающиеся толпы',
         'бежали назад к тому месту где пять минут',
         'тому назад войска проходили мимо императоров.', 
         'Не только трудно 10+4-5 было остановить эту',
         'толпу, но невозможно было самим не податься',
         'назад вместе с толпой. Болконский только',
         'старался 5+5 не отставать от Кутузова и',
         'оглядывался, недоумевая и 1-1 не в силах понять того,',
         'что делалось перед ним.'
         ]

word = ns = ''
st_len = 0
prob = 0
st = ''
fw = input('Выберете слово которое вы хотите заменить: ')
sw = input('Введите слово на которое выхотите заменить: ')
dw = input('Введите слово которое вы хотите удалить: ')

for line in lines:
    line += ' '
    st = line.replace(fw,sw)
    st = st.replace(dw, '')
    if '+' in st or '-' in st:
        st = exp(st)
    tab = round(st_len - len(st))
    prob = round(tab/word_count(st))
    for elem in st:
        if elem != ' ':
            word += elem
        else:
            word += ' '
            ns += word
            ns += ' '*prob
            word = ''
    print(ns)
    ns = ''


    if (len(st)-1) != st_len:
        tab = max_len - len(st) + 1
        prob = round(tab/(word_count(st)-2))
        for elem in st:
            if elem != ' ':
                word += elem
            else:
                ns += word
                ns += ' '*(prob)
                word = ''
        print(ns, len(ns), prob, tab)
        ns = ''
    else:
        print(st, len(st))
