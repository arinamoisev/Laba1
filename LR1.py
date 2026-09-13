import numpy as np
from PIL import Image
from math import *

img_mat = np.zeros((1000,1000,3), dtype = np.uint8)  # матрица

# рисуем квадрат красивый, если хотим градиент, то функцию, а не цвета
#for i in range(1000):
#      for j in range(1000):
#         img_mat[i,j] = 255, 200, 180 # градация серого, полутон (i+j)%256 и ноль после j

# рисуем линии
def line(img_mat,x0,y0,x1,y1):
    d_max = max(abs(floor(x0) - floor(x1)), abs(floor(y0) - floor(y1)))
    L = d_max + 1
    if L == 1:
        px = floor(x0)
        py = floor(y0)
        img_mat[py, px] = 255
        return

    Dx = (x1 - x0) / (L - 1)
    Dy = (y1 - y0) / (L - 1)
    x, y = x0, y0
    for _ in range(L):  # рисуем линию
        img_mat[floor(y), floor(x)] = 255, 140, 185
        x += Dx
        y += Dy
#line(img_mat,100, 200, 334, 344)
#line(img_mat,109, 334, 654, 234)

file = open('model.obj')
v = []  # храниться будуь точки
f = []
for s in file:
    sp = s.split()
    if sp[0]=='v':
        v.append([float(x) for x in sp[1:4]])
    if sp[0]=='f':
        f.append([int(sp[1].split('/')[0]),int(sp[2].split('/')[0]),int(sp[3].split('/')[0])])
#print(v)
#print(f)

# рисуем зайца треугольниками
for i in range(len(f)):  # f[i] номера вершин i треугольника v[f[i][0]-1][0] полигон вершина координата
    x0 = 5000*v[f[i][0]-1][0]+500
    y0 = -5000*v[f[i][0]-1][1]+700
    x1 = 5000 * v[f[i][1] - 1][0] + 500
    y1 = -5000 * v[f[i][1] - 1][1] + 700
    x2 = 5000 * v[f[i][2] - 1][0] + 500
    y2 = -5000 * v[f[i][2] - 1][1] + 700
    line(img_mat,x0,y0,x1,y1)
    line(img_mat, x0, y0, x2, y2)
    line(img_mat, x1, y1, x2, y2)

# рисуем зайца по точкам
for i in range(len(v)):
    x = 5000*v[i][0]+500
    y = -5000*v[i][1]+700  # выравниывем по центру, добавляем половину
 #   img_mat[floor(y), floor(x)] = 255, 140, 185  # красный зеленый синий



img = Image.fromarray(img_mat)  # сохранение
img.save('img.png')
