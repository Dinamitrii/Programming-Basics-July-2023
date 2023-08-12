number = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for x in range(0, number):
    current_number = int(input())

    if current_number < 200:
        group_1 += 1
    elif current_number <= 399:
        group_2 += 1
    elif current_number <= 599:
        group_3 += 1
    elif current_number <= 799:
        group_4 += 1
    else:
        group_5 += 1

group_1_in_percent = group_1 / number * 100
print(f"{group_1_in_percent:.2f}%")
group_2_in_percent = group_2 / number * 100
print(f"{group_2_in_percent:.2f}%")
group_3_in_percent = group_3 / number * 100
print(f"{group_3_in_percent:.2f}%")
group_4_in_percent = group_4 / number * 100
print(f"{group_4_in_percent:.2f}%")
group_5_in_percent = group_5 / number * 100
print(f"{group_5_in_percent:.2f}%")
