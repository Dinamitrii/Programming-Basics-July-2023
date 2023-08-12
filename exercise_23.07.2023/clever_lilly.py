age_of_lilly = int(input())
laundry_machine = float(input())
toy_price = int(input())

money = 0
toy_count = 0
money_taken = 0

for year in range(1, age_of_lilly + 1):
    if year % 2 == 0:
        money += int(year / 2) * 10
        money_taken += 1
    else:
        toy_count += 1

money_from_toys = toy_count * toy_price

total_money = money + money_from_toys - money_taken

difference = abs(total_money - laundry_machine)

if total_money >= laundry_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
