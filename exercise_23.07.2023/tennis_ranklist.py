from math import floor

tournaments_count = int(input())
starting_points = int(input())

result = starting_points
result_average = 0
average_points = 0

possible_result = {
    "W": 2000,
    "F": 1200,
    "SF": 720
}

for _ in range(0, tournaments_count):
    tournaments_result = input()
    result += possible_result.get(tournaments_result)
    if tournaments_result == "W":
        result_average += 1

average_points = ((result - starting_points) / tournaments_count)

print(f"Final points: {result}")
print(f"Average points: {floor(average_points)}")
print(f"{(result_average / tournaments_count) * 100:.2f}%")
