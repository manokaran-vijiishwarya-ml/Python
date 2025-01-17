cars=["swift","toyato","wagonr","BMW"]
for x in cars:
    print(x)
print(len(cars))
print(cars[2])
cars.append("Hondacity")
print(cars)
cars.remove("wagonr")
print(cars)
cars.pop(0)
print(cars)
# car=cars.copy
# print(car)
x=cars.count("BMW")
print(x)
cars.append('BMW')
print(cars.count('BMW'))
print(cars)
car=["vista","lamboghini"]
b=cars.extend(car)
print(b)