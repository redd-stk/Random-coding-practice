import re

def validate():
    while True:
        #an array containing different messages to display depending on the condition
        message = ["Make sure your password has at least 6 values and a maximum of 14 values", "Your password is weak, use a mix of numbers letters and other characters", "Your password is strong"]
        password = input("Enter a password: ")
        password_length = len(password) #saves the length of the password input by the user
        password.islower()
        
        #Checks is the password has a minimum of 6 and maximum of 14 characters
        if password_length < 6 or password_length >14: 
            print(message[0])
        #checks if the password has only numbers or letters
        elif re.search('[0-9]',password) is None:
            print(message[1])
        elif re.search('[a-z]',password) is None:
            print(message[1])
        else:
            print(message[2])
            break
        
# calling the validate function to test if it's working        
validate()