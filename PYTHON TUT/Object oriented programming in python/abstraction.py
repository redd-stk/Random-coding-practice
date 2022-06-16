# abstract class -class with one or more abstract methods == prevent a user from creating an object of that class
# abstract method - method with a declaration but does not have an implementation


from abc import ABC, abstractmethod


class Vehicle(ABC):   #ADD ABC to the class to be abstracted

    @abstractmethod  #add this to every method in the class
    def go(self):
        pass

#for the children classes below to run they need to override the abstract method in the parent class

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()