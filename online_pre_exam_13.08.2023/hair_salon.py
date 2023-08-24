goal_for_day = int(input())

price = 0
profit = 0

while True:
    input_line = input()


    if input_line == "haircut":
        input_line = input()
        if input_line == "mens":
            price = 15
        elif input_line == "ladies":
            price = 20
        elif input_line == "kids":
            price = 10
    elif input_line == "color":

        if input_line == "touch up":
            price = 20
        elif input_line == "full color":
            price = 30



    if input_line == "closed":
        break
profit += price

if profit >= goal_for_day:
        print(profit)
elif profit < goal_for_day:
    print("SHIT")




