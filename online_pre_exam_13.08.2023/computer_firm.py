n = int(input())
total_sales = 0
total_rating = 0

for _ in range(n):
    computer_data = int(input())
    rating = computer_data % 10
    sales = (computer_data // 10) % 100
    total_rating += rating

    if rating == 2:
        sales_percentage = 0
    elif rating == 3:
        sales_percentage = 0.5
    elif rating == 4:
        sales_percentage = 0.7
    elif rating == 5:
        sales_percentage = 0.85
    else:
        sales_percentage = 1

    total_sales += sales * sales_percentage

average_rating = total_rating / n
print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
