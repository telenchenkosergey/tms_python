# Создать родительский класс Auto у которого есть атрибуты: brand, age, cоlor,
# mark и weight. А так же методы: move, birthday и stop. Методы move и stop
# выводят сообщение на экран move и stop, а birthday увеличивает атрибут age
# на 1. Атрибуты brand, age и mark являются обязательными при объявлении
# объекта


class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print(f'{self.brand} {self.mark} move.')

    def birthday(self):
        self.age += 1

    def stop(self):
        print(f'{self.brand} {self.mark} stop.')


mazda = Auto('Mazda', 10, 'white', '6', 1300)
mazda.move()
mazda.stop()
print(mazda.age)
mazda.birthday()
print(mazda.age)
