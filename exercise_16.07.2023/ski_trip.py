days_vacantion = int(input())
type_of_room = input()
evaluation = input()

bill = 0
overnights = days_vacantion - 1
discount = 0

type_of_room_dict = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}

discount_apartment = [0.70, 0.65, 0.50]
discount_presidential_apartment = [0.90, 0.85, 0.80]

# evaluation_tuple = ("positive", "negative")

# if overnights < 10:
#     if type_of_room in type_of_room_dict.keys():
#         bill = overnights * type_of_room_dict.get(type_of_room)
#
# elif 10 <= overnights <= 15:
#     if type_of_room in type_of_room_dict.keys():
#         bill = overnights * type_of_room_dict.get(type_of_room)
#
# elif overnights > 15:
#     if type_of_room in type_of_room_dict.keys():
#         bill = overnights * type_of_room_dict.get(type_of_room)
#
# if evaluation in evaluation_tuple:
#     if evaluation == evaluation_tuple[0]:
#         bill = bill * 1.25
#     elif evaluation == evaluation_tuple[1]:
#         bill = bill * 0.90
#
# print(bill)

evaluation_values = {"positive": 1.25, "negative": 0.90}

if type_of_room in type_of_room_dict:
    bill = overnights * type_of_room_dict.get(type_of_room)
    try:
        bill *= evaluation_values[evaluation]
    except:
        pass

print(bill)
