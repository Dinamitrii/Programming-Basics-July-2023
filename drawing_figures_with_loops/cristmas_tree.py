number = int(input())

for i in reversed(range(number)):
    print("|" + (number - i) * " " "*")

