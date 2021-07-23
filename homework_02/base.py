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

from homework_02.exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):

    def __init__(self, weight=10, fuel=1000, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError("Low fuel")

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance > distance:
            fuel_trip = distance*self.fuel_consumption
            self.fuel -= fuel_trip
            return self.fuel
        else:
            raise NotEnoughFuel("Not enough fuel")

    def __str__(self):
        return f'fuel: {self.fuel} ; consumption: {self.fuel_consumption}'


# if __name__ == '__main__':

    # v1 = Vehicle()
    # v1.start()
    # print(v1)
    # v1.move(10)



