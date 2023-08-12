budget = int(input())
season = input()
count_fishermans = int(input())

seasons_tuple = ("Spring", "Summer", "Autumn", "Winter")

rent_for_boat = 0

discount = 0

diff =0

if season == seasons_tuple[0]:
    rent_for_boat = 3000
elif season == seasons_tuple[1] or season == seasons_tuple[2]:
    rent_for_boat = 4200
elif season == seasons_tuple[3]:
    rent_for_boat = 2600

if count_fishermans <= 6:
    discount = 0.90
    rent_for_boat = rent_for_boat * discount
elif 7 <= count_fishermans <= 11:
    discount = 0.85
    rent_for_boat = rent_for_boat * discount
elif count_fishermans >= 12:
    discount = 0.75
    rent_for_boat = rent_for_boat * discount

if count_fishermans % 2 == 0 and season != seasons_tuple[2]:
    discount = 0.95
    rent_for_boat = rent_for_boat * discount

diff = abs(budget - rent_for_boat)

if budget >= rent_for_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
