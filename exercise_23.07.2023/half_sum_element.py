from sys import maxsize

numbers = int(input())

max_number = - maxsize
sum_of_numbers = 0

for x in range(0, numbers):
    current_number = int(input())
    sum_of_numbers += current_number
    if current_number > max_number:
        max_number = current_number

sum_of_numbers = sum_of_numbers - max_number

if sum_of_numbers == max_number:
    print("Yes")
    print(f"Sum = {sum_of_numbers}")
else:
    print("No")
    print(f"Diff = {abs(max_number - sum_of_numbers)}")
