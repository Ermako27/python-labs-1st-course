from random import randint
n = randint(3,11)
a = [[randint(1,5) for j in range(n)] for i in range(n)]
b = a[:]
print('Матрица до изменения.')
for el in a:
    print(' '.join([str(elem) for elem in el]))

for i in range(n):
    for j in range(i,(n-1-i)):
        k = a[i][j]
        a[i][j] = a[n-j-1][i]
        a[n-j-1][i] = a[n-i-1][n-j-1]
        a[n-i-1][n-j-1] = a[j][n-i-1]
        a[j][n-i-1] = k

print('Поворот марицы по часовой стрелке.')
for el in a:
    print(' '.join([str(elem) for elem in el]))

    
for i in range(n):
    for j in range(i,(n-1-i)):
        t = b[i][j]
        b[i][j] = b[j][n-1-i]
        b[j][n-1-i] = b[n-1-i][n-1-j]
        b[n-1-i][n-1-j] = b[n-1-j][i]
        b[n-1-j][i] = t

print('Поворот матрицы против часовой стрелки.')
for el in b:
    print(' '.join([str(elem) for elem in el]))
        
