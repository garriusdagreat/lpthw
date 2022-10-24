# variables and names
# variables are 'containers' which contain a value
# they can be given any name and value
cars = 100
space_in_car = 4
drivers = 30
passengers = 90
# variables can also contain operations (+ - / *)
# variable names can also be used in operations
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# print statement and values from each variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined

# The error above occured in line 8
# because the variable named 'car_pool_capacity' does not exist
