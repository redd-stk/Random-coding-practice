
from typing import ContextManager


text = "this is my new python created file"

#opening a new file from python
# "w" - write mode, overwrites file contents
# "a" - append mode, you can add new text to existing file text
# "r" - read mode
with open("myfile.txt", "w") as file: 
    file.write(text)


#--------------------------------------------------------------------
#copying files in python
# copyfile() - copies file Content
# copy() - copyfile() + permission +permission directory
# copy2() - copy() copies metadata
import shutil

shutil.copy("myfile.txt", "copiedfile.txt")


#---------------------------------------------------------------------
#moving files using python
import os
source = "myfile.txt"
destination = "C:\\Users\\REDD\\Documents\\text2.txt"

try: #handling the exception incase the file is not found
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+ " was moved")
except FileNotFoundError: 
    print(source+ " was not found")


#---------------------------------------------------------------------
#deleting files using python
try:
    os.remove("nameoffile") #deletes a file
    #os.rmdir("path") - only deletes an empty folder on specified path
    #shutil.rmtree("path") - deletes a folder that is not empty. should import shutil to use
except FileNotFoundError:
    print("The file was not found")
else:
    print("The file was deleted")




