number = int(input())

for row in range(1, number + 1):
    print((number - row) * " " + (row * " " "*"))
for col in reversed(range(number)):
    print((number - col) * " " + (col * " " "*"))
