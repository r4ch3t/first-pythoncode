# num of cars
cars = 100
# amnt of space in a car
space_in_a_car = 4.0
# how many drivers there are
drivers = 30
# amount of passengers there are
passengers = 90
# equations
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "There will be transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
