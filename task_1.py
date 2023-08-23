"""
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


from task6_sem import Animal, Fishes, Birds, Mammals


class AnimalsFactory:
    def __init__(self):
        self.dict_type_str = {str(item.__name__): item for item in Animal.__subclasses__()}
        self.list_type_cls = Animal.__subclasses__()

    def create_animal(self, type_animal, *args):
        if type(type_animal) == str:

            if self.dict_type_str.get(type_animal) is None:
                raise ValueError('Такого вида животного нет')

            return self.dict_type_str[type_animal](*args)
        else:
            if type_animal in self.list_type_cls:
                return type_animal(*args)
            else:
                raise ValueError('Нe входит в класс животных')


if __name__ == '__main__':
    fabric = AnimalsFactory()
    fish = fabric.create_animal(Fishes, 'Карась', 'Федя', 1, 15)
    bird = fabric.create_animal(Birds, 'Синичка', 'Невеличка', 1, 'зеленый')
    animal = fabric.create_animal(Mammals, 'Коала', 'Милашка', 5, 'Сумчатый медведь')

    print(fish.get_kind())
    print(bird.get_specific())
    print(animal.get_specific())