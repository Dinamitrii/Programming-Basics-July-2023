n = int(input())

for row in range(1, n ):
    print((n - row) * " *",end= " ")
    print("*")
    print((row - 1) * " *")