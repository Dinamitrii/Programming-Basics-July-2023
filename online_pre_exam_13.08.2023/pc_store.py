price_cpu_usd = float(input())
price_gpu_usd = float(input())
price_ram_usd = float(input())
number_of_rams = int(input())

discount = float(input())

usd_to_bgn = 1.57

price_cpu_in_bgn = price_cpu_usd * usd_to_bgn
price_gpu_in_bgn = price_gpu_usd * usd_to_bgn
price_ram_in_bgn = price_ram_usd * usd_to_bgn

price_ram_total_in_bgn = price_ram_in_bgn * number_of_rams

price_cpu_in_bgn_discounted = price_cpu_in_bgn * (1 - discount)

price_gpu_in_bgn_discounted = price_gpu_in_bgn * (1 - discount)

total_price = price_cpu_in_bgn_discounted + price_gpu_in_bgn_discounted + price_ram_total_in_bgn

print(f"Money needed - {total_price:.2f} leva.")
