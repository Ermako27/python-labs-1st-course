from functions import max_vector
from tkinter import *


n = int(input('Введите количество точек: '))
dots = []  # массив координат всех точек
triangle = [] # координаты точек треугольника
for i in range(n):  # ввод координат точек
    koordinates = tuple([int(x) for x in input('Введите координаты точки: ').split()])
    dots.append(koordinates)

flag = 1
for i in range(3):
    if flag:
        dot = max_vector(dots)
        triangle.append(dot)
        dots.remove(dot)
        flag = 0
    else:
        dot = max_vector(dots, triangle[0])
        triangle.append(dot)
        dots.remove(dot)
S = (triangle[0][0] - triangle[2][0])*((triangle[1][1] - triangle[2][1])) - \
    ((triangle[1][0] - triangle[2][0]))*((triangle[0][1] - triangle[2][1]))

if S == 0:
    print('Точки лежат на одной прямой')
else:
#print(triangle)
#print(dots)

# Рисунок

    root = Tk()
    canv = Canvas(root,width=2000, height=2000, bg='white')
    x1, y1 = triangle[0][0]*100, triangle[0][1]*100
    x2, y2 = triangle[1][0]*100, triangle[1][1]*100
    x3, y3 = triangle[2][0]*100, triangle[2][1]*100

    canv.create_line(x1, y1, x2, y2, width=2)
    canv.create_line(x2, y2, x3, y3, width=2)
    canv.create_line(x3, y3, x1, y1, width=2)

    dots = triangle + dots
    for i in range(len(dots)):
        x = dots[i][0] * 100
        y = dots[i][1] * 100
        canv.create_oval(x - 5, y - 5, x + 5, y + 5, width=1, fill='red')

    canv.pack()
    root.mainloop()