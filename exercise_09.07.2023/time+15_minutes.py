hours = int(input())
minutes = int(input())

after_time = 15

total_minutes = minutes + after_time

if total_minutes > 59:
    total_minutes = total_minutes - 60
    hours += 1
if hours > 23:
    hours = 0

print(f'{hours}:{total_minutes:02}')
