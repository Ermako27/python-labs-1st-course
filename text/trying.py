a = 'max 4+4+4 ate 2+2 apples 4+4  qwre - qwer 5+5'
num = '1234567890'
s1 = ''
s2 = ''
oper = '-+'
'''
k = 0
p = 0
m = 0
for w in a:
    if w in num and k != 2: 
        s1 += w
        k = 1
        #print('k',k)
    elif w in oper and k == 1:
        if w == '+':
            p = 1
        elif w == '-':
            m = 1
        k = 2
    elif w in num and k == 2:
        s2 += w
    else:
        k = 0

'''


 # замена выражений (+-) на результат
num_mass = '1234567890'
znaki = '+- '
flag = cnt1 = cnt1_1 = 0
num1 = num2 = ''
s1_1 = s2_2 = ''
s1 = s2 = ''
new_string = z = ''
p = k = t = q = 0
kolvo = 0
fl = 0
# разбиение до и после знака
for w in a:
    if w in num_mass: # в этих 3 проверках считается
        q = 1
    if w == '-' or w == '+' and q == 1: # сколько выражений в тексте
        t = 1
    if w in num_mass and t == 1:
        kolvo += 1 # количество выражений
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
print('s1 ',s1)
print('s2 ',s2)

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

print('s1 ',s1)
print('s2 ',s2)
print('s1_1 ', s1_1)
print('s2_2 ', s2_2)
print('num1', num1)
print('num2', num2)
print(new_string)
print('kolvo', kolvo)
        
#if __name__ == '__main__:
    
  
    

        
  
        
        
    
