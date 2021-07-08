"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class NotEnoughFuel(BaseException):
    raise Exception("Not enough fuel")
