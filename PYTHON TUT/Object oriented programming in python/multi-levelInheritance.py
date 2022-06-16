#derived class inherits from another child derived class

class Organisms:
    alive = True

class Animal(Organisms):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive)
dog.bark()
dog.eat()