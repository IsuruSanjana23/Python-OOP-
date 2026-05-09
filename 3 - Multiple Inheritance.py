class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Preditor(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

class Fish(Prey,Preditor):
    pass

rabbit = Rabbit("Bugs Bunny")
#hawk = Hawk()
#fish = Fish()

rabbit.flee()
rabbit.sleep()