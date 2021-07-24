from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo=1000):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_amount):
        if self.max_cargo > self.cargo + cargo_amount:
            self.cargo += cargo_amount
            return self.cargo
        else:
            raise CargoOverload("Cargo overloaded")

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

    def __str__(self):
        return f'{self.cargo}'



