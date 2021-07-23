"""
создайте класс `Car`, наследник `Vehicle`

- в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight=10, fuel=10, fuel_consumption=5):
        super(Car, self).__init__(weight, fuel, fuel_consumption)
        self.engine = Engine

    def set_engine(self, engine: Engine):
        self.engine = engine
        print(f'engine has {self.engine.volume} volume and {self.engine.pistons} pistons')



