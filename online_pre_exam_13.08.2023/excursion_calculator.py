people_count = int(input())
season = input()

price = 0

if season == "spring":
    if people_count <= 5:
        price = 50 * people_count
    else:
        price = 48 * people_count
elif season == "summer":
    if people_count <= 5:
        price = 48.50 * 0.85 * people_count
    else:
        price = 45  * 0.85 * people_count
elif season == "autumn":
    if people_count <= 5:
        price = 60 * people_count
    else:
        price = 49.50 * people_count
elif season == "winter":
    if people_count <= 5:
        price = 86 * 1.08 * people_count
    else:
        price = 85 * 1.08 * people_count


print(f"{price:.2f} leva.")
