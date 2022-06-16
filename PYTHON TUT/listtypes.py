#LISTS

cars = ["sedan", "lorry", "pick-up", "hatchback"]
print(cars)

#printing all items in the above list
for i in cars:
    print(i)

print("------------------------------------------------------------------")
cars.append("trailer") #adding items to the list
cars.remove("sedan") #removing an item from the list
# # cars.pop() #removing the last item from the list
cars.insert(0, "suv")
cars.sort()  #sorts the list in an alphabetical order
# # cars.clear() #removes evrything in the list

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")


#TUPLES - ordered and unchangeable

student = ("Redd", 21, "Male")
print(student.count("Redd"))
print(student.index(21)) 

for x in student:
    print(x)

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")


#--------------------------------------------------------------------------------
#SETS -unordered and unindexed
smartphone_brands = {"Xiaomi", "Apple", "Huawei", "Nokia"}
# print(smartphone_brands)
smartphone_brands.add("Vivo")
# smartphone_brands.remove("Huawei")
# smartphone_brands.clear() #removes everything from the list
small_brands = {"Dodgee", "Samsung", "Tecno", "Infinix", "Apple"}

all_brands = smartphone_brands.union(small_brands)
for x in all_brands:
    print(x)

print(small_brands.difference(smartphone_brands)) #returns items that are in small_brands and not in smartphone_b
print(small_brands.intersection(smartphone_brands))  #returns items that are in both sets

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

#---------------------------------------------------------------------------------
#DICTIONARY -changeable unordered collection of unique key value pairs. fast because they use hashing
capitals = {"Kenya": "Nairobi",
                "Uganda": "Kampala",
                "Russia": "Moscow",
                "China": "Beijing"}
capitals.update({"Germany": "Berlin"})  #adding a new value / can also update existing items 
#capitals.clear() #removes everything in the dictionary
#capitals.pop()  #removes the last item in the dictionary

print(capitals.keys())  #prints only the keys
print(capitals.values()) #prints only the values of the keys
print(capitals.items())  #prints the entire dictionary




