from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_in_seconds = float(input())

slowing_in_seconds = floor(distance_in_meters / 50) * 30

time_to_climb = distance_in_meters * time_per_meter_in_seconds

total_time = time_to_climb + slowing_in_seconds

difference = abs(record_in_seconds - total_time)

if total_time < record_in_seconds:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
