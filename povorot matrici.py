# Ермаков Максим ИУ7-14

from random import randint
n = int(input('Введите размерность матрицы: '))

a = [[randint(1,9) for j in range(n)] for i in range(n)]
print('\nМатрица до изменения.')
for el in a:
    print(' '.join([str(elem) for elem in el]))
while True:
    choice = int(input('\n1 если по часовой, 2 если портив часовой: '))
    if choice == 1:
        
        for i in range(n):
            for j in range(i,(n-1-i)):
                k = a[i][j]
                a[i][j] = a[n-j-1][i]
                a[n-j-1][i] = a[n-i-1][n-j-1]
                a[n-i-1][n-j-1] = a[j][n-i-1]
                a[j][n-i-1] = k

        print('\nПоворот марицы по часовой стрелки.')
        for el in a:
            print(' '.join([str(elem) for elem in el]))

    
    if choice == 2:
        for i in range(n):
            for j in range(i,(n-1-i)):
                t = a[i][j]
                a[i][j] = a[j][n-1-i]
                a[j][n-1-i] = a[n-1-i][n-1-j]
                a[n-1-i][n-1-j] = a[n-1-j][i]
                a[n-1-j][i] = t

        print('\nПоворот матрицы против часовой стрелки.')
        for el in a:
            print(' '.join([str(elem) for elem in el]))
        
