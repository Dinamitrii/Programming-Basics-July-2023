dancers_count = int(input())
points = float(input())
season = input()
country = input()

charity = 0
money = 0


if season == "summer":
    if country == "Bulgaria":
        money  = dancers_count * points
        money = money * 0.95
    elif country == "Abroad":
        money = (dancers_count * points) * 1.50
        money = money * 0.90
elif season == "winter":
    if country == "Bulgaria":
        money = dancers_count * points
        money = money * 0.92
    elif country == "Abroad":
        money = (dancers_count * points) * 1.50
        money = money * 0.85

charity = money * 75 / 100

money = money -charity

money_per_dancer = money / dancers_count


print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
