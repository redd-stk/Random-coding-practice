import time

# #if else loop
# temp = int(input("What is the temperature outside?: "))
# if temp >= 0 and temp < 30:
#     print("The Temperature is good today")
#     print("You can go outside!")
# elif temp < 0 or temp > 50:
#     print("The temperature is not good")
#     print("Do not go outside")
# else:
#     print("No temperature given")


#for loop
for i in range(10, 0-1, -1):
    print(i)
    time.sleep(1)
print("Congratulations!! You made a countdown to zero")


#while loop
while i < 5:
    print("I'm learning python")
    time.sleep(1)


# #nested loop
# rows = int(input("How many rows? "))
# columns = int(input("How many columns? "))
# symbol = input("What symbol should we use? ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()



# continue keyword
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


