"""
создайте класс `Plane`, наследник `Vehicle`
в модуле `plane` создайте класс `Plane`
    - класс `Plane` должен быть наследником `Vehicle`
    - добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    - добавьте `max_cargo` в инициализатор (переопределите родительский)
    - объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение(какое значение оновляет???), в ином случае выкидывает исключение `exceptions.CargoOverload`
    - объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, max_cargo=1000, *args):
        super(Plane, self).__init__(*args)
        self.max_cargo = max_cargo
        self.cargo = 100

    def load_cargo(self, cargo_amount):
        if self.max_cargo > self.cargo:
            return self.cargo + cargo_amount
        else:
            raise CargoOverload("Cargo overloaded")

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

    def __str__(self):
        return f'{self.cargo}'




# if __name__ == '__main__':
#     p1 = Plane()
#     p1.load_cargo(cargo_amount=20)
#     print(p1.remove_all_cargo())
