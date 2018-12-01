def word_len2(line):  # самое длинные слово
    znaki = ';:,.-!?'
    line += ' '
    word = ''
    max_len = 0
    long_word = ''
    for elem in line:
        if elem != ' ' and elem not in znaki:
            word += elem
        elif elem == ' ':
            current_len = len(word)

            if current_len > max_len:
                max_len = current_len
                long_word = word
            word = ''
    if long_word[-1] in znaki:
        return long_word[:-1]
    else:
        return long_word
def word_count2(line):  # количество слов в тексте без учета чисел
    k = 0
  # t = 0
  # znaki = '1234567890-+'
  # l = 0
    for elem in line:
        if elem == ' ':
            k += 1
           # l = 0
        # if elem in znaki and l == 0:  # данная позволяет не учитывать числа
         # t += 1
          # l = 1
    # n = k - t
    return k + 1

def oft2(lines): #  самое частое слово
    sign = '.:;,-?!'
    dictionary = {}
    word = ''
    max_count = 0
    oft_w = ''
    for line in lines:
        line += ' '
        for elem in line:
            if (elem != ' ') and (elem not in sign):
                word += elem
            elif elem == ' ':
                if word not in dictionary.keys():
                    dictionary[word] = 1
                elif word in dictionary.keys():
                    dictionary[word] += 1
                word = ''
    for key in dictionary.keys():
        if dictionary.get(key) > max_count:
            max_count = dictionary.get(key)
            oft_w = key
    return oft_w

def rplc(line,word,change): # замена по шаблону
    string = reword = ''
    sign = '.:;,-?! '
    line += ' '
    sgn = ''
    for elem in line:
        string += elem
        if elem not in sign:
            reword += elem
        else:
            sgn = elem
            if reword == word:
                k = len(string) - len(reword)
                string = string[:k-1] + change + sgn
            reword = ''
    return string


if __name__ == '__main__':
    print(word_count2('a bb ccc dddd'))
    print(word_len2('a bbbbbb ccc'))
    print(oft2('aa bbb aa bbb aa'))
    print(rplc('ham egg, bread', 'egg', 'spam'))








