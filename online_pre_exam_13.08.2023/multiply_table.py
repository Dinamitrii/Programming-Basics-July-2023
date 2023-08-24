number = input()

for figure_one in range(1,int(number[2]) + 1):
    for figure_two in range(1,int(number[1]) + 1):
        for figure_three in range(1,int(number[0]) + 1):

            result = figure_one * figure_two * figure_three
            print(f"{figure_one} * {figure_two} * {figure_three} = {result};")
