##LIST COMPREHENSION
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# -------------------------------
#list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)

print("---------------------------------------") 
students = [100, 90, 80, 70, 60, 50, 40, 20, 10]
passed_students = list(filter(lambda x: x > 60, students))
print(passed_students)

passed_students2 = [i for i in students if i > 60 ]
print(passed_students2)



#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#DICTIONARY COMPREHENSION
cities_infar = {'Kisumu': 32, "Nairobi": 30, "Mombasa": 39, "Naakuru": 29}
cities_incel = {key: round((value - 32) * (5/9)) for (key, value) in cities_infar.items()}
print(cities_incel)

weather = {"Kisumu": "Sunny", "Nairobi": "Cloudy", "Mombasa": "Sunny", "Nakuru": "Snowing", "Eldoret": "Sunny"}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'Sunny'}

descr_cities = {key: ("Warm" if value > 32 else "Cold") for (key, value) in cities_infar.items()}
print(descr_cities)


def checkTemp(value):
    if value >= 35:
        return "HOT"
    elif value >= 31:
        return"WARM"
    else:
        return "COLD"
descr_cities2 = {key: checkTemp(value) for (key, value) in cities_infar.items()}
print(descr_cities2)


