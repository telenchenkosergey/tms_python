# Создать 2 класса Truck и Car, которые являются  наследниками класс Auto.
# Класс Truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи move выводит надпись
# attention, его реализацию сделать при помощи оператора super. А также
# дополнительный метод load. При его вызове происходит пауза 1 сек, затем
# выдается сообщение load, и снова пауза 1 сек. Класс Car имеет дополнительный
# обязательный атрибут max_speed и при вызове move, после появления надписи
# move должна появиться надпись max_speed is <max_speed>. Создать по два объекта
# для каждого из классов, проверить все их методы и атрибуты.


from auto import Auto
import time


class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        Auto.__init__(self, brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)

    def __str__(self):
        return f'{self.color} {self.brand} {self.mark}: {self.age} years'\
            f' old.\nWeight: {self.weight}\nMax Load: {self.max_load}'


class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        Auto.__init__(self, brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max Speed: {self.max_speed} km/h')

    def __str__(self):
        return f'{self.color} {self.brand} {self.mark}: {self.age} years'\
            f' old.\nWeight: {self.weight}'


mercedes = Truck('Mercedes', 23, 'White', 'Atego', 3500, 5000)
print(mercedes)
mercedes.load()
mercedes.move()

daf = Truck('DAF', 15, 'Red', 'XF', 4000, 13000)
print(daf)
daf.load()
daf.move()

mazda = Car('Mazda', 10, 'Green', '6', 1300, 180)
print(mazda)
mazda.move()

peugeot = Car('Peugeot', 20, 'Silver', '307', 1500, 160)
print(peugeot)
mazda.move()
