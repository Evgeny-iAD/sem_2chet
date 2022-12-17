# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#
# text = 'абв Ура, питон крутой абвязык. очень интересный семинарыабв! абв'
# lst = ' '.join(list(filter(lambda  s: 'абв' not in s, text.split())))
# print(lst)
# 1.1 Поиск недостающего числа в строке
# s = list(map(int, '11 12 13 15 16 17 18 19 20'.split()))     #  деление строки по пробелам и преобразование в int, и преобразование в лист
# a = list(filter(lambda x: x[1]-x[0] == s[0], list(zip(range(len(s)), s))))
# print(a)

# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# import random
# def zhereb(x,y):
#     lst = [x, y]
#     if random.choice(lst) == x:
#         return [x, y]
#     else:
#         return [y, x]
#
# def game(lst):
#     n = 0
#     while n <= 2021:
#         a = int(input(f'{lst[0]} введите число: '))
#         if a <= 28:
#             n = n + a
#         a = int(input(f'{lst[1]} введите число: '))
#         if a <= 28:
#             n = n + a
#         print(n)
#     print('Все')
#
# name1 = 'Игрок 1'
# name2 = 'Игрок 2'
# print(zhereb(name1, name2))
# lst = zhereb(name1, name2)
#
# game(lst)

# 3. Создайте программу для игры в ""Крестики-нолики"".
#
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#rle-encode.py
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
# If the prev and current characters
# don't match...
        if char != prev_char:
    # ...then add the count and character
    # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
        # Or increment our counter
        # if the characters do match
            count += 1
    else:
    # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
# If the character is numerical...
        if char.isdigit():
    # ...append it to our count
            count += char
        else:
    # Otherwise we've seen a non-numerical
    # character and need to expand it for
    # the decoding
            decode += char * int(count)
            count = ''
    return decode


encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)
print(rle_decode(encoded_val))
