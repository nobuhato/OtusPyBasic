"""
создайте класс `Plane`, наследник `Vehicle`
в модуле `plane` создайте класс `Plane`
    - класс `Plane` должен быть наследником `Vehicle`
    - добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    - добавьте `max_cargo` в инициализатор (переопределите родительский)
    - объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение(какое значение оновляет???), в ином случае выкидывает исключение `exceptions.CargoOverload`
    - объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления
"""

from base import Vehicle


class Plane(Vehicle):
    cargo = 100
    tmp = 0

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, i):
        Plane.tmp = Plane.cargo
        Plane.cargo += i
        if self.max_cargo > Plane.cargo:
            return Plane.cargo
        else:
            raise Exception("Cargo exception")

    @staticmethod
    def remove_cargo():
        Plane.cargo = Plane.tmp
        Plane.tmp = 0
        print(Plane.cargo)

    def __str__(self):
        return f'{self.cargo}'


if __name__ == '__main__':
    p1 = Plane(1200, 10000, 100, 10)
    p1.load_cargo(20)
    print(p1)
    p1.remove_cargo()
