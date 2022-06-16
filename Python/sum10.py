sum = 0
myArray = []
for i in range(1, 11):
    myArray.append(i)
    while i < 11:
        myArray.append('+')
    sum = sum + i
    print('Running sum : ', end = '')
    print(*myArray, sep = '+', end = '')
    print(' = ', sum)
    