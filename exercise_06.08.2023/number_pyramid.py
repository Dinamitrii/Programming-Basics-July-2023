n = int(input())

current_number = 1
flag = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_number > n:
            flag = True
            break
        print(current_number, end=" ")

        current_number += 1
    print()
    if flag:
        break
