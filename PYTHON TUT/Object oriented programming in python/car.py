class Car:
    wheels = 4  #class variable - declared inside a class but outside the constructor

    def __init__(self, make, model, year, color):  #constructor
        self.make = make    #instance variable - declared inside the constructor
        self.model = model   #instance variable
        self.year = year     #instance variable
        self.color = color   #instance variable
    
    def drive(self):
        print("This "+self.make +" " + self.model +" is in motion")


#Method chaining - using several methods of the same class sequentially
class Vehicle():
    def turn_on(self):
        print("You turn on the car")
        return self  #should be included to every method to enable method chaining
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You hit the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the car")
        return self

car = Vehicle()

car.turn_on().drive()
car.brake().turn_off()
car.brake().turn_off().turn_on()

#for long method chainings use backslash for line continuation and move to next line  - easy readability
car.brake()\
    .turn_off()\
    .turn_on()\
    .drive()\
    .brake()\
    .turn_off()