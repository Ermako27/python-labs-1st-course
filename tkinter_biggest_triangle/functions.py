import math as m

'''
нахождение максимальной длины вектора
аргументы: массив с координатами точек
'''

def max_vector(dots,max_dot = (0,0)):
    max_vec = 0
    for dot in dots:
        vec = sqrt((dot[0] - max_dot[0])**2 + (dot[1] - max_dot[1])**2)
        if vec > max_vec:
            max_vec = vec
            koordinates = dot

    return koordinates
def dlina(x1, y1, x2, y2):
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def S(x1, y1, x2, y2, x3, y3):
    a = dlina(x1, y1, x2, y2)
    b = dlina(x1, y1, x3, y3)
    c = dlina(x3, y3, x2, y2)
    p = (a + b + c) / 2
    return m.sqrt(p * (p - a) * (p - b) * (p - c))


def my_tr(x1, y1, x2, y2, x3, y3, dotx, doty):
    s = S(x1, y1, x2, y2, x3, y3)
    s1 = S(x1, y1, x2, y2, dotx, doty)
    s2 = S(x1, y1, x3, y3, dotx, doty)
    s3 = S(x3, y3, x2, y2, dotx, doty)

    k = round((s1+s2+s3),0)
    s = round((s),0)

    if s == k:
        return 1
    else:
        return 0

def my_circ(dotx, doty, x, y, rad):
    d = m.sqrt((y - doty) ** 2 + (x - dotx) ** 2)

    if d < rad:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #print(max_vector([(1, 1), (4, 4), (2, 2)]))
    #print(S(2,4,5,7,7,1))
