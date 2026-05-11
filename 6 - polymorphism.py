import math
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Square(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)

shapes = [Circle(2) , Square(12,2) , Triangle(4,2)]
for shape in shapes:
    print(f"Area: {shape.area()}")