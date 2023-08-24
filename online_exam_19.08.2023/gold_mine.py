locations = int(input())

for _ in range(locations):
    expected_average_gold = float(input())
    days = int(input())

    total_gold = 0
    for _ in range(days):
        gold_per_day = float(input())
        total_gold += gold_per_day

    average_gold_per_day = total_gold / days

    if average_gold_per_day >= expected_average_gold:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        needed_gold = expected_average_gold - average_gold_per_day
        print(f"You need {needed_gold:.2f} gold.")
