class Rectangle:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self,width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")

    @height.setter
    def height(self,height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive")

    @width.deleter
    def width(self):
        del self.__width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("height deleted")

r1 = Rectangle(10,10)

r1.width = 100
r1.height = 200

del r1.width

print(r1.width)
print(r1.height)
