# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_distance(dot_1, dot_2):
     s = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(s, 2)
print(dot_distance(dot_1, dot_2))

# xa = float(input("Введите координату Х точки А: "))
# ya = float(input("Введите координату Y точки А: "))
# xb = float(input("Введите координату Х точки B: "))
# yb = float(input("Введите координату Y точки B: "))
# result = round(((xb-xa)**2+(yb-ya)**2)**0.5, 2)
# print(result)