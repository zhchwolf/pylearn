# -*- coding: utf-8 -*-
# the count of car.
cars = 100
# the space in the car.
space_in_a_car = 4
# the number of all drivers.
drivers = 30
# all passengers number
passengers = 90
# cars without drivers
cars_not_driven = cars -drivers
# cars with drivers
cars_driven = drivers
# all cars capacity.
carpool_capacity = cars_driven * space_in_a_car
# average passengers in per car.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each cat."
