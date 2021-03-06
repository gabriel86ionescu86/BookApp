def addBook():
    import csv
    try:
        with open('booksDB.csv', mode='r', newline='') as readFile:
            rows = csv.DictReader(readFile, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            # we first check to see if header exists
            try:
                test_bytes = readFile.read(1024)
                readFile.seek(0)
                has_header = csv.Sniffer().has_header(test_bytes)
            # treating the exception where the headers don't exist
            except csv.Error:
                with open('booksDB.csv', mode='w') as writeFile:
                    writer = csv.DictWriter(writeFile, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
                    writer.writeheader()
                writeFile.close()
            else:
                print()
        # then we proceed and ask for book name
        book_name = input('Insert book name -> ')
        with open("booksDB.csv", mode = "r") as file: # we open the csv in read mode and check if the book exists exists
            rows = csv.DictReader(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith","IsRead"])
            for row in rows:
                if row.get("BookName") == book_name:  # if the book is found, we ask user to try adding another book
                    try_again = input(f"{book_name} already exists! Try again? (Y/N? ")
                    if try_again.upper() == "Y":
                        addBook()
                        return
                    else:
                        return

        author_name = input('Insert book author -> ')  # if the book is not found, we continue to add it to the list
        with open('booksDB.csv', mode='a', ) as file:  # mode = 'a' appends to the existing list
            writer = csv.DictWriter(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            writer.writerow({'BookName': book_name,
                             'AuthorName': author_name,
                             'BookStartDate': "None",
                             'BookEndDate': "None",
                             'SharedWith': "None",
                             'IsRead': False})
        print('Book was successfully added!')

        other_book = input('Add another book? (Y/N)? ')  # we ask the user if he wants to add another book
        if other_book.upper() == "Y":
            addBook()
        elif other_book.upper() == "N":
            return
    except IOError:
        print("Unable to read the file!")

def listBooks():
    import csv
    import os
    try:
        with open("booksDB.csv", mode="r") as file:
            rows = csv.DictReader(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            for row in rows:
                if row.get("BookName") == "BookName": # skipping the header row when printing data
                    pass
                else:
                    print(f"Book name: {row.get('BookName')}, Author: {row.get('AuthorName')},Start reading date: {row.get('BookStartDate')}, Finish reading date: {row.get('BookEndDate')}, Shared with: {row.get('SharedWith')}, Is read: {row.get('IsRead')}.")
        input("Press any key to continue...")
        os.system('clear')

    except IOError:
        print("Unable to read the file!")

def updateBook():
    book_name = input("Enter book name: ")
    import csv
    rows = []
    rows_list = []
    try:
        with open('booksDB.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                rows_list.append(row["BookName"])  # we store every book name in a list
            if book_name not in rows_list:  # we search the book the user typed in our list
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
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                if row["BookName"] == book_name:
                    row["IsRead"] = book_read
                    break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            csv_writer.writerows(rows)
        print("Book was updated successfully!")
    except IOError:
        print("Unable to read the file!")

def shareBook():  # share book with smbdy
    book_name = input("What is the name of the book you want to share?  ")
    book_found = False
    import csv
    import time  # we use the time module to add a timeout before returning to main menu
    rows = []
    rows_list = []
    shared_with = []
    try:
        with open('booksDB.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                rows_list.append(row["BookName"])  # we store every book name in a list
            if book_name not in rows_list:  # we check to see if book exits in list
                add_new_book = input(f'The {book_name} book does not exits. Would you like to add it? (Y/N)? ')
                if add_new_book.upper() == "N":
                    time.sleep(1.5)
                    mainMenu()
                    return
                else:
                    addBook()
                    return
            for row in rows:  # we check to see if the book was already shared
                if book_name == row["BookName"]:
                    if (row["SharedWith"] != "None"):
                        add_new_book = input(
                            f'The {book_name} book was already shared. Would you like to add more ppl to the list? (Y/N)? ')
                        if add_new_book.upper() == "N":
                            return
                        else:
                            shared_with = input("With whom do you want to share? Please add names followed by comma: ")
                            continue
                    else:
                        shared_with = input("With whom do you want to share? Please add names followed by comma: ")
                        continue

        with open('booksDB.csv', mode='r') as file:  # we add people/ add more people(if already exits) to the shared list of current book
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                if row["BookName"] == book_name:
                    if (row["SharedWith"] != "None"):
                        row["SharedWith"] = row["SharedWith"] + ", " + str(shared_with)
                    else:
                        row["SharedWith"] = shared_with

        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            csv_writer.writerows(rows)

        print(f"Book was successfully shared with {shared_with}!")
    except IOError:
        print("Unable to read the file!")

def bookDate():
    import csv
    import datetime
    start_reading_date = 0
    end_reading_date = 0
    change_start_date = False
    change_end_date = False
    book_name = input("Enter book name: ")
    rows = []
    rows_list = []
    a = ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"]
    try:
        with open('booksDB.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                rows_list.append(row["BookName"])  # we store every book name in a list
            if book_name not in rows_list:  # we search the book the user typed in our list
                add_new_book = input(f'The {book_name} book does not exits. Would you like to add it? (Y/N)? ')
                if add_new_book.upper() == "N":
                    return
                else:
                    addBook()
                    return
            else:
                start_or_end = input(
                    "Would you like to add a start date? (Y/N)? ")  # we ask if user wants to add a start or end date
                if start_or_end.upper() == "N":
                    start_or_end = input("Would you like to add an end date? (Y/N)? ")
                    if start_or_end.upper() == "N":
                        return
                    else:
                        day = int(input('Enter an ending day: (dd): '))
                        month = int(input('Enter an ending month: (mm): '))
                        year = int(input('Enter an ending year: (yyyy): '))
                        end_reading_date = datetime.date(year, month, day)
                        change_end_date = True
                else:
                    day = int(input('Enter the starting day: (dd): '))
                    month = int(input('Enter the starting month: (mm): '))
                    year = int(input('Enter the starting year: (yyyy): '))
                    start_reading_date = datetime.date(year, month, day)
                    change_start_date = True

        with open('booksDB.csv', mode='r') as file:  # we read the csv and replace start/end date variable for certain book accordingly
            rows = list(csv.DictReader(file, fieldnames=(
            "BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead")))
            for row in rows:
                if row["BookName"] == book_name:
                    if change_start_date == True:
                        if (row["BookStartDate"] == "None"):
                            row["BookStartDate"] = start_reading_date
                            print("The start date was changed!")
                        else:
                            print("The start date already exists. Please change end date instead!")
                            return
                    if change_end_date == True:
                        if (row["BookEndDate"] == "None"):
                            row["BookEndDate"] = end_reading_date
                            print('The end date was changed!')
                        else:
                            print("The end date already exists!")
                            return

        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=
            ["BookName", "AuthorName", "BookStartDate", "BookEndDate", "SharedWith", "IsRead"])
            csv_writer.writerows(rows)
        print("Book date was updated successfully!")
    except IOError:
        print("Unable to read the file!")

def mainMenu():  # here we're adding all the options in a list, and attach a variable "index" to them
    # main menu for user
    import time  # we use the time module to add a timeout before returning to main menu
    options = ["Add a book", "List books", "Update read status of a book", "Share a book",
               "Change reading start/end time", "Clear the list", "Quit"]
    index = 1
    print("Select an option from the Main menu")
    for option in options:
        print(f"{index}. {option}")
        index += 1
    try:
        option = int(input("Please select an option -> "))
        if option == 1:  # starting with this if, we're going to the corresponding function for each attribute
            addBook()
            time.sleep(1.5)
            mainMenu()
        elif option == 2:
            listBooks()
            time.sleep(1.5)
            mainMenu()
        elif option == 3:
            updateBook()
            time.sleep(1.5)
            mainMenu()
        elif option == 4:
            shareBook()
            time.sleep(1.5)
            mainMenu()
        elif option == 5:
            bookDate()
            time.sleep(1.5)
            mainMenu()
        elif option == 6:
            clearCSV()
            time.sleep(1.5)
            mainMenu()
        elif option == 7:
            confirmation = input("Are you sure? (Y/N)? ")
            if confirmation.upper() == "Y":
                print("The app is now closed.")
            else:
                time.sleep(1.5)
                mainMenu()
        else:
            print("Your option is invalid, please try again!")
            time.sleep(1.5)
            mainMenu()

    except ValueError:
        print("Your option is invalid, please try again!")
        time.sleep(1.5)
        mainMenu()


def clearCSV():
    # writing a function that clears the list, with confirmation
    confirmation = input("Clear list. Are you sure? (Y/N)? ")
    if confirmation.upper() == "Y":
        try:
            file = open('booksDB.csv', "w")
            file.close()
            print('List successfully deleted!')
        except IOError:
            print("Unable to read the file!")
    else:
        print('Your list is safe. Nothing was removed.')


mainMenu()













