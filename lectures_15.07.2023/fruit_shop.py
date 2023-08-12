fruit_type = input()
day_of_week = input()
quantity = float(input())

# list of available fruits(it is changeable)
fruit_list = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

# weekday tuple(tuple because days of week are always the same)
weekday_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# same as above tuple (tuple's are immutable or not to be changeable)
weekend_tuple = ("Saturday", "Sunday")

# weekday prices dictionary(it is changeable,also called collection)
fruit_weekdays_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}
# weekend prices dictionary
fruit_weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

#simple check conditions and printing results formatted
if fruit_type in fruit_list and day_of_week in weekday_tuple:
    print(f'{fruit_weekdays_prices[fruit_type] * quantity:.2f}')
elif fruit_type in fruit_list and day_of_week in weekend_tuple:
    print(f'{fruit_weekend_prices[fruit_type] * quantity:.2f}')
else:
    print("error")
