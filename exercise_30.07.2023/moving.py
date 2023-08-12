width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
boxes_sum = 0
input_line = input()

while input_line != "Done":
    current_boxes = int(input_line)
    boxes_sum += current_boxes

    if boxes_sum >= volume:
        break

    input_line = input()

diff = abs(volume - boxes_sum)

if boxes_sum >= volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
