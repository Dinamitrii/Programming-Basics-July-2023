shirt = float(input())
goal = float(input())

shorts_price = shirt * 0.75
socks_price = shorts_price *0.20
shoes_price = (shirt + shorts_price) * 2


total_price = shirt + shorts_price + socks_price + shoes_price

discount = total_price * 15 / 100

total_price = total_price - discount

difference = abs(total_price - goal)

if total_price >= goal:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
