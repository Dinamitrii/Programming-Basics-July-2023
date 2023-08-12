deposit = float(input())
months = int(input())
yearly_interest = float(input())

accumulated_interest = deposit * (yearly_interest / 100)
interest_per_month = accumulated_interest / 12
result = deposit + (months * interest_per_month)

print(result)
