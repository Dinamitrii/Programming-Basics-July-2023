from math import ceil

flag = False

wall_height = int(input())
wall_width = int(input())
area_percent_without_painting = int(input())

square_m_wall = wall_width * wall_height * 4
square_m_wall_net = int(square_m_wall - (square_m_wall * area_percent_without_painting / 100))
max_number = square_m_wall
paint_lt = 0

for i in range(max_number):
    paint_lt_current = input()

    if paint_lt_current == 'Tired!':
        print(f"{ceil(square_m_wall_net)} quadratic m left.")
        flag = True
        break

    paint_lt_current = int(paint_lt_current)
    paint_lt += paint_lt_current
    square_m_wall_net -= paint_lt_current

    if square_m_wall_net == 0:
        print(f"All walls are painted! Great job, Pesho!")
    elif square_m_wall_net < 0:
        print(f"All walls are painted and you have {abs(ceil(square_m_wall_net))} l paint left!")
    if flag:
        break