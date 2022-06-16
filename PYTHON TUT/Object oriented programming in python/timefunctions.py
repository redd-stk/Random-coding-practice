import time

print(time.ctime(0))    #converts time expressed in seconds into a readable string

print(time.time())  #returns how many seconds has passed since the computers epoch #epoch - computer's reference point

print("-----------------------------------------------------------")

print(time.ctime(time.time()))  #returns current date and time

#using time objects
local_time = time.strftime("%B %d %Y %H : %M : %S")
print(local_time)

print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")

# import threading
# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for ", count, " seconds")


# x = threading.Thread(target=timer, daemon=True)
# x.start()

# answer = input("Do you wish to exit? ")