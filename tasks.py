'''
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

my_list = [1, 1, 2, 3, 3, 3, 4]

dupl_elem = set()
for el in range(len(my_list)):
    if my_list.count(my_list[el]) > 1:
        dupl_elem.add(my_list[el])
print(f"С применением множеств: {list(dupl_elem)}")

dupl_elem = []
for el in range(len(my_list)):
    if my_list.count(my_list[el]) > 1 and dupl_elem.count(my_list[el]) < 1:
        dupl_elem.append(my_list[el])
print(f"Без применения множеств: {dupl_elem}")

'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

import operator

with open("text.txt") as file:
    text = file.read().lower().replace(",", "").replace(".", "").split()

TOP_WORDS = 10
count_words = 0
dct = {}

for el in range(len(text)):
    dct.update([(text[el], text.count(text[el]))])
sorted_dct = dict(sorted(dct.items(), key=operator.itemgetter(1)))

for key, value in reversed(sorted_dct.items()):
    count_words += 1
    print(f'#{count_words} {key} {value}')
    if count_words == TOP_WORDS:
        break




'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
'''

travel_items = {'Палатка': 5, 'Спальник': 1, 'Гиря': 16, 'Котелок': 1, 'Вода': 2, 'Еда': 3}
backpack_capacity = 7
res_dict = {}
weight = 0

for key, value in travel_items.items():
    if weight + value > backpack_capacity:
        continue
    if weight <= backpack_capacity:
        res_dict.update(dict([(key, value)]))
        weight += value
print(*res_dict, sep=", ")