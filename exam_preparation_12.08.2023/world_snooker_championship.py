stage_of_championship = input()
type_of_tickets = input()
count_of_tickets = int(input())
picture_with_trophy = input()

price = 0
picture_price = 40 * count_of_tickets

if stage_of_championship == "Quarter final":
    if type_of_tickets == "Standard":
        price = 55.50
    elif type_of_tickets == "Premium":
        price = 105.20
    elif type_of_tickets == "VIP":
        price = 118.90
elif stage_of_championship == "Semi final":
    if type_of_tickets == "Standard":
        price = 75.88
    elif type_of_tickets == "Premium":
        price = 125.22
    elif type_of_tickets == "VIP":
        price = 300.40
elif stage_of_championship == "Final":
    if type_of_tickets == "Standard":
        price = 110.10
    elif type_of_tickets == "Premium":
        price = 160.66
    elif type_of_tickets == "VIP":
        price = 400

price = price * count_of_tickets

if price > 4000:
        price = price - (price * 25 / 100)
        picture_price = 0
elif price > 2500 and picture_with_trophy == "Y":
        price = (price - (price * 10 / 100)) + picture_price
elif price > 2500 and picture_with_trophy == "N":
        price = (price - (price * 10 / 100))
elif picture_with_trophy == "Y":
        price += picture_price
elif picture_with_trophy == "N":
        price = price


print(f"{price:.2f}")
