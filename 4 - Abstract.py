from abc import ABC , abstractmethod

class Vehical(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def go(self):
        print("You Drive the Car")

    def stop(self):
        print("You Stop the Car")

class Motorcycle(Vehical):
    def go(self):
        print("You Drive the Motorcycle")

    def stop(self):
        print("You Stop the Motorcycle")

car = Car()
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()