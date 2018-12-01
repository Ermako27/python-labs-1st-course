def word_len(string): # самое длинное слово
    znak = ';:,.-!?'
    string = string.split()
    line = [] # копия массива с исходным текстом со всеми словами без знаков
    for word in string: # отсекаем знаки от слов т.к. они учитываются в длинне
        if word[-1] in znak:
            line.append(word[:-1])
        else:
            line.append(word)
    biggest_word = sorted(line, key=lambda w: len(w))[-1]
    if biggest_word[-1] in znak:
        return biggest_word[:-1]
    else:
        return biggest_word

def oft(lines): # самое частое слово
    znak = ';:,.-!?'
    t = ' '.join(lines)
    mass_words = t.split()
    wd = ''
    cnt = 0
    text = []
    for word in mass_words:  # цикл для отсечения знака в конце слова
        if word[-1] in znak: # так как при подсчете одно слово со знаком
            text.append(word[:-1])  # и без отличаются
        else:
            text.append(word)
    for word in text:
        if text.count(word) > cnt:
            cnt = text.count(word)
            wd = word
    return wd
def word_count(line):  # количество слов в тексте без учета чисел
    k = 0
  #  t = 0
  #  znaki = '1234567890-+'
  #  l = 0
    for elem in line:
        if elem == ' ':
            k += 1
           # l = 0
        #if elem in znaki and l == 0:  # данная позволяет не учитывать числа
         #   t += 1
          #  l = 1
    #n = k - t
    return k + 1

def exp(a): # замена выражений (+-) на результат
    num_mass = '1234567890'
    znaki = '.,!?:;+- '
    flag = cnt1 = cnt1_1 = 0
    num1 = num2 = ''
    s1_1 = s2_2 = ''
    s1 = s2 = ''
    new_string = z = ''
    p = k = t = q = 0
    kolvo = 0
    fl = 0
    # разбиение до и после знака
    '''
    в первых 3 if производится подсчет выражений состоящих из знака и цифр
    переменное kolvo - количетсво таких выражений
    
    '''
    for w in a:
        if w in num_mass:  
            q = 1
        if w == '-' or w == '+' and q == 1:  
            t = 1
        if w in num_mass and t == 1:
            kolvo += 1  
            q = 0
            t = 0

        if w == '+' or w == '-' and k == 0:
            z = w
            k = 1
        if w != z and flag == 0:
            s1 += w
            if w == ' ':
                cnt1 += 1
        elif w == z:
            flag = 1
        if flag == 1:
            s2 += w

    # часть строки до знака
    for w in s1:
        if cnt1_1 != cnt1:
            s1_1 += w
        if w == ' ':
            cnt1_1 += 1
        if cnt1_1 == cnt1:
            num1 += w
    # число перед знаком
    if num1 != ' ':
        num1 = int(num1)

    # часть строки после знака
    for w in s2:
        if w in znaki and fl == 0:
            num2 += w
            fl = 1
            continue
        if (w not in znaki) and fl == 1:
            num2 += w
        if w in znaki and fl == 1:
            fl = 2
        if fl == 2:
            s2_2 += w
    # число после знака
    if num1 == ' ':
        num2 = ''
    else:
        num2 = int(num2)

    # если вокруг знака нет чисел, то в строке просто останется сам знак
    if num1 != ' ':
        num = str(num1 + num2)
        new_string = s1_1 + num + s2_2
    elif num1 == ' ':
        new_string = s1_1 + z + s2_2

    if kolvo != 1:
        return exp(new_string)
    else:
        return new_string






if __name__ == '__main__':
    print(word_len('qqqw rew qwerwqerwer qwerw qwer'))
    print(oft(['aaa aaa', 'aaa bbb', 'aaa ccc']))
    print(exp('qwer qwer 4+4+4-5 qwer qwer 5+5 qwer qwer'))
    print(word_count('Поют всё песнь одну и ту же'))
