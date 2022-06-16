from car import Car

car_1 = Car("BMW", "M3", "2020", "Black")
car_2 = Car("Ford", "Mustang", "2018", "Red")

print(car_1.make) 
print(car_1.model)
print(car_1.color)

car_1.wheels = 2  #changing the class variable wheels
print(car_1.wheels)
print(car_2.wheels)

car_1.drive()