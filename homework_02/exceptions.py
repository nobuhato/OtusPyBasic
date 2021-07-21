from exceptions import BaseException
"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(BaseException):
    pass


class NotEnoughFuel(BaseException):
    # raise Exception("Not enough fuel")
    pass


class CargoOverload(BaseException):
    pass



