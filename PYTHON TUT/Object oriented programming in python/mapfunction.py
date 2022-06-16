#map function - applies a function to every item in an iterable
store = [
    ("Shirt", 25.00),
    ("Trouser", 30.00),
    ("Sneakers", 50.25),
    ("Socks", 10.20)
]

to_euros = lambda item: (item[0], item[1]*0.85)

store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)

print("---------------------------------------")
#filter() function
friends = (
    ("Pamela", 21),
    ("Andy", 17),
    ("Patrick", 16),
    ("Sandy", 22),
    ("Rose", 21),
    ("Laura", 16)
)
age = lambda data: data[1] >= 18
over_age = list(filter(age, friends))

for i in over_age:
    print(i)


print("--------------------------------------")
# reduce() function


