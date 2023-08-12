open_tabs = int(input())
salary = int(input())

fines_for_tabs = {
    "Facebook":150,
    "Instagram":100,
    "Reddit":50
    }

for _ in range(0,open_tabs):
    tab_name = input()
    tab_name = fines_for_tabs.get(tab_name)
    if tab_name:
        salary -= tab_name

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
