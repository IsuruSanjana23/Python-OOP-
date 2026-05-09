class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is Barking.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is Meowing.")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is Making a noise.")

dog = Dog("Scooby")
cat = Cat("Bobby")
mouse = Mouse("Jerry")


dog.speak()
cat.speak()
mouse.speak()