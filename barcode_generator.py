first_number = input()
second_number = input()

for figure_one in range(int(first_number[0]), int(second_number[0]) + 1):
    for figure_two in range(int(first_number[1]), int(second_number[1]) + 1):
        for figure_three in range(int(first_number[2]), int(second_number[2]) + 1):
            for figure_four in range(int(first_number[3]), int(second_number[3]) + 1):
                if figure_one % 2 != 0 and figure_two % 2 != 0 and figure_three % 2 != 0 and figure_four % 2 != 0:
                    print(f"{figure_one}{figure_two}{figure_three}{figure_four}",end= " ")




