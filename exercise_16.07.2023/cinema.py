projection_type = input()
rows = int(input())
columns = int(input())

income = 0

# tickets prices
premiere_tickets = 12.00
regular_tickets = 7.50
discount_tickets = 5.00

capacity = rows * columns

if projection_type == "Premiere":
    income = capacity * premiere_tickets
elif projection_type == "Normal":
    income = capacity * regular_tickets
elif projection_type == "Discount":
    income = capacity * discount_tickets

print(f'{income:.2f} leva')
