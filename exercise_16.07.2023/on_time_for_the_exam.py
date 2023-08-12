exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_all_in_minutes = (exam_hour * 60) + exam_minutes
arrival_all_in_minutes = (arrival_hour * 60) + arrival_minutes

diff_minutes = abs(arrival_all_in_minutes - exam_all_in_minutes)

if arrival_all_in_minutes > exam_all_in_minutes:
    print("Late")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_minutes} minutes after the start")
elif arrival_all_in_minutes == exam_all_in_minutes or diff_minutes <= 30:
    print("On time")
    if diff_minutes > 0:
        print(f"{diff_minutes} minutes before the start")
else:
    print("Early")
    if diff_minutes >= 60:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_minutes} minutes before the start")
