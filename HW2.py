"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

from math import sqrt

a, b, c = 1, -6, 13

d = b ** 2 - 4 * a * c
if d < 0:
    # x1 = -b / (2 * a) + sqrt(d) / (2 * a)
    # x2 = -b / (2 * a) - sqrt(d) / (2 * a)
    sqrt_d = sqrt(abs(d))
    print(f"Дискриминант: {d}; x1 = {-b / (2 * a)} + {sqrt_d / (2 * a)}i; x1 = {-b / (2 * a)} - {sqrt_d / (2 * a)}i")
elif d == 0:
    x = -b / (2 * a)
    print(f"Дискриминант: {d}; x = {x}")
else:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print(f"Дискриминант: {d}; x1 = {x1}; x2 = {x2}")


    """
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

num_dec = int(input("Введите число: "))
res = ''
DIVIDER = 16

print(hex(num_dec))

while num_dec > 0:
    if num_dec % DIVIDER < 10:
        res = str(num_dec % DIVIDER) + res
    elif num_dec % DIVIDER == 10:
        res = 'A' + res
    elif num_dec % DIVIDER == 11:
        res = 'B' + res
    elif num_dec % DIVIDER == 12:
        res = 'C' + res
    elif num_dec % DIVIDER == 13:
        res = 'D' + res
    elif num_dec % DIVIDER == 14:
        res = 'E' + res
    elif num_dec % DIVIDER == 15:
        res = 'F' + res
    num_dec //= DIVIDER

print(res)



"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

frac1 = input("Введите первую дробь: ")
frac2 = input("Введите вторую дробь: ")

numer1, denomin1 = map(int, frac1.split("/"))
numer2, denomin2 = map(int, frac2.split("/"))

f1 = Fraction(numer1, denomin1)
f2 = Fraction(numer2, denomin2)
print(f"\n*ПРОВЕРКА* Сумма дробей: {f1 + f2}, Произведение дробей: {f1 * f2} \n")

if denomin1 != denomin2:
    numer_sum = numer1 * denomin2 + numer2 * denomin1
    denomin_sum = denomin1 * denomin2
else:
    numer_sum = numer1 + numer2
    denomin_sum = denomin1

numer_prod = numer1 * numer2
denomin_prod = denomin1 * denomin2

print(f"Сумма дробей: {numer_sum}/{denomin_sum}")
print(f"Произведение дробей: {numer_prod}/{denomin_prod}")