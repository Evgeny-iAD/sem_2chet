# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def g(x):
#     su = 0
#     for i in x:
#         su = su + i
#     return su
# list1 = [i for i in range(1, 6)]
# list2 = list(filter(lambda x: not x%2, list1))
# sum = g(list2)
# print(list1)
# print(list2)
# print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def g(x):
#     j=1
#     su =[]
#     for i in range(0, int(len(x)/2+0.5)):
#         s = x[i]*x[len(x)-j]
#         j = j + 1
#         su.append(s)
#     return su
#
# list1 = [2, 3, 4, 5, 6]
#
# print(int(len(list1)/2))
# print(len(list1))
# print(g(list1))

#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
# def f(x):
#     return round(x % 1, 2)
#
# def g(l):
#     max = l[0]
#     min = l[0]
#     for i in l:
#         if i >= max:
#             max = i
#         else:
#             if i !=0 and i < min:
#                 min = i
#     return (max - min)
#
# list1 = [1.1, 1.2, 3.1, 5, 10.01]
#
# list2 = [f(i) for i in list1]
#
# print(list2)
# print(g(list2))


#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101


# number = 45
#
# def f(x):
#     num = ''
#     while x>0:
#         num = str(x%2)+ num
#         x = x // 2
#     return num
#
# print(f(number))
# print(bin(45))




#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = fib2 = 1

k = 8

print(0, fib1, fib2, end=' ')

for i in range(2, k):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

# Херня какая то