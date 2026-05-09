import math


class Shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

    def describe(self):
        return f"It is {self.color} and {'filled' if self.filled else 'not filled'}."

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius

    def Area(self):
        return math.pi * self.radius ** 2

    def describe(self):
        return f"{super().describe()}\nThe area of the circle with radius {self.radius} is {self.Area()}"


class Square(Shape):
    def __init__(self,color,filled,width,height):
        def __init__(self,color,filled,radius):
            super().__init__(color,filled)
        self.width = width
        self.height = height
    def Area(self):
        return  self.width * self.height

class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height

    def Area(self):
        return self.width * self.height * 0.5

circle = Circle("red",False,0.2)
square = Square("blue",1,5 , 23)
triangle = Triangle("green",1,0.2 , 2)

print(circle.Area())
print(circle.describe())
