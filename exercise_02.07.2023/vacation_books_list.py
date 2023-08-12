pages_count = int(input())
readed_pages_per_hour = int(input())
days_to_read = int(input())

total_read_time = pages_count // readed_pages_per_hour
needed_time_dayli = total_read_time // days_to_read

print(needed_time_dayli)
