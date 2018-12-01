import data as d
import functions
'''
0 - выход
1 - создание файла
2 - добавление в существующий файл
3 - вывод содержимого файла
4 - поиск по полю и запись в отдельный файл
'''
start = input(d.start_phrase)
if start == '1':
    file_name = input(d.name) # ввод названия файла
    f = open('%s.txt' % file_name, 'w')
    for position in d.positions: # заполнение файла
        f.write(position + '\n')
    f.close()
    print(d.congrat_phrase)
    functions.menu(file_name) # вызов основного меню


if start == '0':
    print(d.exit)




