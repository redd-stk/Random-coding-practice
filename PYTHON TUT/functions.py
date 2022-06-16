# def multiply(number1, number2):
#     result = number1 * number2
#     return result
# x = multiply(6, 8)
# print(x)


#---------------------------------------------------------------------------
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(2,3,4,5,6,7))

# def hello(**kwargs):
#     print("Hello ", end="")
#     for key, value in kwargs.items():
#         print(value, end="")
#     #print("Hello " + kwargs["first"] + " " + kwargs["last"])
# hello(title="Mr.", first="Eddie ", middle="Ochieng ", last="Odhiambo")

#-----------------------------------------------------------------------------
#generating a random numer
import random
x = random,random.randint(1,100) #generates a random interger
y = random.random()  #generates a random floating number 
myList = ["porsche", "mustang", "charger", "gtr"]
z = random.choice(myList)
print(x)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"k","j","A"]
random.shuffle(cards)  #shuffles a list
print(cards)




