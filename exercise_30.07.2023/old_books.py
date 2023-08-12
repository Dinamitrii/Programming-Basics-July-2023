possible_books_list =["Bourne","True Story","Forever","More Space","The Girl","Spaceship",
                      "Strongest","Profit","Tripple","Stella","The Matrix","Troy","Stronger",
                      "Life Style","Hunger Games","Harry Potter","Torronto","Spotify"]

book_searched_for = input()

current_book_counter = 0
book_found = False

current_book = input()

while  current_book != "No More Books":
    if  current_book == book_searched_for and current_book in possible_books_list:
        book_found = True
        break
    current_book = input()
    current_book_counter += 1


if book_found:
       print(f"You checked {current_book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {current_book_counter} books.")



