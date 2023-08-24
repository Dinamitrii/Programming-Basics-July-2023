percent_of_fats = int(input())
percent_of_proteins = int(input())
percent_of_vh = int(input())
total_calories = int(input())
percent_of_water = int(input())

fats_calories_per_gram = 9
proteins_calories_per_gram = 4
vh_calories_per_gram = 4



total_grams_fats = (percent_of_fats * total_calories/100) / 9
total_grams_proteins = (percent_of_proteins * total_calories/100) / 4
total_grams_vh = (percent_of_vh * total_calories/100) / 4

total_food = total_grams_fats + total_grams_proteins + total_grams_vh

calories_per_gram_food = total_calories / total_food

in_gram_food = calories_per_gram_food * percent_of_water / 100


print(f"{(calories_per_gram_food - in_gram_food):.4f}")
