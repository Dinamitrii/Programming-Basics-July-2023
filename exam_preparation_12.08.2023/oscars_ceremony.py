hall_rent = int(input())
oscars_price = hall_rent * 0.70
catering_price = oscars_price * 0.85
price_for_sound = catering_price / 2


total_cost = hall_rent + oscars_price + catering_price + price_for_sound


print(f"{total_cost:.2f}")
