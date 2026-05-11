# ============================================================
# COMPOSITION PATTERN IN PYTHON
# ============================================================
# Composition: A class contains instances of other classes
# "Has-a" relationship rather than "Is-a" (inheritance)
# Benefits: More flexible, reusable, and maintainable
# ============================================================

# Independent class - Engine has its own responsibility
class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power

# Independent class - Wheel has its own responsibility
class Wheel:
    def __init__(self,wheel_size):
        self.wheel_size = wheel_size

# Car class COMPOSES Engine and Wheel objects
# Car doesn't inherit from Engine or Wheel
# Instead, Car "HAS-A" Engine and "HAS-A" Wheel
class Car:
    def __init__(self,brand,model,horse_power,wheel_size):
        self.brand = brand
        self.model = model
        # Create Engine object as an attribute (composition)
        self.engine = Engine(horse_power)
        # Create Wheel object as an attribute (composition)
        self.wheels = Wheel(wheel_size)

    def display(self):
        # Access composed objects through dot notation
        return f"{self.brand} {self.model} with {self.engine.horse_power} HP and {self.wheels.wheel_size} inch wheels"

# Example usage: Create a Car that CONTAINS Engine and Wheel
bmw = Car("BMW" , "i8" , 1000 , 21)
print(bmw.display())