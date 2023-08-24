# user input for iterations
iterations_count = int(input())
# pyrva suma
prime_sum = int(input()) + int(input())
# definirane na promenlivata za maksimalna razlika
max_diff = 0
# for cikyl
for i in range(iterations_count - 1):
    current_sum = int(input()) + int(input())

    current_diff = abs(prime_sum - current_sum)

    if max_diff < current_diff:
        max_diff = current_diff

    prime_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={prime_sum}')
else:
    print(f'No, maxdiff={max_diff}')
