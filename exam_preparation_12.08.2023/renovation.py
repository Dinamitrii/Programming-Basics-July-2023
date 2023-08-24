from math import ceil

wall_height = int(input())
wall_width = int(input())
not_painted_percent = int(input())
paint_liters = input()

total_wall_area = 4 * wall_height * wall_width
paintable_area = total_wall_area - (total_wall_area * not_painted_percent / 100)

while paint_liters != "Tired!":
    paint_liters = int(paint_liters)
    paintable_area -= paint_liters

    if paintable_area <= 0:
        print("All walls are painted and you have {0} l paint left!".format(abs(paintable_area)))
        break

    paint_liters = input()

if paint_liters == "Tired!" and paintable_area > 0:
    print("{0} quadratic m left.".format(ceil(paintable_area)))
