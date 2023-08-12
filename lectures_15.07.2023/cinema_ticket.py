weekday = input()

price = 0

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Friday":
    price = 12
elif weekday == "Wednesday" or weekday == "Thursday":
    price = 14
elif weekday == "Saturday" or weekday == "Sunday":
    price = 16

print(price)
