from math import ceil

name_of_series = input()
series_lenght_in_mins = int(input())
lunch_break_in_mins = int(input())

lunch_time = lunch_break_in_mins / 8
break_time = lunch_break_in_mins / 4

time_left = lunch_break_in_mins - lunch_time - break_time

if time_left >= series_lenght_in_mins:
    time_left = time_left - series_lenght_in_mins
    print(f"You have enough time to watch {name_of_series} and left with {ceil(time_left)} minutes free time.")
else:
    time_left = series_lenght_in_mins -time_left
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(time_left)} more minutes.")
