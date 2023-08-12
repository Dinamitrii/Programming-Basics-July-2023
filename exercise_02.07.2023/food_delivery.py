chicken_menu_count = int(input())
fish_menu_count = int(input())
vegi_menu_count = int(input())

chicken_menu_price = chicken_menu_count * 10.35
fish_menu_price = fish_menu_count * 12.40
vegi_menu_price = vegi_menu_count * 8.15

all_menu_sum = chicken_menu_price + fish_menu_price + vegi_menu_price
dessert_price = all_menu_sum * 0.20

total_sum = all_menu_sum + dessert_price + 2.50

print(total_sum)
