class Animal:
    alive = True

    def eat(self):
        print("Tis animal is eating")
    def sleep(self):
        print("This animal is sleepng")

class Rabbit(Animal):
    def run(self):
        print("This animal is running")

class Fish(Animal):
    def swim(self):
        print("This animal is swimming")

class Hawk(Animal):
    def fly(self):
        print("This animal is flying")



rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()