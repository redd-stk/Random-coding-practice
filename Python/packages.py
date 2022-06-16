#taking the input of number of packages delivered and current pay from the user 
# and converting their input into integers for arithmetic operations to be possible
noOfPackages = int(input("Please enter the number of packages delivered: "))
currentPay = int(input("Please enter your current pay amount: $"))

#initialization of new pay variable
newPay = 0

#if loop containing the rates of pay raise
if noOfPackages == 0:
    newPay = currentPay + 0/100 * currentPay
    
elif noOfPackages <= 50:
    newPay = currentPay + 1/100 * currentPay
    
elif noOfPackages <= 100:
    newPay = currentPay + 2/100 * currentPay
    
elif noOfPackages <= 200:
    newPay = currentPay + 3/100 * currentPay
    
elif noOfPackages <= 300:
    newPay = currentPay + 4/100 * currentPay
    
elif noOfPackages >300:
    newpay = currentPay + 5/100 * currentPay
    
print("Your new pay is: $", newPay)

