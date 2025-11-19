# class Car:
#     pass

my_car = Car()

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

my_car = Car("Toyota", "Red", 2023)
my_car1 = Car("Lexus", "black", 2024)

print(my_car.brand)
print(my_car.color)
print(my_car.year)
