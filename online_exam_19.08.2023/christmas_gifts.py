total_kids = 0
total_adults = 0
total_toys_cost = 0
total_sweaters_cost = 0

while True:
    command = input()
    if command == "Christmas":
        break

    age = int(command)

    if age <= 16:
        total_kids += 1
        total_toys_cost += 5
    else:
        total_adults += 1
        total_sweaters_cost += 15

print(f"Number of adults: {total_adults}")
print(f"Number of kids: {total_kids}")
print(f"Money for toys: {total_toys_cost}")
print(f"Money for sweaters: {total_sweaters_cost}")
