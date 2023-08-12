budget = float(input())
statists = int(input())
costume_price_per_one = float(input())

decores = budget * 0.10
costume_price_per_all = statists * costume_price_per_one

if statists >= 150:
    discount_only_costumes = costume_price_per_all * 0.90
    budget = budget - decores - discount_only_costumes
else:
    budget = budget - decores - costume_price_per_all
if budget < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget:.2f} leva left.")
    