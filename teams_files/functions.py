import data as d
def field_search(l): # поиск по полю в каждой строке
    search_file = open('search.txt', 'w') # Открытие файла для результатов
    s = input(d.search) # команда, вводимая пользователем
    if s == '5':
        team = input('Какую команду искать? ')
        for line in l:
            if team in line:
                search_file.write(line)
        search_file.close()
    if s == '6':
        goals = input('Введите количество голов: ')
        for line in l:
            if goals in line:
                search_file.write(line)
        search_file.close()
    if s == '7':
        pos = input('Введие позицию: ')
        for line in l:
            if pos in line:
                search_file.write(line)
        search_file.close()

def menu(file_name): # основное меню
    actions = '01234'
    while True:
        action = input(d.next_phrase)
        if action not in actions:
            print('Вы ввели неверную команду.')
            continue
        if action == '1': # создание нового файла
            file_name = input(d.name)
            f = open('%s.txt' % file_name, 'w')
            for position in d.positions:
                f.write(position + '\n')
            print(d.new_name)
            f.close()
        if action == '2': # добавление новой записи
            new_note = input(d.note)
            f = open('%s.txt' % file_name, 'a')
            f.write(new_note + '\n')
            f.close()
        if action == '3': # Чтение из файла
            f = open('%s.txt' % file_name, 'r')
            for line in f:
                line = line[:-1]
                print(line)
            print('\n')
            f.close()
        if action == '4': # поиск по файлу
            f = open('%s.txt' % file_name, 'r')
            lst = f.readlines()
            field_search(lst)
        if action == '0':
            print(d.exit)
            break
