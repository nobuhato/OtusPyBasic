""""- доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`, который, если ещё не состояние `started`, проверяет, что топлива больше нуля,
      и обновляет состояние `started`, иначе выкидывает исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет,
      что достаточно топлива для преодоления переданной дистанции,
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
"""

from abc import ABC


# from exceptions import NotEnoughFuel

class Vehicle(ABC):

    started = False

    def __init__(self, weight=10, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            started = True
            return started
        else:
            raise Exception("not enough fuel")

    def move(self, distance):
        possible_distance = float(self.fuel/self.fuel_consumption)
        if possible_distance >= distance:
            possible_distance -= distance
            print(f'possible distance: {possible_distance}')
        else:
            raise Exception("Not enough fuel")

    def __str__(self):
        return f'fuel: {self.fuel} ; consumption: {self.fuel_consumption}'


if __name__ == '__main__':
    w = 20
    f = 1000
    fc = 5

    v1 = Vehicle(w, f, fc)
    v1.start()
    print(v1)
    v1.move(10)
