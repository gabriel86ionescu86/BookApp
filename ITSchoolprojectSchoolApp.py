# Remember to also delete a certain book

def addBook():
    import csv
    book_name = input('Insert book name -> ')
    with open("booksDB.csv", mode = "r") as file: # we open the csv in read mode and check if the book exists exists
        rows = csv.DictReader(file,fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        for row in rows:
            if row.get("BookName") == book_name: # if the book is found, we ask user to try adding another book
                    try_again = input(f"{book_name} already exists! Try again? (Y/N? ")
                    if  try_again.upper() == "Y":
                        addBook()
                        return
                    else:
                        return

    author_name = input('Insert book author -> ') # if the book is not found, we continue to add it to the list
    with open('booksDB.csv', mode='a', ) as file:  # mode = 'a' appends to the existing list
        writer = csv.DictWriter(file, fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        writer.writerow({'BookName': book_name,
                         'AuthorName': author_name,
                         'SharedWith': "None",
                         'IsRead': False})
    print('Book was successfully added!')

    other_book = input('Add another book? (Y/N)? ') # we ask the user if he wants to add another book
    if other_book.upper() == "Y":
        addBook()
    elif other_book.upper() == "N":
        return


def listBooks():
    import csv
    with open("booksDB.csv", mode = "r") as file:
        rows = csv.DictReader(file,fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        for row in rows:
            print(f"Book name: {row.get('BookName')}, Author: {row.get('AuthorName')}, Shared with: {row.get('ShareWith')}, Is read: {row.get('IsRead')}.")


def updateBook(): # work in progress, currently the entire csv is removed and only the edited book is kept,can't find a solution yet
    book_name = input("Enter book name: ")
    import csv
    rows_list = []
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            rows_list.append(row["BookName"]) # we store every book name in a list
        if book_name not in rows_list: #we search the book the user typed in our list
            add_new_book = input(f' The {book_name} book does not exits. Would you like to add it? (Y/N)? ')
            if add_new_book.upper() == "N":
                return
            else:
                addBook()
                return
        else:
            book_read = input("Is the book read? (Y/N)? ")
            if book_read.upper() == 'Y':
                book_read = True
            else:
                book_read = False
            rows = []
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
        with open('booksDB.csv', mode='w') as file: # WIP, here I can't make the csv keep all books in the list when editing a certain one
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": row.get("SharedWith"),
                                 "IsRead": row.get("IsRead")}
                                )
            # if row["IsRead"] == book_read:
            #     csv_writer.writerow({"BookName": row.get("BookName"),
            #                          "AuthorName": row.get("AuthorName"),
            #                          "SharedWith": row.get("SharedWith"),
            #                          "IsRead": book_read})
            print("Book was updated successfully")





def shareBook(): #share book with smbdy
    book_name = input("What is the name of the book you want to share?  ")
    shared_with = input("With whom do you want to share? : ")# tema faceti lista sa contina mai multe persoane
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["SharedWith"] = shared_with
            else:
                print("The book is not in database")
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": shared_with,
                                 "IsRead": row.get("IsRead")}
                                )
        print(f"Book was successfully shared with {shared_with}")


def mainMenu(): #here we're adding all the options in a list, and attach a variable "index" to them
    # main menu for user
    import time #we use the time module to add a timeout before returning to main menu
    options = ["Add a book", "List books", "Update a book", "Share a book", "Clear the list", "Quit"]
    index = 1
    print("Select an option from the Main menu")
    for option in options:
        print(f"{index}. {option}")
        index += 1

    option = input("Please select an option -> ")

    if option == "1":# starting with this if, we're going to the corresponding function for each attribute
        addBook()
        time.sleep(1.5)
        mainMenu()
    elif option == "2":
        listBooks()
        time.sleep(1.5)
        mainMenu()
    elif option == "3":
        updateBook()
        time.sleep(1.5)
        mainMenu()
    elif option == "4":
        shareBook()
        time.sleep(1.5)
        mainMenu()
    elif option == "5":
        clearCSV()
        time.sleep(1.5)
        mainMenu()
    elif option == "6":
        confirmation = input("Are you sure? (Y/N)? ")
        if confirmation.upper() == "Y":
            print("The app is now closed.")
        else:
            time.sleep(1.5)
            mainMenu()
    else:
        print("Your option is invalid")
        time.sleep(1.5)
        mainMenu()


def clearCSV():
    # writing a function that clears the list, with confirmation
    confirmation = input("Are you sure? (Y/N)? ")
    if confirmation.upper() == "Y":
        file = open('booksDB.csv', "w")
        file.close()
        print('List successfully deleted.')
    else:
        print('Your list is safe. Nothing was removed.')



mainMenu()


