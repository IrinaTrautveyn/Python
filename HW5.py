"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

import os


def elems_path(my_path):
    return os.path.split(my_path)[0], *os.path.split(my_path)[-1].split('.')


print(elems_path('c:/Users/User/Desktop/Python/HW5.py/HW5.py'))


"""
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""


def gen_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in
            zip(names_list, salaries_list, bonuses_list)}


names, salaries, bonuses = ["Ирина", "Антон", "Павел"], [1500, 3000, 5000], ["10%", "15%", "20%"]

print(gen_salary_dict(names, salaries, bonuses))



"""
Создайте функцию генератор чисел Фибоначчи
"""

import itertools


def gen_fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


print(list(itertools.islice(gen_fib(), 100)))