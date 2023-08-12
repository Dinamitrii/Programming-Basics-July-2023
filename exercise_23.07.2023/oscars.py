actor_name = input()
starting_points = float(input())
jury_count = int(input())

result = starting_points

for _ in range(0, jury_count):
    name_of_jury_member = input()
    points_from_jury_member = float(input())
    result +=  (len(name_of_jury_member) * (points_from_jury_member) / 2)
    if result > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {result:.1f}!")
        break

if  not result > 1250.5:
    result = 1250.5 - result
    print(f"Sorry, {actor_name} you need {result:.1f} more!")
