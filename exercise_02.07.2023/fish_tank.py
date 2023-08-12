lenght = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume = lenght * width * height

total_lt = volume / 1000

volume_acc = total_lt * (percent_acc / 100)

result = total_lt- volume_acc

print(result)
