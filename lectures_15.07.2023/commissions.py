city = input()
sales_volume = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = (sales_volume * 5) / 100
    elif 501 <= sales_volume <= 1000:
        commission = (sales_volume * 7) / 100
    elif 1001 <= sales_volume <= 10000:
        commission = (sales_volume * 8) / 100
    elif sales_volume > 10000:
        commission = (sales_volume * 12) / 100

elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = (sales_volume * 4.5) / 100
    elif 501 <= sales_volume <= 1000:
        commission = (sales_volume * 7.5) / 100
    elif 1001 <= sales_volume <= 10000:
        commission = (sales_volume * 10) / 100
    elif sales_volume > 10000:
        commission = (sales_volume * 13) / 100

elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = (sales_volume * 5.5) / 100
    elif 501 <= sales_volume <= 1000:
        commission = (sales_volume * 8) / 100
    elif 1001 <= sales_volume <= 10000:
        commission = (sales_volume * 12) / 100
    elif sales_volume > 10000:
        commission = (sales_volume * 14.5) / 100


if commission == 0:
    print("error")
else:
    print(f"{commission:.2f}")
