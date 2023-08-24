input_line  = int(input())

for a in range(1, 10):
      for b in range(9,a + 1,-1):
          for c in range(10):
            for d in range(9, c + 1,- 1):
                result = a * b * c * d
                summarise = a + b + c + d
                if result == summarise and input_line %
                print(f"{a}{b}{c}{d}")
                print(result)