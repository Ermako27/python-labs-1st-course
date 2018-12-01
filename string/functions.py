def midle_let(s, ln):
    ml = int((ln-1)/2)
    s1 = s[:ml]
    s2 = s[ml+1:]
    return s1 + s2

if __name__ == '__main__':
    print(midle_let('1234567', 7))
