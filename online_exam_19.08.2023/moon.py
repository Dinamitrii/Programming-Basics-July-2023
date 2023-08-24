from math import ceil

motion_velocity_middle_speed = float(input())
liters_fuel_per_hundred_km = float(input())

distance_in_km = 384400
time_on_moon_in_hrs = 3


total_travel_distance = distance_in_km * 2
total_time_travelling = total_travel_distance / motion_velocity_middle_speed
total_time_trip_in_hrs = ceil(total_time_travelling) + time_on_moon_in_hrs

total_fuel_needed = (liters_fuel_per_hundred_km * total_travel_distance)/ 100


print(total_time_trip_in_hrs)
print(int(total_fuel_needed))
