import random

# List containing six elements which will represent the six dice sides
count = [0, 0, 0, 0, 0, 0]

#roll function to generate a random number for the rolling of the dice
def roll():
    randomNumber = random.randint(1,6)
    return randomNumber

#takes input from the user on how many times the dice should be rolled
rolls = int(input("Enter the number of rolls: "))

#loop that adds the element count if a nuumber is rolled
i = 1
while i <= rolls:
    r = roll()
    count[r - 1] = count[r - 1] + 1
    i = i + 1

#for loop that prints the values of the list containing the number of rolls
for x in range(len(count)):
    print('Number of times ', x+1, 'was rolled ', count[x])
    print('Percentage is ', count[x]/rolls) #percentage is calculated as number of rolls of that number over the total rolls