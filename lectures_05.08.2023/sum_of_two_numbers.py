
start_of_interval=int(input())
end_of_interval=int(input())
magic_number=int(input())

combination_counter = 0

end_condition = False

for x in range(start_of_interval,end_of_interval+1):
    for y in range(start_of_interval,end_of_interval+1):
        combination_counter+=1
 
        if x + y == magic_number:
            
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
           
            end_condition=True
            break
    if end_condition:
        break 
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
