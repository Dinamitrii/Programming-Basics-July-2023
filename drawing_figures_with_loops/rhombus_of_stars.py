number = int(input())

for row in range(1, number):
    print((number - row) * " ")
    print("*")
    print((row - 1) * "*")


# for downside in reversed(range(number)):
#     print((number - downside) * " " + (downside * " " "*"))
