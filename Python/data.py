from tabulate import tabulate


data = [['Small', 100, 200, 300],
        ['Medium', 200, 400, 600],
        ['Large', 400, 900, 1200]]
print (tabulate(data, headers=["Size", "Windows", "Dusting", "Floors"]))