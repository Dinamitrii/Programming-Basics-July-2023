width_craft = float(input())
lenght_craft = float(input())
height_craft = float(input())
average_height_astronauts = float(input())

volume_craft = width_craft * lenght_craft * height_craft
one_room_volume = (average_height_astronauts + 0.40) * 2 * 2

will_be_room_for = volume_craft / one_room_volume

number_of_astronauts = int(will_be_room_for)

if 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {number_of_astronauts} astronauts.")
elif number_of_astronauts < 3:
    print("The spacecraft is too small.")
elif number_of_astronauts > 10:
    print("The spacecraft is too big.")
