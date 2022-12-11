# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# def f(x):
#     su = 0
#     for i in x:
#         su = su + i
#     return su
#
# def is_float(str):
#     try:
#         float(str)
#         return float(str)
#     except ValueError:
#         return False
#
# def math(f, list):
#     print(f'{list}, сумма {f(list)}')
#
# s = input('введите произвольное число: ')
#
# if is_float(s) != False:
#     list = [int(i) for i in s if i != '.']
#     math(f, list)
# else:
#     print('Введено не число!')

# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# n = 4
#
# def f(x):
#     j = 1
#     for i in range(1, x+1):
#         j = j*i
#     return j
#
# list = [f(i) for i in range(1, n+1)]
#
# print(list)

# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#
# *Пример:*
#
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06
# n = 4
#
# def f(x):
#     return round((1 + 1/x)**x, 2)
#
# def g(x):
#     su = 0
#     for i in x:
#         su = su + i
#     return su
#
# list = [f(i) for i in range(1, n+1)]
#
# print(f'{list}\n сумма {g(list)}')

# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .
#
# def f(x, lis):
#     for i in lis:
#         if i == x:
#            return x
#
# def list_3(f, data, list1):
#     return [i for i in list1 if f(list1.index(i), data) != None]
#
# def g(lis):
#     su = 1
#     for i in lis:
#         su = su*i
#     return su
#
# list1 = [4, 5, 6, 7]
#
# data = list(map(int, '1 3'.split()))
# # data = '1, 2'.split()
#
# res = list_3(f, data, list1)
# res = g(res)
#
# print(res)

# 5) Реализуйте алгоритм перемешивания списка.
import random

list1 = [i for i in range(1, 20)]
print(list1)
random.shuffle(list1)
print(list1)

