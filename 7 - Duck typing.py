class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    alive = True

    def speak(self):
        print("Wroom!")

objects = [Dog(),Cat(),Car()]

for obj in objects:
    obj.speak()
    print(obj.alive)