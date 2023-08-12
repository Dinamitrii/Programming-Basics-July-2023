number_of_groups_climbing = int(input())

climbers_musala = 0
climbers_montblanc = 0
climbers_kilimandjaro = 0
climbers_k2 = 0

climbers_everest = 0

total_climbers = 0

for _ in range(0, number_of_groups_climbing):
    number_of_people = int(input())
    total_climbers += number_of_people

    if number_of_people <= 5:
                climbers_musala += number_of_people

    elif number_of_people >= 6 and not number_of_people > 12:
                climbers_montblanc += number_of_people

    elif number_of_people >= 13 and not number_of_people > 25:
        climbers_kilimandjaro += number_of_people

    elif number_of_people >= 26 and not number_of_people > 40:
        climbers_k2 += number_of_people

    else:
                climbers_everest += number_of_people


musala = climbers_musala / total_climbers * 100
montblanc = climbers_montblanc / total_climbers * 100
kilimandjaro = climbers_kilimandjaro / total_climbers * 100
k2 = climbers_k2 / total_climbers * 100
everest = climbers_everest / total_climbers * 100

print(f"{musala:.2f}%\n{montblanc:.2f}%\n{kilimandjaro:.2f}%\n{k2:.2f}%\n{everest:.2f}%")
