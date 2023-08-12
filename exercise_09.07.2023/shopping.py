budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250
gpu_total_cost = gpu_count * gpu_price

cpu_price = (gpu_total_cost * 35) / 100
ram_price = (gpu_total_cost * 10) / 100

cpu_total_cost = cpu_count * cpu_price
ram_total_cost = ram_count * ram_price

total_cost = gpu_total_cost + cpu_total_cost + ram_total_cost


if gpu_count > cpu_count:
    total_cost = total_cost * 0.85
else:
    total_cost = total_cost

if budget >= total_cost:
    budget = budget - total_cost
    print(f"You have {budget:.2f} leva left!")
else:
    budget = total_cost - budget
    print(f"Not enough money! You need {budget:.2f} leva more!")
