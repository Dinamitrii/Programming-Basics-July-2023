from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_a_meter = float(input())

# has a delay every 15 meters 12.5 seconds
whole_distance_time = distance_in_meters * time_for_a_meter
delay_time = floor(distance_in_meters / 15) * 12.5

whole_distance_time = whole_distance_time + delay_time

new_time = record_in_seconds - whole_distance_time

if record_in_seconds <= whole_distance_time:
    print(f"No, he failed! He was {abs(new_time):.2f} seconds slower.")
else:
    new_time = whole_distance_time
    print(f" Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
