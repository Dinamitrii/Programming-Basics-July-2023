number_of_cats = int(input())

price_of_food_per_kg = 12.45

group_one_small_cats = 0
group_two_big_cats = 0
group_three_huge_cats = 0

grams_food_all_cats_per_day = 0

for cats in range(1, number_of_cats + 1):
    grams_food_per_cat = float(input())

    if 100 <= grams_food_per_cat < 200:
        group_one_small_cats += 1
        grams_food_all_cats_per_day += grams_food_per_cat
    elif 200 <= grams_food_per_cat < 300:
        group_two_big_cats += 1
        grams_food_all_cats_per_day += grams_food_per_cat
    elif 300 <= grams_food_per_cat < 400:
        group_three_huge_cats += 1
        grams_food_all_cats_per_day += grams_food_per_cat


    if grams_food_all_cats_per_day >= 1000:
       food_per_all_cats_in_kg = grams_food_all_cats_per_day / 1000
       total_price_per_day = price_of_food_per_kg * food_per_all_cats_in_kg
    else:
        grams_food_all_cats_per_day =grams_food_all_cats_per_day
        total_price_per_day = (price_of_food_per_kg * grams_food_all_cats_per_day) / 1000


print(f"Group 1: {group_one_small_cats} cats.")
print(f"Group 2: {group_two_big_cats} cats.")
print(f"Group 3: {group_three_huge_cats} cats.")
print(f"Price for food per day: {total_price_per_day:.2f} lv.")
