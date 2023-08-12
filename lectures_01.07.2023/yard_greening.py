square_meters = float(input())

price_per_sq_meter = 7.61
discount_in_percent = (18 / 100)

sub_total = square_meters * price_per_sq_meter
discount_is = sub_total * discount_in_percent

total = sub_total - discount_is

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount_is} lv.")
