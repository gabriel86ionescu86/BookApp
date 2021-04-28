def addBook():
    import csv
    book_name = input('Insert book name ->')
    #after getting the book name, we read the csv and compare with the 'BookName' value
    with open("booksDB.csv", mode="r") as file:
        rows = csv.DictReader(file, fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        for row in rows:
            if row.get('BookName') == book_name:
                print("The book is already in the list!") #if the same value is found for bookname, we edit to line 23
                break
            else:
                author_name = input('Insert book author ->')
                with open('booksDB.csv', mode='a', ) as file:  # mode = 'a' appends to the existing list
                    writer = csv.DictWriter(file, fieldnames=[
                        'BookName', 'AuthorName', 'SharedWith', 'IsRead'
                    ])
                    writer.writerow({'BookName': book_name,
                                     'AuthorName': author_name,
                                     'SharedWith': "None",
                                     'IsRead': False})
                print('Book was successfully added')
                break
    other_book = input('Add another book? Y/N ') #we ask the user if he wants to add another book
    while other_book == 'Y':
        addBook() #here we're going again through the compare and add features
        return


def listBooks():
    import csv
    with open("booksDB.csv", mode = "r") as file:
        rows = csv.DictReader(file,fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        for row in rows:
            print(f"Book name: {row.get('BookName')}, Author: {row.get('AuthorName')}, Shared with: {row.get('ShareWith')}, Is read: {row.get('IsRead',False)}.")


def updateBook(): # didn't touch this function yet
    book_name = input("Enter book name: ")
    book_read = input("Is the book read? (Y/N)? ")
    if book_read == "Y":
        book_read = True
    else:
        book_read = False
    rows = []
    import csv
    with open("booksDB.csv", mode = "a") as file:
        rows = csv.DictReader(file,fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        for row in rows:
            if book_name == row.get("BookName"):
                row["IsRead"] = book_read
                csv_writer = csv.DictWriter(file, fieldnames=[
                    "BookName", "AuthorName", "SharedWith", "IsRead"
                ])
                csv_writer.writerow(rows)
                break

        print("Book was updated successfully!")


def shareBook(): # didn't touch this function yet
    print("Share a book option")


def mainMenu(): #here we're adding all the options in a list, and attach avaraible "index" to them
    # main menu for user
    options = ["Add a book", "List books", "Update a book", "Share a book", "Clear the list", "Quit"]
    index = 1
    print("Select an option from the Main menu")
    for option in options:
        print(f"{index}. {option}")
        index += 1

    option = input("Please select an option -> ")

    if option == "1":# starting with this if, we're going to the corresponding function for each attribute
        addBook()
        quitQuestioning() #here we're calling a function written below that asks user if he want's to exits the program or not
    elif option == "2":
        listBooks()
        quitQuestioning()
    elif option == "3":
        updateBook()
        quitQuestioning()
    elif option == "4":
        shareBook()
        quitQuestioning()
    elif option == "5":
        clearCSV()
        quitQuestioning()
    elif option == "6":
        print("The app is now closed.")
    else:
        print("Your option is invalid")
        quitQuestioning()


def clearCSV():
    # writing a function that clears the list, with confirmation
    confirmation = input("Are you sure? Y/N ")
    if confirmation == "Y":
        file = open('booksDB.csv', "w")
        file.close()
        print('List succesfully deleted.')
    else:
        print('Your list is safe. Nothing was removed.')


def quitQuestioning():
    # a function that asks the user if he wants to quit or not after he's done with each option from the menu
    quit = input("Would you like to quit the app? Y/N ")
    while quit == 'N':
        mainMenu()
        return
    print("The app is now closed.")


mainMenu()


