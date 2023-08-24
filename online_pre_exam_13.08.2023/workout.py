days_count = int(input())
runned_kilometers_first_day = float(input())

percents = 0
summarise = 0

for day in range(days_count):
    percent_up = int(input())
    percents = runned_kilometers_first_day + (runned_kilometers_first_day * percent_up/100)






print(percents)