sales_report = [
{"product": "Hammer", "price": 10.99, "quantity": 47},

{"product": "Saw", "price": 5.49, "quantity": 112},

{"product": "Nails 100x", "price": 6.15, "quantity": 232},

{"product": "Soft Drinks", "price": 1.15, "quantity": 120},

{"product": "Mars-Bar", "price": 0.75, "quantity": 150},

           ]

total_revenue = 0

for r in range(len(sales_report)):

    revenue = sales_report[r].get("price") * sales_report[r].get("quantity")
    total_revenue += revenue

print(f"{total_revenue:.2f}")
