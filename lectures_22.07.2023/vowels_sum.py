word = input()

vowels_points = {
    "a":1,
    "e":2,
    "i":3,
    "o":4,
    "u":5
}

points = 0

for char in word:
    if char in vowels_points.keys():
        points += vowels_points.get(char)

print(points)
