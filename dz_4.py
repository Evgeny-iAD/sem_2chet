# 1. Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def primfacs(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#    if n > 1:
#        primfac.append(n)
#    return primfac
#
# print(primfacs(998))
# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []
#
# n = 1113384455229
#
# def f(x):
#     k = 0
#     listr = []
#     for i in x:
#         for j in x:
#             if j == i:
#                 k += 1
#             if k == 2:
#                 break
#         if k == 1:
#             listr.append(int(i))
#         k = 0
#     return listr
#
# list1 = [i for i in str(n)]
#
# print(f(list1))


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
# import random
# k = 2
#
# def f(x):
#     list_res = ''
#     for i in range(x, -1, -1):
#         k = random.randint(-100,100)
#         ii = f'x^{i}'
#         if i == 1:
#             ii = 'x'
#         elif i == 0:
#             ii = ''
#         if k < 0:
#             list_res = list_res + f' {k}{ii} '
#         elif k > 0:
#             if i == x:
#                 list_res = list_res + f' {k}{ii} '
#             else:
#                 list_res = list_res + f'+ {k}{ii} '
#
#     return list_res + ' = 0'
#
# print(f(k))
# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 3x + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 10x + 53 = 0

with open('x1.txt') as f1:
    x1 = f1.readline()

with open('x2.txt') as f2:
    x2 = f2.readline()


def f(x):
    y = ''
    for i in x:
        if i != '=':
            y = y + i
        else:
            break
    return y


def g(x):
    if x == '-':
        return '+-'
    else:
        return x


def s(x):
    return list(g(i) for i in x if i != ' ')


def colobora(x):
    num = {}
    for i in x:
        if i.find("x^") != -1:
            part_n, part_x = i.split("x^")
            num[int(part_x)] = int(pusto(part_n))
        elif i.find("x") != -1:
            part_n, part_x = i.split("x")
            num[int(pusto(part_x))] = int(pusto(part_n))
        else:
            num[0] = int(i)
        # i = i[:poz]
    return num


def pusto(x):
    if x == '':
        return 1
    return x


def max_key(x, y):
    maxi = 0
    for i in x.keys():
        if i > maxi:
            maxi = i
    for j in y.keys():
        if j > maxi:
            maxi = j
    return maxi


def proverka(x, i):
    try:
        return x[i]
    except:
        return 0

def sum(x, y):
    su = {}
    res = ''
    for i in range(max_key(x, y), -1, -1):
        su[i] = proverka(x, i) + proverka(y, i)
    for j in su:
        if j == 1:
            if su[j]<0: res = res + f'{su[j]}x'
            else: res = res + f'+{su[j]}x'
        elif j == 0:
            if su[j] < 0: res = res + f'{su[j]}=0'
            else: res = res + f'+{su[j]}=0'
        else:
            if su[j] < 0: res = res + f'{su[j]}x^{j}'
            else:  res = res + f'+{su[j]}x^{j}'
    return res




# print(x1)
# print(x2)

x3 = f(s(x1)).split('+')
x4 = f(s(x2)).split('+')

# print(f'{x3}')
# print(f'{x4}\n')

print(colobora(x3))
print(colobora(x4))

print(sum(colobora(x3), colobora(x4)))
