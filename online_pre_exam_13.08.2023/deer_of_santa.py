from math import ceil,floor

days_gone = int(input())
food_lefted_kg = int(input())
first_deer_food_per_day_kg = float(input())
second_deer_food_per_day_kg = float(input())
third_deer_food_per_day_kg = float(input())

needed_food_total_first_deer = days_gone * first_deer_food_per_day_kg
needed_food_total_second_deer = days_gone * second_deer_food_per_day_kg
needed_food_total_third_deer = days_gone * third_deer_food_per_day_kg

needed_food_total_all_deers = needed_food_total_first_deer + needed_food_total_second_deer + needed_food_total_third_deer

difference = abs(food_lefted_kg - needed_food_total_all_deers)

if food_lefted_kg >= needed_food_total_all_deers:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
