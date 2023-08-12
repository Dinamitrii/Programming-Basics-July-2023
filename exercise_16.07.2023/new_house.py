type_flowers = input()
count_flowers = int(input())
budget = int(input())

sum = 0
diff = 0
price = 0

if type_flowers == "Roses":
    price = 5
    sum = price * count_flowers
    if count_flowers > 80:
        sum = sum * 0.90
elif type_flowers == "Dahlias":
    price = 3.80
    sum = price * count_flowers
    if count_flowers > 90:
        sum = sum * 0.85
elif type_flowers == "Tulips":
    price = 2.80
    sum = price * count_flowers
    if count_flowers > 80:
        sum = sum * 0.85
elif type_flowers == "Narcissus":
    price = 3
    sum = price * count_flowers
    if count_flowers < 120:
        sum = sum * 1.15
elif type_flowers == "Gladiolus":
    price = 2.50
    sum = price * count_flowers
    if count_flowers < 80:
        sum = sum * 1.20

diff = abs(budget - sum)
if sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
