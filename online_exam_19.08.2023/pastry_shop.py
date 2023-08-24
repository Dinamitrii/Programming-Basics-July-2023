type_of_sweets = input()
number_of_sweets = int(input())
day_of_december = int(input())

price = 0
discount_in_percent = 0

if type_of_sweets == "Cake":
    if day_of_december <= 15:
        price = 24
    elif day_of_december > 15:
        price = 28.70
elif type_of_sweets == "Souffle":
    if day_of_december <= 15:
        price = 6.66
    elif day_of_december > 15:
        price = 9.80
elif type_of_sweets == "Baklava":
    if day_of_december <= 15:
        price = 12.60
    elif day_of_december > 15:
        price = 16.98

total_price = price * number_of_sweets

if day_of_december <= 22:
    if 100 <= total_price <= 200:
        discount_in_percent = 15
    elif total_price > 200:
        discount_in_percent = 25

total_price -= total_price * discount_in_percent / 100

if day_of_december <= 15:
    total_price -= total_price * 10 / 100

print(f"{total_price:.2f}")
