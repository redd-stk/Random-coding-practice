from audioop import reverse

#using the sort() method - only works for lists

studentss = ["Redd", "Patrick", "Spongebob", "Crabs", "Squidward"]
studentss.sort()
#students.sort(reverse = True)  #sorts the list in reverse alphabetical order
for i in studentss:
    print(i)

print("----------------------------------------------------------------------")

#using the sorted() function

students = ("Redd", "Patrick", "Spongebob", "Crabs", "Squidward")
#sorted_list = sorted(students)
sorted_list = sorted(students, reverse = True)  #sorts the list in reverse alphabetical order

for i in sorted_list:
    print(i)

print("----------------------------------------------------------------------")

#sorting using the key argument in sort method in a list of tuples
studentsh = [
            ("Redd", "A", 21), 
            ("Patrick", "F", 23), 
            ("Spongebob", "B", 20), 
            ("Krabs", "E", 40), 
            ("Squidward", "C", 35)
            ]
grade = lambda grades: grades[1]
studentsh.sort(key=grade)#sorting using the second column
#studentsh.sort(key=grade, reverse=True)#sorting using the second column in reverse order

#age = lambda age: age[2]#sorting using the third column
#studentsh.sort(key =age)
#  
for i in studentsh:
    print(i)

print("-----------------------------------------------------------------------")
#using sorted function in a tuple of tuples
studentsh = (("Redd", "A", 21), 
            ("Patrick", "F", 23), 
            ("Spongebob", "B", 20), 
            ("Krabs", "E", 40), 
            ("Squidward", "C", 35))
            
grade = lambda grades: grades[1]
studentsh_sorted = sorted(studentsh, key=grade)
print(studentsh_sorted)
