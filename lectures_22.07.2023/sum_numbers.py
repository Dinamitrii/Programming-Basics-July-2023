count_for_nums = int(input())

summarise = 0
current_num = 0

for _ in range(count_for_nums):
    current_num = int(input())
    summarise += current_num

print(summarise)
