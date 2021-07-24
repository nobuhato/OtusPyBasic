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
        max_distance = self.fuel / self.fuel_consumption
        if max_distance >= distance:
            fuel_trip = distance * self.fuel_consumption
            self.fuel -= fuel_trip
            return self.fuel
        else:
            raise NotEnoughFuel("Not enough fuel")

    def __str__(self):
        return f'fuel: {self.fuel} ; consumption: {self.fuel_consumption}'



