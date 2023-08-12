nylon_in_square_meters = int(input())
paint_in_litres = int(input())
coreselin_in_liters = int(input())
finishing_time_in_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
coreselin_price = 5.00
nylon_extra_in_square_meters = 2
paint_extra_in_percent = (10 / 100)
bags_price = 0.40
price_per_labor_in_percent = (30 / 100)

per_nylon_total = (nylon_in_square_meters + nylon_extra_in_square_meters) * nylon_price
per_paint = (paint_in_litres + (paint_in_litres * paint_extra_in_percent)) * paint_price
per_coreselin = coreselin_in_liters * coreselin_price

materials_price = per_nylon_total + per_paint + per_coreselin + bags_price

sub_total = (materials_price  * price_per_labor_in_percent) * finishing_time_in_hours

total = sub_total + materials_price

print(total)
