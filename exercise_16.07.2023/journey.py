budget = float(input())
season = input()

seasons_tuple = ("summer", "winter")
destination_tuple = ("Bulgaria", "Balkans", "Europe")
place_tuple = ("Camp", "Hotel")

location = ""
destination = ""
place = ""

spend = 0

if budget <= 100:
    destination = destination_tuple[0]
    if season == seasons_tuple[0]:
        place = place_tuple[0]
        spend = budget * 0.30
    elif season == seasons_tuple[1]:
        place = place_tuple[1]
        spend = budget * 0.70

elif budget <= 1000:
    destination = destination_tuple[1]
    if season == seasons_tuple[0]:
        place = place_tuple[0]
        spend = budget * 0.40
    elif season == seasons_tuple[1]:
        place = place_tuple[1]
        spend = budget * 0.80

elif budget > 1000:
    destination = destination_tuple[2]
    spend = budget * 0.90
    place = place_tuple[1]

print(f"Somewhere in {destination}")
print(f"{place} - {spend:.2f}")
