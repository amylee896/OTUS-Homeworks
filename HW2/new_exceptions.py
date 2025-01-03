"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __str__(self):
        return 'The amount of fuel is too low!'

class NotEnoughFuel(Exception):
    def __str__(self):
        return 'The amount of fuel is not enough for the intended distance'

class CargoOverload(Exception):
    def __str__(self):
        return 'The weight of cargo exceeds the maximum!'