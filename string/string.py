# Ермаков Максим ИУ7-14
from functions import midle_let


s = input('Введите строку: ').split()
#print(s)
ln = len(s)
f_word = s[0]
s[0] = '.'
#print(s)

#print(f_word, s)
for i in range(ln):
    if s[i] == f_word:
        s[i] = ''
        #s.remove(s[i])
        #s.append('')
        #print('s', s)
    if len(s[i]) % 2 != 0 and len(s[i]) > 1 and s[i] != f_word:
        s[i] = midle_let(s[i], len(s[i]))
s[0] = f_word        
new_string = ' '.join(s)


print('Отредактированная строка: ', new_string)


    
        
    
