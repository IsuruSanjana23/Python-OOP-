class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Preditor:
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

class Fish(Prey,Preditor):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()