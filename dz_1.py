# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# num_den = int(input('Введите число дня недели: '))
#
# for i in range(1, 8, 1):
#     if i == num_den:
#         if num_den == 6 or num_den == 7:
#             print('Да')
#         else:
#             print('Нет')

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# def tabl1():
#     print('\nВыражение 1:')
#     stroka = ''
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 print(f'{x}  {y}  {z}  ¬(X⋁Y⋁Z) = {not_disjunctio(x, y, z)}')
#                 stroka = stroka + str(not_disjunctio(x, y, z))
#     return stroka
#
# def tabl2():
#     print('\nВыражение 2:')
#     stroka = ''
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 print(f'{x}  {y}  {z}  X⋀Y⋀Z = {conjunctio_not(x, y, z)}')
#                 stroka = stroka + str(conjunctio_not(x, y, z))
#     return stroka
#
# def not_disjunctio(x, y, z):
#     if x == 1 or y == 1 or z == 1:
#         return 0
#     else:
#         return 1
#
# def inversion(a):
#     if a == 0:
#         return 1
#     else:
#         return 0
# def conjunctio_not(x, y, z):
#     if inversion(x) == 1 and inversion(y) == 1 and inversion(z) == 1:
#         return 1
#     else:
#         return 0
#
# if tabl1() == tabl2():
#     print('\nВыражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  истино')
# else:
#     print('\nВыражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  лож')

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится)
#
# def search_quarter(x, y):
#     return {
#             x > 0 and y > 0: 'Первая четверть',
#             x < 0 and y > 0: 'Вторая четверть',
#             x < 0 and y < 0: 'Третья четверть',
#             x > 0 and y < 0: 'Четвертая четверть'
#             }[True]
#
# x = int(input('Введите координату Х: '))
# y = int(input('Введите координату Y: '))
#
# if x != 0 and y != 0:
#     print(search_quarter(x, y))

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# def search_koord(x):
#     if 1 <= x <= 4:
#         return {
#                 x == 1: '(0 < x < +∞, 0 < y < +∞)',
#                 x == 2: '(-∞ < x < 0, 0 < y < +∞)',
#                 x == 3: '(-∞ < x < 0, -∞ < y < 0)',
#                 x == 4: '(0 < x < +∞, -∞ < x < 0)'
#                 }[True]
# def is_int(str):
#     try:
#         int(str)
#         return int(str)
#     except ValueError:
#         return False
#
# n = is_int(input('Введите четверть цифрой (Пример: 1): '))
# if n != False:
#     print(search_koord(n))
# else:
#     print('Введено не число!')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def size(a, b):
    return ((a[1]-a[0])**2 + (b[1]-b[0])**2)**0.5

a = [-1, 7]
b = [7, 1]

print(size(a, b))
