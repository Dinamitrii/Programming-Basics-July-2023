packs_pens = int(input())
packs_markers = int(input())
litres_cleaner = int(input())
discount_in_percent = int(input())

price_pens_per_pack = 5.80
price_markers_per_pack = 7.20
price_cleaner_per_liter = 1.20

total_price_pens = packs_pens * price_pens_per_pack
total_price_markers = packs_markers * price_markers_per_pack
total_price_cleaner = litres_cleaner * price_cleaner_per_liter

price_per_all = total_price_pens + total_price_markers + total_price_cleaner

final_price_with_discount = price_per_all - (price_per_all *(discount_in_percent / 100))

print(final_price_with_discount)
