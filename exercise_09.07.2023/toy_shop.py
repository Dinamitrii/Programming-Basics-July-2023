price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

subtotal_sum = puzzle_count * puzzle_price + dolls_count * dolls_price + bears_count * bears_price + minions_count * minions_price + trucks_count * trucks_price

toys_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count

if toys_count >= 50:
    subtotal_sum = subtotal_sum * 0.75
else:
    subtotal_sum = subtotal_sum

rent = subtotal_sum * 0.10

total_profit = subtotal_sum - rent

result = total_profit - price

if result >= 0:
    print(f"Yes! {result:.2f} lv left.")
else:
    print(f"Not enough money! {abs(result):.2f} lv needed.")
