# from car import Car


# my_new_car = Car('audi', 'a4', 2019)

# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(24)
# my_new_car.read_odometer()

# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.Car('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster',2019)
print(my_tesla.get_descriptive_name())

from electric_car import ElectricCar as EC
print(f"\n{my_tesla.get_descriptive_name()}")